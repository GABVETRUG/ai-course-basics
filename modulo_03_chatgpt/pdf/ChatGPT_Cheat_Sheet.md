# ChatGPT Cheat Sheet

**Corso AI Basics — Modulo 3**
*Guida rapida di riferimento*

---

## Accesso e piani

| Piano | Costo | Modelli | Feature principali |
|-------|-------|---------|-------------------|
| Free | Gratis | GPT-4o mini + GPT-4o (limitato) | Chat, upload file, web, DALL-E (limitato) |
| Plus | 20$/mese | GPT-4o + o3 + DALL-E | Tutto illimitato, GPTs custom, Canvas |
| Team | 25$/utente/mese | Come Plus | Workspace condiviso, privacy dati |
| Enterprise | Su richiesta | Tutto | SSO, admin console, privacy enterprise |

**URL**: chat.openai.com oppure chatgpt.com

---

## Funzionalita principali

### Chat
- Ogni conversazione e isolata (contesto separato)
- Usa "Nuova chat" quando cambi argomento
- Rinomina le chat importanti per ritrovarle
- Fissa le chat frequenti con "Pin"

### Upload file
Formati supportati: PDF, DOCX, XLSX, PPTX, CSV, TXT, immagini (JPG, PNG), codice
- Trascina il file nella chat o usa l'icona allegato
- Puoi caricare piu file nella stessa chat
- Max ~50 pagine per risultati ottimali

### Navigazione web
- Si attiva automaticamente per domande su eventi recenti
- Forzala con: "Cerca online..." o "Trova le ultime informazioni su..."
- Mostra le fonti cliccabili nella risposta

### DALL-E (generazione immagini)
- Prompt in linguaggio naturale
- Formula: SOGGETTO + STILE + DETTAGLI + FORMATO
- Non gestisce bene il testo nelle immagini
- Ogni modifica genera un'immagine NUOVA

### Code Interpreter
- Esegue codice Python in ambiente sicuro
- Carica CSV/Excel per analisi automatiche
- Genera grafici scaricabili (PNG, SVG)
- Non serve sapere Python: descrivi cosa vuoi a parole

### Canvas
- Editing collaborativo per testi e codice
- Seleziona porzioni di testo per modifiche mirate
- Attiva con: "Usa canvas per..." o automaticamente per testi lunghi

### Memory
- ChatGPT ricorda informazioni tra conversazioni
- "Ricorda che preferisco risposte in italiano e brevi"
- Gestisci: Impostazioni > Personalizzazione > Memoria

### Istruzioni personalizzate
- Impostazioni > Personalizzazione > Istruzioni personalizzate
- Due campi: "Cosa dovrebbe sapere di te" + "Come dovrebbe rispondere"
- Applicate a OGNI nuova chat automaticamente

---

## GPTs: assistenti personalizzati

### Usare GPTs esistenti
1. Vai su chatgpt.com/gpts
2. Cerca per categoria o parola chiave
3. Clicca per iniziare a usarlo
4. Puoi taggare un GPT con @nome in qualsiasi chat

### Creare un GPT custom
1. Vai su chatgpt.com/gpts/editor
2. Tab "Crea": descrivi cosa vuoi in linguaggio naturale
3. Tab "Configura": nome, istruzioni, file di conoscenza, strumenti
4. Tab "Anteprima": testa e itera
5. Pubblica: Solo per te / Con link / Nello Store

### Istruzioni per GPT: cosa includere
```
Sei [RUOLO] con esperienza in [DOMINIO].
Il tuo compito e [OBIETTIVO].
Rispondi sempre in [LINGUA] con tono [TONO].
Formato delle risposte: [FORMATO].
Vincoli: [VINCOLI].
Quando non sai qualcosa: [COMPORTAMENTO].
```

---

## Prompt efficaci per ChatGPT

### Analisi documento
```
Analizza il documento allegato e crea un riassunto esecutivo.
Struttura: Contesto (2 righe), Punti chiave (5 bullet),
Rischi (3 bullet), Raccomandazione.
Destinatario: [CHI]. Tono: professionale.
```

### Analisi dati (con Code Interpreter)
```
Analizza il dataset allegato:
1. Descrivi struttura e qualita dei dati
2. Identifica i 3 trend principali con grafici
3. Segnala anomalie o outlier
4. Crea un report di 10 righe con 2 raccomandazioni
```

### Generazione immagine (DALL-E)
```
Crea un'immagine di [SOGGETTO].
Stile: [illustrazione flat / fotografico / acquerello / minimal].
Colori: [PALETTE].
Atmosfera: [MOOD].
Formato: [orizzontale 16:9 / verticale / quadrato].
Senza testo nell'immagine.
```

### Creazione presentazione
```
Crea la struttura di una presentazione di [N] slide su [ARGOMENTO].
Pubblico: [CHI]. Durata: [MINUTI].
Per ogni slide: titolo + 3-4 bullet + suggerimento visuale.
Tono: [TONO].
```

### Canvas per editing testo
```
Usa canvas. Scrivi un [TIPO DI TESTO] su [ARGOMENTO].
[ISTRUZIONI SPECIFICHE].
Poi aspetta il mio feedback per le modifiche.
```

---

## Impostazioni importanti

### Privacy dei dati
- **Impostazioni > Controlli dati > Migliora il modello per tutti**: Disattiva
  (impedisce che le tue chat vengano usate per l'addestramento)
- Con piano Team/Enterprise: dati mai usati per l'addestramento

### Ottimizzare l'esperienza
- **Tema scuro**: Impostazioni > Generali > Tema
- **Lingua interfaccia**: Impostazioni > Generali > Lingua
- **Esporta dati**: Impostazioni > Controlli dati > Esporta dati

---

## Keyboard shortcuts

| Shortcut | Azione |
|----------|--------|
| Ctrl/Cmd + Shift + O | Apri/chiudi barra laterale |
| Ctrl/Cmd + Shift + ; | Copia ultima risposta |
| Ctrl/Cmd + / | Mostra tutti i shortcut |

---

## Limiti da ricordare

| Limite | Dettaglio | Workaround |
|--------|-----------|------------|
| Risposte verbose | ChatGPT tende a scrivere troppo | "Rispondi in max 5 bullet di 1 riga" |
| Contesto lungo | Perde il filo in chat molto lunghe | Apri nuova chat con riassunto |
| Testo in immagini | DALL-E scrive testo male | Aggiungi il testo dopo con altro tool |
| Allucinazioni | Puo inventare fatti | Verifica SEMPRE i fatti critici |
| Rifiuti eccessivi | A volte rifiuta richieste legittime | Specifica il contesto professionale |
| URL | Non accede a URL in modo affidabile | Copia-incolla il contenuto |

---

*Documento di riferimento — Corso AI Basics — Aggiornato 2026*
