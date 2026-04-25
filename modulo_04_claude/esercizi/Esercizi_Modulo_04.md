# Scheda Esercizi — Modulo 4: Claude

**Corso AI Basics**
*Durata parte pratica: 2.5 ore*

---

## Lab 1: Analisi documento lungo (30 min)

### Preparazione
- [ ] Accedi a claude.ai
- [ ] Procurati un documento lungo (10+ pagine): regolamento, manuale, report pubblico

### Esercizio 1.1: Analisi strutturale

Carica il documento e invia:
```
Ho caricato un documento su [ARGOMENTO].
Prima di tutto, dimmi di cosa tratta e qual e la sua struttura
(sezioni principali con breve descrizione di ciascuna).
```

**Claude ha individuato correttamente la struttura?** Si / No

**Ha mancato qualche sezione importante?**

_______________________________________________________

### Esercizio 1.2: Domande progressive

Invia queste domande una alla volta, in ordine:

**Livello 1 — Comprensione:**
```
Quali sono i 5 punti piu importanti di questo documento?
```

**Livello 2 — Ricerca specifica:**
```
Cosa dice il documento riguardo [ARGOMENTO SPECIFICO]?
Cita i passaggi rilevanti.
```

**Livello 3 — Analisi critica:**
```
Ci sono ambiguita, contraddizioni o lacune nel documento?
Se si, elencale con il riferimento alla sezione.
```

**Livello 4 — Applicazione:**
```
Basandoti su questo documento, crea una checklist operativa
di 10 punti per [RUOLO/ATTIVITA].
```

### Valutazione

| Livello | Claude ha risposto bene? (1-5) | Ha citato il documento? |
|---------|-------------------------------|------------------------|
| 1. Comprensione | | Si / No |
| 2. Ricerca specifica | | Si / No |
| 3. Analisi critica | | Si / No |
| 4. Applicazione | | Si / No |

---

## Lab 2: Artifacts interattivi (30 min)

### Esercizio 2.1: Documento formattato

Invia a Claude:
```
Crea un artifact con un documento formattato:
Titolo: Guida rapida all'uso dell'AI nel nostro team
Sezioni:
1. Strumenti approvati (ChatGPT, Claude, HuggingChat)
2. Regole d'uso (5 punti)
3. 5 prompt utili per il lavoro quotidiano
4. FAQ (5 domande e risposte)
Formato professionale con indice.
```

- [ ] L'artifact si e aperto nel pannello laterale
- [ ] Il contenuto e ben formattato

**Itera:** "Aggiungi una sezione 'Errori comuni da evitare' con 5 punti"

- [ ] Claude ha aggiornato l'artifact correttamente

### Esercizio 2.2: Calcolatore interattivo

Scegli uno e invialo a Claude:

**Opzione A — Calcolatore ROI:**
```
Crea un artifact HTML con un calcolatore ROI interattivo.
Campi: investimento iniziale, ricavo atteso annuo, costi operativi annui, anni.
Calcola: ROI %, payback period, profitto netto totale.
Design: moderno, pulito, colori blu e bianco.
Mostra i risultati in modo chiaro con formattazione.
```

**Opzione B — Preventivo servizi:**
```
Crea un artifact HTML con un calcolatore di preventivo.
Servizi selezionabili con checkbox e prezzo unitario:
- Consulenza base (500 euro)
- Analisi dati (800 euro)
- Report personalizzato (300 euro)
- Formazione team (1200 euro)
- Supporto mensile (400 euro/mese, seleziona mesi: 1-12)
Calcola: subtotale, sconto volume (>3 servizi: 10%), IVA 22%, totale.
```

**Funziona correttamente?** Si / No

**Se no, cosa va corretto?**

_______________________________________________________

### Esercizio 2.3: Dashboard dati

Invia a Claude:
```
Crea un artifact HTML con una dashboard che visualizzi questi dati:
Vendite trimestrali 2025: Q1 150K, Q2 180K, Q3 165K, Q4 210K
Prodotti: A 40%, B 35%, C 25%
Regioni: Nord 45%, Centro 30%, Sud 25%

Includi:
- Grafico a barre per trimestri
- Grafico a torta per prodotti
- Indicatore crescita YoY
- Tabella riepilogativa
Design moderno, colori coerenti.
```

**La dashboard e visivamente professionale?** (1-5): ___

**I grafici sono corretti?** Si / No

**Iterazione:** "Aggiungi un toggle per mostrare/nascondere ogni sezione"

---

## Lab 3: Confronto diretto Claude vs ChatGPT (25 min)

### Esercizio 3.1: Test comparativo

Scegli UN task e invia lo STESSO prompt a Claude e ChatGPT:

**Task A:**
```
Analizza i pro e contro del lavoro da remoto per un'azienda
di 50 persone nel settore IT. Crea un report di 1 pagina con:
struttura in sezioni, dati a supporto, raccomandazione finale.
Tono: consulente strategico. Max 500 parole.
```

**Task B:**
```
Scrivi una proposta commerciale per un servizio di consulenza
AI rivolto a PMI italiane (10-50 dipendenti).
Struttura: problema, soluzione, benefici, pricing, prossimi passi.
Max 2 pagine, tono professionale ma non burocratico.
```

**Task C:**
```
Crea un piano di onboarding di 30 giorni per un nuovo dipendente
nel reparto marketing. Tabella settimana per settimana con:
attivita, responsabile, obiettivo, output atteso.
Includi una sezione "primi 3 giorni" piu dettagliata.
```

### Scheda confronto

Task scelto: ___

| Criterio | Claude (1-5) | ChatGPT (1-5) | Migliore |
|----------|-------------|---------------|----------|
| Aderenza al prompt (formato, struttura) | | | |
| Qualita del contenuto | | | |
| Concisione (rispetta i limiti?) | | | |
| Originalita delle idee | | | |
| Accuratezza dei fatti/dati | | | |
| Tono e stile richiesto | | | |
| Formattazione visuale | | | |
| **TOTALE** | | | |

**Vincitore per questo task:** _______________

**Perche?** _______________________________________________________

---

## Lab 4: Organizzare il lavoro con Projects (25 min)

### Esercizio 4.1: Creare un progetto

1. Barra laterale > + Nuovo progetto
2. Nome del progetto: ___________________________
3. Scrivi le istruzioni personalizzate:

```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

### Esercizio 4.2: Aggiungere contesto

Carica almeno un file di contesto (template, documento di riferimento, dati):

File caricato: ___________________________

### Esercizio 4.3: Test del progetto

Apri una nuova chat DENTRO il progetto e fai 3 domande:

| Domanda | La risposta ha usato il contesto? | Qualita (1-5) |
|---------|----------------------------------|---------------|
| 1. _______ | Si / No | |
| 2. _______ | Si / No | |
| 3. _______ | Si / No | |

**Il progetto ti farebbe risparmiare tempo nel lavoro quotidiano?** Si / No

**Come?** _______________________________________________________

---

## Quiz di autovalutazione

### Domanda 1
Qual e la finestra di contesto di Claude?
- a) 32.000 token
- b) 128.000 token
- c) 200.000 token
- d) 1.000.000 token

### Domanda 2
Cosa sono gli Artifacts di Claude?
- a) Errori di generazione del modello
- b) Output interattivi che si aprono in un pannello laterale
- c) File scaricabili dal server di Anthropic
- d) Plugin installabili

### Domanda 3
Quale modello Claude e il piu indicato per uso quotidiano?
- a) Opus (il piu potente)
- b) Sonnet (il bilanciato)
- c) Haiku (il piu veloce)
- d) Sono tutti uguali

### Domanda 4
Cosa NON puo fare Claude rispetto a ChatGPT?
- a) Analizzare documenti lunghi
- b) Generare immagini
- c) Creare Artifacts
- d) Rispondere in italiano

### Domanda 5
A cosa servono i Projects di Claude?
- a) A creare presentazioni PowerPoint
- b) A organizzare il lavoro con contesto e istruzioni persistenti
- c) A generare codice Python
- d) A navigare il web

### Risposte
1: c | 2: b | 3: b | 4: b | 5: b

---

*Corso AI Basics — Modulo 4 — Scheda esercizi*
