#!/usr/bin/env python3
"""Generate slides for Module 5 — Open Source Models (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────
title_slide(prs,
    "Module 5",
    "Open Source Models: free and open alternatives",
    "AI Basics Course  |  Duration: 2 hours  |  0.5h Theory + 1.5h Lab")

agenda_slide(prs, [
    "What 'open source' means in AI",
    "The main models: Llama, Mistral, Gemma",
    "Where to use them without installing anything",
    "Lab 1: exploring HuggingChat",
    "Lab 2: Google AI Studio",
    "Lab 3: quality comparison — open vs commercial",
    "When an open model is the right choice",
])

# ── 2. SECTION 1 — OPEN SOURCE IN AI ─────────────────
section_slide(prs, 1, "Open Source in AI",
              "Why it matters and what it means")

highlight_slide(prs,
    "DEFINITION",
    "An 'open' AI model is a model whose weights\n"
    "(parameters) are publicly available.\n"
    "Anyone can download, use, and study it.",
    "Note: 'open' does not always mean 'do whatever you want'. Licenses vary.")

content_slide(prs, "Open source vs open weight vs closed", [
    "FULLY OPEN SOURCE",
    "   Code + training data + model weights are all public",
    "   Examples: OLMo (AI2) — the most transparent",
    "",
    "OPEN WEIGHT (the most common)",
    "   Only the model weights are public (downloadable and usable)",
    "   Training code and data are often not released",
    "   Examples: Llama (Meta), Mistral, Gemma (Google)",
    "",
    "CLOSED SOURCE",
    "   Nothing is public. Access only via API or web interface",
    "   Examples: GPT-4 (OpenAI), Claude (Anthropic)",
    "",
    "For simplicity, in this course we use 'open' to refer to both of the first two.",
])

content_slide(prs, "Why open models matter", [
    "1. TRANSPARENCY: you can know (in part) how they work",
    "   Important for trust and for safety research",
    "",
    "2. INDEPENDENCE: you are not locked into a single provider",
    "   If OpenAI changes prices or policies, you have alternatives",
    "",
    "3. PRIVACY: you can run them on your own computer or server",
    "   Data never leaves your network (if you install them locally)",
    "",
    "4. CUSTOMIZATION: you can fine-tune them for your domain",
    "   A model specialized for your company or industry",
    "",
    "5. COST: many are free for commercial use",
    "   (always check the specific license!)",
])

content_slide(prs, "Licenses: what you can and cannot do", [
    "Every open model has its own license. The most common ones:",
    "",
    "Apache 2.0 (the most permissive):",
    "   Free commercial use, free modification",
    "   Models: Mistral, Gemma 2",
    "",
    "Llama Community License:",
    "   Free if your company has < 700M monthly active users",
    "   Commercial use allowed with restrictions",
    "   Models: Llama 3.1",
    "",
    "PRACTICAL RULE for your everyday use:",
    "   If you use the models through HuggingChat or AI Studio,",
    "   the licenses are handled by the platform. No issues.",
])

# ── 3. SECTION 2 — THE MAIN MODELS ───────────────────
section_slide(prs, 2, "The main models",
              "The key players of open AI")

content_slide(prs, "Llama 3.1 (Meta)", [
    "Developed by Meta (Facebook/Instagram)",
    "One of the most powerful open models in the world",
    "",
    "Available versions:",
    "   Llama 3.1 8B — Lightweight, fast, good quality (runs on a powerful PC)",
    "   Llama 3.1 70B — Very capable, competes with GPT-4 on many tasks",
    "   Llama 3.1 405B — The largest open model, exceptional quality",
    "",
    "Strengths:",
    "   - Excellent at reasoning and writing",
    "   - Multilingual (very good in Italian too)",
    "   - Context window up to 128K tokens",
    "",
    "How to use it: HuggingChat, Groq, Together AI",
])

content_slide(prs, "Mistral and Mixtral", [
    "French company Mistral AI (founded 2023, Paris)",
    "Known for efficiency: small models that are very capable",
    "",
    "Key models:",
    "   Mistral 7B — Small and surprisingly powerful",
    "   Mixtral 8x7B — 'Mixture of Experts' architecture",
    "      (uses only a subset of parameters per response = faster)",
    "   Mistral Large — Competes with top commercial models",
    "",
    "Strengths:",
    "   - Excellent quality-to-size ratio",
    "   - Very fast responses",
    "   - Excellent in French, good in Italian",
    "   - Apache 2.0 license (very permissive)",
])

content_slide(prs, "Gemma 2 (Google)", [
    "Open version of Google's models (a cousin of Gemini)",
    "Designed to be accessible and easy to use",
    "",
    "Versions:",
    "   Gemma 2 2B — Ultra-lightweight, runs even on smartphones",
    "   Gemma 2 9B — Good quality/speed trade-off",
    "   Gemma 2 27B — The most capable in the family",
    "",
    "Strengths:",
    "   - Very efficient (small but capable)",
    "   - Easy to use on Google AI Studio",
    "   - Permissive license for commercial use",
    "   - Well documented and supported by Google",
    "",
    "Ideal for: anyone who wants to experiment with limited resources",
])

content_slide(prs, "Other models to keep an eye on", [
    "Qwen 2.5 (Alibaba, China)",
    "   Very strong in reasoning and mathematics",
    "   Excellent quality/cost ratio even in smaller versions",
    "",
    "Phi-4 (Microsoft)",
    "   Ultra-compact: maximum quality for its size",
    "   Designed to run on local devices",
    "",
    "DeepSeek V3 (DeepSeek, China)",
    "   Very capable model with surprisingly low training costs",
    "   Shook the market by proving you don't need billions",
    "",
    "The landscape changes every few months — staying up to date is important!",
])

table_slide(prs, "Open model comparison",
    ["Model", "Company", "Size", "Quality", "Speed"],
    [
        ["Llama 3.1 70B", "Meta", "70B params", "Excellent", "Medium"],
        ["Mistral Large", "Mistral AI", "123B params", "Very good", "Medium"],
        ["Mixtral 8x7B", "Mistral AI", "47B params", "Good", "Fast"],
        ["Gemma 2 27B", "Google", "27B params", "Good", "Fast"],
        ["Qwen 2.5 72B", "Alibaba", "72B params", "Excellent", "Medium"],
        ["Phi-4", "Microsoft", "14B params", "Good", "Very fast"],
    ])

# ── 4. SECTION 3 — WHERE TO USE THEM ─────────────────
section_slide(prs, 3, "Where to use them without installing anything",
              "Free web platforms for open models")

content_slide(prs, "HuggingChat", [
    "huggingface.co/chat — The go-to platform for open models",
    "",
    "Features:",
    "   - FREE with no significant limits",
    "   - Login optional (recommended to save chats)",
    "   - Wide choice of models: Llama, Mistral, Gemma, Qwen and more",
    "   - You can switch models at any time",
    "   - Interface similar to ChatGPT",
    "   - Supports web search (toggleable)",
    "",
    "Limitations:",
    "   - No file upload (in the basic version)",
    "   - No image generation",
    "   - Sometimes slower than commercial services",
    "   - Quality varies across models",
])

content_slide(prs, "Google AI Studio", [
    "aistudio.google.com — Google's platform for experimentation",
    "",
    "Features:",
    "   - Free access with a Google account",
    "   - Available models: Gemini 2.5 Pro, Gemini Flash, Gemma 2",
    "   - More 'technical' interface than HuggingChat",
    "   - Parameter controls: temperature, top-p, max tokens",
    "   - File and image upload",
    "   - Ability to use 'system instructions'",
    "",
    "Ideal for:",
    "   - Those who want to understand how parameters work",
    "   - Comparing versions of Google models",
    "   - Experimentation and prototyping",
])

content_slide(prs, "Other useful platforms", [
    "Groq (groq.com)",
    "   Open models at extreme speed thanks to specialized chips",
    "   Free with usage limits. Llama, Mistral, Gemma",
    "",
    "Poe (poe.com) — by Quora",
    "   Access to MANY models (open + commercial) from a single interface",
    "   Free tier limited, subscription for unlimited use",
    "",
    "Perplexity (perplexity.ai)",
    "   AI search engine: combines models with web search",
    "   Not strictly 'open', but uses open models internally",
    "   Free with limits",
    "",
    "OpenRouter (openrouter.ai)",
    "   Access to dozens of models (open and closed) with a single API",
])

# ── 5. SECTION 4 — LAB 1 ─────────────────────────────
section_slide(prs, 4, "Lab 1: Exploring HuggingChat",
              "Your first hands-on with open models — 25 min")

content_slide(prs, "Exercise 1: setup and first message", [
    "1. Go to huggingface.co/chat",
    "2. (Optional) Create an account or sign in with Google",
    "3. Observe: which model is selected by default?",
    "",
    "4. Send your first message:",
    "   'Hello! Introduce yourself: tell me which model you are, who created you,",
    "    and what your main strengths and limitations are.'",
    "",
    "5. Look at the response: does the model 'know' who it is?",
    "",
    "6. Try a practical question:",
    "   'Write a presentation email for an IT consulting firm",
    "    to a potential client in the healthcare sector.",
    "    Professional tone, max 150 words.'",
])

content_slide(prs, "Exercise 2: switch models and compare", [
    "1. Click on the model name at the top to change it",
    "2. Select a DIFFERENT model from the previous one",
    "   Suggestion: try Llama, then Mistral, then Qwen",
    "",
    "3. Send the SAME presentation email prompt",
    "4. Compare the responses:",
    "",
    "   - Which email is more professional?",
    "   - Which one better respects the 150-word limit?",
    "   - Which one has better English?",
    "",
    "5. Try a third model and repeat the comparison",
    "",
    ">>> Each model has a different 'personality'!",
    "    Learning to recognize them helps you choose.",
])

content_slide(prs, "Exercise 3: web search", [
    "HuggingChat has a web search feature (if available):",
    "",
    "1. Enable web search (globe icon, if present)",
    "2. Ask something that requires recent information:",
    "   'What are the latest developments in generative AI",
    "    this week?'",
    "",
    "3. Observe: does it provide sources? Are the sources reliable?",
    "",
    "4. Comparison with ChatGPT:",
    "   Ask the same question to ChatGPT with web browsing enabled.",
    "   Which one provides better sources?",
    "   Which information is more up to date?",
])

# ── 6. SECTION 5 — LAB 2 ─────────────────────────────
section_slide(prs, 5, "Lab 2: Google AI Studio",
              "Experimenting with model parameters — 25 min")

content_slide(prs, "Exercise 1: first access", [
    "1. Go to aistudio.google.com",
    "2. Sign in with your Google account",
    "3. Click 'Create new prompt'",
    "",
    "4. Observe the interface:",
    "   - On the left: chat / prompt area",
    "   - On the right: model settings",
    "   - At the top: model selection (Gemini 2.5 Pro, Flash, Gemma)",
    "",
    "5. Select 'Gemini 2.5 Flash' (fast and free)",
    "",
    "6. Write: 'You are an assistant for an international company.",
    "   Always respond in English, in a concise and professional manner.'",
    "   >>> Enter this in the 'System instructions' field",
])

content_slide(prs, "Exercise 2: exploring the parameters", [
    "In the right panel you will find the model parameters:",
    "",
    "TEMPERATURE: try changing it!",
    "   - Set 0.1 and ask: 'Write 3 slogans for an ice cream shop'",
    "   - Then set 1.0 and ask the SAME question",
    "   - Observe: at low temperature the slogans are more 'safe',",
    "     at high temperature they are more creative and unpredictable",
    "",
    "TOP-P (nucleus sampling):",
    "   - Controls the 'diversity' of words considered",
    "   - 0.1 = very conservative, 1.0 = maximum variety",
    "",
    "MAX OUTPUT TOKENS:",
    "   - Maximum token limit in the response",
    "   - Try it: set 50 tokens and observe the truncated response",
])

content_slide(prs, "Exercise 3: upload and analysis", [
    "Google AI Studio supports file and image uploads:",
    "",
    "1. Click the attachment icon",
    "2. Upload an image (photo, screenshot, chart)",
    "3. Ask: 'Describe what you see in this image.",
    "   If it contains text, transcribe it. If it contains data, analyze it.'",
    "",
    "4. Try with a PDF document:",
    "   'Summarize this document in 5 key points.'",
    "",
    "5. Comparison: is the analysis quality comparable",
    "   to ChatGPT and Claude? How does it differ?",
    "",
    ">>> AI Studio is more 'technical' but offers greater control",
])

# ── 7. SECTION 6 — LAB 3 ─────────────────────────────
section_slide(prs, 6, "Lab 3: Open vs Commercial",
              "Quality comparison on real tasks — 25 min")

content_slide(prs, "Exercise: same prompt on 4 tools", [
    "Send the SAME prompt to: ChatGPT, Claude, HuggingChat, Google AI Studio",
    "",
    "Suggested prompt (complex task for a realistic test):",
    "   'You are an HR consultant. An Italian tech company (80 employees)",
    "    has a 25% annual turnover rate. Analyze the possible causes",
    "    and propose a 5-point retention plan, with estimated costs",
    "    and implementation timelines. Format: table + final recommendation.",
    "    Max 400 words.'",
    "",
    "For each one, evaluate:",
    "   - Did it follow the format (table + recommendation)?",
    "   - Are the identified causes plausible?",
    "   - Is the plan realistic and actionable?",
    "   - Did it respect the word limit?",
])

table_slide(prs, "Comparison matrix (fill it in!)",
    ["Criterion", "ChatGPT", "Claude", "HuggingChat", "AI Studio"],
    [
        ["Format adherence", "", "", "", ""],
        ["Content quality", "", "", "", ""],
        ["Cost estimate realism", "", "", "", ""],
        ["Word limit compliance", "", "", "", ""],
        ["Correct English", "", "", "", ""],
        ["TOTAL (1-25)", "", "", "", ""],
    ])

content_slide(prs, "When to prefer an open model?", [
    "PREFER OPEN WHEN:",
    "   - The budget is zero (HuggingChat is completely free)",
    "   - Privacy is critical (local models with Ollama)",
    "   - You want to experiment freely with no message limits",
    "   - The task is simple (emails, summaries, brainstorming)",
    "   - You want to understand how parameters work (AI Studio)",
    "",
    "PREFER COMMERCIAL WHEN:",
    "   - You need the highest quality possible",
    "   - You need advanced features (file upload, code interpreter)",
    "   - You work with long, complex documents",
    "   - You need image generation",
    "   - You want a more polished and reliable user experience",
])

# ── 8. CLOSING ─────────────────────────────────────────
content_slide(prs, "The future of open models", [
    "The gap between open and closed models is shrinking rapidly",
    "",
    "Current trends:",
    "   - Open models improve every 3-6 months (Llama 4 expected soon)",
    "   - Web platforms make access easier and easier",
    "   - Companies like Meta, Google, and Microsoft invest in open models",
    "   - The EU AI Act may favor transparent and open models",
    "",
    "What this means for you:",
    "   - Learn to use both commercial and open tools",
    "   - Don't lock yourself into a single provider",
    "   - Keep an eye on the latest developments (the landscape changes fast)",
    "",
    ">>> Those who master both worlds have a competitive advantage",
])

recap_slide(prs, [
    "'Open' in AI means publicly available (and often reusable) model weights",
    "Llama (Meta), Mistral, and Gemma (Google) are the key players",
    "HuggingChat and Google AI Studio let you use them for free with no installation",
    "The quality of open models is now competitive for many everyday tasks",
    "The open vs commercial choice depends on: budget, privacy, task complexity",
    "The gap is closing fast — staying up to date is essential",
])

next_module_slide(prs,
    "Module 6: AI in everyday work\n"
    "Real-world use cases and practical workflows")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_05_modelli_open", "slides",
                   "Module_05_Open_Models.pptx")
salva(prs, out)
