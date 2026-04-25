# Checklist AI Responsabile

**Corso AI Basics — Modulo 7**
*Documento di approfondimento*

---

## Checklist 1: Prima di inserire dati nell'AI

Usa questa checklist **ogni volta** prima di incollare contenuti in ChatGPT, Claude o altri strumenti AI.

- [ ] **I dati contengono nomi e cognomi reali?**
  Se si: anonimizza (Cliente A, Dipendente B) o rimuovi
- [ ] **Ci sono codici fiscali, numeri di carta, IBAN, password?**
  Se si: NON inserire. Mai. In nessun caso
- [ ] **Ci sono dati sanitari di persone identificabili?**
  Se si: NON inserire (dato sensibile GDPR)
- [ ] **Il testo contiene informazioni aziendali riservate?**
  Piani strategici, dati finanziari non pubblici, accordi NDA: NON inserire
- [ ] **Ci sono dati di clienti o partner?**
  Se si: anonimizza o usa solo dati aggregati
- [ ] **Il contenuto include codice sorgente proprietario?**
  Se si: rimuovi credenziali, chiavi API, informazioni di connessione
- [ ] **Sto usando il piano aziendale/enterprise?**
  I piani enterprise offrono maggiori garanzie di privacy
- [ ] **Ho disattivato l'addestramento sui miei dati?**
  ChatGPT: Impostazioni > Controlli dati > Migliora il modello per tutti: OFF

**Regola d'oro**: se hai dubbi su un dato, NON inserirlo. Chiedi al tuo DPO.

---

## Checklist 2: Dopo aver ricevuto una risposta dall'AI

Usa questa checklist **prima di utilizzare, pubblicare o inoltrare** qualsiasi output AI.

### Verifica accuratezza
- [ ] **Ho letto l'intera risposta con attenzione critica?**
  Non fidarti ciecamente: leggi come se fosse scritta da uno stagista brillante
- [ ] **I fatti citati sono verificabili?**
  Cerca conferma su fonti autorevoli per dati, date, nomi, statistiche
- [ ] **Le citazioni/fonti esistono realmente?**
  Verifica su Google Scholar, siti ufficiali. Le fonti inventate sono comuni
- [ ] **I numeri e i calcoli sono corretti?**
  Ricalcola manualmente i dati numerici importanti
- [ ] **Ci sono affermazioni "troppo sicure" su argomenti incerti?**
  L'AI non dice "non sono sicuro" — sta a te dubitare

### Verifica qualita
- [ ] **Il tono e appropriato per il destinatario?**
  Formale per la direzione, accessibile per i clienti, tecnico per il team
- [ ] **La lunghezza e adeguata?**
  L'AI tende a essere prolissa. Taglia il superfluo
- [ ] **Il contenuto e pertinente al mio contesto specifico?**
  L'AI generalizza. Adatta al tuo settore, azienda, situazione
- [ ] **Ho rimosso i segni evidenti di generazione AI?**
  Frasi troppo perfette, strutture ripetitive, "in conclusione"

### Verifica etica
- [ ] **Il contenuto potrebbe essere discriminatorio o offensivo?**
  Controlla bias di genere, etnia, eta, disabilita
- [ ] **Devo dichiarare che ho usato l'AI?**
  Verifica la policy aziendale e le aspettative del destinatario
- [ ] **Sono pronto ad assumermi la responsabilita di questo contenuto?**
  Se lo firmi con il tuo nome, ne rispondi tu. Non l'AI

---

## Checklist 3: Policy aziendale — Elementi essenziali

Usa questa checklist per verificare che la tua policy aziendale sull'AI sia completa.

### 1. Scopo e ambito
- [ ] A chi si applica la policy (tutti i dipendenti? solo alcuni reparti?)
- [ ] Per quali attivita e consentito l'uso dell'AI
- [ ] Per quali attivita e VIETATO

### 2. Strumenti autorizzati
- [ ] Lista degli strumenti AI approvati dall'azienda
- [ ] Piani/versioni consentiti (free vs enterprise)
- [ ] Processo di approvazione per nuovi strumenti
- [ ] Divieto esplicito di strumenti non autorizzati

### 3. Gestione dei dati
- [ ] Elenco chiaro dei dati che NON possono essere inseriti
- [ ] Procedure di anonimizzazione richieste
- [ ] Impostazioni di privacy obbligatorie (opt-out addestramento)
- [ ] Riferimento alla policy privacy aziendale e GDPR

### 4. Qualita e verifica
- [ ] Obbligo di revisione umana prima della pubblicazione
- [ ] Standard di verifica per diversi tipi di contenuto
- [ ] Processo di approvazione per contenuti esterni (clienti, pubblico)

### 5. Trasparenza
- [ ] Quando dichiarare l'uso dell'AI (interno vs esterno)
- [ ] Formula standard di disclosure
- [ ] Regole per contenuti generati per clienti

### 6. Responsabilita
- [ ] Chi e responsabile degli errori nell'output AI
- [ ] Processo di escalation in caso di incidente
- [ ] Copertura assicurativa (se applicabile)

### 7. Formazione
- [ ] Formazione obbligatoria prima dell'uso
- [ ] Aggiornamenti periodici
- [ ] Canale per dubbi e domande

### 8. Governance
- [ ] Responsabile della policy (chi la gestisce)
- [ ] Frequenza di revisione (consigliato: ogni 6 mesi)
- [ ] Processo di aggiornamento
- [ ] Sanzioni per violazioni

---

## Checklist 4: Valutazione rapida del rischio

Prima di usare l'AI per un'attivita specifica, valuta il rischio con questa griglia.

| Domanda | Basso rischio | Medio rischio | Alto rischio |
|---------|--------------|---------------|-------------|
| Chi vedra l'output? | Solo io | Team interno | Clienti/pubblico |
| Che tipo di dati uso? | Dati pubblici | Dati interni non sensibili | Dati personali/riservati |
| Conseguenza se errato? | Nessuna | Imbarazzo/rework | Danno legale/economico |
| Decisione basata su AI? | Nessuna decisione | Decisione interna | Decisione che impatta altri |
| Settore regolamentato? | No | Parzialmente | Si (sanita, finanza, legale) |

**Punteggio**:
- Tutto "basso": procedi con le normali precauzioni
- Anche un solo "medio": applica verifica accurata + revisione di un collega
- Anche un solo "alto": revisione obbligatoria da responsabile, valuta se usare l'AI

---

## Riferimenti normativi essenziali

### EU AI Act (Regolamento UE 2024/1689)
- **In vigore**: gradualmente dal 2025 al 2027
- **Classifica i sistemi AI per livello di rischio**: inaccettabile, alto, limitato, minimo
- **Obblighi per gli utenti di AI ad alto rischio**: supervisione umana, trasparenza, documentazione
- **Sanzioni**: fino al 7% del fatturato globale annuo

### GDPR (Regolamento UE 2016/679)
- Si applica a TUTTI i dati personali inseriti nell'AI
- Richiede base giuridica per il trattamento
- Diritto di accesso, rettifica, cancellazione
- Obbligo di DPIA (Valutazione d'Impatto) per trattamenti ad alto rischio

### Linee guida EDPB sull'AI
- Il Comitato Europeo per la Protezione dei Dati ha pubblicato linee guida specifiche
- Focus su: liceita dell'addestramento, diritti degli interessati, trasferimento dati extra-UE

---

## Template di disclosure (uso interno)

Quando devi dichiarare l'uso dell'AI, usa una di queste formule:

**Per documenti interni**:
> Questo documento e stato redatto con il supporto di strumenti di AI generativa
> e successivamente rivisto e validato da [NOME, RUOLO].

**Per comunicazioni esterne**:
> Il contenuto e stato sviluppato dal nostro team con l'ausilio di strumenti
> di intelligenza artificiale. Tutte le informazioni sono state verificate
> e validate dal personale competente.

**Per presentazioni**:
> Slide realizzate con il supporto di AI generativa — contenuti verificati da [TEAM/PERSONA].

---

*Documento di riferimento — Corso AI Basics — Aggiornato 2026*
