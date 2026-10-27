set serveroutput on feedback off
exec pkg_resettable.incrementa
exec pkg_resettable.incrementa
exec pkg_normale.incrementa
exec pkg_normale.incrementa
prompt ... intanto un'altra sessione ricompila i due package body
exec dbms_session.sleep(8)
exec pkg_resettable.incrementa
exec pkg_resettable.incrementa
exec pkg_normale.incrementa
set serveroutput on
exec pkg_normale.incrementa
exit
