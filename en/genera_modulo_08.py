#!/usr/bin/env python3
"""Generate the slides for Module 8 — Final Project and Certification (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────────
title_slide(prs,
    "Module 8",
    "Final Project and Certification",
    "AI Basics Course  |  Duration: 2 hours  |  100% Hands-on")

agenda_slide(prs, [
    "Final project objectives",
    "Briefing: what you need to deliver",
    "Phase 1: workflow design (20 min)",
    "Phase 2: building with AI (40 min)",
    "Phase 3: presentation preparation (15 min)",
    "Group presentations (30 min)",
    "Final certification quiz (15 min)",
])

# ── 2. OBJECTIVES ──────────────────────────────────────────
section_slide(prs, 1, "Final project objectives",
              "Demonstrate the skills you have acquired")

highlight_slide(prs,
    "OBJECTIVE",
    "Automate a real workflow\n"
    "from YOUR OWN job using at least\n"
    "2 different AI tools.",
    "Not a theoretical exercise: a deliverable you will take to the office on Monday morning.")

content_slide(prs, "What you will need to demonstrate", [
    "1. IDENTIFY a real task that benefits from AI",
    "      Apply the framework: repetitive, text-based, structured",
    "",
    "2. CHOOSE the right tools",
    "      At least 2 different tools (ChatGPT, Claude, HuggingChat, AI Studio)",
    "      Justify the choice: why THAT tool for THAT task",
    "",
    "3. DESIGN effective prompts",
    "      Use the techniques learned (role, context, format, constraints)",
    "",
    "4. PRODUCE a concrete deliverable",
    "      Something usable: template, procedure, report, analysis",
    "",
    "5. CRITICALLY EVALUATE the result",
    "      What worked, what didn't, where human intervention is needed",
])

content_slide(prs, "Evaluation criteria", [
    "The project will be assessed on 5 criteria (each scored 1-5):",
    "",
    "   RELEVANCE: is the chosen task genuinely useful for your work?",
    "",
    "   PROMPT ENGINEERING: are the prompts well structured?",
    "     (role, context, format, constraints, iteration)",
    "",
    "   MULTI-TOOL USAGE: did you use at least 2 different tools?",
    "     Did you justify your choice?",
    "",
    "   OUTPUT QUALITY: is the deliverable usable as-is?",
    "",
    "   CRITICAL THINKING: did you identify limitations, risks, and",
    "     where human intervention is required?",
    "",
    "SCORE: ___/25     PASSING GRADE: 15/25",
])

# ── 3. BRIEFING ────────────────────────────────────────────
section_slide(prs, 2, "Project briefing",
              "What to build and how")

content_slide(prs, "Project ideas to inspire you", [
    "COMMUNICATION:",
    "   - Kit of 10 email templates for your department",
    "   - System for generating automatic weekly reports",
    "   - Workflow for meeting minutes in 5 minutes",
    "",
    "ANALYSIS:",
    "   - Customer feedback analysis dashboard",
    "   - Sales data analysis report with charts",
    "   - Automatic pre-meeting client briefing",
    "",
    "PRODUCTIVITY:",
    "   - SOP for a process on your team (with checklist)",
    "   - Onboarding kit for new hires in your department",
    "   - Prompt library for your specific role",
    "",
    "STRATEGY:",
    "   - SWOT analysis of your product/service",
    "   - Decision matrix for a choice currently under consideration",
])

content_slide(prs, "Deliverable structure", [
    "Your project must include:",
    "",
    "1. PROJECT BRIEF (1 page):",
    "   - Chosen task and motivation",
    "   - AI tools used and why",
    "   - Estimated time: with AI vs without AI",
    "",
    "2. DOCUMENTED PROMPTS:",
    "   - The prompts used, with the technique applied",
    "   - The iterations made and why",
    "",
    "3. FINAL DELIVERABLE:",
    "   - The concrete output produced (template, report, analysis...)",
    "",
    "4. CRITICAL EVALUATION (5 lines):",
    "   - What worked and what didn't",
    "   - Where human intervention is necessary",
    "   - How you would use it in your daily work",
])

# ── 4. PHASE 1 — DESIGN ───────────────────────────────────
section_slide(prs, 3, "Phase 1: Design",
              "Define your AI workflow — 20 minutes")

content_slide(prs, "Fill in the project brief", [
    "PROJECT NAME: _______________________________________________",
    "",
    "TASK: Which work activity do you want to automate?",
    "_______________________________________________________________",
    "",
    "WHY: How much time does it take today? How often do you do it?",
    "_______________________________________________________________",
    "",
    "TOOL 1: ________________  Why: ________________________________",
    "TOOL 2: ________________  Why: ________________________________",
    "",
    "EXPECTED OUTPUT: what will the project produce?",
    "_______________________________________________________________",
    "",
    "Have the trainer validate your brief before proceeding.",
])

content_slide(prs, "Design the prompts (before writing them!)", [
    "For each step of the workflow, plan the prompt BEFORE sending it:",
    "",
    "PROMPT 1 (Tool: ___________):",
    "   Objective: _________________________________________________",
    "   Technique: [ ] Role [ ] Few-shot [ ] CoT [ ] Structured output",
    "   Draft: _____________________________________________________",
    "",
    "PROMPT 2 (Tool: ___________):",
    "   Objective: _________________________________________________",
    "   Technique: ___________________________________________________",
    "   Draft: _____________________________________________________",
    "",
    "PROMPT 3 (optional follow-up / iteration):",
    "   Objective: _________________________________________________",
    "",
    ">>> Planning FIRST and executing AFTER yields better results.",
])

# ── 5. PHASE 2 — EXECUTION ────────────────────────────────
section_slide(prs, 4, "Phase 2: Execution",
              "Put your workflows into practice — 40 minutes")

content_slide(prs, "Execute your project", [
    "Now is the time to DO. Follow the plan and take notes on everything.",
    "",
    "EXECUTION CHECKLIST:",
    "   [ ] I opened Tool 1 and sent Prompt 1",
    "   [ ] I evaluated the response: satisfactory? Needs iteration?",
    "   [ ] I iterated the prompt if necessary",
    "   [ ] I opened Tool 2 and sent Prompt 2",
    "   [ ] I combined the results from both tools",
    "   [ ] I reviewed the final output with a critical eye",
    "   [ ] I saved the prompts and results",
    "",
    "WHILE WORKING, NOTE DOWN:",
    "   - Pleasant surprises: what worked better than expected",
    "   - Problems: where you had to change your approach",
    "   - Human intervention: what you corrected or added yourself",
])

content_slide(prs, "Time management tips", [
    "40 minutes go by quickly. Manage your time as follows:",
    "",
    "   0-10 min: Execute the first prompt, evaluate, iterate",
    "   10-20 min: Move to the second tool, second prompt",
    "   20-30 min: Combine the results, review the output",
    "   30-40 min: Complete the critical evaluation, finalize the deliverable",
    "",
    "IF YOU ARE STRUGGLING:",
    "   - Simplify: reduce the scope, do fewer things but do them well",
    "   - Ask: the trainer or your colleagues",
    "   - Switch tools: if one isn't working, try the other",
    "",
    "IF YOU FINISH EARLY:",
    "   - Add a third tool for comparison",
    "   - Improve the quality of your prompts",
    "   - Document the iterations more thoroughly",
])

# ── 6. PHASE 3 — PRESENTATION ─────────────────────────────
section_slide(prs, 5, "Phase 3: Presentation",
              "Prepare and share your project — 15 min prep + 30 min pres.")

content_slide(prs, "Prepare your presentation (5 min)", [
    "Presentation structure (MAX 5 minutes per person):",
    "",
    "1. THE PROBLEM (30 sec):",
    "   'In my job, I have to do [TASK] [FREQUENCY].",
    "    It takes me about [TIME] each time.'",
    "",
    "2. THE SOLUTION (1 min):",
    "   'I used [TOOL 1] for [PURPOSE] and [TOOL 2] for [PURPOSE].'",
    "   Show the key prompts.",
    "",
    "3. THE RESULT (1 min):",
    "   Show the deliverable produced.",
    "   'Now this task takes me [NEW TIME] instead of [OLD TIME].'",
    "",
    "4. LESSONS LEARNED (30 sec):",
    "   What worked, what didn't, where human input is needed.",
    "",
    "5. QUESTION FOR THE GROUP (30 sec).",
])

content_slide(prs, "During other people's presentations", [
    "While listening to your colleagues, take note of:",
    "",
    "   - Prompts you could reuse in YOUR work",
    "   - Tools used in ways you hadn't thought of",
    "   - Workflows you could adapt to your context",
    "",
    "After each presentation:",
    "   - Ask a question or give constructive feedback",
    "   - Rate the project (peer evaluation form)",
    "",
    "GOLDEN RULE:",
    "   The greatest value of this session is not YOUR project,",
    "   but the ideas you borrow from others.",
    "",
    ">>> The trainer will collect ALL presented prompts into a",
    "    shared document: your 'class prompt library'.",
])

# ── 7. QUIZ AND CERTIFICATION ─────────────────────────────
section_slide(prs, 6, "Final Quiz and Certification",
              "Verify the skills acquired — 15 minutes")

content_slide(prs, "Final quiz: format and rules", [
    "20 questions in 15 minutes",
    "",
    "Mixed format:",
    "   - 12 multiple-choice questions (4 options)",
    "   - 4 true/false questions",
    "   - 4 short open-answer questions (1-2 sentences)",
    "",
    "Coverage:",
    "   - Modules 1-2: Foundations and prompt engineering (5 questions)",
    "   - Modules 3-4-5: Specific tools (7 questions)",
    "   - Module 6: Real-world use cases (4 questions)",
    "   - Module 7: Responsible AI (4 questions)",
    "",
    "Passing threshold: 60% (12/20)",
    "Using AI tools during the quiz is NOT permitted!",
])

content_slide(prs, "Certification", [
    "Upon completing the course (quiz + project) you will receive:",
    "",
    "CERTIFICATE OF COMPLETION",
    "   'AI Basics Course: Artificial Intelligence Tools for Everyone'",
    "   Duration: 20 hours",
    "   Skills: using ChatGPT, Claude, open-source models,",
    "   prompt engineering, responsible AI, workflow automation",
    "",
    "The certificate attests that you can:",
    "   - Use the main conversational AI tools",
    "   - Write effective prompts using structured techniques",
    "   - Choose the right tool for each task",
    "   - Apply AI responsibly and consciously",
    "   - Integrate AI into your daily workflow",
])

# ── 8. COURSE CLOSING ─────────────────────────────────────
section_slide(prs, 7, "Course Closing",
              "What to take away and next steps")

content_slide(prs, "Your next steps after the course", [
    "WEEK 1: choose ONE task and automate it with AI every day",
    "   Don't try to change everything at once. One task at a time.",
    "",
    "MONTH 1: build your personal prompt library",
    "   Every prompt that works should be saved and categorized.",
    "",
    "MONTHS 2-3: share with your team",
    "   Show your colleagues what you have learned. Become the 'AI go-to person'.",
    "",
    "ONGOING: stay up to date",
    "   AI evolves rapidly. Follow the major developments.",
    "   Recommended newsletters: The Rundown AI, AI Tool Report",
    "",
    ">>> You have the tools. Now you need practice and consistency.",
])

content_slide(prs, "Resources to keep learning", [
    "DAILY PRACTICE:",
    "   Use ChatGPT or Claude for at least 1 task per day",
    "",
    "COMMUNITY:",
    "   r/ChatGPT and r/ClaudeAI on Reddit",
    "   LinkedIn groups on AI and Prompt Engineering",
    "",
    "DEEP DIVES:",
    "   Official ChatGPT and Claude documentation",
    "   OpenAI Cookbook (advanced guides, free)",
    "   Anthropic Prompt Library (prompt examples, free)",
    "",
    "TRENDS:",
    "   The Rundown AI (daily newsletter)",
    "   AI Tool Report (tool news)",
    "",
    ">>> The best way to learn AI is... to use AI!",
])

recap_slide(prs, [
    "You have learned what AI is and how LLMs work (Mod. 1)",
    "You know how to write effective prompts with structured techniques (Mod. 2)",
    "You are proficient with ChatGPT, Claude, and open-source models (Mod. 3-4-5)",
    "You know how to apply AI to real-world use cases in your work (Mod. 6)",
    "You understand the risks, limits, and rules for responsible use (Mod. 7)",
    "You have completed a concrete project you can take to the office (Mod. 8)",
])

highlight_slide(prs,
    "THANK YOU!",
    "Artificial intelligence does not replace\n"
    "human intelligence.\n"
    "It amplifies it.",
    "The future belongs to those who know how to collaborate with AI, not to those who ignore or fear it.")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_08_final_project", "slides",
                   "Module_08_Final_Project.pptx")
salva(prs, out)
