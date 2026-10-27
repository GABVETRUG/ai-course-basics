set linesize 200 pagesize 100 feedback on serveroutput on long 2000
prompt === T6 SQL transpiler ===
create or replace function annuale(p_sal number, p_comm number) return number is
begin
  return p_sal * 12 * (1 + nvl(p_comm, 0));
end;
/
show parameter sql_transpiler
alter session set sql_transpiler = 'OFF';
explain plan for select last_name from hr.employees where annuale(salary, commission_pct) > 200000;
select plan_table_output from table(dbms_xplan.display(format => 'BASIC +PREDICATE')) where plan_table_output like '%filter%';
alter session set sql_transpiler = 'ON';
explain plan for select last_name from hr.employees where annuale(salary, commission_pct) > 200000;
select plan_table_output from table(dbms_xplan.display(format => 'BASIC +PREDICATE')) where plan_table_output like '%filter%';
alter session set sql_transpiler = 'OFF';
prompt === T5 JSON constructor from PL/SQL record ===
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
prompt === T5b JSON_VALUE into a record ===
declare
  type t_emp is record (employee_id number, last_name varchar2(25), salary number);
  r t_emp;
begin
  r := json_value('{"employee_id":7,"last_name":"Rossi","salary":3000}', '$' returning t_emp);
  dbms_output.put_line(r.last_name || ' ' || r.salary);
end;
/
prompt === T8 VECTOR in PL/SQL ===
declare
  v1 vector := to_vector('[1, 2, 3]');
  v2 vector := to_vector('[2, 2, 3]');
begin
  dbms_output.put_line('distanza euclidea: ' || vector_distance(v1, v2, euclidean));
  dbms_output.put_line('dimensioni: ' || vector_dimension_count(v1));
end;
/
prompt === T10 RETURNING OLD/NEW ===
declare
  l_old number; l_new number;
begin
  update hr.employees set salary = salary * 1.1 where employee_id = 100
  returning old salary, new salary into l_old, l_new;
  dbms_output.put_line('prima ' || l_old || ', dopo ' || l_new);
  rollback;
end;
/
prompt === T9 DBMS_DEVELOPER ===
select json_serialize(dbms_developer.get_metadata(name => 'REGIONS', schema => 'HR', level => 'BASIC') pretty) md;
