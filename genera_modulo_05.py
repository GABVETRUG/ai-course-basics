#!/usr/bin/env python3
"""Genera le slide del Modulo 5 — Modelli Open Source (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 5",
    "Modelli Open Source: alternative libere e gratuite",
    "Corso AI Basics  |  Durata: 2 ore  |  0.5h Teoria + 1.5h Laboratorio")

agenda_slide(prs, [
    "Cosa significa 'open source' nell'AI",
    "I modelli principali: Llama, Mistral, Gemma",
    "Dove usarli senza installare nulla",
    "Lab 1: esplorare HuggingChat",
    "Lab 2: Google AI Studio",
    "Lab 3: confronto qualita open vs commerciale",
    "Quando conviene un modello open",
])

# ── 2. SEZIONE 1 — OPEN SOURCE NELL'AI ─────────────────
section_slide(prs, 1, "Open Source nell'AI",
              "Perche e importante e cosa significa")

highlight_slide(prs,
    "DEFINIZIONE",
    "Un modello AI 'open' e un modello i cui pesi\n"
    "(parametri) sono pubblicamente disponibili.\n"
    "Chiunque puo scaricarlo, usarlo e studiarlo.",
    "Attenzione: 'open' non significa sempre 'fai quello che vuoi'. Le licenze variano.")

content_slide(prs, "Open source vs open weight vs closed", [
    "OPEN SOURCE COMPLETO",
    "   Codice + dati di training + pesi del modello pubblici",
    "   Esempi: OLMo (AI2) — il piu trasparente",
    "",
    "OPEN WEIGHT (il piu comune)",
    "   Solo i pesi del modello sono pubblici (scaricabili e usabili)",
    "   Codice di training e dati spesso non rilasciati",
    "   Esempi: Llama (Meta), Mistral, Gemma (Google)",
    "",
    "CLOSED SOURCE",
    "   Nulla e pubblico. Accesso solo tramite API o interfaccia web",
    "   Esempi: GPT-4 (OpenAI), Claude (Anthropic)",
    "",
    "Per semplicita, nel corso usiamo 'open' per indicare entrambi i primi due.",
])

content_slide(prs, "Perche i modelli open sono importanti", [
    "1. TRASPARENZA: puoi sapere (in parte) come funzionano",
    "   Importante per la fiducia e per la ricerca sulla sicurezza",
    "",
    "2. INDIPENDENZA: non sei legato a un singolo provider",
    "   Se OpenAI cambia i prezzi o le policy, hai alternative",
    "",
    "3. PRIVACY: puoi eseguirli sul tuo computer o server",
    "   I dati non escono dalla tua rete (se li installi localmente)",
    "",
    "4. PERSONALIZZAZIONE: puoi fare fine-tuning per il tuo dominio",
    "   Un modello specializzato per la tua azienda/settore",
    "",
    "5. COSTO: molti sono gratuiti per uso commerciale",
    "   (controlla sempre la licenza specifica!)",
])

content_slide(prs, "Le licenze: cosa puoi e cosa non puoi fare", [
    "Ogni modello open ha la sua licenza. Le piu comuni:",
    "",
    "Apache 2.0 (la piu permissiva):",
    "   Uso commerciale libero, modifica libera",
    "   Modelli: Mistral, Gemma 2",
    "",
    "Llama Community License:",
    "   Gratuito se la tua azienda ha < 700M utenti mensili",
    "   Uso commerciale permesso con restrizioni",
    "   Modelli: Llama 3.1",
    "",
    "REGOLA PRATICA per il vostro uso quotidiano:",
    "   Se usate i modelli tramite HuggingChat o AI Studio,",
    "   le licenze sono gestite dalla piattaforma. Nessun problema.",
])

# ── 3. SEZIONE 2 — I MODELLI PRINCIPALI ────────────────
section_slide(prs, 2, "I modelli principali",
              "Chi sono i protagonisti dell'AI aperta")

content_slide(prs, "Llama 3.1 (Meta)", [
    "Sviluppato da Meta (Facebook/Instagram)",
    "Uno dei modelli open piu potenti al mondo",
    "",
    "Versioni disponibili:",
    "   Llama 3.1 8B — Leggero, veloce, buona qualita (gira su PC potente)",
    "   Llama 3.1 70B — Molto capace, compete con GPT-4 in molti task",
    "   Llama 3.1 405B — Il piu grande modello open, qualita eccezionale",
    "",
    "Punti di forza:",
    "   - Eccellente in ragionamento e scrittura",
    "   - Multilingue (ottimo anche in italiano)",
    "   - Supporto contesto fino a 128K token",
    "",
    "Come usarlo: HuggingChat, Groq, Together AI",
])

content_slide(prs, "Mistral e Mixtral", [
    "Azienda francese Mistral AI (fondata 2023, Parigi)",
    "Nota per l'efficienza: modelli piccoli ma molto capaci",
    "",
    "Modelli chiave:",
    "   Mistral 7B — Piccolo e sorprendentemente potente",
    "   Mixtral 8x7B — Architettura 'Mixture of Experts'",
    "      (usa solo una parte dei parametri per ogni risposta = piu veloce)",
    "   Mistral Large — Compete con i modelli top commerciali",
    "",
    "Punti di forza:",
    "   - Ottimo rapporto qualita/dimensione",
    "   - Molto veloce nelle risposte",
    "   - Eccellente in francese, buono in italiano",
    "   - Licenza Apache 2.0 (molto permissiva)",
])

content_slide(prs, "Gemma 2 (Google)", [
    "Versione open dei modelli Google (cugino di Gemini)",
    "Pensato per essere accessibile e facile da usare",
    "",
    "Versioni:",
    "   Gemma 2 2B — Ultra-leggero, gira anche su smartphone",
    "   Gemma 2 9B — Buon compromesso qualita/velocita",
    "   Gemma 2 27B — Il piu capace della famiglia",
    "",
    "Punti di forza:",
    "   - Molto efficiente (piccolo ma capace)",
    "   - Facile da usare su Google AI Studio",
    "   - Licenza permissiva per uso commerciale",
    "   - Ben documentato e supportato da Google",
    "",
    "Ideale per: chi vuole sperimentare con risorse limitate",
])

content_slide(prs, "Altri modelli da tenere d'occhio", [
    "Qwen 2.5 (Alibaba, Cina)",
    "   Molto forte in ragionamento e matematica",
    "   Ottimo rapporto qualita/prezzo anche nelle versioni piccole",
    "",
    "Phi-4 (Microsoft)",
    "   Ultra-compatto: massima qualita per le dimensioni",
    "   Progettato per funzionare su dispositivi locali",
    "",
    "DeepSeek V3 (DeepSeek, Cina)",
    "   Modello molto capace con costi di addestramento sorprendentemente bassi",
    "   Ha scosso il mercato dimostrando che non servono miliardi",
    "",
    "Il panorama cambia ogni pochi mesi — restare aggiornati e importante!",
])

table_slide(prs, "Confronto modelli open",
    ["Modello", "Azienda", "Dimensioni", "Qualita", "Velocita"],
    [
        ["Llama 3.1 70B", "Meta", "70B param", "Eccellente", "Media"],
        ["Mistral Large", "Mistral AI", "123B param", "Ottima", "Media"],
        ["Mixtral 8x7B", "Mistral AI", "47B param", "Molto buona", "Veloce"],
        ["Gemma 2 27B", "Google", "27B param", "Buona", "Veloce"],
        ["Qwen 2.5 72B", "Alibaba", "72B param", "Eccellente", "Media"],
        ["Phi-4", "Microsoft", "14B param", "Buona", "Molto veloce"],
    ])

# ── 4. SEZIONE 3 — DOVE USARLI ─────────────────────────
section_slide(prs, 3, "Dove usarli senza installare nulla",
              "Piattaforme web gratuite per i modelli open")

content_slide(prs, "HuggingChat", [
    "huggingface.co/chat — La piattaforma di riferimento per modelli open",
    "",
    "Caratteristiche:",
    "   - GRATUITO e senza limiti significativi",
    "   - Login opzionale (consigliato per salvare le chat)",
    "   - Ampia scelta di modelli: Llama, Mistral, Gemma, Qwen e altri",
    "   - Puoi cambiare modello in qualsiasi momento",
    "   - Interfaccia simile a ChatGPT",
    "   - Supporta ricerca web (attivabile)",
    "",
    "Limiti:",
    "   - Nessun upload file (nella versione base)",
    "   - Nessuna generazione immagini",
    "   - A volte piu lento dei servizi commerciali",
    "   - Qualita variabile tra i modelli",
])

content_slide(prs, "Google AI Studio", [
    "aistudio.google.com — Piattaforma Google per sperimentare",
    "",
    "Caratteristiche:",
    "   - Accesso gratuito con account Google",
    "   - Modelli disponibili: Gemini 2.5 Pro, Gemini Flash, Gemma 2",
    "   - Interfaccia piu 'tecnica' di HuggingChat",
    "   - Controllo parametri: temperatura, top-p, max token",
    "   - Upload file e immagini",
    "   - Possibilita di usare 'system instructions'",
    "",
    "Ideale per:",
    "   - Chi vuole capire come funzionano i parametri",
    "   - Confrontare versioni di modelli Google",
    "   - Sperimentazione e prototipazione",
])

content_slide(prs, "Altre piattaforme utili", [
    "Groq (groq.com)",
    "   Modelli open a velocita estrema grazie a chip specializzati",
    "   Gratuito con limiti di utilizzo. Llama, Mistral, Gemma",
    "",
    "Poe (poe.com) — di Quora",
    "   Accesso a MOLTI modelli (open + commerciali) da un'unica interfaccia",
    "   Free limitato, abbonamento per uso illimitato",
    "",
    "Perplexity (perplexity.ai)",
    "   Motore di ricerca AI: combina modelli con ricerca web",
    "   Non strettamente 'open', ma usa modelli open internamente",
    "   Gratuito con limiti",
    "",
    "OpenRouter (openrouter.ai)",
    "   Accesso a decine di modelli (open e closed) con una sola API",
])

# ── 5. SEZIONE 4 — LAB 1 ───────────────────────────────
section_slide(prs, 4, "Lab 1: Esplorare HuggingChat",
              "Il tuo primo contatto con i modelli open — 25 min")

content_slide(prs, "Esercizio 1: setup e primo messaggio", [
    "1. Vai su huggingface.co/chat",
    "2. (Opzionale) Crea un account o accedi con Google",
    "3. Osserva: quale modello e selezionato di default?",
    "",
    "4. Invia il primo messaggio:",
    "   'Ciao! Presentati: dimmi quale modello sei, chi ti ha creato,",
    "    e quali sono i tuoi punti di forza e limiti principali.'",
    "",
    "5. Osserva la risposta: il modello 'sa' chi e?",
    "",
    "6. Prova una domanda pratica:",
    "   'Scrivi un'email di presentazione per un'azienda di consulenza",
    "    IT a un potenziale cliente nel settore sanitario.",
    "    Tono professionale, max 150 parole.'",
])

content_slide(prs, "Esercizio 2: cambiare modello e confrontare", [
    "1. Clicca sul nome del modello in alto per cambiarlo",
    "2. Seleziona un modello DIVERSO dal precedente",
    "   Suggerimento: prova Llama, poi Mistral, poi Qwen",
    "",
    "3. Invia la STESSA domanda dell'email di presentazione",
    "4. Confronta le risposte:",
    "",
    "   - Quale email e piu professionale?",
    "   - Quale rispetta meglio il vincolo di 150 parole?",
    "   - Quale ha un italiano migliore?",
    "",
    "5. Prova un terzo modello e ripeti il confronto",
    "",
    ">>> Ogni modello ha una 'personalita' diversa!",
    "    Imparare a riconoscerle ti aiuta a scegliere.",
])

content_slide(prs, "Esercizio 3: ricerca web", [
    "HuggingChat ha una funzione di ricerca web (se disponibile):",
    "",
    "1. Attiva la ricerca web (icona globo, se presente)",
    "2. Chiedi qualcosa che richiede informazioni recenti:",
    "   'Quali sono le ultime novita nel campo dell'AI generativa",
    "    di questa settimana?'",
    "",
    "3. Osserva: fornisce fonti? Le fonti sono affidabili?",
    "",
    "4. Confronto con ChatGPT:",
    "   Fai la stessa domanda a ChatGPT con navigazione web attiva.",
    "   Quale fornisce fonti migliori?",
    "   Quale informazione e piu aggiornata?",
])

# ── 6. SEZIONE 5 — LAB 2 ───────────────────────────────
section_slide(prs, 5, "Lab 2: Google AI Studio",
              "Sperimentare con i parametri dei modelli — 25 min")

content_slide(prs, "Esercizio 1: primo accesso", [
    "1. Vai su aistudio.google.com",
    "2. Accedi con il tuo account Google",
    "3. Clicca 'Create new prompt' (o 'Nuovo prompt')",
    "",
    "4. Osserva l'interfaccia:",
    "   - A sinistra: area di chat / prompt",
    "   - A destra: impostazioni del modello",
    "   - In alto: selezione modello (Gemini 2.5 Pro, Flash, Gemma)",
    "",
    "5. Seleziona 'Gemini 2.5 Flash' (veloce e gratuito)",
    "",
    "6. Scrivi: 'Sei un assistente per un'azienda italiana.",
    "   Rispondi sempre in italiano, in modo conciso e professionale.'",
    "   >>> Inseriscilo nel campo 'System instructions'",
])

content_slide(prs, "Esercizio 2: esplorare i parametri", [
    "Nel pannello destro trovi i parametri del modello:",
    "",
    "TEMPERATURA: prova a cambiarla!",
    "   - Imposta 0.1 e chiedi: 'Scrivi 3 slogan per una gelateria'",
    "   - Poi imposta 1.0 e rifai la STESSA domanda",
    "   - Osserva: a temperatura bassa gli slogan sono piu 'sicuri',",
    "     a temperatura alta sono piu creativi e imprevedibili",
    "",
    "TOP-P (nucleus sampling):",
    "   - Controlla la 'diversita' delle parole considerate",
    "   - 0.1 = molto conservativo, 1.0 = massima varieta",
    "",
    "MAX OUTPUT TOKENS:",
    "   - Limite massimo di token nella risposta",
    "   - Provalo: imposta 50 token e osserva la risposta troncata",
])

content_slide(prs, "Esercizio 3: upload e analisi", [
    "Google AI Studio supporta upload di file e immagini:",
    "",
    "1. Clicca l'icona allegato",
    "2. Carica un'immagine (foto, screenshot, grafico)",
    "3. Chiedi: 'Descrivi cosa vedi in questa immagine.",
    "   Se contiene testo, trascrivilo. Se contiene dati, analizzali.'",
    "",
    "4. Prova con un documento PDF:",
    "   'Riassumi questo documento in 5 punti chiave.'",
    "",
    "5. Confronto: la qualita dell'analisi e paragonabile",
    "   a ChatGPT e Claude? In cosa differisce?",
    "",
    ">>> AI Studio e piu 'tecnico' ma offre controllo maggiore",
])

# ── 7. SEZIONE 6 — LAB 3 ───────────────────────────────
section_slide(prs, 6, "Lab 3: Open vs Commerciale",
              "Confronto qualita su task reali — 25 min")

content_slide(prs, "Esercizio: stesso prompt su 4 strumenti", [
    "Invia lo STESSO prompt a: ChatGPT, Claude, HuggingChat, Google AI Studio",
    "",
    "Prompt suggerito (task complesso per test realistico):",
    "   'Sei un consulente HR. Un'azienda tech italiana (80 dipendenti)",
    "    ha un turnover del 25% annuo. Analizza le possibili cause",
    "    e proponi un piano di retention in 5 punti, con costi stimati",
    "    e tempi di implementazione. Formato: tabella + raccomandazione",
    "    finale. Max 400 parole.'",
    "",
    "Per ciascuno, valuta:",
    "   - Ha rispettato il formato (tabella + raccomandazione)?",
    "   - Le cause identificate sono plausibili?",
    "   - Il piano e realistico e azionabile?",
    "   - Ha rispettato il limite di parole?",
])

table_slide(prs, "Matrice di confronto (compilala!)",
    ["Criterio", "ChatGPT", "Claude", "HuggingChat", "AI Studio"],
    [
        ["Aderenza al formato", "", "", "", ""],
        ["Qualita contenuto", "", "", "", ""],
        ["Realismo stime costi", "", "", "", ""],
        ["Rispetto limite parole", "", "", "", ""],
        ["Italiano corretto", "", "", "", ""],
        ["TOTALE (1-25)", "", "", "", ""],
    ])

content_slide(prs, "Quando preferire un modello open?", [
    "PREFERISCI OPEN QUANDO:",
    "   - Il budget e zero (HuggingChat e completamente gratuito)",
    "   - La privacy e critica (modelli locali con Ollama)",
    "   - Vuoi sperimentare liberamente senza limiti di messaggi",
    "   - Il task e semplice (email, riassunti, brainstorming)",
    "   - Vuoi capire come funzionano i parametri (AI Studio)",
    "",
    "PREFERISCI COMMERCIALE QUANDO:",
    "   - Serve la massima qualita possibile",
    "   - Ti servono feature avanzate (upload file, code interpreter)",
    "   - Lavori con documenti lunghi e complessi",
    "   - Hai bisogno di generazione immagini",
    "   - Vuoi un'esperienza utente piu curata e affidabile",
])

# ── 8. CHIUSURA ─────────────────────────────────────────
content_slide(prs, "Il futuro dei modelli open", [
    "Il gap tra modelli open e closed si sta riducendo rapidamente",
    "",
    "Trend in corso:",
    "   - I modelli open migliorano ogni 3-6 mesi (Llama 4 atteso a breve)",
    "   - Le piattaforme web rendono l'accesso sempre piu facile",
    "   - Aziende come Meta, Google e Microsoft investono nell'open",
    "   - L'EU AI Act potrebbe favorire modelli trasparenti e aperti",
    "",
    "Cosa significa per te:",
    "   - Impara a usare sia strumenti commerciali che open",
    "   - Non legarti a un singolo provider",
    "   - Tieni d'occhio le novita (il panorama cambia velocemente)",
    "",
    ">>> Chi padroneggia entrambi i mondi ha un vantaggio competitivo",
])

recap_slide(prs, [
    "'Open' nell'AI significa pesi del modello pubblici e (spesso) riutilizzabili",
    "Llama (Meta), Mistral e Gemma (Google) sono i protagonisti",
    "HuggingChat e Google AI Studio permettono di usarli gratis senza installare nulla",
    "La qualita dei modelli open e ormai competitiva per molti task quotidiani",
    "La scelta open vs commerciale dipende da: budget, privacy, complessita del task",
    "Il gap si sta chiudendo rapidamente — restare aggiornati e fondamentale",
])

next_module_slide(prs,
    "Modulo 6: AI nel lavoro quotidiano\n"
    "Casi d'uso reali e workflow pratici")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_05_modelli_open", "slides",
                   "Modulo_05_Modelli_Open.pptx")
salva(prs, out)
