# Claude Cheat Sheet

**Corso AI Basics — Modulo 4**
*Guida rapida di riferimento*

---

## Accesso e piani

| Piano | Costo | Modelli | Feature principali |
|-------|-------|---------|-------------------|
| Free | Gratis | Sonnet | Chat, Artifacts, upload file (limitato) |
| Pro | 20$/mese | Opus + Sonnet + Haiku | 5x messaggi, Projects, tutti i modelli |
| Team | 25$/utente/mese | Come Pro | Workspace condiviso, admin tools |
| Enterprise | Su richiesta | Tutto | SSO, SAML, SLA, privacy enterprise |

**URL**: claude.ai

---

## I tre modelli

| Modello | Uso ideale | Velocita | Qualita |
|---------|-----------|----------|---------|
| **Haiku** | Domande rapide, task semplici | Molto veloce | Buona |
| **Sonnet** | Uso quotidiano, bilanciato (default) | Veloce | Molto buona |
| **Opus** | Analisi complesse, ragionamento, coding | Piu lento | Eccellente |

**Come cambiare**: menu a tendina in alto nell'area chat.

**Regola pratica**: parti con Sonnet. Se la risposta non e soddisfacente, rifai con Opus. Usa Haiku per domande rapide da "si/no".

---

## Feature distintive

### Contesto lungo (200K token)
- Circa 500 pagine di testo in una singola conversazione
- Ideale per: contratti, manuali, report lunghi, codice sorgente
- ChatGPT Free gestisce circa 100 pagine (128K), Claude ne gestisce 500 (200K)
- Carica il documento e Claude lo analizza per intero

### Artifacts
Output interattivi che si aprono in un pannello laterale:

| Tipo | Esempio | Come chiedere |
|------|---------|---------------|
| Documento | Report formattato con indice | "Crea un documento formattato su..." |
| Codice | Script con syntax highlighting | "Scrivi un programma che..." |
| HTML interattivo | Calcolatore, quiz, dashboard | "Crea un calcolatore interattivo per..." |
| SVG | Diagrammi, grafici, icone | "Crea un diagramma di flusso di..." |
| Tabella | Dati strutturati | "Crea una tabella comparativa di..." |

**Azioni sugli Artifacts**:
- Copia il contenuto
- Scarica come file
- Condividi via link (se attivo)
- Chiedi modifiche: "Modifica l'artifact: cambia..."

### Projects
Spazi di lavoro con contesto persistente:

1. Crea un progetto (barra laterale > + Nuovo progetto)
2. Aggiungi **istruzioni personalizzate** (system prompt)
3. Carica **file di contesto** (template, dati, documenti di riferimento)
4. Ogni nuova chat nel progetto eredita automaticamente istruzioni e file

**Esempi di progetti utili**:
- Report ricorrente (template + KPI + dati storici)
- Assistente progetto (brief + timeline + stakeholder)
- Base di conoscenza (manuali + procedure + FAQ)
- Scrittura brand (tone of voice + brand guidelines + esempi)

---

## Prompt efficaci per Claude

### Analisi documento lungo
```
Ho caricato un documento di [N] pagine su [ARGOMENTO].
1. Descrivi la struttura (sezioni principali)
2. Elenca i 5 punti chiave
3. Identifica eventuali ambiguita o contraddizioni
4. Crea una checklist operativa basata sul contenuto
Cita i passaggi rilevanti dal documento.
```

### Creare un Artifact documento
```
Crea un artifact con un documento formattato:
Titolo: [TITOLO]
Sezioni: [LISTA SEZIONI]
Formato: professionale con indice
Includi: [ELEMENTI SPECIFICI]
```

### Creare un Artifact calcolatore
```
Crea un artifact HTML con un calcolatore interattivo per [SCOPO].
Campi di input: [LISTA CAMPI]
Formula: [FORMULA O LOGICA]
Output: [COSA MOSTRARE]
Design: pulito, moderno, colori [PALETTE]
```

### Creare un Artifact dashboard
```
Crea un artifact HTML con una dashboard che visualizzi questi dati:
[DATI]
Includi: [TIPI DI GRAFICI]
Design: [STILE]
Aggiungi interattivita: [FILTRI, TOGGLE, etc.]
```

### Analisi comparativa
```
Confronta [OPZIONE A] e [OPZIONE B] su questi criteri: [LISTA].
Per ogni criterio: valutazione 1-5 con motivazione breve.
Formato: tabella + raccomandazione finale.
Concludi con: per chi e meglio A e per chi e meglio B.
```

### Configurare un Project
Istruzioni personalizzate (esempio):
```
Sei un [RUOLO] per [AZIENDA/CONTESTO].
Quando ti invio [TIPO DI INPUT], rispondi con [FORMATO].
Usa sempre: [VINCOLI PERMANENTI].
Fai riferimento ai file di contesto quando pertinente.
Tono: [TONO].
```

---

## Differenze chiave Claude vs ChatGPT

| Aspetto | Claude | ChatGPT |
|---------|--------|---------|
| Contesto massimo | 200K token (~500 pagine) | 128K token (~100 pagine) |
| Generazione immagini | No | Si (DALL-E) |
| Navigazione web | No | Si |
| Output interattivi | Si (Artifacts) | Parziale (Canvas) |
| Spazi di lavoro | Si (Projects) | Si (GPTs) |
| Code execution | No | Si (Code Interpreter) |
| Stile risposte | Preciso, strutturato | Discorsivo, versatile |
| Fedeltà al prompt | Molto alta | Alta |
| Onesta ("non so") | Molto presente | Meno presente |
| Voce | No | Si |

---

## Best practice per Claude

1. **Specifica il formato**: Claude e eccellente nel rispettarlo
2. **Usa Artifacts** per qualsiasi output che beneficia di struttura visuale
3. **Projects per lavoro ricorrente**: configura una volta, usa per mesi
4. **Scegli il modello giusto**: Haiku per velocita, Sonnet di default, Opus per complessita
5. **Chiedi di citare**: "Cita i passaggi rilevanti dal documento" migliora l'affidabilita
6. **Itera gli Artifacts**: puoi perfezionarli con feedback puntuali
7. **Documenti lunghi**: Claude e il migliore per contratti, manuali, specifiche tecniche
8. **Non genera immagini**: per visual, crea Artifacts SVG/HTML oppure usa DALL-E su ChatGPT

---

## Impostazioni consigliate

### Privacy
- **Piano Pro/Team**: i dati NON sono usati per l'addestramento
- **Piano Free**: i dati possono essere usati per il miglioramento del servizio
- In ogni caso: non inserire dati sensibili, personali o riservati

### Organizzazione
- Rinomina le conversazioni importanti
- Usa i Projects per raggruppare il lavoro per tema
- Usa le stelle per marcare le conversazioni da ritrovare

---

*Documento di riferimento — Corso AI Basics — Aggiornato 2026*
