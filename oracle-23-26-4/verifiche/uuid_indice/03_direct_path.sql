set linesize 200 pagesize 100 feedback off serveroutput on
begin execute immediate 'drop table t_conv purge'; exception when others then null; end;
/
begin execute immediate 'drop table t_dp purge'; exception when others then null; end;
/
create table t_conv (id raw(16) primary key, pad varchar2(40));
create table t_dp   (id raw(16) primary key, pad varchar2(40));
insert into t_conv select uuid7_at(1790613449463 + trunc(level / 100)), rpad('x', 40, 'x') from dual connect by level <= 200000;
commit;
insert /*+ append */ into t_dp select uuid7_at(1790613449463 + trunc(level / 100)), rpad('x', 40, 'x') from dual connect by level <= 200000;
commit;
declare
  procedure show(p_tab varchar2) is
    l_idx varchar2(128); l_lf number; l_pct number;
  begin
    select index_name into l_idx from user_indexes where table_name = p_tab;
    execute immediate 'analyze index ' || l_idx || ' validate structure';
    select lf_blks, pct_used into l_lf, l_pct from index_stats;
    dbms_output.put_line(rpad(p_tab, 7) || ' foglie=' || l_lf || '  riempimento=' || l_pct || '%');
  end;
begin
  show('T_CONV'); show('T_DP');
end;
/
