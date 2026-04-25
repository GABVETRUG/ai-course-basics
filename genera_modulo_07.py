#!/usr/bin/env python3
"""Genera le slide del Modulo 7 — AI Responsabile (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 7",
    "AI Responsabile: limiti, rischi e buone pratiche",
    "Corso AI Basics  |  Durata: 2 ore  |  1.5h Teoria + 0.5h Laboratorio")

agenda_slide(prs, [
    "Allucinazioni: il rischio numero uno",
    "Bias e equita: quando l'AI discrimina",
    "Privacy e dati sensibili: cosa NON dare all'AI",
    "Copyright e proprieta intellettuale",
    "EU AI Act: la normativa europea (cenni)",
    "Lab: creare una policy aziendale per l'uso dell'AI",
    "Riepilogo e domande",
])

# ── 2. SEZIONE 1 — ALLUCINAZIONI ───────────────────────
section_slide(prs, 1, "Allucinazioni",
              "Quando l'AI inventa con sicurezza")

highlight_slide(prs,
    "DEFINIZIONE",
    "Un'allucinazione e una risposta dell'AI che suona\n"
    "plausibile e sicura, ma e parzialmente\n"
    "o completamente FALSA.",
    "Il modello non 'sa' di star inventando. Per lui, sta semplicemente generando testo probabile.")

content_slide(prs, "Esempi reali di allucinazioni", [
    "Un avvocato USA ha citato in tribunale 6 sentenze inventate da ChatGPT",
    "   >>> Nessuna delle sentenze esisteva. E stato sanzionato dal giudice.",
    "",
    "ChatGPT ha inventato articoli scientifici con DOI e autori inesistenti",
    "   >>> Formato perfetto, contenuto completamente falso.",
    "",
    "Modelli AI hanno generato biografie con fatti mai accaduti",
    "   >>> Date, luoghi e dettagli plausibili ma inventati.",
    "",
    "Google Bard ha affermato che il telescopio James Webb ha scattato",
    "   la prima foto di un esopianeta (falso, era stato SPHERE/VLT).",
    "   >>> Errore nella demo di lancio, ha causato perdita di valore in borsa.",
])

content_slide(prs, "Perche accadono le allucinazioni?", [
    "1. Il modello NON accede a un database di fatti",
    "   Genera testo statisticamente probabile, non 'cerca' la verita",
    "",
    "2. Addestrato per essere FLUENTE, non necessariamente ACCURATO",
    "   Un testo fluente e convincente non e per forza corretto",
    "",
    "3. Non distingue tra 'so' e 'non so'",
    "   Non ha un meccanismo di 'incertezza' naturale",
    "",
    "4. Pattern di addestramento",
    "   Se ha visto molti testi con un certo pattern, lo riproduce",
    "   anche quando i dettagli specifici sono inventati",
])

content_slide(prs, "Come riconoscere le allucinazioni", [
    "SEGNALI D'ALLARME:",
    "",
    "Dettagli troppo specifici su fatti verificabili",
    "   (date, nomi, numeri, citazioni con riferimenti precisi)",
    "",
    "Risposta troppo sicura su argomenti controversi o di nicchia",
    "",
    "Informazioni che non riesci a confermare con una ricerca web",
    "",
    "Incongruenze interne nella stessa risposta",
    "",
    "Citazioni bibliografiche con titoli e DOI molto specifici",
    "   >>> Se sembra troppo preciso per essere vero, VERIFICA!",
])

content_slide(prs, "Tecniche di verifica anti-allucinazione", [
    "1. VERIFICA INCROCIATA: confronta la risposta con fonti affidabili",
    "   Google, Wikipedia, siti ufficiali, documenti interni",
    "",
    "2. CHIEDI LE FONTI: 'Cita le fonti di queste informazioni'",
    "   Se le fonti non esistono, e un'allucinazione",
    "",
    "3. CHIEDI DUE VOLTE: rifai la stessa domanda in una nuova chat",
    "   Risposte molto diverse = probabile allucinazione",
    "",
    "4. USA PIU STRUMENTI: confronta ChatGPT, Claude, ricerca web",
    "",
    "5. REGOLA D'ORO: mai pubblicare, inviare o decidere",
    "   basandosi solo sull'output AI senza verifica umana!",
])

# ── 3. SEZIONE 2 — BIAS ────────────────────────────────
section_slide(prs, 2, "Bias e equita",
              "Quando l'AI riproduce pregiudizi")

highlight_slide(prs,
    "DEFINIZIONE",
    "Il bias algoritmico e la tendenza di un modello AI\n"
    "a produrre risultati sistematicamente distorti\n"
    "che favoriscono o svantaggiano certi gruppi.",
    "L'AI non 'sceglie' di discriminare: riflette i pregiudizi presenti nei dati di addestramento.")

content_slide(prs, "Da dove viene il bias?", [
    "1. DAI DATI DI ADDESTRAMENTO",
    "   Internet non e neutrale: contiene stereotipi, sottorappresentazioni,",
    "   visioni culturali dominanti (anglocentrismo, etc.)",
    "",
    "2. DA CHI SELEZIONA I DATI",
    "   Le scelte di cosa includere/escludere introducono distorsioni",
    "",
    "3. DAI FEEDBACK UMANI",
    "   I valutatori umani usati per migliorare i modelli portano i loro bias",
    "",
    "4. DAL PROMPT STESSO",
    "   Come formuliamo la domanda puo orientare la risposta",
])

content_slide(prs, "Esempi reali di bias nell'AI", [
    "Amazon: sistema di screening CV penalizzava candidature femminili",
    "   >>> Addestrato su 10 anni di assunzioni prevalentemente maschili",
    "",
    "Generazione immagini: 'CEO' genera prevalentemente uomini bianchi",
    "   >>> Riflette lo squilibrio presente nelle immagini online",
    "",
    "Traduzione: lingue con genere neutro tradotte con stereotipi",
    "   'O bir doktor' (turco, neutro) tradotto 'He is a doctor'",
    "",
    "Chatbot: risposte diverse a seconda del nome dell'utente",
    "   Nomi 'etnici' ricevono a volte risposte meno dettagliate",
])

content_slide(prs, "Come mitigare il bias nell'uso quotidiano", [
    "1. CONSAPEVOLEZZA: sapere che il bias esiste e il primo passo",
    "",
    "2. PROMPT INCLUSIVI: evita di specificare genere/etnia quando non serve",
    "",
    "3. VERIFICA GLI OUTPUT: se l'AI produce liste di nomi, profili, esempi,",
    "   controlla che siano diversificati e rappresentativi",
    "",
    "4. TESTA CON VARIAZIONI: cambia il nome, il genere, l'origine",
    "   nel prompt e verifica se la risposta cambia ingiustamente",
    "",
    "5. SEGNALA: i principali provider hanno canali per segnalare bias",
    "   (feedback nei loro prodotti)",
])

# ── 4. SEZIONE 3 — PRIVACY ─────────────────────────────
section_slide(prs, 3, "Privacy e dati sensibili",
              "Cosa succede ai dati che inserisci nell'AI?")

content_slide(prs, "Cosa succede ai tuoi dati?", [
    "Quando inserisci testo in ChatGPT, Claude o altri strumenti:",
    "",
    "1. I dati vengono INVIATI ai server del provider (USA o Europa)",
    "",
    "2. Possono essere USATI PER ADDESTRARE il modello (dipende dal piano)",
    "   - ChatGPT Free: SI, per default (si puo disattivare)",
    "   - ChatGPT Plus/Enterprise: NO",
    "   - Claude Free: puo usarli per il miglioramento del servizio",
    "   - Claude Pro: no addestramento",
    "",
    "3. Vengono CONSERVATI per un periodo variabile (log, debug, sicurezza)",
    "",
    "4. Il personale del provider PUO visualizzarli (review qualita/sicurezza)",
])

content_slide(prs, "Dati che NON devi MAI inserire nell'AI", [
    "DATI PERSONALI IDENTIFICATIVI",
    "   Codice fiscale, numeri di carta, password, dati sanitari",
    "",
    "DATI AZIENDALI RISERVATI",
    "   Piani strategici, dati finanziari non pubblici, contratti",
    "",
    "DATI DEI CLIENTI",
    "   Nomi + dati sensibili, email con informazioni personali",
    "",
    "CODICE SORGENTE PROPRIETARIO",
    "   Algoritmi core, credenziali, chiavi API",
    "",
    "INFORMAZIONI LEGALI RISERVATE",
    "   Cause in corso, accordi NDA, documenti confidenziali",
])

table_slide(prs, "Policy privacy dei principali provider",
    ["Aspetto", "ChatGPT Free", "ChatGPT Enterprise", "Claude Pro"],
    [
        ["Addestramento su dati utente", "Si (disattivabile)", "No", "No"],
        ["Conservazione dati", "30 giorni", "30 giorni", "30 giorni"],
        ["Review umana", "Possibile", "No", "Possibile (sicurezza)"],
        ["Localizzazione dati", "USA", "USA/EU (opzione)", "USA"],
        ["Conformita GDPR", "Parziale", "Si", "Parziale"],
        ["Crittografia", "In transito", "In transito + a riposo", "In transito + a riposo"],
    ])

content_slide(prs, "GDPR e AI: cosa devi sapere", [
    "Il GDPR (Regolamento Generale sulla Protezione dei Dati) si applica anche all'AI",
    "",
    "Punti chiave:",
    "   - Inserire dati personali di terzi nell'AI richiede base giuridica",
    "   - L'azienda e RESPONSABILE dei dati inseriti dai dipendenti",
    "   - Il diritto all'oblio: puoi chiedere la cancellazione dei tuoi dati",
    "   - Profilazione automatizzata: diritto a non essere soggetti a decisioni",
    "     basate solo su trattamento automatizzato",
    "",
    ">>> In caso di dubbio, consulta il DPO (Data Protection Officer)",
    "    della tua organizzazione PRIMA di usare dati personali con l'AI",
])

content_slide(prs, "Best practice per la privacy", [
    "1. ANONIMIZZA: sostituisci nomi reali con fittizi prima di incollare",
    "   'Mario Rossi, CF RSSMRA80A01H501X' >>> 'Cliente A, CF XXXXXXXX'",
    "",
    "2. GENERALIZZA: rimuovi dettagli identificativi non necessari",
    "   'Ordine #45231 di Via Roma 15, Milano' >>> 'Ordine cliente, citta del nord'",
    "",
    "3. SEGMENTA: invia solo la porzione di dati strettamente necessaria",
    "",
    "4. CONTROLLA LE IMPOSTAZIONI: disattiva l'addestramento sui tuoi dati",
    "   (ChatGPT: Impostazioni > Controlli dati > Migliora il modello)",
    "",
    "5. USA PIANI ENTERPRISE quando possibile per dati aziendali",
])

# ── 5. SEZIONE 4 — COPYRIGHT ───────────────────────────
section_slide(prs, 4, "Copyright e proprieta intellettuale",
              "Chi possiede cio che l'AI produce?")

content_slide(prs, "Chi possiede l'output dell'AI?", [
    "La situazione legale e ancora IN EVOLUZIONE a livello globale",
    "",
    "Posizioni attuali:",
    "   USA: l'output di pura AI non e brevettabile/copyrightable",
    "        (l'input umano significativo puo rendere l'opera proteggibile)",
    "   UE: situazione in definizione con l'AI Act",
    "   Italia: nessuna normativa specifica ancora",
    "",
    "In pratica per l'uso aziendale:",
    "   - L'output AI e un PUNTO DI PARTENZA, non un prodotto finito",
    "   - Se lo modifichi sostanzialmente, la tua opera e protetta",
    "   - I provider (OpenAI, Anthropic) non rivendicano diritti sull'output",
])

content_slide(prs, "Rischi legali da conoscere", [
    "1. PLAGIO INVOLONTARIO: il modello puo riprodurre testi protetti",
    "   Se pubblica materiale troppo simile a fonti esistenti, rischi contestazioni",
    "",
    "2. MARCHI E LOGHI: non usare l'AI per creare loghi simili a marchi esistenti",
    "",
    "3. ATTRIBUZIONE: se usi AI per scrivere articoli/report ufficiali,",
    "   la tua organizzazione potrebbe richiedere disclosure",
    "",
    "4. RESPONSABILITA: l'output AI con errori e RESPONSABILITA TUA",
    "   Se pubblichi informazioni false generate dall'AI, ne rispondi tu",
    "",
    ">>> L'AI genera, TU verifichi e ti assumi la responsabilita",
])

content_slide(prs, "Linee guida per un uso sicuro del copyright", [
    "1. Non pubblicare output AI senza revisione e modifica umana",
    "2. Verifica sempre che l'output non sia troppo simile a fonti note",
    "3. Quando richiesto, dichiara l'uso dell'AI nella creazione del contenuto",
    "4. Non usare l'AI per aggirare paywall o riprodurre contenuti protetti",
    "5. Per contenuti critici (legali, medici, finanziari), fai validare da esperti",
    "6. Conserva i prompt usati come documentazione del processo creativo",
    "",
    "REGOLA PRATICA: se non lo firmeresti con il tuo nome,",
    "non lo pubblicare. L'AI e un assistente, non un autore.",
])

# ── 6. SEZIONE 5 — EU AI ACT ───────────────────────────
section_slide(prs, 5, "EU AI Act",
              "La normativa europea sull'Intelligenza Artificiale")

highlight_slide(prs,
    "EU AI ACT (2024)",
    "La prima legge al mondo che regola\n"
    "l'Intelligenza Artificiale in modo organico.\n"
    "In vigore graduale dal 2025 al 2027.",
    "Non si applica solo ai produttori di AI, ma anche a chi la UTILIZZA in contesti professionali.")

content_slide(prs, "Classificazione dei rischi", [
    "L'AI Act classifica i sistemi AI in 4 livelli di rischio:",
    "",
    "RISCHIO INACCETTABILE (VIETATO)",
    "   Social scoring, manipolazione subliminale, sorveglianza biometrica di massa",
    "",
    "RISCHIO ALTO (REGOLAMENTATO)",
    "   Selezione del personale, credito, sanita, giustizia, istruzione",
    "",
    "RISCHIO LIMITATO (OBBLIGHI DI TRASPARENZA)",
    "   Chatbot, deepfake, contenuti generati >>> obbligo di dichiarare l'uso AI",
    "",
    "RISCHIO MINIMO (NESSUN OBBLIGO)",
    "   Filtri spam, videogiochi, raccomandazioni prodotti",
])

content_slide(prs, "Impatti pratici per le aziende", [
    "Cosa cambia per chi USA l'AI in azienda (non solo chi la produce):",
    "",
    "1. TRASPARENZA: devi informare quando un contenuto e generato dall'AI",
    "   Esempio: chatbot di assistenza clienti deve dichiarare di essere AI",
    "",
    "2. SUPERVISIONE UMANA: decisioni ad alto impatto richiedono revisione umana",
    "   Esempio: screening CV con AI richiede validazione da HR umano",
    "",
    "3. DOCUMENTAZIONE: tenere traccia di come e perche si usa l'AI",
    "",
    "4. FORMAZIONE: i dipendenti che usano AI devono essere formati",
    "   (e questo corso e un primo passo!)",
    "",
    ">>> Le sanzioni possono arrivare fino al 7% del fatturato globale",
])

# ── 7. SEZIONE 6 — LABORATORIO ─────────────────────────
section_slide(prs, 6, "Laboratorio pratico",
              "Creare una policy aziendale per l'uso dell'AI")

content_slide(prs, "Perche serve una policy aziendale?", [
    "Senza una policy chiara, ogni dipendente decide da solo:",
    "   - Quali dati inserire (rischio privacy)",
    "   - Come usare l'output (rischio qualita)",
    "   - Se dichiarare l'uso dell'AI (rischio trasparenza)",
    "   - Quali strumenti usare (rischio sicurezza)",
    "",
    "Una policy aziendale:",
    "   - Protegge l'azienda da rischi legali",
    "   - Da linee guida chiare ai dipendenti",
    "   - Abilita l'uso responsabile e produttivo dell'AI",
    "   - Dimostra conformita normativa (AI Act)",
])

content_slide(prs, "Template: sezioni di una policy AI", [
    "1. SCOPO E AMBITO: a chi si applica, per quali attivita",
    "2. STRUMENTI AUTORIZZATI: lista dei tool approvati e piani consentiti",
    "3. DATI VIETATI: elenco chiaro di cosa NON inserire nell'AI",
    "4. VERIFICA OUTPUT: obbligo di revisione umana prima della pubblicazione",
    "5. TRASPARENZA: quando e come dichiarare l'uso dell'AI",
    "6. FORMAZIONE: requisiti minimi per i dipendenti",
    "7. RESPONSABILITA: chi e responsabile di errori nell'output AI",
    "8. REVISIONE: frequenza di aggiornamento della policy",
    "",
    ">>> Usa ChatGPT o Claude per creare una prima bozza, poi personalizzala!",
])

content_slide(prs, "Esercizio: scrivi la tua policy", [
    "In gruppi di 2-3 persone:",
    "",
    "1. Scegliete un'azienda tipo (la vostra o una fittizia)",
    "2. Usate il template della slide precedente",
    "3. Chiedete a Claude o ChatGPT di generare una prima bozza:",
    "   'Crea una policy aziendale per l'uso dell'AI generativa in",
    "    un'azienda di [settore] con [N] dipendenti. La policy deve",
    "    coprire: strumenti autorizzati, dati vietati, obbligo di verifica,",
    "    trasparenza, formazione. Tono formale, max 1 pagina.'",
    "4. Revisionate e personalizzate la bozza",
    "5. Presentate la vostra policy al gruppo (5 minuti)",
])

content_slide(prs, "Discussione: confronto tra policy", [
    "Dopo le presentazioni, discutiamo insieme:",
    "",
    "- Quali elementi sono COMUNI a tutte le policy?",
    "- Quali differenze sono emerse tra settori diversi?",
    "- La bozza generata dall'AI era gia buona o ha richiesto molto lavoro?",
    "- Cosa aggiungereste dopo questa discussione?",
    "",
    "TAKEAWAY: una buona policy e un DOCUMENTO VIVO",
    "che va aggiornato man mano che la tecnologia evolve.",
    "Pianificate una revisione almeno ogni 6 mesi.",
])

# ── 8. CHIUSURA ─────────────────────────────────────────
recap_slide(prs, [
    "Le allucinazioni sono inevitabili: VERIFICA SEMPRE prima di fidarti",
    "Il bias esiste nei dati e si riflette nell'AI: sii consapevole",
    "Mai inserire dati personali, riservati o sensibili nell'AI",
    "L'output AI e RESPONSABILITA TUA: l'AI assiste, tu decidi",
    "L'EU AI Act impone trasparenza, supervisione e formazione",
    "Una policy aziendale chiara protegge te e la tua organizzazione",
])

next_module_slide(prs,
    "Modulo 8: Progetto finale\n"
    "Metti in pratica tutto cio che hai imparato")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_07_ai_responsabile", "slides",
                   "Modulo_07_AI_Responsabile.pptx")
salva(prs, out)
