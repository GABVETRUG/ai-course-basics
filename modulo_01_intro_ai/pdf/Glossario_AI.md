# Glossario AI — Termini Chiave per Iniziare

**Corso AI Basics — Modulo 1**
*Documento di approfondimento*

---

## Termini fondamentali

### Intelligenza Artificiale (AI / IA)
Campo dell'informatica che si occupa di creare sistemi in grado di svolgere compiti che normalmente richiedono intelligenza umana: comprendere il linguaggio, riconoscere immagini, prendere decisioni, generare contenuti.

### Machine Learning (ML)
Sottocampo dell'AI in cui i sistemi **imparano dai dati** invece di essere programmati esplicitamente con regole. L'algoritmo trova pattern nei dati e li usa per fare previsioni o classificazioni.

### Deep Learning (DL)
Sottocampo del Machine Learning basato su **reti neurali profonde** (con molti strati). Eccelle nel riconoscimento di pattern complessi in immagini, audio e testo.

### LLM (Large Language Model)
Modello linguistico di grandi dimensioni, addestrato su enormi quantita di testo per comprendere e generare linguaggio naturale. Esempi: GPT-4 (OpenAI), Claude (Anthropic), Llama (Meta).

### AI Generativa
Categoria di AI capace di **creare nuovi contenuti**: testo, immagini, audio, video, codice. ChatGPT e Claude sono esempi di AI generativa testuale; DALL-E e Midjourney sono AI generative per immagini.

---

## Come funzionano i modelli

### Token
Unita minima di testo elaborata da un LLM. Un token e circa 3/4 di una parola in inglese (leggermente meno in italiano). "Intelligenza Artificiale" corrisponde a circa 4-5 token.

### Contesto (Context Window)
Quantita massima di testo che un modello puo "vedere" in una singola interazione. Include la tua domanda, le risposte precedenti e le istruzioni di sistema. Quando il contesto si riempie, il modello perde i messaggi piu vecchi.

| Modello | Finestra di contesto |
|---------|---------------------|
| GPT-4o | ~128.000 token |
| Claude Opus/Sonnet | ~200.000 token |
| Llama 3.1 | ~128.000 token |
| Gemini 2.5 Pro | ~1.000.000 token |

### Temperatura
Parametro che controlla la "creativita" del modello. Temperatura bassa (0.0-0.3) produce risposte precise e ripetibili; temperatura alta (0.7-1.0) produce risposte piu varie e creative.

### Parametri
I "pesi" interni del modello, appresi durante l'addestramento. Piu parametri generalmente significa un modello piu capace (ma anche piu lento e costoso). GPT-4 ha circa 1.700 miliardi di parametri.

### Addestramento (Training)
Processo in cui il modello legge enormi quantita di testo per apprendere i pattern del linguaggio. Puo richiedere settimane su migliaia di GPU e costare milioni di dollari.

### Fine-tuning
Processo di addestramento aggiuntivo su un dataset specifico per specializzare un modello pre-addestrato. Esempio: un modello generale addestrato ulteriormente su documenti medici per uso sanitario.

### Inferenza
Il momento in cui il modello **genera una risposta**. Quando chatti con ChatGPT, il modello sta facendo inferenza. Ha un costo computazionale (e economico) per ogni token generato.

---

## Interazione con i modelli

### Prompt
L'istruzione o domanda che invii al modello AI. La qualita del prompt determina la qualita della risposta. Vedi Modulo 2 per le tecniche di Prompt Engineering.

### Allucinazione
Risposta dell'AI che suona plausibile ma e **parzialmente o completamente falsa**. Il modello genera testo statisticamente probabile, non verifica i fatti. Vedi Modulo 7 per approfondimento.

### System Prompt
Istruzione di sistema, invisibile all'utente, che definisce il comportamento del modello. Esempio: "Sei un assistente utile che risponde sempre in italiano formale."

### Chat / Conversazione
Modalita di interazione in cui il modello mantiene il **contesto dei messaggi precedenti** nella stessa sessione. Permette di raffinare le risposte e approfondire un argomento.

### Streaming
Modalita di visualizzazione in cui la risposta appare **parola per parola** in tempo reale, anziche attendere la generazione completa. E cio che vedi normalmente su ChatGPT e Claude.

---

## Strumenti e piattaforme

### ChatGPT
Chatbot di OpenAI basato sui modelli GPT. Il piu diffuso al mondo. Disponibile in versione gratuita (GPT-4o mini + GPT-4o limitato) e a pagamento (Plus, 20$/mese).

### Claude
Chatbot di Anthropic, focalizzato su sicurezza e affidabilita. Modelli: Opus (potente), Sonnet (bilanciato), Haiku (veloce). Disponibile gratis (limitato) e Pro (20$/mese).

### Gemini
Chatbot di Google, integrato nell'ecosistema Google (Gmail, Drive, Docs). Gratuito con account Google. Modelli Gemini 2.5 Pro e Flash.

### Copilot
Assistente AI di Microsoft integrato in Windows, Edge e Office 365. Basato su tecnologia OpenAI (GPT-4). Gratis nella versione base.

### HuggingChat
Interfaccia web gratuita di Hugging Face che permette di usare modelli open source (Llama, Mistral, etc.) senza installazione.

### Google AI Studio
Piattaforma di Google per sperimentare con i modelli Gemini e Gemma. Gratuita con account Google.

---

## Modelli Open Source

### Open Source / Open Weight
Modello il cui codice sorgente e/o i pesi sono pubblicamente disponibili. Chiunque puo scaricarli, usarli e modificarli. Non sempre gratuito per uso commerciale (dipende dalla licenza).

### Llama (Meta)
Famiglia di modelli open di Meta (Facebook). Llama 3.1 e tra i piu potenti modelli open disponibili. Versioni da 8B a 405B parametri.

### Mistral / Mixtral
Modelli dell'azienda francese Mistral AI. Noti per l'ottimo rapporto qualita/dimensione. Mixtral usa un'architettura "Mixture of Experts".

### Gemma (Google)
Versione open dei modelli Google, piu piccola e adatta a sperimentazione e uso locale. Gemma 2 disponibile da 2B a 27B parametri.

### Ollama
Software che permette di **eseguire modelli AI sul proprio computer**, senza inviare dati a server esterni. Richiede competenze tecniche per l'installazione.

---

## Concetti avanzati (cenni)

### API (Application Programming Interface)
Interfaccia che permette a programmi e applicazioni di **comunicare con i modelli AI via codice**, senza usare l'interfaccia web. Essenziale per integrare l'AI in software aziendali.

### RAG (Retrieval-Augmented Generation)
Tecnica che permette al modello di **cercare informazioni in documenti specifici** prima di rispondere. Riduce le allucinazioni e permette di usare dati aziendali aggiornati.

### Embedding
Rappresentazione numerica di un testo (vettore) che cattura il suo significato. Usato per ricerca semantica, confronto di documenti e sistemi RAG.

### Multimodale
Modello capace di elaborare **piu tipi di input**: testo, immagini, audio, video. GPT-4o e Claude sono multimodali (testo + immagini). Gemini gestisce anche audio e video.

### Agenti AI
Sistemi che possono **eseguire azioni autonomamente**: navigare il web, scrivere codice, usare strumenti, prendere decisioni. Rappresentano l'evoluzione dei semplici chatbot.

### Transformer
Architettura di rete neurale alla base di tutti i modelli linguistici moderni. Introdotta da Google nel 2017 ("Attention Is All You Need"). La "T" di GPT sta per Transformer.

---

*Questo glossario e un documento vivo: i termini e le definizioni evolvono con la tecnologia. Ultimo aggiornamento: 2026.*
