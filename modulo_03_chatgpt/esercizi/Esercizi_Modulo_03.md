# Scheda Esercizi — Modulo 3: ChatGPT

**Corso AI Basics**
*Durata parte pratica: 2.5 ore*

---

## Lab 1: Riassunto esecutivo da documento (25 min)

### Preparazione
- [ ] Accedi a chat.openai.com
- [ ] Procurati un documento di almeno 5 pagine (report, articolo, regolamento pubblico)

### Esercizio 1.1: Upload e analisi

1. Carica il documento in ChatGPT (icona allegato)
2. Invia questo prompt:
```
Analizza il documento allegato e crea un riassunto esecutivo.
Struttura: Contesto (2 righe), Punti chiave (5 bullet),
Rischi/Criticita (3 bullet), Raccomandazione finale.
Destinatario: CEO non tecnico. Tono: professionale e diretto.
```

**Valutazione della risposta:**

| Criterio | Voto (1-5) | Note |
|----------|-----------|------|
| Ha compreso correttamente il documento? | | |
| La struttura richiesta e stata rispettata? | | |
| Il tono e adatto a un CEO? | | |
| I punti chiave sono quelli giusti? | | |

### Esercizio 1.2: Iterazione

Prova almeno 2 prompt di follow-up:
```
Rendi il tono piu incisivo, meno descrittivo
```
```
Riscrivi in formato email pronta da inviare al CEO
```

La seconda versione e migliore? In cosa?

_______________________________________________________

---

## Lab 2: Analisi dati con Code Interpreter (30 min)

### Esercizio 2.1: Creare un dataset di esempio

Se non hai un tuo file CSV, chiedi a ChatGPT di crearne uno:
```
Genera un file CSV con dati di vendita:
12 mesi (gen-dic 2025), 4 prodotti (A, B, C, D),
colonne: Mese, Prodotto, Quantita, Fatturato, Regione (Nord/Centro/Sud).
150 righe circa. Includi qualche anomalia per rendere l'analisi interessante.
Scaricabile come file.
```

- [ ] Ho scaricato il file CSV

### Esercizio 2.2: Analisi guidata

Carica il CSV in una NUOVA chat e segui questi step:

**Step 1 — Esplorazione:**
```
Esplora questo dataset. Dimmi: numero righe/colonne,
tipi di dati, valori mancanti, statistiche descrittive base.
```

**Step 2 — Visualizzazione:**
```
Crea 3 grafici:
1. Trend fatturato mensile totale (linea)
2. Fatturato per prodotto (barre)
3. Distribuzione per regione (torta)
Stile professionale, colori coerenti.
```

**Step 3 — Insight:**
```
Qual e il prodotto con la crescita maggiore mese su mese?
C'e un mese con un calo anomalo? Quali possibili cause?
```

**Step 4 — Report:**
```
Crea un report di analisi di 10 righe con:
- 3 insight principali
- 2 raccomandazioni operative
Tono: analista dati, con numeri a supporto.
```

### Valutazione

| Aspetto | Voto (1-5) |
|---------|-----------|
| I grafici sono chiari e leggibili? | |
| Gli insight sono pertinenti? | |
| Le anomalie sono state individuate? | |
| Il report e utilizzabile? | |

- [ ] Ho scaricato almeno un grafico

---

## Lab 3: Generazione immagini con DALL-E (25 min)

### Esercizio 3.1: Prima immagine

Scegli un tema e crea un'immagine con questo prompt (adattalo):
```
Un ufficio moderno open space con persone che collaborano.
Stile: illustrazione flat design, colori pastello blu e verde.
Luce naturale. Vista leggermente dall'alto.
Formato orizzontale 16:9. Nessun testo nell'immagine.
```

**L'immagine ti piace?** _______________

**Cosa cambieresti?** _______________

### Esercizio 3.2: Iterazione

Partendo dall'immagine precedente, prova queste modifiche:
```
Stessa scena ma con colori piu caldi (arancione e giallo)
```
```
Cambia lo stile in fotografico realistico
```
```
Rimuovi le persone, tieni solo l'ambiente
```

**Quale versione preferisci?** _______________

### Esercizio 3.3: Immagine per il tuo lavoro

Crea un'immagine che potresti usare realmente in una presentazione:

Il tuo prompt:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**La useresti davvero in una presentazione?** Si / No

**Perche?** _______________________________________________________

---

## Lab 4: Creare un GPT custom (30 min)

### Esercizio 4.1: Scegli il tuo GPT

Quale GPT vuoi creare? (segna con X)

- [ ] A. Assistente Email — scrive email nel tuo stile
- [ ] B. Analista Report — riassume documenti con il tuo formato
- [ ] C. Coach Presentazioni — aiuta a strutturare slide
- [ ] D. FAQ Team — risponde a domande frequenti
- [ ] E. Altro: _______________

### Esercizio 4.2: Configurazione

1. Vai su chatgpt.com/gpts/editor
2. Tab "Crea": descrivi in linguaggio naturale

Il tuo messaggio di descrizione:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

3. Rispondi alle domande di ChatGPT (nome, tono, comportamento)
4. Passa alla tab "Configura" e verifica le istruzioni generate

### Esercizio 4.3: Test

Testa il GPT con 3 domande:

| Domanda di test | Risposta soddisfacente? (1-5) | Note |
|----------------|-------------------------------|------|
| 1. ____________ | | |
| 2. ____________ | | |
| 3. ____________ | | |

Prova un caso limite (domanda fuori tema):

Domanda: _______________

Risposta: Si e comportato bene? _______________

### Esercizio 4.4: Pubblicazione

- [ ] Ho pubblicato il GPT come "Solo per me"
- [ ] Ho testato con almeno 3 domande
- [ ] Lo userei nel mio lavoro quotidiano? Si / No

---

## Quiz di autovalutazione

### Domanda 1
Quale funzionalita di ChatGPT permette di eseguire codice Python e analizzare dati?
- a) DALL-E
- b) Code Interpreter
- c) Canvas
- d) GPT Store

### Domanda 2
Cosa NON puoi fare con il piano Free di ChatGPT?
- a) Caricare un file PDF
- b) Creare GPT personalizzati
- c) Usare la navigazione web
- d) Fare domande generiche

### Domanda 3
Qual e il limite principale di DALL-E nella generazione immagini?
- a) Non genera immagini a colori
- b) Non gestisce bene il testo nelle immagini
- c) Genera solo immagini in bianco e nero
- d) Non puo creare immagini di persone

### Domanda 4
A cosa servono le "Istruzioni personalizzate" di ChatGPT?
- a) A cambiare il colore dell'interfaccia
- b) A impostare istruzioni permanenti applicate a ogni nuova chat
- c) A creare un GPT custom
- d) A cambiare il modello di default

### Domanda 5
Dove si disattiva l'uso dei propri dati per l'addestramento?
- a) Impostazioni > Controlli dati > Migliora il modello
- b) Impostazioni > Generali > Privacy
- c) Non e possibile disattivarlo
- d) Si disattiva automaticamente con il piano Plus

### Risposte
1: b | 2: b | 3: b | 4: b | 5: a

---

*Corso AI Basics — Modulo 3 — Scheda esercizi*
