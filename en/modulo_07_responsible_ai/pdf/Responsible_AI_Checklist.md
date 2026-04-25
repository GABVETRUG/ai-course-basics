# Responsible AI Checklist

**AI Basics Course — Module 7**
*In-depth document*

---

## Checklist 1: Before entering data into AI

Use this checklist **every time** before pasting content into ChatGPT, Claude, or other AI tools.

- [ ] **Does the data contain real first and last names?**
  If yes: anonymize (Client A, Employee B) or remove
- [ ] **Are there tax IDs, card numbers, IBANs, passwords?**
  If yes: DO NOT enter. Ever. Under any circumstances
- [ ] **Are there health data of identifiable individuals?**
  If yes: DO NOT enter (GDPR sensitive data)
- [ ] **Does the text contain confidential business information?**
  Strategic plans, non-public financial data, NDA agreements: DO NOT enter
- [ ] **Are there client or partner data?**
  If yes: anonymize or use only aggregated data
- [ ] **Does the content include proprietary source code?**
  If yes: remove credentials, API keys, connection information
- [ ] **Am I using the business/enterprise plan?**
  Enterprise plans offer greater privacy guarantees
- [ ] **Have I disabled training on my data?**
  ChatGPT: Settings > Data controls > Improve the model for everyone: OFF

**Golden rule**: if you have doubts about any data, DO NOT enter it. Ask your DPO.

---

## Checklist 2: After receiving a response from AI

Use this checklist **before using, publishing, or forwarding** any AI output.

### Accuracy verification
- [ ] **Have I read the entire response with a critical eye?**
  Don't trust blindly: read as if it were written by a brilliant intern
- [ ] **Are the cited facts verifiable?**
  Seek confirmation from authoritative sources for data, dates, names, statistics
- [ ] **Do the citations/sources actually exist?**
  Check on Google Scholar, official websites. Fabricated sources are common
- [ ] **Are the numbers and calculations correct?**
  Manually recalculate important numerical data
- [ ] **Are there statements that are "overly confident" on uncertain topics?**
  AI doesn't say "I'm not sure" — it's up to you to question it

### Quality verification
- [ ] **Is the tone appropriate for the recipient?**
  Formal for executives, accessible for clients, technical for the team
- [ ] **Is the length appropriate?**
  AI tends to be verbose. Cut the unnecessary parts
- [ ] **Is the content relevant to my specific context?**
  AI generalizes. Adapt to your industry, company, situation
- [ ] **Have I removed obvious signs of AI generation?**
  Overly perfect sentences, repetitive structures, "in conclusion"

### Ethics verification
- [ ] **Could the content be discriminatory or offensive?**
  Check for bias related to gender, ethnicity, age, disability
- [ ] **Do I need to disclose that I used AI?**
  Check your company policy and the recipient's expectations
- [ ] **Am I ready to take responsibility for this content?**
  If you sign it with your name, you are accountable. Not the AI

---

## Checklist 3: Corporate policy — Essential elements

Use this checklist to verify that your corporate AI policy is complete.

### 1. Purpose and scope
- [ ] Who the policy applies to (all employees? only certain departments?)
- [ ] For which activities AI use is permitted
- [ ] For which activities it is PROHIBITED

### 2. Authorized tools
- [ ] List of AI tools approved by the company
- [ ] Permitted plans/versions (free vs enterprise)
- [ ] Approval process for new tools
- [ ] Explicit prohibition of unauthorized tools

### 3. Data management
- [ ] Clear list of data that CANNOT be entered
- [ ] Required anonymization procedures
- [ ] Mandatory privacy settings (opt-out of training)
- [ ] Reference to the corporate privacy policy and GDPR

### 4. Quality and verification
- [ ] Mandatory human review before publication
- [ ] Verification standards for different types of content
- [ ] Approval process for external content (clients, public)

### 5. Transparency
- [ ] When to disclose AI use (internal vs external)
- [ ] Standard disclosure formula
- [ ] Rules for content generated for clients

### 6. Responsibility
- [ ] Who is responsible for errors in AI output
- [ ] Escalation process in case of an incident
- [ ] Insurance coverage (if applicable)

### 7. Training
- [ ] Mandatory training before use
- [ ] Periodic updates
- [ ] Channel for questions and concerns

### 8. Governance
- [ ] Policy owner (who manages it)
- [ ] Review frequency (recommended: every 6 months)
- [ ] Update process
- [ ] Penalties for violations

---

## Checklist 4: Quick risk assessment

Before using AI for a specific activity, assess the risk using this grid.

| Question | Low risk | Medium risk | High risk |
|----------|----------|-------------|-----------|
| Who will see the output? | Only me | Internal team | Clients/public |
| What type of data am I using? | Public data | Non-sensitive internal data | Personal/confidential data |
| Consequence if wrong? | None | Embarrassment/rework | Legal/financial damage |
| Decision based on AI? | No decision | Internal decision | Decision that impacts others |
| Regulated industry? | No | Partially | Yes (healthcare, finance, legal) |

**Scoring**:
- All "low": proceed with normal precautions
- Even one "medium": apply thorough verification + peer review
- Even one "high": mandatory review by a supervisor, consider whether to use AI at all

---

## Essential regulatory references

### EU AI Act (EU Regulation 2024/1689)
- **In effect**: gradually from 2025 to 2027
- **Classifies AI systems by risk level**: unacceptable, high, limited, minimal
- **Obligations for users of high-risk AI**: human oversight, transparency, documentation
- **Penalties**: up to 7% of annual global revenue

### GDPR (EU Regulation 2016/679)
- Applies to ALL personal data entered into AI
- Requires a legal basis for processing
- Right of access, rectification, erasure
- Mandatory DPIA (Data Protection Impact Assessment) for high-risk processing

### EDPB Guidelines on AI
- The European Data Protection Board has published specific guidelines
- Focus on: lawfulness of training, data subject rights, data transfer outside the EU

---

## Disclosure template (for internal use)

When you need to disclose the use of AI, use one of these formulas:

**For internal documents**:
> This document was drafted with the support of generative AI tools
> and subsequently reviewed and validated by [NAME, ROLE].

**For external communications**:
> The content was developed by our team with the assistance of
> artificial intelligence tools. All information has been verified
> and validated by qualified personnel.

**For presentations**:
> Slides created with the support of generative AI — content verified by [TEAM/PERSON].

---

*Reference document — AI Basics Course — Updated 2026*
