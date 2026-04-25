#!/usr/bin/env python3
"""Generate slides for Module 3 — ChatGPT: mastering the most popular tool (3h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────
title_slide(prs,
    "Module 3",
    "ChatGPT: mastering the most popular tool",
    "AI Basics Course  |  Duration: 3 hours  |  0.5h Theory + 2.5h Lab")

agenda_slide(prs, [
    "OpenAI and ChatGPT: overview, models and plans",
    "The interface: finding your way around ChatGPT",
    "Core features: files, web, images, data analysis",
    "GPTs: creating custom assistants",
    "Lab 1: executive summary from a document",
    "Lab 2: data analysis with Code Interpreter",
    "Lab 3: image generation with DALL-E",
    "Lab 4: creating your first custom GPT",
])

# ── 2. SECTION 1 — OVERVIEW ──────────────────────────
section_slide(prs, 1, "ChatGPT Overview",
              "The company, the models and the available plans")

content_slide(prs, "OpenAI and the birth of ChatGPT", [
    "OpenAI founded in 2015 (Altman, Musk, Sutskever and others)",
    "Mission: develop safe and beneficial AI for humanity",
    "",
    "Key timeline:",
    "   2020 — GPT-3: first model to show surprising capabilities",
    "   Nov 2022 — ChatGPT launch: 1 million users in 5 days",
    "   Mar 2023 — GPT-4: a massive qualitative leap",
    "   May 2024 — GPT-4o: multimodal model (text, voice, vision)",
    "   2025 — GPT-4.5 and reasoning models (o3)",
    "",
    "Today ChatGPT has over 200 million weekly active users",
])

content_slide(prs, "Available models", [
    "GPT-4o ('omni') — The main model",
    "   Multimodal: text, images, audio, video",
    "   Fast and capable, ideal for most tasks",
    "",
    "GPT-4o mini — Lightweight and ultra-fast version",
    "   Less powerful but very fast and cost-effective",
    "   Used by default on the Free plan",
    "",
    "o3 / o3-mini — Reasoning models",
    "   'Think' before responding (internal chain-of-thought)",
    "   Excellent for math, logic, programming",
    "   Slower but more accurate on complex problems",
])

table_slide(prs, "Plans and pricing",
    ["Feature", "Free", "Plus ($20/month)", "Team ($25/month/user)"],
    [
        ["Base model", "GPT-4o mini", "GPT-4o + o3", "GPT-4o + o3"],
        ["GPT-4o messages", "Limited", "Much more", "Much more"],
        ["DALL-E (images)", "Limited", "Yes", "Yes"],
        ["File upload", "Yes", "Yes", "Yes"],
        ["Web browsing", "Yes", "Yes", "Yes"],
        ["Custom GPTs", "Use only", "Create + use", "Create + use"],
        ["Code Interpreter", "Limited", "Yes", "Yes"],
        ["Data privacy", "Used for training", "Used for training", "Not used"],
    ])

content_slide(prs, "The interface: where to find everything", [
    "LEFT SIDEBAR",
    "   - New chat (+)",
    "   - Conversation history (searchable)",
    "   - Your favorite GPTs",
    "",
    "CENTRAL AREA",
    "   - Input field (prompt) at the bottom",
    "   - Model selection at the top",
    "   - Attachment icon: upload files, photos, documents",
    "",
    "SETTINGS (profile icon, bottom left)",
    "   - Personalization: custom instructions",
    "   - Data controls: training opt-out",
    "   - Light/dark theme",
])

# ── 3. SECTION 2 — CORE FEATURES ─────────────────────
section_slide(prs, 2, "Core features",
              "Everything ChatGPT can do (and how to do it well)")

content_slide(prs, "Chat: conversation and history", [
    "Each conversation is a separate 'chat' with its own context",
    "",
    "Chat best practices:",
    "   - ONE chat per TOPIC (don't mix different subjects)",
    "   - Give descriptive names to important chats",
    "   - Use 'New chat' when you switch topics",
    "   - Context accumulates: long chats lose focus",
    "",
    "Useful commands in chat:",
    "   - 'Let's start over with this approach...'",
    "   - 'Fix only point 3, the rest is fine'",
    "   - 'Rewrite shorter / more detailed / in a different tone'",
])

content_slide(prs, "File upload: document analysis", [
    "You can upload directly into the chat:",
    "   PDF, Word, Excel, PowerPoint, images, CSV, source code",
    "",
    "What it can do with files:",
    "   - Summarize long documents",
    "   - Answer questions about the content",
    "   - Extract specific data",
    "   - Translate entire documents",
    "   - Compare multiple documents with each other",
    "",
    "Limitations:",
    "   - Max ~50 pages per file (better results with shorter files)",
    "   - Does not handle complex tables in scanned PDFs well",
    "   - Remember: files are sent to OpenAI's servers!",
])

content_slide(prs, "Web browsing", [
    "ChatGPT can search for up-to-date information on the Internet",
    "",
    "When it activates automatically:",
    "   - Questions about recent events, news, current prices",
    "   - Explicit requests: 'Search online...'",
    "",
    "How to use it effectively:",
    "   - 'Search for the latest statistics on [topic] and cite your sources'",
    "   - 'Compare current prices of [product] across different sites'",
    "   - 'What is the latest version of [software]?'",
    "",
    "Caution:",
    "   - It doesn't always trigger a search (sometimes it answers from memory)",
    "   - Cited sources should still be verified",
])

content_slide(prs, "DALL-E: image generation", [
    "ChatGPT integrates DALL-E 3 to generate images from text",
    "",
    "What you can create:",
    "   - Illustrations for presentations and documents",
    "   - Mockups and visual concepts",
    "   - Simple infographics",
    "   - Logos and icons (as a starting point)",
    "",
    "How to write a good image prompt:",
    "   1. Describe the SUBJECT in detail",
    "   2. Specify the STYLE (photographic, illustration, flat design...)",
    "   3. Indicate COLORS and MOOD",
    "   4. Define the FORMAT (landscape, portrait, square)",
    "",
    "Limitation: it does not render text well in images",
])

content_slide(prs, "Code Interpreter: data analysis", [
    "ChatGPT can run Python code safely and analyze data",
    "",
    "What you can do:",
    "   - Upload a CSV/Excel and get automatic analysis",
    "   - Create professional charts and visualizations",
    "   - Clean and transform data",
    "   - Statistical calculations and simple forecasts",
    "   - Download results as files",
    "",
    "How to use it:",
    "   1. Upload the data file into the chat",
    "   2. Ask: 'Analyze this dataset, show me the main trends",
    "      with charts. Highlight anomalies.'",
    "   3. Iterate: 'Now create a bar chart for [column]'",
])

content_slide(prs, "Canvas: collaborative editing", [
    "Side-by-side working mode for text and code",
    "",
    "How it works:",
    "   - A side panel opens with the document",
    "   - You can select portions of text and request targeted edits",
    "   - The AI modifies only the selected part, it doesn't rewrite everything",
    "",
    "When to use Canvas:",
    "   - Writing and revising long texts (articles, reports)",
    "   - Collaborative editing with AI",
    "   - When you want to review changes step by step",
    "",
    "How to activate it: 'Use canvas to write...'",
    "   or it activates automatically for longer texts",
])

content_slide(prs, "Memory and custom instructions", [
    "MEMORY:",
    "   - ChatGPT can remember information across different conversations",
    "   - 'Remember that I work in the pharmaceutical industry'",
    "   - 'Remember that I prefer short answers in English'",
    "   - Manageable: Settings > Personalization > Memory",
    "",
    "CUSTOM INSTRUCTIONS:",
    "   - Permanent instructions applied to EVERY chat",
    "   - Two fields: 'What would you like ChatGPT to know about you?'",
    "                'How would you like ChatGPT to respond?'",
    "",
    "Example of a custom instruction:",
    "   'I am a project manager at an IT company. Always respond",
    "    in English, concisely. Use bullet points.'",
])

# ── 4. SECTION 3 — GPTs ──────────────────────────────
section_slide(prs, 3, "GPTs: custom assistants",
              "Creating and using specialized chatbots")

highlight_slide(prs,
    "WHAT ARE GPTs?",
    "Customized versions of ChatGPT,\n"
    "configured for specific tasks\n"
    "with dedicated instructions, knowledge and tools.",
    "How to create a virtual colleague specialized in your area of work.")

content_slide(prs, "GPT Store: the most useful for work", [
    "The GPT Store contains thousands of GPTs created by the community",
    "",
    "Useful categories for work:",
    "   WRITING: Copywriter, Email Assistant, Resume Builder",
    "   PRODUCTIVITY: Notion Helper, Slides Creator, Meeting Notes",
    "   ANALYSIS: Data Analyst, Research Assistant, PDF Summarizer",
    "   CODING: Code Review, Debug Helper, SQL Assistant",
    "",
    "How to find the best ones:",
    "   - Browse by category in the GPT Store",
    "   - Check the number of conversations (popularity)",
    "   - Try before you trust: test with a real task",
])

content_slide(prs, "Creating a custom GPT: the steps", [
    "1. Go to chat.openai.com > Explore GPTs > Create",
    "   (or: chatgpt.com/gpts/editor)",
    "",
    "2. Configure via CONVERSATION ('Create' tab):",
    "   - ChatGPT guides you with questions to define the GPT",
    "   - Describe what you want it to do, how, and for whom",
    "",
    "3. Or configure manually ('Configure' tab):",
    "   - Name and description",
    "   - Detailed instructions (the 'system prompt')",
    "   - Upload knowledge files (documents, data)",
    "   - Enable/disable: web, DALL-E, Code Interpreter",
    "",
    "4. Test in the preview and iterate until you get the desired result",
    "5. Publish: Only for me / With link / In the Store",
])

# ── 5. SECTION 4 — LAB 1 ─────────────────────────────
section_slide(prs, 4, "Lab 1: Executive summary",
              "Creating a professional summary from a document — 25 min")

content_slide(prs, "Exercise: from document to summary", [
    "Objective: transform a long document into an executive summary",
    "",
    "Material: use a document from your work (not confidential!)",
    "   or download a public report (e.g., a company annual report)",
    "",
    "Step 1: Upload the document to ChatGPT (attachment icon)",
    "Step 2: Use this prompt:",
    "   'Analyze the attached document and create a 1-page executive",
    "    summary. Structure: Context (2 lines), Key Points (5 bullets),",
    "    Risks/Issues (3 bullets), Final Recommendation.",
    "    Audience: non-technical CEO. Tone: professional and direct.'",
    "Step 3: Evaluate and request changes if needed",
])

content_slide(prs, "Iteration and refinement", [
    "After the first result, try these follow-up prompts:",
    "",
    "   'Make the tone more impactful, less descriptive'",
    "",
    "   'Add the 3 most important numerical data points from the document'",
    "",
    "   'Rewrite in email format, as if you were sending it to the CEO'",
    "",
    "   'Also create a 3-line version for a Slack message'",
    "",
    "Notice: each follow-up prompt produces a different version.",
    "The ability to iterate is what distinguishes a basic user",
    "from an advanced user.",
])

# ── 6. SECTION 5 — LAB 2 ─────────────────────────────
section_slide(prs, 5, "Lab 2: Data analysis",
              "Exploring data and creating charts with Code Interpreter — 30 min")

content_slide(prs, "Preparation: the sample dataset", [
    "If you have your own CSV/Excel file (NON-sensitive data), use it!",
    "",
    "Otherwise, ask ChatGPT to create one:",
    "   'Generate a sample CSV file with sales data:",
    "    12 months, 5 products, columns: Month, Product, Quantity,",
    "    Revenue, Region. About 200 rows. Include a few",
    "    anomalies in the data to make the analysis interesting.'",
    "",
    "ChatGPT will create the file and make it downloadable.",
    "Download it, then upload it in a new chat for analysis.",
])

content_slide(prs, "Exercise: guided analysis", [
    "With the dataset uploaded, proceed as follows:",
    "",
    "Prompt 1: 'Explore this dataset. Tell me how many rows and columns it has,",
    "   what the data types are, and flag any anomalies.'",
    "",
    "Prompt 2: 'Create 3 charts showing: (1) monthly revenue trend,",
    "   (2) distribution by product, (3) comparison across regions.'",
    "",
    "Prompt 3: 'Which product has the highest growth?",
    "   Is there a month with an unusual decline? Explain possible causes.'",
    "",
    "Prompt 4: 'Create a 10-line report with the top 3 insights",
    "   and 2 recommendations. Analyst tone, backed by data.'",
])

content_slide(prs, "Downloading and reusing results", [
    "ChatGPT lets you download:",
    "   - Generated charts (PNG, SVG)",
    "   - Transformed data files (CSV, Excel)",
    "   - Python code used for the analysis",
    "",
    "How to download: click the download icon below each output",
    "",
    "Practical use:",
    "   - Insert charts into your presentations",
    "   - Use the Python code as a base for recurring analyses",
    "   - Share the report with the team",
    "",
    ">>> You don't need to know Python! ChatGPT writes and runs the code for you.",
])

# ── 7. SECTION 6 — LAB 3 ─────────────────────────────
section_slide(prs, 6, "Lab 3: Image generation",
              "Creating professional visuals with DALL-E — 25 min")

content_slide(prs, "How to write effective image prompts", [
    "Formula: SUBJECT + STYLE + DETAILS + FORMAT",
    "",
    "VAGUE example: 'Draw an office'",
    "   >>> Generic and unpredictable result",
    "",
    "EFFECTIVE example:",
    "   'A modern open-space office with 4 people collaborating",
    "    around a table. Style: flat design illustration, pastel",
    "    blue and green colors. Natural light from the window. Slightly",
    "    tilted top-down view. Landscape format 16:9.'",
    "",
    "Useful styles for work:",
    "   - Flat design / vector illustration (presentations)",
    "   - Photorealistic (marketing, social media)",
    "   - Infographic (reports, documents)",
])

content_slide(prs, "Exercise: visuals for a presentation", [
    "Create 3 images for a business presentation on [topic of your choice]:",
    "",
    "Image 1 — Cover:",
    "   'Create a cover image for a presentation on [TOPIC].",
    "    Modern and professional style, [PALETTE] colors, no text.'",
    "",
    "Image 2 — Abstract concept:",
    "   'Illustration representing [CONCEPT] metaphorically.",
    "    Flat design style, transparent background, suitable for slides.'",
    "",
    "Image 3 — Scenario:",
    "   'Scene of [WORK SITUATION] in a [DESCRIPTION] environment.",
    "    Photographic style, professional composition.'",
    "",
    "Evaluate: which image would you actually use? Which needs to be redone?",
])

content_slide(prs, "Iterating on images", [
    "After the first generation, you can refine:",
    "",
    "   'Same image but with warmer colors'",
    "   'Remove the people, keep only the environment'",
    "   'Change the style to hand-drawn illustration'",
    "   'Add an element representing innovation'",
    "",
    "Limitations to know:",
    "   - DALL-E does NOT handle text in images well",
    "   - It does not create professionally usable logos",
    "   - Each edit generates a NEW image (it does not modify the existing one)",
    "   - Images are the user's property (for commercial use)",
])

# ── 8. SECTION 7 — LAB 4 ─────────────────────────────
section_slide(prs, 7, "Lab 4: Creating a custom GPT",
              "Your first personalized assistant — 30 min")

content_slide(prs, "Exercise: a GPT for your work", [
    "Choose ONE of these GPTs to create:",
    "",
    "A. EMAIL ASSISTANT — Writes replies in your style and tone",
    "B. REPORT ANALYST — Summarizes documents in your preferred format",
    "C. PRESENTATION COACH — Helps you structure presentations",
    "D. COMPANY FAQ — Answers your team's frequently asked questions",
    "E. OTHER — A GPT specific to your needs",
    "",
    "No technical skills required: ChatGPT guides you step by step!",
])

content_slide(prs, "Step-by-step: configuring the GPT", [
    "1. Go to chatgpt.com/gpts/editor",
    "",
    "2. 'Create' tab: describe what you want in natural language",
    "   'I want an assistant that helps me write business emails",
    "    in the IT sector. It should use a professional but friendly tone,",
    "    always in English, and structure the emails with: greeting,",
    "    context, proposal, call-to-action, closing.'",
    "",
    "3. ChatGPT will ask you follow-up questions. Answer them!",
    "",
    "4. 'Configure' tab: review and customize",
    "   - Add knowledge files (price list, FAQ, templates)",
    "   - Enable/disable web, DALL-E, Code Interpreter",
    "",
    "5. 'Preview' tab: test with real questions. Iterate until satisfied.",
])

content_slide(prs, "Test and share your GPT", [
    "Tests to do before considering it ready:",
    "   - Ask 3-5 typical questions for the use case",
    "   - Try an edge case (off-topic question: it should handle it well)",
    "   - Verify that the tone and format are consistent",
    "   - Upload a test file if the GPT needs to analyze documents",
    "",
    "Sharing:",
    "   - 'Only for me': personal use (default)",
    "   - 'Anyone with the link': share with colleagues",
    "   - 'Public': visible in the GPT Store",
    "",
    ">>> A good custom GPT can save you hours every week!",
])

# ── 9. TIPS & TRICKS ─────────────────────────────────
section_slide(prs, 8, "Tips & Tricks",
              "10 tricks to use ChatGPT like a professional")

content_slide(prs, "10 tricks that few people know", [
    "1. CUSTOM INSTRUCTIONS: set once, applied every time",
    "2. KEYBOARD SHORTCUTS: Ctrl+Shift+; to copy the last response",
    "3. MENTION GPT: tag a GPT with @ inside any chat",
    "4. 'Be concise': add it to the prompt for shorter answers",
    "5. EDIT PROMPT: edit an already sent message with the pencil icon",
    "6. BRANCH: click '<' '>' to explore alternative responses",
    "7. SHARE CHAT: share icon to create a public link",
    "8. VOICE: use voice mode for hands-free brainstorming",
    "9. CHAIN OF CHATS: 'based on the previous chat...' (doesn't work!)",
    "   >>> Each chat is isolated. Copy the necessary context.",
    "10. PINNED CHATS: pin important conversations to the top",
])

content_slide(prs, "Limitations and workarounds", [
    "LIMITATION: responses are too long and verbose",
    "   Workaround: 'Answer in max 5 bullet points of 1 line each'",
    "",
    "LIMITATION: loses context in long conversations",
    "   Workaround: open a new chat with a summary of the context",
    "",
    "LIMITATION: refuses legitimate requests due to excessive caution",
    "   Workaround: rephrase by specifying the professional context",
    "",
    "LIMITATION: cannot access specific URLs reliably",
    "   Workaround: copy-paste the content directly into the chat",
    "",
    "LIMITATION: DALL-E does not render text in images",
    "   Workaround: add text afterwards with Canva, PowerPoint, etc.",
])

# ── 10. CLOSING ────────────────────────────────────────
recap_slide(prs, [
    "ChatGPT is the most versatile AI tool: chat, files, web, images, code",
    "The Free plan is enough to get started, Plus unlocks its full potential",
    "File upload + specific prompt = professional analysis in minutes",
    "Code Interpreter turns anyone into a data analyst",
    "Custom GPTs are the best way to automate repetitive tasks",
    "Memory and custom instructions make the experience tailored to you",
])

next_module_slide(prs,
    "Module 4: Claude\n"
    "The rival you need to know")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_03_chatgpt", "slides",
                   "Module_03_ChatGPT.pptx")
salva(prs, out)
