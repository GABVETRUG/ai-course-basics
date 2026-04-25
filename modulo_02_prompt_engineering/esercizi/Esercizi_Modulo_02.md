# Scheda Esercizi — Modulo 2: Prompt Engineering

**Corso AI Basics**
*Durata parte pratica: 2 ore*

---

## Lab 1: Da prompt vaghi a prompt efficaci (30 min)

### Esercizio 1.1: Email professionale

**Il prompt vago** (invialo cosi com'e a ChatGPT o Claude):
```
Scrivi un'email al capo
```

**Analisi della risposta**: cosa manca?
- [ ] Contesto specifico
- [ ] Tono definito
- [ ] Obiettivo chiaro
- [ ] Lunghezza controllata
- [ ] Altro: _______________

**Ora riscrivi il prompt usando le tecniche apprese:**
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**Confronto**: la seconda risposta e migliore? In cosa?

_______________________________________________________

---

### Esercizio 1.2: Riassunto

**Il prompt vago**:
```
Riassumi questo testo
```
(Usa un articolo di giornale o un documento a tua scelta)

**Riscrivi il prompt con: destinatario, lunghezza, formato, aspetti da evidenziare:**
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

---

### Esercizio 1.3: Brainstorming

**Il prompt vago**:
```
Dammi idee per il marketing
```

**Riscrivi il prompt con: ruolo, contesto, vincoli, formato output:**
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**Quante delle tecniche hai usato?**
- [ ] Ruolo (role-playing)
- [ ] Contesto
- [ ] Formato output
- [ ] Vincoli (lunghezza, tono, etc.)
- [ ] Few-shot (esempi)

---

## Lab 2: Scenari lavorativi reali (45 min)

Scegli **almeno 4** degli 8 scenari seguenti. Per ciascuno: scrivi il prompt, invialo, valuta la risposta.

### Scenario A: Brainstorming progetto

**Prompt da usare** (adattalo alla tua realta):
```
Sei un consulente strategico. La mia azienda [SETTORE] ha il problema
di [PROBLEMA]. Genera 8 idee per risolverlo. Per ogni idea indica:
azione, costo (basso/medio/alto), impatto (1-5), tempi.
Ordina per rapporto impatto/costo.
```

**Il tuo prompt personalizzato**:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**Valutazione risposta** (1-5): Pertinenza __ | Qualita idee __ | Formato __

---

### Scenario B: Report executive

**Prompt da usare**:
```
Scrivi un report executive di 1 pagina su [ARGOMENTO].
Dati: [INSERISCI DATI].
Struttura: Sintesi (3 righe), Risultati chiave (tabella),
Criticita (lista), Azioni per il prossimo periodo (3 punti).
Tono professionale, pronto per il management.
```

**Il tuo prompt personalizzato**:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**Valutazione risposta** (1-5): Pertinenza __ | Qualita __ | Formato __

---

### Scenario C: Traduzione adattata

**Prompt da usare**:
```
Traduci il seguente testo dall'italiano all'inglese.
Non tradurre letteralmente: adatta il tono al mercato [PAESE].
Mantieni registro [TIPO]. Segnala le scelte di adattamento.
Testo: [INSERISCI TESTO]
```

**Valutazione**: la traduzione e naturale o suona "tradotta"?

_______________________________________________________

---

### Scenario D: Supporto decisionale

**Prompt da usare**:
```
Aiutami a scegliere tra: Opzione A [DESC] e Opzione B [DESC].
Criteri: [LISTA CON PESI].
Crea matrice decisionale pesata (punteggio 1-5 per criterio).
Concludi con raccomandazione motivata.
```

**La decisione suggerita dall'AI ti convince? Perche si/no?**

_______________________________________________________

---

### Scenario E: Preparazione presentazione

**Prompt da usare**:
```
Crea la struttura di una presentazione di 10 slide su [ARGOMENTO].
Pubblico: [CHI]. Durata: [MINUTI].
Per ogni slide: titolo + 3-4 bullet + suggerimento visuale.
```

**Useresti questa struttura? Cosa cambieresti?**

_______________________________________________________

---

### Scenario F: Social media

**Prompt da usare**:
```
Sei un social media manager per [AZIENDA/SETTORE].
Crea 3 post LinkedIn su [TEMA]. 100-150 parole ciascuno.
Hook iniziale + call-to-action + 3 hashtag.
Stili diversi: storytelling, dato statistico, domanda.
```

**Il tono e coerente con il brand? Cosa aggiusteresti?**

_______________________________________________________

---

### Scenario G: Analisi feedback

**Prompt da usare** (inserisci feedback reali o inventati):
```
Analizza questi feedback: [INCOLLA]
Classifica: sentiment, tema, urgenza.
Riepilogo: temi ricorrenti, punti critici, azioni di miglioramento.
```

**L'AI ha individuato pattern che non avevi notato?**

_______________________________________________________

---

### Scenario H: Template email

**Prompt da usare**:
```
Crea 3 template email per: [SITUAZIONI].
Per ciascuno: oggetto + corpo (max 100 parole).
Tono professionale ma cordiale.
Segnaposti: [NOME], [DATA], [DETTAGLIO].
```

**I template sono utilizzabili? Cosa modificheresti?**

_______________________________________________________

---

## Lab 3: Confronto tra strumenti (30 min)

### Istruzioni
1. Scegli UNO degli scenari del Lab 2
2. Invia lo **stesso identico prompt** a ChatGPT, Claude e HuggingChat
3. Compila la tabella di confronto

### Scenario scelto: _______________________

### Tabella di confronto

| Criterio | ChatGPT (1-5) | Claude (1-5) | HuggingChat (1-5) |
|----------|---------------|-------------|-------------------|
| Pertinenza (risponde a cio che hai chiesto?) | | | |
| Completezza (copre tutti i punti?) | | | |
| Formato (rispetta la struttura richiesta?) | | | |
| Qualita linguaggio | | | |
| Originalita / valore aggiunto | | | |
| Velocita di risposta | | | |
| **TOTALE** | | | |

### Osservazioni

**Quale strumento ha dato il risultato migliore?** _______________

**Perche?** _______________________________________________________

**Per questo tipo di task, in futuro useresti**: _______________

---

## Esercizio bonus: il meta-prompt

Se hai tempo, prova questo approccio potente:

```
Devo [OBIETTIVO] per [CONTESTO].
Non so come chiederti di aiutarmi al meglio.
Fammi 3 domande per capire meglio cosa mi serve,
poi proponi il prompt ottimale per ottenere il risultato.
```

**Ha funzionato? Il prompt suggerito dall'AI era buono?**

_______________________________________________________

---

## Riepilogo: le mie tecniche preferite

Dopo gli esercizi, segna le tecniche che ti sono risultate piu utili:

- [ ] Role-playing (assegnare un ruolo)
- [ ] Few-shot (dare esempi)
- [ ] Chain-of-thought (ragionamento passo-passo)
- [ ] Output strutturato (specificare il formato)
- [ ] Vincoli (lunghezza, tono, lingua)
- [ ] Decomposizione (spezzare in sotto-compiti)
- [ ] Iterazione (raffinare dopo la prima risposta)
- [ ] Meta-prompt (chiedere all'AI di aiutarti a chiedere)

---

## Note personali

```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

---

*Corso AI Basics — Modulo 2 — Scheda esercizi*
