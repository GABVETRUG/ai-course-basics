set feedback off
create or replace package pkg_body_state resettable is
  procedure incrementa;
end;
/
create or replace package body pkg_body_state resettable is
  contatore number := 0;
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('stato nel body: contatore = ' || contatore);
  end;
end;
/
create or replace package pkg_spec_state resettable is
  contatore number := 0;
  procedure incrementa;
end;
/
create or replace package body pkg_spec_state resettable is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('stato nella spec: contatore = ' || contatore);
  end;
end;
/
exit
