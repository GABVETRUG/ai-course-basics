#!/usr/bin/env python3
"""
genera_tutto.py — Rigenera TUTTE le slide del corso AI Basics.
Esegui questo script dopo ogni modifica ai contenuti.
"""
import subprocess
import sys
import os
import time

SCRIPTS = [
    "genera_modulo_01.py",
    "genera_modulo_02.py",
    "genera_modulo_03.py",
    "genera_modulo_04.py",
    "genera_modulo_05.py",
    "genera_modulo_06.py",
    "genera_modulo_07.py",
    "genera_modulo_08.py",
]

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    ok, fail = 0, 0
    t0 = time.time()

    print("=" * 60)
    print("  GENERAZIONE SLIDE — Corso AI Basics")
    print("=" * 60)

    for script in SCRIPTS:
        path = os.path.join(base, script)
        if not os.path.exists(path):
            print(f"  MANCANTE: {script}")
            fail += 1
            continue
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True, text=True, cwd=base
        )
        if result.returncode == 0:
            print(f"  OK  {result.stdout.strip()}")
            ok += 1
        else:
            print(f"  ERRORE  {script}: {result.stderr.strip()}")
            fail += 1

    elapsed = time.time() - t0
    print("=" * 60)
    print(f"  Completato in {elapsed:.1f}s — {ok} OK, {fail} errori")
    print("=" * 60)

    # Conteggio slide totali
    try:
        from pptx import Presentation
        total = 0
        for d in sorted(os.listdir(base)):
            pdir = os.path.join(base, d, "slides")
            if os.path.isdir(pdir):
                for f in os.listdir(pdir):
                    if f.endswith(".pptx"):
                        p = Presentation(os.path.join(pdir, f))
                        total += len(p.slides)
        print(f"\n  Slide totali: {total}")
    except Exception:
        pass

    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
