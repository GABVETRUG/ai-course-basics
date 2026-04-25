# Instructor Guide

**AI Basics: Artificial Intelligence Tools for Everyone**

---

## Before the Course

### Classroom Setup
- [ ] Projector/screen working (slides are 16:9)
- [ ] Stable Wi-Fi (participants will use web-based tools)
- [ ] Enough power outlets for laptops
- [ ] Print exercise sheets (1 copy per participant per module)
- [ ] Print the Project Sheet + Quiz (Module 8)

### Instructor Account Setup
- [ ] ChatGPT Plus account (to demonstrate all features)
- [ ] Claude Pro account (to demonstrate Opus, Artifacts, Projects)
- [ ] HuggingChat account
- [ ] Google AI Studio account
- [ ] Test all logins the day before (platforms can change)

### Backup Materials
- [ ] Screenshots of interfaces (in case of connectivity issues)
- [ ] Sample PDF to use for live demos
- [ ] Sample CSV dataset for the Code Interpreter lab (Mod. 3)
- [ ] A long document (10+ pages) for the Claude lab (Mod. 4)

### Pre-Course Communication
Send to participants 3-5 days before:
- Course agenda
- Request to create accounts: ChatGPT, Claude (links in the email)
- Bring a work document (non-sensitive) for the exercises
- Reminder to bring a laptop and charger

---

## Facilitation Guidelines

### Pace and Energy
- **Never more than 30 minutes of theory** without a hands-on or interactive moment
- **Live demo > slides**: whenever possible, show directly on the tool
- **Live mistakes = opportunities**: if the AI gets something wrong during a demo, it is a perfect teaching moment
- **Breaks**: 10 min every 90 minutes. Labs count as an "active break"

### Managing a Non-Technical Audience
- **Zero unexplained jargon**: every technical term must be defined the first time it appears
- **Analogies before definitions**: "It is like your phone's autocomplete, but much more sophisticated"
- **Validate frustration**: "It is normal if it does not work on the first try -- that is part of the process"
- **No judgment on questions**: "Great question" is the right answer to any question

### Troubleshooting Technical Issues
| Problem | Solution |
|---------|----------|
| Account not created | Help on-site, allocate 5 extra min at Module 1 |
| ChatGPT/Claude not responding | Use HuggingChat as backup |
| Slow Wi-Fi | Switch to slides + demo from the instructor's screen |
| Rate limit reached | Use an alternative tool or the instructor's account for the demo |
| Participant falling behind | Assign a "buddy" from the faster participants |

---

## Module-by-Module Notes

### Module 1 -- What is AI (2h)

**Critical point**: the "How an LLM Works" section can feel abstract.
- Use the phone autocomplete analogy: show how a phone suggests the next word, then explain that an LLM does the same thing but on a vastly larger scale.
- Live demo: type an incomplete sentence into ChatGPT and show how it completes it.

**Lab**: make sure everyone has access to all 3 tools BEFORE starting. Dedicate 5-10 minutes to setup if needed.

**Frequently asked questions**:
- "Will AI take my job?" -- Reassure: AI is a tool, like Excel. Those who know how to use it will have an advantage, not be replaced.
- "Is my data safe?" -- Briefly preview the topic (covered in depth in Module 7).

---

### Module 2 -- Prompt Engineering (3h)

**Critical point**: bridging theory and practice. Participants tend to write vague prompts despite the explanations.
- Technique: show the VAGUE prompt and the poor result before the EFFECTIVE prompt. The "before/after" effect is very convincing.
- Have participants fill in the checklist of techniques used after each exercise.

**Lab 2 (workplace scenarios)**: it is not necessary to do all 8 scenarios. Participants choose at least 4 based on relevance to their own work.

**Lab 3 (comparison)**: this lab always sparks interesting discussions. Allow at least 10 minutes for the group debrief.

---

### Module 3 -- ChatGPT (3h)

**Recommended demos** (instructor performs in front of the class):
1. Upload a PDF and summarize it (2 min)
2. Analyze a CSV with Code Interpreter + generate a chart (5 min)
3. Generate an image with DALL-E (2 min)

**Lab 4 (custom GPT)**: this is the most ambitious lab. Some participants may not be able to complete it. That is fine: the goal is to START the creation, not necessarily to publish.

**Heads up**: the ChatGPT interface changes frequently. Verify screenshots and instructions in the slides 1-2 days before delivery.

---

### Module 4 -- Claude (3h)

**Recommended demos**:
1. Upload a long document and ask progressive questions (3 min)
2. Create an interactive calculator Artifact (3 min) -- guaranteed "wow" effect
3. Show a pre-configured Project (2 min)

**Lab 2 (Artifacts)**: participants are often surprised by what Artifacts can do. Allow extra time for free exploration.

**Claude vs ChatGPT comparison**: avoid taking sides. The message should be: "different tools for different needs."

---

### Module 5 -- Open Models (2h)

**Critical point**: non-technical participants may perceive open models as "second tier." Counter this perception with the comparison lab.

**Google AI Studio**: the interface is more technical. Walk participants through the first login step by step. Focus on the temperature experiment -- it is the concept that sticks the most.

**Key message**: you do not need to know how to code to use open models. HuggingChat is as simple as ChatGPT.

---

### Module 6 -- Real-World Use Cases (3h)

**The most important module for the course ROI.** This is where participants connect everything they have learned to THEIR OWN work.

**Workshop**: let participants work on THEIR OWN real tasks, not fictional exercises. The value lies in immediate application.

**Final sharing**: manage time strictly (max 2 min per person). The goal is not a polished presentation but an exchange of ideas.

**Prompt collection**: at the end of the workshop, collect the best prompts presented and create a shared document. This is the most valued deliverable among participants.

---

### Module 7 -- Responsible AI (2h)

**Critical point**: the risk is that it becomes "the boring lecture." Prevent this with:
- Hallucination exercise: generate a response with false facts LIVE. The shock effect works.
- Bias exercise: show the difference in responses when using different names. This creates discussion.

**Company AI policy**: if participants are from the same organization, the policy created in the lab can become a real deliverable. Suggest this.

**EU AI Act**: stick to practical concepts. There is no need to go into legal details. The message is: "legislation exists, it applies to you, keep learning."

---

### Module 8 -- Final Project (2h)

**Time management** (critical -- 2h is tight):
- 0:00-0:05 -- Briefing and objectives
- 0:05-0:25 -- Phase 1: planning
- 0:25-1:05 -- Phase 2: execution
- 1:05-1:20 -- Phase 3: presentation preparation
- 1:20-1:50 -- Presentations (with 8 participants: ~3-4 min each)
- 1:50-2:00 -- Quiz + closing

**Planning phase**: circulate among participants and validate each project BEFORE they start. Avoid excessive ambitions: a simple task done well is better.

**Presentations**: be strict on time. Use a visible timer. If the group is large (>10), reduce to 3 min per person or select the best ones.

**Quiz**: distribute the printed sheet. 15 minutes. Collect them, grade during a break or after the course.

---

## After the Course

### Recommended Follow-Up
- **Day 1**: send a thank-you email with links to materials and the shared prompt library
- **Week 1**: send a reminder "Did you use AI this week? What was your best prompt?"
- **Month 1**: short follow-up survey (3 questions: did you use AI? how much time do you save? suggestions for the course?)

### Updating Materials
AI tool interfaces and features change rapidly. Plan for:
- Verify screenshots and instructions: before every delivery
- Update models and plans: every 3-6 months
- Update regulations (AI Act): when new provisions take effect
- The Python scripts (`genera_modulo_XX.py`) allow you to regenerate slides after making changes

---

## Course Customization

### For Specific Companies
- Replace generic scenarios with scenarios from the company's industry
- Add the company logo to the slides (edit `pptx_helper.py`)
- Customize the AI policy (Module 7) with company-specific requirements
- Create pre-configured GPTs/Projects for the company's workflows

### For Different Formats

| Format | Adaptation |
|--------|------------|
| 5 days x 4h | 2 modules per day, long break between them |
| 10 sessions x 2h | 1 module per session (Mod. 6 and 8 require consecutive sessions) |
| Intensive 3 days | Compress Mod. 1+2 into 4h, Mod. 3+4 into 5h, Mod. 5+6+7+8 into 6h |
| Online synchronous | Add 15% extra time for technical management. Use breakout rooms for labs |
| Blended | Asynchronous theory (video), synchronous practice (labs in-person or online) |

---

*Instructor Guide -- AI Basics: Artificial Intelligence Tools for Everyone -- Version 1.0*
