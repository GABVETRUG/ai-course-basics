#!/usr/bin/env python3
"""Genera le slide del Modulo 1 — Cos'e l'Intelligenza Artificiale (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 1",
    "Cos'e l'Intelligenza Artificiale",
    "Corso AI Basics  |  Durata: 2 ore  |  Teoria + Laboratorio")

agenda_slide(prs, [
    "Cos'e l'Intelligenza Artificiale: definizione e storia",
    "Machine Learning, Deep Learning e LLM",
    "Come funziona un modello linguistico (LLM)",
    "Panoramica degli strumenti disponibili",
    "Laboratorio: prima interazione con ChatGPT, Claude e HuggingChat",
    "Riepilogo e domande",
])

# ── 2. SEZIONE 1 — COS'E L'AI ──────────────────────────
section_slide(prs, 1, "Cos'e l'Intelligenza Artificiale",
              "Definizione, storia e presenza nella vita quotidiana")

highlight_slide(prs,
    "DEFINIZIONE",
    "L'Intelligenza Artificiale e la capacita di un sistema\n"
    "informatico di svolgere compiti che normalmente\n"
    "richiedono intelligenza umana.",
    "Comprendere il linguaggio, riconoscere immagini, prendere decisioni, generare contenuti.")

content_slide(prs, "Breve storia dell'AI", [
    "1950 — Alan Turing propone il 'Test di Turing'",
    "1956 — Nasce ufficialmente il campo dell'AI (conferenza di Dartmouth)",
    "1960-80 — Primi sistemi esperti, poi il primo 'inverno dell'AI'",
    "1997 — Deep Blue (IBM) batte Kasparov a scacchi",
    "2012 — Rivoluzione Deep Learning: le reti neurali profonde decollano",
    "2017 — Google pubblica 'Attention Is All You Need' (architettura Transformer)",
    "2022 — ChatGPT apre l'AI generativa al grande pubblico",
    "2023-oggi — Esplosione di strumenti AI accessibili a tutti",
])

content_slide(prs, "L'AI nella tua vita quotidiana", [
    "Assistenti vocali (Siri, Alexa, Google Assistant)",
    "Suggerimenti di Netflix, Spotify, YouTube",
    "Filtri anti-spam nella posta elettronica",
    "Navigatore GPS con traffico in tempo reale",
    "Traduttore automatico (Google Translate, DeepL)",
    "Riconoscimento facciale per sbloccare il telefono",
    "Correzione automatica e suggerimenti di testo",
    ">>> Usi gia l'AI ogni giorno, senza saperlo!",
])

two_col_slide(prs, "AI debole vs AI forte",
    "AI Debole (Narrow AI)", [
        "Specializzata in un singolo compito",
        "Quella che usiamo oggi",
        "ChatGPT, riconoscimento immagini, etc.",
        "Non 'capisce' realmente, elabora pattern",
        "Molto potente nel suo ambito specifico",
    ],
    "AI Forte (General AI)", [
        "Capace di qualsiasi compito intellettuale",
        "Non esiste ancora",
        "Obiettivo della ricerca a lungo termine",
        "Richiederebbe comprensione reale",
        "Spesso confusa con l'AI nei film",
    ])

# ── 3. SEZIONE 2 — ML, DL, LLM ────────────────────────
section_slide(prs, 2, "Machine Learning, Deep Learning e LLM",
              "I tre livelli dell'AI moderna")

content_slide(prs, "I tre livelli: una struttura a matrioska", [
    "INTELLIGENZA ARTIFICIALE (il campo piu ampio)",
    "   contiene: MACHINE LEARNING (apprendimento dai dati)",
    "      contiene: DEEP LEARNING (reti neurali profonde)",
    "         contiene: LLM (modelli linguistici di grandi dimensioni)",
    "",
    "Ogni livello e un sottoinsieme del precedente.",
    "Noi ci concentreremo sugli LLM, che sono lo strato piu recente.",
])

highlight_slide(prs,
    "MACHINE LEARNING",
    "Un sistema che impara dai dati\n"
    "invece di essere programmato esplicitamente.",
    "Analogia: non scrivi le regole, mostri migliaia di esempi e il sistema trova i pattern da solo.")

content_slide(prs, "Deep Learning: reti neurali profonde", [
    "Ispirato (vagamente) al funzionamento del cervello umano",
    "Reti di 'neuroni artificiali' organizzati in strati (layers)",
    "Piu strati = piu profondo = 'Deep' Learning",
    "Eccelle nel riconoscimento di pattern complessi:",
    "   - Immagini, audio, video, testo",
    "Richiede enormi quantita di dati e potenza di calcolo",
    "E la tecnologia alla base dei modelli AI moderni",
])

content_slide(prs, "LLM: Large Language Models", [
    "Modelli di linguaggio 'grandi' — addestrati su enormi quantita di testo",
    "Comprendono e generano linguaggio naturale",
    "Esempi: GPT-4 (OpenAI), Claude (Anthropic), Llama (Meta), Gemini (Google)",
    "Sono il motore dietro ChatGPT, Claude e gli altri chatbot",
    "Parametri: da miliardi a migliaia di miliardi",
    "   GPT-4: stimati ~1.700 miliardi di parametri",
    "   Llama 3.1: fino a 405 miliardi di parametri",
    "Non sono 'intelligenti' — sono predittori di testo estremamente sofisticati",
])

table_slide(prs, "Confronto: ML vs DL vs LLM",
    ["Caratteristica", "Machine Learning", "Deep Learning", "LLM"],
    [
        ["Tipo di dati", "Tabelle, numeri", "Immagini, audio, testo", "Testo naturale"],
        ["Complessita", "Media", "Alta", "Molto alta"],
        ["Dati necessari", "Migliaia", "Milioni", "Miliardi"],
        ["Esempi", "Filtro spam, previsioni", "Riconosc. facciale", "ChatGPT, Claude"],
        ["Interazione utente", "Indiretta", "Indiretta", "Conversazionale"],
    ])

# ── 4. SEZIONE 3 — COME FUNZIONA UN LLM ────────────────
section_slide(prs, 3, "Come funziona un LLM",
              "Spiegazione intuitiva, senza matematica")

highlight_slide(prs,
    "IL CONCETTO CHIAVE",
    "Un LLM prevede la parola successiva\n"
    "piu probabile, una alla volta.",
    "Come l'autocompletamento del telefono, ma enormemente piu sofisticato.")

content_slide(prs, "Su cosa e stato addestrato?", [
    "Libri, articoli scientifici, pagine web, Wikipedia, forum, codice sorgente...",
    "Centinaia di miliardi di parole in decine di lingue",
    "Il modello NON memorizza i testi — impara i PATTERN del linguaggio",
    "Analogia: chi legge 10.000 romanzi non li ricorda tutti,",
    "   ma sa come si costruisce una frase, un dialogo, un ragionamento",
    "",
    ">>> Il modello e il risultato di cio che ha letto, non una copia",
])

content_slide(prs, "Token: le unita di testo", [
    "Il modello non legge 'parole' ma 'token'",
    "Un token e circa 3/4 di una parola (in inglese)",
    "Esempio: 'Intelligenza Artificiale' = 4-5 token",
    "Perche e importante?",
    "   - I costi si calcolano in token",
    "   - La lunghezza massima si misura in token",
    "   - ChatGPT-4o: ~128.000 token di contesto",
    "   - Claude Opus: ~200.000 token di contesto",
])

content_slide(prs, "La finestra di contesto", [
    "Quantita massima di testo che il modello 'vede' in una conversazione",
    "Include: le tue domande + le risposte del modello + istruzioni di sistema",
    "Quando il contesto si riempie, il modello 'dimentica' i messaggi piu vecchi",
    "",
    "Analogia: una scrivania con spazio limitato.",
    "Puoi avere tanti fogli, ma a un certo punto devi togliere i piu vecchi.",
    "",
    ">>> Conversazioni troppo lunghe possono perdere il filo!",
])

content_slide(prs, "Temperatura: creativita vs precisione", [
    "La 'temperatura' controlla quanto il modello e creativo vs prevedibile",
    "",
    "Temperatura BASSA (0.0 - 0.3):",
    "   Risposte precise, ripetibili, conservative",
    "   Ideale per: dati, analisi, fatti",
    "",
    "Temperatura ALTA (0.7 - 1.0):",
    "   Risposte varie, creative, sorprendenti",
    "   Ideale per: brainstorming, scrittura creativa, idee",
    "",
    "La maggior parte dei tool gestisce questo automaticamente per te.",
])

content_slide(prs, "Cosa un LLM NON sa fare", [
    "NON accede a Internet in tempo reale (salvo plugin specifici)",
    "NON ha memoria tra conversazioni diverse (salvo funzioni dedicate)",
    "NON 'ragiona' come un umano — simula il ragionamento tramite pattern",
    "NON e aggiornato — ha una data limite di addestramento",
    "NON garantisce accuratezza — puo inventare fatti ('allucinazioni')",
    "NON capisce realmente — non ha coscienza, emozioni o intenzioni",
    "",
    ">>> Strumento potentissimo, ma va usato con consapevolezza!",
])

content_slide(prs, "Analogie utili per ricordare", [
    "LLM come AUTOCOMPLETAMENTO avanzato del telefono",
    "   Prevede la prossima parola, ma con molta piu sofisticazione",
    "",
    "LLM come STAGISTA brillante ma inesperto",
    "   Veloce, produttivo, ma va sempre verificato",
    "",
    "LLM come PAPPAGALLO colto",
    "   Riproduce pattern linguistici senza vera comprensione",
    "",
    "LLM come CALCOLATRICE per il linguaggio",
    "   Strumento potente, ma il giudizio resta umano",
])

# ── 5. SEZIONE 4 — PANORAMICA STRUMENTI ────────────────
section_slide(prs, 4, "Panoramica degli strumenti disponibili",
              "ChatGPT, Claude, Gemini e modelli open source")

content_slide(prs, "Il panorama AI nel 2025-2026", [
    "Il mercato degli strumenti AI conversazionali e in rapida evoluzione",
    "Tre categorie principali:",
    "",
    "1. COMMERCIALI CHIUSI: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google)",
    "   - Facili da usare, potenti, ma con limitazioni sul piano gratuito",
    "",
    "2. OPEN SOURCE / OPEN WEIGHT: Llama (Meta), Mistral, Gemma (Google)",
    "   - Gratuiti, personalizzabili, ma richiedono piu competenze",
    "",
    "3. INTEGRATI: Microsoft Copilot, Apple Intelligence, Notion AI",
    "   - Incorporati in strumenti che gia usi",
])

content_slide(prs, "ChatGPT (OpenAI)", [
    "Il piu conosciuto e diffuso al mondo",
    "Modello principale: GPT-4o (omni) — testo, immagini, audio, video",
    "Piano Free: GPT-4o mini, uso limitato di GPT-4o",
    "Piano Plus (20$/mese): accesso completo, DALL-E, GPTs personalizzati",
    "Punti di forza:",
    "   - Ecosistema vastissimo (plugin, GPTs, API)",
    "   - Navigazione web integrata",
    "   - Generazione immagini con DALL-E",
    "Limiti: puo essere verboso, allucinazioni, privacy dei dati",
])

content_slide(prs, "Claude (Anthropic)", [
    "Creato da Anthropic, focalizzato su sicurezza e affidabilita",
    "Modelli: Opus (potente), Sonnet (bilanciato), Haiku (veloce)",
    "Piano Free: Claude Sonnet, uso limitato",
    "Piano Pro (20$/mese): accesso a tutti i modelli, piu utilizzo",
    "Punti di forza:",
    "   - Eccellente nell'analisi di documenti lunghi (200K token)",
    "   - Artifacts: genera codice, grafici, documenti interattivi",
    "   - Projects: organizza conversazioni per progetto",
    "   - Risposte spesso piu precise e meno verbose di ChatGPT",
    "Limiti: no generazione immagini nativa, ecosistema piu piccolo",
])

two_col_slide(prs, "Altri strumenti da conoscere",
    "Google Gemini", [
        "Integrato nell'ecosistema Google",
        "Accesso a dati Google (Gmail, Drive...)",
        "Modelli Gemini 2.5 Pro/Flash",
        "Gratuito con account Google",
        "Forte nel ragionamento multimodale",
    ],
    "Microsoft Copilot", [
        "Integrato in Windows e Office 365",
        "Basato su GPT-4 di OpenAI",
        "Gratis nella versione base",
        "Copilot Pro in Word, Excel, PPT",
        "Ideale se usi gia Microsoft 365",
    ])

content_slide(prs, "Modelli Open Source", [
    "Modelli il cui codice/pesi sono pubblicamente disponibili",
    "",
    "Llama 3.1 (Meta): uno dei piu potenti modelli open",
    "Mistral / Mixtral: azienda francese, ottima qualita",
    "Gemma 2 (Google): versione open dei modelli Google",
    "",
    "Come usarli SENZA installare nulla?",
    "   - HuggingChat (huggingface.co/chat) — interfaccia web gratuita",
    "   - Google AI Studio (aistudio.google.com) — per Gemma e Gemini",
    "",
    ">>> Nel Modulo 5 li esploreremo in dettaglio",
])

table_slide(prs, "Confronto rapido tra strumenti",
    ["Caratteristica", "ChatGPT", "Claude", "HuggingChat"],
    [
        ["Azienda", "OpenAI", "Anthropic", "Hugging Face"],
        ["Piano gratuito", "Si (limitato)", "Si (limitato)", "Si (illimitato)"],
        ["Analisi documenti", "Buona", "Eccellente", "Base"],
        ["Generazione immagini", "Si (DALL-E)", "No", "Si (alcuni modelli)"],
        ["Navigazione web", "Si", "No", "No"],
        ["Ideale per", "Uso generico", "Analisi e scrittura", "Sperimentare open source"],
    ])

# ── 6. SEZIONE 5 — LABORATORIO ─────────────────────────
section_slide(prs, 5, "Laboratorio pratico",
              "Prima interazione con ChatGPT, Claude e HuggingChat")

content_slide(prs, "Preparazione: crea i tuoi account", [
    "1. ChatGPT: vai su chat.openai.com e registrati (gratis)",
    "2. Claude: vai su claude.ai e registrati (gratis)",
    "3. HuggingChat: vai su huggingface.co/chat (gratis, opzionale login)",
    "",
    "Suggerimenti:",
    "   - Usa la stessa email per tutti (facilita la gestione)",
    "   - I piani gratuiti sono sufficienti per tutto il corso",
    "   - Se hai gia un account, assicurati di poter accedere",
])

content_slide(prs, "Esercizio 1: La stessa domanda su tre strumenti", [
    "Poni la STESSA domanda a ChatGPT, Claude e HuggingChat:",
    "",
    "Domanda suggerita:",
    "   'Spiega cos'e l'intelligenza artificiale a un bambino di 10 anni,",
    "    usando un esempio tratto dalla vita quotidiana.'",
    "",
    "Per ogni risposta, annota:",
    "   - Lunghezza della risposta",
    "   - Chiarezza e semplicita del linguaggio",
    "   - Qualita dell'esempio scelto",
    "   - Quale preferisci e perche",
])

content_slide(prs, "Esercizio 2: analizza le differenze", [
    "Dopo aver ricevuto le tre risposte, rifletti:",
    "",
    "1. Le risposte sono simili o molto diverse?",
    "2. Quale strumento ha centrato meglio il tono (bambino di 10 anni)?",
    "3. Quale esempio ti sembra piu efficace?",
    "4. Hai notato errori o informazioni discutibili?",
    "",
    ">>> Non esiste una risposta 'giusta' — l'obiettivo e sviluppare",
    "    senso critico verso gli output dell'AI",
])

content_slide(prs, "Discussione di gruppo", [
    "Condividi le tue osservazioni con il gruppo:",
    "",
    "- Quale strumento hai preferito e perche?",
    "- Hai trovato differenze sorprendenti?",
    "- Ti sei fidato subito delle risposte?",
    "- Cambieresti qualcosa nella domanda per ottenere risultati migliori?",
    "",
    ">>> Spoiler: la qualita della domanda e importante",
    "    quanto la qualita dello strumento!",
    "",
    "(Nel prossimo modulo impareremo esattamente come formulare domande efficaci)",
])

# ── 7. CHIUSURA ─────────────────────────────────────────
recap_slide(prs, [
    "L'AI e un campo vasto; gli LLM sono lo strato piu recente e accessibile",
    "Un LLM prevede la parola successiva — non 'capisce' realmente",
    "Esistono strumenti commerciali (ChatGPT, Claude) e open source (Llama, Mistral)",
    "I piani gratuiti sono sufficienti per iniziare",
    "Ogni strumento ha punti di forza diversi — confrontare e fondamentale",
    "La qualita della domanda determina la qualita della risposta",
])

next_module_slide(prs,
    "Modulo 2: Prompt Engineering\n"
    "L'arte di fare le domande giuste all'AI")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_01_intro_ai", "slides", "Modulo_01_Intro_AI.pptx")
salva(prs, out)
