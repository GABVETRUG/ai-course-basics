set linesize 200 pagesize 100 feedback off serveroutput on
create or replace function uuid7_at(p_ms number) return raw is
  l_r varchar2(32);
begin
  select rawtohex(uuid()) into l_r from dual;
  return hextoraw(lpad(to_char(p_ms, 'FMXXXXXXXXXXXX'), 12, '0') || '7' || substr(l_r, 14, 3) || substr(l_r, 17, 16));
end;
/
create or replace procedure load_rate(p_rate pls_integer, p_rows pls_integer) is
  l_tab varchar2(30) := 'T_R' || p_rate;
  l_base number := 1790613449463;
  l_s1 number; l_s2 number; l_e1 number; l_e2 number;
  l_idx varchar2(128); l_lf number; l_pct number;
  function stat(p varchar2) return number is v number;
  begin select s.value into v from v$mystat s join v$statname n on n.statistic# = s.statistic# where n.name = p; return v; end;
begin
  begin execute immediate 'drop table ' || l_tab || ' purge'; exception when others then null; end;
  execute immediate 'create table ' || l_tab || ' (id raw(16) primary key, pad varchar2(40))';
  l_s1 := stat('leaf node splits'); l_s2 := stat('leaf node 90-10 splits');
  for i in 0 .. p_rows - 1 loop
    execute immediate 'insert into ' || l_tab || ' values (:1, :2)' using uuid7_at(l_base + trunc(i / p_rate)), rpad('x', 40, 'x');
    if mod(i, 1000) = 0 then commit; end if;
  end loop;
  commit;
  l_e1 := stat('leaf node splits') - l_s1; l_e2 := stat('leaf node 90-10 splits') - l_s2;
  select index_name into l_idx from user_indexes where table_name = l_tab;
  execute immediate 'analyze index ' || l_idx || ' validate structure';
  select lf_blks, pct_used into l_lf, l_pct from index_stats;
  dbms_output.put_line('v7 con ' || lpad(p_rate, 3) || ' righe/ms: split=' || l_e1 || ' (90-10=' || l_e2 || ', 50-50=' || (l_e1 - l_e2) || ')  foglie=' || l_lf || '  riempimento=' || l_pct || '%');
end;
/
exec load_rate(1, 200000)
exec load_rate(2, 200000)
exec load_rate(5, 200000)
exec load_rate(25, 200000)
exec load_rate(100, 200000)
