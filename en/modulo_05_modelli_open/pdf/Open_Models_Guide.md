# Guide to Open Source Models

**AI Basics Course — Module 5**
*In-depth document*

---

## Overview of open models

### What is an "open" model

An "open" (or "open weight") AI model is a model whose parameters (weights) are publicly available. Anyone can download, use, and in many cases modify them for their own purposes.

**What is public** (in most cases):
- The model weights (the file containing the trained parameters)
- Documentation and usage instructions
- Benchmarks and evaluation results

**What is often NOT public**:
- The complete training dataset
- The detailed training code
- The costs and resources used

---

## The main models

### Llama 3.1 (Meta)

| Feature | Detail |
|---------|--------|
| Developer | Meta (Facebook/Instagram) |
| Sizes | 8B, 70B, 405B parameters |
| Context | 128K tokens |
| Languages | Multilingual (excellent Italian) |
| License | Llama Community License (free if < 700M users) |
| Strengths | Reasoning, writing, coding, complex instructions |
| Where to use it | HuggingChat, Groq, Together AI, Ollama (local) |

**When to choose it**: complex tasks requiring advanced reasoning; when you need quality comparable to commercial models.

### Mistral / Mixtral (Mistral AI)

| Feature | Detail |
|---------|--------|
| Developer | Mistral AI (Paris, France) |
| Sizes | 7B (Mistral), 47B (Mixtral 8x7B), 123B (Large) |
| Context | 32K - 128K tokens |
| Languages | Excellent in French, good in Italian |
| License | Apache 2.0 (very permissive) |
| Strengths | Efficiency, speed, quality-to-size ratio |
| Where to use it | HuggingChat, Groq, Mistral Platform, Ollama |

**Mixture of Experts (MoE) Architecture**: Mixtral has 47B total parameters but uses only ~13B for each response. Result: quality of a large model, speed of a small model.

**When to choose it**: everyday tasks where speed is needed; limited budget; preference for European companies.

### Gemma 2 (Google)

| Feature | Detail |
|---------|--------|
| Developer | Google DeepMind |
| Sizes | 2B, 9B, 27B parameters |
| Context | 8K tokens |
| Languages | Multilingual (English is best) |
| License | Gemma Terms of Use (permissive, commercial use OK) |
| Strengths | Ultra-efficient, easy to use on AI Studio |
| Where to use it | Google AI Studio, HuggingChat, Ollama |

**When to choose it**: experimentation with limited resources; those already using the Google ecosystem; simple and fast tasks.

### Qwen 2.5 (Alibaba)

| Feature | Detail |
|---------|--------|
| Developer | Alibaba Cloud (China) |
| Sizes | 0.5B, 3B, 7B, 14B, 32B, 72B parameters |
| Context | 32K - 128K tokens |
| Languages | Excellent Chinese and English, good in other languages |
| License | Apache 2.0 |
| Strengths | Mathematics, reasoning, wide range of sizes |
| Where to use it | HuggingChat, Ollama |

**When to choose it**: mathematical or reasoning tasks; when you need a model available in many sizes.

### DeepSeek V3

| Feature | Detail |
|---------|--------|
| Developer | DeepSeek (China) |
| Sizes | 685B total (37B active, MoE architecture) |
| Context | 128K tokens |
| License | MIT (very permissive) |
| Strengths | Exceptional quality, low training costs |
| Where to use it | DeepSeek Chat, HuggingChat |

**Note**: DeepSeek has sparked debate due to geopolitical and privacy implications. The servers are in China.

---

## Where to use open models (without installing anything)

### HuggingChat (huggingface.co/chat)

**The recommended choice to get started.**

| Aspect | Detail |
|--------|--------|
| Cost | Free |
| Account | Optional (recommended to save chats) |
| Models | Llama, Mistral, Gemma, Qwen and others |
| File upload | No (basic version) |
| Web search | Yes (can be enabled) |
| Advantages | Very simple, many models, free |
| Limitations | No file upload, variable speed |

**How to change model**: click on the model name at the top of the chat.

### Google AI Studio (aistudio.google.com)

**The choice for those who want to experiment with parameters.**

| Aspect | Detail |
|--------|--------|
| Cost | Free |
| Account | Google Account required |
| Models | Gemini 2.5 Pro, Gemini Flash, Gemma 2 |
| File upload | Yes (documents and images) |
| Parameters | Temperature, top-p, max tokens (configurable) |
| Advantages | File upload, parameter control, system instructions |
| Limitations | More technical interface, fewer open models |

**System Instructions**: a field where you can write permanent instructions for the session. Example: "Always respond in English, in a concise manner."

### Groq (groq.com)

**The choice for those who want extreme speed.**

| Aspect | Detail |
|--------|--------|
| Cost | Free with usage limits |
| Models | Llama, Mistral, Gemma (the fastest on the market) |
| Advantages | 10-50x faster speed thanks to specialized chips (LPU) |
| Limitations | Usage limits on the free plan |

### Other platforms

| Platform | URL | Notes |
|----------|-----|-------|
| Poe | poe.com | Multi-model (open + closed). By Quora |
| Perplexity | perplexity.ai | AI search + open models |
| OpenRouter | openrouter.ai | Multi-model API gateway |

---

## Model parameters: practical guide

### Temperature
Controls the "creativity" vs "predictability" of responses.

| Value | Behavior | Ideal use |
|-------|----------|-----------|
| 0.0 - 0.3 | Precise, repeatable, conservative responses | Facts, data, instructions |
| 0.4 - 0.6 | Balanced between precision and variety | General use |
| 0.7 - 1.0 | Varied, creative, surprising responses | Brainstorming, creative writing |
| > 1.0 | Unpredictable responses, possible nonsense | Not recommended for professional use |

### Top-P (Nucleus Sampling)
Controls the diversity of words considered by the model.

| Value | Effect |
|-------|--------|
| 0.1 | Only the most probable words (very conservative) |
| 0.5 | Good balance |
| 0.9 - 1.0 | All words considered (maximum diversity) |

**Tip**: usually adjusting the Temperature is enough. Leave Top-P at the default (0.9-1.0) unless you have specific needs.

### Max Output Tokens
The maximum number of tokens the model can generate in the response.
- 100 tokens ~ 75 words
- 500 tokens ~ 375 words
- 2000 tokens ~ 1500 words (approximately 2 pages)

---

## Quick comparison: open vs commercial

| Criterion | Open Models (HuggingChat) | Commercial Models (ChatGPT/Claude) |
|-----------|--------------------------|-------------------------------------|
| Cost | Free | Limited free, $20/month full |
| Top task quality | Good-Excellent | Excellent |
| File upload | Limited | Yes |
| Image generation | Limited | Yes (ChatGPT) |
| Privacy | Variable (better if local) | Depends on the plan |
| Customization | High (if technical) | Limited to the interface |
| Speed | Variable | Consistent |
| Italian support | Good (Llama, Mistral) | Excellent |
| Service reliability | Medium | High |

---

## For those who want to go further: local installation

For technical users who want maximum privacy and control:

### Ollama (ollama.com)
- Software to run AI models on your own computer
- Simple installation (Mac, Linux, Windows)
- Command: `ollama run llama3.1` to start a local chat
- Data NEVER leaves your computer
- Requirements: 8-16 GB RAM for small models, 32-64 GB for large models

### LM Studio (lmstudio.ai)
- Graphical interface to run local models
- More user-friendly than Ollama
- Download models with one click from the built-in catalog
- Available for Mac, Windows, Linux

**Note**: local installation is beyond the scope of this basic course. It is mentioned as a reference for those who want to explore further.

---

*Reference document — AI Basics Course — Updated 2026*
