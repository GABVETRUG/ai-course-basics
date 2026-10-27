# Oracle AI Database 23.26.4: novità SQL e PL/SQL

Materiale nato dal post LinkedIn di Chris Saxon «Oracle AI Database 23.26.4 is here!» (ottobre 2026) e dalle slide
che lo accompagnano: le novità SQL della release update 23.26.4 spiegate con esempi, il confronto con la release
precedente e le novità PL/SQL della serie 26ai.

Questa cartella è indipendente dal resto del repository (il corso AI Basics).

## Contenuto

| Percorso | Contenuto |
| --- | --- |
| `approfondimento/novita-sql-23-26-4.html` | La pagina completa sulle sei novità SQL (`SELECT *, espr`, `FETCH FIRST … FOR UPDATE`, UUID v5 e v7, `BAR_CHART`, `CREATE MACRO`, `TUMBLE`/`HOP`/`CUMULATE`/`SESSIONS`): cosa fanno, come si ottenevano prima, esempi con l'output, diagrammi ed errori da evitare. Si apre direttamente nel browser. |
| `approfondimento/build/` | I sorgenti della pagina: `python3 build.py` la rigenera, solo con la libreria standard. |
| `lab/novita_23_26_4.sql` | Tutti gli esempi con la sintassi della 23.26.4. |
| `lab/equivalenti_fino_23_26_3.sql` | Gli stessi esempi per le release precedenti. Gira su 23.26.3; le istruzioni che falliscono di proposito sono marcate «ERRORE ATTESO». |
| `slide-macro-with/` | Sorgenti delle 9 slide «Macro SQL e clausola WITH», nel formato del tipo Slides degli artifact di Claude: `deck.json` e una pagina HTML per slide. |
| `note-plsql.md` | Le novità PL/SQL della serie 26ai fino alla 23.26.4, con esempi verificati. |
| `verifiche/` | Gli script usati per le verifiche e le istruzioni per rieseguirli. |

## Versioni pubblicate

Link privati, visibili solo al proprietario finché non vengono condivisi:

- pagina: <https://claude.ai/artifact/MzJEajgpX7r8ZttQt38miF>
- slide: <https://claude.ai/artifact/7QKgPK1f4RbsVmE7c1g3gh>, scaricabili in PowerPoint o PDF

## Come è stato verificato

La 23.26.4 non era disponibile. Le prove sono state fatte su Oracle AI Database 26ai Free 23.26.3.0.0 (immagine
`gvenzl/oracle-free:23.26.3-slim-faststart`) con lo schema HR ufficiale, lo stesso delle slide: 107 dipendenti assunti
tra il 2011 e il 2018.

- Il comportamento della 23.26.3, con errori e soluzioni tradizionali, è stato eseguito.
- I risultati delle slide di Oracle sono stati ricostruiti con SQL classico e coincidono tutti, comprese le finestre di
  `TUMBLE`, `HOP`, `CUMULATE` e `SESSIONS` e i cinque UUID v5, identici a quelli di Python
  `uuid.uuid5(uuid.NAMESPACE_URL, …)`.
- Gli output delle funzioni nuove che non compaiono nelle slide sono calcolati con query equivalenti e indicati come
  attesi.

## Risultati principali

- **`SELECT *, espr`**: fino alla 23.26.3 dava ORA-00936 o ORA-00923. Con nomi di colonna duplicati una subquery dà
  ORA-00918 e una `CREATE TABLE … AS SELECT` dà ORA-00957.
- **`FETCH FIRST … FOR UPDATE SKIP LOCKED`**: fino alla 23.26.3 dava ORA-02014. Le soluzioni con `ROWNUM` o con una
  subquery restituiscono meno righe del richiesto quando qualcuna è bloccata; quella corretta era un cursore PL/SQL con
  `BULK COLLECT … LIMIT`.
- **UUID**: la v7 è ordinata al millisecondo, ma dentro lo stesso millisecondo l'ordine è casuale. Sull'indice di
  chiave primaria, fino a 2 righe/ms i blocchi restano pieni al 100%; da 5 righe/ms scendono al 51%, peggio della v4
  (69%). Con `INSERT /*+ APPEND */` tornano al 100%.
- **`CREATE MACRO`**: con la forma PL/SQL un errore di sintassi emerge solo all'uso (ORA-64626), e un parametro con il
  nome di una colonna dà risultati sbagliati (106 righe invece di 45).
- **Macro e `WITH`**: fino alla 23.26.3 era vietata solo la chiamata della macro dentro una CTE (ORA-64630). Macro
  nella query principale, CTE passate come tabella e inline view funzionavano già.
- **Finestre temporali**: partono da istanti fissi e la fine è esclusa. `HOP` conta ogni riga in più finestre: nella
  slide la somma dei conteggi è 428 = 4 × 107.
- **PL/SQL**: la 23.26.4 non cambia il linguaggio. Le novità della serie sono `RESETTABLE` (23.26.0), `WAIT`/`NOWAIT`
  nelle DML (23.26.2) e le funzionalità 23ai descritte in `note-plsql.md`.

## Da verificare sulla 23.26.4

1. `DEFAULT uuid(7)`: su 23.26.3 la clausola `DEFAULT` accetta `uuid()` ma rifiuta `uuid(4)` (ORA-00907).
2. `PARTITION BY` dentro `SESSIONS`, per avere sessioni separate per utente o negozio.
3. `DROP MACRO`: usato negli script di pulizia, ma non documentato nelle fonti consultate.
4. Una macro con la `WITH` nel corpo e il parametro usato dentro la `WITH` (ORA-00904 su 23.26.3).
5. Le macro definite con `WITH FUNCTION` e usate dentro una CTE (ORA-64630 su 23.26.3).
6. `UUID` e `RAW_TO_UUID` chiamati direttamente da PL/SQL (PLS-00201 su 23.26.3).
7. La misura sugli indici con il vero `UUID(7)` al posto dell'emulazione (`verifiche/uuid_indice/`).
8. Il disegno esatto delle frazioni di `BAR_CHART`, per esempio 17.000 su 24.000 con larghezza 10.

## Rigenerare la pagina

```bash
cd approfondimento/build
python3 build.py              # ../novita-sql-23-26-4.html, documento HTML completo
python3 build.py --artifact   # stessa pagina senza <html>/<head>/<body>, per ripubblicarla come artifact
```

## Fonti

- Chris Saxon, post LinkedIn «Oracle AI Database 23.26.4 is here!» e slide allegate, ottobre 2026
- [Oracle AI Database 26ai New Features – SQL](https://docs.oracle.com/en/database/oracle/oracle-database/26/nfcoa/appdev_sql.html)
- [SQL Language Reference 26 – SELECT](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/SELECT.html)
- [SQL Language Reference 26 – UUID](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/uuid.html)
- [SQL Language Reference 26 – TIME_BUCKET](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/time_bucket-datetime.html)
- [All Things SQL – How to create views with parameters in Oracle AI Database](https://blogs.oracle.com/sql/how-to-create-views-with-parameters-in-oracle-ai-database)
- [Apache Flink – Windowing table-valued functions](https://nightlies.apache.org/flink/flink-docs-stable/docs/sql/reference/queries/window-tvf/)
- [RFC 9562 – Universally Unique IDentifiers](https://www.rfc-editor.org/rfc/rfc9562)
- Le fonti PL/SQL sono elencate in `note-plsql.md`.
