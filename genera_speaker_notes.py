#!/usr/bin/env python3
"""
genera_speaker_notes.py — Aggiunge note del relatore a tutte le slide.
Rileva automaticamente il tipo di slide e genera note contestuali.
Supporta IT e EN.
"""
import os
import glob
from pptx import Presentation
from pptx.util import Emu

# ── Colori di riferimento per detection ─────────────────
INK_RGB    = (0x0B, 0x0B, 0x0C)
COBALT_RGB = (0x1E, 0x3C, 0xFF)


def get_bg(slide):
    try:
        rgb = slide.background.fill.fore_color.rgb
        return (rgb[0], rgb[1], rgb[2])
    except:
        return None


def get_texts(slide):
    """Restituisce tutti i testi della slide come lista."""
    texts = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                t = p.text.strip()
                if t:
                    texts.append(t)
    return texts


def has_table(slide):
    return any(shape.has_table for shape in slide.shapes)


def get_title_and_bullets(texts):
    """Separa il titolo (primo testo lungo) dai bullet."""
    title = ""
    bullets = []
    for t in texts:
        if not title and len(t) > 3 and not t.startswith("·") and not t.startswith("/"):
            title = t
        elif t.startswith("·"):
            bullets.append(t.replace("·", "").strip())
    return title, bullets


def detect_type(slide, texts, slide_idx, total):
    bg = get_bg(slide)
    joined = " ".join(texts).lower()

    if slide_idx == 0:
        return "title"

    if bg == COBALT_RGB:
        return "next_module"

    if bg == INK_RGB:
        if "domande?" in joined or "questions?" in joined:
            return "question"
        if "riepilogo" in joined or "recap" in joined:
            return "recap"
        return "section"

    # Paper background
    if slide_idx == 1 and ("programma" in joined or "syllabus" in joined):
        return "agenda"

    if has_table(slide):
        return "table"

    if "concetto chiave" in joined or "key concept" in joined:
        return "highlight"

    # Two-col: ha card shapes (rounded rectangles with borders)
    rounded_count = sum(1 for s in slide.shapes
                       if hasattr(s, 'shape_type') and 'AUTO_SHAPE' in str(s.shape_type)
                       and s.width > Emu(914400 * 3))  # shapes > 3 inches
    if rounded_count >= 2:
        return "two_col"

    return "content"


def make_notes_it(stype, texts, slide_idx, total, module_num):
    title, bullets = get_title_and_bullets(texts)
    first_bullets = bullets[:3]
    bullet_summary = "; ".join(first_bullets) if first_bullets else ""

    notes = {
        "title": (
            f"APERTURA MODULO {module_num}\n\n"
            f"· Presenta il modulo e gli obiettivi\n"
            f"· Verifica che tutti abbiano accesso agli strumenti\n"
            f"· Anticipa la struttura: prima la teoria, poi la pratica\n"
            f"· Tempo suggerito: 2-3 minuti\n\n"
            f"Domanda di apertura: 'Qualcuno di voi ha gia usato strumenti AI questa settimana?'"
        ),
        "agenda": (
            f"AGENDA\n\n"
            f"· Scorri brevemente ogni punto dell'agenda\n"
            f"· Indica i momenti pratici (lab) e le pause\n"
            f"· Chiedi se ci sono aspettative particolari\n"
            f"· Tempo suggerito: 2 minuti"
        ),
        "section": (
            f"TRANSIZIONE DI SEZIONE\n\n"
            f"Titolo: {title}\n\n"
            f"· Pausa breve: 'Fin qui tutto chiaro?'\n"
            f"· Introduci il tema della nuova sezione\n"
            f"· Collegamento con la sezione precedente\n"
            f"· Tempo suggerito: 1 minuto"
        ),
        "content": (
            f"SLIDE: {title}\n\n"
            f"Punti chiave da enfatizzare:\n"
            + (f"· {bullet_summary}\n\n" if bullet_summary else "\n")
            + f"Suggerimenti:\n"
            f"· Non leggere i bullet — parafrasa e aggiungi contesto\n"
            f"· Usa esempi concreti dal lavoro quotidiano\n"
            f"· Chiedi: 'Qualcuno ha esperienza diretta con questo?'\n"
            f"· Tempo suggerito: 2-3 minuti"
        ),
        "two_col": (
            f"CONFRONTO: {title}\n\n"
            f"· Presenta prima il lato sinistro, poi il destro\n"
            f"· Evidenzia le differenze chiave\n"
            f"· Chiedi ai partecipanti quale preferiscono e perche\n"
            f"· Non schierarti: il messaggio e 'dipende dal contesto'\n"
            f"· Tempo suggerito: 3-4 minuti"
        ),
        "table": (
            f"TABELLA: {title}\n\n"
            f"· Non leggere tutta la tabella — evidenzia 2-3 righe chiave\n"
            f"· Chiedi ai partecipanti di trovare il dato piu sorprendente\n"
            f"· Lascia la tabella visibile qualche secondo per la lettura\n"
            f"· Tempo suggerito: 2-3 minuti"
        ),
        "highlight": (
            f"CONCETTO CHIAVE\n\n"
            f">>> PAUSA QUI — Lascia il tempo di leggere <<<\n\n"
            f"· Questa slide contiene un concetto fondamentale\n"
            f"· Leggi il testo ad alta voce, poi parafrasa\n"
            f"· Chiedi: 'Qualcuno puo riformularlo con parole sue?'\n"
            f"· Assicurati che tutti abbiano compreso prima di proseguire\n"
            f"· Tempo suggerito: 2-3 minuti"
        ),
        "recap": (
            f"RIEPILOGO MODULO\n\n"
            f"· Scorri ogni punto rapidamente — NON rispiegare tutto\n"
            f"· Chiedi: 'Qual e il concetto che vi ha colpito di piu?'\n"
            f"· Chiedi: 'C'e qualcosa che non e chiaro?'\n"
            f"· Se ci sono dubbi, chiarisci ora prima di proseguire\n"
            f"· Tempo suggerito: 3-4 minuti"
        ),
        "question": (
            f"SESSIONE DOMANDE\n\n"
            f"· Apri il microfono: 'Ci sono domande?'\n"
            f"· Se nessuno chiede, proponi una domanda stimolo:\n"
            f"  'Quale strumento pensate di usare per primo nel vostro lavoro?'\n"
            f"· Gestisci il tempo: max 5 minuti\n"
            f"· Se le domande sono troppe, offri di rispondere durante la pausa"
        ),
        "next_module": (
            f"ANTEPRIMA PROSSIMO MODULO\n\n"
            f"· Presenta brevemente cosa si vedra dopo\n"
            f"· Crea curiosita senza anticipare troppo\n"
            f"· Annuncia la pausa se prevista\n"
            f"· Tempo suggerito: 1 minuto"
        ),
    }
    return notes.get(stype, f"Slide {slide_idx + 1}/{total}")


def make_notes_en(stype, texts, slide_idx, total, module_num):
    title, bullets = get_title_and_bullets(texts)
    first_bullets = bullets[:3]
    bullet_summary = "; ".join(first_bullets) if first_bullets else ""

    notes = {
        "title": (
            f"MODULE {module_num} OPENING\n\n"
            f"· Introduce the module and its objectives\n"
            f"· Verify everyone has access to the tools\n"
            f"· Preview the structure: theory first, then hands-on\n"
            f"· Suggested time: 2-3 minutes\n\n"
            f"Opening question: 'Has anyone used AI tools this week?'"
        ),
        "agenda": (
            f"AGENDA\n\n"
            f"· Walk through each agenda item briefly\n"
            f"· Point out the hands-on labs and breaks\n"
            f"· Ask if there are any particular expectations\n"
            f"· Suggested time: 2 minutes"
        ),
        "section": (
            f"SECTION TRANSITION\n\n"
            f"Title: {title}\n\n"
            f"· Brief pause: 'Everything clear so far?'\n"
            f"· Introduce the new section topic\n"
            f"· Connect with the previous section\n"
            f"· Suggested time: 1 minute"
        ),
        "content": (
            f"SLIDE: {title}\n\n"
            f"Key points to emphasize:\n"
            + (f"· {bullet_summary}\n\n" if bullet_summary else "\n")
            + f"Tips:\n"
            f"· Don't read the bullets — paraphrase and add context\n"
            f"· Use real-world examples from everyday work\n"
            f"· Ask: 'Has anyone experienced this firsthand?'\n"
            f"· Suggested time: 2-3 minutes"
        ),
        "two_col": (
            f"COMPARISON: {title}\n\n"
            f"· Present the left side first, then the right\n"
            f"· Highlight the key differences\n"
            f"· Ask participants which they prefer and why\n"
            f"· Stay neutral: the message is 'it depends on context'\n"
            f"· Suggested time: 3-4 minutes"
        ),
        "table": (
            f"TABLE: {title}\n\n"
            f"· Don't read the whole table — highlight 2-3 key rows\n"
            f"· Ask participants to find the most surprising data point\n"
            f"· Leave the table visible for a few seconds for reading\n"
            f"· Suggested time: 2-3 minutes"
        ),
        "highlight": (
            f"KEY CONCEPT\n\n"
            f">>> PAUSE HERE — Give time to read <<<\n\n"
            f"· This slide contains a fundamental concept\n"
            f"· Read the text aloud, then paraphrase\n"
            f"· Ask: 'Can someone rephrase this in their own words?'\n"
            f"· Make sure everyone understands before moving on\n"
            f"· Suggested time: 2-3 minutes"
        ),
        "recap": (
            f"MODULE RECAP\n\n"
            f"· Go through each point quickly — DON'T re-explain everything\n"
            f"· Ask: 'What concept stood out the most?'\n"
            f"· Ask: 'Is there anything that's still unclear?'\n"
            f"· If there are doubts, clarify now before moving on\n"
            f"· Suggested time: 3-4 minutes"
        ),
        "question": (
            f"Q&A SESSION\n\n"
            f"· Open the floor: 'Any questions?'\n"
            f"· If nobody asks, prompt with:\n"
            f"  'Which tool do you think you'll use first at work?'\n"
            f"· Manage time: max 5 minutes\n"
            f"· If too many questions, offer to continue during the break"
        ),
        "next_module": (
            f"NEXT MODULE PREVIEW\n\n"
            f"· Briefly preview what's coming next\n"
            f"· Build curiosity without giving too much away\n"
            f"· Announce the break if scheduled\n"
            f"· Suggested time: 1 minute"
        ),
    }
    return notes.get(stype, f"Slide {slide_idx + 1}/{total}")


def add_notes_to_pptx(pptx_path, lang="it", module_num=1):
    prs = Presentation(pptx_path)
    total = len(prs.slides)
    make_notes = make_notes_it if lang == "it" else make_notes_en

    for idx, slide in enumerate(prs.slides):
        texts = get_texts(slide)
        stype = detect_type(slide, texts, idx, total)
        note_text = make_notes(stype, texts, idx, total, module_num)

        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = note_text

    prs.save(pptx_path)
    return total


def process_all(base_dir, lang="it"):
    label = "NOTE RELATORE" if lang == "it" else "SPEAKER NOTES"
    print(f"\n{'=' * 60}")
    print(f"  {label} — {lang.upper()}")
    print(f"{'=' * 60}")

    pptx_files = sorted(glob.glob(os.path.join(base_dir, "modulo_*/slides/*.pptx")))

    total_slides = 0
    for pptx_path in pptx_files:
        fname = os.path.basename(pptx_path)
        # Estrai numero modulo dal nome file
        try:
            mod_num = int(''.join(c for c in fname.split('_')[1] if c.isdigit()))
        except:
            mod_num = 0

        n = add_notes_to_pptx(pptx_path, lang, mod_num)
        total_slides += n
        print(f"  OK  {fname} ({n} slide)")

    print(f"{'=' * 60}")
    print(f"  {total_slides} slide con note del relatore")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # IT
    process_all(script_dir, "it")

    # EN
    en_dir = os.path.join(script_dir, "..", "ai_course_basics_en")
    if os.path.isdir(en_dir):
        process_all(en_dir, "en")
