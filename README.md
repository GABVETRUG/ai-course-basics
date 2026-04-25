# AI Basics Course

**Strumenti di Intelligenza Artificiale per Tutti / Artificial Intelligence Tools for Everyone**

20 hours | 8 modules | 285 slides | 2 languages (IT + EN) | Target: non-technical staff

---

## Languages

| | Italian | English |
|--|---------|---------|
| Folder | `./` (root) | `./en/` |
| Slides | 285 | 285 |
| PDFs | 8 | 8 |
| Exercises | 8 | 8 |
| Lab datasets | 5 | 5 |
| Certificates | 3 styles | 3 styles |
| Speaker notes | All slides | All slides |
| Program + Guide | Yes | Yes |

## Structure

```
ai_course_basics/
|
|-- modulo_01_intro_ai/            What is AI (2h)
|-- modulo_02_prompt_engineering/   Prompt Engineering (3h)
|-- modulo_03_chatgpt/             ChatGPT (3h)
|-- modulo_04_claude/              Claude (3h)
|-- modulo_05_modelli_open/        Open Source Models (2h)
|-- modulo_06_casi_uso/            Real-World Use Cases (3h)
|-- modulo_07_ai_responsabile/     Responsible AI (2h)
|-- modulo_08_progetto_finale/     Final Project + Quiz (2h)
|
|-- materiale_trasversale/         Program, Guide, Certificates (IT)
|-- en/                            Full English version (same structure)
|
|-- pptx_helper.py                 Shared style module
|-- genera_modulo_XX.py            Slide generation scripts
|-- genera_tutto.py                Regenerate all slides (< 2 sec)
|-- genera_speaker_notes.py        Add speaker notes to all slides
|-- genera_certificato.py/v2/v3   Certificate generators (3 styles)
|-- genera_lab_materiali.py        Lab dataset generator
```

Each module contains:
- `slides/` — PowerPoint 16:9 with speaker notes
- `pdf/` — Deep-dive document (Markdown)
- `esercizi/` or `exercises/` — Worksheets with quizzes

## Quick Start

```bash
pip install python-pptx lxml Pillow

# Regenerate all Italian slides
python3 genera_tutto.py

# Regenerate all English slides
cd en && python3 genera_tutto.py && cd ..

# Add speaker notes (both languages)
python3 genera_speaker_notes.py

# Generate certificates (3 styles, IT + EN)
python3 genera_certificato.py
python3 genera_certificato_v2.py
python3 genera_certificato_v3.py

# Generate lab datasets
python3 genera_lab_materiali.py
```

## Customization

- **Content**: edit `genera_modulo_XX.py` scripts, then rerun
- **Visual style**: edit colors/fonts in `pptx_helper.py`
- **PDFs & exercises**: edit Markdown files directly

## Visual Style

Inspired by [Oracle PL/SQL Basics v2](). Paper background, Georgia serif titles, vibrant accent palette (lime, tangerine, cobalt, magenta, amber, mint).

## License

Course materials for educational use.
