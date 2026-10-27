update hr.employees set salary = salary where employee_id = 100;
exec dbms_session.sleep(15)
rollback;
exit
