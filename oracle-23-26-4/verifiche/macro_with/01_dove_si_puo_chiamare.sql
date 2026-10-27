set linesize 200 pagesize 100 feedback on
create or replace function dept_totals ( hired_after date ) return varchar2 sql_macro(table) is
begin
  return q'[select department_id, count(*) emp# from hr.employees where hire_date > hired_after group by all]';
end;
/
create or replace function get_3_rows ( table_name dbms_tf.table_t ) return varchar2 sql_macro(table) is
begin
  return 'select * from table_name fetch first 3 rows only';
end;
/
create or replace function top_n ( tab dbms_tf.table_t, n number ) return varchar2 sql_macro(table) is
begin
  return 'select * from tab fetch first n rows only';
end;
/
create or replace function formatted_name ( given varchar2, family varchar2 ) return varchar2 sql_macro(scalar) is
begin
  return q'[family || ', ' || given]';
end;
/
create or replace function contains_z ( str varchar2 ) return varchar2 sql_macro(scalar) is
begin
  return q'[( str like '%z%' collate binary_ci )]';
end;
/
prompt === T1a: table macro inside CTE ===
with recenti as (select * from dept_totals(date '2017-01-01'))
select * from recenti;
prompt === T1b: table macro inside inline view ===
select * from (select * from dept_totals(date '2017-01-01')) order by emp# desc, department_id;
prompt === T1c: table macro in main query, statement has a WITH ===
with reparti as (select department_id, department_name from hr.departments where department_id <= 30)
select * from reparti left join dept_totals(date '2015-01-01') using (department_id) order by department_id;
prompt === T1d: scalar macro in main query, statement has a WITH ===
with e as (select first_name, last_name from hr.employees)
select formatted_name(first_name, last_name) nome from e where contains_z(last_name) order by 1;
prompt === T1e: scalar macro inside CTE ===
with z as (select formatted_name(first_name, last_name) nome from hr.employees where contains_z(last_name))
select * from z order by 1;
prompt === T2: CTE passed as table argument to polymorphic macro ===
with emp50 as (select employee_id, last_name, salary from hr.employees where department_id = 50 order by salary desc)
select * from top_n(emp50, 3);
prompt === T2b: CTE passed to get_3_rows ===
with emp50 as (select employee_id, last_name, salary from hr.employees where department_id = 50)
select * from get_3_rows(emp50);
