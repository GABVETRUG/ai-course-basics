"""Builds the explainer page for the Oracle 23.26.4 SQL features.

    python3 build.py              ../novita-sql-23-26-4.html as a standalone HTML document
    python3 build.py --artifact   the same page without <html>/<head>/<body>, for publishing as an Artifact
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from diagrams import svg_windows, svg_uuid, svg_lock  # noqa: E402

OUT = Path(__file__).parent.parent / "novita-sql-23-26-4.html"

# ---------------------------------------------------------------- highlighting
KW = set("""select from where group by all order fetch first next rows row only for update skip locked nowait wait
create or replace macro is table join left right inner outer cross using on with as connect level interval year
month day hour minute second columns and not null like collate insert into values commit rollback declare begin end
cursor loop open close bulk collect limit type of return function sql_macro scalar primary key default generated
always identity case when then else over partition qualify distinct in exists set delete merge matched union raw
number varchar2 date timestamp if index alter add invisible drop purge desc asc between explain plan
pragma autonomous_transaction exception others""".split())
FN = set("""uuid bar_chart tumble hop cumulate sessions time_bucket lag row_number sum count upper lower raw_to_uuid
uuid_to_raw is_uuid standard_hash rawtohex hextoraw substr to_number numtodsinterval add_months extract round rpad
nvl min max trunc mod least greatest replace unistr ratio_to_report sysdate systimestamp sys_context rowid rownum
ora_rowscn regexp_replace dbms_utility expand_sql_text dbms_output put_line utl_raw bit_or bit_and concat
cast_to_raw dbms_xplan display""".split())
TOK = re.compile(r"(?P<cm>--[^\n]*|/\*.*?\*/)|(?P<st>q'\[.*?\]'|'(?:[^']|'')*')|(?P<nu>\b\d+(?:\.\d+)?\b)"
                 r"|(?P<id>[A-Za-z_][A-Za-z0-9_$#]*)|(?P<ot>.)", re.S)


def esc(s):
    return html.escape(s, quote=False)


def hl(src):
    out = []
    for m in TOK.finditer(src):
        kind, t = m.lastgroup, m.group()
        if kind == "cm":
            out.append(f'<span class="c">{esc(t)}</span>')
        elif kind == "st":
            out.append(f'<span class="s">{esc(t)}</span>')
        elif kind == "nu":
            out.append(f'<span class="n">{esc(t)}</span>')
        elif kind == "id":
            lw = t.lower()
            if lw in KW:
                out.append(f'<span class="k">{esc(t)}</span>')
            elif lw in FN:
                out.append(f'<span class="f">{esc(t)}</span>')
            else:
                out.append(esc(t))
        else:
            out.append(esc(t))
    return "".join(out)


def hl_marked(src):
    parts = re.split(r"(⟦.*?⟧)", src, flags=re.S)
    res = []
    for p in parts:
        if p.startswith("⟦") and p.endswith("⟧"):
            res.append('<mark class="nw">' + hl(p[1:-1]) + "</mark>")
        else:
            res.append(hl(p))
    return "".join(res)


TAGS = {
    "new": '<span class="chip new">23.26.4</span>',
    "old": '<span class="chip old">fino a 23.26.3</span>',
    "any": "",
}


def code(src, tag="any", title="SQL", lang="sql"):
    body = hl_marked(src.strip("\n")) if lang == "sql" else esc(src.strip("\n"))
    return (f'<div class="code"><div class="blk-h"><span class="blk-t">{title}</span>{TAGS[tag]}'
            f'<button class="copy" type="button">Copia</button></div>'
            f'<pre><code>{body}</code></pre></div>')


PROV = {
    "slide": '<span class="chip slide">slide 23.26.4</span>',
    "run": '<span class="chip run">eseguito 23.26.3</span>',
    "exp": '<span class="chip exp">atteso</span>',
}


def out(text, prov, title="Risultato"):
    return (f'<div class="out"><div class="blk-h"><span class="blk-t">{title}</span>{PROV[prov]}</div>'
            f'<pre>{esc(text.strip(chr(10)))}</pre></div>')


def err(text, title="Errore"):
    return (f'<div class="out err"><div class="blk-h"><span class="blk-t">{title}</span>{PROV["run"]}</div>'
            f'<pre>{esc(text.strip(chr(10)))}</pre></div>')


def compare(left, right, lt="Fino a 23.26.3", rt="Con 23.26.4"):
    return (f'<div class="cmp"><div class="cmp-col"><p class="cmp-t old">{lt}</p>{left}</div>'
            f'<div class="cmp-col"><p class="cmp-t new">{rt}</p>{right}</div></div>')


def tbl(cols, rows):
    """SQL*Plus style result text. cols: (name, width, 'l'|'r')."""
    def cell(v, w, a):
        v = "" if v is None else str(v)
        return v.ljust(w) if a == "l" else v.rjust(w)
    head = " ".join(cell(n, w, a) for n, w, a in cols).rstrip()
    sep = " ".join("-" * w for _, w, _ in cols)
    body = [" ".join(cell(v, w, a) for v, (_, w, a) in zip(r, cols)).rstrip() for r in rows]
    return "\n".join([head, sep] + body)


def fig(svg, caption, wide=True):
    cls = "fig wide" if wide else "fig"
    hint = '<span class="scroll-hint">Scorri il diagramma in orizzontale. </span>' if wide else ""
    return f'<figure class="{cls}"><div class="fig-scroll">{svg}</div><figcaption>{hint}{caption}</figcaption></figure>'


def section(sid, eyebrow, title, kicker, body):
    return (f'<section id="{sid}" class="feat"><header class="feat-h"><p class="eyebrow">{eyebrow}</p>'
            f'<h2>{title}</h2><p class="kicker">{kicker}</p></header>{body}</section>')


def h3(t):
    return f"<h3>{t}</h3>"


def p(t):
    return f"<p>{t}</p>"


def ul(items, cls="list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def warn(items):
    return '<div class="warn"><p class="warn-t">Attenzione</p>' + ul(items, "list") + "</div>"


# ---------------------------------------------------------------- results
REGIONS_SLIDE = tbl([("ROWID", 18, "l"), ("UPPER_NAME", 25, "l"), ("REGION_ID", 10, "r"), ("REGION_NAME", 25, "l")], [
    ("AAASjQAABAAAIb8AAA", "EUROPE", 1, "Europe"),
    ("AAASjQAABAAAIb8AAB", "AMERICAS", 2, "Americas"),
    ("AAASjQAABAAAIb8AAC", "ASIA", 3, "Asia"),
    ("AAASjQAABAAAIb8AAD", "MIDDLE EAST AND AFRICA", 4, "Middle East and Africa"),
])

EMP_COLS = [("EMPLOYEE_ID", 11, "r"), ("FIRST_NAME", 10, "l"), ("LAST_NAME", 9, "l"), ("EMAIL", 8, "l"),
            ("PHONE_NUMBER", 14, "l"), ("HIRE_DATE", 9, "l"), ("JOB_ID", 8, "l"), ("SALARY", 6, "r"),
            ("COMMISSION_PCT", 14, "r"), ("MANAGER_ID", 10, "r"), ("DEPARTMENT_ID", 13, "r")]
TOP2 = tbl(EMP_COLS + [("RN", 2, "r")], [
    (201, "Michael", "Martinez", "MMARTINE", "1.515.555.0166", "17-FEB-14", "MK_MAN", 13000, None, 100, 20, 1),
    (202, "Pat", "Davis", "PDAVIS", "1.603.555.0167", "17-AUG-15", "MK_REP", 6000, None, 201, 20, 2),
    (114, "Den", "Li", "DLI", "1.515.555.0114", "07-DEC-12", "PU_MAN", 11000, None, 100, 30, 1),
    (115, "Alexander", "Khoo", "AKHOO", "1.515.555.0115", "18-MAY-13", "PU_CLERK", 3100, None, 114, 30, 2),
])

JOBS3 = tbl([("JOB_ID", 10, "l"), ("JOB_TITLE", 24, "l"), ("MIN_SALARY", 10, "r"), ("MAX_SALARY", 10, "r"),
             ("TOTALE_RIGHE", 12, "r")], [
    ("AC_ACCOUNT", "Public Accountant", 4200, 9000, 19),
    ("AC_MGR", "Accounting Manager", 8200, 16000, 19),
    ("AD_ASST", "Administration Assistant", 3000, 6000, 19),
])

JOIN_OUT = tbl([("DEPARTMENT_ID", 13, "r"), ("EMPLOYEE_ID", 11, "r"), ("FIRST_NAME", 10, "l"), ("LAST_NAME", 9, "l"),
                ("EMAIL", 6, "l"), ("PHONE_NUMBER", 14, "l"), ("HIRE_DATE", 9, "l"), ("JOB_ID", 6, "l"),
                ("SALARY", 6, "r"), ("COMMISSION_PCT", 14, "r"), ("MANAGER_ID", 10, "r"),
                ("DEPARTMENT_NAME", 15, "l"), ("MANAGER_ID", 10, "r"), ("LOCATION_ID", 11, "r"),
                ("STIPENDIO_ANNUO", 15, "r")], [
    (90, 101, "Neena", "Yang", "NYANG", "1.515.555.0101", "21-SEP-15", "AD_VP", 17000, None, 100, "Executive", 100,
     1700, 204000),
])

LOCK_SLIDE = """EMPLOYEE_ID
-----------
        101 -- ID bypassed
        102
        103"""

UUID_SLIDE = tbl([("ORDERED", 32, "l"), ("NAME_HASH", 32, "l")], [
    ("01A0E8E0EAF77905AC36727337DF0863", "7A6FAB4AAD8D580DB94DC96326ECAFD3"),
    ("01A0E8E0EAF774B598794591B00B11F8", "71C14E795E2952268BF902F6AB8BF253"),
    ("01A0E8E0EAF77AE1B9C60F09E5D10539", "F0605E638A0D5D3F83AAB922D53E34AD"),
    ("01A0E8E0EAF770C2B96AE74FB6DC19FD", "0FF40BF60259579BA9753E2DFBE1FEA7"),
    ("01A0E8E0EAF77C788E278EAE68E1E447", "5506B60E7A0C5FDFB1A0D97AF8D41A6F"),
])

V5_MANUAL = tbl([("N", 2, "r"), ("UUID_V5", 32, "l")], [
    (1, "7A6FAB4AAD8D580DB94DC96326ECAFD3"),
    (2, "71C14E795E2952268BF902F6AB8BF253"),
    (3, "F0605E638A0D5D3F83AAB922D53E34AD"),
    (4, "0FF40BF60259579BA9753E2DFBE1FEA7"),
    (5, "5506B60E7A0C5FDFB1A0D97AF8D41A6F"),
])

V7_DECODE = tbl([("UUID_TESTO", 36, "l"), ("V", 1, "l"), ("CREATO_UTC", 35, "l")], [
    ("01a0e8e0-eaf7-7905-ac36-727337df0863", "7", "28-SEP-26 04.37.29.463000000 PM UTC"),
])

IDX_OUT = tbl([("CHIAVE", 21, "l"), ("FOGLIE", 6, "r"), ("PCT", 3, "r"), ("RIEMPIMENTO", 11, "l")], [
    ("IDENTITY (sequenza)", 374, 100, "██████████"),
    ("UUID v7, 1 riga/ms", 676, 100, "██████████"),
    ("UUID v4 (casuale)", 985, 69, "██████▉"),
    ("UUID v7, 5 righe/ms", 1154, 59, "█████▉"),
    ("UUID v7, 100 righe/ms", 1328, 51, "█████▏"),
    ("UUID v7, 25 righe/ms", 1333, 51, "█████▏"),
])

BAR_SLIDE = tbl([("SALARY", 10, "r"), ("MAX_100", 10, "l"), ("MAX_24000", 10, "l"), ("MAX_24000_20_CHARS", 20, "l")], [
    (24000, "██████████", "██████████", "####################"),
    (17000, "██████████", "███████", "##############"),
    (17000, "██████████", "███████", "##############"),
    (9000, "██████████", "███▊", "########"),
    (6000, "██████████", "██▌", "#####"),
    (4800, "██████████", "██", "####"),
    (4800, "██████████", "██", "####"),
]) + "\n..."

SHARE_OUT = tbl([("DEPARTMENT_NAME", 18, "l"), ("PCT", 5, "r"), ("QUOTA", 20, "l")], [
    ("Sales", "44.5", "████████▉"),
    ("Shipping", "22.9", "████▋"),
    ("Executive", "8.5", "█▊"),
    ("Finance", "7.5", "█▌"),
    ("IT", "4.2", "▉"),
    ("Purchasing", "3.6", "▊"),
    ("Accounting", "3", "▋"),
    ("Marketing", "2.8", "▌"),
    ("Public Relations", "1.5", "▎"),
    ("Human Resources", ".9", "▏"),
    ("Administration", ".6", "▏"),
])

HIST_OUT = tbl([("ANNO", 4, "r"), ("N", 3, "r"), ("GRAFICO", 30, "l")], [
    (2011, 1, "#"), (2012, 7, "#######"), (2013, 6, "######"), (2014, 10, "##########"),
    (2015, 29, "##############################"), (2016, 24, "#########################"),
    (2017, 19, "####################"), (2018, 11, "###########"),
])

HOP_ROWS = [("01-JUL-2009", 1), ("01-JAN-2010", 1), ("01-JUL-2010", 5), ("01-JAN-2011", 8), ("01-JUL-2011", 10),
            ("01-JAN-2012", 13), ("01-JUL-2012", 16), ("01-JAN-2013", 16), ("01-JUL-2013", 27),
            ("01-JAN-2014", 39), ("01-JUL-2014", 48), ("01-JAN-2015", 53), ("01-JUL-2015", 51),
            ("01-JAN-2016", 43), ("01-JUL-2016", 38), ("01-JAN-2017", 30), ("01-JUL-2017", 18),
            ("01-JAN-2018", 11)]
HOP_BAR = tbl([("WINDOW_START", 12, "l"), ("N", 3, "r"), ("GRAFICO", 30, "l")],
              [(d, n, "#" * int(n / 53 * 30 + 0.5)) for d, n in HOP_ROWS])

MACRO_SLIDE = tbl([("DEPARTMENT_ID", 13, "r"), ("DEPARTMENT_NAME", 30, "l"), ("MANAGER_ID", 10, "r"),
                   ("LOCATION_ID", 11, "r"), ("EMP#", 10, "r")], [
    (30, "Purchasing", 114, 1700, 4),
    (20, "Marketing", 201, 1800, 1),
    (10, "Administration", 200, 1700, "<null>"),
])

NAMES_OUT = """FORMATTED_NAME(FIRST_NAME,LAST_NAME)
----------------------------------------------
Errazuriz, Alberto
Gietz, William
Martinez, Michael
Ozer, Lisa
Venzl, Timothy
Zlotkey, Eleni"""

PLAN_OUT = """----------------------------------------
| Id  | Operation        | Name        |
----------------------------------------
|   0 | SELECT STATEMENT |             |
|*  1 |  INDEX FULL SCAN | EMP_NAME_IX |
----------------------------------------

Predicate Information (identified by operation id):
---------------------------------------------------
   1 - filter(("LAST_NAME" LIKE '%z%' COLLATE "BINARY_CI")=TRUE)"""

TOPN_OUT = tbl([("JOB_ID", 10, "l"), ("JOB_TITLE", 29, "l"), ("MIN_SALARY", 10, "r"), ("MAX_SALARY", 10, "r")], [
    ("AD_PRES", "President", 20080, 40000),
    ("AD_VP", "Administration Vice President", 15000, 30000),
])

ANNUO_OUT = tbl([("LAST_NAME", 9, "l"), ("SALARY", 6, "r"), ("COMMISSION_PCT", 14, "r"), ("ANNUO", 6, "r")], [
    ("Zlotkey", 10500, ".2", 151200), ("Marvins", 7200, ".1", 95040), ("Lee", 6800, ".1", 89760),
    ("Ande", 6400, ".1", 84480), ("Banda", 6200, ".1", 81840),
])

WITH_OUT = tbl([("DEPARTMENT_ID", 13, "r"), ("EMP#", 10, "r")], [
    (50, 13), (80, 12), (60, 2), (30, 1), (100, 1), (None, 1),
])

TUMBLE_SLIDE = tbl([("WINDOW_START", 20, "l"), ("COUNT(*)", 10, "r")], [
    ("01-JAN-2010 00:00:00", 1), ("01-JAN-2012 00:00:00", 13), ("01-JAN-2014 00:00:00", 39),
    ("01-JAN-2016 00:00:00", 43), ("01-JAN-2018 00:00:00", 11),
])
HOP_SLIDE = tbl([("WINDOW_START", 20, "l"), ("COUNT(*)", 10, "r")], [
    ("01-JUL-2009 00:00:00", 1), ("01-JAN-2010 00:00:00", 1), ("01-JUL-2010 00:00:00", 5),
    ("01-JAN-2011 00:00:00", 8),
]) + "\n..."
HOP_FULL = tbl([("WINDOW_START", 20, "l"), ("COUNT(*)", 10, "r")], [(d + " 00:00:00", n) for d, n in HOP_ROWS])
CUM_SLIDE = tbl([("WINDOW_START", 20, "l"), ("WINDOW_END", 20, "l"), ("COUNT(*)", 10, "r")], [
    ("01-JAN-2010 00:00:00", "01-JAN-2012 00:00:00", 1), ("01-JAN-2010 00:00:00", "01-JAN-2014 00:00:00", 14),
    ("01-JAN-2010 00:00:00", "01-JAN-2016 00:00:00", 53), ("01-JAN-2010 00:00:00", "01-JAN-2018 00:00:00", 96),
    ("01-JAN-2010 00:00:00", "01-JAN-2020 00:00:00", 107),
])
SES_SLIDE = tbl([("WINDOW_START", 20, "l"), ("WINDOW_END", 20, "l"), ("COUNT(*)", 10, "r")], [
    ("13-JAN-2011 00:00:00", "21-APR-2020 00:00:00", 107),
])

V_COLS = [("WINDOW_START", 17, "l"), ("WINDOW_END", 17, "l"), ("ORDINI", 6, "r"), ("TOTALE", 6, "r")]
V_TUMBLE = tbl(V_COLS, [
    ("26-OCT-2026 08:00", "26-OCT-2026 09:00", 3, 245), ("26-OCT-2026 09:00", "26-OCT-2026 10:00", 3, 295),
    ("26-OCT-2026 10:00", "26-OCT-2026 11:00", 1, 150), ("26-OCT-2026 11:00", "26-OCT-2026 12:00", 2, 165),
    ("26-OCT-2026 12:00", "26-OCT-2026 13:00", 1, 300),
])
V_TUMBLE_NEG = tbl([("WINDOW_START", 17, "l"), ("NEGOZIO", 7, "l"), ("ORDINI", 6, "r"), ("TOTALE", 6, "r")], [
    ("26-OCT-2026 08:00", "Milano", 2, 165), ("26-OCT-2026 08:00", "Roma", 1, 80),
    ("26-OCT-2026 09:00", "Milano", 1, 60), ("26-OCT-2026 09:00", "Roma", 2, 235),
    ("26-OCT-2026 10:00", "Milano", 1, 150), ("26-OCT-2026 11:00", "Milano", 1, 75),
    ("26-OCT-2026 11:00", "Roma", 1, 90), ("26-OCT-2026 12:00", "Roma", 1, 300),
])
V_HOP = tbl(V_COLS, [
    ("26-OCT-2026 07:00", "26-OCT-2026 09:00", 3, 245), ("26-OCT-2026 08:00", "26-OCT-2026 10:00", 6, 540),
    ("26-OCT-2026 09:00", "26-OCT-2026 11:00", 4, 445), ("26-OCT-2026 10:00", "26-OCT-2026 12:00", 3, 315),
    ("26-OCT-2026 11:00", "26-OCT-2026 13:00", 3, 465), ("26-OCT-2026 12:00", "26-OCT-2026 14:00", 1, 300),
])
V_CUM = tbl([("WINDOW_START", 17, "l"), ("WINDOW_END", 17, "l"), ("ORDINI", 6, "r"), ("PROGRESSIVO", 11, "r")], [
    ("26-OCT-2026 00:00", "26-OCT-2026 09:00", 3, 245), ("26-OCT-2026 00:00", "26-OCT-2026 10:00", 6, 540),
    ("26-OCT-2026 00:00", "26-OCT-2026 11:00", 7, 690), ("26-OCT-2026 00:00", "26-OCT-2026 12:00", 9, 855),
    ("26-OCT-2026 00:00", "26-OCT-2026 13:00", 10, 1155), ("26-OCT-2026 00:00", "26-OCT-2026 14:00", 10, 1155),
]) + "\n...   (una riga per ogni ora fino a 27-OCT-2026 00:00, sempre 10 e 1155: 16 righe in tutto)"
V_SES = tbl(V_COLS, [
    ("26-OCT-2026 08:05", "26-OCT-2026 10:08", 6, 540), ("26-OCT-2026 10:55", "26-OCT-2026 12:00", 3, 315),
    ("26-OCT-2026 12:45", "26-OCT-2026 13:15", 1, 300),
])
V_SES_NEG = tbl([("NEGOZIO", 7, "l"), ("WINDOW_START", 17, "l"), ("WINDOW_END", 17, "l"), ("ORDINI", 6, "r"),
                 ("TOTALE", 6, "r")], [
    ("Milano", "26-OCT-2026 08:05", "26-OCT-2026 08:35", 1, 120),
    ("Milano", "26-OCT-2026 08:48", "26-OCT-2026 09:42", 2, 105),
    ("Milano", "26-OCT-2026 10:55", "26-OCT-2026 11:25", 1, 150),
    ("Milano", "26-OCT-2026 11:30", "26-OCT-2026 12:00", 1, 75),
    ("Roma", "26-OCT-2026 08:20", "26-OCT-2026 08:50", 1, 80),
    ("Roma", "26-OCT-2026 09:10", "26-OCT-2026 10:08", 2, 235),
    ("Roma", "26-OCT-2026 11:05", "26-OCT-2026 11:35", 1, 90),
    ("Roma", "26-OCT-2026 12:45", "26-OCT-2026 13:15", 1, 300),
])
TB_EQ = tbl([("WINDOW_START", 11, "l"), ("COUNT(*)", 8, "r")], [
    ("01-JAN-2010", 1), ("01-JAN-2012", 13), ("01-JAN-2014", 39), ("01-JAN-2016", 43), ("01-JAN-2018", 11),
])

# ---------------------------------------------------------------- sections
S = []

# ---- SELECT *
S.append(section("select-star", "SELECT *, &lt;espressione&gt;", "SELECT * insieme ad altre colonne",
    "L'asterisco senza prefisso ora si può mescolare con colonne, espressioni e pseudocolonne, in qualsiasi "
    "posizione della lista. Prima bisognava dare un alias alla tabella e scrivere <code>t.*</code>.",
    compare(
        err("""select rowid, upper(region_name) upper_name, *
from   hr.regions;
ORA-00936: missing expression

select *, upper(region_name)
from   hr.regions;
ORA-00923: FROM keyword not found where expected""", "Asterisco non qualificato")
        + code("""-- unica strada: alias e asterisco qualificato
select rowid, upper(region_name) upper_name, r.*
from   hr.regions r;""", "old"),
        code("""select rowid, upper ( region_name ) upper_name, ⟦*⟧
from   hr.regions;""", "new")
        + out(REGIONS_SLIDE, "slide"))
    + p("L'asterisco viene espanso nel punto in cui lo scrivi: prima le espressioni alla sua sinistra, poi le colonne "
        "della tabella nel loro ordine, poi quelle a destra. Secondo la documentazione può stare ovunque nella lista, "
        "anche più di una volta, e continua a escludere pseudocolonne e colonne <code>INVISIBLE</code>.")
    + p('<span class="aside">Nello schema HR pubblicato oggi su GitHub le regioni sono cinque, con ID da 10 a 50: '
        "la slide usa una versione precedente della tabella.</span>")
    + h3("Esempi")
    + '<h4>Funzioni analitiche accanto a tutte le colonne</h4>'
    + p("È lo schema classico del top-N per gruppo e della deduplica. Con <code>QUALIFY</code>, già disponibile "
        "prima della 23.26.4, il filtro sul numero di riga sta nella stessa query.")
    + code("""-- i due stipendi più alti dei reparti 20 e 30
select ⟦*,⟧ row_number() over (partition by department_id order by salary desc) rn
from   hr.employees
where  department_id in (20, 30)
qualify rn <= 2
order  by department_id, rn;""", "new")
    + out(TOP2, "run", "Risultato (con e.* su 23.26.3)")
    + '<h4>Una pagina di risultati con il totale</h4>'
    + p("Le funzioni analitiche vengono calcolate prima di <code>FETCH FIRST</code>: ogni riga della pagina riporta "
        "il numero totale di righe (19 job), senza una seconda query per contarle.")
    + code("""select ⟦*,⟧ count(*) over () totale_righe
from   hr.jobs
order  by job_id
fetch  first 3 rows only;""", "new")
    + out(JOBS3, "run", "Risultato (con j.* su 23.26.3)")
    + '<h4>Copia o archivio con una colonna in più</h4>'
    + p("Le colonne di <code>*</code> arrivano nell'ordine della tabella: la colonna aggiunta va in coda, nella stessa "
        "posizione che ha nella tabella di destinazione.")
    + code("""create table emp_snapshot as
  select ⟦*,⟧ sysdate as snapshot_at
  from   hr.employees;

insert into emp_snapshot
  select ⟦*,⟧ sysdate
  from   hr.employees
  where  department_id = 50;""", "new")
    + '<h4>Colonne invisibili e pseudocolonne</h4>'
    + p("<code>*</code> non restituisce le colonne <code>INVISIBLE</code> (12c) né le pseudocolonne. Ora le aggiungi "
        "senza riscrivere l'elenco delle colonne.")
    + code("""create table clienti (
  id    number,
  nome  varchar2(30),
  nota  varchar2(30) invisible
);

-- ID, NOME
select * from clienti;
-- ID, NOME, NOTA
select ⟦*,⟧ nota from clienti;
-- SCN dell'ultima modifica e indirizzo fisico della riga
select ora_rowscn, rowid, ⟦*⟧ from clienti;""", "new")
    + '<h4>Join</h4>'
    + p("In una join <code>*</code> restituisce le colonne di tutte le tabelle. Con <code>USING</code> la colonna di "
        "join compare una volta sola, in testa; <code>MANAGER_ID</code> esiste in entrambe le tabelle e compare due volte.")
    + code("""select ⟦*,⟧ e.salary * 12 stipendio_annuo
from   hr.employees e
join   hr.departments d using (department_id)
where  employee_id = 101;""", "new")
    + out(JOIN_OUT, "exp")
    + warn([
        "<strong>Nomi duplicati.</strong> Una query di primo livello li accetta. Una subquery che usa la colonna "
        "duplicata fallisce con ORA-00918, una <code>CREATE TABLE … AS SELECT</code> o una vista con ORA-00957.",
        "<strong>Codice di produzione.</strong> Con <code>*</code> l'elenco delle colonne dipende dalla tabella: se la "
        "tabella cambia, cambia il risultato. Ottimo per query esplorative, debug e script; nelle viste e nel codice "
        "applicativo conviene elencare le colonne.",
    ])
    + err("""select salary from (select e.*, salary * 12 salary from hr.employees e);
ORA-00918: SALARY: column ambiguously specified

create table emp_copy as select e.*, salary * 12 salary from hr.employees e;
ORA-00957: duplicate column name""", "Nomi duplicati (stesse regole con *)")
))

# ---- FOR UPDATE
S.append(section("for-update", "FETCH FIRST … FOR UPDATE [SKIP LOCKED]", "Top-N con FOR UPDATE e SKIP LOCKED",
    "Una query top-N ora può bloccare le righe che restituisce. Con <code>SKIP LOCKED</code> le righe già bloccate "
    "da altre transazioni vengono saltate e non contano nel limite: la query continua finché trova N righe libere.",
    '<div class="fig-pair">'
    + f'<figure class="fig"><div class="fig-scroll">{svg_lock("rownum")}</div></figure>'
    + f'<figure class="fig"><div class="fig-scroll">{svg_lock("fetch")}</div></figure>'
    + '</div><p class="figcap">La sessione 1 tiene bloccato il dipendente 100. La sessione 2 chiede tre righe: con '
      "<code>ROWNUM</code> la riga bloccata occupa uno dei tre posti e ne arrivano due; con <code>FETCH FIRST</code> "
      "non conta e ne arrivano tre.</p>"
    + h3("L'esempio della slide")
    + compare(
        code("""-- sessione 1: blocca il dipendente 100, senza commit
update hr.employees
set    hire_date = sysdate
where  employee_id = 100;""", "any", "Sessione 1"),
        code("""-- sessione 2: blocca i primi 3 ID liberi
select employee_id
from   hr.employees
order  by employee_id
⟦fetch  first 3 rows only⟧
⟦for    update skip locked⟧;""", "new", "Sessione 2")
        + out(LOCK_SLIDE, "slide"),
        "Sessione 1", "Sessione 2")
    + h3("Prima della 23.26.4")
    + p("La combinazione era vietata. <code>FETCH FIRST</code> viene riscritto come vista interna (lo mostra "
        "<code>DBMS_UTILITY.EXPAND_SQL_TEXT</code>) e <code>FOR UPDATE</code> su una vista di quel tipo non era ammesso.")
    + err("""select employee_id from hr.employees
order by employee_id fetch first 3 rows only
for update skip locked;
ORA-02014: cannot select FOR UPDATE from view with DISTINCT, GROUP BY, etc.""", "Errore")
    + out("""SELECT "A1"."EMPLOYEE_ID" "EMPLOYEE_ID"
FROM  (SELECT "A2"."EMPLOYEE_ID" "EMPLOYEE_ID"
       FROM "HR"."EMPLOYEES" "A2"
       ORDER BY "A2"."EMPLOYEE_ID") "A1"
WHERE ROWNUM<=3""", "run", "EXPAND_SQL_TEXT (riformattato)")
    + p("I due workaround più diffusi danno meno righe del richiesto, sempre con la sessione 1 che blocca il 100:")
    + compare(
        code("""select employee_id from hr.employees
where  rownum <= 3
for update skip locked;""", "old", "ROWNUM")
        + out("""EMPLOYEE_ID
-----------
        101
        102""", "run"),
        code("""select employee_id from hr.employees
where  employee_id in (select employee_id
                       from   hr.employees
                       order  by employee_id
                       fetch  first 3 rows only)
for update skip locked;""", "old", "Subquery")
        + out("""EMPLOYEE_ID
-----------
        101
        102""", "run"),
        "ROWNUM: conta il 100 e poi lo salta", "Subquery: sceglie 100, 101, 102 ignorando i lock")
    + p("La soluzione corretta richiedeva PL/SQL: un cursore <code>FOR UPDATE SKIP LOCKED</code> letto con "
        "<code>BULK COLLECT … LIMIT</code>. Funziona perché con <code>SKIP LOCKED</code> le righe vengono bloccate "
        "al momento del <code>FETCH</code>. L'ho verificato con una funzione in transazione autonoma che tenta "
        "<code>SELECT … FOR UPDATE NOWAIT</code>: dopo il fetch sono bloccate solo 101, 102 e 103. Senza "
        "<code>SKIP LOCKED</code>, invece, un cursore <code>FOR UPDATE</code> blocca tutte le righe già all'<code>OPEN</code>.")
    + code("""declare
  cursor c is
    select employee_id from hr.employees
    order  by employee_id
    for    update skip locked;
  type t_ids is table of hr.employees.employee_id%type;
  l_ids t_ids;
begin
  open c;
  fetch c bulk collect into l_ids limit 3;
  -- elaborazione di l_ids ...
  close c;
  commit;
end;
/""", "old", "Workaround corretto")
    + out("""preso: 101
preso: 102
preso: 103
101 -> BLOCCATA | 103 -> BLOCCATA | 104 -> libera | 150 -> libera

-- cursore FOR UPDATE senza SKIP LOCKED, subito dopo l'OPEN:
104 -> BLOCCATA | 110 -> BLOCCATA""", "run", "Verifica dei lock")
    + h3("Esempio completo: una coda di lavori")
    + p("Il caso d'uso tipico: più processi prelevano lavori dalla stessa tabella senza aspettarsi a vicenda e senza "
        "prendere due volte lo stesso lavoro.")
    + code("""create table jobs (
  job_id     number generated always as identity primary key,
  payload    varchar2(100) not null,
  stato      varchar2(10) default 'NUOVO' not null,
  creato_il  timestamp default systimestamp not null,
  preso_da   varchar2(30),
  finito_il  timestamp
);
create index jobs_coda_ix on jobs (stato, creato_il);

insert into jobs (payload)
select 'job ' || level connect by level <= 20;
commit;""", "any", "Tabella")
    + code("""declare
  cursor c_lotto is
    select job_id, payload
    from   jobs
    where  stato = 'NUOVO'
    order  by creato_il, job_id
    ⟦fetch  first 5 rows only⟧
    ⟦for    update skip locked⟧;
begin
  for j in c_lotto loop
    -- elaborazione di j.payload ...
    update jobs
    set    stato     = 'FATTO',
           preso_da  = sys_context('userenv', 'sid'),
           finito_il = systimestamp
    where  job_id = j.job_id;
  end loop;
  -- il COMMIT chiude il lotto e rilascia i lock
  commit;
end;
/""", "new", "Worker")
    + p("Due worker avviati insieme dovrebbero ricevere lotti diversi (1–5 e 6–10): è il comportamento descritto "
        "dalla documentazione, non l'ho potuto eseguire senza la 23.26.4.")
    + h3("Le quattro varianti di FOR UPDATE")
    + '<div class="tbl"><table><thead><tr><th>Clausola</th><th>Se una riga è bloccata da un altro</th></tr></thead><tbody>'
      "<tr><td><code>for update</code></td><td>Aspetta che si liberi. Ordine rispettato, nessun salto.</td></tr>"
      "<tr><td><code>for update nowait</code></td><td>Errore immediato ORA-00054.</td></tr>"
      "<tr><td><code>for update wait 5</code></td><td>Aspetta fino a 5 secondi, poi errore.</td></tr>"
      "<tr><td><code>for update skip locked</code></td><td>Salta la riga. Con <code>FETCH FIRST</code> la riga saltata non conta nel limite.</td></tr>"
      "</tbody></table></div>"
    + warn([
        "<strong>Senza ORDER BY</strong> le prime N righe sono righe qualsiasi.",
        "<strong>SKIP LOCKED rinuncia all'ordine rigoroso:</strong> un worker può finire il job 6 prima che un altro "
        "finisca il 5. Per una coda va bene, per elaborazioni strettamente sequenziali no.",
        "<strong>Indice.</strong> Serve un indice che porti subito alle righe da prelevare (qui "
        "<code>stato, creato_il</code>); senza, ogni worker legge tutta la tabella.",
        "<strong>Transazioni brevi.</strong> I lock restano fino a <code>COMMIT</code> o <code>ROLLBACK</code>.",
        "<strong>Row limiting partizionato.</strong> La documentazione garantisce che le righe bloccate non contano "
        "nel limite per il row limiting non partizionato, cioè <code>FETCH FIRST</code> senza <code>PARTITION BY</code>.",
    ])
))

# ---- UUID
S.append(section("uuid", "UUID ( 7 ) · UUID ( 5, namespace, nome )", "UUID versione 7 e versione 5",
    "<code>UUID()</code> esiste dalla 23.9 e genera UUID casuali, versione 4, come <code>RAW(16)</code>. Ora genera "
    "anche la versione 7, che comincia con un timestamp ed è quindi ordinata nel tempo, e la versione 5, ricavata "
    "in modo deterministico da un namespace e da un nome.",
    fig(svg_uuid(), "Tre UUID reali, carattere per carattere. Nella v7 i primi 12 caratteri sono il timestamp; nella "
        "v5 tutto viene dall'hash SHA-1; nella v4 tutto è casuale. Il 13° carattere è sempre la versione, il 17° "
        "la variante.")
    + h3("L'esempio della slide")
    + code("""select uuid ( ⟦7⟧ ) ordered,
       uuid ( ⟦5, 'url', 'test.com/' || level⟧ ) name_hash
connect by level <= 5;""", "new")
    + out(UUID_SLIDE, "slide")
    + h3("Come si legge")
    + ul([
        "<strong>ORDERED (v7).</strong> <code>01A0E8E0EAF7</code> sono 1.790.613.449.463 millisecondi dal 1° gennaio "
        "1970, cioè il 28 settembre 2026 alle 16:37:29,463 UTC: il momento in cui è stata preparata la slide.",
        "<strong>Stesso millisecondo, ordine casuale.</strong> Le cinque righe hanno lo stesso prefisso perché sono "
        "nate nello stesso millisecondo. Le cifre successive (905, 4B5, AE1, 0C2, C78) non crescono: l'ordine segue "
        "il tempo al millisecondo, dentro il millisecondo è casuale.",
        "<strong>NAME_HASH (v5).</strong> I cinque valori coincidono con quelli di Python "
        "<code>uuid.uuid5(uuid.NAMESPACE_URL, 'test.com/1')</code> … <code>'test.com/5'</code>: li ho confrontati "
        "tutti. <code>'url'</code> è uno dei namespace standard; la documentazione cita DNS, URL, OID e X500.",
    ])
    + code("""import uuid
uuid.uuid5(uuid.NAMESPACE_URL, 'test.com/1')
# UUID('7a6fab4a-ad8d-580d-b94d-c96326ecafd3')""", "any", "Python", "py")
    + h3("Prima della 23.26.4")
    + err("""select uuid(7);
ORA-62433: Invalid or unsupported argument to UUID function

select uuid(5, 'url', 'test.com/1');
ORA-00939: too many arguments for function

select is_uuid('7a6fab4a-ad8d-580d-b94d-c96326ecafd3');
FALSE

select uuid_to_raw('7a6fab4a-ad8d-580d-b94d-c96326ecafd3');
ORA-62432: 7a6fab4a-ad8d-580d-b94d-c96326ecafd3 is not a valid UUID value.""", "Su 23.26.3")
    + p("Su 23.26.3 anche le funzioni di supporto (<code>IS_UUID</code>, <code>UUID_TO_RAW</code>, "
        "<code>RAW_TO_UUID</code>) accettano solo la versione 4: un UUID v5 o v7 generato da un'applicazione viene "
        "rifiutato. Nella 23.26.4 <code>IS_UUID</code> riconosce le versioni 4, 5 e 7.")
    + h3("Come funziona la v5, in SQL")
    + p("La v5 è l'hash SHA-1 del namespace seguito dal nome, troncato a 128 bit, con versione e variante "
        "sovrascritte. Questa query ricostruisce i valori della slide senza <code>UUID(5, …)</code>: utile per capire "
        "il meccanismo e per generare le stesse chiavi su release precedenti.")
    + code("""select level n,
       utl_raw.bit_or(
         utl_raw.bit_and(
           utl_raw.substr(
             standard_hash(utl_raw.concat(hextoraw('6BA7B8119DAD11D180B400C04FD430C8'),  -- namespace URL
                                          utl_raw.cast_to_raw('test.com/' || level)), 'SHA1'), 1, 16),
           hextoraw('FFFFFFFFFFFF0FFF3FFFFFFFFFFFFFFF')),      -- azzera versione e variante
         hextoraw('00000000000050008000000000000000')) uuid_v5  -- versione 5, variante RFC
connect by level <= 5;""", "old")
    + out(V5_MANUAL, "run")
    + h3("Esempi")
    + '<h4>Quando è stato creato un UUID v7</h4>'
    + code("""with u as (select hextoraw('01A0E8E0EAF77905AC36727337DF0863') id)
select regexp_replace(lower(rawtohex(id)),
                      '(.{8})(.{4})(.{4})(.{4})(.{12})', '\\1-\\2-\\3-\\4-\\5') uuid_testo,
       substr(rawtohex(id), 13, 1) v,
       timestamp '1970-01-01 00:00:00 UTC'
         + numtodsinterval(to_number(substr(rawtohex(id), 1, 12), 'XXXXXXXXXXXX') / 1000, 'SECOND') creato_utc
from   u;""", "any")
    + out(V7_DECODE, "run")
    + p("Con la 23.26.4 basta sostituire il letterale con <code>uuid(7)</code>. Il <code>REGEXP_REPLACE</code> "
        "formatta qualsiasi valore a 32 cifre, anche quando <code>RAW_TO_UUID</code> non riconosce la versione.")
    + '<h4>Chiave primaria ordinata nel tempo</h4>'
    + code("""create table ordini (
  id       raw(16) primary key,
  cliente  varchar2(30) not null,
  importo  number(10,2) not null
);

insert into ordini (id, cliente, importo) values (⟦uuid ( 7 )⟧, 'ACME', 120);

-- ORDER BY id restituisce l'ordine di inserimento, al millisecondo
select raw_to_uuid(id) id, cliente, importo from ordini order by id;""", "new")
    + p('<span class="aside">Su 23.26.3 la clausola <code>DEFAULT</code> accetta <code>uuid()</code> ma rifiuta '
        "<code>uuid(4)</code> con ORA-00907, anche se <code>select uuid(4)</code> funziona. Prima di scrivere "
        "<code>default uuid(7)</code> verifica che la tua release lo accetti; valorizzare l'ID nell'INSERT funziona "
        "comunque.</span>")
    + '<h4>Chiave stabile per caricamenti ripetibili</h4>'
    + p("La v5 dà sempre lo stesso UUID per lo stesso nome. Ricaricando lo stesso file la chiave non cambia: niente "
        "duplicati e niente tabella di corrispondenza. Un'applicazione che usa <code>uuid5(NAMESPACE_URL, …)</code> "
        "ottiene lo stesso valore.")
    + code("""merge into clienti_dw d
using (select ⟦uuid ( 5, 'url', 'https://crm.example.it/clienti/' || codice )⟧ id,
              codice, nome
       from   stg_clienti) s
on (d.id = s.id)
when matched then
  update set d.nome = s.nome
when not matched then
  insert (id, codice, nome) values (s.id, s.codice, s.nome);""", "new")
    + h3("Misura: cosa succede all'indice di chiave primaria")
    + p("200.000 inserimenti riga per riga in tabelle con chiave primaria <code>RAW(16)</code>, su 23.26.3. La v7 è "
        "emulata con lo stesso layout di bit e con bit casuali dentro il millisecondo, come nella slide. Il ritmo è "
        "in righe per millisecondo sullo stesso indice: 5 righe/ms sono 5.000 righe al secondo. Fonti: statistiche "
        "<code>leaf node splits</code> e <code>INDEX_STATS</code>.")
    + out(IDX_OUT, "run", "Foglie dell'indice e riempimento medio dei blocchi")
    + ul([
        "<strong>Sequenza:</strong> chiavi crescenti e corte, split 90-10, blocchi pieni al 100%. Resta la chiave più "
        "compatta.",
        "<strong>v4:</strong> chiavi sparse, split 50-50, blocchi pieni al 69% circa, il valore tipico degli "
        "inserimenti casuali. Ogni insert può toccare qualsiasi blocco dell'indice: quando l'indice non sta in "
        "memoria diventano letture da disco.",
        "<strong>v7 fino a 2 righe/ms:</strong> le chiavi arrivano in ordine e l'indice si comporta come con una "
        "sequenza: 100% e insert concentrati sul bordo destro.",
        "<strong>v7 da 5 righe/ms in su:</strong> nello stesso millisecondo l'ordine è casuale, il blocco di destra si "
        "divide 50-50 e la metà sinistra non riceve più chiavi. Risultato: blocchi pieni al 51%, peggio di v4.",
        "<strong>Caricamenti massivi:</strong> lo stesso carico a 100 righe/ms con <code>INSERT /*+ APPEND */</code> "
        "(direct-path) produce un indice pieno al 100% (676 foglie contro 1.329), perché l'indice viene aggiornato "
        "in blocco a fine istruzione.",
    ])
    + warn([
        "<strong>Un v7 rivela quando è stato creato.</strong> Chi vede l'ID vede la data e l'ora.",
        "<strong>La v5 è deterministica.</strong> Chiunque conosca namespace e nome la ricalcola: non usarla come "
        "token segreto. Normalizza il nome prima di calcolarla: <code>'Test.com/1'</code> e "
        "<code>'test.com/1'</code> danno UUID diversi, e con caratteri non ASCII conta la codifica dei byte.",
        "<strong>Conserva gli UUID come RAW(16):</strong> 16 byte contro i 36 di <code>VARCHAR2(36)</code>, "
        "confronti più veloci e indici più piccoli. Il formato con i trattini serve solo in visualizzazione.",
        "<strong>PL/SQL.</strong> Su 23.26.3 <code>UUID</code> e <code>RAW_TO_UUID</code> non si possono chiamare "
        "come funzioni PL/SQL (PLS-00201): si usano dentro un'istruzione SQL, per esempio "
        "<code>select raw_to_uuid(uuid()) into l_id;</code>.",
    ])
))

# ---- BAR_CHART
S.append(section("bar-chart", "BAR_CHART ( valore, massimo, minimo, larghezza, simbolo )", "BAR_CHART",
    "Una funzione che restituisce una barra di testo proporzionale a un valore. Serve a vedere una distribuzione "
    "direttamente nel risultato di una query, in SQL*Plus, SQLcl o qualsiasi altro client.",
    code("""BAR_CHART ( valore [, massimo [, minimo [, larghezza [, simbolo ] ] ] ] )""", "new", "Sintassi")
    + '<div class="tbl"><table><thead><tr><th>Parametro</th><th>Predefinito</th><th>Significato</th></tr></thead><tbody>'
      "<tr><td><code>massimo</code></td><td>100</td><td>Valore che riempie tutta la barra. Viene <em>prima</em> del minimo.</td></tr>"
      "<tr><td><code>minimo</code></td><td>0</td><td>Valore che corrisponde alla barra vuota.</td></tr>"
      "<tr><td><code>larghezza</code></td><td>10</td><td>Caratteri della barra piena.</td></tr>"
      "<tr><td><code>simbolo</code></td><td>blocchi Unicode</td><td>Se omesso, la parte frazionaria è disegnata con i "
      "blocchi parziali ▏▎▍▌▋▊▉; con un simbolo scelto, per esempio <code>'#'</code>, la lunghezza viene arrotondata "
      "all'intero.</td></tr>"
      "</tbody></table></div>"
    + p("La lunghezza vale (valore − minimo) ÷ (massimo − minimo) × larghezza. Oltre il massimo la barra resta piena.")
    + h3("L'esempio della slide")
    + code("""select salary,
       ⟦bar_chart ( salary )⟧ max_100,
       ⟦bar_chart ( salary, 24000 )⟧ max_24000,
       ⟦bar_chart ( salary, 24000, 0, 20, '#' )⟧ max_24000_20_chars
from   hr.employees;""", "new")
    + out(BAR_SLIDE, "slide", "Risultato (ricopiato dalla slide)")
    + ul([
        "<strong>MAX_100:</strong> con la scala predefinita 0–100 ogni stipendio supera il massimo, quindi tutte le "
        "barre sono piene. La scala predefinita è pensata per le percentuali.",
        "<strong>MAX_24000:</strong> 9.000 su 24.000 vale 3,75 caratteri: tre blocchi pieni e uno da tre quarti.",
        "<strong>MAX_24000_20_CHARS:</strong> con <code>'#'</code> e larghezza 20, 9.000 vale 7,5 caratteri e diventa "
        "8 <code>#</code>; 17.000 vale 14,2 e diventa 14. Ho riprodotto tutti i conteggi della colonna con "
        "<code>RPAD</code> e <code>ROUND</code>.",
    ])
    + h3("Esempi")
    + '<h4>Percentuali</h4>'
    + p("La quota della spesa per stipendi di ogni reparto. La scala resta 0–100; la larghezza 20 dà più dettaglio.")
    + code("""select department_name,
       round(100 * ratio_to_report(sum(salary)) over (), 1) pct,
       ⟦bar_chart ( round(100 * ratio_to_report(sum(salary)) over (), 1), 100, 0, 20 )⟧ quota
from   hr.employees
join   hr.departments using (department_id)
group  by department_name
order  by pct desc;""", "new")
    + out(SHARE_OUT, "exp")
    + '<h4>Istogramma con scala automatica</h4>'
    + p("Passando come massimo <code>MAX(...) OVER ()</code>, la riga più alta riempie sempre la barra, qualunque "
        "siano i valori.")
    + code("""select extract(year from hire_date) anno,
       count(*) n,
       ⟦bar_chart ( count(*), max(count(*)) over (), 0, 30, '#' )⟧ grafico
from   hr.employees
group  by extract(year from hire_date)
order  by anno;""", "new")
    + out(HIST_OUT, "exp")
    + '<h4>Insieme alle finestre temporali</h4>'
    + p("Assunzioni nei due anni successivi, calcolate ogni sei mesi con <code>HOP</code> (vedi più sotto): la "
        "colonna di barre diventa un piccolo grafico dell'andamento.")
    + code("""select window_start,
       count(*) n,
       ⟦bar_chart ( count(*), max(count(*)) over (), 0, 30, '#' )⟧ grafico
from   ⟦hop ( hr.employees, columns ( hire_date ), interval '6' month, interval '2' year )⟧
group  by window_start
order  by window_start;""", "new")
    + out(HOP_BAR, "exp")
    + '<h4>Prima della 23.26.4</h4>'
    + p("Le stesse barre si ottengono con <code>RPAD</code> per un simbolo ASCII e con <code>UNISTR</code> per i "
        "blocchi Unicode. È anche il modo più chiaro di spiegare cosa calcola la funzione.")
    + code("""-- come bar_chart(salary, 24000, 0, 20, '#')
select salary,
       rpad('#', round((salary - 0) / (24000 - 0) * 20), '#') barra
from   hr.employees;

-- come bar_chart(salary, 24000): blocchi pieni + un blocco parziale in ottavi
with d as (
  select salary, least(greatest((salary - 0) / (24000 - 0), 0), 1) * 10 x
  from   hr.employees
)
select salary,
       replace(rpad(' ', trunc(x)), ' ', unistr('\\2588'))
       || substr(unistr(' \\258F\\258E\\258D\\258C\\258B\\258A\\2589'), round(mod(x, 1) * 8) + 1, 1) barra
from   d;""", "old")
    + warn([
        "<strong>Ordine dei parametri.</strong> Il secondo parametro è il massimo, il terzo il minimo.",
        "<strong>Scala predefinita.</strong> 0–100 va bene per le percentuali; per altri valori passa sempre il "
        "massimo, o calcolalo con <code>MAX() OVER ()</code>.",
        "<strong>Caratteri.</strong> I blocchi Unicode richiedono un client e un font che li mostrino; se vedi simboli "
        "strani usa un simbolo ASCII come <code>'#'</code>.",
        "<strong>È per l'esplorazione.</strong> Utile in aula, nel debug e nei report testuali; non sostituisce un "
        "grafico.",
    ])
))

# ---- MACRO
S.append(section("macro", "CREATE MACRO", "CREATE MACRO",
    "Le SQL macro esistono dalla 19c (di tabella) e dalla 21c (scalari), ma si scrivevano come funzioni PL/SQL che "
    "restituiscono il testo SQL dentro una stringa. <code>CREATE MACRO</code> permette di scrivere direttamente il SQL: "
    "una macro scalare è un'espressione riutilizzabile, una macro di tabella è una vista con parametri.",
    h3("Macro di tabella: prima e ora")
    + compare(
        code("""create or replace function dept_totals ( hired_after date )
  return varchar2 sql_macro(table) is
begin
  return q'[select department_id, count(*) emp#
            from   hr.employees
            where  hire_date > hired_after
            group  by all]';
end;
/

create or replace function get_3_rows ( table_name dbms_tf.table_t )
  return varchar2 sql_macro(table) is
begin
  return 'select * from table_name fetch first 3 rows only';
end;
/""", "old"),
        code("""/* Parameterized view */
⟦create or replace macro⟧ dept_totals ( hired_after date ) ⟦is⟧
  select department_id, count(*) emp# from hr.employees
  where  hire_date > hired_after group by all;

/* Polymorphic view - pass table name as parameter */
⟦create or replace macro⟧ get_3_rows ( table_name ⟦table⟧ ) ⟦is⟧
  select * from table_name fetch first 3 rows only;""", "new"))
    + code("""select * from get_3_rows ( hr.departments )
left join dept_totals ( date '2015-01-01' ) using ( department_id );""", "any", "Uso (identico nelle due forme)")
    + out(MACRO_SLIDE, "slide")
    + p("<code>dept_totals</code> è una vista con un parametro: conta, per reparto, gli assunti dopo una data. "
        "<code>get_3_rows</code> è polimorfica: accetta una tabella qualsiasi tramite il tipo <code>TABLE</code>, che "
        "prende il posto di <code>DBMS_TF.TABLE_T</code>. Si combinano in join come tabelle. Con le macro in forma "
        "PL/SQL su 23.26.3 la stessa query dà lo stesso risultato.")
    + h3("Macro scalari")
    + code("""/* Scalar macro to format the name */
⟦create or replace macro⟧ formatted_name ( given varchar2, family varchar2 ) ⟦is⟧
family || ', ' || given;

/* Does the string contain Z or z? */
-- Parentheses => predicate use in WHERE
⟦create or replace macro⟧ contains_z ( str varchar2 ) ⟦is⟧
( str like '%z%' collate binary_ci );

select formatted_name ( first_name, last_name ) from hr.employees
where  contains_z ( last_name );""", "new")
    + out(NAMES_OUT, "run", "Risultato (macro in forma PL/SQL, ordinato)")
    + p("Il corpo di <code>contains_z</code> è una condizione. Tra parentesi diventa un'espressione booleana (il tipo "
        "<code>BOOLEAN</code> di 23ai) e la macro si usa direttamente nella <code>WHERE</code>, come dice il commento "
        "della slide. Nel piano d'esecuzione la macro non c'è più, c'è il suo testo:")
    + out(PLAN_OUT, "run", "DBMS_XPLAN")
    + p("Nessuna chiamata di funzione: niente passaggi tra SQL e PL/SQL a ogni riga, e l'ottimizzatore lavora "
        "sull'espressione vera (qui sceglie la scansione dell'indice sui nomi).")
    + h3("Cosa cambia rispetto alla funzione SQL_MACRO")
    + ul([
        "<strong>Niente PL/SQL e niente stringhe.</strong> Spariscono <code>return varchar2</code>, "
        "<code>begin … end</code>, gli apici raddoppiati e <code>q'[…]'</code>; l'editor evidenzia e completa il SQL.",
        "<strong>Gli errori di sintassi emergono subito.</strong> Il corpo fa parte dell'istruzione, quindi un errore "
        "fa fallire il <code>CREATE</code>. Con la funzione classica il testo è una stringa: la funzione viene creata "
        "senza errori e il problema emerge solo quando qualcuno la usa.",
        "<strong>Macro nella clausola WITH.</strong> Dalla 23.26.4 si possono usare dentro la <code>WITH</code>; "
        "prima l'errore era ORA-64630 (fonte: blog Oracle sulle viste con parametri).",
    ])
    + err("""create or replace function macro_rotta return varchar2 sql_macro(table) is
begin
  return 'selec * from dual';
end;
/
Function created.

select * from macro_rotta();
ORA-64626: invalid SQL text returned from SQL macro:
ORA-00907: missing right parenthesis

with x as (select * from dept_totals(date '2017-01-01'))
select * from x;
ORA-64630: unsupported use of SQL macro: use of SQL macro inside WITH clause is not supported""",
        "La forma PL/SQL su 23.26.3")
    + h3("Altri esempi")
    + '<h4>Primi N di una tabella qualsiasi</h4>'
    + code("""⟦create or replace macro⟧ top_n ( tab ⟦table⟧, n number ) ⟦is⟧
  select * from tab fetch first n rows only;

select * from top_n ( hr.jobs, 2 );""", "new")
    + out(TOPN_OUT, "run", "Risultato (forma PL/SQL)")
    + '<h4>Regole di business come espressioni</h4>'
    + code("""⟦create or replace macro⟧ stipendio_annuo ( sal number, comm number ) ⟦is⟧
  sal * 12 * ( 1 + nvl ( comm, 0 ) );

⟦create or replace macro⟧ tra ( d date, da date, a date ) ⟦is⟧
  ( d >= da and d < a );

select last_name, salary, commission_pct,
       stipendio_annuo ( salary, commission_pct ) annuo
from   hr.employees
where  tra ( hire_date, date '2018-01-01', date '2019-01-01' )
order  by annuo desc
fetch  first 5 rows only;""", "new")
    + out(ANNUO_OUT, "run", "Risultato (forma PL/SQL)")
    + '<h4>Macro dentro la WITH</h4>'
    + code("""with recenti as (
  select * from ⟦dept_totals ( date '2017-01-01' )⟧
)
select * from recenti
order  by emp# desc, department_id;""", "new")
    + out(WITH_OUT, "exp")
    + warn([
        "<strong>Non dare ai parametri il nome di una colonna.</strong> Con la forma PL/SQL (verificato su 23.26.3) una "
        "macro con parametro <code>department_id</code> e filtro <code>where department_id = department_id</code> "
        "restituisce 106 righe invece di 45: il confronto diventa colonna = colonna. Usa nomi distinti, come fa la "
        "slide (<code>hired_after</code>, <code>given</code>, <code>family</code>).",
        "<strong>FETCH FIRST senza ORDER BY.</strong> <code>get_3_rows</code> restituisce tre righe qualsiasi: nella "
        "slide escono i reparti 30, 20 e 10. Internamente diventa <code>WHERE ROWNUM &lt;= 3</code>. Se l'ordine conta, "
        "mettilo nella macro.",
        "<strong>Dove si usano.</strong> Una macro di tabella va nella <code>FROM</code>; una macro scalare va dove "
        "va un'espressione (<code>SELECT</code>, <code>WHERE</code>, <code>ORDER BY</code>), non nella <code>FROM</code>.",
    ])
))

# ---- WINDOWS
S.append(section("finestre", "TUMBLE · HOP · CUMULATE · SESSIONS", "Finestre temporali nella FROM",
    "Quattro funzioni da usare nella <code>FROM</code>: assegnano ogni riga a una o più finestre di tempo e "
    "aggiungono le colonne <code>WINDOW_START</code> e <code>WINDOW_END</code>, su cui poi si aggrega. Il modello è "
    "quello delle window table function di Apache Flink, applicato ai dati delle tabelle.",
    fig(svg_windows(), "Dieci ordini di una mattina e le finestre che ogni funzione genera. Nei riquadri: numero di "
        "ordini · totale in euro. Le finestre tratteggiate di TUMBLE non contengono righe e non compaiono nel "
        "risultato. In SESSIONS la parte tratteggiata è la coda di 30 minuti dopo l'ultimo ordine; CUMULATE continua "
        "con 14:00, 15:00 … 24:00, sempre 10 · 1155.")
    + '<div class="tbl"><table><thead><tr><th>Funzione</th><th>Argomenti dopo tabella e COLUMNS(colonna)</th>'
      "<th>Finestre</th><th>Una riga finisce in</th></tr></thead><tbody>"
      "<tr><td><code>TUMBLE</code></td><td>durata</td><td>Consecutive, stessa durata, senza sovrapposizioni.</td><td>1 finestra</td></tr>"
      "<tr><td><code>HOP</code></td><td>passo, durata</td><td>Stessa durata, una nuova ogni passo: si sovrappongono.</td><td>durata ÷ passo finestre</td></tr>"
      "<tr><td><code>CUMULATE</code></td><td>passo, durata massima</td><td>Stesso inizio, si allungano di un passo fino al massimo.</td><td>tutte quelle che finiscono dopo di lei</td></tr>"
      "<tr><td><code>SESSIONS</code></td><td>pausa</td><td>Decise dai dati: se tra due righe consecutive passa più della pausa, ne inizia una nuova.</td><td>1 finestra</td></tr>"
      "</tbody></table></div>"
    + p("Gli argomenti di tempo sono letterali <code>INTERVAL</code> (anni e mesi, oppure giorni, ore, minuti e "
        "secondi). In <code>HOP</code> il passo viene prima della durata.")
    + h3("Le query delle slide, schema HR")
    + compare(
        code("""select window_start, count (*)
from   ⟦tumble (
  hr.employees,       -- group these rows
  columns ( hire_date ), -- on this column
  interval '2' year   -- into 2 year windows
)⟧
group  by all order by window_start;""", "new") + out(TUMBLE_SLIDE, "slide"),
        code("""select window_start, count (*)
from   ⟦hop (
  hr.employees,       -- group these rows
  columns ( hire_date ), -- on this column
  interval '6' month, -- starting every 6 months
  interval '2' year   -- into 2 year windows
)⟧
group  by all order by window_start;""", "new") + out(HOP_SLIDE, "slide"),
        "TUMBLE", "HOP")
    + ul([
        "<strong>TUMBLE:</strong> finestre di due anni allineate agli anni pari (2010, 2012…), indipendentemente dal "
        "primo dato. 1 + 13 + 39 + 43 + 11 = 107 dipendenti: ognuno sta in una sola finestra.",
        "<strong>HOP:</strong> finestre di due anni che partono ogni sei mesi, quindi ogni dipendente cade in quattro "
        "finestre. La prima parte a luglio 2009 perché contiene già l'assunzione del 13 gennaio 2011. Le righe in "
        "tutto sono 18 e la somma dei conteggi è 428, cioè 4 × 107.",
    ])
    + compare(
        code("""select window_start, window_end, count (*)
from   ⟦cumulate (
  hr.employees,       -- group these rows
  columns ( hire_date ), -- on this column
  interval '2' year,  -- adding 2 years
  interval '10' year  -- up to 10 years
)⟧
group  by all order by window_start, window_end;""", "new") + out(CUM_SLIDE, "slide"),
        code("""select window_start, window_end, count (*)
from   ⟦sessions (
  hr.employees,       -- group these rows
  columns ( hire_date ), -- on this column
  interval '2' year   -- where row is within 2 years of previous
)⟧
group  by all order by window_start;""", "new") + out(SES_SLIDE, "slide"),
        "CUMULATE", "SESSIONS")
    + ul([
        "<strong>CUMULATE:</strong> tutte le finestre partono il 1° gennaio 2010 (allineamento ai 10 anni) e si "
        "allungano di due anni alla volta. I conteggi sono i totali progressivi di TUMBLE: 1, 1+13, 14+39, 53+43, 96+11.",
        "<strong>SESSIONS:</strong> tra due assunzioni consecutive non passano mai due anni (la pausa più lunga è di "
        "511 giorni), quindi c'è una sola sessione. <code>WINDOW_END</code> è l'ultima assunzione, 21 aprile 2018, "
        "più la pausa: 21 aprile 2020.",
    ])
    + h3("Esempi su un caso più concreto: le vendite di una mattina")
    + code("""create table vendite (
  id      number generated always as identity primary key,
  ts      timestamp not null,
  negozio varchar2(10) not null,
  importo number(10,2) not null
);
insert into vendite (ts, negozio, importo) values
  (timestamp '2026-10-26 08:05:00', 'Milano', 120),
  (timestamp '2026-10-26 08:20:00', 'Roma',    80),
  (timestamp '2026-10-26 08:48:00', 'Milano',  45),
  (timestamp '2026-10-26 09:10:00', 'Roma',   200),
  (timestamp '2026-10-26 09:12:00', 'Milano',  60),
  (timestamp '2026-10-26 09:38:00', 'Roma',    35),
  (timestamp '2026-10-26 10:55:00', 'Milano', 150),
  (timestamp '2026-10-26 11:05:00', 'Roma',    90),
  (timestamp '2026-10-26 11:30:00', 'Milano',  75),
  (timestamp '2026-10-26 12:45:00', 'Roma',   300);
commit;""", "any", "Dati di esempio")
    + p("Gli output qui sotto sono calcolati su 23.26.3 applicando a questa tabella le query equivalenti mostrate più "
        "avanti, le stesse che riproducono esattamente i risultati delle slide.")
    + '<h4>TUMBLE: ordini per ora, anche per negozio</h4>'
    + code("""select window_start, window_end, count(*) ordini, sum(importo) totale
from   ⟦tumble ( vendite, columns ( ts ), interval '1' hour )⟧
group  by all
order  by window_start;""", "new")
    + out(V_TUMBLE, "exp")
    + code("""select window_start, negozio, count(*) ordini, sum(importo) totale
from   ⟦tumble ( vendite, columns ( ts ), interval '1' hour )⟧
group  by all
order  by window_start, negozio;""", "new")
    + out(V_TUMBLE_NEG, "exp")
    + '<h4>HOP: finestre di due ore, una ogni ora</h4>'
    + code("""select window_start, window_end, count(*) ordini, sum(importo) totale
from   ⟦hop ( vendite, columns ( ts ), interval '1' hour, interval '2' hour )⟧
group  by all
order  by window_start;""", "new")
    + out(V_HOP, "exp")
    + '<h4>CUMULATE: progressivo della giornata, ora per ora</h4>'
    + p("È l'esempio citato nel post: il totale della giornata aggiornato ogni ora.")
    + code("""select window_start, window_end, count(*) ordini, sum(importo) progressivo
from   ⟦cumulate ( vendite, columns ( ts ), interval '1' hour, interval '1' day )⟧
group  by all
order  by window_end;""", "new")
    + out(V_CUM, "exp")
    + '<h4>SESSIONS: raffiche di ordini separate da almeno 30 minuti</h4>'
    + code("""select window_start, window_end, count(*) ordini, sum(importo) totale
from   ⟦sessions ( vendite, columns ( ts ), interval '30' minute )⟧
group  by all
order  by window_start;""", "new")
    + out(V_SES, "exp")
    + p("Per avere sessioni distinte per negozio o per utente serve partizionare. Le slide non lo mostrano: la sintassi "
        "delle polymorphic table function prevede <code>PARTITION BY</code> sulla tabella e Flink lo prevede per "
        "<code>SESSION</code>, ma verifica nel manuale della 23.26.4 prima di contarci. Con SQL classico funziona "
        "comunque:")
    + code("""with segnate as (
  select v.*,
         case when ts <= lag(ts) over (partition by negozio order by ts) + interval '30' minute
              then 0 else 1 end nuova
  from   vendite v
), numerate as (
  select s.*, sum(nuova) over (partition by negozio order by ts) sessione
  from   segnate s
)
select negozio, min(ts) window_start, max(ts) + interval '30' minute window_end,
       count(*) ordini, sum(importo) totale
from   numerate
group  by negozio, sessione
order  by negozio, window_start;""", "old")
    + out(V_SES_NEG, "run")
    + h3("Prima della 23.26.4: le query equivalenti")
    + p("Queste query riproducono esattamente i risultati delle slide su 23.26.3 e mostrano cosa fa ogni funzione. "
        "<code>TIME_BUCKET</code>, già presente nelle release precedenti, restituisce l'inizio dell'intervallo a "
        "cui appartiene una data, contando da un'origine.")
    + code("""-- TUMBLE ( hr.employees, columns ( hire_date ), interval '2' year )
select time_bucket(hire_date, interval '2' year, date '1970-01-01') window_start, count(*)
from   hr.employees
group  by all
order  by window_start;""", "old", "TUMBLE")
    + out(TB_EQ, "run")
    + code("""-- HOP ( ..., interval '6' month, interval '2' year ): ogni riga in 2 anni / 6 mesi = 4 finestre
select add_months(time_bucket(e.hire_date, interval '6' month, date '1970-01-01'), -6 * n.k) window_start,
       count(*)
from   hr.employees e
cross  join (select level - 1 k connect by level <= 4) n
group  by all
order  by window_start;""", "old", "HOP")
    + out(HOP_FULL, "run")
    + code("""-- CUMULATE ( ..., interval '2' year, interval '10' year ): 10 / 2 = 5 passi
select time_bucket(e.hire_date, interval '10' year, date '1970-01-01') window_start,
       add_months(time_bucket(e.hire_date, interval '10' year, date '1970-01-01'), 24 * n.k) window_end,
       count(*)
from   hr.employees e
cross  join (select level k connect by level <= 5) n
where  e.hire_date < add_months(time_bucket(e.hire_date, interval '10' year, date '1970-01-01'), 24 * n.k)
group  by all
order  by window_start, window_end;""", "old", "CUMULATE")
    + code("""-- SESSIONS ( ..., interval '2' year ): isole e buchi con LAG e somma progressiva
with segnate as (
  select hire_date,
         case when hire_date <= add_months(lag(hire_date) over (order by hire_date), 24)
              then 0 else 1 end nuova_sessione
  from   hr.employees
), numerate as (
  select hire_date, sum(nuova_sessione) over (order by hire_date) sessione
  from   segnate
)
select min(hire_date) window_start, add_months(max(hire_date), 24) window_end, count(*)
from   numerate
group  by sessione
order  by window_start;""", "old", "SESSIONS")
    + p("Per CUMULATE e SESSIONS i risultati coincidono con quelli delle slide (1, 14, 53, 96, 107 e una sessione "
        "da 107 righe).")
    + warn([
        "<strong>Le finestre vuote non compaiono.</strong> Nell'esempio delle vendite non c'è la riga 07:00–08:00. Se "
        "servono gli zeri, fai un outer join con un calendario.",
        "<strong>HOP e CUMULATE moltiplicano le righe.</strong> La somma dei conteggi delle finestre non è il totale: "
        "nella slide di HOP fa 428, cioè 4 × 107.",
        "<strong>Inizio incluso, fine esclusa.</strong> Una vendita delle 09:00:00 cade nella finestra 09:00–10:00.",
        "<strong>Allineamento fisso.</strong> Le finestre partono da istanti fissi (anni pari, ore piene), non dalla "
        "prima riga. Per un'origine diversa, come un anno fiscale che inizia ad aprile o turni che partono alle 6:00, "
        "<code>TIME_BUCKET</code> accetta un'origine esplicita.",
        "<strong>Batch, non streaming.</strong> I nomi vengono dallo streaming SQL, ma qui le funzioni lavorano sui "
        "dati presenti nella tabella al momento della query.",
    ])
))

# ---- EXTRA
S.append(section("altro", "Dettagli visti nelle slide", "Altre cose che compaiono nelle slide",
    "Alcuni elementi delle slide non sono novità della 23.26.4 ma è utile riconoscerli.",
    '<dl class="defs">'
    "<dt><code>GROUP BY ALL</code></dt><dd>Raggruppa per tutte le espressioni della <code>SELECT</code> che non "
    "contengono funzioni di aggregazione. Funziona già su 23.26.3.</dd>"
    "<dt><code>SELECT</code> senza <code>FROM</code></dt><dd>Da 23ai <code>FROM DUAL</code> è facoltativo, anche "
    "con <code>CONNECT BY</code>: <code>select uuid(7) … connect by level &lt;= 5</code>.</dd>"
    "<dt><code>QUALIFY</code></dt><dd>Filtra sul risultato delle funzioni analitiche senza subquery. Funziona già su "
    "23.26.3.</dd>"
    "<dt>Macro nella <code>WITH</code></dt><dd>Novità della 23.26.4 non citata nel post: le SQL macro si possono "
    "usare dentro la clausola <code>WITH</code>.</dd>"
    "</dl>"
))

# ---- SOURCES
SOURCES = [
    ("Chris Saxon, post LinkedIn “Oracle AI Database 23.26.4 is here!” e slide allegate", None),
    ("Oracle AI Database 26ai New Features: SQL", "https://docs.oracle.com/en/database/oracle/oracle-database/26/nfcoa/appdev_sql.html"),
    ("SQL Language Reference 26: SELECT", "https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/SELECT.html"),
    ("SQL Language Reference 26: UUID", "https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/uuid.html"),
    ("SQL Language Reference 26: TIME_BUCKET", "https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/time_bucket-datetime.html"),
    ("PL/SQL Language Reference 26: SQL_MACRO clause", "https://docs.oracle.com/en/database/oracle/oracle-database/26/lnpls/SQL_MACRO-clause.html"),
    ("All Things SQL: How to create views with parameters in Oracle AI Database", "https://blogs.oracle.com/sql/how-to-create-views-with-parameters-in-oracle-ai-database"),
    ("ORACLE-BASE: UUID function in 23ai", "https://oracle-base.com/articles/23/uuid-function-23"),
    ("Ask TOM: Fetch limited rows for update", "https://asktom.oracle.com/ords/asktom.search?tag=fetch-limited-rows-for-update"),
    ("Apache Flink: Windowing table-valued functions", "https://nightlies.apache.org/flink/flink-docs-stable/docs/sql/reference/queries/window-tvf/"),
    ("RFC 9562: Universally Unique IDentifiers (UUIDs)", "https://www.rfc-editor.org/rfc/rfc9562"),
    ("Schema HR: oracle-samples/db-sample-schemas", "https://github.com/oracle-samples/db-sample-schemas"),
]
src_items = "".join(
    f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></li>' if u else f"<li>{esc(t)}</li>"
    for t, u in SOURCES)
S.append(f'<section id="fonti" class="feat"><header class="feat-h"><p class="eyebrow">Fonti</p><h2>Fonti</h2></header>'
         f'<ul class="list src">{src_items}</ul></section>')

# ---------------------------------------------------------------- summary table
SUMMARY = """<div class="tbl summary"><table><thead><tr><th>Novità</th><th>A cosa serve</th><th>Fino a 23.26.3</th>
<th>Con 23.26.4</th></tr></thead><tbody>
<tr><td><a href="#select-star"><code>SELECT *, espr</code></a></td><td>Aggiungere colonne calcolate a tutte le colonne</td>
<td>ORA-00923 / ORA-00936: serviva l'alias <code>t.*</code></td><td><code>select rowid, *, upper(x) from t</code></td></tr>
<tr><td><a href="#for-update"><code>FETCH FIRST … FOR UPDATE</code></a></td><td>Prelevare i prossimi N record liberi da una coda</td>
<td>ORA-02014; con ROWNUM arrivano meno righe del richiesto</td><td>Una query; le righe bloccate non contano nel limite</td></tr>
<tr><td><a href="#uuid"><code>UUID(7)</code>, <code>UUID(5, …)</code></a></td><td>Chiavi ordinate nel tempo o riproducibili</td>
<td>Solo v4 casuale; <code>uuid(7)</code> dà ORA-62433</td><td>v7 ordinata al millisecondo, v5 deterministica</td></tr>
<tr><td><a href="#bar-chart"><code>BAR_CHART</code></a></td><td>Vedere una distribuzione senza uscire dal SQL</td>
<td><code>RPAD</code> scritto a mano</td><td><code>bar_chart(val, max, min, larghezza, simbolo)</code></td></tr>
<tr><td><a href="#macro"><code>CREATE MACRO</code></a></td><td>Viste con parametri ed espressioni riutilizzabili</td>
<td>Funzione PL/SQL <code>SQL_MACRO</code> che restituisce una stringa</td><td>SQL scritto direttamente; usabile anche nella <code>WITH</code></td></tr>
<tr><td><a href="#finestre"><code>TUMBLE</code> <code>HOP</code> <code>CUMULATE</code> <code>SESSIONS</code></a></td><td>Raggruppare righe in finestre di tempo</td>
<td><code>TIME_BUCKET</code>, generatori di righe, <code>LAG</code> + somma progressiva</td><td>Una funzione nella <code>FROM</code> aggiunge <code>WINDOW_START</code> e <code>WINDOW_END</code></td></tr>
</tbody></table></div>"""

NAV = """<nav class="toc" aria-label="Sezioni"><div class="toc-in">
<a href="#select-star">SELECT *</a><a href="#for-update">FOR UPDATE</a><a href="#uuid">UUID</a>
<a href="#bar-chart">BAR_CHART</a><a href="#macro">MACRO</a><a href="#finestre">Finestre</a>
<a href="#altro">Altro</a><a href="#fonti">Fonti</a></div></nav>"""

CSS = (Path(__file__).parent / "page.css").read_text()
JS = (Path(__file__).parent / "page.js").read_text()

PAGE = f"""<title>Novità SQL Oracle 23.26.4</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
{CSS}
</style>
<header class="hero"><div class="hero-in">
<p class="eyebrow">Oracle AI Database 26ai · Release Update 23.26.4</p>
<h1>Novità SQL della 23.26.4</h1>
<p class="lead">Le sei funzionalità presentate da Chris Saxon, una per una: cosa fanno, come si ottenevano prima, esempi
completi e gli errori da evitare.</p>
<div class="method">
<p class="method-t">Come sono stati verificati gli esempi</p>
<p>Ho installato Oracle AI Database 26ai Free 23.26.3, la release precedente, con lo schema HR ufficiale: lo stesso
delle slide, con 107 dipendenti assunti tra il 2011 e il 2018. Lì ho eseguito i workaround tradizionali, registrato
gli errori e ricostruito con SQL classico i risultati delle slide, che coincidono. La 23.26.4 non era disponibile:
gli output delle nuove funzioni che non compaiono nelle slide sono calcolati con query equivalenti.</p>
<ul class="legend">
<li><span class="chip slide">slide 23.26.4</span> output delle slide di Oracle</li>
<li><span class="chip run">eseguito 23.26.3</span> eseguito sulla release precedente</li>
<li><span class="chip exp">atteso</span> calcolato con una query equivalente</li>
<li><mark class="nw lg">evidenziato</mark> sintassi nuova della 23.26.4</li>
</ul>
</div>
</div></header>
{NAV}
<main class="wrap">
<section class="feat intro"><header class="feat-h"><p class="eyebrow">In sintesi</p><h2>Cosa cambia</h2></header>
{SUMMARY}</section>
{"".join(S)}
<footer class="foot">Prove eseguite il 26 ottobre 2026 su Oracle AI Database 26ai Free 23.26.3.0.0 (immagine
container gvenzl/oracle-free) con lo schema HR di oracle-samples/db-sample-schemas.</footer>
</main>
<script>
{JS}
</script>
"""

# Default: a standalone document that opens directly in a browser.
# --artifact: the page content only, for the Artifact tool, which adds the document skeleton itself.
if "--artifact" in sys.argv:
    OUT.write_text(PAGE)
else:
    head, body = PAGE.split("</style>\n", 1)
    OUT.write_text('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
                   '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                   f'{head}</style>\n<style>body {{ margin: 0; }} [hidden] {{ display: none !important; }}</style>\n'
                   f'</head>\n<body>\n{body}</body>\n</html>\n')
print(OUT)
