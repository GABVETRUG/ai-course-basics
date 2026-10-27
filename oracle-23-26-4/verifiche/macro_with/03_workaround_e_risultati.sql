set linesize 200 pagesize 100 feedback on
prompt === T3d: same logic with an inline view instead of WITH inside the macro ===
create or replace function dept_staff ( p_dept number ) return varchar2 sql_macro(table) is
begin
  return q'[select count(*) n
            from (select employee_id, last_name from hr.employees where department_id = p_dept) d]';
end;
/
select * from dept_staff(50);
select * from dept_staff(60);
prompt === T3e: param in main select, WITH only for constant logic ===
create or replace function dept_staff2 ( p_dept number ) return varchar2 sql_macro(table) is
begin
  return q'[with d as (select employee_id, last_name, department_id from hr.employees)
            select count(*) n from d where department_id = p_dept]';
end;
/
select * from dept_staff2(50);
prompt === expected output for 23.26.4 pipeline example (inline views instead of CTE) ===
select * from (select * from get_3_rows(hr.departments)) r
left join (select * from dept_totals(date '2015-01-01')) a using (department_id)
order by department_id;
prompt === scalar macros via inline view ===
select * from (select formatted_name(first_name, last_name) nome from hr.employees where contains_z(last_name)) z order by 1;
