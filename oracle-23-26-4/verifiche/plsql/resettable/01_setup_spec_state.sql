set feedback on
create or replace package pkg_normale is
  contatore number := 0;
  procedure incrementa;
end;
/
create or replace package body pkg_normale is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('pkg_normale: contatore = ' || contatore);
  end;
end;
/
create or replace package pkg_resettable resettable is
  contatore number := 0;
  procedure incrementa;
end;
/
create or replace package body pkg_resettable resettable is
  procedure incrementa is
  begin
    contatore := contatore + 1;
    dbms_output.put_line('pkg_resettable: contatore = ' || contatore);
  end;
end;
/
select object_name, object_type, status from user_objects where object_name like 'PKG_%' order by 1, 2;
exit
