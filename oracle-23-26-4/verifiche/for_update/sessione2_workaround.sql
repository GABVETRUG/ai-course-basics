set linesize 200 pagesize 100 feedback on serveroutput on
create or replace function is_locked(p_id number) return varchar2 is
  pragma autonomous_transaction;
  l number;
begin
  select employee_id into l from employees where employee_id = p_id for update nowait;
  rollback;
  return 'libera';
exception when others then
  rollback;
  return case when sqlcode = -54 then 'BLOCCATA' else sqlerrm end;
end;
/
prompt === (a) ROWNUM + SKIP LOCKED: chiedo 3 righe ===
select employee_id from employees where rownum <= 3 for update skip locked;
rollback;
prompt === (b) IN (subquery FETCH FIRST) + SKIP LOCKED ===
select employee_id from employees
where employee_id in (select employee_id from employees order by employee_id fetch first 3 rows only)
for update skip locked;
rollback;
prompt === (c) PL/SQL cursor SKIP LOCKED + BULK COLLECT LIMIT 3 ===
declare
  cursor c is select employee_id from employees order by employee_id for update skip locked;
  type t_ids is table of employees.employee_id%type;
  l_ids t_ids;
begin
  open c;
  fetch c bulk collect into l_ids limit 3;
  for i in 1 .. l_ids.count loop dbms_output.put_line('preso: ' || l_ids(i)); end loop;
  dbms_output.put_line('101 -> ' || is_locked(101) || ' | 103 -> ' || is_locked(103) || ' | 104 -> ' || is_locked(104) || ' | 150 -> ' || is_locked(150));
  close c;
  rollback;
end;
/
prompt === (d) plain FOR UPDATE cursor (no skip locked): when are rows locked? ===
declare
  cursor c is select employee_id from employees where employee_id between 101 and 110 order by employee_id for update;
  type t_ids is table of employees.employee_id%type;
  l_ids t_ids;
begin
  open c;
  dbms_output.put_line('dopo OPEN, prima del FETCH: 104 -> ' || is_locked(104) || ' | 110 -> ' || is_locked(110));
  fetch c bulk collect into l_ids limit 3;
  close c;
  rollback;
end;
/
prompt === (e) FOR UPDATE NOWAIT on locked row ===
select employee_id from employees where employee_id = 100 for update nowait;
prompt === (f) FOR UPDATE WAIT 2 on locked row ===
select employee_id from employees where employee_id = 100 for update wait 2;
exit
