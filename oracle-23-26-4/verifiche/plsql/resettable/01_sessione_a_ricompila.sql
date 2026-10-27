set feedback on
create or replace package body pkg_normale is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('pkg_normale (v2): contatore = ' || contatore);
  end;
end;
/
create or replace package body pkg_resettable resettable is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('pkg_resettable (v2): contatore = ' || contatore);
  end;
end;
/
exit
