# AI Glossary — Key Terms to Get Started

**AI Basics Course — Module 1**
*Supplementary document*

---

## Fundamental Terms

### Artificial Intelligence (AI)

A field of computer science focused on creating systems capable of performing tasks that normally require human intelligence: understanding language, recognizing images, making decisions, generating content.

### Machine Learning (ML)

A subfield of AI in which systems **learn from data** instead of being explicitly programmed with rules. The algorithm finds patterns in the data and uses them to make predictions or classifications.

### Deep Learning (DL)

A subfield of Machine Learning based on **deep neural networks** (with many layers). It excels at recognizing complex patterns in images, audio, and text.

### LLM (Large Language Model)

A large-scale language model trained on enormous amounts of text to understand and generate natural language. Examples: GPT-4 (OpenAI), Claude (Anthropic), Llama (Meta).

### Generative AI

A category of AI capable of **creating new content**: text, images, audio, video, code. ChatGPT and Claude are examples of text-based generative AI; DALL-E and Midjourney are image-based generative AI.

---

## How Models Work

### Token

The smallest unit of text processed by an LLM. One token is approximately 3/4 of a word in English (slightly less in Italian). "Artificial Intelligence" corresponds to roughly 4-5 tokens.

### Context (Context Window)

The maximum amount of text a model can "see" in a single interaction. It includes your question, previous responses, and system instructions. When the context fills up, the model loses the oldest messages.

| Model | Context Window |
|---------|---------------------|
| GPT-4o | ~128,000 tokens |
| Claude Opus/Sonnet | ~200,000 tokens |
| Llama 3.1 | ~128,000 tokens |
| Gemini 2.5 Pro | ~1,000,000 tokens |

### Temperature

A parameter that controls the "creativity" of the model. Low temperature (0.0-0.3) produces precise and repeatable responses; high temperature (0.7-1.0) produces more varied and creative responses.

### Parameters

The internal "weights" of the model, learned during training. More parameters generally means a more capable model (but also slower and more expensive). GPT-4 has approximately 1.7 trillion parameters.

### Training

The process in which the model reads enormous amounts of text to learn language patterns. It can take weeks on thousands of GPUs and cost millions of dollars.

### Fine-tuning

An additional training process on a specific dataset to specialize a pre-trained model. Example: a general model further trained on medical documents for healthcare use.

### Inference

The moment the model **generates a response**. When you chat with ChatGPT, the model is performing inference. It has a computational (and financial) cost for each token generated.

---

## Interacting with Models

### Prompt

The instruction or question you send to the AI model. The quality of the prompt determines the quality of the response. See Module 2 for Prompt Engineering techniques.

### Hallucination

An AI response that sounds plausible but is **partially or completely false**. The model generates statistically probable text; it does not verify facts. See Module 7 for further details.

### System Prompt

A system instruction, invisible to the user, that defines the model's behavior. Example: "You are a helpful assistant that always responds in formal English."

### Chat / Conversation

An interaction mode in which the model maintains the **context of previous messages** within the same session. It allows you to refine responses and explore a topic in greater depth.

### Streaming

A display mode in which the response appears **word by word** in real time, rather than waiting for the full generation to complete. This is what you normally see on ChatGPT and Claude.

---

## Tools and Platforms

### ChatGPT

OpenAI's chatbot based on GPT models. The most widely used in the world. Available in a free version (GPT-4o mini + limited GPT-4o) and a paid version (Plus, $20/month).

### Claude

Anthropic's chatbot, focused on safety and reliability. Models: Opus (powerful), Sonnet (balanced), Haiku (fast). Available for free (limited) and Pro ($20/month).

### Gemini

Google's chatbot, integrated into the Google ecosystem (Gmail, Drive, Docs). Free with a Google account. Gemini 2.5 Pro and Flash models.

### Copilot

Microsoft's AI assistant integrated into Windows, Edge, and Office 365. Based on OpenAI technology (GPT-4). Free in the basic version.

### HuggingChat

A free web interface by Hugging Face that allows you to use open-source models (Llama, Mistral, etc.) without installation.

### Google AI Studio

Google's platform for experimenting with Gemini and Gemma models. Free with a Google account.

---

## Open Source Models

### Open Source / Open Weight

A model whose source code and/or weights are publicly available. Anyone can download, use, and modify them. Not always free for commercial use (depends on the license).

### Llama (Meta)

Meta's (Facebook) family of open models. Llama 3.1 is among the most powerful open models available. Versions range from 8B to 405B parameters.

### Mistral / Mixtral

Models from the French company Mistral AI. Known for their excellent quality-to-size ratio. Mixtral uses a "Mixture of Experts" architecture.

### Gemma (Google)

The open version of Google's models, smaller and suited for experimentation and local use. Gemma 2 is available from 2B to 27B parameters.

### Ollama

Software that allows you to **run AI models on your own computer**, without sending data to external servers. Requires technical knowledge for installation.

---

## Advanced Concepts (Overview)

### API (Application Programming Interface)

An interface that allows programs and applications to **communicate with AI models via code**, without using the web interface. Essential for integrating AI into business software.

### RAG (Retrieval-Augmented Generation)

A technique that allows the model to **search for information in specific documents** before responding. It reduces hallucinations and enables the use of up-to-date business data.

### Embedding

A numerical representation of text (vector) that captures its meaning. Used for semantic search, document comparison, and RAG systems.

### Multimodal

A model capable of processing **multiple types of input**: text, images, audio, video. GPT-4o and Claude are multimodal (text + images). Gemini also handles audio and video.

### AI Agents

Systems that can **perform actions autonomously**: browse the web, write code, use tools, make decisions. They represent the evolution of simple chatbots.

### Transformer

The neural network architecture underlying all modern language models. Introduced by Google in 2017 ("Attention Is All You Need"). The "T" in GPT stands for Transformer.

---

*This glossary is a living document: terms and definitions evolve with technology. Last updated: 2026.*
