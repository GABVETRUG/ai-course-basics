# Exercise Worksheet — Module 3: ChatGPT

**AI Basics Course**
*Hands-on session duration: 2.5 hours*

---

## Lab 1: Executive Summary from a Document (25 min)

### Preparation
- [ ] Log in to chat.openai.com
- [ ] Obtain a document of at least 5 pages (report, article, public regulation)

### Exercise 1.1: Upload and Analysis

1. Upload the document to ChatGPT (attachment icon)
2. Send this prompt:
```
Analyze the attached document and create an executive summary.
Structure: Context (2 lines), Key points (5 bullets),
Risks/Issues (3 bullets), Final recommendation.
Audience: non-technical CEO. Tone: professional and direct.
```

**Response evaluation:**

| Criterion | Score (1-5) | Notes |
|-----------|-----------|-------|
| Did it correctly understand the document? | | |
| Was the requested structure followed? | | |
| Is the tone appropriate for a CEO? | | |
| Are the key points the right ones? | | |

### Exercise 1.2: Iteration

Try at least 2 follow-up prompts:
```
Make the tone more impactful, less descriptive
```
```
Rewrite it as an email ready to send to the CEO
```

Is the second version better? In what way?

_______________________________________________________

---

## Lab 2: Data Analysis with Code Interpreter (30 min)

### Exercise 2.1: Creating a Sample Dataset

If you don't have your own CSV file, ask ChatGPT to create one:
```
Generate a CSV file with sales data:
12 months (Jan-Dec 2025), 4 products (A, B, C, D),
columns: Month, Product, Quantity, Revenue, Region (North/Central/South).
About 150 rows. Include some anomalies to make the analysis interesting.
Downloadable as a file.
```

- [ ] I downloaded the CSV file

### Exercise 2.2: Guided Analysis

Upload the CSV in a NEW chat and follow these steps:

**Step 1 — Exploration:**
```
Explore this dataset. Tell me: number of rows/columns,
data types, missing values, basic descriptive statistics.
```

**Step 2 — Visualization:**
```
Create 3 charts:
1. Total monthly revenue trend (line chart)
2. Revenue by product (bar chart)
3. Distribution by region (pie chart)
Professional style, consistent colors.
```

**Step 3 — Insights:**
```
Which product has the highest month-over-month growth?
Is there a month with an unusual dip? What are the possible causes?
```

**Step 4 — Report:**
```
Create a 10-line analysis report with:
- 3 key insights
- 2 operational recommendations
Tone: data analyst, supported by numbers.
```

### Evaluation

| Aspect | Score (1-5) |
|--------|-----------|
| Are the charts clear and readable? | |
| Are the insights relevant? | |
| Were the anomalies identified? | |
| Is the report usable? | |

- [ ] I downloaded at least one chart

---

## Lab 3: Image Generation with DALL-E (25 min)

### Exercise 3.1: First Image

Choose a theme and create an image with this prompt (adapt it):
```
A modern open-space office with people collaborating.
Style: flat design illustration, pastel blue and green colors.
Natural light. Slightly elevated view.
Horizontal format 16:9. No text in the image.
```

**Do you like the image?** _______________

**What would you change?** _______________

### Exercise 3.2: Iteration

Starting from the previous image, try these modifications:
```
Same scene but with warmer colors (orange and yellow)
```
```
Change the style to photorealistic
```
```
Remove the people, keep only the environment
```

**Which version do you prefer?** _______________

### Exercise 3.3: Image for Your Work

Create an image you could actually use in a presentation:

Your prompt:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**Would you actually use it in a presentation?** Yes / No

**Why?** _______________________________________________________

---

## Lab 4: Creating a Custom GPT (30 min)

### Exercise 4.1: Choose Your GPT

Which GPT do you want to create? (mark with X)

- [ ] A. Email Assistant — writes emails in your style
- [ ] B. Report Analyst — summarizes documents in your format
- [ ] C. Presentation Coach — helps structure slides
- [ ] D. Team FAQ — answers frequently asked questions
- [ ] E. Other: _______________

### Exercise 4.2: Configuration

1. Go to chatgpt.com/gpts/editor
2. "Create" tab: describe in natural language

Your description message:
```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

3. Answer ChatGPT's questions (name, tone, behavior)
4. Switch to the "Configure" tab and review the generated instructions

### Exercise 4.3: Testing

Test the GPT with 3 questions:

| Test question | Satisfactory response? (1-5) | Notes |
|---------------|-------------------------------|-------|
| 1. ____________ | | |
| 2. ____________ | | |
| 3. ____________ | | |

Try an edge case (off-topic question):

Question: _______________

Response: Did it behave well? _______________

### Exercise 4.4: Publishing

- [ ] I published the GPT as "Only me"
- [ ] I tested it with at least 3 questions
- [ ] Would I use it in my daily work? Yes / No

---

## Self-Assessment Quiz

### Question 1
Which ChatGPT feature allows you to execute Python code and analyze data?
- a) DALL-E
- b) Code Interpreter
- c) Canvas
- d) GPT Store

### Question 2
What can you NOT do with ChatGPT's Free plan?
- a) Upload a PDF file
- b) Create custom GPTs
- c) Use web browsing
- d) Ask general questions

### Question 3
What is the main limitation of DALL-E in image generation?
- a) It does not generate color images
- b) It does not handle text well within images
- c) It only generates black-and-white images
- d) It cannot create images of people

### Question 4
What are ChatGPT's "Custom Instructions" for?
- a) To change the interface color
- b) To set permanent instructions applied to every new chat
- c) To create a custom GPT
- d) To change the default model

### Question 5
Where do you disable the use of your data for model training?
- a) Settings > Data controls > Improve the model
- b) Settings > General > Privacy
- c) It is not possible to disable it
- d) It is automatically disabled with the Plus plan

### Answers
1: b | 2: b | 3: b | 4: b | 5: a

---

*AI Basics Course — Module 3 — Exercise Worksheet*
