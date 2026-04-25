# Guida ai Modelli Open Source

**Corso AI Basics — Modulo 5**
*Documento di approfondimento*

---

## Panoramica dei modelli open

### Cos'e un modello "open"

Un modello AI "open" (o "open weight") e un modello i cui parametri (pesi) sono pubblicamente disponibili. Chiunque puo scaricarli, usarli e, in molti casi, modificarli per i propri scopi.

**Cosa e pubblico** (nella maggior parte dei casi):
- I pesi del modello (il file che contiene i parametri addestrati)
- La documentazione e le istruzioni per l'uso
- Benchmark e risultati di valutazione

**Cosa spesso NON e pubblico**:
- Il dataset di addestramento completo
- Il codice di addestramento dettagliato
- I costi e le risorse impiegate

---

## I modelli principali

### Llama 3.1 (Meta)

| Caratteristica | Dettaglio |
|---------------|-----------|
| Sviluppatore | Meta (Facebook/Instagram) |
| Dimensioni | 8B, 70B, 405B parametri |
| Contesto | 128K token |
| Lingue | Multilingue (ottimo italiano) |
| Licenza | Llama Community License (gratis se < 700M utenti) |
| Punti di forza | Ragionamento, scrittura, coding, istruzioni complesse |
| Dove usarlo | HuggingChat, Groq, Together AI, Ollama (locale) |

**Quando sceglierlo**: task complessi che richiedono ragionamento avanzato; quando serve qualita paragonabile ai modelli commerciali.

### Mistral / Mixtral (Mistral AI)

| Caratteristica | Dettaglio |
|---------------|-----------|
| Sviluppatore | Mistral AI (Parigi, Francia) |
| Dimensioni | 7B (Mistral), 47B (Mixtral 8x7B), 123B (Large) |
| Contesto | 32K - 128K token |
| Lingue | Ottimo in francese, buono in italiano |
| Licenza | Apache 2.0 (molto permissiva) |
| Punti di forza | Efficienza, velocita, rapporto qualita/dimensione |
| Dove usarlo | HuggingChat, Groq, Mistral Platform, Ollama |

**Architettura Mixture of Experts (MoE)**: Mixtral ha 47B parametri totali ma ne usa solo ~13B per ogni risposta. Risultato: qualita di un modello grande, velocita di un modello piccolo.

**Quando sceglierlo**: task quotidiani dove serve velocita; budget limitato; preferenza per aziende europee.

### Gemma 2 (Google)

| Caratteristica | Dettaglio |
|---------------|-----------|
| Sviluppatore | Google DeepMind |
| Dimensioni | 2B, 9B, 27B parametri |
| Contesto | 8K token |
| Lingue | Multilingue (inglese migliore) |
| Licenza | Gemma Terms of Use (permissiva, uso commerciale OK) |
| Punti di forza | Ultra-efficiente, facile da usare su AI Studio |
| Dove usarlo | Google AI Studio, HuggingChat, Ollama |

**Quando sceglierlo**: sperimentazione con risorse limitate; chi usa gia l'ecosistema Google; task semplici e veloci.

### Qwen 2.5 (Alibaba)

| Caratteristica | Dettaglio |
|---------------|-----------|
| Sviluppatore | Alibaba Cloud (Cina) |
| Dimensioni | 0.5B, 3B, 7B, 14B, 32B, 72B parametri |
| Contesto | 32K - 128K token |
| Lingue | Eccellente cinese e inglese, buono in altre lingue |
| Licenza | Apache 2.0 |
| Punti di forza | Matematica, ragionamento, ampia gamma di dimensioni |
| Dove usarlo | HuggingChat, Ollama |

**Quando sceglierlo**: task matematici o di ragionamento; quando serve un modello disponibile in molte dimensioni.

### DeepSeek V3

| Caratteristica | Dettaglio |
|---------------|-----------|
| Sviluppatore | DeepSeek (Cina) |
| Dimensioni | 685B totali (37B attivi, architettura MoE) |
| Contesto | 128K token |
| Licenza | MIT (molto permissiva) |
| Punti di forza | Qualita eccezionale, costi di addestramento bassi |
| Dove usarlo | DeepSeek Chat, HuggingChat |

**Nota**: DeepSeek ha suscitato dibattito per le implicazioni geopolitiche e di privacy. I server sono in Cina.

---

## Dove usare i modelli open (senza installare nulla)

### HuggingChat (huggingface.co/chat)

**La scelta consigliata per iniziare.**

| Aspetto | Dettaglio |
|---------|-----------|
| Costo | Gratuito |
| Account | Opzionale (consigliato per salvare chat) |
| Modelli | Llama, Mistral, Gemma, Qwen e altri |
| Upload file | No (versione base) |
| Ricerca web | Si (attivabile) |
| Vantaggi | Semplicissimo, molti modelli, gratuito |
| Limiti | No upload file, velocita variabile |

**Come cambiare modello**: clicca sul nome del modello in alto nella chat.

### Google AI Studio (aistudio.google.com)

**La scelta per chi vuole sperimentare con i parametri.**

| Aspetto | Dettaglio |
|---------|-----------|
| Costo | Gratuito |
| Account | Google Account obbligatorio |
| Modelli | Gemini 2.5 Pro, Gemini Flash, Gemma 2 |
| Upload file | Si (documenti e immagini) |
| Parametri | Temperatura, top-p, max token (configurabili) |
| Vantaggi | Upload file, controllo parametri, system instructions |
| Limiti | Interfaccia piu tecnica, meno modelli open |

**System Instructions**: campo dove puoi scrivere istruzioni permanenti per la sessione. Esempio: "Rispondi sempre in italiano, in modo conciso."

### Groq (groq.com)

**La scelta per chi vuole velocita estrema.**

| Aspetto | Dettaglio |
|---------|-----------|
| Costo | Gratuito con limiti di utilizzo |
| Modelli | Llama, Mistral, Gemma (i piu veloci del mercato) |
| Vantaggi | Velocita 10-50x superiore grazie a chip specializzati (LPU) |
| Limiti | Limiti di utilizzo sul piano gratuito |

### Altre piattaforme

| Piattaforma | URL | Note |
|------------|-----|------|
| Poe | poe.com | Multi-modello (open + closed). Di Quora |
| Perplexity | perplexity.ai | Ricerca AI + modelli open |
| OpenRouter | openrouter.ai | Gateway API multi-modello |

---

## Parametri dei modelli: guida pratica

### Temperatura
Controlla la "creativita" vs "prevedibilita" delle risposte.

| Valore | Comportamento | Uso ideale |
|--------|-------------|-----------|
| 0.0 - 0.3 | Risposte precise, ripetibili, conservative | Fatti, dati, istruzioni |
| 0.4 - 0.6 | Bilanciato tra precisione e varieta | Uso generico |
| 0.7 - 1.0 | Risposte varie, creative, sorprendenti | Brainstorming, scrittura creativa |
| > 1.0 | Risposte imprevedibili, possibili nonsense | Sconsigliato per uso professionale |

### Top-P (Nucleus Sampling)
Controlla la diversita delle parole considerate dal modello.

| Valore | Effetto |
|--------|---------|
| 0.1 | Solo le parole piu probabili (molto conservativo) |
| 0.5 | Buon bilanciamento |
| 0.9 - 1.0 | Tutte le parole considerate (massima diversita) |

**Consiglio**: di solito basta regolare la Temperatura. Lascia Top-P al default (0.9-1.0) a meno che tu non abbia esigenze specifiche.

### Max Output Tokens
Il numero massimo di token che il modello puo generare nella risposta.
- 100 token ~ 75 parole
- 500 token ~ 375 parole
- 2000 token ~ 1500 parole (circa 2 pagine)

---

## Confronto rapido: open vs commerciale

| Criterio | Modelli Open (HuggingChat) | Modelli Commerciali (ChatGPT/Claude) |
|----------|--------------------------|--------------------------------------|
| Costo | Gratuito | Gratis limitato, 20$/mese full |
| Qualita top task | Buona-Ottima | Eccellente |
| Upload file | Limitato | Si |
| Gen. immagini | Limitato | Si (ChatGPT) |
| Privacy | Variabile (meglio se locale) | Dipende dal piano |
| Personalizzazione | Alta (se tecnico) | Limitata all'interfaccia |
| Velocita | Variabile | Costante |
| Supporto italiano | Buono (Llama, Mistral) | Eccellente |
| Affidabilita servizio | Media | Alta |

---

## Per chi vuole andare oltre: installazione locale

Per utenti tecnici che vogliono massima privacy e controllo:

### Ollama (ollama.com)
- Software per eseguire modelli AI sul proprio computer
- Installazione semplice (Mac, Linux, Windows)
- Comando: `ollama run llama3.1` per avviare una chat locale
- I dati NON escono mai dal tuo computer
- Richiede: 8-16 GB RAM per modelli piccoli, 32-64 GB per modelli grandi

### LM Studio (lmstudio.ai)
- Interfaccia grafica per eseguire modelli locali
- Piu user-friendly di Ollama
- Scarica modelli con un click dal catalogo integrato
- Disponibile per Mac, Windows, Linux

**Nota**: l'installazione locale esula dagli obiettivi di questo corso base. E menzionata come riferimento per chi vuole approfondire.

---

*Documento di riferimento — Corso AI Basics — Aggiornato 2026*
