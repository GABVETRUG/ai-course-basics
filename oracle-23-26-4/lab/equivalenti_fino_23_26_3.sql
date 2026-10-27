-- =====================================================================
--  Come si ottiene, fino alla 23.26.3, quello che la 23.26.4 fa in modo
--  nativo. Script verificato su Oracle AI Database 26ai Free 23.26.3
--  con lo schema HR ufficiale (github.com/oracle-samples/db-sample-schemas).
--
--  Le istruzioni marcate "ERRORE ATTESO" mostrano il limite della release:
--  falliscono di proposito.
--  Le parti "DUE SESSIONI" vanno eseguite a mano in due finestre.
-- =====================================================================
set linesize 200 pagesize 100 serveroutput on
alter session set nls_date_format = 'DD-MON-YYYY';
alter session set nls_timestamp_format = 'DD-MON-YYYY HH24:MI';


-- ---------------------------------------------------------------------
-- 1. SELECT * insieme ad altre espressioni
-- ---------------------------------------------------------------------
-- ERRORE ATTESO: ORA-00936: missing expression
select rowid, upper(region_name) upper_name, * from hr.regions;

-- ERRORE ATTESO: ORA-00923: FROM keyword not found where expected
select *, upper(region_name) from hr.regions;

-- Soluzione classica: alias di tabella e asterisco qualificato
select rowid, upper(region_name) upper_name, r.* from hr.regions r;

-- Top-2 stipendi per reparto
select e.*, row_number() over (partition by department_id order by salary desc) rn
from   hr.employees e
where  department_id in (20, 30)
qualify rn <= 2
order  by department_id, rn;

-- Pagina di risultati con il totale delle righe
select j.*, count(*) over () totale_righe
from   hr.jobs j
order  by job_id
fetch  first 3 rows only;

-- Nomi di colonna duplicati
-- ERRORE ATTESO: ORA-00918: column ambiguously specified
select salary from (select e.*, salary * 12 salary from hr.employees e);
-- ERRORE ATTESO: ORA-00957: duplicate column name
create table emp_copy as select e.*, salary * 12 salary from hr.employees e;

-- Colonne invisibili
create table clienti_demo (id number, nome varchar2(30), nota varchar2(30) invisible);
insert into clienti_demo (id, nome, nota) values (1, 'Rossi', 'nascosta');
-- restituisce ID, NOME
select * from clienti_demo;
-- restituisce ID, NOME, NOTA
select c.*, nota from clienti_demo c;
drop table clienti_demo purge;


-- ---------------------------------------------------------------------
-- 2. Top-N con FOR UPDATE [SKIP LOCKED]
-- ---------------------------------------------------------------------
-- ERRORE ATTESO: ORA-02014: cannot select FOR UPDATE from view with DISTINCT, GROUP BY, etc.
select employee_id from hr.employees
order  by employee_id
fetch  first 3 rows only
for    update skip locked;

-- Perche': FETCH FIRST viene riscritto come vista interna
variable testo clob
set long 4000
exec dbms_utility.expand_sql_text('select employee_id from hr.employees order by employee_id fetch first 3 rows only', :testo)
print testo

-- Funzione di supporto: dice se una riga e' bloccata da un'altra transazione
create or replace function is_locked ( p_id number ) return varchar2 is
  pragma autonomous_transaction;
  l_id number;
begin
  select employee_id into l_id from hr.employees where employee_id = p_id for update nowait;
  rollback;
  return 'libera';
exception
  when others then
    rollback;
    return case when sqlcode = -54 then 'BLOCCATA' else sqlerrm end;
end;
/

-- DUE SESSIONI ---------------------------------------------------------
-- Sessione 1 (lasciarla aperta, senza COMMIT):
--   update hr.employees set hire_date = sysdate where employee_id = 100;
--
-- Sessione 2, workaround con ROWNUM: restituisce 101, 102 (solo 2 righe)
--   select employee_id from hr.employees where rownum <= 3 for update skip locked;
--   rollback;
--
-- Sessione 2, workaround con subquery: restituisce 101, 102 (solo 2 righe)
--   select employee_id from hr.employees
--   where  employee_id in (select employee_id from hr.employees
--                          order by employee_id fetch first 3 rows only)
--   for update skip locked;
--   rollback;
--
-- Sessione 2, workaround corretto: il blocco PL/SQL qui sotto
-- (restituisce 101, 102, 103 e blocca solo quelle tre righe)
-- ---------------------------------------------------------------------
declare
  cursor c is
    select employee_id from hr.employees
    order  by employee_id
    for    update skip locked;
  type t_ids is table of hr.employees.employee_id%type;
  l_ids t_ids;
begin
  open c;
  fetch c bulk collect into l_ids limit 3;   -- con SKIP LOCKED il lock avviene al FETCH
  for i in 1 .. l_ids.count loop
    dbms_output.put_line('preso: ' || l_ids(i));
  end loop;
  dbms_output.put_line('104 -> ' || is_locked(104) || ' | 150 -> ' || is_locked(150));
  close c;
  rollback;
end;
/

-- Senza SKIP LOCKED un cursore FOR UPDATE blocca tutte le righe gia' all'OPEN
declare
  cursor c is
    select employee_id from hr.employees
    where  employee_id between 101 and 110
    order  by employee_id
    for    update;
begin
  open c;
  dbms_output.put_line('dopo OPEN: 104 -> ' || is_locked(104) || ' | 110 -> ' || is_locked(110));
  close c;
  rollback;
end;
/


-- ---------------------------------------------------------------------
-- 3. UUID
-- ---------------------------------------------------------------------
select uuid() v4, raw_to_uuid(uuid()) v4_testo;

-- ERRORE ATTESO: ORA-62433: Invalid or unsupported argument to UUID function
select uuid(7);
-- ERRORE ATTESO: ORA-00939: too many arguments for function
select uuid(5, 'url', 'test.com/1');
-- IS_UUID riconosce solo la versione 4: FALSE
select is_uuid('7a6fab4a-ad8d-580d-b94d-c96326ecafd3') v5_valido;
-- ERRORE ATTESO: ORA-62432: ... is not a valid UUID value
select uuid_to_raw('7a6fab4a-ad8d-580d-b94d-c96326ecafd3');

-- UUID v5 calcolato a mano (RFC 9562): stessi valori della slide
select level n,
       utl_raw.bit_or(
         utl_raw.bit_and(
           utl_raw.substr(
             standard_hash(utl_raw.concat(hextoraw('6BA7B8119DAD11D180B400C04FD430C8'),   -- namespace URL
                                          utl_raw.cast_to_raw('test.com/' || level)), 'SHA1'), 1, 16),
           hextoraw('FFFFFFFFFFFF0FFF3FFFFFFFFFFFFFFF')),      -- azzera versione e variante
         hextoraw('00000000000050008000000000000000')) uuid_v5  -- versione 5, variante RFC
connect by level <= 5;

-- Istante di creazione di un UUID v7 (valore preso dalla slide)
with u as (select hextoraw('01A0E8E0EAF77905AC36727337DF0863') id)
select regexp_replace(lower(rawtohex(id)), '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5') uuid_testo,
       substr(rawtohex(id), 13, 1) versione,
       timestamp '1970-01-01 00:00:00 UTC'
         + numtodsinterval(to_number(substr(rawtohex(id), 1, 12), 'XXXXXXXXXXXX') / 1000, 'SECOND') creato_utc
from   u;

-- DEFAULT UUID() come chiave primaria
create table ordini_demo (id raw(16) default uuid() primary key, cliente varchar2(30));
insert into ordini_demo (cliente) values ('ACME');
select raw_to_uuid(id) id, cliente from ordini_demo;
drop table ordini_demo purge;

-- Nella clausola DEFAULT la versione non si puo' indicare
-- ERRORE ATTESO: ORA-00907: missing right parenthesis
create table ordini_demo (id raw(16) default uuid(4) primary key, cliente varchar2(30));

-- In PL/SQL UUID e RAW_TO_UUID non sono richiamabili direttamente
-- (PLS-00201): si passa da un'istruzione SQL
declare
  l_id varchar2(36);
begin
  select raw_to_uuid(uuid()) into l_id;
  dbms_output.put_line(l_id);
end;
/


-- ---------------------------------------------------------------------
-- 4. BAR_CHART emulato
--    bar_chart(val, max, min, larghezza, '#')  ~  rpad + round
--    bar_chart(val, max, min, larghezza)       ~  blocchi Unicode a ottavi
-- ---------------------------------------------------------------------
select salary,
       rpad('#', round((salary - 0) / (24000 - 0) * 20), '#') max_24000_20_chars
from   hr.employees
where  employee_id between 100 and 106
order  by salary desc;

with d as (
  select salary, least(greatest((salary - 0) / (24000 - 0), 0), 1) * 10 x
  from   hr.employees
  where  employee_id between 100 and 106
)
select salary,
       replace(rpad(' ', trunc(x)), ' ', unistr('\2588'))
       || substr(unistr(' \258F\258E\258D\258C\258B\258A\2589'), round(mod(x, 1) * 8) + 1, 1) max_24000
from   d
order  by salary desc;

-- Istogramma: assunzioni per anno
select extract(year from hire_date) anno,
       count(*) n,
       rpad('#', round(count(*) / max(count(*)) over () * 30), '#') grafico
from   hr.employees
group  by extract(year from hire_date)
order  by anno;


-- ---------------------------------------------------------------------
-- 5. SQL macro nella forma classica (funzioni PL/SQL con SQL_MACRO)
-- ---------------------------------------------------------------------
create or replace function dept_totals ( hired_after date )
  return varchar2 sql_macro(table) is
begin
  return q'[select department_id, count(*) emp# from hr.employees
            where hire_date > hired_after group by all]';
end;
/
create or replace function get_3_rows ( table_name dbms_tf.table_t )
  return varchar2 sql_macro(table) is
begin
  return 'select * from table_name fetch first 3 rows only';
end;
/
create or replace function formatted_name ( given varchar2, family varchar2 )
  return varchar2 sql_macro(scalar) is
begin
  return q'[family || ', ' || given]';
end;
/
create or replace function contains_z ( str varchar2 )
  return varchar2 sql_macro(scalar) is
begin
  return q'[( str like '%z%' collate binary_ci )]';
end;
/
select * from get_3_rows ( hr.departments )
left join dept_totals ( date '2015-01-01' ) using ( department_id );

select formatted_name ( first_name, last_name ) from hr.employees
where  contains_z ( last_name )
order  by 1;

-- La macro scalare viene sostituita dal suo testo: lo mostra il piano
explain plan for
select formatted_name ( first_name, last_name ) from hr.employees where contains_z ( last_name );
select * from table(dbms_xplan.display(format => 'BASIC +PREDICATE'));

-- ERRORE ATTESO: ORA-64630: use of SQL macro inside WITH clause is not supported
with x as (select * from dept_totals ( date '2017-01-01' ))
select * from x;

-- Il testo e' una stringa: l'errore di sintassi emerge solo all'uso
create or replace function macro_rotta return varchar2 sql_macro(table) is
begin
  return 'selec * from dual';
end;
/
-- ERRORE ATTESO: ORA-64626: invalid SQL text returned from SQL macro
select * from macro_rotta();

-- Parametro con lo stesso nome di una colonna: risultato sbagliato
create or replace function by_dept ( department_id number ) return varchar2 sql_macro(table) is
begin
  return 'select count(*) n from hr.employees where department_id = department_id';
end;
/
-- restituisce 106, non 45
select * from by_dept ( 50 );
-- il valore giusto: 45
select count(*) n from hr.employees where department_id = 50;

create or replace function top_n ( tab dbms_tf.table_t, n number ) return varchar2 sql_macro(table) is
begin
  return 'select * from tab fetch first n rows only';
end;
/
select * from top_n ( hr.jobs, 2 );

create or replace function stipendio_annuo ( sal number, comm number ) return varchar2 sql_macro(scalar) is
begin
  return 'sal * 12 * ( 1 + nvl ( comm, 0 ) )';
end;
/
create or replace function tra ( d date, da date, a date ) return varchar2 sql_macro(scalar) is
begin
  return '( d >= da and d < a )';
end;
/
select last_name, salary, commission_pct,
       stipendio_annuo ( salary, commission_pct ) annuo
from   hr.employees
where  tra ( hire_date, date '2018-01-01', date '2019-01-01' )
order  by annuo desc
fetch  first 5 rows only;

drop function macro_rotta;
drop function by_dept;


-- ---------------------------------------------------------------------
-- 6. Finestre temporali con SQL classico (stessi risultati delle slide)
-- ---------------------------------------------------------------------
-- TUMBLE ( hr.employees, columns ( hire_date ), interval '2' year )
select time_bucket(hire_date, interval '2' year, date '1970-01-01') window_start, count(*)
from   hr.employees
group  by all
order  by window_start;

-- HOP ( ..., interval '6' month, interval '2' year ): ogni riga in 2 anni / 6 mesi = 4 finestre
select add_months(time_bucket(e.hire_date, interval '6' month, date '1970-01-01'), -6 * n.k) window_start,
       count(*)
from   hr.employees e
cross  join (select level - 1 k connect by level <= 4) n
group  by all
order  by window_start;

-- CUMULATE ( ..., interval '2' year, interval '10' year ): 10 / 2 = 5 passi
select time_bucket(e.hire_date, interval '10' year, date '1970-01-01') window_start,
       add_months(time_bucket(e.hire_date, interval '10' year, date '1970-01-01'), 24 * n.k) window_end,
       count(*)
from   hr.employees e
cross  join (select level k connect by level <= 5) n
where  e.hire_date < add_months(time_bucket(e.hire_date, interval '10' year, date '1970-01-01'), 24 * n.k)
group  by all
order  by window_start, window_end;

-- SESSIONS ( ..., interval '2' year ): isole e buchi con LAG + SUM
with segnate as (
  select hire_date,
         case when hire_date <= add_months(lag(hire_date) over (order by hire_date), 24)
              then 0 else 1 end nuova_sessione
  from   hr.employees
), numerate as (
  select hire_date, sum(nuova_sessione) over (order by hire_date) sessione
  from   segnate
)
select min(hire_date) window_start, add_months(max(hire_date), 24) window_end, count(*)
from   numerate
group  by sessione
order  by window_start;

-- Dataset vendite
create table vendite (
  id      number generated always as identity primary key,
  ts      timestamp not null,
  negozio varchar2(10) not null,
  importo number(10,2) not null
);
insert into vendite (ts, negozio, importo) values
  (timestamp '2026-10-26 08:05:00', 'Milano', 120),
  (timestamp '2026-10-26 08:20:00', 'Roma',    80),
  (timestamp '2026-10-26 08:48:00', 'Milano',  45),
  (timestamp '2026-10-26 09:10:00', 'Roma',   200),
  (timestamp '2026-10-26 09:12:00', 'Milano',  60),
  (timestamp '2026-10-26 09:38:00', 'Roma',    35),
  (timestamp '2026-10-26 10:55:00', 'Milano', 150),
  (timestamp '2026-10-26 11:05:00', 'Roma',    90),
  (timestamp '2026-10-26 11:30:00', 'Milano',  75),
  (timestamp '2026-10-26 12:45:00', 'Roma',   300);
commit;

-- Sessioni per negozio (pausa massima 30 minuti)
with segnate as (
  select v.*,
         case when ts <= lag(ts) over (partition by negozio order by ts) + interval '30' minute
              then 0 else 1 end nuova
  from   vendite v
), numerate as (
  select s.*, sum(nuova) over (partition by negozio order by ts) sessione
  from   segnate s
)
select negozio, min(ts) window_start, max(ts) + interval '30' minute window_end,
       count(*) ordini, sum(importo) totale
from   numerate
group  by negozio, sessione
order  by negozio, window_start;


-- ---------------------------------------------------------------------
-- Pulizia
-- ---------------------------------------------------------------------
drop table vendite purge;
drop function is_locked;
drop function dept_totals;
drop function get_3_rows;
drop function formatted_name;
drop function contains_z;
drop function top_n;
drop function stipendio_annuo;
drop function tra;
