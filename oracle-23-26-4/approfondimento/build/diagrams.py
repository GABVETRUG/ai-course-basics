"""SVG diagrams for the 23.26.4 explainer page (inline, themed via page CSS classes)."""


def _hm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def svg_windows():
    W, H = 800, 374
    x0, x1 = 172, 784
    t0, t1 = 7 * 60, 14 * 60

    def X(t):
        m = _hm(t) if isinstance(t, str) else t
        return round(x0 + (m - t0) * (x1 - x0) / (t1 - t0), 1)

    events = ["08:05", "08:20", "08:48", "09:10", "09:12", "09:38", "10:55", "11:05", "11:30", "12:45"]
    out = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Dieci ordini tra le 8 e le 13 e le finestre generate da TUMBLE, HOP, CUMULATE e SESSIONS">']

    # grid + hour labels
    for h in range(7, 15):
        x = X(h * 60)
        out.append(f'<line class="dg-grid" x1="{x}" y1="26" x2="{x}" y2="{H - 8}"/>')
        out.append(f'<text class="dg-axis" x="{x}" y="16" text-anchor="middle">{h:02d}:00</text>')

    # lane labels
    def lane(y, name, sub):
        out.append(f'<text class="dg-lbl" x="8" y="{y}">{name}</text>')
        if sub:
            out.append(f'<text class="dg-sub" x="8" y="{y + 15}">{sub}</text>')

    lane(48, "Ordini", None)
    lane(80, "TUMBLE", "1 h")
    lane(128, "HOP", "2 h, una ogni ora")
    lane(204, "CUMULATE", "+1 h, max 1 giorno")
    lane(332, "SESSIONS", "pausa max 30 min")

    # events
    for e in events:
        out.append(f'<circle class="dg-ev" cx="{X(e)}" cy="44" r="4.5"/>')

    def win(a, b, y, h, label=None, cls="dg-win", anchor="middle", lx=None):
        xa, xb = X(a) + 1.5, X(b) - 1.5
        out.append(f'<rect class="{cls}" x="{xa}" y="{y}" width="{round(xb - xa, 1)}" height="{h}" rx="3"/>')
        if label:
            tx = lx if lx is not None else round((xa + xb) / 2, 1)
            out.append(f'<text class="dg-num" x="{tx}" y="{y + h / 2 + 4}" text-anchor="{anchor}">{label}</text>')

    # TUMBLE
    tumble = [("07:00", "08:00", None), ("08:00", "09:00", "3 · 245"), ("09:00", "10:00", "3 · 295"),
              ("10:00", "11:00", "1 · 150"), ("11:00", "12:00", "2 · 165"), ("12:00", "13:00", "1 · 300"),
              ("13:00", "14:00", None)]
    for a, b, lab in tumble:
        win(a, b, 68, 26, lab, "dg-win" if lab else "dg-empty")

    # HOP (two sub-rows so overlapping windows stay readable)
    for a, b, lab in [("07:00", "09:00", "3 · 245"), ("09:00", "11:00", "4 · 445"), ("11:00", "13:00", "3 · 465")]:
        win(a, b, 112, 21, lab)
    for a, b, lab in [("08:00", "10:00", "6 · 540"), ("10:00", "12:00", "3 · 315"), ("12:00", "14:00", "1 · 300")]:
        win(a, b, 137, 21, lab)

    # CUMULATE: every window starts at 00:00 (off the left edge)
    out.append(f'<text class="dg-sub" x="{x0 + 4}" y="178">← iniziano tutte alle 00:00</text>')
    cum = [("09:00", "3 · 245"), ("10:00", "6 · 540"), ("11:00", "7 · 690"), ("12:00", "9 · 855"), ("13:00", "10 · 1155")]
    for i, (end, lab) in enumerate(cum):
        y = 186 + i * 19
        xb = X(end) - 1.5
        out.append(f'<rect class="dg-win" x="{x0}" y="{y}" width="{round(xb - x0, 1)}" height="15" rx="2"/>')
        out.append(f'<text class="dg-num" x="{round(xb - 6, 1)}" y="{y + 11.5}" text-anchor="end">{lab}</text>')

    # SESSIONS: solid = from first to last order, dashed tail = +30 min
    sess = [("08:05", "09:38", "10:08", "6 · 540"), ("10:55", "11:30", "12:00", "3 · 315"), ("12:45", "12:45", "13:15", "1 · 300")]
    y = 324
    for first, last, end, lab in sess:
        xa, xl, xe = X(first), X(last), X(end)
        if xl > xa:
            out.append(f'<rect class="dg-win" x="{xa}" y="{y}" width="{round(xl - xa, 1)}" height="24" rx="3"/>')
        out.append(f'<rect class="dg-tail" x="{xl}" y="{y}" width="{round(xe - xl, 1)}" height="24" rx="3"/>')
        if lab == "1 · 300":
            out.append(f'<text class="dg-num" x="{round(xe + 5, 1)}" y="{y + 16}" text-anchor="start">{lab}</text>')
        else:
            out.append(f'<text class="dg-num" x="{round((xa + xe) / 2, 1)}" y="{y + 16}" text-anchor="middle">{lab}</text>')
    for e in events:
        out.append(f'<circle class="dg-ev-in" cx="{X(e)}" cy="{y + 24 + 6}" r="2.5"/>')
    # gaps that open a new session
    for a, b, txt in [("09:38", "10:55", "pausa 77 min"), ("11:30", "12:45", "pausa 75 min")]:
        xa, xb = X(a), X(b)
        out.append(f'<path class="dg-dim" d="M{xa} 314 V308 H{xb} V314"/>')
        out.append(f'<text class="dg-sub" x="{round((xa + xb) / 2, 1)}" y="303" text-anchor="middle">{txt}</text>')

    out.append("</svg>")
    return "".join(out)


def svg_uuid():
    rows = [
        ("v4", "90C03C438CC04FF2AAFA95C7B5045D10"),
        ("v5", "7A6FAB4AAD8D580DB94DC96326ECAFD3"),
        ("v7", "01A0E8E0EAF77905AC36727337DF0863"),
    ]
    lx, cw, ch, gap = 58, 20, 28, 10
    W = lx + 32 * cw + 4 * gap + 12
    row_h = 92
    top = 44
    H = top + 3 * row_h - 10

    def cx(i):
        g = sum(1 for b in (8, 12, 16, 20) if i >= b)
        return lx + i * cw + g * gap

    out = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="I 128 bit di un UUID v4, v5 e v7: nella v7 i primi 12 caratteri esadecimali sono il timestamp in millisecondi">']

    # version / variant leader labels at the top
    vx = cx(12) + cw / 2
    rx = cx(16) + cw / 2
    out.append(f'<text class="dg-sub" x="{vx}" y="14" text-anchor="middle">versione</text>')
    out.append(f'<line class="dg-dim" x1="{vx}" y1="19" x2="{vx}" y2="{top - 2}"/>')
    out.append(f'<text class="dg-sub" x="{rx + 6}" y="30" text-anchor="start">variante RFC (8, 9, A o B)</text>')
    out.append(f'<line class="dg-dim" x1="{rx}" y1="34" x2="{rx}" y2="{top - 2}"/>')

    for r, (name, hexs) in enumerate(rows):
        y = top + r * row_h
        out.append(f'<text class="dg-lbl" x="6" y="{y + 19}">{name}</text>')
        for i, c in enumerate(hexs):
            if i == 12:
                cls = "dg-ver"
            elif i == 16:
                cls = "dg-var"
            elif name == "v7" and i < 12:
                cls = "dg-ts"
            elif name == "v5":
                cls = "dg-hash"
            else:
                cls = "dg-rnd"
            x = cx(i)
            out.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{cw - 2}" height="{ch}" rx="2"/>')
            out.append(f'<text class="dg-hex" x="{x + (cw - 2) / 2}" y="{y + 19}" text-anchor="middle">{c}</text>')
        for b in (8, 12, 16, 20):
            gx = cx(b) - gap / 2 - 1
            out.append(f'<text class="dg-sub" x="{gx}" y="{y + 19}" text-anchor="middle">-</text>')

        def bracket(i1, i2, text):
            xa, xb = cx(i1), cx(i2) + cw - 2
            yb = y + ch + 6
            out.append(f'<path class="dg-dim" d="M{xa} {yb} V{yb + 6} H{xb} V{yb}"/>')
            out.append(f'<text class="dg-sub" x="{round((xa + xb) / 2, 1)}" y="{yb + 22}" text-anchor="middle">{text}</text>')

        if name == "v4":
            bracket(0, 31, "tutti gli altri bit sono casuali (122)")
        elif name == "v5":
            bracket(0, 31, "SHA-1( namespace URL + 'test.com/1' ), primi 128 bit")
        else:
            bracket(0, 11, "ms dal 1/1/1970 = 28/09/2026 16:37:29.463 UTC")
            bracket(13, 31, "casuali (74 bit)")
    out.append("</svg>")
    return "".join(out)


def svg_lock(kind):
    W, H = 362, 292
    bx, bw, bh = 104, 92, 26
    y0 = 64
    ids = [100, 101, 102, 103, 104, 105]
    if kind == "rownum":
        title, sub = "WHERE ROWNUM <= 3", "fino a 23.26.3"
        taken = {101, 102}
        brk = (0, 2, "3 candidati")
        result = "2 righe: 101, 102"
        note100 = "bloccata da S1, saltata"
    else:
        title, sub = "FETCH FIRST 3 ROWS ONLY", "23.26.4"
        taken = {101, 102, 103}
        brk = (1, 3, "3 righe libere")
        result = "3 righe: 101, 102, 103"
        note100 = "bloccata da S1, non conta"
    label = "Con ROWNUM la riga bloccata occupa uno dei tre posti" if kind == "rownum" else \
        "Con FETCH FIRST la riga bloccata non conta nel limite"
    out = [f'<svg class="dg" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">']
    out.append(f'<text class="dg-code" x="8" y="20">{title}</text>')
    out.append(f'<text class="dg-code" x="8" y="38">FOR UPDATE SKIP LOCKED</text>')
    out.append(f'<text class="dg-sub" x="{W - 8}" y="20" text-anchor="end">{sub}</text>')
    for i, rid in enumerate(ids):
        y = y0 + i * 34
        cls = "dg-locked" if rid == 100 else ("dg-taken" if rid in taken else "dg-row")
        out.append(f'<rect class="{cls}" x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="3"/>')
        out.append(f'<text class="dg-hex" x="{bx + bw / 2}" y="{y + 17.5}" text-anchor="middle">{rid}</text>')
        if rid == 100:
            out.append(f'<text class="dg-sub" x="{bx + bw + 8}" y="{y + 17.5}">{note100}</text>')
        elif rid in taken:
            out.append(f'<text class="dg-sub" x="{bx + bw + 8}" y="{y + 17.5}">bloccata da S2</text>')
    a, b, txt = brk
    ya, yb = y0 + a * 34, y0 + b * 34 + bh
    out.append(f'<path class="dg-dim" d="M{bx - 6} {ya} H{bx - 12} V{yb} H{bx - 6}"/>')
    out.append(f'<text class="dg-sub" x="{bx - 16}" y="{(ya + yb) / 2 + 4}" text-anchor="end">{txt}</text>')
    out.append(f'<text class="dg-lbl" x="8" y="{H - 8}">{result}</text>')
    out.append("</svg>")
    return "".join(out)
