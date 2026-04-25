# Guida del Formatore

**Corso AI Basics: Strumenti di Intelligenza Artificiale per Tutti**

---

## Prima del corso

### Preparazione aula
- [ ] Proiettore/schermo funzionante (le slide sono 16:9)
- [ ] Wi-Fi stabile (i partecipanti useranno strumenti web)
- [ ] Prese elettriche sufficienti per i portatili
- [ ] Stampare le schede esercizi (1 copia per partecipante per modulo)
- [ ] Stampare la Scheda Progetto + Quiz (Modulo 8)

### Preparazione account del formatore
- [ ] Account ChatGPT Plus (per mostrare tutte le funzionalita)
- [ ] Account Claude Pro (per mostrare Opus, Artifacts, Projects)
- [ ] Account HuggingChat
- [ ] Account Google AI Studio
- [ ] Testare tutti gli accessi il giorno prima (le piattaforme possono cambiare)

### Materiale di backup
- [ ] Screenshot delle interfacce (in caso di problemi di connessione)
- [ ] PDF di esempio da usare per le demo live
- [ ] Dataset CSV di esempio per il lab di Code Interpreter (Mod. 3)
- [ ] Un documento lungo (10+ pagine) per il lab Claude (Mod. 4)

### Comunicazione pre-corso
Inviare ai partecipanti 3-5 giorni prima:
- Programma del corso
- Richiesta di creare account: ChatGPT, Claude (link nella mail)
- Portare un documento di lavoro (non sensibile) per gli esercizi
- Ricordare di portare portatile e caricatore

---

## Linee guida di conduzione

### Ritmo e energia
- **Mai piu di 30 minuti di teoria** senza un momento pratico o interattivo
- **Demo live > slide**: quando possibile, mostra direttamente sullo strumento
- **Errori live = opportunita**: se l'AI sbaglia durante una demo, e un momento didattico perfetto
- **Pause**: 10 min ogni 90 minuti. I lab contano come "pausa attiva"

### Gestione del pubblico non tecnico
- **Zero gergo non spiegato**: ogni termine tecnico va definito la prima volta
- **Analogie prima delle definizioni**: "E come l'autocompletamento del telefono, ma molto piu sofisticato"
- **Validare la frustrazione**: "E normale se non funziona al primo tentativo, fa parte del processo"
- **No giudizio sulle domande**: "Ottima domanda" e la risposta giusta a qualsiasi domanda

### Gestione problemi tecnici
| Problema | Soluzione |
|----------|----------|
| Account non creato | Aiutare in loco, allocare 5 min extra al Modulo 1 |
| ChatGPT/Claude non risponde | Usare HuggingChat come backup |
| Wi-Fi lento | Passare a slide + demo da schermo del formatore |
| Rate limit raggiunto | Usare un tool alternativo o l'account del formatore per la demo |
| Partecipante rimane indietro | Assegnare un "buddy" tra i partecipanti piu veloci |

---

## Note modulo per modulo

### Modulo 1 — Cos'e l'AI (2h)

**Punto critico**: la sezione "Come funziona un LLM" puo sembrare astratta.
- Usa l'analogia dell'autocompletamento del telefono: fai vedere come il telefono suggerisce la parola successiva, poi spiega che un LLM fa la stessa cosa ma su scala enormemente piu grande.
- Demo live: scrivi una frase incompleta in ChatGPT e mostra come la completa.

**Lab**: assicurati che tutti abbiano accesso ai 3 tool PRIMA di iniziare. Dedica 5-10 minuti al setup se necessario.

**Domande frequenti**:
- "L'AI mi rubera il lavoro?" — Rassicurare: l'AI e uno strumento, come Excel. Chi sa usarla avra un vantaggio, non sara sostituito.
- "I miei dati sono al sicuro?" — Anticipare brevemente il tema (approfondito nel Modulo 7).

---

### Modulo 2 — Prompt Engineering (3h)

**Punto critico**: passare dalla teoria alla pratica. I partecipanti tendono a scrivere prompt vaghi nonostante le spiegazioni.
- Tecnica: mostra il prompt VAGO e il risultato scadente prima del prompt EFFICACE. L'effetto "prima/dopo" e molto convincente.
- Fai compilare la checklist delle tecniche usate dopo ogni esercizio.

**Lab 2 (scenari lavorativi)**: non e necessario fare tutti e 8 gli scenari. I partecipanti scelgono almeno 4 in base alla rilevanza per il loro lavoro.

**Lab 3 (confronto)**: questo lab genera sempre discussioni interessanti. Lascia almeno 10 minuti per il debrief di gruppo.

---

### Modulo 3 — ChatGPT (3h)

**Demo consigliate** (fai tu davanti a tutti):
1. Upload di un PDF e riassunto (2 min)
2. Analisi di un CSV con Code Interpreter + generazione grafico (5 min)
3. Generazione immagine con DALL-E (2 min)

**Lab 4 (GPT custom)**: e il lab piu ambizioso. Alcuni partecipanti potrebbero non riuscire a completarlo. Va bene: l'obiettivo e INIZIARE la creazione, non per forza pubblicare.

**Attenzione**: le interfacce di ChatGPT cambiano frequentemente. Verifica screenshot e istruzioni nelle slide 1-2 giorni prima dell'erogazione.

---

### Modulo 4 — Claude (3h)

**Demo consigliate**:
1. Caricare un documento lungo e fare domande progressive (3 min)
2. Creare un Artifact calcolatore interattivo (3 min) — effetto "wow" garantito
3. Mostrare un Project gia configurato (2 min)

**Lab 2 (Artifacts)**: i partecipanti restano spesso sorpresi dalle capacita degli Artifacts. Lascia tempo extra per l'esplorazione libera.

**Confronto Claude vs ChatGPT**: evita di schierarti. Il messaggio deve essere: "strumenti diversi per esigenze diverse".

---

### Modulo 5 — Modelli Open (2h)

**Punto critico**: i partecipanti non tecnici potrebbero percepire i modelli open come "di serie B". Contrasta questa percezione con il lab di confronto.

**Google AI Studio**: l'interfaccia e piu tecnica. Guida i partecipanti passo per passo nel primo accesso. Focalizzati sull'esperimento con la temperatura — e il concetto che resta piu impresso.

**Messaggio chiave**: non serve saper programmare per usare i modelli open. HuggingChat e semplice come ChatGPT.

---

### Modulo 6 — Casi d'uso reali (3h)

**Il modulo piu importante per il ROI del corso.** Qui i partecipanti collegano tutto cio che hanno imparato al PROPRIO lavoro.

**Workshop**: lascia che i partecipanti lavorino sui PROPRI task reali, non su esercizi fittizi. Il valore e nell'applicazione immediata.

**Condivisione finale**: gestisci il tempo con rigore (max 2 min a persona). L'obiettivo non e la presentazione perfetta ma lo scambio di idee.

**Raccolta prompt**: alla fine del workshop, raccogli i migliori prompt presentati e crea un documento condiviso. E il deliverable piu apprezzato dai partecipanti.

---

### Modulo 7 — AI Responsabile (2h)

**Punto critico**: il rischio e che diventi "la lezione noiosa". Previenilo con:
- Esercizio allucinazioni: genera una risposta con fatti falsi IN DIRETTA. L'effetto shock funziona.
- Esercizio bias: mostra la differenza nelle risposte con nomi diversi. Crea discussione.

**Policy aziendale**: se i partecipanti sono della stessa azienda, la policy creata nel lab puo diventare un deliverable reale. Suggeriscilo.

**EU AI Act**: limitati ai concetti pratici. Non serve entrare nei dettagli legali. Il messaggio e: "esiste una normativa, vi riguarda, formatevi".

---

### Modulo 8 — Progetto finale (2h)

**Gestione del tempo** (critico — 2h sono poche):
- 0:00-0:05 — Briefing e obiettivi
- 0:05-0:25 — Fase 1: progettazione
- 0:25-1:05 — Fase 2: realizzazione
- 1:05-1:20 — Fase 3: preparazione presentazione
- 1:20-1:50 — Presentazioni (con 8 partecipanti: ~3-4 min ciascuno)
- 1:50-2:00 — Quiz + chiusura

**Fase progettazione**: gira tra i partecipanti e valida il progetto PRIMA che inizino. Evita ambizioni eccessive: meglio un task semplice ben fatto.

**Presentazioni**: sii rigoroso sul tempo. Usa un timer visibile. Se il gruppo e grande (>10), riduci a 3 min a persona o seleziona i migliori.

**Quiz**: distribuisci la scheda stampata. 15 minuti. Raccogli, correggi durante una pausa o dopo il corso.

---

## Dopo il corso

### Follow-up consigliato
- **Giorno 1**: inviare email di ringraziamento con link ai materiali e libreria di prompt condivisa
- **Settimana 1**: inviare reminder "Hai usato l'AI questa settimana? Qual e stato il tuo prompt migliore?"
- **Mese 1**: breve survey di follow-up (3 domande: hai usato l'AI? quanto tempo risparmi? suggerimenti per il corso?)

### Aggiornamento materiali
Le interfacce e le funzionalita degli strumenti AI cambiano rapidamente. Pianifica:
- Verifica screenshot e istruzioni: prima di ogni erogazione
- Aggiornamento modelli e piani: ogni 3-6 mesi
- Aggiornamento normativa (AI Act): quando nuove disposizioni entrano in vigore
- Gli script Python (`genera_modulo_XX.py`) permettono di rigenerare le slide dopo le modifiche

---

## Personalizzazione del corso

### Per aziende specifiche
- Sostituisci gli scenari generici con scenari del settore dell'azienda
- Aggiungi il logo aziendale alle slide (modifica `pptx_helper.py`)
- Personalizza la policy AI (Modulo 7) con le specifiche dell'azienda
- Crea GPT/Projects pre-configurati per i workflow dell'azienda

### Per formati diversi

| Formato | Adattamento |
|---------|------------|
| 5 giornate x 4h | 2 moduli al giorno, pausa lunga tra i due |
| 10 sessioni x 2h | 1 modulo per sessione (Mod. 6 e 8 richiedono sessioni consecutive) |
| Intensivo 3 giorni | Comprimi Mod. 1+2 in 4h, Mod. 3+4 in 5h, Mod. 5+6+7+8 in 6h |
| Online sincrono | Aggiungi 15% tempo per gestione tecnica. Usa breakout rooms per i lab |
| Blended | Teoria asincrona (video), pratica sincrona (lab in aula o online) |

---

*Guida del Formatore — Corso AI Basics — Versione 1.0*
