#!/usr/bin/env python3
"""Generate slides for Module 1 — What Is Artificial Intelligence (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────────
title_slide(prs,
    "Module 1",
    "What Is Artificial Intelligence",
    "AI Basics Course  |  Duration: 2 hours  |  Theory + Lab")

agenda_slide(prs, [
    "What is Artificial Intelligence: definition and history",
    "Machine Learning, Deep Learning and LLMs",
    "How a Large Language Model (LLM) works",
    "Overview of available tools",
    "Lab: first interaction with ChatGPT, Claude and HuggingChat",
    "Recap and Q&A",
])

# ── 2. SECTION 1 — WHAT IS AI ─────────────────────────────
section_slide(prs, 1, "What Is Artificial Intelligence",
              "Definition, history and presence in everyday life")

highlight_slide(prs,
    "DEFINITION",
    "Artificial Intelligence is the ability of a computer\n"
    "system to perform tasks that normally\n"
    "require human intelligence.",
    "Understanding language, recognizing images, making decisions, generating content.")

content_slide(prs, "A brief history of AI", [
    "1950 — Alan Turing proposes the 'Turing Test'",
    "1956 — The field of AI is officially born (Dartmouth conference)",
    "1960-80 — First expert systems, then the first 'AI winter'",
    "1997 — Deep Blue (IBM) defeats Kasparov at chess",
    "2012 — Deep Learning revolution: deep neural networks take off",
    "2017 — Google publishes 'Attention Is All You Need' (Transformer architecture)",
    "2022 — ChatGPT opens generative AI to the general public",
    "2023-today — Explosion of AI tools accessible to everyone",
])

content_slide(prs, "AI in your daily life", [
    "Voice assistants (Siri, Alexa, Google Assistant)",
    "Recommendations from Netflix, Spotify, YouTube",
    "Anti-spam filters in email",
    "GPS navigation with real-time traffic",
    "Automatic translation (Google Translate, DeepL)",
    "Facial recognition to unlock your phone",
    "Autocorrect and text suggestions",
    ">>> You already use AI every day, without even knowing it!",
])

two_col_slide(prs, "Narrow AI vs General AI",
    "Narrow AI (Weak AI)", [
        "Specialized in a single task",
        "What we use today",
        "ChatGPT, image recognition, etc.",
        "Does not truly 'understand', it processes patterns",
        "Very powerful within its specific domain",
    ],
    "General AI (Strong AI)", [
        "Capable of any intellectual task",
        "Does not exist yet",
        "Long-term research goal",
        "Would require genuine understanding",
        "Often confused with AI in movies",
    ])

# ── 3. SECTION 2 — ML, DL, LLM ───────────────────────────
section_slide(prs, 2, "Machine Learning, Deep Learning and LLMs",
              "The three layers of modern AI")

content_slide(prs, "The three layers: a matryoshka structure", [
    "ARTIFICIAL INTELLIGENCE (the broadest field)",
    "   contains: MACHINE LEARNING (learning from data)",
    "      contains: DEEP LEARNING (deep neural networks)",
    "         contains: LLMs (Large Language Models)",
    "",
    "Each layer is a subset of the previous one.",
    "We will focus on LLMs, which are the most recent layer.",
])

highlight_slide(prs,
    "MACHINE LEARNING",
    "A system that learns from data\n"
    "instead of being explicitly programmed.",
    "Analogy: you don't write the rules, you show thousands of examples and the system finds the patterns on its own.")

content_slide(prs, "Deep Learning: deep neural networks", [
    "Loosely inspired by how the human brain works",
    "Networks of 'artificial neurons' organized in layers",
    "More layers = deeper = 'Deep' Learning",
    "Excels at recognizing complex patterns:",
    "   - Images, audio, video, text",
    "Requires enormous amounts of data and computing power",
    "It is the technology behind modern AI models",
])

content_slide(prs, "LLM: Large Language Models", [
    "'Large' language models — trained on enormous amounts of text",
    "They understand and generate natural language",
    "Examples: GPT-4 (OpenAI), Claude (Anthropic), Llama (Meta), Gemini (Google)",
    "They are the engine behind ChatGPT, Claude and other chatbots",
    "Parameters: from billions to trillions",
    "   GPT-4: estimated ~1.7 trillion parameters",
    "   Llama 3.1: up to 405 billion parameters",
    "They are not 'intelligent' — they are extremely sophisticated text predictors",
])

table_slide(prs, "Comparison: ML vs DL vs LLM",
    ["Feature", "Machine Learning", "Deep Learning", "LLM"],
    [
        ["Data type", "Tables, numbers", "Images, audio, text", "Natural text"],
        ["Complexity", "Medium", "High", "Very high"],
        ["Data required", "Thousands", "Millions", "Billions"],
        ["Examples", "Spam filter, forecasts", "Facial recognition", "ChatGPT, Claude"],
        ["User interaction", "Indirect", "Indirect", "Conversational"],
    ])

# ── 4. SECTION 3 — HOW AN LLM WORKS ──────────────────────
section_slide(prs, 3, "How an LLM Works",
              "An intuitive explanation, no math required")

highlight_slide(prs,
    "THE KEY CONCEPT",
    "An LLM predicts the next most\n"
    "probable word, one at a time.",
    "Like your phone's autocomplete, but enormously more sophisticated.")

content_slide(prs, "What was it trained on?", [
    "Books, scientific papers, web pages, Wikipedia, forums, source code...",
    "Hundreds of billions of words in dozens of languages",
    "The model does NOT memorize the texts — it learns the PATTERNS of language",
    "Analogy: someone who reads 10,000 novels doesn't remember them all,",
    "   but knows how to construct a sentence, a dialogue, an argument",
    "",
    ">>> The model is the result of what it has read, not a copy",
])

content_slide(prs, "Tokens: the units of text", [
    "The model does not read 'words' but 'tokens'",
    "A token is roughly 3/4 of a word (in English)",
    "Example: 'Artificial Intelligence' = 2-3 tokens",
    "Why does this matter?",
    "   - Costs are calculated in tokens",
    "   - Maximum length is measured in tokens",
    "   - ChatGPT-4o: ~128,000 token context window",
    "   - Claude Opus: ~200,000 token context window",
])

content_slide(prs, "The context window", [
    "The maximum amount of text the model 'sees' in a conversation",
    "Includes: your questions + the model's answers + system instructions",
    "When the context fills up, the model 'forgets' the oldest messages",
    "",
    "Analogy: a desk with limited space.",
    "You can have many pages, but at some point you must remove the oldest ones.",
    "",
    ">>> Conversations that are too long can lose the thread!",
])

content_slide(prs, "Temperature: creativity vs precision", [
    "'Temperature' controls how creative vs predictable the model is",
    "",
    "LOW temperature (0.0 - 0.3):",
    "   Precise, repeatable, conservative responses",
    "   Ideal for: data, analysis, facts",
    "",
    "HIGH temperature (0.7 - 1.0):",
    "   Varied, creative, surprising responses",
    "   Ideal for: brainstorming, creative writing, ideas",
    "",
    "Most tools handle this automatically for you.",
])

content_slide(prs, "What an LLM CANNOT do", [
    "Does NOT access the Internet in real time (except with specific plugins)",
    "Does NOT have memory across different conversations (except with dedicated features)",
    "Does NOT 'reason' like a human — it simulates reasoning through patterns",
    "Is NOT up to date — it has a training data cutoff date",
    "Does NOT guarantee accuracy — it can make up facts ('hallucinations')",
    "Does NOT truly understand — it has no consciousness, emotions or intentions",
    "",
    ">>> An extremely powerful tool, but use it with awareness!",
])

content_slide(prs, "Useful analogies to remember", [
    "LLM as an advanced phone AUTOCOMPLETE",
    "   It predicts the next word, but with much greater sophistication",
    "",
    "LLM as a brilliant but inexperienced INTERN",
    "   Fast, productive, but always needs to be verified",
    "",
    "LLM as an educated PARROT",
    "   It reproduces language patterns without true understanding",
    "",
    "LLM as a CALCULATOR for language",
    "   A powerful tool, but the judgment remains human",
])

# ── 5. SECTION 4 — TOOLS OVERVIEW ─────────────────────────
section_slide(prs, 4, "Overview of available tools",
              "ChatGPT, Claude, Gemini and open-source models")

content_slide(prs, "The AI landscape in 2025-2026", [
    "The market for conversational AI tools is evolving rapidly",
    "Three main categories:",
    "",
    "1. CLOSED COMMERCIAL: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google)",
    "   - Easy to use, powerful, but with free-tier limitations",
    "",
    "2. OPEN SOURCE / OPEN WEIGHT: Llama (Meta), Mistral, Gemma (Google)",
    "   - Free, customizable, but require more expertise",
    "",
    "3. INTEGRATED: Microsoft Copilot, Apple Intelligence, Notion AI",
    "   - Embedded in tools you already use",
])

content_slide(prs, "ChatGPT (OpenAI)", [
    "The most well-known and widely used in the world",
    "Main model: GPT-4o (omni) — text, images, audio, video",
    "Free plan: GPT-4o mini, limited use of GPT-4o",
    "Plus plan ($20/month): full access, DALL-E, custom GPTs",
    "Strengths:",
    "   - Vast ecosystem (plugins, GPTs, API)",
    "   - Built-in web browsing",
    "   - Image generation with DALL-E",
    "Limitations: can be verbose, hallucinations, data privacy",
])

content_slide(prs, "Claude (Anthropic)", [
    "Created by Anthropic, focused on safety and reliability",
    "Models: Opus (powerful), Sonnet (balanced), Haiku (fast)",
    "Free plan: Claude Sonnet, limited usage",
    "Pro plan ($20/month): access to all models, higher usage",
    "Strengths:",
    "   - Excellent at analyzing long documents (200K tokens)",
    "   - Artifacts: generates code, charts, interactive documents",
    "   - Projects: organizes conversations by project",
    "   - Responses often more precise and less verbose than ChatGPT",
    "Limitations: no native image generation, smaller ecosystem",
])

two_col_slide(prs, "Other tools worth knowing",
    "Google Gemini", [
        "Integrated with the Google ecosystem",
        "Access to Google data (Gmail, Drive...)",
        "Gemini 2.5 Pro/Flash models",
        "Free with a Google account",
        "Strong in multimodal reasoning",
    ],
    "Microsoft Copilot", [
        "Integrated in Windows and Office 365",
        "Powered by OpenAI's GPT-4",
        "Free in the basic version",
        "Copilot Pro in Word, Excel, PPT",
        "Ideal if you already use Microsoft 365",
    ])

content_slide(prs, "Open Source Models", [
    "Models whose code/weights are publicly available",
    "",
    "Llama 3.1 (Meta): one of the most powerful open models",
    "Mistral / Mixtral: French company, excellent quality",
    "Gemma 2 (Google): open version of Google's models",
    "",
    "How to use them WITHOUT installing anything?",
    "   - HuggingChat (huggingface.co/chat) — free web interface",
    "   - Google AI Studio (aistudio.google.com) — for Gemma and Gemini",
    "",
    ">>> In Module 5 we will explore them in detail",
])

table_slide(prs, "Quick comparison of tools",
    ["Feature", "ChatGPT", "Claude", "HuggingChat"],
    [
        ["Company", "OpenAI", "Anthropic", "Hugging Face"],
        ["Free plan", "Yes (limited)", "Yes (limited)", "Yes (unlimited)"],
        ["Document analysis", "Good", "Excellent", "Basic"],
        ["Image generation", "Yes (DALL-E)", "No", "Yes (some models)"],
        ["Web browsing", "Yes", "No", "No"],
        ["Ideal for", "General use", "Analysis and writing", "Experimenting with open source"],
    ])

# ── 6. SECTION 5 — LAB ────────────────────────────────────
section_slide(prs, 5, "Hands-on lab",
              "First interaction with ChatGPT, Claude and HuggingChat")

content_slide(prs, "Preparation: create your accounts", [
    "1. ChatGPT: go to chat.openai.com and sign up (free)",
    "2. Claude: go to claude.ai and sign up (free)",
    "3. HuggingChat: go to huggingface.co/chat (free, optional login)",
    "",
    "Tips:",
    "   - Use the same email for all of them (easier to manage)",
    "   - The free plans are sufficient for the entire course",
    "   - If you already have an account, make sure you can log in",
])

content_slide(prs, "Exercise 1: The same question on three tools", [
    "Ask the SAME question to ChatGPT, Claude and HuggingChat:",
    "",
    "Suggested question:",
    "   'Explain what artificial intelligence is to a 10-year-old child,",
    "    using an example from everyday life.'",
    "",
    "For each response, note:",
    "   - Length of the response",
    "   - Clarity and simplicity of the language",
    "   - Quality of the chosen example",
    "   - Which one you prefer and why",
])

content_slide(prs, "Exercise 2: analyze the differences", [
    "After receiving the three responses, reflect:",
    "",
    "1. Are the responses similar or very different?",
    "2. Which tool best matched the tone (10-year-old child)?",
    "3. Which example seems most effective to you?",
    "4. Did you notice any errors or questionable information?",
    "",
    ">>> There is no 'right' answer — the goal is to develop",
    "    critical thinking about AI outputs",
])

content_slide(prs, "Group discussion", [
    "Share your observations with the group:",
    "",
    "- Which tool did you prefer and why?",
    "- Did you find any surprising differences?",
    "- Did you immediately trust the responses?",
    "- Would you change anything in the question to get better results?",
    "",
    ">>> Spoiler: the quality of the question is just as important",
    "    as the quality of the tool!",
    "",
    "(In the next module we will learn exactly how to formulate effective questions)",
])

# ── 7. CLOSING ─────────────────────────────────────────────
recap_slide(prs, [
    "AI is a vast field; LLMs are the most recent and accessible layer",
    "An LLM predicts the next word — it does not truly 'understand'",
    "There are commercial tools (ChatGPT, Claude) and open source (Llama, Mistral)",
    "The free plans are sufficient to get started",
    "Each tool has different strengths — comparing them is essential",
    "The quality of the question determines the quality of the answer",
])

next_module_slide(prs,
    "Module 2: Prompt Engineering\n"
    "The art of asking the right questions to AI")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_01_intro_ai", "slides", "Module_01_Intro_AI.pptx")
salva(prs, out)
