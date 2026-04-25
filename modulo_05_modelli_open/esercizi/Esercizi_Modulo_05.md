# Scheda Esercizi — Modulo 5: Modelli Open Source

**Corso AI Basics**
*Durata parte pratica: 1.5 ore*

---

## Lab 1: Esplorare HuggingChat (25 min)

### Preparazione
- [ ] Vai su huggingface.co/chat
- [ ] (Opzionale) Crea un account per salvare le chat

### Esercizio 1.1: Primo contatto

1. Osserva: quale modello e selezionato di default? _______________

2. Invia questo messaggio:
```
Ciao! Presentati: dimmi quale modello sei, chi ti ha creato,
e quali sono i tuoi 3 punti di forza e 3 limiti principali.
```

**Il modello sa chi e?** Si / No / Parzialmente

**I limiti dichiarati ti sembrano onesti?** _______________

### Esercizio 1.2: Task pratico

Invia questo prompt:
```
Scrivi un'email di presentazione per un'azienda di consulenza IT
a un potenziale cliente nel settore sanitario.
Tono professionale, max 150 parole.
```

**Valutazione:**

| Criterio | Voto (1-5) |
|----------|-----------|
| Qualita del testo | |
| Italiano corretto | |
| Rispetta il limite di parole? | |
| Tono appropriato | |

### Esercizio 1.3: Cambio modello e confronto

1. Clicca sul nome del modello in alto
2. Seleziona un modello DIVERSO (suggerimento: se avevi Llama, prova Mistral)
3. Invia la STESSA email di presentazione

Modello 1 usato: _______________
Modello 2 usato: _______________

| Criterio | Modello 1 (1-5) | Modello 2 (1-5) |
|----------|----------------|----------------|
| Qualita testo | | |
| Italiano | | |
| Rispetto vincoli | | |
| Tono | | |
| **Preferenza** | | |

3. (Opzionale) Prova un terzo modello e ripeti

---

## Lab 2: Google AI Studio (25 min)

### Preparazione
- [ ] Vai su aistudio.google.com
- [ ] Accedi con il tuo account Google

### Esercizio 2.1: Setup e system instructions

1. Clicca "Create new prompt"
2. Nel campo "System instructions" (in alto), scrivi:
```
Sei un assistente professionale per un'azienda italiana.
Rispondi sempre in italiano, in modo conciso e strutturato.
Usa bullet point quando appropriato.
```

3. Seleziona il modello: "Gemini 2.5 Flash"
4. Invia una domanda di test:
```
Quali sono i 5 vantaggi principali dell'uso dell'AI in azienda?
```

**Ha rispettato le system instructions (italiano, conciso, bullet)?** Si / No

### Esercizio 2.2: Sperimentare con la temperatura

**Test 1 — Temperatura bassa (0.1):**
1. Nel pannello destro, imposta Temperature: 0.1
2. Invia: `Scrivi 3 slogan per una gelateria artigianale`
3. Annota i 3 slogan:
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

**Test 2 — Temperatura alta (1.0):**
1. Imposta Temperature: 1.0
2. Invia la STESSA domanda
3. Annota i 3 slogan:
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

**Differenze notate:**

_______________________________________________________

**Quale temperatura ha prodotto slogan migliori per un uso reale?**

_______________________________________________________

### Esercizio 2.3: Max output tokens

1. Imposta "Max output tokens" a **50**
2. Invia: `Spiega cos'e il machine learning`
3. Osserva: la risposta e stata troncata? _______________
4. Ora imposta a **500** e rifai la stessa domanda
5. Differenza nella qualita: _______________

**Lezione appresa sui token:** _______________

### Esercizio 2.4: Upload immagine (se disponibile)

1. Clicca l'icona allegato
2. Carica un'immagine (foto, screenshot, grafico)
3. Chiedi:
```
Descrivi cosa vedi in questa immagine.
Se contiene testo, trascrivilo. Se contiene dati, analizzali.
```

**La descrizione e accurata?** (1-5): ___

---

## Lab 3: Confronto Open vs Commerciale (25 min)

### Esercizio 3.1: Test su 4 strumenti

Invia lo STESSO prompt a tutti e 4 gli strumenti:

**Prompt:**
```
Sei un consulente HR. Un'azienda tech italiana (80 dipendenti)
ha un turnover del 25% annuo. Analizza le possibili cause
e proponi un piano di retention in 5 punti, con costi stimati
e tempi di implementazione. Formato: tabella + raccomandazione
finale. Max 400 parole.
```

Compila per ogni strumento:

### ChatGPT
- Formato rispettato (tabella + raccomandazione)? Si / No
- Limite parole rispettato? Si / No / Approssimativo
- Qualita contenuto (1-5): ___
- Note: _______________________________________________

### Claude
- Formato rispettato? Si / No
- Limite parole rispettato? Si / No / Approssimativo
- Qualita contenuto (1-5): ___
- Note: _______________________________________________

### HuggingChat (modello: _______________)
- Formato rispettato? Si / No
- Limite parole rispettato? Si / No / Approssimativo
- Qualita contenuto (1-5): ___
- Note: _______________________________________________

### Google AI Studio (modello: _______________)
- Formato rispettato? Si / No
- Limite parole rispettato? Si / No / Approssimativo
- Qualita contenuto (1-5): ___
- Note: _______________________________________________

### Classifica finale

| Posizione | Strumento | Punteggio totale |
|-----------|-----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

### Riflessione

**Il gap di qualita tra open e commerciale e grande o piccolo?**

_______________________________________________________

**Per questo task specifico, un modello open sarebbe sufficiente?**

_______________________________________________________

**In quali situazioni sceglieresti un modello open?**

_______________________________________________________

---

## Quiz di autovalutazione

### Domanda 1
Cosa significa "open weight" per un modello AI?
- a) Il modello e gratuito per qualsiasi uso
- b) I pesi (parametri) del modello sono pubblicamente disponibili
- c) Il codice di addestramento e pubblico
- d) Il modello funziona senza connessione internet

### Domanda 2
Quale di questi e un modello open source?
- a) GPT-4o (OpenAI)
- b) Claude Opus (Anthropic)
- c) Llama 3.1 (Meta)
- d) Gemini 2.5 Pro (Google)

### Domanda 3
Su quale piattaforma puoi usare modelli open SENZA installare nulla?
- a) Ollama
- b) LM Studio
- c) HuggingChat
- d) Visual Studio Code

### Domanda 4
Cosa controlla il parametro "temperatura" in un modello AI?
- a) La velocita di risposta
- b) Il livello di creativita vs prevedibilita delle risposte
- c) La lunghezza massima della risposta
- d) La lingua della risposta

### Domanda 5
Quando e meglio preferire un modello open a uno commerciale?
- a) Quando serve la massima qualita possibile
- b) Quando il budget e zero e il task non e troppo complesso
- c) Quando serve generare immagini
- d) Quando serve analizzare documenti di 100+ pagine

### Risposte
1: b | 2: c | 3: c | 4: b | 5: b

---

## La mia mappa degli strumenti

Dopo aver provato tutti gli strumenti, compila la tua mappa personale:

| Per questo tipo di task... | Usero... | Perche... |
|---------------------------|----------|-----------|
| Email e comunicazione | | |
| Analisi dati | | |
| Documenti lunghi | | |
| Brainstorming | | |
| Immagini | | |
| Task semplici e veloci | | |
| Quando la privacy e critica | | |

---

*Corso AI Basics — Modulo 5 — Scheda esercizi*
