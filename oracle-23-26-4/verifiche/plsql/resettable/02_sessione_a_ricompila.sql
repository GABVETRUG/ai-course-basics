set feedback on
-- ricompila il BODY che contiene lo stato
create or replace package body pkg_body_state resettable is
  contatore number := 0;
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('stato nel body (v2): contatore = ' || contatore);
  end;
end;
/
-- ricompila la SPEC che contiene lo stato
create or replace package pkg_spec_state resettable is
  contatore number := 0;
  procedure incrementa;
  versione constant varchar2(2) := 'v2';
end;
/
exit
