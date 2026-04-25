#!/usr/bin/env python3
"""Genera le slide del Modulo 3 — ChatGPT: padroneggiare lo strumento piu diffuso (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 3",
    "ChatGPT: padroneggiare lo strumento piu diffuso",
    "Corso AI Basics  |  Durata: 3 ore  |  0.5h Teoria + 2.5h Laboratorio")

agenda_slide(prs, [
    "OpenAI e ChatGPT: panoramica, modelli e piani",
    "L'interfaccia: orientarsi in ChatGPT",
    "Funzionalita core: file, web, immagini, analisi dati",
    "GPTs: creare assistenti personalizzati",
    "Lab 1: riassunto esecutivo da documento",
    "Lab 2: analisi dati con Code Interpreter",
    "Lab 3: generazione immagini con DALL-E",
    "Lab 4: creare il tuo primo GPT custom",
])

# ── 2. SEZIONE 1 — PANORAMICA ──────────────────────────
section_slide(prs, 1, "Panoramica ChatGPT",
              "L'azienda, i modelli e i piani disponibili")

content_slide(prs, "OpenAI e la nascita di ChatGPT", [
    "OpenAI fondata nel 2015 (Altman, Musk, Sutskever e altri)",
    "Missione: sviluppare AI sicura e benefica per l'umanita",
    "",
    "Timeline chiave:",
    "   2020 — GPT-3: primo modello a mostrare capacita sorprendenti",
    "   Nov 2022 — Lancio di ChatGPT: 1 milione di utenti in 5 giorni",
    "   Mar 2023 — GPT-4: salto qualitativo enorme",
    "   Mag 2024 — GPT-4o: modello multimodale (testo, voce, visione)",
    "   2025 — GPT-4.5 e modelli di ragionamento (o3)",
    "",
    "Oggi ChatGPT ha oltre 200 milioni di utenti attivi settimanali",
])

content_slide(prs, "I modelli disponibili", [
    "GPT-4o ('omni') — Il modello principale",
    "   Multimodale: testo, immagini, audio, video",
    "   Veloce e capace, ideale per la maggior parte dei compiti",
    "",
    "GPT-4o mini — Versione leggera e velocissima",
    "   Meno potente ma molto rapido e economico",
    "   Usato di default nel piano Free",
    "",
    "o3 / o3-mini — Modelli di ragionamento",
    "   'Pensano' prima di rispondere (chain-of-thought interno)",
    "   Eccellenti per matematica, logica, programmazione",
    "   Piu lenti ma piu accurati su problemi complessi",
])

table_slide(prs, "Piani e prezzi",
    ["Caratteristica", "Free", "Plus (20$/mese)", "Team (25$/mese/utente)"],
    [
        ["Modello base", "GPT-4o mini", "GPT-4o + o3", "GPT-4o + o3"],
        ["Messaggi GPT-4o", "Limitati", "Molto di piu", "Molto di piu"],
        ["DALL-E (immagini)", "Limitato", "Si", "Si"],
        ["Upload file", "Si", "Si", "Si"],
        ["Navigazione web", "Si", "Si", "Si"],
        ["GPTs personalizzati", "Solo uso", "Crea + usa", "Crea + usa"],
        ["Code Interpreter", "Limitato", "Si", "Si"],
        ["Privacy dati", "Usati per training", "Usati per training", "Non usati"],
    ])

content_slide(prs, "L'interfaccia: dove trovare tutto", [
    "BARRA LATERALE SINISTRA",
    "   - Nuova chat (+)",
    "   - Storico conversazioni (cercabili)",
    "   - I tuoi GPTs preferiti",
    "",
    "AREA CENTRALE",
    "   - Campo di input (prompt) in basso",
    "   - Selezione modello in alto",
    "   - Icona allegati: upload file, foto, documenti",
    "",
    "IMPOSTAZIONI (icona profilo in basso a sinistra)",
    "   - Personalizzazione: istruzioni personalizzate",
    "   - Controlli dati: opt-out addestramento",
    "   - Tema chiaro/scuro",
])

# ── 3. SEZIONE 2 — FUNZIONALITA CORE ───────────────────
section_slide(prs, 2, "Funzionalita core",
              "Tutto quello che ChatGPT sa fare (e come farlo bene)")

content_slide(prs, "Chat: conversazione e storico", [
    "Ogni conversazione e una 'chat' separata con il suo contesto",
    "",
    "Best practice per le chat:",
    "   - UNA chat per ARGOMENTO (non mischiare temi diversi)",
    "   - Dai un nome descrittivo alle chat importanti",
    "   - Usa 'Nuova chat' quando cambi argomento",
    "   - Il contesto si accumula: chat lunghe perdono il focus",
    "",
    "Comandi utili in chat:",
    "   - 'Ricominciamo da capo con questo approccio...'",
    "   - 'Correggi solo il punto 3, il resto va bene'",
    "   - 'Riscrivi piu breve / piu dettagliato / in un altro tono'",
])

content_slide(prs, "Upload file: analisi documenti", [
    "Puoi caricare direttamente nella chat:",
    "   PDF, Word, Excel, PowerPoint, immagini, CSV, codice sorgente",
    "",
    "Cosa puo fare con i file:",
    "   - Riassumere documenti lunghi",
    "   - Rispondere a domande sul contenuto",
    "   - Estrarre dati specifici",
    "   - Tradurre documenti interi",
    "   - Confrontare piu documenti tra loro",
    "",
    "Limiti:",
    "   - Max ~50 pagine per file (risultati migliori con file piu corti)",
    "   - Non gestisce bene tabelle complesse in PDF scansionati",
    "   - Ricorda: i file vengono inviati ai server di OpenAI!",
])

content_slide(prs, "Navigazione web", [
    "ChatGPT puo cercare informazioni aggiornate su Internet",
    "",
    "Quando si attiva automaticamente:",
    "   - Domande su eventi recenti, notizie, prezzi attuali",
    "   - Richieste esplicite: 'Cerca online...'",
    "",
    "Come usarla al meglio:",
    "   - 'Cerca le ultime statistiche su [argomento] e cita le fonti'",
    "   - 'Confronta i prezzi attuali di [prodotto] su diversi siti'",
    "   - 'Qual e l'ultima versione di [software]?'",
    "",
    "Attenzione:",
    "   - Non sempre attiva la ricerca (a volte risponde dalla memoria)",
    "   - Le fonti citate vanno comunque verificate",
])

content_slide(prs, "DALL-E: generazione immagini", [
    "ChatGPT integra DALL-E 3 per generare immagini da testo",
    "",
    "Cosa puoi creare:",
    "   - Illustrazioni per presentazioni e documenti",
    "   - Mockup e concept visivi",
    "   - Infografiche semplici",
    "   - Loghi e icone (come punto di partenza)",
    "",
    "Come scrivere un buon prompt per immagini:",
    "   1. Descrivi il SOGGETTO in dettaglio",
    "   2. Specifica lo STILE (fotografico, illustrazione, flat design...)",
    "   3. Indica COLORI e ATMOSFERA",
    "   4. Definisci il FORMATO (orizzontale, verticale, quadrato)",
    "",
    "Limite: non scrive bene il testo nelle immagini",
])

content_slide(prs, "Code Interpreter: analisi dati", [
    "ChatGPT puo eseguire codice Python in modo sicuro e analizzare dati",
    "",
    "Cosa puoi fare:",
    "   - Caricare un CSV/Excel e ottenere analisi automatiche",
    "   - Creare grafici e visualizzazioni professionali",
    "   - Pulire e trasformare dati",
    "   - Calcoli statistici e previsioni semplici",
    "   - Scaricare i risultati come file",
    "",
    "Come usarlo:",
    "   1. Carica il file dati nella chat",
    "   2. Chiedi: 'Analizza questo dataset, mostrami i trend principali",
    "      con grafici. Evidenzia anomalie.'",
    "   3. Itera: 'Ora fai un grafico a barre per [colonna]'",
])

content_slide(prs, "Canvas: editing collaborativo", [
    "Modalita di lavoro fianco-a-fianco per testi e codice",
    "",
    "Come funziona:",
    "   - Si apre un pannello laterale con il documento",
    "   - Puoi selezionare porzioni di testo e chiedere modifiche mirate",
    "   - L'AI modifica solo la parte selezionata, non riscrive tutto",
    "",
    "Quando usare Canvas:",
    "   - Scrittura e revisione di testi lunghi (articoli, report)",
    "   - Editing collaborativo con l'AI",
    "   - Quando vuoi controllare le modifiche passo per passo",
    "",
    "Come attivarlo: 'Usa canvas per scrivere...'",
    "   oppure si attiva automaticamente per testi lunghi",
])

content_slide(prs, "Memory e istruzioni personalizzate", [
    "MEMORY (Memoria):",
    "   - ChatGPT puo ricordare informazioni tra conversazioni diverse",
    "   - 'Ricorda che lavoro nel settore farmaceutico'",
    "   - 'Ricorda che preferisco risposte brevi e in italiano'",
    "   - Gestibile: Impostazioni > Personalizzazione > Memoria",
    "",
    "ISTRUZIONI PERSONALIZZATE (Custom Instructions):",
    "   - Istruzioni permanenti applicate a OGNI chat",
    "   - Due campi: 'Cosa vorresti che ChatGPT sapesse di te?'",
    "                'Come vorresti che ChatGPT rispondesse?'",
    "",
    "Esempio di istruzione personalizzata:",
    "   'Sono un project manager in un'azienda IT. Rispondi sempre",
    "    in italiano, in modo conciso. Usa bullet point.'",
])

# ── 4. SEZIONE 3 — GPTs ────────────────────────────────
section_slide(prs, 3, "GPTs: assistenti personalizzati",
              "Creare e usare chatbot specializzati")

highlight_slide(prs,
    "COSA SONO I GPTs?",
    "Versioni personalizzate di ChatGPT,\n"
    "configurate per compiti specifici\n"
    "con istruzioni, conoscenze e strumenti dedicati.",
    "Come creare un collega virtuale specializzato nel tuo ambito di lavoro.")

content_slide(prs, "GPT Store: i piu utili per il lavoro", [
    "Il GPT Store contiene migliaia di GPT creati dalla community",
    "",
    "Categorie utili per il lavoro:",
    "   SCRITTURA: Copywriter, Email Assistant, Resume Builder",
    "   PRODUTTIVITA: Notion Helper, Slides Creator, Meeting Notes",
    "   ANALISI: Data Analyst, Research Assistant, PDF Summarizer",
    "   CODING: Code Review, Debug Helper, SQL Assistant",
    "",
    "Come trovare i migliori:",
    "   - Cerca per categoria nel GPT Store",
    "   - Guarda il numero di conversazioni (popolarita)",
    "   - Prova prima di fidarti: testa con un task reale",
])

content_slide(prs, "Creare un GPT custom: i passaggi", [
    "1. Vai su chat.openai.com > Esplora GPTs > Crea",
    "   (oppure: chatgpt.com/gpts/editor)",
    "",
    "2. Configura tramite CONVERSAZIONE (tab 'Crea'):",
    "   - ChatGPT ti guida con domande per definire il GPT",
    "   - Descrivi cosa vuoi che faccia, come, per chi",
    "",
    "3. Oppure configura manualmente (tab 'Configura'):",
    "   - Nome e descrizione",
    "   - Istruzioni dettagliate (il 'system prompt')",
    "   - Carica file di conoscenza (documenti, dati)",
    "   - Abilita/disabilita: web, DALL-E, Code Interpreter",
    "",
    "4. Testa nella preview e itera fino al risultato desiderato",
    "5. Pubblica: Solo per te / Con link / Nello Store",
])

# ── 5. SEZIONE 4 — LAB 1 ───────────────────────────────
section_slide(prs, 4, "Lab 1: Riassunto esecutivo",
              "Creare un riassunto professionale da un documento — 25 min")

content_slide(prs, "Esercizio: dal documento al riassunto", [
    "Obiettivo: trasformare un documento lungo in un riassunto esecutivo",
    "",
    "Materiale: usa un documento del tuo lavoro (non riservato!)",
    "   oppure scarica un report pubblico (es. report annuale di un'azienda)",
    "",
    "Step 1: Carica il documento in ChatGPT (icona allegato)",
    "Step 2: Usa questo prompt:",
    "   'Analizza il documento allegato e crea un riassunto esecutivo",
    "    di 1 pagina. Struttura: Contesto (2 righe), Punti chiave (5 bullet),",
    "    Rischi/Criticita (3 bullet), Raccomandazione finale.",
    "    Destinatario: CEO non tecnico. Tono: professionale e diretto.'",
    "Step 3: Valuta e chiedi modifiche se necessario",
])

content_slide(prs, "Iterazione e raffinamento", [
    "Dopo il primo risultato, prova questi prompt di follow-up:",
    "",
    "   'Rendi il tono piu incisivo, meno descrittivo'",
    "",
    "   'Aggiungi i 3 dati numerici piu importanti dal documento'",
    "",
    "   'Riscrivi in formato email, come se lo inviassi al CEO'",
    "",
    "   'Crea anche una versione in 3 righe per un messaggio Slack'",
    "",
    "Osserva: ogni prompt di follow-up produce una versione diversa.",
    "La capacita di iterare e cio che distingue un utente base",
    "da un utente avanzato.",
])

# ── 6. SEZIONE 5 — LAB 2 ───────────────────────────────
section_slide(prs, 5, "Lab 2: Analisi dati",
              "Esplorare dati e creare grafici con Code Interpreter — 30 min")

content_slide(prs, "Preparazione: il dataset di esempio", [
    "Se hai un tuo file CSV/Excel (dati NON sensibili), usalo!",
    "",
    "Altrimenti, chiedi a ChatGPT di crearne uno:",
    "   'Genera un file CSV di esempio con dati di vendita:",
    "    12 mesi, 5 prodotti, colonne: Mese, Prodotto, Quantita,",
    "    Fatturato, Regione. 200 righe circa. Includi qualche",
    "    anomalia nei dati per rendere l'analisi interessante.'",
    "",
    "ChatGPT creera il file e lo rendera scaricabile.",
    "Scaricalo, poi caricalo in una nuova chat per l'analisi.",
])

content_slide(prs, "Esercizio: analisi guidata", [
    "Con il dataset caricato, procedi cosi:",
    "",
    "Prompt 1: 'Esplora questo dataset. Dimmi quante righe e colonne ha,",
    "   quali sono i tipi di dati, e segnala eventuali anomalie.'",
    "",
    "Prompt 2: 'Crea 3 grafici che mostrino: (1) trend fatturato mensile,",
    "   (2) distribuzione per prodotto, (3) confronto tra regioni.'",
    "",
    "Prompt 3: 'Qual e il prodotto con la crescita maggiore?",
    "   C'e un mese con un calo anomalo? Spiega le possibili cause.'",
    "",
    "Prompt 4: 'Crea un report di 10 righe con i 3 insight principali",
    "   e 2 raccomandazioni. Tono da analista, con dati a supporto.'",
])

content_slide(prs, "Scaricare e riutilizzare i risultati", [
    "ChatGPT ti permette di scaricare:",
    "   - I grafici generati (PNG, SVG)",
    "   - File dati trasformati (CSV, Excel)",
    "   - Codice Python usato per l'analisi",
    "",
    "Come scaricare: clicca sull'icona di download sotto ogni output",
    "",
    "Uso pratico:",
    "   - Inserisci i grafici nelle tue presentazioni",
    "   - Usa il codice Python come base per analisi ricorrenti",
    "   - Condividi il report con il team",
    "",
    ">>> Non serve sapere Python! ChatGPT scrive e esegue il codice per te.",
])

# ── 7. SEZIONE 6 — LAB 3 ───────────────────────────────
section_slide(prs, 6, "Lab 3: Generazione immagini",
              "Creare visual professionali con DALL-E — 25 min")

content_slide(prs, "Come scrivere prompt per immagini efficaci", [
    "Formula: SOGGETTO + STILE + DETTAGLI + FORMATO",
    "",
    "Esempio VAGO: 'Disegna un ufficio'",
    "   >>> Risultato generico e imprevedibile",
    "",
    "Esempio EFFICACE:",
    "   'Un ufficio moderno open space con 4 persone che collaborano",
    "    attorno a un tavolo. Stile: illustrazione flat design, colori",
    "    pastello blu e verde. Luce naturale dalla finestra. Vista",
    "    dall'alto leggermente inclinata. Formato orizzontale 16:9.'",
    "",
    "Stili utili per il lavoro:",
    "   - Flat design / illustrazione vettoriale (presentazioni)",
    "   - Fotografico realistico (marketing, social)",
    "   - Infografica (report, documenti)",
])

content_slide(prs, "Esercizio: visual per una presentazione", [
    "Crea 3 immagini per una presentazione aziendale su [argomento a scelta]:",
    "",
    "Immagine 1 — Copertina:",
    "   'Crea un'immagine di copertina per una presentazione su [TEMA].",
    "    Stile moderno e professionale, colori [PALETTE], senza testo.'",
    "",
    "Immagine 2 — Concetto astratto:",
    "   'Illustrazione che rappresenti [CONCETTO] in modo metaforico.",
    "    Stile flat design, sfondo trasparente, adatto a slide.'",
    "",
    "Immagine 3 — Scenario:",
    "   'Scena di [SITUAZIONE LAVORATIVA] in un ambiente [DESCRIZIONE].",
    "    Stile fotografico, composizione professionale.'",
    "",
    "Valuta: quale immagine useresti davvero? Quale va rifatta?",
])

content_slide(prs, "Iterare le immagini", [
    "Dopo la prima generazione, puoi perfezionare:",
    "",
    "   'Stessa immagine ma con colori piu caldi'",
    "   'Rimuovi le persone, tieni solo l'ambiente'",
    "   'Cambia lo stile in illustrazione disegnata a mano'",
    "   'Aggiungi un elemento che rappresenti l'innovazione'",
    "",
    "Limiti da conoscere:",
    "   - DALL-E NON gestisce bene il testo nelle immagini",
    "   - Non crea loghi utilizzabili professionalmente",
    "   - Ogni modifica genera un'immagine NUOVA (non modifica l'esistente)",
    "   - Le immagini sono di proprieta dell'utente (per uso commerciale)",
])

# ── 8. SEZIONE 7 — LAB 4 ───────────────────────────────
section_slide(prs, 7, "Lab 4: Creare un GPT custom",
              "Il tuo primo assistente personalizzato — 30 min")

content_slide(prs, "Esercizio: GPT per il tuo lavoro", [
    "Scegli UNO di questi GPT da creare:",
    "",
    "A. ASSISTENTE EMAIL — Scrive risposte nel tuo stile e tono",
    "B. ANALISTA REPORT — Riassume documenti con il formato che preferisci",
    "C. COACH PRESENTAZIONI — Ti aiuta a strutturare presentazioni",
    "D. FAQ AZIENDALE — Risponde alle domande frequenti del tuo team",
    "E. ALTRO — Un GPT specifico per una tua esigenza",
    "",
    "Non serve essere tecnici: ChatGPT ti guida passo per passo!",
])

content_slide(prs, "Step-by-step: configurare il GPT", [
    "1. Vai su chatgpt.com/gpts/editor",
    "",
    "2. Tab 'Crea': descrivi cosa vuoi in linguaggio naturale",
    "   'Voglio un assistente che mi aiuti a scrivere email commerciali",
    "    nel settore IT. Deve usare un tono professionale ma cordiale,",
    "    sempre in italiano, e strutturare le email con: saluto,",
    "    contesto, proposta, call-to-action, saluto finale.'",
    "",
    "3. ChatGPT ti fara domande di approfondimento. Rispondi!",
    "",
    "4. Tab 'Configura': rivedi e personalizza",
    "   - Aggiungi file di conoscenza (listino prezzi, FAQ, template)",
    "   - Abilita/disabilita web, DALL-E, Code Interpreter",
    "",
    "5. Tab 'Anteprima': testa con domande reali. Itera fino a soddisfazione.",
])

content_slide(prs, "Testa e condividi il tuo GPT", [
    "Test da fare prima di considerarlo pronto:",
    "   - Fai 3-5 domande tipiche del caso d'uso",
    "   - Prova un caso limite (domanda fuori tema: deve gestirla bene)",
    "   - Verifica che il tono e il formato siano costanti",
    "   - Carica un file di test se il GPT deve analizzare documenti",
    "",
    "Condivisione:",
    "   - 'Solo per me': uso personale (default)",
    "   - 'Chiunque abbia il link': condividi con colleghi",
    "   - 'Pubblico': visibile nel GPT Store",
    "",
    ">>> Un buon GPT custom puo farti risparmiare ore ogni settimana!",
])

# ── 9. TIPS & TRICKS ───────────────────────────────────
section_slide(prs, 8, "Tips & Tricks",
              "10 trucchi per usare ChatGPT come un professionista")

content_slide(prs, "10 trucchi che pochi conoscono", [
    "1. ISTRUZIONI PERSONALIZZATE: imposta una volta, applicate sempre",
    "2. KEYBOARD SHORTCUTS: Ctrl+Shift+; per copiare l'ultima risposta",
    "3. MENZIONE GPT: tagga un GPT con @ dentro qualsiasi chat",
    "4. 'Sii conciso': aggiungilo al prompt per risposte piu brevi",
    "5. EDIT PROMPT: modifica un messaggio gia inviato con l'icona matita",
    "6. BRANCH: clicca '<' '>' per esplorare risposte alternative",
    "7. CONDIVIDI CHAT: icona condividi per creare un link pubblico",
    "8. VOCE: usa la modalita voce per brainstorming 'a mani libere'",
    "9. CATENA DI CHAT: 'basandoti sulla chat precedente...' (non funziona!)",
    "   >>> Ogni chat e isolata. Copia il contesto necessario.",
    "10. PINNED CHATS: fissa le conversazioni importanti in alto",
])

content_slide(prs, "Limiti e workaround", [
    "LIMITE: risposte troppo lunghe e verbose",
    "   Workaround: 'Rispondi in max 5 bullet point di 1 riga ciascuno'",
    "",
    "LIMITE: perde il contesto in conversazioni lunghe",
    "   Workaround: apri una nuova chat con un riassunto del contesto",
    "",
    "LIMITE: rifiuta richieste legittime per eccesso di cautela",
    "   Workaround: riformula specificando il contesto professionale",
    "",
    "LIMITE: non puo accedere a URL specifici in modo affidabile",
    "   Workaround: copia-incolla il contenuto direttamente nella chat",
    "",
    "LIMITE: DALL-E non scrive testo nelle immagini",
    "   Workaround: aggiungi il testo dopo con Canva, PowerPoint, etc.",
])

# ── 10. CHIUSURA ────────────────────────────────────────
recap_slide(prs, [
    "ChatGPT e lo strumento AI piu versatile: chat, file, web, immagini, codice",
    "Il piano Free e sufficiente per iniziare, il Plus sblocca il pieno potenziale",
    "Upload file + prompt specifico = analisi professionali in pochi minuti",
    "Code Interpreter trasforma chiunque in un analista dati",
    "I GPT custom sono il modo migliore per automatizzare task ripetitivi",
    "Memory e istruzioni personalizzate rendono l'esperienza su misura",
])

next_module_slide(prs,
    "Modulo 4: Claude\n"
    "Il rivale che devi conoscere")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_03_chatgpt", "slides",
                   "Modulo_03_ChatGPT.pptx")
salva(prs, out)
