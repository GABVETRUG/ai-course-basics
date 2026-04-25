#!/usr/bin/env python3
"""Genera le slide del Modulo 6 — AI nel lavoro quotidiano: casi d'uso reali (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 6",
    "AI nel lavoro quotidiano: casi d'uso reali",
    "Corso AI Basics  |  Durata: 3 ore  |  1h Teoria + 2h Workshop")

agenda_slide(prs, [
    "Dall'apprendimento all'azione: come integrare l'AI nel lavoro",
    "Workflow 1: Comunicazione — email, report, verbali",
    "Workflow 2: Analisi — dati, feedback, ricerca",
    "Workflow 3: Produttivita — automazione, template, procedure",
    "Workflow 4: Decisioni — confronti, SWOT, scenari",
    "Workshop: identifica e automatizza 3 task dal TUO lavoro",
    "Integrazione con gli strumenti di tutti i giorni",
    "Riepilogo e domande",
])

# ── 2. SEZIONE 1 — DALL'APPRENDIMENTO ALL'AZIONE ──────
section_slide(prs, 1, "Dall'apprendimento all'azione",
              "Il vero valore dell'AI e nella pratica quotidiana")

highlight_slide(prs,
    "LA DOMANDA CHIAVE",
    "Non 'cosa puo fare l'AI?'\n"
    "ma 'quali dei MIEI compiti\n"
    "puo rendere piu veloci o migliori?'",
    "Il ROI dell'AI si misura in tempo risparmiato e qualita migliorata sui TUOI task reali.")

content_slide(prs, "Come identificare i task 'AI-friendly'", [
    "Un task e ideale per l'AI quando e:",
    "",
    "  RIPETITIVO: lo fai spesso con variazioni minime",
    "     Es: email di risposta, report settimanali, meeting notes",
    "",
    "  TESTUALE: coinvolge leggere, scrivere, riassumere, tradurre",
    "     Es: documentazione, comunicazione, analisi qualitativa",
    "",
    "  STRUTTURABILE: il risultato segue uno schema prevedibile",
    "     Es: tabelle, liste, modelli standard, procedure",
    "",
    "  A BASSO RISCHIO: un errore non causa danni gravi",
    "     Es: bozze, brainstorming, esplorazioni (NON contratti legali finali)",
])

content_slide(prs, "Il framework 'Prima-Durante-Dopo'", [
    "Per ogni task, pensa all'AI in tre momenti:",
    "",
    "PRIMA — Preparazione e ricerca",
    "   Raccogliere informazioni, analizzare contesto, generare idee",
    "   Esempio: 'Preparami un briefing su questo cliente'",
    "",
    "DURANTE — Produzione e bozza",
    "   Scrivere la prima bozza, strutturare, formattare",
    "   Esempio: 'Scrivi la prima versione di questa email'",
    "",
    "DOPO — Revisione e miglioramento",
    "   Correggere, semplificare, tradurre, adattare il tono",
    "   Esempio: 'Rendi questo testo piu conciso e formale'",
    "",
    ">>> L'AI e piu utile nelle fasi PRIMA e DURANTE.",
    "    La fase DOPO resta prevalentemente umana.",
])

content_slide(prs, "La regola dell'80/20 con l'AI", [
    "L'AI genera l'80% del lavoro in il 20% del tempo",
    "TU aggiungi il 20% finale che fa la differenza:",
    "",
    "   AI genera la bozza (2 minuti)",
    "   Tu revisioni, personalizzi, verifichi (5 minuti)",
    "   TOTALE: 7 minuti invece di 30",
    "",
    "NON delegare tutto. Il valore aggiunto umano e:",
    "   - Giudizio di contesto (conosci il tuo interlocutore)",
    "   - Verifica fattuale (l'AI puo sbagliare)",
    "   - Tocco personale (relazioni, empatia, sfumature)",
    "   - Responsabilita (firmi tu, non l'AI)",
    "",
    ">>> L'obiettivo non e eliminare il lavoro, ma eliminare il lavoro noioso.",
])

# ── 3. SEZIONE 2 — WORKFLOW COMUNICAZIONE ──────────────
section_slide(prs, 2, "Workflow 1: Comunicazione",
              "Email, report, verbali e contenuti scritti")

content_slide(prs, "Email: il caso d'uso piu immediato", [
    "L'impiegato medio scrive 40+ email al giorno.",
    "L'AI puo dimezzare il tempo per le email di routine.",
    "",
    "TIPOLOGIE AUTOMATIZZABILI:",
    "   - Risposte a richieste informazioni standard",
    "   - Conferme, ringraziamenti, follow-up",
    "   - Solleciti cortesi",
    "   - Email di presentazione e cold outreach",
    "   - Riepilogo meeting inviato ai partecipanti",
    "",
    "WORKFLOW:",
    "   1. Copia il contenuto dell'email ricevuta",
    "   2. Prompt: 'Rispondi a questa email. Contesto: [X]. Tono: [Y].'",
    "   3. Rivedi, personalizza, invia",
])

content_slide(prs, "Report e documenti: dalla bozza al prodotto", [
    "Report settimanale, mensile, trimestrale — sempre la stessa struttura:",
    "",
    "WORKFLOW CON AI:",
    "   1. Prepara i dati (numeri, KPI, fatti chiave)",
    "   2. Prompt: 'Scrivi un report [TIPO] con questi dati: [DATI].",
    "      Struttura: [SEZIONI]. Destinatario: [CHI]. Max [N] parole.'",
    "   3. L'AI genera la bozza strutturata",
    "   4. Tu aggiungi: interpretazione, commenti, raccomandazioni",
    "",
    "SUGGERIMENTO AVANZATO (con Claude Projects):",
    "   Crea un progetto 'Report Mensile' con template e istruzioni.",
    "   Ogni mese, carica solo i nuovi dati. Claude sa gia il formato.",
    "",
    "RISPARMIO STIMATO: da 2-3 ore a 30-45 minuti per report.",
])

content_slide(prs, "Verbali di riunione: da appunti a documento", [
    "Problema: prendere appunti E partecipare attivamente e difficile.",
    "",
    "WORKFLOW:",
    "   1. Durante il meeting: annota parole chiave e decisioni",
    "      (anche in modo disordinato, abbreviazioni, frasi incomplete)",
    "   2. Dopo il meeting, incolla gli appunti in ChatGPT o Claude:",
    "      'Trasforma questi appunti in un verbale professionale.",
    "       Formato: data, partecipanti, punti discussi (numerati),",
    "       decisioni prese, azioni (con responsabile e scadenza).",
    "       Tono formale e sintetico.'",
    "   3. Rivedi, correggi nomi e dettagli specifici, invia",
    "",
    "Tempo: da 30 minuti di redazione a 5 minuti di revisione.",
])

content_slide(prs, "Contenuti social e comunicazione esterna", [
    "Post LinkedIn, newsletter, comunicati — l'AI come copywriter:",
    "",
    "WORKFLOW PER POST LINKEDIN:",
    "   1. Definisci il messaggio chiave (1 frase)",
    "   2. Prompt: 'Crea 3 versioni di un post LinkedIn su [TEMA].",
    "      Target: [CHI]. Stili: storytelling, dato statistico, lista.",
    "      100-150 parole, hook iniziale, CTA finale, 3 hashtag.'",
    "   3. Scegli la versione migliore, personalizza con la tua voce",
    "",
    "WORKFLOW PER NEWSLETTER:",
    "   1. Elenca i temi da coprire",
    "   2. Prompt: 'Scrivi una newsletter di 500 parole con questi temi: [...].",
    "      Tono: [BRAND]. Includi: intro accattivante, sezione per ogni tema,",
    "      CTA finale.'",
    "   3. Aggiungi link, immagini, revisiona il tono",
])

# ── 4. SEZIONE 3 — WORKFLOW ANALISI ────────────────────
section_slide(prs, 3, "Workflow 2: Analisi",
              "Dati, feedback, ricerche e sintesi")

content_slide(prs, "Analisi dati senza saper programmare", [
    "Con ChatGPT (Code Interpreter) chiunque puo analizzare dati:",
    "",
    "WORKFLOW:",
    "   1. Esporta i dati in CSV o Excel",
    "   2. Carica su ChatGPT e chiedi:",
    "      'Analizza questo dataset. Mostrami: trend principali con grafici,",
    "       anomalie, top/bottom performer. Concludi con 3 raccomandazioni.'",
    "   3. L'AI scrive ed esegue il codice Python per te",
    "   4. Scarica grafici e risultati",
    "",
    "CASI D'USO REALI:",
    "   - Vendite: trend, confronti periodo, segmentazione prodotto/regione",
    "   - HR: turnover, assenze, survey soddisfazione",
    "   - Marketing: performance campagne, conversion rate",
    "   - Finance: scostamenti budget, analisi costi",
])

content_slide(prs, "Analisi qualitativa: feedback e recensioni", [
    "Trasformare testo non strutturato in insight azionabili:",
    "",
    "WORKFLOW:",
    "   1. Raccogli i feedback (Google Reviews, survey, email, ticket)",
    "   2. Copia-incolla in Claude o ChatGPT:",
    "      'Analizza questi [N] feedback. Per ciascuno classifica:",
    "       sentiment, tema, urgenza. Poi: temi ricorrenti, punti critici,",
    "       punti di forza, 3 azioni prioritarie.'",
    "   3. Risultato: analisi strutturata da testo grezzo",
    "",
    "APPLICAZIONI:",
    "   - NPS verbatim: capire il 'perche' dietro i numeri",
    "   - Reclami: categorizzare e prioritizzare",
    "   - Survey interni: estrarre insight dalla workforce",
    "   - Review competitor: capire dove battono e dove soffrono",
])

content_slide(prs, "Ricerca e preparazione meeting", [
    "L'AI come analista junior che prepara i briefing per te:",
    "",
    "PRIMA DI UN MEETING CON UN CLIENTE:",
    "   'Preparami un briefing su [AZIENDA]. Copri: settore, dimensioni,",
    "    prodotti principali, sfide tipiche del settore, notizie recenti.",
    "    Poi suggerisci 5 domande intelligenti da porre nel meeting.'",
    "",
    "PRIMA DI UNA PRESENTAZIONE:",
    "   'Sto presentando [PROPOSTA] a [PUBBLICO]. Anticipa le 5 obiezioni",
    "    piu probabili e preparami una risposta per ciascuna.'",
    "",
    "PRIMA DI UNA NEGOZIAZIONE:",
    "   'Analizza i pro/contro della nostra posizione su [TEMA].",
    "    Identifica il nostro BATNA e suggerisci la strategia.',",
    "",
    ">>> Nota: verifica sempre i fatti con fonti indipendenti!",
])

# ── 5. SEZIONE 4 — WORKFLOW PRODUTTIVITA ───────────────
section_slide(prs, 4, "Workflow 3: Produttivita",
              "Automazione, template e procedure")

content_slide(prs, "Template riutilizzabili: crea una volta, usa sempre", [
    "L'approccio piu efficiente: farsi creare i template dall'AI",
    "",
    "STEP 1: Identifica un task ripetitivo (email, report, checklist)",
    "STEP 2: Chiedi all'AI di creare il template:",
    "   'Crea un template per [TIPO] con segnaposti [NOME], [DATA],",
    "    [DETTAGLIO]. Includi 3 varianti per contesti diversi.'",
    "STEP 3: Salva il template nel tuo archivio personale",
    "STEP 4: Ogni volta che serve, riempi solo i segnaposti",
    "",
    "ESEMPI DI TEMPLATE UTILI:",
    "   - 5 template email (conferma, sollecito, ringraziamento, etc.)",
    "   - Template report settimanale/mensile",
    "   - Checklist di avvio progetto",
    "   - Script per chiamate commerciali",
])

content_slide(prs, "Procedure operative (SOP) con l'AI", [
    "Documentare i processi e spesso trascurato ma fondamentale:",
    "",
    "WORKFLOW:",
    "   1. Descrivi il processo a voce (anche in modo informale)",
    "   2. Prompt: 'Trasforma questa descrizione in una SOP formale.",
    "      Struttura: scopo, chi la esegue, prerequisiti, procedura",
    "      passo-passo (numerata), criteri di successo, troubleshooting.',",
    "   3. Revisiona con chi esegue realmente il processo",
    "   4. Pubblica e distribuisci",
    "",
    "VANTAGGIO: il knowledge non resta nella testa di una sola persona.",
    "Se un collega va in ferie, la SOP copre.",
    "",
    ">>> Claude Projects e ideale: crea un progetto 'SOP Aziendali'",
    "    e aggiorna le procedure nel tempo.",
])

content_slide(prs, "Traduzione e localizzazione quotidiana", [
    "Oltre Google Translate: traduzioni adattate al contesto:",
    "",
    "TRADUZIONE DOCUMENTO:",
    "   'Traduci questo documento in inglese. Non tradurre letteralmente:",
    "    adatta il tono al mercato internazionale. Segnala le scelte",
    "    di adattamento significative.'",
    "",
    "LOCALIZZAZIONE MARKETING:",
    "   'Adatta questo testo promozionale per il mercato tedesco.",
    "    Considera differenze culturali e preferenze comunicative.'",
    "",
    "MULTILINGUAL SUPPORT:",
    "   'Ho ricevuto questa email in [LINGUA]. Traduci e suggeriscimi",
    "    una risposta appropriata nella stessa lingua.'",
    "",
    ">>> L'AI gestisce bene 20+ lingue. Per traduzioni critiche",
    "    (legali, mediche), fai comunque validare da un professionista.",
])

content_slide(prs, "Formazione e onboarding con l'AI", [
    "Creare materiale formativo diventa rapidissimo:",
    "",
    "QUIZ E VALUTAZIONI:",
    "   'Crea un quiz di 10 domande su [ARGOMENTO]. Mix di scelta",
    "    multipla e vero/falso. Livello: [BASE/AVANZATO].",
    "    Risposte alla fine con spiegazione.'",
    "",
    "GUIDE PER NUOVI ASSUNTI:",
    "   'Crea una guida di onboarding per un nuovo [RUOLO].",
    "    Piano 30 giorni: settimana per settimana con attivita,",
    "    obiettivi, persone da incontrare, risorse da leggere.'",
    "",
    "FAQ INTERNE:",
    "   'Basandoti su queste domande frequenti [LISTA], crea un",
    "    documento FAQ strutturato con risposte chiare e concise.'",
    "",
    ">>> Perfetto per team in crescita che devono scalare velocemente.",
])

# ── 6. SEZIONE 5 — WORKFLOW DECISIONI ──────────────────
section_slide(prs, 5, "Workflow 4: Supporto decisionale",
              "Confronti, scenari e analisi strategiche")

content_slide(prs, "Matrice decisionale assistita dall'AI", [
    "Quando devi scegliere tra piu opzioni:",
    "",
    "WORKFLOW:",
    "   1. Definisci le opzioni e i criteri di valutazione",
    "   2. Prompt: 'Confronta Opzione A [DESC] e Opzione B [DESC].",
    "      Criteri: costo (peso 3), qualita (peso 5), tempi (peso 4),",
    "      scalabilita (peso 2). Matrice 1-5 per criterio, punteggio",
    "      pesato, raccomandazione motivata.'",
    "   3. L'AI struttura il ragionamento che tu poi validi",
    "",
    "L'AI NON decide per te. L'AI ti aiuta a:",
    "   - Strutturare i criteri che altrimenti restano impliciti",
    "   - Non dimenticare aspetti importanti",
    "   - Visualizzare il confronto in modo oggettivo",
    "   - Documentare il processo decisionale",
])

content_slide(prs, "Analisi scenari 'what if'", [
    "Esplorare scenari futuri prima di prendere una decisione:",
    "",
    "PROMPT TIPO:",
    "   'Siamo un'azienda di [SETTORE] con [N] dipendenti.",
    "    Stiamo valutando di [DECISIONE].",
    "    Analizza 3 scenari:",
    "    - Scenario ottimistico: cosa succede se va tutto bene",
    "    - Scenario realistico: l'esito piu probabile",
    "    - Scenario pessimistico: cosa succede se va male",
    "    Per ogni scenario: probabilita stimata, impatto su fatturato,",
    "    impatto su team, azioni di mitigazione.'",
    "",
    "APPLICAZIONI: lancio prodotto, assunzioni, apertura mercato,",
    "    cambio fornitore, investimento tecnologico.",
])

content_slide(prs, "SWOT e analisi strategica rapida", [
    "L'AI come 'consulente strategico tascabile':",
    "",
    "ANALISI SWOT:",
    "   'Crea un'analisi SWOT per [AZIENDA/PROGETTO].",
    "    Contesto: [SETTORE, MERCATO]. 5 punti per quadrante,",
    "    con breve spiegazione. Concludi con 3 raccomandazioni.'",
    "",
    "ANALISI COMPETITIVA:",
    "   'Confronta la nostra offerta con i competitor [A, B, C].",
    "    Criteri: prezzo, qualita, servizio, innovazione.",
    "    Identifica il nostro vantaggio competitivo e 2 vulnerabilita.'",
    "",
    "ANALISI RISCHI:",
    "   'Identifica i 5 rischi principali per [PROGETTO/INIZIATIVA].",
    "    Per ciascuno: probabilita, impatto, azione di mitigazione.",
    "    Formato: matrice rischi.'",
])

# ── 7. SEZIONE 6 — WORKSHOP ────────────────────────────
section_slide(prs, 6, "Workshop: automatizza il TUO lavoro",
              "Identifica e automatizza 3 task reali — 60 min")

content_slide(prs, "Step 1: Identifica i tuoi 'time waster' (10 min)", [
    "Pensa alla tua settimana lavorativa tipica.",
    "Quali attivita ripetitive ti rubano piu tempo?",
    "",
    "Compila questa lista (almeno 5 attivita):",
    "   1. __________________________________ (~___ min/settimana)",
    "   2. __________________________________ (~___ min/settimana)",
    "   3. __________________________________ (~___ min/settimana)",
    "   4. __________________________________ (~___ min/settimana)",
    "   5. __________________________________ (~___ min/settimana)",
    "",
    "Ora seleziona le 3 piu adatte all'AI (ripetitive + testuali + basso rischio)",
    "e segna un asterisco (*) accanto.",
])

content_slide(prs, "Step 2: Progetta il workflow AI (15 min)", [
    "Per ciascuno dei 3 task selezionati, definisci:",
    "",
    "TASK 1: ___________________________",
    "   Quale tool? (ChatGPT / Claude / altro): _______________",
    "   Input: cosa devi fornire all'AI? _______________",
    "   Prompt: come lo chiederesti? _______________",
    "   Output atteso: cosa vuoi ottenere? _______________",
    "   Tempo stimato CON AI: ___ min (vs ___ min senza AI)",
    "",
    "Ripeti per Task 2 e Task 3.",
    "",
    "Suggerimento: inizia dal task piu semplice,",
    "cosi costruisci fiducia nel processo.",
])

content_slide(prs, "Step 3: Testa in diretta (25 min)", [
    "Ora PROVA davvero i tuoi 3 workflow con l'AI!",
    "",
    "Per ogni task:",
    "   1. Apri lo strumento scelto",
    "   2. Scrivi il prompt che hai progettato",
    "   3. Valuta il risultato: e utilizzabile?",
    "   4. Se no, itera e migliora il prompt",
    "   5. Quando sei soddisfatto, SALVA il prompt per riusarlo",
    "",
    "Mentre lavori, annota:",
    "   - Cosa ha funzionato subito",
    "   - Cosa ha richiesto iterazione",
    "   - Cosa non ha funzionato (e perche)",
    "",
    ">>> Il prompt che funziona e il tuo nuovo 'strumento di lavoro'.",
    "    Salvalo dove puoi ritrovarlo (note, documento, Project Claude).",
])

content_slide(prs, "Step 4: Condividi con il gruppo (10 min)", [
    "Ogni partecipante presenta brevemente:",
    "",
    "   1. Quale task hai automatizzato",
    "   2. Quale tool hai usato",
    "   3. Il prompt che ha funzionato meglio",
    "   4. Quanto tempo risparmi",
    "   5. Una cosa che ti ha sorpreso",
    "",
    "REGOLA: ascolta i prompt degli altri!",
    "   Spesso il workflow migliore lo trovi",
    "   adattando l'idea di un collega al tuo contesto.",
    "",
    ">>> A fine sessione, il formatore raccoglie i migliori prompt",
    "    e li condivide con tutto il gruppo come 'libreria di partenza'.",
])

# ── 8. SEZIONE 7 — INTEGRAZIONE STRUMENTI ──────────────
section_slide(prs, 7, "Integrazione con gli strumenti di lavoro",
              "Come l'AI si inserisce nel tuo ecosistema")

two_col_slide(prs, "AI nell'ecosistema Microsoft 365",
    "Microsoft Copilot", [
        "Integrato in Word, Excel, PowerPoint, Outlook",
        "Riassumi email e conversazioni Teams",
        "Genera bozze di documenti in Word",
        "Crea presentazioni da un brief",
        "Analizza dati in Excel con linguaggio naturale",
        "Richiede licenza Copilot Pro/Business",
    ],
    "Come usarlo oggi (senza Copilot)", [
        "Copia testo da Word a ChatGPT/Claude",
        "Esporta dati Excel in CSV, analizza con AI",
        "Genera struttura slide, poi monta in PPT",
        "Usa l'AI per le bozze, Office per il formatting",
        "Il workflow manuale funziona benissimo!",
        "Copilot lo rende solo piu fluido",
    ])

two_col_slide(prs, "AI nell'ecosistema Google Workspace",
    "Google Gemini in Workspace", [
        "Integrato in Gmail, Docs, Sheets, Slides",
        "'Aiutami a scrivere' in Gmail e Docs",
        "Formula AI in Sheets",
        "Generazione slide da prompt",
        "Riassunto email lunghe",
        "Disponibile con piani Business/Enterprise",
    ],
    "Come usarlo oggi (senza Gemini)", [
        "Copia da Docs a ChatGPT/Claude",
        "Esporta Sheets in CSV, analizza con AI",
        "Usa Google AI Studio per Gemini gratis",
        "Incolla il risultato nei tuoi documenti",
        "Il copia-incolla resta il metodo universale",
        "",
    ])

content_slide(prs, "L'approccio 'copia-incolla' funziona (e bene)", [
    "Non serve aspettare le integrazioni native.",
    "Il workflow universale e:",
    "",
    "   1. COPIA il contenuto dal tuo strumento di lavoro",
    "   2. INCOLLA in ChatGPT/Claude con un prompt mirato",
    "   3. REVISIONA l'output",
    "   4. COPIA il risultato e INCOLLA nel tuo strumento",
    "",
    "E 'primitivo'? Si. Funziona? Assolutamente si.",
    "",
    "Vantaggi del copia-incolla rispetto alle integrazioni native:",
    "   - Funziona con QUALSIASI strumento",
    "   - Hai il pieno controllo del prompt e del risultato",
    "   - Non richiede licenze aggiuntive",
    "   - Puoi scegliere il modello migliore per ogni task",
])

# ── 9. CHIUSURA ─────────────────────────────────────────
recap_slide(prs, [
    "Cerca i task 'AI-friendly': ripetitivi, testuali, strutturabili, a basso rischio",
    "Framework Prima-Durante-Dopo: l'AI aiuta piu nella preparazione e nella bozza",
    "Regola 80/20: l'AI fa l'80%, tu aggiungi il 20% che fa la differenza",
    "Comunicazione, analisi, produttivita, decisioni: 4 aree ad alto impatto",
    "Salva i prompt che funzionano: diventano i tuoi strumenti di lavoro",
    "Il copia-incolla e il workflow universale: non serve aspettare le integrazioni",
])

next_module_slide(prs,
    "Modulo 7: AI Responsabile\n"
    "(gia completato)\n\n"
    "Modulo 8: Progetto finale")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_06_casi_uso", "slides",
                   "Modulo_06_Casi_Uso.pptx")
salva(prs, out)
