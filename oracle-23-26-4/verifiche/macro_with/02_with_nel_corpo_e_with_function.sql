set linesize 200 pagesize 100 feedback on
prompt === T3a: macro whose body contains a WITH, param used outside the subquery ===
create or replace function top_earners ( n number ) return varchar2 sql_macro(table) is
begin
  return q'[with ranked as (
              select employee_id, last_name, salary,
                     dense_rank() over (order by salary desc) rnk
              from   hr.employees)
            select employee_id, last_name, salary, rnk from ranked where rnk <= n]';
end;
/
select * from top_earners(3);
prompt === T3b: macro body with WITH, scalar param used INSIDE the subquery ===
create or replace function dept_staff ( p_dept number ) return varchar2 sql_macro(table) is
begin
  return q'[with d as (select employee_id, last_name from hr.employees where department_id = p_dept)
            select count(*) n from d]';
end;
/
select * from dept_staff(50);
select * from dept_staff(60);
prompt === T3c: macro with WITH body, called from a statement that has its own WITH ===
with x as (select 3 lim from dual)
select t.* from x, top_earners(3) t;
prompt === T4a: inline table macro via WITH FUNCTION ===
with function top3 ( t dbms_tf.table_t ) return varchar2 sql_macro(table) is
begin
  return 'select * from t fetch first 3 rows only';
end;
select * from top3(hr.jobs)
/
prompt === T4b: inline scalar macro used in main query ===
with function annuo ( sal number ) return varchar2 sql_macro(scalar) is
begin
  return 'sal * 12';
end;
select last_name, annuo(salary) annuo from hr.employees where employee_id in (100, 101)
/
prompt === T4c: inline scalar macro used inside a CTE ===
with function annuo ( sal number ) return varchar2 sql_macro(scalar) is
begin
  return 'sal * 12';
end;
x as (select last_name, annuo(salary) annuo from hr.employees where employee_id in (100, 101))
select * from x
/
prompt === T5: nested WITH (23.26.2+) ===
with a as (
  with b as (select department_id, count(*) n from hr.employees group by department_id)
  select * from b where n > 5
)
select * from a order by n desc;
