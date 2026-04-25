#!/usr/bin/env python3
"""
genera_lab_materiali.py — Genera tutti i file di esempio per i laboratori:
  - CSV vendite per Modulo 3 (Code Interpreter) e Modulo 6 (Workshop)
  - CSV feedback clienti per Modulo 6
  - Documento lungo (report aziendale) per Modulo 4 (analisi Claude)
  - CSV survey dipendenti per Modulo 6
"""
import csv
import os
import random
import textwrap

random.seed(42)  # riproducibilita

BASE = os.path.dirname(os.path.abspath(__file__))

# ═══════════════════════════════════════════════════════════
# 1. DATASET VENDITE (Modulo 3 — Lab 2 + Modulo 6)
# ═══════════════════════════════════════════════════════════

def genera_vendite():
    mesi = [
        "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
        "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"
    ]
    prodotti = {
        "Software Gestionale": {"base": 45, "prezzo": 1200, "trend": 1.03},
        "Licenza Cloud":       {"base": 60, "prezzo": 800,  "trend": 1.06},
        "Assistenza Premium":  {"base": 30, "prezzo": 2500, "trend": 1.01},
        "Formazione":          {"base": 20, "prezzo": 600,  "trend": 0.98},
    }
    regioni = ["Nord", "Centro", "Sud"]
    pesi_regione = [0.50, 0.30, 0.20]
    venditori = [
        "Marco Bianchi", "Laura Rossi", "Giuseppe Verdi",
        "Anna Marino", "Luca Ferrari"
    ]

    rows = []
    for i_mese, mese in enumerate(mesi):
        for nome_prod, info in prodotti.items():
            for regione, peso_r in zip(regioni, pesi_regione):
                base_q = info["base"] * peso_r
                stagione = 1.0
                if i_mese in (0, 1):
                    stagione = 0.8
                elif i_mese in (5, 6):
                    stagione = 0.7  # calo estivo
                elif i_mese in (10, 11):
                    stagione = 1.25  # picco fine anno

                trend = info["trend"] ** i_mese
                q = int(base_q * stagione * trend * random.uniform(0.8, 1.2))
                if q < 1:
                    q = 1

                # Anomalia intenzionale: calo drastico Sud ad Agosto
                if mese == "Agosto" and regione == "Sud" and nome_prod == "Software Gestionale":
                    q = 2

                prezzo_u = info["prezzo"] * random.uniform(0.95, 1.05)
                fatturato = round(q * prezzo_u, 2)
                costo = round(fatturato * random.uniform(0.35, 0.55), 2)
                margine = round(fatturato - costo, 2)

                rows.append({
                    "Mese": mese,
                    "Mese_Num": i_mese + 1,
                    "Prodotto": nome_prod,
                    "Regione": regione,
                    "Venditore": random.choice(venditori),
                    "Quantita": q,
                    "Prezzo_Unitario": round(prezzo_u, 2),
                    "Fatturato": fatturato,
                    "Costo": costo,
                    "Margine": margine,
                })

    path = os.path.join(BASE, "modulo_03_chatgpt", "lab_materiali",
                        "vendite_2025.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  OK  {path}  ({len(rows)} righe)")

    # Copia anche per modulo 6
    path2 = os.path.join(BASE, "modulo_06_casi_uso", "lab_materiali",
                         "vendite_2025.csv")
    with open(path2, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  OK  {path2}  (copia)")


# ═══════════════════════════════════════════════════════════
# 2. FEEDBACK CLIENTI (Modulo 6 — analisi qualitativa)
# ═══════════════════════════════════════════════════════════

def genera_feedback():
    feedback_list = [
        # Positivi
        ("5", "Servizio eccellente, il team di assistenza ha risolto il problema in meno di un'ora. Molto soddisfatto."),
        ("5", "Il software gestionale ha semplificato enormemente il nostro lavoro. Lo consiglio a tutte le PMI."),
        ("4", "Buon prodotto nel complesso. L'interfaccia potrebbe essere piu intuitiva ma le funzionalita sono ottime."),
        ("5", "La formazione ricevuta e stata eccezionale. Il docente era preparato e disponibile. Torneremo sicuramente."),
        ("4", "Ottimo rapporto qualita-prezzo. L'unica pecca e la documentazione, che potrebbe essere piu completa."),
        ("5", "Assistenza premium impeccabile. Ogni volta che chiamo risolvono subito. Vale ogni centesimo."),
        ("4", "Migrazione al cloud gestita perfettamente. Un piccolo ritardo sulla timeline ma risultato ottimo."),
        # Neutri
        ("3", "Prodotto nella media. Fa quello che deve fare ma niente di eccezionale. Aspetto la prossima versione."),
        ("3", "Il corso era informativo ma troppo teorico. Avrei preferito piu esercitazioni pratiche."),
        ("3", "Funzionalita ok, ma l'app mobile e ancora molto limitata. Spero in aggiornamenti presto."),
        ("3", "Tempi di risposta dell'assistenza accettabili durante la settimana, molto lenti nel weekend."),
        # Negativi
        ("2", "Ho avuto problemi con la fatturazione per tre mesi consecutivi. Ogni volta devo chiamare per correggere."),
        ("1", "Il software si e bloccato durante la chiusura trimestrale, perdendo 2 ore di lavoro. Inaccettabile."),
        ("2", "Interfaccia confusa e poco intuitiva. Ho dovuto chiamare l'assistenza solo per configurare le email."),
        ("1", "Corso annullato 2 giorni prima senza alternativa proposta. Pessima organizzazione."),
        ("2", "La migrazione ha causato la perdita di alcuni dati storici. Il recupero ha richiesto 3 settimane."),
        ("2", "Prezzo aumentato del 30% al rinnovo senza preavviso adeguato. Sto valutando alternative."),
        ("1", "Tempi di attesa dell'assistenza superiori a 40 minuti. Per un servizio premium e vergognoso."),
        # Misti
        ("3", "Il prodotto in se e buono, ma il processo di onboarding e stato caotico. Servono guide migliori."),
        ("4", "Finalmente hanno aggiunto l'export in Excel! Era l'unica funzionalita che mancava. Ora sono soddisfatto."),
        ("2", "Seconda volta che segnalo lo stesso bug sul modulo fatture. A quanto pare non leggono i ticket."),
        ("4", "Buon supporto tecnico e team competente. Peccato che gli aggiornamenti siano troppo frequenti e rompano cose che funzionavano."),
        ("3", "Il webinar gratuito era interessante ma troppo breve. 30 minuti non bastano per un argomento cosi complesso."),
        ("5", "Ho convinto il mio responsabile a comprare il pacchetto enterprise dopo il trial. Il ROI si e visto subito."),
        ("1", "Contratto firmato a maggio, installazione completata a settembre. 4 mesi per un software cloud sono troppi."),
        ("4", "L'integrazione con il nostro ERP ha funzionato al primo tentativo. Complimenti al team tecnico."),
    ]

    random.shuffle(feedback_list)

    rows = []
    nomi = ["Mario R.", "Giulia T.", "Alessandro P.", "Francesca B.",
            "Roberto M.", "Chiara L.", "Davide S.", "Elena C.",
            "Stefano V.", "Valentina G.", "Andrea N.", "Sara D.",
            "Michele F.", "Claudia Z.", "Simone A.", "Paola I.",
            "Matteo O.", "Silvia U.", "Lorenzo E.", "Martina Q.",
            "Giorgio H.", "Federica K.", "Tommaso J.", "Beatrice W.",
            "Filippo X."]
    mesi_date = [
        "2025-01", "2025-01", "2025-02", "2025-02", "2025-03",
        "2025-03", "2025-04", "2025-04", "2025-05", "2025-05",
        "2025-06", "2025-06", "2025-07", "2025-07", "2025-08",
        "2025-08", "2025-09", "2025-09", "2025-10", "2025-10",
        "2025-11", "2025-11", "2025-12", "2025-12", "2025-12",
    ]
    canali = ["Google Review", "Email", "Survey NPS", "Ticket supporto",
              "LinkedIn", "Telefono", "Trustpilot"]

    for i, (voto, testo) in enumerate(feedback_list):
        rows.append({
            "ID": f"FB-{i+1:03d}",
            "Data": mesi_date[i % len(mesi_date)],
            "Cliente": nomi[i % len(nomi)],
            "Canale": random.choice(canali),
            "Voto": voto,
            "Feedback": testo,
        })

    path = os.path.join(BASE, "modulo_06_casi_uso", "lab_materiali",
                        "feedback_clienti.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  OK  {path}  ({len(rows)} feedback)")


# ═══════════════════════════════════════════════════════════
# 3. SURVEY DIPENDENTI (Modulo 6 — analisi HR)
# ═══════════════════════════════════════════════════════════

def genera_survey():
    reparti = ["Commerciale", "Sviluppo", "Marketing", "Amministrazione", "Supporto"]
    anzianita = ["< 1 anno", "1-3 anni", "3-5 anni", "5-10 anni", "> 10 anni"]
    commenti = [
        "Ottimo ambiente di lavoro, colleghi disponibili.",
        "Troppo carico di lavoro, servirebbero piu assunzioni.",
        "La formazione interna potrebbe essere migliorata.",
        "Mi piace il lavoro da remoto, spero continui.",
        "Lo stipendio non e competitivo rispetto al mercato.",
        "Il management ascolta poco le nostre proposte.",
        "Buone opportunita di crescita professionale.",
        "Gli strumenti di lavoro sono obsoleti.",
        "L'azienda sta crescendo e si sente l'energia positiva.",
        "Troppi meeting inutili che tolgono tempo al lavoro vero.",
        "Vorrei piu chiarezza sugli obiettivi aziendali.",
        "Il team e fantastico, ci supportiamo a vicenda.",
        "La comunicazione tra reparti e un problema serio.",
        "Apprezzo la flessibilita sugli orari.",
        "Non sono chiare le possibilita di promozione.",
        "",  # alcuni senza commento
        "",
        "",
    ]

    rows = []
    for i in range(60):
        rep = random.choice(reparti)
        anz = random.choice(anzianita)

        # Sviluppo piu soddisfatto, Supporto meno
        base = {"Sviluppo": 4, "Commerciale": 3.5, "Marketing": 3.8,
                "Amministrazione": 3.3, "Supporto": 2.8}
        b = base[rep]

        rows.append({
            "ID": f"SRV-{i+1:03d}",
            "Reparto": rep,
            "Anzianita": anz,
            "Soddisfazione_Generale": min(5, max(1, int(b + random.uniform(-1.5, 1.5)))),
            "Work_Life_Balance": min(5, max(1, int(b + random.uniform(-1, 1.5)))),
            "Crescita_Professionale": min(5, max(1, int(b + random.uniform(-2, 1)))),
            "Rapporto_Colleghi": min(5, max(1, int(b + random.uniform(-0.5, 2)))),
            "Rapporto_Management": min(5, max(1, int(b + random.uniform(-2, 1)))),
            "Strumenti_Lavoro": min(5, max(1, int(b + random.uniform(-1.5, 1)))),
            "Consiglierebbe_Azienda": random.choice(["Si", "Si", "Si", "No", "Forse"]) if b > 3 else random.choice(["Si", "No", "No", "Forse"]),
            "Commento": random.choice(commenti),
        })

    path = os.path.join(BASE, "modulo_06_casi_uso", "lab_materiali",
                        "survey_dipendenti.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  OK  {path}  ({len(rows)} risposte)")


# ═══════════════════════════════════════════════════════════
# 4. REPORT AZIENDALE (Modulo 4 — documento lungo per Claude)
# ═══════════════════════════════════════════════════════════

def genera_report():
    report = textwrap.dedent("""\
    ================================================================
    TECHSOLUTIONS S.R.L.
    REPORT ANNUALE 2025
    ================================================================

    INDICE
    1. Lettera dell'Amministratore Delegato
    2. Chi Siamo
    3. Risultati Finanziari
    4. Analisi per Business Unit
    5. Risorse Umane e Organizzazione
    6. Innovazione e Ricerca
    7. Sostenibilita e Responsabilita Sociale
    8. Rischi e Opportunita
    9. Piano Strategico 2026-2028
    10. Note e Disclaimer

    ================================================================
    1. LETTERA DELL'AMMINISTRATORE DELEGATO
    ================================================================

    Cari stakeholder,

    Il 2025 e stato un anno di trasformazione per TechSolutions. In un
    contesto macroeconomico caratterizzato da incertezza geopolitica e
    rapida evoluzione tecnologica, la nostra azienda ha saputo cogliere
    le opportunita offerte dall'Intelligenza Artificiale e dal cloud
    computing, registrando una crescita del fatturato del 18% rispetto
    all'anno precedente.

    Il risultato piu significativo non e stato solo numerico. Abbiamo
    completato con successo la migrazione dell'85% dei nostri clienti
    verso la piattaforma cloud, un traguardo che ci posiziona come
    leader nel segmento delle PMI italiane per le soluzioni gestionali
    in cloud.

    Guardando al futuro, il nostro Piano Strategico 2026-2028 si fonda
    su tre pilastri: espansione internazionale (mercati DACH e Iberia),
    integrazione dell'AI nei nostri prodotti, e sviluppo del canale
    di formazione come seconda linea di ricavo.

    La sfida piu grande resta l'attrazione e la retention dei talenti.
    Il turnover del 22% nel reparto Sviluppo ci impone una riflessione
    seria sulla nostra proposta di valore come datore di lavoro. Su
    questo fronte, il nuovo programma "TechGrowth" rappresenta la
    nostra risposta concreta.

    Ringrazio tutti i collaboratori, i clienti e i partner per la
    fiducia accordataci. Il meglio deve ancora venire.

    Maria Conti
    Amministratore Delegato


    ================================================================
    2. CHI SIAMO
    ================================================================

    TechSolutions S.r.l. e stata fondata nel 2008 a Milano con la
    missione di rendere accessibile la tecnologia alle piccole e medie
    imprese italiane.

    DATI SOCIETARI
    - Ragione sociale: TechSolutions S.r.l.
    - Sede legale: Via dell'Innovazione 42, 20135 Milano
    - Anno di fondazione: 2008
    - Dipendenti: 127 (al 31/12/2025)
    - Fatturato 2025: 14.2 milioni di euro
    - Settore: Software gestionale e servizi IT per PMI

    PRODOTTI E SERVIZI
    - GestPro Cloud: software gestionale ERP in cloud
    - GestPro Analytics: modulo di business intelligence
    - Assistenza Premium: supporto tecnico dedicato 24/7
    - TechAcademy: programmi di formazione IT per aziende

    CLIENTI
    Oltre 2.400 aziende clienti in tutta Italia, prevalentemente
    nel segmento 10-250 dipendenti. Settori principali: manifattura
    (35%), servizi professionali (25%), commercio (20%), altro (20%).

    CERTIFICAZIONI
    - ISO 9001:2015 (Qualita)
    - ISO 27001:2022 (Sicurezza delle informazioni)
    - SOC 2 Type II (in corso di ottenimento, previsto Q2 2026)


    ================================================================
    3. RISULTATI FINANZIARI
    ================================================================

    CONTO ECONOMICO SINTETICO (migliaia di euro)

    Voce                      2024        2025      Var %
    -------------------------------------------------------
    Ricavi totali            12.034      14.200     +18,0%
    - Licenze e abbonamenti   7.220       8.946     +23,9%
    - Assistenza Premium      2.408       2.698     +12,0%
    - Formazione              1.204       1.278      +6,1%
    - Servizi professionali   1.202       1.278      +6,3%
    Costi operativi           9.626      11.076     +15,1%
    - Personale               6.019       7.100     +18,0%
    - Infrastruttura cloud    1.443       1.704     +18,1%
    - Marketing e vendite     1.204       1.420     +17,9%
    - Generali e amm.           960         852     -11,3%
    EBITDA                    2.408       3.124     +29,7%
    Margine EBITDA            20,0%       22,0%
    Utile netto               1.204       1.704     +41,5%

    NOTA: La riduzione dei costi generali e amministrativi (-11,3%)
    e attribuibile all'automazione di processi interni tramite AI
    e alla rinegoziazione di contratti con fornitori.

    Il margine EBITDA e migliorato di 2 punti percentuali grazie
    alla scalabilita del modello cloud (costi marginali decrescenti
    all'aumentare della base clienti).

    ANALISI RICAVI PER TRIMESTRE

    Trimestre    Ricavi (K)    Var. vs Q prec.
    --------------------------------------------
    Q1 2025        3.050         -
    Q2 2025        3.380         +10,8%
    Q3 2025        3.410         +0,9%
    Q4 2025        4.360         +27,9%

    Il Q4 registra tradizionalmente il picco grazie ai rinnovi
    annuali e alle nuove acquisizioni legate al budget di fine anno
    delle aziende clienti. Il Q3 mostra un rallentamento stagionale
    legato al periodo estivo.


    ================================================================
    4. ANALISI PER BUSINESS UNIT
    ================================================================

    4.1 GESTPRO CLOUD (63% dei ricavi)

    Il prodotto principale ha registrato una crescita del 23,9%
    trainata dalla migrazione dei clienti on-premise al cloud
    e dall'acquisizione di 380 nuovi clienti netti.

    Metriche chiave:
    - ARR (Annual Recurring Revenue): 8,9M euro (+24%)
    - Clienti attivi: 2.420 (+18%)
    - Churn rate: 4,2% (in calo dal 5,8% del 2024)
    - NPS (Net Promoter Score): 52 (in aumento da 45)
    - ARPU (Average Revenue Per User): 3.696 euro/anno (+5%)

    L'introduzione del modulo AI per la categorizzazione automatica
    delle fatture (rilasciato in Q3) ha contribuito alla riduzione
    del churn e all'aumento dell'NPS.

    4.2 ASSISTENZA PREMIUM (19% dei ricavi)

    Crescita moderata (+12%) ma con margini elevati (65%).

    Metriche chiave:
    - Clienti Premium: 540 (22% della base clienti)
    - Tempo medio di risoluzione: 2,4 ore (target: 2 ore)
    - Soddisfazione assistenza: 4,3/5,0
    - Ticket mensili medi: 1.200

    Criticita: il tempo medio di risoluzione e ancora sopra il
    target. Il piano prevede l'introduzione di un chatbot AI per
    il primo livello di supporto entro Q2 2026.

    4.3 TECHACADEMY — FORMAZIONE (9% dei ricavi)

    La business unit formazione mostra la crescita piu debole (+6,1%).
    I corsi in aula tradizionali sono in calo (-15%), compensati
    parzialmente dalla crescita dei corsi online (+45%).

    Corsi erogati nel 2025:
    - Corsi in aula: 48 (vs 62 nel 2024)
    - Corsi online sincroni: 85 (vs 52 nel 2024)
    - Corsi on-demand: 12 titoli disponibili (vs 5 nel 2024)
    - Partecipanti totali: 1.840 (+8%)

    Piano: nel 2026 verra lanciata la piattaforma e-learning
    "TechAcademy Online" con modello subscription (target: 200
    abbonamenti nel primo anno, ARPU 1.200 euro/anno).

    4.4 SERVIZI PROFESSIONALI (9% dei ricavi)

    Consulenza, personalizzazione e integrazione. Crescita del 6,3%
    con margini stabili al 40%.

    Nota: il management sta valutando se questa BU debba rimanere
    standalone o essere integrata come servizio accessorio alle
    altre BU. Decision attesa entro Q1 2026.


    ================================================================
    5. RISORSE UMANE E ORGANIZZAZIONE
    ================================================================

    ORGANICO

    Reparto              2024    2025    Var.
    ------------------------------------------
    Sviluppo               42      48    +14%
    Commerciale             22      25    +14%
    Supporto tecnico        18      20    +11%
    Marketing               12      14    +17%
    Amministrazione         10      10      0%
    Management               8      10    +25%
    TOTALE                 112     127    +13%

    ETA MEDIA: 34 anni | 42% donne, 58% uomini

    TURNOVER
    Il turnover complessivo e stato del 19%, con un picco del 22%
    nel reparto Sviluppo. Le cause principali emerse dalle exit
    interview sono:
    1. Retribuzione non competitiva rispetto al mercato (52%)
    2. Limitate opportunita di crescita verticale (28%)
    3. Workload eccessivo (15%)
    4. Altro (5%)

    INIZIATIVE 2025
    - Programma "TechGrowth": percorsi di carriera strutturati
    - Aumento budget formazione del 40%
    - Introduzione smart working ibrido (3 giorni remoto/settimana)
    - Revisione bande retributive (completata in Q4, effettiva da Q1 2026)

    OBIETTIVO 2026: ridurre il turnover al 15% (-4pp vs 2025).


    ================================================================
    6. INNOVAZIONE E RICERCA
    ================================================================

    Investimento in R&D: 1,42M euro (10% dei ricavi, +30% vs 2024).

    PROGETTI COMPLETATI NEL 2025
    1. AI Invoice Classifier: categorizzazione automatica fatture
       con accuratezza del 94%. Rilasciato in Q3 2025.
    2. Dashboard Analytics v2: nuova interfaccia BI con grafici
       interattivi e report personalizzabili.
    3. Mobile App v3: riscrittura completa dell'app mobile con
       funzionalita offline.

    PROGETTI IN CORSO (rilascio previsto 2026)
    1. AI Chatbot Supporto: primo livello di assistenza automatizzato.
       Obiettivo: gestire il 40% dei ticket senza intervento umano.
       Stato: beta testing con 50 clienti pilota.
    2. GestPro Marketplace: piattaforma per plugin di terze parti.
       Obiettivo: creare un ecosistema di partner sviluppatori.
       Stato: architettura completata, SDK in sviluppo.
    3. Integrazione con AI generativa: permettere ai clienti di
       interrogare i propri dati aziendali in linguaggio naturale.
       Stato: proof of concept completato, roadmap in definizione.

    BREVETTI E PROPRIETA INTELLETTUALE
    - 2 brevetti depositati nel 2025 (AI Invoice Classifier, algoritmo
      di anomaly detection per transazioni)
    - 1 brevetto in fase di valutazione


    ================================================================
    7. SOSTENIBILITA E RESPONSABILITA SOCIALE
    ================================================================

    IMPATTO AMBIENTALE
    La migrazione al cloud ha permesso la dismissione di 3 data center
    on-premise, con una riduzione stimata del 35% delle emissioni di CO2
    legate all'infrastruttura IT.

    Il cloud provider utilizzato (AWS, region eu-south-1 Milano) si
    e impegnato a raggiungere il 100% di energia rinnovabile entro il 2025.

    INIZIATIVE SOCIALI
    - "Code4Future": programma di mentoring per studenti universitari
      (24 studenti nel 2025, 8 assunti dopo lo stage)
    - "TechForGood": 200 ore di consulenza pro-bono per 5 ONG
    - Donazione del 2% dell'utile netto a progetti STEM (34.000 euro)

    DIVERSITY & INCLUSION
    - 42% donne nell'organico complessivo (+3pp vs 2024)
    - 30% donne in ruoli tecnici (+5pp vs 2024)
    - Obiettivo 2026: 35% donne in ruoli tecnici, 25% nel management


    ================================================================
    8. RISCHI E OPPORTUNITA
    ================================================================

    RISCHI PRINCIPALI

    1. CONCENTRAZIONE RICAVI
       Il 15% del fatturato dipende dai top 10 clienti.
       Mitigazione: diversificazione base clienti, nessun cliente
       sopra il 3% del fatturato.

    2. RETENTION TALENTI
       Il turnover nel reparto Sviluppo (22%) minaccia la capacita
       di esecuzione. Mitigazione: programma TechGrowth, revisione
       retributiva, employer branding.

    3. CYBERSECURITY
       L'aumento della superficie d'attacco legata al cloud richiede
       investimenti continui. Budget cybersecurity 2026: +25%.

    4. REGOLAMENTAZIONE AI
       L'EU AI Act imporra nuovi requisiti sui prodotti che integrano
       AI. Impatto atteso: costi di compliance +150K euro nel 2026.

    5. CONCORRENZA
       Ingresso di player internazionali (SAP Business One, Zoho)
       nel segmento PMI italiano. Differenziazione: localizzazione
       e assistenza in lingua italiana.

    OPPORTUNITA

    1. MERCATO AI PER PMI
       Il 72% delle PMI italiane non utilizza ancora strumenti AI.
       TechSolutions e posizionata per essere il partner di riferimento.

    2. ESPANSIONE INTERNAZIONALE
       I mercati DACH (Germania, Austria, Svizzera) e Iberia mostrano
       domanda crescente per soluzioni cloud ERP localizzate.

    3. FORMAZIONE COME RICAVO RICORRENTE
       La piattaforma TechAcademy Online puo generare ricavi ad alto
       margine con costi incrementali minimi.

    4. PARTNERSHIP STRATEGICHE
       Accordi con system integrator e studi commercialisti per
       ampliare il canale di vendita indiretto.


    ================================================================
    9. PIANO STRATEGICO 2026-2028
    ================================================================

    VISIONE: Diventare il partner tecnologico di riferimento per le
    PMI in Europa meridionale, con soluzioni AI-powered accessibili.

    OBIETTIVI TRIENNALI

    Metrica               2025 (actual)   2028 (target)
    -------------------------------------------------------
    Fatturato             14,2M euro      25M euro
    Clienti attivi        2.420           4.500
    Dipendenti            127             200
    Margine EBITDA        22%             25%
    % ricavi esteri       2%              15%
    NPS                   52              60
    Turnover              19%             12%

    PILASTRI STRATEGICI

    Pilastro 1: AI-Powered Products
    - Integrare AI generativa in tutti i prodotti entro 2027
    - Lanciare GestPro Copilot (assistente AI per gli utenti)
    - Obiettivo: 60% dei clienti utilizza almeno una feature AI

    Pilastro 2: Espansione Internazionale
    - Q3 2026: apertura ufficio commerciale a Monaco di Baviera
    - Q1 2027: localizzazione prodotto per mercato spagnolo
    - Q4 2027: partnership con distributori locali in Austria e Svizzera

    Pilastro 3: TechAcademy Online
    - Q2 2026: lancio piattaforma e-learning
    - 2027: 500 abbonati, certificazioni riconosciute
    - 2028: formazione come 15% dei ricavi (vs 9% attuale)

    INVESTIMENTI PREVISTI
    - R&D: 5M euro nel triennio (+18% annuo)
    - Internazionalizzazione: 2M euro (uffici, marketing, localizzazione)
    - TechAcademy: 800K euro (piattaforma, contenuti, marketing)
    - Totale: ~8M euro, finanziati da cash flow operativo e linea di
      credito gia negoziata con Intesa Sanpaolo.


    ================================================================
    10. NOTE E DISCLAIMER
    ================================================================

    Questo report e stato redatto a scopi formativi come materiale di
    esempio per il corso "AI Basics: Strumenti di Intelligenza
    Artificiale per Tutti".

    TechSolutions S.r.l. e un'azienda fittizia. Tutti i dati, i nomi
    e le informazioni contenute in questo documento sono inventati e
    non corrispondono a persone, aziende o situazioni reali.

    Il documento e progettato per essere utilizzato come materiale di
    esercitazione per:
    - Analisi di documenti lunghi con Claude (Modulo 4)
    - Estrazione di insight e riassunti esecutivi
    - Domande progressive a diversi livelli di profondita
    - Identificazione di rischi, opportunita e contraddizioni

    Lunghezza: circa 15 pagine (~2.500 parole)
    Struttura: 10 sezioni con dati quantitativi e qualitativi

    ================================================================
    Fine del Report — TechSolutions S.r.l. — Report Annuale 2025
    ================================================================
    """)

    path = os.path.join(BASE, "modulo_04_claude", "lab_materiali",
                        "Report_Annuale_TechSolutions_2025.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  OK  {path}  ({len(report.splitlines())} righe)")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  GENERAZIONE MATERIALI LABORATORIO — Corso AI Basics")
    print("=" * 60)
    genera_vendite()
    genera_feedback()
    genera_survey()
    genera_report()
    print("=" * 60)
    print("  Completato!")
    print("=" * 60)
