#!/usr/bin/env python3
"""Generate slides for Module 6 — AI in everyday work: real-world use cases (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────
title_slide(prs,
    "Module 6",
    "AI in everyday work: real-world use cases",
    "AI Basics Course  |  Duration: 3 hours  |  1h Theory + 2h Workshop")

agenda_slide(prs, [
    "From learning to action: how to integrate AI into work",
    "Workflow 1: Communication — emails, reports, meeting minutes",
    "Workflow 2: Analysis — data, feedback, research",
    "Workflow 3: Productivity — automation, templates, procedures",
    "Workflow 4: Decision-making — comparisons, SWOT, scenarios",
    "Workshop: identify and automate 3 tasks from YOUR job",
    "Integration with everyday tools",
    "Recap and questions",
])

# ── 2. SECTION 1 — FROM LEARNING TO ACTION ───────────
section_slide(prs, 1, "From learning to action",
              "The real value of AI lies in everyday practice")

highlight_slide(prs,
    "THE KEY QUESTION",
    "Not 'what can AI do?'\n"
    "but 'which of MY tasks\n"
    "can it make faster or better?'",
    "The ROI of AI is measured in time saved and quality improved on YOUR real tasks.")

content_slide(prs, "How to identify 'AI-friendly' tasks", [
    "A task is ideal for AI when it is:",
    "",
    "  REPETITIVE: you do it often with minimal variations",
    "     E.g.: reply emails, weekly reports, meeting notes",
    "",
    "  TEXT-BASED: it involves reading, writing, summarizing, translating",
    "     E.g.: documentation, communication, qualitative analysis",
    "",
    "  STRUCTURABLE: the output follows a predictable pattern",
    "     E.g.: tables, lists, standard templates, procedures",
    "",
    "  LOW RISK: an error does not cause serious damage",
    "     E.g.: drafts, brainstorming, explorations (NOT final legal contracts)",
])

content_slide(prs, "The 'Before-During-After' framework", [
    "For every task, think about AI in three stages:",
    "",
    "BEFORE — Preparation and research",
    "   Gather information, analyze context, generate ideas",
    "   Example: 'Prepare a briefing on this client for me'",
    "",
    "DURING — Production and drafting",
    "   Write the first draft, structure, format",
    "   Example: 'Write the first version of this email'",
    "",
    "AFTER — Review and improvement",
    "   Correct, simplify, translate, adjust the tone",
    "   Example: 'Make this text more concise and formal'",
    "",
    ">>> AI is most useful in the BEFORE and DURING stages.",
    "    The AFTER stage remains primarily human.",
])

content_slide(prs, "The 80/20 rule with AI", [
    "AI generates 80% of the work in 20% of the time",
    "YOU add the final 20% that makes the difference:",
    "",
    "   AI generates the draft (2 minutes)",
    "   You review, personalize, verify (5 minutes)",
    "   TOTAL: 7 minutes instead of 30",
    "",
    "DO NOT delegate everything. The human added value is:",
    "   - Contextual judgment (you know your audience)",
    "   - Fact-checking (AI can make mistakes)",
    "   - Personal touch (relationships, empathy, nuance)",
    "   - Accountability (you sign off, not the AI)",
    "",
    ">>> The goal is not to eliminate work, but to eliminate tedious work.",
])

# ── 3. SECTION 2 — COMMUNICATION WORKFLOW ────────────
section_slide(prs, 2, "Workflow 1: Communication",
              "Emails, reports, minutes, and written content")

content_slide(prs, "Email: the most immediate use case", [
    "The average office worker writes 40+ emails per day.",
    "AI can cut the time for routine emails in half.",
    "",
    "AUTOMATABLE TYPES:",
    "   - Replies to standard information requests",
    "   - Confirmations, thank-yous, follow-ups",
    "   - Polite reminders",
    "   - Introduction emails and cold outreach",
    "   - Meeting summary sent to participants",
    "",
    "WORKFLOW:",
    "   1. Copy the content of the received email",
    "   2. Prompt: 'Reply to this email. Context: [X]. Tone: [Y].'",
    "   3. Review, personalize, send",
])

content_slide(prs, "Reports and documents: from draft to finished product", [
    "Weekly, monthly, quarterly reports — always the same structure:",
    "",
    "WORKFLOW WITH AI:",
    "   1. Prepare the data (numbers, KPIs, key facts)",
    "   2. Prompt: 'Write a [TYPE] report with this data: [DATA].",
    "      Structure: [SECTIONS]. Audience: [WHO]. Max [N] words.'",
    "   3. AI generates the structured draft",
    "   4. You add: interpretation, commentary, recommendations",
    "",
    "ADVANCED TIP (with Claude Projects):",
    "   Create a 'Monthly Report' project with template and instructions.",
    "   Each month, upload only the new data. Claude already knows the format.",
    "",
    "ESTIMATED SAVINGS: from 2-3 hours down to 30-45 minutes per report.",
])

content_slide(prs, "Meeting minutes: from notes to document", [
    "Problem: taking notes AND actively participating is hard.",
    "",
    "WORKFLOW:",
    "   1. During the meeting: jot down keywords and decisions",
    "      (even messy, with abbreviations, incomplete sentences)",
    "   2. After the meeting, paste your notes into ChatGPT or Claude:",
    "      'Turn these notes into professional meeting minutes.",
    "       Format: date, attendees, discussion points (numbered),",
    "       decisions made, action items (with owner and deadline).",
    "       Tone: formal and concise.'",
    "   3. Review, correct names and specific details, send",
    "",
    "Time: from 30 minutes of writing down to 5 minutes of review.",
])

content_slide(prs, "Social content and external communication", [
    "LinkedIn posts, newsletters, press releases — AI as copywriter:",
    "",
    "WORKFLOW FOR LINKEDIN POSTS:",
    "   1. Define the key message (1 sentence)",
    "   2. Prompt: 'Create 3 versions of a LinkedIn post about [TOPIC].",
    "      Target: [WHO]. Styles: storytelling, statistical fact, listicle.",
    "      100-150 words, opening hook, closing CTA, 3 hashtags.'",
    "   3. Pick the best version, personalize with your own voice",
    "",
    "WORKFLOW FOR NEWSLETTERS:",
    "   1. List the topics to cover",
    "   2. Prompt: 'Write a 500-word newsletter covering these topics: [...].",
    "      Tone: [BRAND]. Include: catchy intro, one section per topic,",
    "      closing CTA.'",
    "   3. Add links, images, review the tone",
])

# ── 4. SECTION 3 — ANALYSIS WORKFLOW ─────────────────
section_slide(prs, 3, "Workflow 2: Analysis",
              "Data, feedback, research, and synthesis")

content_slide(prs, "Data analysis without knowing how to code", [
    "With ChatGPT (Code Interpreter) anyone can analyze data:",
    "",
    "WORKFLOW:",
    "   1. Export the data to CSV or Excel",
    "   2. Upload to ChatGPT and ask:",
    "      'Analyze this dataset. Show me: main trends with charts,",
    "       anomalies, top/bottom performers. Conclude with 3 recommendations.'",
    "   3. AI writes and runs the Python code for you",
    "   4. Download the charts and results",
    "",
    "REAL-WORLD USE CASES:",
    "   - Sales: trends, period comparisons, product/region segmentation",
    "   - HR: turnover, absences, satisfaction surveys",
    "   - Marketing: campaign performance, conversion rates",
    "   - Finance: budget variances, cost analysis",
])

content_slide(prs, "Qualitative analysis: feedback and reviews", [
    "Turning unstructured text into actionable insights:",
    "",
    "WORKFLOW:",
    "   1. Collect the feedback (Google Reviews, surveys, emails, tickets)",
    "   2. Copy-paste into Claude or ChatGPT:",
    "      'Analyze these [N] pieces of feedback. For each, classify:",
    "       sentiment, topic, urgency. Then: recurring themes, pain points,",
    "       strengths, 3 priority actions.'",
    "   3. Result: structured analysis from raw text",
    "",
    "APPLICATIONS:",
    "   - NPS verbatim: understand the 'why' behind the numbers",
    "   - Complaints: categorize and prioritize",
    "   - Internal surveys: extract insights from the workforce",
    "   - Competitor reviews: understand where they excel and where they struggle",
])

content_slide(prs, "Research and meeting preparation", [
    "AI as a junior analyst who prepares briefings for you:",
    "",
    "BEFORE A MEETING WITH A CLIENT:",
    "   'Prepare a briefing on [COMPANY]. Cover: industry, size,",
    "    main products, typical industry challenges, recent news.",
    "    Then suggest 5 smart questions to ask in the meeting.'",
    "",
    "BEFORE A PRESENTATION:",
    "   'I am presenting [PROPOSAL] to [AUDIENCE]. Anticipate the 5 most",
    "    likely objections and prepare a response for each.'",
    "",
    "BEFORE A NEGOTIATION:",
    "   'Analyze the pros/cons of our position on [TOPIC].",
    "    Identify our BATNA and suggest a strategy.'",
    "",
    ">>> Note: always verify facts with independent sources!",
])

# ── 5. SECTION 4 — PRODUCTIVITY WORKFLOW ─────────────
section_slide(prs, 4, "Workflow 3: Productivity",
              "Automation, templates, and procedures")

content_slide(prs, "Reusable templates: create once, use forever", [
    "The most efficient approach: have AI create the templates for you",
    "",
    "STEP 1: Identify a repetitive task (email, report, checklist)",
    "STEP 2: Ask AI to create the template:",
    "   'Create a template for [TYPE] with placeholders [NAME], [DATE],",
    "    [DETAIL]. Include 3 variants for different contexts.'",
    "STEP 3: Save the template in your personal archive",
    "STEP 4: Every time you need it, just fill in the placeholders",
    "",
    "EXAMPLES OF USEFUL TEMPLATES:",
    "   - 5 email templates (confirmation, reminder, thank-you, etc.)",
    "   - Weekly/monthly report template",
    "   - Project kickoff checklist",
    "   - Script for sales calls",
])

content_slide(prs, "Standard Operating Procedures (SOPs) with AI", [
    "Documenting processes is often neglected but essential:",
    "",
    "WORKFLOW:",
    "   1. Describe the process verbally (even informally)",
    "   2. Prompt: 'Turn this description into a formal SOP.",
    "      Structure: purpose, who executes it, prerequisites, step-by-step",
    "      procedure (numbered), success criteria, troubleshooting.'",
    "   3. Review with the person who actually performs the process",
    "   4. Publish and distribute",
    "",
    "BENEFIT: knowledge does not stay locked in one person's head.",
    "If a colleague goes on vacation, the SOP has you covered.",
    "",
    ">>> Claude Projects is ideal: create a 'Company SOPs' project",
    "    and update procedures over time.",
])

content_slide(prs, "Everyday translation and localization", [
    "Beyond Google Translate: translations adapted to context:",
    "",
    "DOCUMENT TRANSLATION:",
    "   'Translate this document into English. Do not translate literally:",
    "    adapt the tone for the international market. Flag any significant",
    "    adaptation choices.'",
    "",
    "MARKETING LOCALIZATION:",
    "   'Adapt this promotional text for the German market.",
    "    Consider cultural differences and communication preferences.'",
    "",
    "MULTILINGUAL SUPPORT:",
    "   'I received this email in [LANGUAGE]. Translate it and suggest",
    "    an appropriate reply in the same language.'",
    "",
    ">>> AI handles 20+ languages well. For critical translations",
    "    (legal, medical), always have a professional validate.",
])

content_slide(prs, "Training and onboarding with AI", [
    "Creating training material becomes incredibly fast:",
    "",
    "QUIZZES AND ASSESSMENTS:",
    "   'Create a 10-question quiz on [TOPIC]. Mix of multiple",
    "    choice and true/false. Level: [BEGINNER/ADVANCED].",
    "    Answers at the end with explanations.'",
    "",
    "NEW HIRE GUIDES:",
    "   'Create an onboarding guide for a new [ROLE].",
    "    30-day plan: week by week with activities,",
    "    goals, people to meet, resources to read.'",
    "",
    "INTERNAL FAQS:",
    "   'Based on these frequently asked questions [LIST], create a",
    "    structured FAQ document with clear, concise answers.'",
    "",
    ">>> Perfect for growing teams that need to scale quickly.",
])

# ── 6. SECTION 5 — DECISION-MAKING WORKFLOW ──────────
section_slide(prs, 5, "Workflow 4: Decision support",
              "Comparisons, scenarios, and strategic analysis")

content_slide(prs, "AI-assisted decision matrix", [
    "When you have to choose among multiple options:",
    "",
    "WORKFLOW:",
    "   1. Define the options and evaluation criteria",
    "   2. Prompt: 'Compare Option A [DESC] and Option B [DESC].",
    "      Criteria: cost (weight 3), quality (weight 5), time (weight 4),",
    "      scalability (weight 2). Matrix 1-5 per criterion, weighted score,",
    "      reasoned recommendation.'",
    "   3. AI structures the reasoning that you then validate",
    "",
    "AI DOES NOT decide for you. AI helps you to:",
    "   - Structure criteria that would otherwise remain implicit",
    "   - Not forget important aspects",
    "   - Visualize the comparison objectively",
    "   - Document the decision-making process",
])

content_slide(prs, "'What if' scenario analysis", [
    "Exploring future scenarios before making a decision:",
    "",
    "SAMPLE PROMPT:",
    "   'We are a [INDUSTRY] company with [N] employees.",
    "    We are considering [DECISION].",
    "    Analyze 3 scenarios:",
    "    - Optimistic scenario: what happens if everything goes well",
    "    - Realistic scenario: the most likely outcome",
    "    - Pessimistic scenario: what happens if things go wrong",
    "    For each scenario: estimated probability, revenue impact,",
    "    team impact, mitigation actions.'",
    "",
    "APPLICATIONS: product launch, hiring, market entry,",
    "    vendor change, technology investment.",
])

content_slide(prs, "SWOT and rapid strategic analysis", [
    "AI as a 'pocket strategy consultant':",
    "",
    "SWOT ANALYSIS:",
    "   'Create a SWOT analysis for [COMPANY/PROJECT].",
    "    Context: [INDUSTRY, MARKET]. 5 points per quadrant,",
    "    with a brief explanation. Conclude with 3 recommendations.'",
    "",
    "COMPETITIVE ANALYSIS:",
    "   'Compare our offering with competitors [A, B, C].",
    "    Criteria: price, quality, service, innovation.",
    "    Identify our competitive advantage and 2 vulnerabilities.'",
    "",
    "RISK ANALYSIS:",
    "   'Identify the 5 main risks for [PROJECT/INITIATIVE].",
    "    For each: probability, impact, mitigation action.",
    "    Format: risk matrix.'",
])

# ── 7. SECTION 6 — WORKSHOP ──────────────────────────
section_slide(prs, 6, "Workshop: automate YOUR work",
              "Identify and automate 3 real tasks — 60 min")

content_slide(prs, "Step 1: Identify your 'time wasters' (10 min)", [
    "Think about your typical work week.",
    "Which repetitive activities take up the most time?",
    "",
    "Fill in this list (at least 5 activities):",
    "   1. __________________________________ (~___ min/week)",
    "   2. __________________________________ (~___ min/week)",
    "   3. __________________________________ (~___ min/week)",
    "   4. __________________________________ (~___ min/week)",
    "   5. __________________________________ (~___ min/week)",
    "",
    "Now select the 3 best suited for AI (repetitive + text-based + low risk)",
    "and mark an asterisk (*) next to them.",
])

content_slide(prs, "Step 2: Design the AI workflow (15 min)", [
    "For each of the 3 selected tasks, define:",
    "",
    "TASK 1: ___________________________",
    "   Which tool? (ChatGPT / Claude / other): _______________",
    "   Input: what do you need to provide to AI? _______________",
    "   Prompt: how would you ask? _______________",
    "   Expected output: what do you want to get? _______________",
    "   Estimated time WITH AI: ___ min (vs ___ min without AI)",
    "",
    "Repeat for Task 2 and Task 3.",
    "",
    "Tip: start with the simplest task,",
    "so you build confidence in the process.",
])

content_slide(prs, "Step 3: Test it live (25 min)", [
    "Now ACTUALLY TRY your 3 workflows with AI!",
    "",
    "For each task:",
    "   1. Open the tool you chose",
    "   2. Write the prompt you designed",
    "   3. Evaluate the result: is it usable?",
    "   4. If not, iterate and improve the prompt",
    "   5. When satisfied, SAVE the prompt for reuse",
    "",
    "While working, take note of:",
    "   - What worked right away",
    "   - What required iteration",
    "   - What did not work (and why)",
    "",
    ">>> The prompt that works is your new 'work tool'.",
    "    Save it where you can find it (notes, document, Claude Project).",
])

content_slide(prs, "Step 4: Share with the group (10 min)", [
    "Each participant briefly presents:",
    "",
    "   1. Which task you automated",
    "   2. Which tool you used",
    "   3. The prompt that worked best",
    "   4. How much time you save",
    "   5. One thing that surprised you",
    "",
    "RULE: listen to others' prompts!",
    "   Often the best workflow comes from",
    "   adapting a colleague's idea to your own context.",
    "",
    ">>> At the end of the session, the trainer collects the best prompts",
    "    and shares them with the whole group as a 'starter library'.",
])

# ── 8. SECTION 7 — TOOL INTEGRATION ──────────────────
section_slide(prs, 7, "Integration with work tools",
              "How AI fits into your ecosystem")

two_col_slide(prs, "AI in the Microsoft 365 ecosystem",
    "Microsoft Copilot", [
        "Integrated in Word, Excel, PowerPoint, Outlook",
        "Summarize emails and Teams conversations",
        "Generate document drafts in Word",
        "Create presentations from a brief",
        "Analyze data in Excel with natural language",
        "Requires Copilot Pro/Business license",
    ],
    "How to use it today (without Copilot)", [
        "Copy text from Word to ChatGPT/Claude",
        "Export Excel data to CSV, analyze with AI",
        "Generate slide structure, then build in PPT",
        "Use AI for drafts, Office for formatting",
        "The manual workflow works perfectly well!",
        "Copilot just makes it more seamless",
    ])

two_col_slide(prs, "AI in the Google Workspace ecosystem",
    "Google Gemini in Workspace", [
        "Integrated in Gmail, Docs, Sheets, Slides",
        "'Help me write' in Gmail and Docs",
        "AI formulas in Sheets",
        "Slide generation from prompt",
        "Long email summarization",
        "Available with Business/Enterprise plans",
    ],
    "How to use it today (without Gemini)", [
        "Copy from Docs to ChatGPT/Claude",
        "Export Sheets to CSV, analyze with AI",
        "Use Google AI Studio for Gemini for free",
        "Paste the result into your documents",
        "Copy-paste remains the universal method",
        "",
    ])

content_slide(prs, "The 'copy-paste' approach works (and works well)", [
    "No need to wait for native integrations.",
    "The universal workflow is:",
    "",
    "   1. COPY the content from your work tool",
    "   2. PASTE into ChatGPT/Claude with a targeted prompt",
    "   3. REVIEW the output",
    "   4. COPY the result and PASTE into your work tool",
    "",
    "Is it 'primitive'? Yes. Does it work? Absolutely.",
    "",
    "Advantages of copy-paste over native integrations:",
    "   - Works with ANY tool",
    "   - You have full control over the prompt and the result",
    "   - No additional licenses required",
    "   - You can choose the best model for each task",
])

# ── 9. CLOSING ─────────────────────────────────────────
recap_slide(prs, [
    "Look for 'AI-friendly' tasks: repetitive, text-based, structurable, low risk",
    "Before-During-After framework: AI helps most in preparation and drafting",
    "80/20 rule: AI does 80%, you add the 20% that makes the difference",
    "Communication, analysis, productivity, decisions: 4 high-impact areas",
    "Save the prompts that work: they become your work tools",
    "Copy-paste is the universal workflow: no need to wait for native integrations",
])

next_module_slide(prs,
    "Module 7: Responsible AI\n"
    "(already completed)\n\n"
    "Module 8: Final Project")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_06_use_cases", "slides",
                   "Module_06_Use_Cases.pptx")
salva(prs, out)
