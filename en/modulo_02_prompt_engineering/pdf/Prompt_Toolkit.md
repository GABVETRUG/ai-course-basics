# Prompt Toolkit — 20 Ready-to-Use Templates

**AI Basics Course — Module 2**
*Supplementary document*

---

## How to use this document

Each template is structured as follows:
- **Scenario**: when to use it
- **Template**: the prompt to copy and adapt (replace the placeholders in [brackets])
- **Example**: the prompt filled in with realistic data
- **Tip**: a suggestion to improve results

Works with ChatGPT, Claude, and HuggingChat. Placeholders [IN UPPERCASE] should be replaced with your own data.

---

## Category 1: Written Communication

### 1. Professional Email

**Scenario**: You need to write a formal email for a specific work situation.

**Template**:
```
Write a professional email to [RECIPIENT] regarding [TOPIC].
Context: [SITUATION].
Goal of the email: [WHAT YOU WANT TO ACHIEVE].
Tone: [formal/friendly/assertive].
Maximum length: [N] words.
Include: the email subject line.
```

**Example**:
```
Write a professional email to the sales director regarding the delay
in the delivery of the Alpha project.
Context: the supplier has communicated a 2-week delay due to supply
chain issues. Our deadline is July 30.
Goal: inform about the delay, propose a mitigation plan,
request a meeting to discuss options.
Tone: professional but not alarmist.
Maximum length: 200 words.
Include: the email subject line.
```

**Tip**: Always specify the tone. "Professional" and "friendly" produce very different emails.

---

### 2. Response to a Complaint

**Scenario**: You need to respond to a dissatisfied customer.

**Template**:
```
You are a customer service manager with 10 years of experience.
Write a professional response to the following complaint:
"[COMPLAINT TEXT]"

The response must:
- Acknowledge the customer's frustration
- Briefly explain the cause (if known): [CAUSE]
- Propose a concrete solution: [SOLUTION]
- Close with a next step
Tone: empathetic and solution-oriented. Max 150 words.
```

**Tip**: Role-playing ("You are a manager...") dramatically improves the tone of the response.

---

### 3. Meeting Minutes

**Scenario**: You need to turn messy notes into structured minutes.

**Template**:
```
Transform the following notes into professional meeting minutes:

[PASTE YOUR NOTES HERE]

Required format:
- Date, attendees, duration
- Discussion points (numbered)
- Decisions made
- Action items (with owner and deadline)
- Next meeting
Tone: formal and concise.
```

**Tip**: Even very messy notes work well. AI is excellent at bringing structure to chaos.

---

### 4. LinkedIn Post

**Scenario**: You need to create an effective LinkedIn post.

**Template**:
```
Create a LinkedIn post about [TOPIC].
Goal: [WHAT YOU WANT TO COMMUNICATE].
Target: [AUDIENCE].
Style: [storytelling / statistic / open question / list / lesson learned].
Length: 100-150 words.
Include a compelling opening hook and a final call-to-action.
Suggest 3-5 relevant hashtags.
```

**Tip**: Ask for variants in different styles, then choose the best one. "Give me 3 alternative versions" is a very powerful prompt.

---

## Category 2: Analysis and Research

### 5. SWOT Analysis

**Scenario**: You need to do a quick strategic analysis.

**Template**:
```
Create a SWOT analysis for [COMPANY/PROJECT/PRODUCT].
Context: [INDUSTRY, MARKET, CURRENT SITUATION].
Main competitors: [LIST].

For each quadrant (Strengths, Weaknesses, Opportunities, Threats)
provide 4-5 points with a brief explanation.
Conclude with 3 prioritized strategic recommendations.
Format: 2x2 table + recommendations list.
```

**Tip**: The more context you provide about the industry and competitors, the more relevant and less generic the analysis will be.

---

### 6. Feedback / Review Analysis

**Scenario**: You have collected feedback and want to extract insights.

**Template**:
```
Analyze the following customer feedback:

[PASTE FEEDBACK HERE]

For each one, classify:
- Sentiment: positive / negative / neutral
- Theme: [product / service / price / support / delivery]
- Urgency: high / medium / low

Then provide:
1. The 3 most recurring themes
2. The 2 main critical issues
3. The 2 strengths that emerged
4. 3 prioritized improvement actions
5. Estimated satisfaction score (1-10)
```

**Tip**: Works great with feedback copied from Google Reviews, Trustpilot, internal surveys.

---

### 7. Quick Market Research

**Scenario**: You need to get up to speed on a new market or topic.

**Template**:
```
You are a market analyst. Give me a briefing on [MARKET/INDUSTRY].
Cover the following aspects:
1. Market size and growth trends
2. Main players (top 5) with positioning
3. Typical customer target
4. Challenges and barriers to entry
5. Emerging opportunities
6. Relevant technology trends

Format: one section per point, with concise bullet points.
Note: indicate when information may not be up to date.
```

**Tip**: Adding "Note: indicate when information may not be up to date" helps reduce the risk of hallucinations.

---

### 8. Options Comparison / Decision

**Scenario**: You need to choose between multiple alternatives.

**Template**:
```
Help me compare the following options for [DECISION]:
Option A: [DESCRIPTION]
Option B: [DESCRIPTION]
Option C: [DESCRIPTION] (optional)

Evaluation criteria: [LIST OF CRITERIA with relative weight]
Example: cost (weight 3), quality (weight 5), timeline (weight 4)

Create a decision matrix with a 1-5 score for each criterion.
Calculate the weighted total score.
Conclude with a reasoned recommendation.
```

**Tip**: Relative weights are critical. Without them, the AI assigns equal weights that may not reflect your priorities.

---

## Category 3: Daily Productivity

### 9. To-do List from Free Text

**Scenario**: You have messy text with many things to do and want an organized list.

**Template**:
```
Extract all action items from the following text and organize them
into a to-do list:

[PASTE YOUR TEXT HERE]

Format for each action:
- [ ] Action (priority: high/medium/low) — deadline if mentioned
Group by category or project if possible.
Sort by descending priority.
```

**Tip**: Works great with emails, meeting notes, transcribed voice messages.

---

### 10. Document Summary

**Scenario**: You need to summarize a long document.

**Template**:
```
Summarize the following document in [N] key points:

[PASTE THE DOCUMENT]

The summary is intended for [RECIPIENT] who needs to [OBJECTIVE].
Highlight in particular: [ASPECTS TO HIGHLIGHT].
Format: numbered list, each point in 1-2 sentences.
Conclude with: "Action required: [yes/no and what]"
```

**Tip**: Claude excels at summarizing long documents thanks to its 200K-token context window.

---

### 11. Meeting Preparation

**Scenario**: You need to prepare for an important meeting.

**Template**:
```
Help me prepare for a meeting about [TOPIC].
Attendees: [WHO].
My role: [ROLE].
Meeting objective: [OBJECTIVE].

Prepare for me:
1. 5 key questions to ask
2. 3 possible objections and how to respond
3. The most important data/facts to have ready
4. Proposed agenda (with time allocations)
5. 2-3 possible meeting outcomes
```

**Tip**: Add information about the political/relational context ("manager X is skeptical about...") for more calibrated responses.

---

### 12. Text Revision

**Scenario**: You have written a text and want to improve it.

**Template**:
```
Revise the following text:

[PASTE THE TEXT]

Revision criteria:
- Grammatical and spelling correctness
- Clarity and readability
- Tone: [DESIRED TONE]
- Target audience: [RECIPIENT]

Provide:
1. The corrected text (highlight changes with **bold**)
2. List of main changes with rationale
3. One general suggestion for improving the writing
DO NOT change the meaning or add content not present in the original.
```

**Tip**: "DO NOT change the meaning" is crucial. Without this constraint, AI tends to rewrite too much.

---

## Category 4: Training and Learning

### 13. Explain a Concept

**Scenario**: You need to understand or explain a complex topic to others.

**Template**:
```
Explain [CONCEPT] so that [TARGET AUDIENCE] can understand it.
Use:
- An analogy from everyday life
- A practical example
- Max [N] words
Avoid: jargon, unexplained acronyms, assumed prior knowledge.
At the end add "3 things to remember" as a bulleted list.
```

**Tip**: The constraint on the target audience and the analogy are the two elements that transform the response from encyclopedic to useful.

---

### 14. Self-Assessment Quiz

**Scenario**: You want to test your knowledge on a topic.

**Template**:
```
Create a quiz of [N] questions on [TOPIC].
Level: [beginner/intermediate/advanced].
Mix of formats: multiple choice, true/false, short open answer.
For each question provide the correct answer and a brief explanation.
Put the answers at the end of the quiz, not after each question.
```

**Tip**: Use the quiz to verify what you actually understood after studying a topic.

---

### 15. Study Plan

**Scenario**: You want to learn something new and need a roadmap.

**Template**:
```
Create a study plan for learning [TOPIC].
Current level: [BEGINNER/INTERMEDIATE].
Available time: [N hours/week] for [N weeks].
Goal: [WHAT YOU WANT TO BE ABLE TO DO AT THE END].

For each week indicate:
- Topic
- Recommended resources (free)
- Practical exercise
- How to verify understanding
```

**Tip**: Add "free resources" to avoid getting only paid course suggestions.

---

## Category 5: Data and Organization

### 16. Structured Data from Text

**Scenario**: You need to extract structured data from unstructured text.

**Template**:
```
Extract the following data from the text and organize them in a table:

Data to extract: [LIST OF FIELDS, e.g.: name, email, company, role]

Text:
[PASTE THE TEXT]

Output format: markdown table.
If a data point is not present, write "N/A".
```

**Tip**: Works surprisingly well with emails, photographed business cards (on multimodal models), and resumes in text format.

---

### 17. Excel / Google Sheets Formula

**Scenario**: You need a formula you don't know how to write.

**Template**:
```
I have an Excel/Google Sheets spreadsheet with these columns:
[DESCRIPTION OF COLUMNS]

I need a formula that: [WHAT IT SHOULD DO].

Provide:
1. The formula
2. Where to place it (which cell)
3. Step-by-step explanation of how it works
4. An example with sample data
If multiple formulas are needed, number them in order of execution.
```

**Tip**: Describe the spreadsheet structure using column letters (A, B, C) and row numbers for more precise answers.

---

### 18. Standard Operating Procedure (SOP)

**Scenario**: You need to document a business process.

**Template**:
```
Create a SOP (Standard Operating Procedure) for [PROCESS].
Context: [DEPARTMENT/FUNCTION].
Performed by: [ROLE].
Frequency: [HOW OFTEN].

Structure:
1. Purpose
2. Scope
3. Prerequisites and required tools
4. Step-by-step procedure (numbered)
5. Success criteria
6. What to do in case of problems
7. Reference contacts

Tone: clear, imperative ("Do X", not "You could do X").
```

**Tip**: The generated SOP is an excellent starting point, but it should always be validated by the person who actually performs the process.

---

## Category 6: Creativity and Brainstorming

### 19. Structured Brainstorming

**Scenario**: You need creative ideas for a problem or project.

**Template**:
```
You are an expert consultant in [INDUSTRY] with 20 years of experience.
Problem/Challenge: [DESCRIPTION].
Constraints: [BUDGET, TIME, RESOURCES].
Target: [WHO WILL BENEFIT].

Generate [N] creative ideas; for each one indicate:
- Name/Title of the idea
- Description (2-3 sentences)
- Estimated cost: low / medium / high
- Expected impact: 1-5
- Implementation time: short / medium / long
- Main risk

Sort by impact-to-cost ratio (best first).
Include at least 2 "out-of-the-box" ideas.
```

**Tip**: "Include at least 2 out-of-the-box ideas" pushes the model beyond the obvious answers.

---

### 20. Project/Product Name

**Scenario**: You need to find a catchy name.

**Template**:
```
Generate 10 name proposals for [TYPE: project/product/event/course]
about [TOPIC].

Requirements:
- Target: [AUDIENCE]
- Tone: [professional/creative/playful/technical]
- Language: [English/bilingual]
- Length: max [N] words

For each proposal:
- Name
- Meaning/rationale (1 line)
- Pros and cons of the name

Include diverse variants: acronyms, metaphors, wordplay, descriptive names.
```

**Tip**: Also ask "Which of these names likely have available web domains?" for an extra check.

---

## Emergency Prompt

When you don't know how to formulate a prompt, use this **meta-prompt**:

```
I need to [OBJECTIVE] for [CONTEXT].
My audience is [WHO].
I'm not sure how to ask you to help me.
Ask me 3 questions to better understand what I need,
then propose the best prompt to achieve the result.
```

This meta-prompt works because it delegates to the AI the task of helping you formulate the right question.

---

*Reference document — AI Basics Course — Updated 2026*
