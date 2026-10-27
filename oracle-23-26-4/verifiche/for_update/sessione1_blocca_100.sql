set feedback on
update employees set hire_date = sysdate where employee_id = 100;
exec dbms_session.sleep(40)
rollback;
exit
