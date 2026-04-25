#!/usr/bin/env python3
"""Genera le slide del Modulo 2 — Prompt Engineering (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COPERTINA + AGENDA ───────────────────────────────
title_slide(prs,
    "Modulo 2",
    "Prompt Engineering: l'arte di chiedere bene",
    "Corso AI Basics  |  Durata: 3 ore  |  1h Teoria + 2h Laboratorio")

agenda_slide(prs, [
    "Cos'e il Prompt Engineering e perche e importante",
    "Anatomia di un buon prompt",
    "Tecniche fondamentali: zero-shot, few-shot, chain-of-thought, role-playing",
    "Lab 1: trasformare prompt vaghi in prompt efficaci",
    "Lab 2: scenari lavorativi reali (8 esercizi)",
    "Lab 3: confronto tra strumenti",
    "Errori comuni e come evitarli",
    "Riepilogo e domande",
])

# ── 2. SEZIONE 1 — COS'E IL PROMPT ENGINEERING ─────────
section_slide(prs, 1, "Cos'e il Prompt Engineering",
              "La competenza piu importante dell'era AI")

highlight_slide(prs,
    "DEFINIZIONE",
    "Il Prompt Engineering e l'arte di formulare\n"
    "istruzioni efficaci per ottenere dall'AI\n"
    "esattamente il risultato desiderato.",
    "Non serve saper programmare. Serve saper comunicare con precisione.")

content_slide(prs, "Perche il Prompt Engineering e cosi importante", [
    "Lo STESSO strumento puo dare risultati pessimi o eccellenti",
    "La differenza non e nel modello, ma in COME gli parli",
    "",
    "Prompt vago: 'Scrivi qualcosa sul marketing'",
    "   >>> Risultato generico, inutilizzabile",
    "",
    "Prompt efficace: 'Scrivi 5 idee per una campagna social media",
    "   per un ristorante italiano a Milano, target 25-40 anni,",
    "   budget limitato, tono informale e accattivante'",
    "   >>> Risultato specifico, azionabile, utile",
])

content_slide(prs, "Il prompt come interfaccia", [
    "Il prompt e la tua UNICA interfaccia con il modello AI",
    "Non puoi 'mostrare' cosa vuoi — devi DESCRIVERLO a parole",
    "",
    "Pensa al prompt come a un brief per un collega:",
    "   - Chi e il destinatario?",
    "   - Qual e l'obiettivo?",
    "   - Che formato vuoi?",
    "   - Che tono usare?",
    "   - Ci sono vincoli o requisiti specifici?",
    "",
    "Piu contesto dai, migliore sara il risultato.",
])

content_slide(prs, "Anatomia di un buon prompt", [
    "Un prompt efficace ha fino a 6 componenti:",
    "",
    "1. RUOLO — Chi deve essere l'AI (es: 'Sei un esperto di marketing')",
    "2. CONTESTO — Informazioni di background rilevanti",
    "3. COMPITO — Cosa deve fare, in modo specifico",
    "4. FORMATO — Come vuoi l'output (lista, tabella, email, ecc.)",
    "5. TONO — Formale, informale, tecnico, divulgativo",
    "6. VINCOLI — Lunghezza, lingua, cose da evitare",
    "",
    "Non servono sempre tutti e sei, ma piu ne usi, migliore sara il risultato.",
])

# ── 3. SEZIONE 2 — TECNICHE FONDAMENTALI ───────────────
section_slide(prs, 2, "Tecniche fondamentali",
              "Gli strumenti del prompt engineer")

two_col_slide(prs, "Tecnica 1: Zero-shot",
    "Cos'e", [
        "Dare un'istruzione diretta",
        "SENZA fornire esempi",
        "Il modello usa solo le sue conoscenze",
        "La tecnica piu semplice e immediata",
    ],
    "Esempio", [
        "Prompt:",
        "'Traduci in inglese: Buongiorno,",
        "come posso aiutarla?'",
        "",
        "Quando usarla:",
        "Per compiti semplici e ben definiti",
    ])

two_col_slide(prs, "Tecnica 2: Few-shot (con esempi)",
    "Cos'e", [
        "Fornire 2-3 ESEMPI di input/output",
        "Il modello impara il pattern dagli esempi",
        "Molto piu preciso dello zero-shot",
        "Ideale per compiti con formato specifico",
    ],
    "Esempio", [
        "Prompt:",
        "'Classifica il sentiment: ",
        "  Ottimo prodotto! -> Positivo",
        "  Pessima esperienza -> Negativo",
        "  Il pacco e arrivato -> Neutro",
        "  Fantastico servizio clienti -> ?'",
    ])

two_col_slide(prs, "Tecnica 3: Chain-of-Thought (ragionamento passo-passo)",
    "Cos'e", [
        "Chiedere all'AI di ragionare PASSO PER PASSO",
        "Migliora la qualita su problemi complessi",
        "Il modello 'mostra il suo lavoro'",
        "Riduce gli errori di ragionamento",
    ],
    "Esempio", [
        "Prompt:",
        "'Un negozio vende magliette a 25 euro.",
        "Sconto 20% + spedizione 5 euro.",
        "Quanto paga il cliente?",
        "Ragiona passo per passo.'",
    ])

two_col_slide(prs, "Tecnica 4: Role-playing",
    "Cos'e", [
        "Assegnare un RUOLO specifico all'AI",
        "Il modello adatta linguaggio e competenze",
        "Uno dei trucchi piu potenti e semplici",
        "Cambia drasticamente la qualita dell'output",
    ],
    "Esempio", [
        "Prompt:",
        "'Sei un nutrizionista sportivo con 20 anni",
        "di esperienza. Un atleta amatoriale ti chiede",
        "un piano alimentare per la settimana prima",
        "di una maratona. Rispondi in modo chiaro",
        "e pratico.'",
    ])

content_slide(prs, "Tecnica 5: Output strutturato", [
    "Chiedere esplicitamente un FORMATO specifico per la risposta",
    "",
    "Formati utili:",
    "   - Lista puntata o numerata",
    "   - Tabella (con colonne specifiche)",
    "   - JSON o CSV (per dati)",
    "   - Email gia formattata",
    "   - Schema con titoli e sottotitoli",
    "",
    "Esempio: 'Crea una tabella con 3 colonne: Strumento, Pro, Contro.",
    "   Confronta ChatGPT, Claude e Gemini per uso in ufficio.'",
])

content_slide(prs, "Tecnica 6: Decomposizione del compito", [
    "Spezzare un compito COMPLESSO in sotto-compiti piu semplici",
    "",
    "INVECE DI: 'Scrivi un business plan per un ristorante'",
    "",
    "MEGLIO:",
    "   1. 'Analizza il mercato della ristorazione a Milano'",
    "   2. 'Definisci il target di clientela per un ristorante giapponese'",
    "   3. 'Stima i costi di avvio per un locale da 40 posti'",
    "   4. 'Scrivi l'executive summary basandoti su queste informazioni'",
    "",
    "Ogni sotto-compito riceve piu attenzione e produce risultati migliori.",
])

content_slide(prs, "Tecnica 7: Vincoli e delimitazione", [
    "Aggiungere VINCOLI espliciti per controllare l'output",
    "",
    "Vincoli di lunghezza: 'Rispondi in massimo 100 parole'",
    "Vincoli di lingua: 'Rispondi in italiano formale'",
    "Vincoli di contenuto: 'Non usare gergo tecnico'",
    "Vincoli di esclusione: 'Non menzionare competitor'",
    "Vincoli di pubblico: 'Scrivi per un pubblico non tecnico'",
    "",
    "Senza vincoli, il modello decide da solo e spesso e troppo lungo",
    "e generico. I vincoli sono il tuo volante.",
])

content_slide(prs, "Iterazione e raffinamento", [
    "Il primo prompt raramente e quello perfetto",
    "",
    "Processo iterativo:",
    "   1. Scrivi il prompt iniziale",
    "   2. Leggi la risposta con occhio critico",
    "   3. Identifica cosa manca o cosa non va",
    "   4. RAFFINA il prompt aggiungendo contesto/vincoli",
    "   5. Ripeti fino a ottenere il risultato voluto",
    "",
    "E una CONVERSAZIONE, non un comando unico!",
    "Usa frasi come: 'Bene, ma ora rendi il tono piu informale'",
    "oppure: 'Ottimo, aggiungi anche una sezione sui rischi'",
])

content_slide(prs, "Errori comuni nel prompting", [
    "1. TROPPO VAGO: 'Dimmi qualcosa sull'AI'",
    "   >>> Aggiungi contesto e obiettivo specifico",
    "",
    "2. TROPPO LUNGO: prompt di 500 parole con informazioni irrilevanti",
    "   >>> Sii conciso ma completo",
    "",
    "3. ASPETTATIVE IRREALISTICHE: 'Scrivi il mio intero libro'",
    "   >>> Decomponere in sotto-compiti gestibili",
    "",
    "4. NESSUN FORMATO: non specificare come vuoi la risposta",
    "   >>> Sempre indicare il formato desiderato",
    "",
    "5. NON ITERARE: accettare la prima risposta senza raffinare",
    "   >>> Il prompt perfetto richiede 2-3 tentativi",
])

table_slide(prs, "Riepilogo tecniche",
    ["Tecnica", "Quando usarla", "Livello"],
    [
        ["Zero-shot", "Compiti semplici e diretti", "Base"],
        ["Few-shot", "Serve un formato/pattern specifico", "Base"],
        ["Chain-of-thought", "Ragionamento, calcoli, analisi", "Intermedio"],
        ["Role-playing", "Serve competenza di dominio", "Base"],
        ["Output strutturato", "Serve un formato preciso", "Base"],
        ["Decomposizione", "Compiti complessi", "Intermedio"],
        ["Vincoli", "Controllare lunghezza/tono/stile", "Base"],
        ["Iterazione", "Sempre! Dopo ogni risposta", "Base"],
    ])

# ── 4. SEZIONE 3 — LAB 1 ──────────────────────────────
section_slide(prs, 3, "Lab 1: Da prompt vaghi a prompt efficaci",
              "Esercitazione pratica — 30 minuti")

two_col_slide(prs, "Esercizio 1: Email professionale",
    "Prompt VAGO", [
        "'Scrivi un'email al capo'",
        "",
        "Problemi:",
        "- Nessun contesto",
        "- Nessun obiettivo",
        "- Nessun tono",
        "- Quale capo? Per dire cosa?",
    ],
    "Prompt EFFICACE", [
        "'Scrivi un'email formale al mio",
        "responsabile di dipartimento per",
        "richiedere 3 giorni di ferie dal",
        "15 al 17 luglio. Menziona che il",
        "progetto X sara completato entro",
        "il 14. Tono professionale, max 150",
        "parole.'",
    ])

two_col_slide(prs, "Esercizio 2: Riassunto di un documento",
    "Prompt VAGO", [
        "'Riassumi questo testo'",
        "",
        "Problemi:",
        "- Quanto lungo deve essere?",
        "- Per chi e il riassunto?",
        "- Quali aspetti evidenziare?",
        "- Che formato usare?",
    ],
    "Prompt EFFICACE", [
        "'Riassumi il documento in 5 punti",
        "chiave, ognuno di 1-2 frasi.",
        "Il riassunto e per il direttore",
        "commerciale che deve prendere una",
        "decisione. Evidenzia costi, tempi e",
        "rischi principali. Concludi con una",
        "raccomandazione.'",
    ])

two_col_slide(prs, "Esercizio 3: Analisi dati",
    "Prompt VAGO", [
        "'Analizza questi dati di vendita'",
        "",
        "Problemi:",
        "- Che tipo di analisi?",
        "- Quali metriche interessano?",
        "- Che confronti fare?",
        "- Come presentare i risultati?",
    ],
    "Prompt EFFICACE", [
        "'Analizza i dati di vendita allegati.",
        "Identifica: (1) i 3 prodotti con",
        "maggiore crescita, (2) il mese con",
        "il calo piu significativo, (3) trend",
        "anno su anno. Presenta i risultati",
        "in una tabella e concludi con 3",
        "azioni suggerite.'",
    ])

content_slide(prs, "Il tuo turno: esercitati!", [
    "Apri ChatGPT o Claude e prova:",
    "",
    "1. Scrivi un prompt VAGO per un compito a tua scelta",
    "2. Osserva la risposta: cosa manca? Cosa non va?",
    "3. Riscrivi il prompt usando le tecniche apprese:",
    "   - Aggiungi un RUOLO",
    "   - Specifica il CONTESTO",
    "   - Definisci il FORMATO dell'output",
    "   - Aggiungi VINCOLI",
    "4. Confronta le due risposte",
    "",
    ">>> Tempo: 10 minuti. Poi condividiamo i risultati!",
])

# ── 5. SEZIONE 4 — LAB 2 ──────────────────────────────
section_slide(prs, 4, "Lab 2: Scenari lavorativi reali",
              "8 scenari pratici dal mondo del lavoro — 45 minuti")

content_slide(prs, "Scenario 1: Brainstorming per un progetto", [
    "Contesto: Devi proporre idee innovative per il prossimo trimestre",
    "",
    "Prompt consigliato:",
    "'Sei un consulente strategico. La mia azienda vende software gestionale",
    "per PMI italiane. Il fatturato e stagnante da 2 trimestri.",
    "Genera 10 idee creative per aumentare le vendite nel Q3,",
    "considerando budget limitato e team di 5 persone.",
    "Per ogni idea indica: azione, costo stimato (basso/medio/alto),",
    "impatto atteso (1-5), tempi di implementazione.'",
    "",
    ">>> Prova su ChatGPT e Claude: quale ti da idee migliori?",
])

content_slide(prs, "Scenario 2: Redazione di un report", [
    "Contesto: Devi scrivere un report mensile per la direzione",
    "",
    "Prompt consigliato:",
    "'Scrivi un report executive di 1 pagina sui risultati del mese di giugno.",
    "Dati: vendite +12%, nuovi clienti 45, churn 3%, NPS 72.",
    "Struttura: Sintesi (3 righe), Risultati chiave (tabella),",
    "Criticita (lista), Azioni per il mese prossimo (3 punti).",
    "Tono professionale, numeri in evidenza, pronto per il CEO.'",
    "",
    ">>> Suggerimento: incolla dati reali (non sensibili) per risultati migliori",
])

content_slide(prs, "Scenario 3: Traduzione e localizzazione", [
    "Contesto: Devi tradurre contenuti marketing per il mercato estero",
    "",
    "Prompt consigliato:",
    "'Traduci il seguente testo dall'italiano all'inglese britannico.",
    "Non fare una traduzione letterale: adatta il tono al mercato UK.",
    "Mantieni un registro professionale ma accessibile.",
    "Se ci sono riferimenti culturali italiani, adattali al contesto UK.",
    "Dopo la traduzione, segnala eventuali passaggi dove hai fatto",
    "scelte di adattamento significative e perche.'",
    "",
    ">>> Il prompt 'adatta, non tradurre' fa tutta la differenza!",
])

content_slide(prs, "Scenario 4: Supporto decisionale", [
    "Contesto: Devi scegliere tra due fornitori / opzioni / strategie",
    "",
    "Prompt consigliato:",
    "'Aiutami a decidere tra le opzioni A e B per [decisione].",
    "Opzione A: [descrizione]. Opzione B: [descrizione].",
    "I miei criteri: costo, qualita, tempi di consegna, scalabilita.",
    "Crea una matrice decisionale pesata (tabella) con punteggio 1-5",
    "per ogni criterio. Concludi con una raccomandazione motivata.'",
    "",
    ">>> L'AI non decide per te, ma struttura il ragionamento!",
])

content_slide(prs, "Scenario 5: Preparare una presentazione", [
    "Contesto: Devi creare una presentazione per un meeting interno",
    "",
    "Prompt consigliato:",
    "'Crea la struttura di una presentazione di 10 slide su [argomento].",
    "Pubblico: dirigenti non tecnici. Durata: 15 minuti.",
    "Per ogni slide indica: titolo, 3-4 bullet point con il contenuto,",
    "suggerimento per un elemento visuale (grafico, icona, immagine).",
    "La prima slide e il titolo, l'ultima e 'Prossimi passi'.",
    "Tono: chiaro, orientato ai risultati, con dati dove possibile.'",
])

content_slide(prs, "Scenario 6: Social media e comunicazione", [
    "Contesto: Devi creare contenuti per i social aziendali",
    "",
    "Prompt consigliato:",
    "'Sei un social media manager per un'azienda di [settore].",
    "Crea 5 post per LinkedIn sul tema [argomento].",
    "Ogni post deve: essere 100-150 parole, avere un hook iniziale",
    "accattivante, includere una call-to-action finale,",
    "usare 3-5 hashtag pertinenti. Alterna formati: testo puro,",
    "lista puntata, domanda aperta, storytelling, dato statistico.'",
    "",
    ">>> Chiedi varianti fino a trovare il tono giusto per il tuo brand",
])

content_slide(prs, "Scenario 7: Analisi feedback clienti", [
    "Contesto: Hai raccolto recensioni/feedback e devi analizzarli",
    "",
    "Prompt consigliato:",
    "'Analizza i seguenti feedback dei clienti [incolla feedback].",
    "Per ciascuno classifica: sentiment (positivo/negativo/neutro),",
    "tema principale (prodotto/servizio/prezzo/assistenza),",
    "urgenza (alta/media/bassa).",
    "Poi crea un riepilogo con: temi ricorrenti, punti critici,",
    "suggerimenti di miglioramento prioritizzati, un indice di",
    "soddisfazione generale stimato.'",
    "",
    ">>> Perfetto per trasformare dati qualitativi in insight azionabili",
])

content_slide(prs, "Scenario 8: Automazione risposte email", [
    "Contesto: Devi rispondere a email ripetitive (richieste info, conferme...)",
    "",
    "Prompt consigliato:",
    "'Crea 5 template di risposta email per le richieste piu comuni:",
    "1. Richiesta informazioni sui nostri servizi",
    "2. Conferma appuntamento",
    "3. Sollecito pagamento (tono cortese)",
    "4. Ringraziamento post-meeting",
    "5. Risposta a reclamo",
    "Per ogni template: oggetto, corpo (max 100 parole), tono professionale",
    "ma cordiale. Includi segnaposti [NOME], [DATA], [DETTAGLIO].'",
])

# ── 6. SEZIONE 5 — LAB 3 ──────────────────────────────
section_slide(prs, 5, "Lab 3: Confronto tra strumenti",
              "Stesso prompt, risposte diverse — 30 minuti")

content_slide(prs, "Esercizio: prompt identico su 3 tool", [
    "Scegli UNO degli scenari del Lab 2",
    "Invia lo STESSO prompt a ChatGPT, Claude e HuggingChat",
    "",
    "Valuta ogni risposta su questi criteri (1-5):",
    "   - Pertinenza: risponde a cio che hai chiesto?",
    "   - Completezza: copre tutti i punti richiesti?",
    "   - Formato: rispetta la struttura richiesta?",
    "   - Qualita: linguaggio chiaro, contenuto utile?",
    "   - Originalita: idee interessanti o risposta banale?",
    "",
    "Compila la tabella di confronto nella scheda esercizi",
])

table_slide(prs, "Template confronto (compilalo tu!)",
    ["Criterio", "ChatGPT (1-5)", "Claude (1-5)", "HuggingChat (1-5)"],
    [
        ["Pertinenza", "", "", ""],
        ["Completezza", "", "", ""],
        ["Formato", "", "", ""],
        ["Qualita", "", "", ""],
        ["Originalita", "", "", ""],
        ["TOTALE", "", "", ""],
    ])

content_slide(prs, "Quando usare quale strumento?", [
    "Non esiste un tool 'migliore in assoluto' — dipende dal compito:",
    "",
    "ChatGPT eccelle in: uso generico, navigazione web, generazione immagini,",
    "   ampio ecosistema di plugin, community vastissima",
    "",
    "Claude eccelle in: analisi di documenti lunghi, qualita della scrittura,",
    "   precisione nelle istruzioni, ragionamento strutturato",
    "",
    "HuggingChat eccelle in: accesso gratuito illimitato, sperimentazione",
    "   con modelli diversi, privacy (puo funzionare senza login)",
    "",
    ">>> Il prompt engineer esperto sa scegliere lo strumento giusto!",
])

# ── 7. CHIUSURA ─────────────────────────────────────────
recap_slide(prs, [
    "Un buon prompt ha: ruolo, contesto, compito, formato, tono, vincoli",
    "Le tecniche chiave: zero-shot, few-shot, chain-of-thought, role-playing",
    "L'output strutturato e i vincoli sono i tuoi migliori alleati",
    "Iterare e raffinare e normale e necessario",
    "Ogni strumento ha punti di forza diversi — scegli in base al compito",
    "La pratica costante e l'unico modo per migliorare",
])

next_module_slide(prs,
    "Modulo 3: ChatGPT\n"
    "Padroneggiare lo strumento piu diffuso")

question_slide(prs)

# ── SALVA ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_02_prompt_engineering", "slides",
                   "Modulo_02_Prompt_Engineering.pptx")
salva(prs, out)
