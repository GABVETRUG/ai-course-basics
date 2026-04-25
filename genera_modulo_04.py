#!/usr/bin/env python3
"""Genera le slide del Modulo 4 — Claude: il rivale che devi conoscere (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 4",
    "Claude: il rivale che devi conoscere",
    "Corso AI Basics  |  Durata: 3 ore  |  0.5h Teoria + 2.5h Laboratorio")

agenda_slide(prs, [
    "Anthropic: chi c'e dietro Claude e perche e diverso",
    "I modelli Claude: Opus, Sonnet, Haiku",
    "Le feature distintive: contesto lungo, Artifacts, Projects",
    "Claude vs ChatGPT: punti di forza a confronto",
    "Lab 1: analisi di un documento lungo",
    "Lab 2: creare Artifacts interattivi",
    "Lab 3: confronto diretto Claude vs ChatGPT",
    "Lab 4: organizzare il lavoro con Projects",
])

# ── 2. SEZIONE 1 — ANTHROPIC E CLAUDE ──────────────────
section_slide(prs, 1, "Anthropic e Claude",
              "L'azienda, la filosofia e i modelli")

content_slide(prs, "Chi e Anthropic", [
    "Fondata nel 2021 da ex-ricercatori di OpenAI (Dario e Daniela Amodei)",
    "Missione: costruire AI affidabile, interpretabile e guidabile",
    "",
    "Differenza chiave rispetto a OpenAI:",
    "   OpenAI: 'Muoviamoci velocemente, l'AI e troppo importante per rallentare'",
    "   Anthropic: 'Muoviamoci in modo responsabile, la sicurezza prima di tutto'",
    "",
    "Finanziata da Google, Amazon e altri per oltre 7 miliardi di dollari",
    "Sede: San Francisco",
    "",
    "Claude e l'unico prodotto consumer di Anthropic",
    "   Il nome viene da Claude Shannon, padre della teoria dell'informazione",
])

highlight_slide(prs,
    "LA FILOSOFIA DI CLAUDE",
    "Constitutional AI:\n"
    "il modello segue un insieme di principi etici\n"
    "definiti esplicitamente, non solo feedback umano.",
    "Risultato: Claude tende a essere piu prudente, onesto e strutturato nelle risposte.")

content_slide(prs, "I modelli Claude", [
    "Claude Opus — Il piu potente",
    "   Ragionamento complesso, analisi approfondite, compiti difficili",
    "   Piu lento e costoso, ma qualita superiore",
    "",
    "Claude Sonnet — Il bilanciato (modello di default)",
    "   Ottimo rapporto qualita/velocita",
    "   Ideale per la maggior parte degli usi quotidiani",
    "",
    "Claude Haiku — Il velocissimo",
    "   Risposte quasi istantanee",
    "   Ideale per compiti semplici e rapidi",
    "",
    "Tutti e tre i modelli condividono: contesto da 200K token,",
    "   analisi immagini e file, stile di risposta Claude",
])

table_slide(prs, "Piani e prezzi",
    ["Caratteristica", "Free", "Pro (20$/mese)", "Team (25$/mese/utente)"],
    [
        ["Modello default", "Sonnet", "Sonnet + Opus + Haiku", "Sonnet + Opus + Haiku"],
        ["Messaggi giornalieri", "Limitati", "5x rispetto a Free", "Ancora di piu"],
        ["Contesto", "200K token", "200K token", "200K token"],
        ["Artifacts", "Si", "Si", "Si"],
        ["Projects", "Si (limitato)", "Si", "Si (condivisi)"],
        ["Upload file", "Si", "Si", "Si"],
        ["Privacy dati", "Possibile review", "No addestramento", "No addestramento"],
    ])

content_slide(prs, "L'interfaccia Claude.ai", [
    "BARRA LATERALE SINISTRA",
    "   - Nuova chat (icona +)",
    "   - Recenti: storico conversazioni",
    "   - Projects: i tuoi progetti organizzati",
    "   - Stella: conversazioni preferite",
    "",
    "AREA CENTRALE",
    "   - Chat pulita e minimale",
    "   - Selezione modello in alto (Opus / Sonnet / Haiku)",
    "   - Icona allegato per upload file e immagini",
    "   - Pannello Artifact a destra (quando attivo)",
    "",
    "Design piu pulito e meno 'affollato' rispetto a ChatGPT",
])

# ── 3. SEZIONE 2 — FEATURE DISTINTIVE ──────────────────
section_slide(prs, 2, "Le feature distintive",
              "Cosa rende Claude diverso dagli altri")

highlight_slide(prs,
    "CONTESTO LUNGO: 200.000 TOKEN",
    "Claude puo analizzare in una singola conversazione\n"
    "circa 500 pagine di testo.\n"
    "Per confronto: ChatGPT Free ne gestisce circa 100.",
    "Ideale per: analisi contratti, report lunghi, manuali, codice sorgente completo.")

content_slide(prs, "Artifacts: output interattivi", [
    "Artifacts e la feature piu innovativa di Claude",
    "",
    "Cos'e: un pannello laterale che mostra output INTERATTIVI",
    "   - Documenti formattati (Markdown)",
    "   - Codice con syntax highlighting",
    "   - Pagine HTML/CSS interattive",
    "   - Grafici SVG",
    "   - Diagrammi e flowchart",
    "   - Applicazioni web semplici (calcolatori, quiz, dashboard)",
    "",
    "Come attivarlo:",
    "   Chiedi qualcosa che si presta a un output strutturato.",
    "   Claude decide autonomamente quando creare un Artifact.",
    "   Oppure: 'Crea un artifact con...'",
])

content_slide(prs, "Tipi di Artifact piu utili per il lavoro", [
    "DOCUMENTI: 'Crea un documento formattato con indice per...'",
    "   Perfetto per: report, procedure, manuali, verbali",
    "",
    "CALCOLATORI: 'Crea un calcolatore interattivo per [formula]'",
    "   Perfetto per: preventivi, ROI, conversioni, stime",
    "",
    "DASHBOARD: 'Crea una dashboard HTML che visualizzi questi dati...'",
    "   Perfetto per: visualizzazioni dati, KPI, panoramiche",
    "",
    "DIAGRAMMI: 'Crea un diagramma di flusso del processo...'",
    "   Perfetto per: workflow, procedure, organigrammi",
    "",
    "Puoi scaricare ogni Artifact, copiarlo o condividerlo via link",
])

content_slide(prs, "Projects: organizzare il lavoro", [
    "Projects permette di creare 'spazi di lavoro' dedicati",
    "",
    "Ogni progetto contiene:",
    "   - Istruzioni personalizzate (system prompt specifico)",
    "   - Documenti di contesto (upload file permanenti)",
    "   - Cronologia delle chat relative al progetto",
    "",
    "Esempio pratico:",
    "   Progetto: 'Report Mensile Marketing'",
    "   Istruzioni: 'Sei un analista marketing. Usa i dati dei file allegati",
    "              per rispondere. Formato: executive summary + dettaglio.'",
    "   File: template report, dati mese precedente, brand guidelines",
    "",
    "Ogni nuova chat nel progetto ha GIA tutto il contesto necessario!",
])

content_slide(prs, "Analisi documenti e immagini", [
    "Upload e analisi file (come ChatGPT, ma con alcune differenze):",
    "   - PDF, documenti, fogli di calcolo, immagini, codice",
    "   - La finestra da 200K token permette documenti molto piu lunghi",
    "",
    "Punti di forza di Claude nell'analisi documenti:",
    "   - Segue le istruzioni in modo piu fedele",
    "   - Struttura le risposte con maggiore precisione",
    "   - Gestisce meglio documenti con struttura complessa",
    "   - Cita le parti rilevanti del documento nelle risposte",
    "",
    "Analisi immagini:",
    "   - Legge e interpreta grafici, tabelle, screenshot",
    "   - Estrae testo da immagini (OCR)",
    "   - NON genera immagini (a differenza di ChatGPT)",
])

content_slide(prs, "Lo stile di risposta Claude", [
    "Claude ha uno stile riconoscibile e diverso da ChatGPT:",
    "",
    "ONESTA: ammette quando non sa qualcosa",
    "   'Non ho informazioni sufficienti per rispondere con certezza'",
    "",
    "STRUTTURA: risposte molto ben organizzate di default",
    "   Header, liste, sezioni chiare senza doverlo chiedere",
    "",
    "CONCISIONE: tendenzialmente meno verboso di ChatGPT",
    "   Va al punto senza preamboli eccessivi",
    "",
    "PRUDENZA: piu conservativo su affermazioni incerte",
    "   Meno allucinazioni, piu disclamer quando appropriato",
    "",
    "LETTERALITA: segue le istruzioni del prompt alla lettera",
    "   Rispetta formato, lunghezza, vincoli piu fedelmente",
])

# ── 4. SEZIONE 3 — CLAUDE VS CHATGPT ───────────────────
section_slide(prs, 3, "Claude vs ChatGPT",
              "Non e una gara: e una scelta consapevole")

two_col_slide(prs, "Punti di forza a confronto",
    "Claude eccelle in", [
        "Analisi documenti lunghi (200K token)",
        "Fedeltà alle istruzioni del prompt",
        "Artifacts: output interattivi e visuali",
        "Projects: organizzazione del lavoro",
        "Qualita della scrittura e struttura",
        "Onesta (ammette quando non sa)",
        "Coding e ragionamento logico",
    ],
    "ChatGPT eccelle in", [
        "Generazione immagini (DALL-E)",
        "Navigazione web integrata",
        "Ecosistema GPTs vastissimo",
        "Code Interpreter per analisi dati",
        "Memory tra conversazioni",
        "Modalita voce avanzata",
        "Community e risorse online",
    ])

content_slide(prs, "Quando scegliere Claude", [
    "Scegli Claude quando:",
    "",
    "   - Devi analizzare documenti lunghi (contratti, manuali, report)",
    "   - Ti serve una risposta molto strutturata e precisa",
    "   - Vuoi creare output interattivi (Artifacts)",
    "   - Lavori su un progetto con contesto fisso (Projects)",
    "   - Ti serve qualita nella scrittura (tono, stile, struttura)",
    "   - Vuoi risposte oneste ('non lo so' invece di inventare)",
    "   - Devi scrivere o analizzare codice complesso",
    "",
    "In sintesi: Claude e ideale per lavoro strutturato,",
    "analisi approfondite e produzione di documenti.",
])

content_slide(prs, "Quando scegliere ChatGPT", [
    "Scegli ChatGPT quando:",
    "",
    "   - Ti servono immagini (DALL-E)",
    "   - Devi cercare informazioni aggiornate online",
    "   - Vuoi un GPT specializzato dalla community",
    "   - Hai bisogno di analisi dati con grafici (Code Interpreter)",
    "   - Vuoi usare la modalita voce",
    "   - Ti serve uno strumento 'tuttofare' generico",
    "   - Cerchi la community e le risorse piu ampie",
    "",
    "In sintesi: ChatGPT e ideale per attivita varie,",
    "ricerca web, immagini e uso generico.",
])

# ── 5. SEZIONE 4 — LAB 1 ───────────────────────────────
section_slide(prs, 4, "Lab 1: Analisi documento lungo",
              "Sfruttare la finestra di contesto da 200K token — 30 min")

content_slide(prs, "Esercizio: caricare e interrogare un documento", [
    "Materiale: un documento lungo (10+ pagine)",
    "   Suggerimento: usa un regolamento, manuale, contratto o report pubblico",
    "   (scaricabile da siti istituzionali, niente dati riservati!)",
    "",
    "Step 1: Carica il documento su claude.ai",
    "",
    "Step 2: Prompt iniziale:",
    "   'Ho caricato un documento di [N] pagine su [ARGOMENTO].",
    "    Prima di tutto, dimmi di cosa tratta e qual e la sua struttura",
    "    (sezioni principali con breve descrizione di ciascuna).'",
    "",
    "Step 3: Lascia che Claude analizzi. Osserva la qualita della sintesi.",
])

content_slide(prs, "Domande mirate sul documento", [
    "Dopo l'analisi iniziale, fai domande progressivamente piu specifiche:",
    "",
    "Livello 1 (comprensione generale):",
    "   'Quali sono i 5 punti piu importanti di questo documento?'",
    "",
    "Livello 2 (ricerca specifica):",
    "   'Cosa dice il documento riguardo [argomento specifico]?",
    "    Cita i passaggi rilevanti.'",
    "",
    "Livello 3 (analisi critica):",
    "   'Ci sono contraddizioni o ambiguita nel documento?",
    "    Evidenzia eventuali lacune o punti poco chiari.'",
    "",
    "Livello 4 (applicazione):",
    "   'Basandoti su questo documento, crea una checklist operativa",
    "    di 10 punti per [ruolo/attivita].'",
])

content_slide(prs, "Confronto: stesso documento su ChatGPT", [
    "Se il tempo lo permette, carica lo stesso documento su ChatGPT",
    "e fai le stesse domande.",
    "",
    "Confronta:",
    "   - Quale ha compreso meglio la struttura del documento?",
    "   - Quale ha risposto meglio alle domande specifiche?",
    "   - Quale ha citato i passaggi in modo piu preciso?",
    "   - Quale ha gestito meglio le domande critiche?",
    "",
    "Di solito noterai:",
    "   Claude: piu preciso nelle citazioni, piu strutturato",
    "   ChatGPT: piu discorsivo, a volte piu creativo nelle interpretazioni",
])

# ── 6. SEZIONE 5 — LAB 2 ───────────────────────────────
section_slide(prs, 5, "Lab 2: Artifacts interattivi",
              "Creare output visuali e funzionali — 30 min")

content_slide(prs, "Esercizio 1: documento formattato", [
    "Chiedi a Claude:",
    "",
    "   'Crea un artifact con un documento formattato:",
    "    Titolo: Guida rapida all'uso dell'AI nel nostro team",
    "    Sezioni: Strumenti approvati, Regole d'uso, 5 prompt utili,",
    "    FAQ (5 domande). Formato professionale con indice.'",
    "",
    "Osserva:",
    "   - L'artifact si apre nel pannello laterale destro",
    "   - Puoi copiare, scaricare o modificare il contenuto",
    "   - Puoi chiedere modifiche: 'Aggiungi una sezione su...'",
    "",
    "Esercizio extra: 'Trasforma questo artifact in una email",
    "   da inviare al team per annunciare queste linee guida'",
])

content_slide(prs, "Esercizio 2: calcolatore interattivo", [
    "Chiedi a Claude:",
    "",
    "   'Crea un artifact HTML con un calcolatore interattivo",
    "    per [SCEGLI UNO]:",
    "    a) Calcolo del ROI di un progetto",
    "    b) Preventivo per un servizio",
    "    c) Conversione unita di misura",
    "    d) Calcolatore di scadenze/timeline",
    "",
    "    Deve avere: campi di input, pulsante Calcola,",
    "    area risultati con spiegazione. Design pulito e moderno.'",
    "",
    "Prova ad usare il calcolatore: funziona? I calcoli sono corretti?",
    "Se qualcosa non va: 'Il calcolo del campo X e sbagliato,",
    "   la formula corretta e [FORMULA]'",
])

content_slide(prs, "Esercizio 3: dashboard dati", [
    "Chiedi a Claude:",
    "",
    "   'Crea un artifact HTML con una dashboard che visualizzi",
    "    questi dati di vendita trimestrali:",
    "    Q1: 150K, Q2: 180K, Q3: 165K, Q4: 210K",
    "    Prodotto A: 40%, Prodotto B: 35%, Prodotto C: 25%",
    "",
    "    Includi: grafico a barre per trimestri, grafico a torta",
    "    per prodotti, indicatore di crescita anno su anno,",
    "    tabella riepilogativa. Design moderno con colori coerenti.'",
    "",
    "Itera: 'Cambia i colori in [palette]'",
    "       'Aggiungi un campo per inserire i dati del prossimo trimestre'",
])

# ── 7. SEZIONE 6 — LAB 3 ───────────────────────────────
section_slide(prs, 6, "Lab 3: Confronto diretto",
              "Stesso task, due strumenti, risultati diversi — 25 min")

content_slide(prs, "Esercizio: test comparativo strutturato", [
    "Scegli UN task complesso e invia lo STESSO prompt a Claude e ChatGPT",
    "",
    "Task suggeriti:",
    "   A. 'Analizza i pro e contro del lavoro da remoto per un'azienda",
    "       di 50 persone. Crea un report di 1 pagina con raccomandazione.'",
    "",
    "   B. 'Scrivi una proposta commerciale per un servizio di consulenza",
    "       AI rivolto a PMI italiane. Max 2 pagine, tono professionale.'",
    "",
    "   C. 'Crea un piano di onboarding di 30 giorni per un nuovo",
    "       dipendente nel reparto marketing. Tabella settimana per settimana.'",
    "",
    "Invia lo STESSO prompt, parola per parola, a entrambi.",
])

table_slide(prs, "Scheda confronto (compilala!)",
    ["Criterio", "Claude", "ChatGPT", "Migliore"],
    [
        ["Aderenza al prompt", "", "", ""],
        ["Struttura e formattazione", "", "", ""],
        ["Qualita del contenuto", "", "", ""],
        ["Concisione vs verbosita", "", "", ""],
        ["Originalita delle idee", "", "", ""],
        ["Accuratezza dei fatti", "", "", ""],
        ["Tono e stile", "", "", ""],
    ])

# ── 8. SEZIONE 7 — LAB 4 ───────────────────────────────
section_slide(prs, 7, "Lab 4: Projects",
              "Organizzare il lavoro con contesto persistente — 25 min")

content_slide(prs, "Creare un progetto su Claude", [
    "Step 1: Nella barra laterale, clicca '+ Nuovo progetto'",
    "Step 2: Dai un nome al progetto (es: 'Report settimanale vendite')",
    "Step 3: Scrivi le istruzioni personalizzate:",
    "",
    "   Esempio:",
    "   'Sei un analista di vendite per un'azienda di [settore].",
    "    Quando ti invio dati, analizzali e crea un report con:",
    "    - Riepilogo performance (3 righe)",
    "    - Top 3 prodotti per crescita",
    "    - Segnali di allarme",
    "    - 2 azioni suggerite",
    "    Formato: bullet point, tono professionale, max 1 pagina.'",
    "",
    "Step 4: Carica file di contesto (template, dati storici, KPI)",
])

content_slide(prs, "Lavorare nel contesto del progetto", [
    "Una volta configurato, ogni nuova chat nel progetto:",
    "   - Conosce GIA le istruzioni e i file caricati",
    "   - Non devi ripetere il contesto ogni volta",
    "   - Puo fare riferimento ai documenti caricati",
    "",
    "Esempio di workflow:",
    "   Lunedi: 'Ecco i dati di questa settimana [incolla]. Analizza.'",
    "   >>> Claude produce il report nel formato definito",
    "",
    "   Martedi: 'Confronta con la settimana scorsa [incolla].'",
    "   >>> Claude sa gia il formato e il contesto",
    "",
    "   Venerdi: 'Crea il riepilogo settimanale per il management.'",
    "   >>> Claude conosce tutti i dati della settimana",
])

content_slide(prs, "Idee per Projects utili", [
    "REPORT RICORRENTI: report settimanali/mensili con formato fisso",
    "   Carica: template, KPI target, dati storici",
    "",
    "ASSISTENTE PROGETTO: un AI dedicata a un progetto specifico",
    "   Carica: brief, timeline, documenti di riferimento, stakeholder",
    "",
    "BASE DI CONOSCENZA: FAQ e procedure del tuo team",
    "   Carica: manuali, procedure, regolamenti interni",
    "",
    "SCRITTURA BRAND: contenuti coerenti con il tono aziendale",
    "   Carica: brand guidelines, esempi di comunicazione, tone of voice",
    "",
    ">>> Un buon progetto si configura una volta e si usa per mesi!",
])

# ── 9. CHIUSURA ─────────────────────────────────────────
content_slide(prs, "Tips & tricks per Claude", [
    "1. USA ARTIFACTS per qualsiasi output strutturato o visuale",
    "2. PROJECTS per tutto cio che e ricorrente (report, analisi, scrittura)",
    "3. SPECIFICA IL FORMATO: Claude e eccellente nel rispettarlo",
    "4. DOCUMENTI LUNGHI: Claude e il migliore per analisi di contratti/manuali",
    "5. SCEGLI IL MODELLO: Haiku per domande rapide, Sonnet per uso quotidiano,",
    "   Opus per analisi complesse",
    "6. CHIEDI DI CITARE: 'Cita i passaggi rilevanti dal documento'",
    "7. ITERA GLI ARTIFACTS: puoi perfezionarli con feedback specifici",
    "8. NON GENERA IMMAGINI: per visual, crea l'artifact e usa DALL-E per le foto",
])

recap_slide(prs, [
    "Claude e costruito sulla filosofia 'AI sicura' di Anthropic",
    "Tre modelli: Opus (potente), Sonnet (bilanciato), Haiku (veloce)",
    "Contesto da 200K token: ideale per documenti lunghi",
    "Artifacts: output interattivi unici nel panorama (calcolatori, dashboard, documenti)",
    "Projects: spazi di lavoro con contesto persistente",
    "Claude e ChatGPT hanno punti di forza diversi — usa entrambi strategicamente",
])

next_module_slide(prs,
    "Modulo 5: Modelli Open Source\n"
    "Alternative libere e gratuite")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_04_claude", "slides",
                   "Modulo_04_Claude.pptx")
salva(prs, out)
