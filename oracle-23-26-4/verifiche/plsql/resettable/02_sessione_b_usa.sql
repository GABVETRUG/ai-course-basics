set serveroutput on feedback off
exec pkg_body_state.incrementa
exec pkg_body_state.incrementa
exec pkg_spec_state.incrementa
exec pkg_spec_state.incrementa
exec dbms_session.sleep(8)
prompt --- dopo la ricompilazione
exec pkg_body_state.incrementa
exec pkg_body_state.incrementa
exec pkg_spec_state.incrementa
exec pkg_spec_state.incrementa
exit
