# Verifiche

Gli script usati per verificare il materiale di questa cartella. Girano su Oracle AI Database 26ai Free **23.26.3**,
la release precedente alla 23.26.4, con lo schema HR ufficiale. Sulla 23.26.4 servono per rifare le prove con le
funzioni nuove e chiudere i punti aperti elencati nel README principale.

## Preparare il database

1. Avvia Oracle Database Free in un container:

   ```bash
   docker run -d --name ora -p 1521:1521 \
     -e ORACLE_PASSWORD=<password_sys> \
     -e APP_USER=hr -e APP_USER_PASSWORD=<password_hr> \
     gvenzl/oracle-free:23.26.3-slim-faststart
   ```

   - Se Docker Hub risponde 429 (troppe richieste), la stessa immagine è su `mirror.gcr.io/gvenzl/oracle-free`.
   - Se all'avvio il log mostra `ORA-00600 [ksipc: no private ips avail for use]`, il container non ha una rete
     utilizzabile: usa `--network host` al posto di `-p 1521:1521`.
   - Per la 23.26.4 usa il tag corrispondente quando sarà pubblicato (a fine ottobre 2026 l'ultimo era 23.26.3).

2. Installa lo schema HR con gli script ufficiali di
   [oracle-samples/db-sample-schemas](https://github.com/oracle-samples/db-sample-schemas), cartella
   `human_resources`, eseguiti come utente HR:

   ```bash
   for f in hr_create.sql hr_populate.sql hr_code.sql; do
     curl -sSLO "https://raw.githubusercontent.com/oracle-samples/db-sample-schemas/main/human_resources/$f"
     docker cp "$f" "ora:/tmp/$f"
   done
   docker exec -i ora bash -c 'cd /tmp && sqlplus -s hr/<password_hr>@localhost/FREEPDB1' <<'EOF'
   @hr_create.sql
   @hr_populate.sql
   @hr_code.sql
   EOF
   ```

3. Solo per le misure sugli indici (`uuid_indice/`), come SYSDBA:

   ```sql
   alter session set container = FREEPDB1;
   grant select on v_$mystat to hr;
   grant select on v_$statname to hr;
   grant create table to hr;
   ```

## Eseguire gli script

```bash
export CONN=hr/<password_hr>@localhost/FREEPDB1
./esegui.sh plsql/01_case_ifexists_boolean.sql
./esegui_due_sessioni.sh plsql/dml_nowait/sessione1_blocca_100.sql plsql/dml_nowait/sessione2_nowait_wait.sql
```

`esegui_due_sessioni.sh` avvia il primo script subito e il secondo dopo 3 secondi (terzo parametro facoltativo),
poi stampa l'output di entrambi. Serve per i test con i lock e con la ricompilazione dei package. Il nome del
container si cambia con `CONTAINER` (predefinito `ora`).

## Cosa verifica ogni script

| Script | Come si lancia | Risultato su 23.26.3 |
| --- | --- | --- |
| `01_prima_della_23_26_4.sql` | `esegui.sh` | Le nuove sintassi falliscono: ORA-00936 e ORA-00923 (`SELECT *, espr`), ORA-02014 (`FETCH FIRST … FOR UPDATE`), ORA-62433 e ORA-00939 (`UUID(7)`, `UUID(5, …)`), ORA-00904 (`BAR_CHART`, `TUMBLE`), ORA-00922 (`CREATE MACRO`). `GROUP BY ALL`, `TIME_BUCKET` e `SELECT` senza `FROM` funzionano già. |
| `for_update/` | `esegui_due_sessioni.sh for_update/sessione1_blocca_100.sql for_update/sessione2_workaround.sql` | Con il dipendente 100 bloccato, `ROWNUM` e la subquery restituiscono 2 righe su 3; il cursore con `BULK COLLECT … LIMIT 3` restituisce 101, 102, 103 e blocca solo quelle; senza `SKIP LOCKED` il cursore blocca tutte le righe già all'`OPEN`. La sessione 1 tiene il lock per 40 secondi. |
| `uuid_indice/01_tempo_reale.sql` | `esegui.sh` | 200.000 inserimenti riga per riga: foglie e riempimento dell'indice con UUID v4, v7 emulato e `IDENTITY` (nelle prove: 985 e 69%, 1270 e 54%, 374 e 100%; i valori variano con la velocità della macchina). |
| `uuid_indice/02_righe_per_ms.sql` | `esegui.sh` | v7 emulato a 1, 2, 5, 25 e 100 righe per millisecondo: riempimento 100%, 100%, 59%, 51%, 51%. |
| `uuid_indice/03_direct_path.sql` | `esegui.sh`, dopo `02` | Stesso carico a 100 righe/ms: 51% con `INSERT` convenzionale, 100% con `INSERT /*+ APPEND */`. |
| `macro_with/01_dove_si_puo_chiamare.sql` | `esegui.sh` | Macro di tabella e scalare dentro una CTE: ORA-64630. Macro nella query principale di una `WITH`, CTE passata a una macro polimorfica, macro in una inline view: funzionano. |
| `macro_with/02_with_nel_corpo_e_with_function.sql` | `esegui.sh`, dopo `01` | `WITH` nel corpo della macro: funziona se il parametro è fuori dalla `WITH`, ORA-00904 se è dentro. `WITH FUNCTION … SQL_MACRO`: funziona nella query principale, ORA-64630 dentro una CTE. `WITH` annidate: funzionano. |
| `macro_with/03_workaround_e_risultati.sql` | `esegui.sh`, dopo `01` | Soluzione con inline view (reparto 50: 45, reparto 60: 5) e i risultati usati nelle slide. |
| `plsql/01_case_ifexists_boolean.sql` | `esegui.sh` | CASE con liste e confronti parziali; `IF [NOT] EXISTS` (ORA-11541 con `OR REPLACE`); funzione BOOLEAN usata in SQL; sintassi `WAIT`/`NOWAIT` nelle DML; `USER_MACRO_PARAMETERS` non esiste ancora. |
| `plsql/02_transpiler_json_vector.sql` | `esegui.sh` | Transpiler (predicato riscritto nel piano), JSON da un record, `JSON_VALUE` in un record, `VECTOR`, `RETURNING OLD/NEW`, `DBMS_DEVELOPER.GET_METADATA`. |
| `plsql/resettable/01_*` | `esegui.sh plsql/resettable/01_setup_spec_state.sql`, poi `esegui_due_sessioni.sh plsql/resettable/01_sessione_b_usa.sql plsql/resettable/01_sessione_a_ricompila.sql` | Package normale: ORA-04068. Package `RESETTABLE`: nessun errore, il contatore continua (3, 4). |
| `plsql/resettable/02_*` | `esegui.sh plsql/resettable/02_setup_body_e_spec.sql`, poi `esegui_due_sessioni.sh plsql/resettable/02_sessione_b_usa.sql plsql/resettable/02_sessione_a_ricompila.sql` | `RESETTABLE` con le variabili nel body o nella specifica ricompilati: nessun errore, il contatore riparte da 1. |
| `plsql/dml_nowait/` | `esegui_due_sessioni.sh plsql/dml_nowait/sessione1_blocca_100.sql plsql/dml_nowait/sessione2_nowait_wait.sql` | `NOWAIT`: ORA-00054 subito. `WAIT 3`: ORA-00054 dopo 3 secondi. In PL/SQL l'errore arriva come `SQLCODE` -54. |

Alla prima esecuzione alcuni script segnalano ORA-00942 sui `DROP` iniziali: è normale, gli oggetti non esistono
ancora.
