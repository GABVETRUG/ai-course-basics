-- =====================================================================
--  Novita' SQL di Oracle AI Database 23.26.4: script dimostrativo.
--  Richiede la 23.26.4 (o successiva) e lo schema HR ufficiale
--  (github.com/oracle-samples/db-sample-schemas).
--  Gli stessi esempi, riscritti per la 23.26.3 e verificati, sono in
--  equivalenti_fino_23_26_3.sql.
--  Le parti "DUE SESSIONI" vanno eseguite a mano in due finestre.
-- =====================================================================
set linesize 200 pagesize 100 serveroutput on
alter session set nls_date_format = 'DD-MON-YYYY HH24:MI:SS';
alter session set nls_timestamp_format = 'DD-MON-YYYY HH24:MI';


-- ---------------------------------------------------------------------
-- 1. SELECT * insieme ad altre espressioni
-- ---------------------------------------------------------------------
select rowid, upper ( region_name ) upper_name, *
from   hr.regions;

select sysdate, rowid, * from hr.regions;

-- Top-2 stipendi per reparto
select *, row_number() over (partition by department_id order by salary desc) rn
from   hr.employees
where  department_id in (20, 30)
qualify rn <= 2
order  by department_id, rn;

-- Pagina di risultati con il totale delle righe
select *, count(*) over () totale_righe
from   hr.jobs
order  by job_id
fetch  first 3 rows only;

-- Copia con una colonna in piu' (va in coda)
create table emp_snapshot as
  select *, sysdate as snapshot_at
  from   hr.employees;

-- Colonne invisibili e pseudocolonne
create table clienti_demo (id number, nome varchar2(30), nota varchar2(30) invisible);
insert into clienti_demo (id, nome, nota) values (1, 'Rossi', 'nascosta');
select *, nota from clienti_demo;
select ora_rowscn, rowid, * from clienti_demo;

-- Join: DEPARTMENT_ID una volta sola, MANAGER_ID due volte
select *, e.salary * 12 stipendio_annuo
from   hr.employees e
join   hr.departments d using (department_id)
where  employee_id = 101;

drop table emp_snapshot purge;
drop table clienti_demo purge;


-- ---------------------------------------------------------------------
-- 2. FETCH FIRST con FOR UPDATE [SKIP LOCKED]
-- ---------------------------------------------------------------------
-- DUE SESSIONI ---------------------------------------------------------
-- Sessione 1 (lasciarla aperta, senza COMMIT):
--   update hr.employees
--   set    hire_date = sysdate
--   where  employee_id = 100;
--
-- Sessione 2: restituisce 101, 102, 103
--   select employee_id
--   from   hr.employees
--   order  by employee_id
--   fetch  first 3 rows only
--   for    update skip locked;
-- ---------------------------------------------------------------------

-- Coda di lavori
create table jobs_demo (
  job_id     number generated always as identity primary key,
  payload    varchar2(100) not null,
  stato      varchar2(10) default 'NUOVO' not null,
  creato_il  timestamp default systimestamp not null,
  preso_da   varchar2(30),
  finito_il  timestamp
);
create index jobs_demo_coda_ix on jobs_demo (stato, creato_il);

insert into jobs_demo (payload)
select 'job ' || level connect by level <= 20;
commit;

-- Worker: da eseguire anche in piu' sessioni contemporaneamente
declare
  cursor c_lotto is
    select job_id, payload
    from   jobs_demo
    where  stato = 'NUOVO'
    order  by creato_il, job_id
    fetch  first 5 rows only
    for    update skip locked;
begin
  for j in c_lotto loop
    -- elaborazione di j.payload ...
    update jobs_demo
    set    stato     = 'FATTO',
           preso_da  = sys_context('userenv', 'sid'),
           finito_il = systimestamp
    where  job_id = j.job_id;
  end loop;
  commit;
end;
/
select job_id, stato, preso_da from jobs_demo order by job_id fetch first 8 rows only;

drop table jobs_demo purge;


-- ---------------------------------------------------------------------
-- 3. UUID v5 e v7
-- ---------------------------------------------------------------------
select uuid ( 7 ) ordered,
       uuid ( 5, 'url', 'test.com/' || level ) name_hash
connect by level <= 5;

-- Istante di creazione di un UUID v7
with u as (select uuid ( 7 ) id)
select raw_to_uuid(id) uuid_testo,
       timestamp '1970-01-01 00:00:00 UTC'
         + numtodsinterval(to_number(substr(rawtohex(id), 1, 12), 'XXXXXXXXXXXX') / 1000, 'SECOND') creato_utc
from   u;

-- Chiave primaria v7 valorizzata nell'INSERT.
-- Nota: su 23.26.3 la clausola DEFAULT accetta uuid() ma non uuid(4) (ORA-00907):
-- verifica se la tua release accetta DEFAULT uuid(7) prima di usarlo.
create table ordini_demo (
  id       raw(16) primary key,
  cliente  varchar2(30) not null,
  importo  number(10,2) not null
);
insert into ordini_demo (id, cliente, importo) values (uuid ( 7 ), 'ACME', 120);
insert into ordini_demo (id, cliente, importo) values (uuid ( 7 ), 'Globex', 80);
select raw_to_uuid(id) id, cliente, importo from ordini_demo order by id;

-- Chiave stabile v5: stesso input, stesso UUID (anche in Python con uuid.uuid5)
select raw_to_uuid ( uuid ( 5, 'url', 'https://crm.example.it/clienti/C001' ) ) id_cliente;

select is_uuid('7a6fab4a-ad8d-580d-b94d-c96326ecafd3') v5_valido;

drop table ordini_demo purge;


-- ---------------------------------------------------------------------
-- 4. BAR_CHART ( valore [, massimo [, minimo [, larghezza [, simbolo ]]]] )
-- ---------------------------------------------------------------------
select salary,
       bar_chart ( salary ) max_100,
       bar_chart ( salary, 24000 ) max_24000,
       bar_chart ( salary, 24000, 0, 20, '#' ) max_24000_20_chars
from   hr.employees;

-- Percentuali: quota della spesa per stipendi per reparto
select department_name,
       round(100 * ratio_to_report(sum(salary)) over (), 1) pct,
       bar_chart ( round(100 * ratio_to_report(sum(salary)) over (), 1), 100, 0, 20 ) quota
from   hr.employees
join   hr.departments using (department_id)
group  by department_name
order  by pct desc;

-- Istogramma con scala automatica
select extract(year from hire_date) anno,
       count(*) n,
       bar_chart ( count(*), max(count(*)) over (), 0, 30, '#' ) grafico
from   hr.employees
group  by extract(year from hire_date)
order  by anno;


-- ---------------------------------------------------------------------
-- 5. CREATE MACRO
-- ---------------------------------------------------------------------
-- Vista con parametri
create or replace macro dept_totals ( hired_after date ) is
  select department_id, count(*) emp# from hr.employees
  where  hire_date > hired_after group by all;

-- Vista polimorfica: il nome della tabella e' un parametro
create or replace macro get_3_rows ( table_name table ) is
  select * from table_name fetch first 3 rows only;

select * from get_3_rows ( hr.departments )
left join dept_totals ( date '2015-01-01' ) using ( department_id );

-- Macro scalari
create or replace macro formatted_name ( given varchar2, family varchar2 ) is
family || ', ' || given;

-- Le parentesi rendono il corpo un predicato, usabile nella WHERE
create or replace macro contains_z ( str varchar2 ) is
( str like '%z%' collate binary_ci );

select formatted_name ( first_name, last_name ) from hr.employees
where  contains_z ( last_name );

create or replace macro top_n ( tab table, n number ) is
  select * from tab fetch first n rows only;

select * from top_n ( hr.jobs, 2 );

create or replace macro stipendio_annuo ( sal number, comm number ) is
  sal * 12 * ( 1 + nvl ( comm, 0 ) );

create or replace macro tra ( d date, da date, a date ) is
  ( d >= da and d < a );

select last_name, salary, commission_pct,
       stipendio_annuo ( salary, commission_pct ) annuo
from   hr.employees
where  tra ( hire_date, date '2018-01-01', date '2019-01-01' )
order  by annuo desc
fetch  first 5 rows only;

-- Macro nella clausola WITH (fino alla 23.26.3: ORA-64630)
with recenti as (
  select * from dept_totals ( date '2017-01-01' )
)
select * from recenti order by emp# desc, department_id;


-- ---------------------------------------------------------------------
-- 6. TUMBLE, HOP, CUMULATE, SESSIONS
-- ---------------------------------------------------------------------
select window_start, count (*)
from   tumble (
  hr.employees,
  columns ( hire_date ),
  interval '2' year
)
group  by all order by window_start;

select window_start, count (*)
from   hop (
  hr.employees,
  columns ( hire_date ),
  interval '6' month,
  interval '2' year
)
group  by all order by window_start;

select window_start, window_end, count (*)
from   cumulate (
  hr.employees,
  columns ( hire_date ),
  interval '2' year,
  interval '10' year
)
group  by all order by window_start, window_end;

select window_start, window_end, count (*)
from   sessions (
  hr.employees,
  columns ( hire_date ),
  interval '2' year
)
group  by all order by window_start;

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

-- Ordini per ora
select window_start, window_end, count(*) ordini, sum(importo) totale
from   tumble ( vendite, columns ( ts ), interval '1' hour )
group  by all
order  by window_start;

-- Ordini per ora e negozio
select window_start, negozio, count(*) ordini, sum(importo) totale
from   tumble ( vendite, columns ( ts ), interval '1' hour )
group  by all
order  by window_start, negozio;

-- Finestre di 2 ore che partono ogni ora
select window_start, window_end, count(*) ordini, sum(importo) totale
from   hop ( vendite, columns ( ts ), interval '1' hour, interval '2' hour )
group  by all
order  by window_start;

-- Progressivo della giornata, ora per ora
select window_start, window_end, count(*) ordini, sum(importo) progressivo
from   cumulate ( vendite, columns ( ts ), interval '1' hour, interval '1' day )
group  by all
order  by window_end;

-- Raffiche di ordini separate da almeno 30 minuti di pausa
select window_start, window_end, count(*) ordini, sum(importo) totale
from   sessions ( vendite, columns ( ts ), interval '30' minute )
group  by all
order  by window_start;

-- BAR_CHART + HOP: assunzioni nei due anni successivi, ogni sei mesi
select window_start,
       count(*) n,
       bar_chart ( count(*), max(count(*)) over (), 0, 30, '#' ) grafico
from   hop ( hr.employees, columns ( hire_date ), interval '6' month, interval '2' year )
group  by window_start
order  by window_start;


-- ---------------------------------------------------------------------
-- Pulizia
-- ---------------------------------------------------------------------
drop table vendite purge;
-- DROP MACRO: sintassi attesa per analogia con CREATE MACRO (verificala sul manuale)
drop macro dept_totals;
drop macro get_3_rows;
drop macro formatted_name;
drop macro contains_z;
drop macro top_n;
drop macro stipendio_annuo;
drop macro tra;
