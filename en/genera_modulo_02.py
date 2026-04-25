#!/usr/bin/env python3
"""Generate slides for Module 2 — Prompt Engineering (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────────
title_slide(prs,
    "Module 2",
    "Prompt Engineering: the art of asking well",
    "AI Basics Course  |  Duration: 3 hours  |  1h Theory + 2h Lab")

agenda_slide(prs, [
    "What is Prompt Engineering and why it matters",
    "Anatomy of a good prompt",
    "Fundamental techniques: zero-shot, few-shot, chain-of-thought, role-playing",
    "Lab 1: turning vague prompts into effective prompts",
    "Lab 2: real-world work scenarios (8 exercises)",
    "Lab 3: comparing tools",
    "Common mistakes and how to avoid them",
    "Recap and Q&A",
])

# ── 2. SECTION 1 — WHAT IS PROMPT ENGINEERING ─────────────
section_slide(prs, 1, "What Is Prompt Engineering",
              "The most important skill of the AI era")

highlight_slide(prs,
    "DEFINITION",
    "Prompt Engineering is the art of crafting\n"
    "effective instructions to get exactly\n"
    "the desired result from AI.",
    "You don't need to know how to code. You need to know how to communicate with precision.")

content_slide(prs, "Why Prompt Engineering is so important", [
    "The SAME tool can deliver terrible or excellent results",
    "The difference is not the model, but HOW you talk to it",
    "",
    "Vague prompt: 'Write something about marketing'",
    "   >>> Generic, unusable result",
    "",
    "Effective prompt: 'Write 5 ideas for a social media campaign",
    "   for an Italian restaurant in Milan, target audience 25-40,",
    "   limited budget, informal and engaging tone'",
    "   >>> Specific, actionable, useful result",
])

content_slide(prs, "The prompt as an interface", [
    "The prompt is your ONLY interface with the AI model",
    "You cannot 'show' what you want — you must DESCRIBE it in words",
    "",
    "Think of the prompt as a brief for a colleague:",
    "   - Who is the audience?",
    "   - What is the objective?",
    "   - What format do you want?",
    "   - What tone should be used?",
    "   - Are there specific constraints or requirements?",
    "",
    "The more context you provide, the better the result.",
])

content_slide(prs, "Anatomy of a good prompt", [
    "An effective prompt has up to 6 components:",
    "",
    "1. ROLE — Who the AI should be (e.g., 'You are a marketing expert')",
    "2. CONTEXT — Relevant background information",
    "3. TASK — What it should do, in specific terms",
    "4. FORMAT — How you want the output (list, table, email, etc.)",
    "5. TONE — Formal, informal, technical, accessible",
    "6. CONSTRAINTS — Length, language, things to avoid",
    "",
    "You don't always need all six, but the more you use, the better the result.",
])

# ── 3. SECTION 2 — FUNDAMENTAL TECHNIQUES ─────────────────
section_slide(prs, 2, "Fundamental techniques",
              "The prompt engineer's toolkit")

two_col_slide(prs, "Technique 1: Zero-shot",
    "What it is", [
        "Giving a direct instruction",
        "WITHOUT providing examples",
        "The model uses only its own knowledge",
        "The simplest and most immediate technique",
    ],
    "Example", [
        "Prompt:",
        "'Translate to French: Good morning,",
        "how can I help you?'",
        "",
        "When to use it:",
        "For simple, well-defined tasks",
    ])

two_col_slide(prs, "Technique 2: Few-shot (with examples)",
    "What it is", [
        "Providing 2-3 EXAMPLES of input/output",
        "The model learns the pattern from examples",
        "Much more precise than zero-shot",
        "Ideal for tasks with a specific format",
    ],
    "Example", [
        "Prompt:",
        "'Classify the sentiment: ",
        "  Great product! -> Positive",
        "  Terrible experience -> Negative",
        "  The package arrived -> Neutral",
        "  Fantastic customer service -> ?'",
    ])

two_col_slide(prs, "Technique 3: Chain-of-Thought (step-by-step reasoning)",
    "What it is", [
        "Asking the AI to reason STEP BY STEP",
        "Improves quality on complex problems",
        "The model 'shows its work'",
        "Reduces reasoning errors",
    ],
    "Example", [
        "Prompt:",
        "'A store sells t-shirts for $25.",
        "20% discount + $5 shipping.",
        "How much does the customer pay?",
        "Reason step by step.'",
    ])

two_col_slide(prs, "Technique 4: Role-playing",
    "What it is", [
        "Assigning a SPECIFIC ROLE to the AI",
        "The model adapts its language and expertise",
        "One of the most powerful and simple tricks",
        "Drastically changes the quality of the output",
    ],
    "Example", [
        "Prompt:",
        "'You are a sports nutritionist with 20 years",
        "of experience. An amateur athlete asks you",
        "for a meal plan for the week before",
        "a marathon. Respond clearly",
        "and practically.'",
    ])

content_slide(prs, "Technique 5: Structured output", [
    "Explicitly request a SPECIFIC FORMAT for the response",
    "",
    "Useful formats:",
    "   - Bulleted or numbered list",
    "   - Table (with specific columns)",
    "   - JSON or CSV (for data)",
    "   - Pre-formatted email",
    "   - Outline with headings and subheadings",
    "",
    "Example: 'Create a table with 3 columns: Tool, Pros, Cons.",
    "   Compare ChatGPT, Claude and Gemini for office use.'",
])

content_slide(prs, "Technique 6: Task decomposition", [
    "Breaking a COMPLEX task into simpler sub-tasks",
    "",
    "INSTEAD OF: 'Write my entire business plan for a restaurant'",
    "",
    "BETTER:",
    "   1. 'Analyze the restaurant market in Milan'",
    "   2. 'Define the target clientele for a Japanese restaurant'",
    "   3. 'Estimate startup costs for a 40-seat venue'",
    "   4. 'Write the executive summary based on this information'",
    "",
    "Each sub-task receives more attention and produces better results.",
])

content_slide(prs, "Technique 7: Constraints and delimitation", [
    "Adding EXPLICIT constraints to control the output",
    "",
    "Length constraints: 'Respond in 100 words or fewer'",
    "Language constraints: 'Respond in formal English'",
    "Content constraints: 'Do not use technical jargon'",
    "Exclusion constraints: 'Do not mention competitors'",
    "Audience constraints: 'Write for a non-technical audience'",
    "",
    "Without constraints, the model decides on its own and is often too long",
    "and generic. Constraints are your steering wheel.",
])

content_slide(prs, "Iteration and refinement", [
    "The first prompt is rarely the perfect one",
    "",
    "Iterative process:",
    "   1. Write the initial prompt",
    "   2. Read the response with a critical eye",
    "   3. Identify what is missing or what went wrong",
    "   4. REFINE the prompt by adding context/constraints",
    "   5. Repeat until you get the desired result",
    "",
    "It is a CONVERSATION, not a one-off command!",
    "Use phrases like: 'Good, but now make the tone more informal'",
    "or: 'Great, also add a section on risks'",
])

content_slide(prs, "Common prompting mistakes", [
    "1. TOO VAGUE: 'Tell me something about AI'",
    "   >>> Add context and a specific objective",
    "",
    "2. TOO LONG: a 500-word prompt with irrelevant information",
    "   >>> Be concise yet complete",
    "",
    "3. UNREALISTIC EXPECTATIONS: 'Write my entire book'",
    "   >>> Break it down into manageable sub-tasks",
    "",
    "4. NO FORMAT: not specifying how you want the response",
    "   >>> Always indicate the desired format",
    "",
    "5. NOT ITERATING: accepting the first response without refining",
    "   >>> The perfect prompt usually takes 2-3 attempts",
])

table_slide(prs, "Techniques summary",
    ["Technique", "When to use it", "Level"],
    [
        ["Zero-shot", "Simple, straightforward tasks", "Basic"],
        ["Few-shot", "A specific format/pattern is needed", "Basic"],
        ["Chain-of-thought", "Reasoning, calculations, analysis", "Intermediate"],
        ["Role-playing", "Domain expertise is needed", "Basic"],
        ["Structured output", "A precise format is needed", "Basic"],
        ["Decomposition", "Complex tasks", "Intermediate"],
        ["Constraints", "Controlling length/tone/style", "Basic"],
        ["Iteration", "Always! After every response", "Basic"],
    ])

# ── 4. SECTION 3 — LAB 1 ─────────────────────────────────
section_slide(prs, 3, "Lab 1: From vague prompts to effective prompts",
              "Hands-on exercise — 30 minutes")

two_col_slide(prs, "Exercise 1: Professional email",
    "VAGUE prompt", [
        "'Write an email to the boss'",
        "",
        "Problems:",
        "- No context",
        "- No objective",
        "- No tone",
        "- Which boss? To say what?",
    ],
    "EFFECTIVE prompt", [
        "'Write a formal email to my",
        "department head to request",
        "3 days off from July 15 to 17.",
        "Mention that project X will be",
        "completed by the 14th. Professional",
        "tone, max 150 words.'",
    ])

two_col_slide(prs, "Exercise 2: Document summary",
    "VAGUE prompt", [
        "'Summarize this text'",
        "",
        "Problems:",
        "- How long should it be?",
        "- Who is the summary for?",
        "- Which aspects to highlight?",
        "- What format to use?",
    ],
    "EFFECTIVE prompt", [
        "'Summarize the document in 5 key",
        "points, each 1-2 sentences.",
        "The summary is for the sales",
        "director who needs to make a",
        "decision. Highlight costs, timelines",
        "and main risks. Conclude with a",
        "recommendation.'",
    ])

two_col_slide(prs, "Exercise 3: Data analysis",
    "VAGUE prompt", [
        "'Analyze this sales data'",
        "",
        "Problems:",
        "- What type of analysis?",
        "- Which metrics matter?",
        "- What comparisons to make?",
        "- How to present the results?",
    ],
    "EFFECTIVE prompt", [
        "'Analyze the attached sales data.",
        "Identify: (1) the 3 products with",
        "the highest growth, (2) the month",
        "with the most significant decline,",
        "(3) year-over-year trends. Present",
        "results in a table and conclude",
        "with 3 suggested actions.'",
    ])

content_slide(prs, "Your turn: practice!", [
    "Open ChatGPT or Claude and try:",
    "",
    "1. Write a VAGUE prompt for a task of your choice",
    "2. Observe the response: what is missing? What went wrong?",
    "3. Rewrite the prompt using the techniques you have learned:",
    "   - Add a ROLE",
    "   - Specify the CONTEXT",
    "   - Define the output FORMAT",
    "   - Add CONSTRAINTS",
    "4. Compare the two responses",
    "",
    ">>> Time: 10 minutes. Then we share the results!",
])

# ── 5. SECTION 4 — LAB 2 ─────────────────────────────────
section_slide(prs, 4, "Lab 2: Real-world work scenarios",
              "8 practical scenarios from the workplace — 45 minutes")

content_slide(prs, "Scenario 1: Brainstorming for a project", [
    "Context: You need to propose innovative ideas for the next quarter",
    "",
    "Suggested prompt:",
    "'You are a strategic consultant. My company sells business management",
    "software for small and medium-sized enterprises. Revenue has been",
    "stagnant for 2 quarters. Generate 10 creative ideas to increase",
    "sales in Q3, considering a limited budget and a team of 5 people.",
    "For each idea, indicate: action, estimated cost (low/medium/high),",
    "expected impact (1-5), implementation timeline.'",
    "",
    ">>> Try it on ChatGPT and Claude: which gives you better ideas?",
])

content_slide(prs, "Scenario 2: Writing a report", [
    "Context: You need to write a monthly report for management",
    "",
    "Suggested prompt:",
    "'Write a 1-page executive report on June results.",
    "Data: sales +12%, new clients 45, churn 3%, NPS 72.",
    "Structure: Summary (3 lines), Key results (table),",
    "Issues (list), Actions for next month (3 points).",
    "Professional tone, numbers highlighted, ready for the CEO.'",
    "",
    ">>> Tip: paste real data (non-sensitive) for better results",
])

content_slide(prs, "Scenario 3: Translation and localization", [
    "Context: You need to translate marketing content for a foreign market",
    "",
    "Suggested prompt:",
    "'Translate the following text from English to French.",
    "Do not do a literal translation: adapt the tone to the French market.",
    "Maintain a professional but accessible register.",
    "If there are cultural references, adapt them to the French context.",
    "After the translation, flag any passages where you made",
    "significant adaptation choices and explain why.'",
    "",
    ">>> The prompt 'adapt, don't translate' makes all the difference!",
])

content_slide(prs, "Scenario 4: Decision support", [
    "Context: You need to choose between two vendors / options / strategies",
    "",
    "Suggested prompt:",
    "'Help me decide between option A and option B for [decision].",
    "Option A: [description]. Option B: [description].",
    "My criteria: cost, quality, delivery time, scalability.",
    "Create a weighted decision matrix (table) with a score of 1-5",
    "for each criterion. Conclude with a reasoned recommendation.'",
    "",
    ">>> AI does not decide for you, but it structures the reasoning!",
])

content_slide(prs, "Scenario 5: Preparing a presentation", [
    "Context: You need to create a presentation for an internal meeting",
    "",
    "Suggested prompt:",
    "'Create the structure of a 10-slide presentation on [topic].",
    "Audience: non-technical executives. Duration: 15 minutes.",
    "For each slide, indicate: title, 3-4 bullet points with the content,",
    "suggestion for a visual element (chart, icon, image).",
    "The first slide is the title, the last is 'Next Steps'.",
    "Tone: clear, results-oriented, with data where possible.'",
])

content_slide(prs, "Scenario 6: Social media and communication", [
    "Context: You need to create content for corporate social media",
    "",
    "Suggested prompt:",
    "'You are a social media manager for a company in [industry].",
    "Create 5 LinkedIn posts on the topic of [subject].",
    "Each post should: be 100-150 words, have an engaging opening hook,",
    "include a final call-to-action,",
    "use 3-5 relevant hashtags. Alternate formats: plain text,",
    "bulleted list, open question, storytelling, statistical fact.'",
    "",
    ">>> Ask for variations until you find the right tone for your brand",
])

content_slide(prs, "Scenario 7: Customer feedback analysis", [
    "Context: You have collected reviews/feedback and need to analyze them",
    "",
    "Suggested prompt:",
    "'Analyze the following customer feedback [paste feedback].",
    "For each one, classify: sentiment (positive/negative/neutral),",
    "main topic (product/service/price/support),",
    "urgency (high/medium/low).",
    "Then create a summary with: recurring themes, critical points,",
    "prioritized improvement suggestions, an estimated overall",
    "satisfaction score.'",
    "",
    ">>> Perfect for turning qualitative data into actionable insights",
])

content_slide(prs, "Scenario 8: Automating email responses", [
    "Context: You need to reply to repetitive emails (info requests, confirmations...)",
    "",
    "Suggested prompt:",
    "'Create 5 email response templates for the most common requests:",
    "1. Request for information about our services",
    "2. Appointment confirmation",
    "3. Payment reminder (polite tone)",
    "4. Post-meeting thank you",
    "5. Response to a complaint",
    "For each template: subject line, body (max 100 words), professional",
    "yet friendly tone. Include placeholders [NAME], [DATE], [DETAIL].'",
])

# ── 6. SECTION 5 — LAB 3 ─────────────────────────────────
section_slide(prs, 5, "Lab 3: Comparing tools",
              "Same prompt, different responses — 30 minutes")

content_slide(prs, "Exercise: identical prompt on 3 tools", [
    "Choose ONE of the scenarios from Lab 2",
    "Send the SAME prompt to ChatGPT, Claude and HuggingChat",
    "",
    "Evaluate each response on these criteria (1-5):",
    "   - Relevance: does it answer what you asked?",
    "   - Completeness: does it cover all requested points?",
    "   - Format: does it follow the requested structure?",
    "   - Quality: clear language, useful content?",
    "   - Originality: interesting ideas or generic response?",
    "",
    "Fill in the comparison table in the exercise sheet",
])

table_slide(prs, "Comparison template (fill it in yourself!)",
    ["Criterion", "ChatGPT (1-5)", "Claude (1-5)", "HuggingChat (1-5)"],
    [
        ["Relevance", "", "", ""],
        ["Completeness", "", "", ""],
        ["Format", "", "", ""],
        ["Quality", "", "", ""],
        ["Originality", "", "", ""],
        ["TOTAL", "", "", ""],
    ])

content_slide(prs, "When to use which tool?", [
    "There is no tool that is 'the best overall' — it depends on the task:",
    "",
    "ChatGPT excels at: general use, web browsing, image generation,",
    "   large plugin ecosystem, huge community",
    "",
    "Claude excels at: analyzing long documents, writing quality,",
    "   instruction following, structured reasoning",
    "",
    "HuggingChat excels at: unlimited free access, experimenting",
    "   with different models, privacy (can work without login)",
    "",
    ">>> The expert prompt engineer knows how to choose the right tool!",
])

# ── 7. CLOSING ─────────────────────────────────────────────
recap_slide(prs, [
    "A good prompt has: role, context, task, format, tone, constraints",
    "Key techniques: zero-shot, few-shot, chain-of-thought, role-playing",
    "Structured output and constraints are your best allies",
    "Iterating and refining is normal and necessary",
    "Each tool has different strengths — choose based on the task",
    "Consistent practice is the only way to improve",
])

next_module_slide(prs,
    "Module 3: ChatGPT\n"
    "Mastering the most widely used tool")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_02_prompt_engineering", "slides",
                   "Module_02_Prompt_Engineering.pptx")
salva(prs, out)
