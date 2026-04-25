# Claude Cheat Sheet

**AI Basics Course — Module 4**
*Quick reference guide*

---

## Access and Plans

| Plan | Cost | Models | Main Features |
|-------|-------|---------|-------------------|
| Free | Free | Sonnet | Chat, Artifacts, file upload (limited) |
| Pro | $20/month | Opus + Sonnet + Haiku | 5x messages, Projects, all models |
| Team | $25/user/month | Same as Pro | Shared workspace, admin tools |
| Enterprise | On request | Everything | SSO, SAML, SLA, enterprise privacy |

**URL**: claude.ai

---

## The Three Models

| Model | Ideal Use | Speed | Quality |
|---------|-----------|----------|---------|
| **Haiku** | Quick questions, simple tasks | Very fast | Good |
| **Sonnet** | Daily use, balanced (default) | Fast | Very good |
| **Opus** | Complex analysis, reasoning, coding | Slower | Excellent |

**How to switch**: dropdown menu at the top of the chat area.

**Rule of thumb**: start with Sonnet. If the response is not satisfactory, retry with Opus. Use Haiku for quick "yes/no" questions.

---

## Distinctive Features

### Long Context (200K tokens)
- Approximately 500 pages of text in a single conversation
- Ideal for: contracts, manuals, long reports, source code
- ChatGPT Free handles about 100 pages (128K); Claude handles 500 (200K)
- Upload the document and Claude analyzes it in its entirety

### Artifacts
Interactive outputs that open in a side panel:

| Type | Example | How to Request |
|------|---------|---------------|
| Document | Formatted report with table of contents | "Create a formatted document about..." |
| Code | Script with syntax highlighting | "Write a program that..." |
| Interactive HTML | Calculator, quiz, dashboard | "Create an interactive calculator for..." |
| SVG | Diagrams, charts, icons | "Create a flowchart of..." |
| Table | Structured data | "Create a comparison table of..." |

**Actions on Artifacts**:
- Copy the content
- Download as a file
- Share via link (if enabled)
- Request changes: "Edit the artifact: change..."

### Projects
Workspaces with persistent context:

1. Create a project (sidebar > + New Project)
2. Add **custom instructions** (system prompt)
3. Upload **context files** (templates, data, reference documents)
4. Every new chat in the project automatically inherits the instructions and files

**Examples of useful projects**:
- Recurring report (template + KPIs + historical data)
- Project assistant (brief + timeline + stakeholders)
- Knowledge base (manuals + procedures + FAQ)
- Brand writing (tone of voice + brand guidelines + examples)

---

## Effective Prompts for Claude

### Long Document Analysis
```
I have uploaded a [N]-page document about [TOPIC].
1. Describe the structure (main sections)
2. List the 5 key points
3. Identify any ambiguities or contradictions
4. Create an operational checklist based on the content
Cite relevant passages from the document.
```

### Creating a Document Artifact
```
Create an artifact with a formatted document:
Title: [TITLE]
Sections: [LIST OF SECTIONS]
Format: professional with table of contents
Include: [SPECIFIC ELEMENTS]
```

### Creating a Calculator Artifact
```
Create an HTML artifact with an interactive calculator for [PURPOSE].
Input fields: [LIST OF FIELDS]
Formula: [FORMULA OR LOGIC]
Output: [WHAT TO DISPLAY]
Design: clean, modern, colors [PALETTE]
```

### Creating a Dashboard Artifact
```
Create an HTML artifact with a dashboard that visualizes this data:
[DATA]
Include: [CHART TYPES]
Design: [STYLE]
Add interactivity: [FILTERS, TOGGLES, etc.]
```

### Comparative Analysis
```
Compare [OPTION A] and [OPTION B] on these criteria: [LIST].
For each criterion: rating 1-5 with brief rationale.
Format: table + final recommendation.
Conclude with: who Option A is better for and who Option B is better for.
```

### Configuring a Project
Custom instructions (example):
```
You are a [ROLE] for [COMPANY/CONTEXT].
When I send you [TYPE OF INPUT], respond with [FORMAT].
Always use: [PERMANENT CONSTRAINTS].
Refer to the context files when relevant.
Tone: [TONE].
```

---

## Key Differences: Claude vs ChatGPT

| Aspect | Claude | ChatGPT |
|---------|--------|---------|
| Maximum context | 200K tokens (~500 pages) | 128K tokens (~100 pages) |
| Image generation | No | Yes (DALL-E) |
| Web browsing | No | Yes |
| Interactive outputs | Yes (Artifacts) | Partial (Canvas) |
| Workspaces | Yes (Projects) | Yes (GPTs) |
| Code execution | No | Yes (Code Interpreter) |
| Response style | Precise, structured | Conversational, versatile |
| Prompt adherence | Very high | High |
| Honesty ("I don't know") | Very present | Less present |
| Voice | No | Yes |

---

## Best Practices for Claude

1. **Specify the format**: Claude is excellent at following it
2. **Use Artifacts** for any output that benefits from visual structure
3. **Projects for recurring work**: configure once, use for months
4. **Choose the right model**: Haiku for speed, Sonnet by default, Opus for complexity
5. **Ask for citations**: "Cite relevant passages from the document" improves reliability
6. **Iterate on Artifacts**: you can refine them with specific feedback
7. **Long documents**: Claude is the best for contracts, manuals, technical specifications
8. **No image generation**: for visuals, create SVG/HTML Artifacts or use DALL-E on ChatGPT

---

## Recommended Settings

### Privacy
- **Pro/Team plan**: data is NOT used for training
- **Free plan**: data may be used for service improvement
- In any case: do not enter sensitive, personal, or confidential data

### Organization
- Rename important conversations
- Use Projects to group work by topic
- Use stars to bookmark conversations you want to find later

---

*Reference document — AI Basics Course — Updated 2026*
