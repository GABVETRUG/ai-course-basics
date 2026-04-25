#!/usr/bin/env python3
"""Genera le slide del Modulo 8 — Progetto finale e certificazione (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 8",
    "Progetto finale e certificazione",
    "Corso AI Basics  |  Durata: 2 ore  |  100% Pratica")

agenda_slide(prs, [
    "Obiettivi del progetto finale",
    "Briefing: cosa dovete realizzare",
    "Fase 1: progettazione del workflow (20 min)",
    "Fase 2: realizzazione con l'AI (40 min)",
    "Fase 3: preparazione presentazione (15 min)",
    "Presentazioni al gruppo (30 min)",
    "Quiz finale di certificazione (15 min)",
])

# ── 2. OBIETTIVI ────────────────────────────────────────
section_slide(prs, 1, "Obiettivi del progetto finale",
              "Dimostrare le competenze acquisite")

highlight_slide(prs,
    "OBIETTIVO",
    "Automatizzare un workflow reale\n"
    "del PROPRIO lavoro usando almeno\n"
    "2 strumenti AI diversi.",
    "Non un esercizio teorico: un deliverable che porterai in ufficio lunedi mattina.")

content_slide(prs, "Cosa dovrete dimostrare", [
    "1. IDENTIFICARE un task reale che beneficia dell'AI",
    "      Applicare il framework: ripetitivo, testuale, strutturabile",
    "",
    "2. SCEGLIERE gli strumenti giusti",
    "      Almeno 2 tool diversi (ChatGPT, Claude, HuggingChat, AI Studio)",
    "      Motivare la scelta: perche QUEL tool per QUEL task",
    "",
    "3. PROGETTARE i prompt efficaci",
    "      Usare le tecniche apprese (ruolo, contesto, formato, vincoli)",
    "",
    "4. PRODURRE un deliverable concreto",
    "      Qualcosa di usabile: template, procedura, report, analisi",
    "",
    "5. VALUTARE criticamente il risultato",
    "      Cosa ha funzionato, cosa no, dove serve intervento umano",
])

content_slide(prs, "Criteri di valutazione", [
    "Il progetto sara valutato su 5 criteri (ciascuno 1-5 punti):",
    "",
    "   PERTINENZA: il task scelto e realmente utile per il tuo lavoro?",
    "",
    "   PROMPT ENGINEERING: i prompt usati sono ben strutturati?",
    "     (ruolo, contesto, formato, vincoli, iterazione)",
    "",
    "   USO MULTI-TOOL: hai usato almeno 2 strumenti diversi?",
    "     Hai motivato la scelta?",
    "",
    "   QUALITA OUTPUT: il deliverable e utilizzabile cosi com'e?",
    "",
    "   PENSIERO CRITICO: hai identificato limiti, rischi e",
    "     dove serve l'intervento umano?",
    "",
    "PUNTEGGIO: ___/25     SUFFICIENZA: 15/25",
])

# ── 3. BRIEFING ─────────────────────────────────────────
section_slide(prs, 2, "Briefing del progetto",
              "Cosa realizzare e come")

content_slide(prs, "Idee di progetto per ispirarvi", [
    "COMUNICAZIONE:",
    "   - Kit di 10 template email per il tuo reparto",
    "   - Sistema per generare report settimanali automatici",
    "   - Workflow per verbali riunione in 5 minuti",
    "",
    "ANALISI:",
    "   - Dashboard analisi feedback clienti",
    "   - Report analisi dati di vendita con grafici",
    "   - Briefing automatico pre-meeting con clienti",
    "",
    "PRODUTTIVITA:",
    "   - SOP per un processo del tuo team (con checklist)",
    "   - Kit onboarding per nuovi assunti del tuo reparto",
    "   - Libreria di prompt per il tuo ruolo specifico",
    "",
    "STRATEGIA:",
    "   - Analisi SWOT del tuo prodotto/servizio",
    "   - Matrice decisionale per una scelta in corso",
])

content_slide(prs, "Struttura del deliverable", [
    "Il vostro progetto deve includere:",
    "",
    "1. SCHEDA PROGETTO (1 pagina):",
    "   - Task scelto e motivazione",
    "   - Strumenti AI utilizzati e perche",
    "   - Tempo stimato: con AI vs senza AI",
    "",
    "2. PROMPT DOCUMENTATI:",
    "   - I prompt usati, con la tecnica applicata",
    "   - Le iterazioni fatte e perche",
    "",
    "3. DELIVERABLE FINALE:",
    "   - L'output concreto prodotto (template, report, analisi...)",
    "",
    "4. VALUTAZIONE CRITICA (5 righe):",
    "   - Cosa ha funzionato e cosa no",
    "   - Dove e necessario l'intervento umano",
    "   - Come lo useresti nel lavoro quotidiano",
])

# ── 4. FASE 1 — PROGETTAZIONE ──────────────────────────
section_slide(prs, 3, "Fase 1: Progettazione",
              "Definisci il tuo workflow AI — 20 minuti")

content_slide(prs, "Compila la scheda progetto", [
    "NOME PROGETTO: _______________________________________________",
    "",
    "TASK: Quale attivita lavorativa vuoi automatizzare?",
    "_______________________________________________________________",
    "",
    "PERCHE: Quanto tempo ti richiede oggi? Quanto spesso lo fai?",
    "_______________________________________________________________",
    "",
    "TOOL 1: ________________  Perche: _____________________________",
    "TOOL 2: ________________  Perche: _____________________________",
    "",
    "OUTPUT ATTESO: cosa produrra il progetto?",
    "_______________________________________________________________",
    "",
    "Fai validare la scheda con il formatore prima di procedere.",
])

content_slide(prs, "Progetta i prompt (prima di scriverli!)", [
    "Per ogni step del workflow, pianifica il prompt PRIMA di inviarlo:",
    "",
    "PROMPT 1 (Tool: ___________):",
    "   Obiettivo: _________________________________________________",
    "   Tecnica: [ ] Ruolo [ ] Few-shot [ ] CoT [ ] Output strutturato",
    "   Bozza: _____________________________________________________",
    "",
    "PROMPT 2 (Tool: ___________):",
    "   Obiettivo: _________________________________________________",
    "   Tecnica: ___________________________________________________",
    "   Bozza: _____________________________________________________",
    "",
    "PROMPT 3 (eventuale follow-up / iterazione):",
    "   Obiettivo: _________________________________________________",
    "",
    ">>> Pianificare PRIMA e eseguire POI porta risultati migliori.",
])

# ── 5. FASE 2 — REALIZZAZIONE ──────────────────────────
section_slide(prs, 4, "Fase 2: Realizzazione",
              "Metti in pratica i tuoi workflow — 40 minuti")

content_slide(prs, "Esegui il tuo progetto", [
    "Ora e il momento di FARE. Segui il piano e annota tutto.",
    "",
    "CHECKLIST DI ESECUZIONE:",
    "   [ ] Ho aperto il Tool 1 e inviato il Prompt 1",
    "   [ ] Ho valutato la risposta: soddisfacente? Serve iterazione?",
    "   [ ] Ho iterato il prompt se necessario",
    "   [ ] Ho aperto il Tool 2 e inviato il Prompt 2",
    "   [ ] Ho combinato i risultati dei due tool",
    "   [ ] Ho revisionato l'output finale con occhio critico",
    "   [ ] Ho salvato prompt e risultati",
    "",
    "DURANTE IL LAVORO ANNOTA:",
    "   - Sorprese positive: cosa ha funzionato meglio del previsto",
    "   - Problemi: dove hai dovuto cambiare approccio",
    "   - Intervento umano: cosa hai corretto/aggiunto tu",
])

content_slide(prs, "Suggerimenti per il tempo", [
    "40 minuti passano velocemente. Gestisci il tempo cosi:",
    "",
    "   0-10 min: Esegui il primo prompt, valuta, itera",
    "   10-20 min: Passa al secondo tool, secondo prompt",
    "   20-30 min: Combina i risultati, revisiona l'output",
    "   30-40 min: Compila la valutazione critica, prepara il deliverable",
    "",
    "SE SEI IN DIFFICOLTA:",
    "   - Semplifica: riduci l'ambizione, fai meno cose ma bene",
    "   - Chiedi: al formatore o ai colleghi",
    "   - Cambia tool: se uno non funziona, prova l'altro",
    "",
    "SE HAI FINITO IN ANTICIPO:",
    "   - Aggiungi un terzo tool di confronto",
    "   - Migliora la qualita dei prompt",
    "   - Documenta meglio le iterazioni",
])

# ── 6. FASE 3 — PRESENTAZIONE ──────────────────────────
section_slide(prs, 5, "Fase 3: Presentazione",
              "Prepara e condividi il tuo progetto — 15 min prep + 30 min pres.")

content_slide(prs, "Prepara la tua presentazione (5 min)", [
    "Struttura della presentazione (MAX 5 minuti a persona):",
    "",
    "1. IL PROBLEMA (30 sec):",
    "   'Nel mio lavoro, devo fare [TASK] [FREQUENZA].",
    "    Mi richiede circa [TEMPO] ogni volta.'",
    "",
    "2. LA SOLUZIONE (1 min):",
    "   'Ho usato [TOOL 1] per [COSA] e [TOOL 2] per [COSA].'",
    "   Mostra i prompt chiave.",
    "",
    "3. IL RISULTATO (1 min):",
    "   Mostra il deliverable prodotto.",
    "   'Ora questo task mi richiede [NUOVO TEMPO] invece di [VECCHIO].'",
    "",
    "4. LEZIONI APPRESE (30 sec):",
    "   Cosa ha funzionato, cosa no, dove serve l'umano.",
    "",
    "5. DOMANDA AL GRUPPO (30 sec).",
])

content_slide(prs, "Durante le presentazioni degli altri", [
    "Mentre ascolti i colleghi, prendi nota di:",
    "",
    "   - Prompt che potresti riutilizzare nel TUO lavoro",
    "   - Tool usati in modi a cui non avevi pensato",
    "   - Workflow che potresti adattare al tuo contesto",
    "",
    "Dopo ogni presentazione:",
    "   - Fai una domanda o dai un feedback costruttivo",
    "   - Vota il progetto (scheda valutazione peer)",
    "",
    "REGOLA D'ORO:",
    "   Il valore piu grande di questa sessione non e il TUO progetto,",
    "   ma le idee che rubi dagli altri.",
    "",
    ">>> Il formatore raccogliera TUTTI i prompt presentati in un",
    "    documento condiviso: la vostra 'libreria di prompt di classe'.",
])

# ── 7. QUIZ E CERTIFICAZIONE ───────────────────────────
section_slide(prs, 6, "Quiz finale e certificazione",
              "Verifica le competenze acquisite — 15 minuti")

content_slide(prs, "Quiz finale: formato e regole", [
    "20 domande in 15 minuti",
    "",
    "Formato misto:",
    "   - 12 domande a scelta multipla (4 opzioni)",
    "   - 4 domande vero/falso",
    "   - 4 domande a risposta aperta breve (1-2 frasi)",
    "",
    "Copertura:",
    "   - Modulo 1-2: Fondamenti e prompt engineering (5 domande)",
    "   - Modulo 3-4-5: Strumenti specifici (7 domande)",
    "   - Modulo 6: Casi d'uso reali (4 domande)",
    "   - Modulo 7: AI responsabile (4 domande)",
    "",
    "Soglia di superamento: 60% (12/20)",
    "NON e consentito usare strumenti AI durante il quiz!",
])

content_slide(prs, "Certificazione", [
    "Al completamento del corso (quiz + progetto) riceverai:",
    "",
    "CERTIFICATO DI COMPLETAMENTO",
    "   'Corso AI Basics: Strumenti di Intelligenza Artificiale per Tutti'",
    "   Durata: 20 ore",
    "   Competenze: uso ChatGPT, Claude, modelli open source,",
    "   prompt engineering, AI responsabile, automazione workflow",
    "",
    "Il certificato attesta che sai:",
    "   - Usare i principali strumenti AI conversazionali",
    "   - Scrivere prompt efficaci con tecniche strutturate",
    "   - Scegliere lo strumento giusto per ogni task",
    "   - Applicare l'AI in modo responsabile e consapevole",
    "   - Integrare l'AI nel workflow lavorativo quotidiano",
])

# ── 8. CHIUSURA DEL CORSO ──────────────────────────────
section_slide(prs, 7, "Chiusura del corso",
              "Cosa portare a casa e prossimi passi")

content_slide(prs, "I vostri 'next step' dopo il corso", [
    "SETTIMANA 1: scegli UN task e automatizzalo con l'AI ogni giorno",
    "   Non cercare di cambiare tutto subito. Un task alla volta.",
    "",
    "MESE 1: costruisci la tua libreria personale di prompt",
    "   Ogni prompt che funziona va salvato e categorizzato.",
    "",
    "MESE 2-3: condividi con il team",
    "   Mostra ai colleghi cosa hai imparato. Diventa il 'referente AI'.",
    "",
    "CONTINUO: resta aggiornato",
    "   L'AI evolve velocemente. Segui le novita principali.",
    "   Newsletter consigliate: The Rundown AI, AI Tool Report",
    "",
    ">>> Avete gli strumenti. Ora servono pratica e costanza.",
])

content_slide(prs, "Risorse per continuare a imparare", [
    "PRATICA QUOTIDIANA:",
    "   Usa ChatGPT o Claude per almeno 1 task al giorno",
    "",
    "COMMUNITY:",
    "   r/ChatGPT e r/ClaudeAI su Reddit",
    "   Gruppi LinkedIn su AI e Prompt Engineering",
    "",
    "APPROFONDIMENTO:",
    "   Documentazione ufficiale ChatGPT e Claude",
    "   OpenAI Cookbook (guide avanzate, gratuito)",
    "   Anthropic Prompt Library (esempi di prompt, gratuito)",
    "",
    "TREND:",
    "   The Rundown AI (newsletter quotidiana)",
    "   AI Tool Report (novita strumenti)",
    "",
    ">>> Il miglior modo per imparare l'AI e... usare l'AI!",
])

recap_slide(prs, [
    "Avete imparato cos'e l'AI e come funzionano gli LLM (Mod. 1)",
    "Sapete scrivere prompt efficaci con tecniche strutturate (Mod. 2)",
    "Padroneggiate ChatGPT, Claude e i modelli open source (Mod. 3-4-5)",
    "Sapete applicare l'AI a casi d'uso reali del vostro lavoro (Mod. 6)",
    "Conoscete rischi, limiti e regole per un uso responsabile (Mod. 7)",
    "Avete realizzato un progetto concreto e portabile in ufficio (Mod. 8)",
])

highlight_slide(prs,
    "GRAZIE!",
    "L'intelligenza artificiale non sostituisce\n"
    "l'intelligenza umana.\n"
    "La amplifica.",
    "Il futuro appartiene a chi sa collaborare con l'AI, non a chi la ignora o la teme.")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_08_progetto_finale", "slides",
                   "Modulo_08_Progetto_Finale.pptx")
salva(prs, out)
