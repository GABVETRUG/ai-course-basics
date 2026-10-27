set linesize 200 pagesize 100 feedback on serveroutput on
prompt === T2 extended CASE (statement) ===
declare
  procedure classifica(n number) is
  begin
    case n
      when < 0 then dbms_output.put_line(n || ': negativo');
      when 0 then dbms_output.put_line(n || ': zero');
      when 1, 3, 5, 7, 9 then dbms_output.put_line(n || ': dispari sotto 10');
      when between 10 and 99 then dbms_output.put_line(n || ': due cifre');
      when is null then dbms_output.put_line('null');
      else dbms_output.put_line(n || ': altro');
    end case;
  end;
begin
  classifica(-5); classifica(0); classifica(7); classifica(42); classifica(null); classifica(8);
end;
/
prompt === T2b extended CASE (expression) ===
declare
  s varchar2(20);
begin
  for i in 1 .. 4 loop
    s := case i when 1, 2 then 'basso' when > 3 then 'alto' else 'medio' end;
    dbms_output.put_line(i || ' -> ' || s);
  end loop;
end;
/
prompt === T3 IF NOT EXISTS ===
create procedure if not exists p_demo is begin null; end;
/
create procedure if not exists p_demo is begin dbms_output.put_line('seconda versione'); end;
/
select text from user_source where name = 'P_DEMO' order by line;
drop procedure if exists p_demo;
drop procedure if exists p_demo;
create or replace procedure if not exists p_demo is begin null; end;
/
prompt === T4 BOOLEAN function callable from SQL ===
create or replace function guadagna_molto(p_sal number) return boolean is
begin
  return p_sal > 15000;
end;
/
select last_name, salary, guadagna_molto(salary) molto from hr.employees where guadagna_molto(salary) order by salary desc;
prompt === T7 DML NOWAIT syntax probe (no lock held: just syntax) ===
update hr.employees set salary = salary where employee_id = 100 nowait;
rollback;
update hr.employees set salary = salary where employee_id = 100 wait 2;
rollback;
prompt === T11 macro dictionary views ===
select count(*) from user_macro_parameters;
select count(*) from user_macros;
