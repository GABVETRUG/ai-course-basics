# Novità PL/SQL in Oracle AI Database 26ai, fino alla 23.26.4

Nella 23.26.4 il linguaggio PL/SQL non cambia: le note ufficiali consultate a fine ottobre 2026 non elencano
modifiche alla PL/SQL Language Reference per questa release update. Le novità che toccano chi scrive PL/SQL sono
quelle SQL della 23.26.4; le novità del linguaggio sono arrivate con le release update 23.26.x precedenti e con la 23ai.

Tutti gli esempi marcati **verificato** sono stati eseguiti su Oracle AI Database 26ai Free 23.26.3 con lo schema HR.
Gli script sono in `verifiche/plsql/`.

## Cosa porta la 23.26.4 a chi scrive PL/SQL

- **`CREATE MACRO`**: per una SQL macro non serve più una funzione PL/SQL che restituisce il testo SQL in una
  stringa. La documentazione (Database Reference, modifiche della 23.26.4) aggiunge le viste `ALL_MACRO_PARAMETERS`,
  `DBA_MACRO_PARAMETERS` e `USER_MACRO_PARAMETERS`; su 23.26.3 `USER_MACRO_PARAMETERS` non esiste (ORA-00942).
- **Macro nella clausola `WITH`**: fino alla 23.26.3 una macro chiamata dentro una CTE dava ORA-64630.
  Dettagli e casi limite nelle slide `slide-macro-with/`.
- **`FETCH FIRST … FOR UPDATE SKIP LOCKED`**: il cursore di un processo che preleva lavori da una tabella diventa una
  sola query.

  ```sql
  declare
    cursor c_lotto is
      select job_id, payload
      from   jobs
      where  stato = 'NUOVO'
      order  by creato_il, job_id
      fetch  first 5 rows only
      for    update skip locked;
  begin
    for j in c_lotto loop
      update jobs set stato = 'FATTO', finito_il = systimestamp where job_id = j.job_id;
    end loop;
    commit;
  end;
  /
  ```

  Fino alla 23.26.3 la stessa query dava ORA-02014 e serviva un cursore `FOR UPDATE SKIP LOCKED` letto con
  `BULK COLLECT … LIMIT` (verificato: con `SKIP LOCKED` il lock avviene al `FETCH`, quindi si bloccano solo le righe
  lette).
- **`UUID(7)` e `UUID(5, …)`**: su 23.26.3 `UUID` e `RAW_TO_UUID` non si possono chiamare come funzioni PL/SQL
  (PLS-00201, verificato). Si usano dentro un'istruzione SQL:

  ```sql
  select raw_to_uuid(uuid()) into l_id;
  ```

  Sulla 23.26.4 è da verificare.

## Novità delle release update 23.26.x

### `RESETTABLE` (23.26.0)

Evita l'errore ORA-04068 quando un package viene ricompilato mentre altre sessioni lo stanno usando, tipico durante un
rilascio o l'applicazione di una patch.

```sql
create or replace package pkg_contatore resettable is
  contatore number := 0;
  procedure incrementa;
end;
/
create or replace package body pkg_contatore resettable is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('contatore = ' || contatore);
  end;
end;
/
```

Verificato con due sessioni: la sessione B chiama il package due volte, la sessione A ricompila il package body, la
sessione B lo richiama.

| Caso | Dopo la ricompilazione |
| --- | --- |
| Package senza `RESETTABLE`, variabile nella specifica, ricompilato il body | ORA-04068, ORA-04061, ORA-04065. La sessione perde le variabili di **tutti** i package, compreso `DBMS_OUTPUT`: l'output non compare più finché non si rilancia `set serveroutput on`. La chiamata successiva riparte da 1. |
| `RESETTABLE`, variabile nella specifica, ricompilato solo il body | Nessun errore, gira il nuovo body e il contatore continua: 3, 4. |
| `RESETTABLE`, variabile nel body, ricompilato il body | Nessun errore, il contatore riparte da 1. |
| `RESETTABLE`, variabile nella specifica, ricompilata la specifica | Nessun errore, il contatore riparte da 1. |

I valori delle variabili si perdono comunque quando l'unità che li contiene viene ricompilata: `RESETTABLE` è adatto a
package con dati ricostruibili, come cache e contatori.

Script: `verifiche/plsql/resettable/`.

### `WAIT` e `NOWAIT` nelle DML (23.26.2)

Prima esistevano solo per `SELECT … FOR UPDATE` e `LOCK TABLE`; ora valgono anche per `INSERT`, `UPDATE`,
`DELETE` e `MERGE`.

```sql
declare
  e_riga_occupata exception;
  pragma exception_init(e_riga_occupata, -54);
begin
  update hr.employees set salary = salary + 1
  where  employee_id = 100
  wait 3;
exception
  when e_riga_occupata then
    dbms_output.put_line('Riga occupata da un''altra sessione');
end;
/
```

Verificato con la riga 100 bloccata da un'altra sessione: `nowait` dà ORA-00054 subito, `wait 3` dopo 3 secondi; sulle
righe libere l'aggiornamento procede normalmente. Script: `verifiche/plsql/dml_nowait/`.

## Dalla 23ai, ancora poco conosciute

Tutte verificate su 23.26.3 (`verifiche/plsql/01_case_ifexists_boolean.sql` e `02_transpiler_json_vector.sql`).

### Funzioni BOOLEAN usabili in SQL

```sql
create or replace function guadagna_molto(p_sal number) return boolean is
begin
  return p_sal > 15000;
end;
/
select last_name, salary, guadagna_molto(salary) molto
from   hr.employees
where  guadagna_molto(salary);
```

Restituisce King, Garcia e Yang con `MOLTO = TRUE`: la funzione si usa direttamente come condizione.

### CASE con liste di valori e confronti parziali

```sql
case n
  when < 0 then dbms_output.put_line('negativo');
  when 0 then dbms_output.put_line('zero');
  when 1, 3, 5, 7, 9 then dbms_output.put_line('dispari sotto 10');
  when between 10 and 99 then dbms_output.put_line('due cifre');
  when is null then dbms_output.put_line('null');
  else dbms_output.put_line('altro');
end case;
```

Funziona anche nelle espressioni: `case i when 1, 2 then 'basso' when > 3 then 'alto' else 'medio' end`.

### `IF [NOT] EXISTS` anche per procedure e package

- `create procedure if not exists p_demo …` non sovrascrive una procedura che esiste già: l'istruzione riesce ma il
  sorgente resta quello di prima.
- `drop procedure if exists p_demo` non dà errore se la procedura non c'è.
- `create or replace procedure if not exists …` dà ORA-11541: le due clausole non si combinano.

### JSON e record PL/SQL

```sql
declare
  r hr.employees%rowtype;
  j json;
  s varchar2(4000);
begin
  select * into r from hr.employees where employee_id = 100;
  j := json(r);
  select json_serialize(j) into s;
  dbms_output.put_line(s);
end;
/
```

Produce il JSON della riga, con le chiavi non necessariamente nell'ordine delle colonne
(`{"PHONE_NUMBER":"1.515.555.0100","JOB_ID":"AD_PRES","SALARY":24000,…}`). Nel verso opposto
`json_value(doc, '$' returning t_emp)` riempie un record PL/SQL.

### Conversione automatica da PL/SQL a SQL

```sql
alter session set sql_transpiler = 'ON';
```

Con il parametro attivo (su 23.26.3 è `OFF` di default) Oracle sostituisce una funzione PL/SQL semplice con la sua
espressione. Nel piano `annuale(salary, commission_pct) > 200000` diventa
`"SALARY"*12*(1+NVL("COMMISSION_PCT",0))>200000`: niente passaggio da SQL a PL/SQL a ogni riga.

### `RETURNING OLD` e `NEW`

```sql
update hr.employees set salary = salary * 1.1
where  employee_id = 100
returning old salary, new salary into l_old, l_new;
```

Restituisce 24000 e 26400.

### Tipo `VECTOR` in PL/SQL

```sql
declare
  v1 vector := to_vector('[1, 2, 3]');
  v2 vector := to_vector('[2, 2, 3]');
begin
  dbms_output.put_line(vector_distance(v1, v2, euclidean));
end;
/
```

### `DBMS_DEVELOPER.GET_METADATA`

```sql
select json_serialize(dbms_developer.get_metadata(name => 'REGIONS', schema => 'HR', level => 'BASIC') pretty);
```

Restituisce la struttura della tabella come JSON (colonne, tipi, obbligatorietà).

## Package nuovi o aggiornati

Dalla documentazione, non provati: `DBMS_VECTOR`, `DBMS_VECTOR_CHAIN`, `DBMS_HYBRID_VECTOR`, `DBMS_DICTIONARY_CHECK`;
`DBMS_CRYPTO` con SHA-3, SM2, SM3, SM4 ed ECDH; `DBMS_SQL_FIREWALL.APPEND_ALLOW_LIST_SINGLE_SQL`; digest SHA-256 in
`UTL_HTTP`.

## Fonti

- [PL/SQL Language Reference 26 – Changes in This Release](https://docs.oracle.com/en/database/oracle/oracle-database/26/lnpls/release-changes.html)
- [RESETTABLE Clause](https://docs.oracle.com/en/database/oracle/oracle-database/26/lnpls/RESETTABLE-clause.html)
- [ORACLE-BASE – RESETTABLE Clause in Oracle AI Database 26ai](https://oracle-base.com/articles/26/resettable-clause-26)
- [Database Reference 26 – Changes in This Release](https://docs.oracle.com/en/database/oracle/oracle-database/26/refrn/changes-this-release-oracle-database-reference.html)
- [All Things SQL – How to stop updates from hanging forever with [no]wait](https://blogs.oracle.com/sql/how-to-stop-updates-from-hanging-forever-with-nowait-in-oracle-ai-database)
- [PL/SQL Packages and Types Reference 26 – Changes in This Release](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/release-changes.html)
- [Security Guide 26 – Changes in This Release](https://docs.oracle.com/en/database/oracle/oracle-database/26/dbseg/release-changes.html)
- [ORACLE-BASE – SQL and PL/SQL Enhancements in 23ai/26ai](https://oracle-base.com/articles/23/sql-and-plsql-enhancements-23)
