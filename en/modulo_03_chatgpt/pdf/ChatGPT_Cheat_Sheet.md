# ChatGPT Cheat Sheet

**AI Basics Course — Module 3**
*Quick reference guide*

---

## Access and Plans

| Plan | Cost | Models | Main Features |
|-------|-------|---------|-------------------|
| Free | Free | GPT-4o mini + GPT-4o (limited) | Chat, file upload, web, DALL-E (limited) |
| Plus | $20/month | GPT-4o + o3 + DALL-E | Everything unlimited, custom GPTs, Canvas |
| Team | $25/user/month | Same as Plus | Shared workspace, data privacy |
| Enterprise | On request | Everything | SSO, admin console, enterprise privacy |

**URL**: chat.openai.com or chatgpt.com

---

## Main Features

### Chat
- Each conversation is isolated (separate context)
- Use "New chat" when you change topics
- Rename important chats to find them later
- Pin frequent chats with "Pin"

### File Upload
Supported formats: PDF, DOCX, XLSX, PPTX, CSV, TXT, images (JPG, PNG), code
- Drag the file into the chat or use the attachment icon
- You can upload multiple files in the same chat
- Max ~50 pages for optimal results

### Web Browsing
- Activates automatically for questions about recent events
- Force it with: "Search online..." or "Find the latest information on..."
- Shows clickable sources in the response

### DALL-E (Image Generation)
- Natural language prompts
- Formula: SUBJECT + STYLE + DETAILS + FORMAT
- Does not handle text in images well
- Each edit generates a NEW image

### Code Interpreter
- Runs Python code in a secure environment
- Upload CSV/Excel for automatic analysis
- Generates downloadable charts (PNG, SVG)
- No Python knowledge needed: describe what you want in plain language

### Canvas
- Collaborative editing for text and code
- Select portions of text for targeted modifications
- Activate with: "Use canvas for..." or automatically for long texts

### Memory
- ChatGPT remembers information across conversations
- "Remember that I prefer responses in English and brief"
- Manage: Settings > Personalization > Memory

### Custom Instructions
- Settings > Personalization > Custom Instructions
- Two fields: "What should ChatGPT know about you" + "How should ChatGPT respond"
- Applied to EVERY new chat automatically

---

## GPTs: Custom Assistants

### Using Existing GPTs
1. Go to chatgpt.com/gpts
2. Search by category or keyword
3. Click to start using it
4. You can tag a GPT with @name in any chat

### Creating a Custom GPT
1. Go to chatgpt.com/gpts/editor
2. "Create" tab: describe what you want in natural language
3. "Configure" tab: name, instructions, knowledge files, tools
4. "Preview" tab: test and iterate
5. Publish: Only for you / With link / In the Store

### GPT Instructions: What to Include
```
You are a [ROLE] with experience in [DOMAIN].
Your task is [OBJECTIVE].
Always respond in [LANGUAGE] with a [TONE] tone.
Response format: [FORMAT].
Constraints: [CONSTRAINTS].
When you don't know something: [BEHAVIOR].
```

---

## Effective Prompts for ChatGPT

### Document Analysis
```
Analyze the attached document and create an executive summary.
Structure: Context (2 lines), Key Points (5 bullets),
Risks (3 bullets), Recommendation.
Audience: [WHO]. Tone: professional.
```

### Data Analysis (with Code Interpreter)
```
Analyze the attached dataset:
1. Describe the structure and quality of the data
2. Identify the 3 main trends with charts
3. Flag anomalies or outliers
4. Create a 10-line report with 2 recommendations
```

### Image Generation (DALL-E)
```
Create an image of [SUBJECT].
Style: [flat illustration / photographic / watercolor / minimal].
Colors: [PALETTE].
Mood: [MOOD].
Format: [landscape 16:9 / portrait / square].
No text in the image.
```

### Presentation Creation
```
Create the structure of a [N]-slide presentation on [TOPIC].
Audience: [WHO]. Duration: [MINUTES].
For each slide: title + 3-4 bullets + visual suggestion.
Tone: [TONE].
```

### Canvas for Text Editing
```
Use canvas. Write a [TYPE OF TEXT] about [TOPIC].
[SPECIFIC INSTRUCTIONS].
Then wait for my feedback before making changes.
```

---

## Important Settings

### Data Privacy
- **Settings > Data Controls > Improve the model for everyone**: Disable
  (prevents your chats from being used for training)
- With Team/Enterprise plans: data is never used for training

### Optimizing the Experience
- **Dark theme**: Settings > General > Theme
- **Interface language**: Settings > General > Language
- **Export data**: Settings > Data Controls > Export Data

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl/Cmd + Shift + O | Open/close sidebar |
| Ctrl/Cmd + Shift + ; | Copy last response |
| Ctrl/Cmd + / | Show all shortcuts |

---

## Limitations to Remember

| Limitation | Detail | Workaround |
|--------|-----------|------------|
| Verbose responses | ChatGPT tends to write too much | "Respond in max 5 bullets of 1 line" |
| Long context | Loses track in very long chats | Open a new chat with a summary |
| Text in images | DALL-E renders text poorly | Add text afterward with another tool |
| Hallucinations | Can invent facts | ALWAYS verify critical facts |
| Excessive refusals | Sometimes refuses legitimate requests | Specify the professional context |
| URLs | Does not access URLs reliably | Copy-paste the content |

---

*Reference document — AI Basics Course — Updated 2026*
