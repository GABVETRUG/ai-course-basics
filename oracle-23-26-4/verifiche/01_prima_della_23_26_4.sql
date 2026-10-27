set linesize 200 pagesize 100 feedback on
prompt === 1a select rowid, upper(..), * ===
select rowid, upper(region_name) upper_name, * from regions;
prompt === 1b select *, expr ===
select *, upper(region_name) from regions;
prompt === 1c qualified star workaround ===
select rowid, upper(region_name) upper_name, r.* from regions r;
prompt === 2 fetch first + for update ===
select employee_id from employees order by employee_id fetch first 3 rows only for update skip locked;
rollback;
prompt === 3a uuid() ===
select uuid() u, raw_to_uuid(uuid()) s from dual;
prompt === 3b uuid(4) / uuid(0) ===
select uuid(4) from dual;
select uuid(0) from dual;
prompt === 3c uuid(7) ===
select uuid(7) from dual;
prompt === 3d uuid(5,...) ===
select uuid(5, 'url', 'test.com/1') from dual;
prompt === 3e is_uuid ===
select is_uuid('7a6fab4a-ad8d-580d-b94d-c96326ecafd3') v5, is_uuid('6ba7b811-9dad-11d1-80b4-00c04fd430c8') v1 from dual;
prompt === 4 bar_chart ===
select bar_chart(50) from dual;
prompt === 5 create macro ===
create or replace macro formatted_name ( given varchar2, family varchar2 ) is family || ', ' || given;
prompt === 6 tumble ===
select window_start, count(*) from tumble(employees, columns(hire_date), interval '2' year) group by all order by window_start;
prompt === 7a group by all ===
select department_id, count(*) from employees group by all order by 1 fetch first 3 rows only;
prompt === 7b time_bucket ===
select time_bucket(hire_date, interval '2' year, date '1970-01-01') b, count(*) from employees group by all order by 1;
prompt === 7c select without from + connect by ===
select level connect by level <= 3;
