#!/usr/bin/env python3
"""Generate slides for Module 4 — Claude: the rival you need to know (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────
title_slide(prs,
    "Module 4",
    "Claude: the rival you need to know",
    "AI Basics Course  |  Duration: 3 hours  |  0.5h Theory + 2.5h Lab")

agenda_slide(prs, [
    "Anthropic: who is behind Claude and why it's different",
    "The Claude models: Opus, Sonnet, Haiku",
    "Distinctive features: long context, Artifacts, Projects",
    "Claude vs ChatGPT: strengths compared",
    "Lab 1: analyzing a long document",
    "Lab 2: creating interactive Artifacts",
    "Lab 3: direct comparison Claude vs ChatGPT",
    "Lab 4: organizing work with Projects",
])

# ── 2. SECTION 1 — ANTHROPIC AND CLAUDE ──────────────
section_slide(prs, 1, "Anthropic and Claude",
              "The company, the philosophy and the models")

content_slide(prs, "Who is Anthropic", [
    "Founded in 2021 by former OpenAI researchers (Dario and Daniela Amodei)",
    "Mission: build reliable, interpretable and steerable AI",
    "",
    "Key difference from OpenAI:",
    "   OpenAI: 'Let's move fast, AI is too important to slow down'",
    "   Anthropic: 'Let's move responsibly, safety comes first'",
    "",
    "Funded by Google, Amazon and others for over 7 billion dollars",
    "Headquarters: San Francisco",
    "",
    "Claude is Anthropic's only consumer product",
    "   The name comes from Claude Shannon, father of information theory",
])

highlight_slide(prs,
    "THE PHILOSOPHY OF CLAUDE",
    "Constitutional AI:\n"
    "the model follows a set of ethical principles\n"
    "defined explicitly, not just human feedback.",
    "Result: Claude tends to be more cautious, honest and structured in its responses.")

content_slide(prs, "The Claude models", [
    "Claude Opus — The most powerful",
    "   Complex reasoning, in-depth analysis, difficult tasks",
    "   Slower and more expensive, but superior quality",
    "",
    "Claude Sonnet — The balanced one (default model)",
    "   Excellent quality/speed ratio",
    "   Ideal for most daily uses",
    "",
    "Claude Haiku — The ultra-fast one",
    "   Near-instant responses",
    "   Ideal for simple and quick tasks",
    "",
    "All three models share: 200K token context,",
    "   image and file analysis, Claude response style",
])

table_slide(prs, "Plans and pricing",
    ["Feature", "Free", "Pro ($20/month)", "Team ($25/month/user)"],
    [
        ["Default model", "Sonnet", "Sonnet + Opus + Haiku", "Sonnet + Opus + Haiku"],
        ["Daily messages", "Limited", "5x compared to Free", "Even more"],
        ["Context", "200K tokens", "200K tokens", "200K tokens"],
        ["Artifacts", "Yes", "Yes", "Yes"],
        ["Projects", "Yes (limited)", "Yes", "Yes (shared)"],
        ["File upload", "Yes", "Yes", "Yes"],
        ["Data privacy", "Possible review", "No training", "No training"],
    ])

content_slide(prs, "The Claude.ai interface", [
    "LEFT SIDEBAR",
    "   - New chat (+ icon)",
    "   - Recent: conversation history",
    "   - Projects: your organized projects",
    "   - Star: favorite conversations",
    "",
    "CENTRAL AREA",
    "   - Clean and minimal chat",
    "   - Model selection at the top (Opus / Sonnet / Haiku)",
    "   - Attachment icon for file and image uploads",
    "   - Artifact panel on the right (when active)",
    "",
    "Cleaner and less 'cluttered' design compared to ChatGPT",
])

# ── 3. SECTION 2 — DISTINCTIVE FEATURES ──────────────
section_slide(prs, 2, "Distinctive features",
              "What makes Claude different from the rest")

highlight_slide(prs,
    "LONG CONTEXT: 200,000 TOKENS",
    "Claude can analyze in a single conversation\n"
    "approximately 500 pages of text.\n"
    "For comparison: ChatGPT Free handles about 100.",
    "Ideal for: contract analysis, long reports, manuals, complete source code.")

content_slide(prs, "Artifacts: interactive outputs", [
    "Artifacts is Claude's most innovative feature",
    "",
    "What it is: a side panel that displays INTERACTIVE outputs",
    "   - Formatted documents (Markdown)",
    "   - Code with syntax highlighting",
    "   - Interactive HTML/CSS pages",
    "   - SVG charts",
    "   - Diagrams and flowcharts",
    "   - Simple web applications (calculators, quizzes, dashboards)",
    "",
    "How to activate it:",
    "   Ask for something that lends itself to a structured output.",
    "   Claude decides on its own when to create an Artifact.",
    "   Or: 'Create an artifact with...'",
])

content_slide(prs, "Most useful Artifact types for work", [
    "DOCUMENTS: 'Create a formatted document with a table of contents for...'",
    "   Perfect for: reports, procedures, manuals, meeting minutes",
    "",
    "CALCULATORS: 'Create an interactive calculator for [formula]'",
    "   Perfect for: quotes, ROI, conversions, estimates",
    "",
    "DASHBOARDS: 'Create an HTML dashboard that visualizes this data...'",
    "   Perfect for: data visualizations, KPIs, overviews",
    "",
    "DIAGRAMS: 'Create a flowchart of the process...'",
    "   Perfect for: workflows, procedures, org charts",
    "",
    "You can download, copy or share any Artifact via link",
])

content_slide(prs, "Projects: organizing your work", [
    "Projects lets you create dedicated 'workspaces'",
    "",
    "Each project contains:",
    "   - Custom instructions (specific system prompt)",
    "   - Context documents (permanent file uploads)",
    "   - Chat history related to the project",
    "",
    "Practical example:",
    "   Project: 'Monthly Marketing Report'",
    "   Instructions: 'You are a marketing analyst. Use the data from the attached",
    "              files to respond. Format: executive summary + detail.'",
    "   Files: report template, previous month data, brand guidelines",
    "",
    "Every new chat in the project ALREADY has all the necessary context!",
])

content_slide(prs, "Document and image analysis", [
    "Upload and file analysis (like ChatGPT, but with some differences):",
    "   - PDFs, documents, spreadsheets, images, code",
    "   - The 200K token window allows for much longer documents",
    "",
    "Claude's strengths in document analysis:",
    "   - Follows instructions more faithfully",
    "   - Structures responses with greater precision",
    "   - Handles documents with complex structures better",
    "   - Cites relevant parts of the document in its responses",
    "",
    "Image analysis:",
    "   - Reads and interprets charts, tables, screenshots",
    "   - Extracts text from images (OCR)",
    "   - Does NOT generate images (unlike ChatGPT)",
])

content_slide(prs, "Claude's response style", [
    "Claude has a recognizable style that differs from ChatGPT:",
    "",
    "HONESTY: admits when it doesn't know something",
    "   'I don't have enough information to answer with certainty'",
    "",
    "STRUCTURE: very well-organized responses by default",
    "   Headers, lists, clear sections without having to ask",
    "",
    "CONCISENESS: tends to be less verbose than ChatGPT",
    "   Gets to the point without excessive preambles",
    "",
    "CAUTION: more conservative on uncertain claims",
    "   Fewer hallucinations, more disclaimers when appropriate",
    "",
    "LITERALNESS: follows prompt instructions to the letter",
    "   Respects format, length, constraints more faithfully",
])

# ── 4. SECTION 3 — CLAUDE VS CHATGPT ─────────────────
section_slide(prs, 3, "Claude vs ChatGPT",
              "It's not a competition: it's a conscious choice")

two_col_slide(prs, "Strengths compared",
    "Claude excels at", [
        "Long document analysis (200K tokens)",
        "Faithfulness to prompt instructions",
        "Artifacts: interactive and visual outputs",
        "Projects: work organization",
        "Writing quality and structure",
        "Honesty (admits when it doesn't know)",
        "Coding and logical reasoning",
    ],
    "ChatGPT excels at", [
        "Image generation (DALL-E)",
        "Integrated web browsing",
        "Vast GPT ecosystem",
        "Code Interpreter for data analysis",
        "Memory across conversations",
        "Advanced voice mode",
        "Community and online resources",
    ])

content_slide(prs, "When to choose Claude", [
    "Choose Claude when:",
    "",
    "   - You need to analyze long documents (contracts, manuals, reports)",
    "   - You need a highly structured and precise response",
    "   - You want to create interactive outputs (Artifacts)",
    "   - You work on a project with fixed context (Projects)",
    "   - You need quality in writing (tone, style, structure)",
    "   - You want honest responses ('I don't know' instead of making things up)",
    "   - You need to write or analyze complex code",
    "",
    "In summary: Claude is ideal for structured work,",
    "in-depth analysis and document production.",
])

content_slide(prs, "When to choose ChatGPT", [
    "Choose ChatGPT when:",
    "",
    "   - You need images (DALL-E)",
    "   - You need to search for up-to-date information online",
    "   - You want a specialized GPT from the community",
    "   - You need data analysis with charts (Code Interpreter)",
    "   - You want to use voice mode",
    "   - You need a general-purpose 'all-rounder' tool",
    "   - You are looking for the broadest community and resources",
    "",
    "In summary: ChatGPT is ideal for varied tasks,",
    "web search, images and general use.",
])

# ── 5. SECTION 4 — LAB 1 ─────────────────────────────
section_slide(prs, 4, "Lab 1: Long document analysis",
              "Leveraging the 200K token context window — 30 min")

content_slide(prs, "Exercise: upload and query a document", [
    "Material: a long document (10+ pages)",
    "   Suggestion: use a regulation, manual, contract or public report",
    "   (downloadable from official websites, no confidential data!)",
    "",
    "Step 1: Upload the document to claude.ai",
    "",
    "Step 2: Initial prompt:",
    "   'I have uploaded a [N]-page document about [TOPIC].",
    "    First, tell me what it is about and what its structure is",
    "    (main sections with a brief description of each).'",
    "",
    "Step 3: Let Claude analyze. Observe the quality of the summary.",
])

content_slide(prs, "Targeted questions about the document", [
    "After the initial analysis, ask progressively more specific questions:",
    "",
    "Level 1 (general understanding):",
    "   'What are the 5 most important points of this document?'",
    "",
    "Level 2 (specific search):",
    "   'What does the document say about [specific topic]?",
    "    Cite the relevant passages.'",
    "",
    "Level 3 (critical analysis):",
    "   'Are there contradictions or ambiguities in the document?",
    "    Highlight any gaps or unclear points.'",
    "",
    "Level 4 (application):",
    "   'Based on this document, create an operational checklist",
    "    of 10 points for [role/activity].'",
])

content_slide(prs, "Comparison: same document on ChatGPT", [
    "If time allows, upload the same document to ChatGPT",
    "and ask the same questions.",
    "",
    "Compare:",
    "   - Which one understood the document structure better?",
    "   - Which one answered specific questions better?",
    "   - Which one cited passages more precisely?",
    "   - Which one handled critical questions better?",
    "",
    "You will usually notice:",
    "   Claude: more precise in citations, more structured",
    "   ChatGPT: more conversational, sometimes more creative in interpretations",
])

# ── 6. SECTION 5 — LAB 2 ─────────────────────────────
section_slide(prs, 5, "Lab 2: Interactive Artifacts",
              "Creating visual and functional outputs — 30 min")

content_slide(prs, "Exercise 1: formatted document", [
    "Ask Claude:",
    "",
    "   'Create an artifact with a formatted document:",
    "    Title: Quick Guide to Using AI in Our Team",
    "    Sections: Approved Tools, Usage Rules, 5 Useful Prompts,",
    "    FAQ (5 questions). Professional format with table of contents.'",
    "",
    "Observe:",
    "   - The artifact opens in the right side panel",
    "   - You can copy, download or modify the content",
    "   - You can request changes: 'Add a section about...'",
    "",
    "Extra exercise: 'Transform this artifact into an email",
    "   to send to the team to announce these guidelines'",
])

content_slide(prs, "Exercise 2: interactive calculator", [
    "Ask Claude:",
    "",
    "   'Create an HTML artifact with an interactive calculator",
    "    for [CHOOSE ONE]:",
    "    a) Project ROI calculation",
    "    b) Service quote",
    "    c) Unit conversion",
    "    d) Deadline/timeline calculator",
    "",
    "    It should have: input fields, Calculate button,",
    "    results area with explanation. Clean and modern design.'",
    "",
    "Try using the calculator: does it work? Are the calculations correct?",
    "If something is wrong: 'The calculation for field X is incorrect,",
    "   the correct formula is [FORMULA]'",
])

content_slide(prs, "Exercise 3: data dashboard", [
    "Ask Claude:",
    "",
    "   'Create an HTML artifact with a dashboard that visualizes",
    "    this quarterly sales data:",
    "    Q1: 150K, Q2: 180K, Q3: 165K, Q4: 210K",
    "    Product A: 40%, Product B: 35%, Product C: 25%",
    "",
    "    Include: bar chart for quarters, pie chart",
    "    for products, year-over-year growth indicator,",
    "    summary table. Modern design with consistent colors.'",
    "",
    "Iterate: 'Change the colors to [palette]'",
    "         'Add a field to enter next quarter's data'",
])

# ── 7. SECTION 6 — LAB 3 ─────────────────────────────
section_slide(prs, 6, "Lab 3: Direct comparison",
              "Same task, two tools, different results — 25 min")

content_slide(prs, "Exercise: structured comparative test", [
    "Choose ONE complex task and send the SAME prompt to Claude and ChatGPT",
    "",
    "Suggested tasks:",
    "   A. 'Analyze the pros and cons of remote work for a company",
    "       of 50 people. Create a 1-page report with a recommendation.'",
    "",
    "   B. 'Write a business proposal for an AI consulting service",
    "       aimed at SMEs. Max 2 pages, professional tone.'",
    "",
    "   C. 'Create a 30-day onboarding plan for a new",
    "       employee in the marketing department. Week-by-week table.'",
    "",
    "Send the SAME prompt, word for word, to both.",
])

table_slide(prs, "Comparison sheet (fill it in!)",
    ["Criterion", "Claude", "ChatGPT", "Winner"],
    [
        ["Adherence to prompt", "", "", ""],
        ["Structure and formatting", "", "", ""],
        ["Content quality", "", "", ""],
        ["Conciseness vs verbosity", "", "", ""],
        ["Originality of ideas", "", "", ""],
        ["Factual accuracy", "", "", ""],
        ["Tone and style", "", "", ""],
    ])

# ── 8. SECTION 7 — LAB 4 ─────────────────────────────
section_slide(prs, 7, "Lab 4: Projects",
              "Organizing work with persistent context — 25 min")

content_slide(prs, "Creating a project on Claude", [
    "Step 1: In the sidebar, click '+ New project'",
    "Step 2: Name the project (e.g., 'Weekly Sales Report')",
    "Step 3: Write the custom instructions:",
    "",
    "   Example:",
    "   'You are a sales analyst for a company in [industry].",
    "    When I send you data, analyze it and create a report with:",
    "    - Performance summary (3 lines)",
    "    - Top 3 products by growth",
    "    - Warning signals",
    "    - 2 suggested actions",
    "    Format: bullet points, professional tone, max 1 page.'",
    "",
    "Step 4: Upload context files (templates, historical data, KPIs)",
])

content_slide(prs, "Working within the project context", [
    "Once configured, every new chat in the project:",
    "   - ALREADY knows the instructions and uploaded files",
    "   - You don't need to repeat the context every time",
    "   - Can reference the uploaded documents",
    "",
    "Example workflow:",
    "   Monday: 'Here is this week's data [paste]. Analyze.'",
    "   >>> Claude produces the report in the defined format",
    "",
    "   Tuesday: 'Compare with last week [paste].'",
    "   >>> Claude already knows the format and context",
    "",
    "   Friday: 'Create the weekly summary for management.'",
    "   >>> Claude knows all the week's data",
])

content_slide(prs, "Ideas for useful Projects", [
    "RECURRING REPORTS: weekly/monthly reports with a fixed format",
    "   Upload: template, target KPIs, historical data",
    "",
    "PROJECT ASSISTANT: an AI dedicated to a specific project",
    "   Upload: brief, timeline, reference documents, stakeholders",
    "",
    "KNOWLEDGE BASE: FAQ and procedures for your team",
    "   Upload: manuals, procedures, internal regulations",
    "",
    "BRAND WRITING: content consistent with the company tone",
    "   Upload: brand guidelines, communication examples, tone of voice",
    "",
    ">>> A good project is configured once and used for months!",
])

# ── 9. CLOSING ─────────────────────────────────────────
content_slide(prs, "Tips & tricks for Claude", [
    "1. USE ARTIFACTS for any structured or visual output",
    "2. PROJECTS for anything recurring (reports, analysis, writing)",
    "3. SPECIFY THE FORMAT: Claude is excellent at respecting it",
    "4. LONG DOCUMENTS: Claude is the best for contract/manual analysis",
    "5. CHOOSE THE MODEL: Haiku for quick questions, Sonnet for daily use,",
    "   Opus for complex analysis",
    "6. ASK FOR CITATIONS: 'Cite the relevant passages from the document'",
    "7. ITERATE ON ARTIFACTS: you can refine them with specific feedback",
    "8. NO IMAGE GENERATION: for visuals, create the artifact and use DALL-E for photos",
])

recap_slide(prs, [
    "Claude is built on Anthropic's 'safe AI' philosophy",
    "Three models: Opus (powerful), Sonnet (balanced), Haiku (fast)",
    "200K token context: ideal for long documents",
    "Artifacts: uniquely interactive outputs (calculators, dashboards, documents)",
    "Projects: workspaces with persistent context",
    "Claude and ChatGPT have different strengths — use both strategically",
])

next_module_slide(prs,
    "Module 5: Open Source Models\n"
    "Free and open alternatives")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_04_claude", "slides",
                   "Module_04_Claude.pptx")
salva(prs, out)
