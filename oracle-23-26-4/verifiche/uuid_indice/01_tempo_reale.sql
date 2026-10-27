set linesize 200 pagesize 100 feedback off serveroutput on
create or replace function uuid7_emu return raw is
  -- emulazione UUIDv7 (RFC 9562) solo per il test su 23.26.3
  l_ts timestamp(6) := sys_extract_utc(systimestamp);
  l_iv interval day(9) to second(6) := l_ts - timestamp '1970-01-01 00:00:00';
  l_ms number := trunc(((extract(day from l_iv) * 24 + extract(hour from l_iv)) * 60 + extract(minute from l_iv)) * 60000
                       + extract(second from l_iv) * 1000);
  l_r  varchar2(32);
begin
  select rawtohex(uuid()) into l_r from dual;
  return hextoraw(lpad(to_char(l_ms, 'FMXXXXXXXXXXXX'), 12, '0') || '7' || substr(l_r, 14, 3) || substr(l_r, 17, 16));
end;
/
select uuid7_emu() v7, sys_extract_utc(systimestamp) now_utc from dual;
drop table t_v4 purge;
drop table t_v7 purge;
drop table t_seq purge;
create table t_v4  (id raw(16) primary key, pad varchar2(40));
create table t_v7  (id raw(16) primary key, pad varchar2(40));
create table t_seq (id number generated always as identity primary key, pad varchar2(40));
create or replace procedure load_test(p_kind varchar2, p_rows pls_integer) is
  l_s1 number; l_s2 number; l_e1 number; l_e2 number; t0 number := dbms_utility.get_time;
  function stat(p varchar2) return number is v number;
  begin select s.value into v from v$mystat s join v$statname n on n.statistic# = s.statistic# where n.name = p; return v; end;
begin
  l_s1 := stat('leaf node splits'); l_s2 := stat('leaf node 90-10 splits');
  for i in 1 .. p_rows loop
    case p_kind
      when 'v4'  then insert into t_v4 (id, pad) values (uuid(), rpad('x', 40, 'x'));
      when 'v7'  then insert into t_v7 (id, pad) values (uuid7_emu(), rpad('x', 40, 'x'));
      when 'seq' then insert into t_seq (pad) values (rpad('x', 40, 'x'));
    end case;
    if mod(i, 1000) = 0 then commit; end if;
  end loop;
  commit;
  l_e1 := stat('leaf node splits') - l_s1; l_e2 := stat('leaf node 90-10 splits') - l_s2;
  dbms_output.put_line(rpad(p_kind, 4) || ' leaf splits=' || l_e1 || ' (di cui 90-10=' || l_e2 || ', 50-50=' || (l_e1 - l_e2) || ')  tempo=' || (dbms_utility.get_time - t0)/100 || 's');
end;
/
exec load_test('v4', 200000)
exec load_test('v7', 200000)
exec load_test('seq', 200000)
declare
  procedure show(p_tab varchar2) is
    l_idx varchar2(128); l_lf number; l_pct number; l_h number;
  begin
    select index_name into l_idx from user_indexes where table_name = p_tab;
    execute immediate 'analyze index ' || l_idx || ' validate structure';
    select lf_blks, pct_used, height into l_lf, l_pct, l_h from index_stats;
    dbms_output.put_line(rpad(p_tab, 6) || ' foglie=' || l_lf || '  riempimento medio=' || l_pct || '%  altezza=' || l_h);
  end;
begin
  show('T_V4'); show('T_V7'); show('T_SEQ');
end;
/
