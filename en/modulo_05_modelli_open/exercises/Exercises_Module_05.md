# Exercise Worksheet — Module 5: Open Source Models

**AI Basics Course**
*Hands-on session duration: 1.5 hours*

---

## Lab 1: Exploring HuggingChat (25 min)

### Preparation
- [ ] Go to huggingface.co/chat
- [ ] (Optional) Create an account to save your chats

### Exercise 1.1: First contact

1. Observe: which model is selected by default? _______________

2. Send this message:
```
Hello! Introduce yourself: tell me which model you are, who created you,
and what your 3 main strengths and 3 main limitations are.
```

**Does the model know who it is?** Yes / No / Partially

**Do the stated limitations seem honest?** _______________

### Exercise 1.2: Practical task

Send this prompt:
```
Write an introductory email for an IT consulting firm
to a potential client in the healthcare sector.
Professional tone, max 150 words.
```

**Evaluation:**

| Criterion | Score (1-5) |
|-----------|------------|
| Text quality | |
| Correct English | |
| Does it respect the word limit? | |
| Appropriate tone | |

### Exercise 1.3: Change model and compare

1. Click on the model name at the top
2. Select a DIFFERENT model (suggestion: if you had Llama, try Mistral)
3. Send the SAME introductory email

Model 1 used: _______________
Model 2 used: _______________

| Criterion | Model 1 (1-5) | Model 2 (1-5) |
|-----------|---------------|---------------|
| Text quality | | |
| English | | |
| Constraint compliance | | |
| Tone | | |
| **Preference** | | |

3. (Optional) Try a third model and repeat

---

## Lab 2: Google AI Studio (25 min)

### Preparation
- [ ] Go to aistudio.google.com
- [ ] Sign in with your Google account

### Exercise 2.1: Setup and system instructions

1. Click "Create new prompt"
2. In the "System instructions" field (at the top), write:
```
You are a professional assistant for a company.
Always respond in English, in a concise and structured manner.
Use bullet points when appropriate.
```

3. Select the model: "Gemini 2.5 Flash"
4. Send a test question:
```
What are the 5 main advantages of using AI in business?
```

**Did it follow the system instructions (English, concise, bullet points)?** Yes / No

### Exercise 2.2: Experimenting with temperature

**Test 1 — Low temperature (0.1):**
1. In the right panel, set Temperature: 0.1
2. Send: `Write 3 slogans for an artisanal ice cream shop`
3. Note down the 3 slogans:
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

**Test 2 — High temperature (1.0):**
1. Set Temperature: 1.0
2. Send the SAME question
3. Note down the 3 slogans:
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________

**Differences noticed:**

_______________________________________________________

**Which temperature produced better slogans for real-world use?**

_______________________________________________________

### Exercise 2.3: Max output tokens

1. Set "Max output tokens" to **50**
2. Send: `Explain what machine learning is`
3. Observe: was the response truncated? _______________
4. Now set it to **500** and ask the same question again
5. Difference in quality: _______________

**Lesson learned about tokens:** _______________

### Exercise 2.4: Upload an image (if available)

1. Click the attachment icon
2. Upload an image (photo, screenshot, chart)
3. Ask:
```
Describe what you see in this image.
If it contains text, transcribe it. If it contains data, analyze it.
```

**Is the description accurate?** (1-5): ___

---

## Lab 3: Open vs Commercial Comparison (25 min)

### Exercise 3.1: Test on 4 tools

Send the SAME prompt to all 4 tools:

**Prompt:**
```
You are an HR consultant. An Italian tech company (80 employees)
has a 25% annual turnover rate. Analyze the possible causes
and propose a 5-point retention plan, with estimated costs
and implementation timelines. Format: table + final recommendation.
Max 400 words.
```

Fill in for each tool:

### ChatGPT
- Format followed (table + recommendation)? Yes / No
- Word limit respected? Yes / No / Approximate
- Content quality (1-5): ___
- Notes: _______________________________________________

### Claude
- Format followed? Yes / No
- Word limit respected? Yes / No / Approximate
- Content quality (1-5): ___
- Notes: _______________________________________________

### HuggingChat (model: _______________)
- Format followed? Yes / No
- Word limit respected? Yes / No / Approximate
- Content quality (1-5): ___
- Notes: _______________________________________________

### Google AI Studio (model: _______________)
- Format followed? Yes / No
- Word limit respected? Yes / No / Approximate
- Content quality (1-5): ___
- Notes: _______________________________________________

### Final ranking

| Position | Tool | Total score |
|----------|------|------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

### Reflection

**Is the quality gap between open and commercial models large or small?**

_______________________________________________________

**For this specific task, would an open model be sufficient?**

_______________________________________________________

**In which situations would you choose an open model?**

_______________________________________________________

---

## Self-assessment quiz

### Question 1
What does "open weight" mean for an AI model?
- a) The model is free for any use
- b) The model's weights (parameters) are publicly available
- c) The training code is public
- d) The model works without an internet connection

### Question 2
Which of the following is an open source model?
- a) GPT-4o (OpenAI)
- b) Claude Opus (Anthropic)
- c) Llama 3.1 (Meta)
- d) Gemini 2.5 Pro (Google)

### Question 3
On which platform can you use open models WITHOUT installing anything?
- a) Ollama
- b) LM Studio
- c) HuggingChat
- d) Visual Studio Code

### Question 4
What does the "temperature" parameter control in an AI model?
- a) The response speed
- b) The level of creativity vs predictability of responses
- c) The maximum response length
- d) The response language

### Question 5
When is it better to prefer an open model over a commercial one?
- a) When you need the highest possible quality
- b) When the budget is zero and the task is not too complex
- c) When you need to generate images
- d) When you need to analyze documents of 100+ pages

### Answers
1: b | 2: c | 3: c | 4: b | 5: b

---

## My tool map

After trying all the tools, fill in your personal map:

| For this type of task... | I will use... | Because... |
|--------------------------|---------------|------------|
| Email and communication | | |
| Data analysis | | |
| Long documents | | |
| Brainstorming | | |
| Images | | |
| Simple and quick tasks | | |
| When privacy is critical | | |

---

*AI Basics Course — Module 5 — Exercise worksheet*
