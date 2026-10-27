set feedback on timing on
prompt === UPDATE ... NOWAIT su riga bloccata ===
update hr.employees set salary = salary + 1 where employee_id = 100 nowait;
prompt === UPDATE ... WAIT 3 su riga bloccata ===
update hr.employees set salary = salary + 1 where employee_id = 100 wait 3;
prompt === UPDATE ... NOWAIT su altre righe (non bloccate) ===
update hr.employees set salary = salary where department_id = 60 nowait;
rollback;
prompt === in PL/SQL ===
set serveroutput on
begin
  update hr.employees set salary = salary + 1 where employee_id = 100 nowait;
exception
  when others then
    dbms_output.put_line('catturato: ' || sqlcode);
end;
/
exit
