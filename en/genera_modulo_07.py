#!/usr/bin/env python3
"""Generate the slides for Module 7 — Responsible AI (2h)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pptx_helper import *

prs = crea_presentazione()

# ── 1. COVER + AGENDA ─────────────────────────────────────
title_slide(prs,
    "Module 7",
    "Responsible AI: Limits, Risks, and Best Practices",
    "AI Basics Course  |  Duration: 2 hours  |  1.5h Theory + 0.5h Lab")

agenda_slide(prs, [
    "Hallucinations: the number-one risk",
    "Bias and fairness: when AI discriminates",
    "Privacy and sensitive data: what NOT to give the AI",
    "Copyright and intellectual property",
    "EU AI Act: the European regulation (overview)",
    "Lab: creating a corporate AI usage policy",
    "Recap and Q&A",
])

# ── 2. SECTION 1 — HALLUCINATIONS ─────────────────────────
section_slide(prs, 1, "Hallucinations",
              "When AI invents with confidence")

highlight_slide(prs,
    "DEFINITION",
    "A hallucination is an AI response that sounds\n"
    "plausible and confident, yet is partially\n"
    "or completely FALSE.",
    "The model does not 'know' it is making things up. It is simply generating statistically likely text.")

content_slide(prs, "Real-world examples of hallucinations", [
    "A US attorney cited 6 court rulings in a brief — all invented by ChatGPT",
    "   >>> None of the rulings existed. He was sanctioned by the judge.",
    "",
    "ChatGPT fabricated scientific papers with DOIs and non-existent authors",
    "   >>> Perfect formatting, entirely false content.",
    "",
    "AI models have generated biographies containing events that never happened",
    "   >>> Dates, locations, and details that are plausible but fabricated.",
    "",
    "Google Bard claimed the James Webb Space Telescope took",
    "   the first photo of an exoplanet (false — it was SPHERE/VLT).",
    "   >>> This error during the launch demo caused a stock price drop.",
])

content_slide(prs, "Why do hallucinations happen?", [
    "1. The model does NOT access a database of facts",
    "   It generates statistically probable text; it does not 'search' for truth",
    "",
    "2. Trained to be FLUENT, not necessarily ACCURATE",
    "   Fluent and convincing text is not necessarily correct",
    "",
    "3. It cannot distinguish between 'I know' and 'I don't know'",
    "   It lacks a natural 'uncertainty' mechanism",
    "",
    "4. Training patterns",
    "   If it has seen many texts with a certain pattern, it reproduces it",
    "   even when the specific details are fabricated",
])

content_slide(prs, "How to spot hallucinations", [
    "WARNING SIGNS:",
    "",
    "Overly specific details about verifiable facts",
    "   (dates, names, numbers, citations with precise references)",
    "",
    "Overly confident answers on controversial or niche topics",
    "",
    "Information you cannot confirm with a web search",
    "",
    "Internal inconsistencies within the same response",
    "",
    "Bibliographic citations with very specific titles and DOIs",
    "   >>> If it seems too precise to be true, VERIFY!",
])

content_slide(prs, "Anti-hallucination verification techniques", [
    "1. CROSS-CHECK: compare the response with reliable sources",
    "   Google, Wikipedia, official websites, internal documents",
    "",
    "2. ASK FOR SOURCES: 'Cite the sources for this information'",
    "   If the sources don't exist, it's a hallucination",
    "",
    "3. ASK TWICE: ask the same question again in a new chat",
    "   Very different answers = probable hallucination",
    "",
    "4. USE MULTIPLE TOOLS: compare ChatGPT, Claude, web search",
    "",
    "5. GOLDEN RULE: never publish, send, or make decisions",
    "   based solely on AI output without human verification!",
])

# ── 3. SECTION 2 — BIAS ───────────────────────────────────
section_slide(prs, 2, "Bias and Fairness",
              "When AI reproduces prejudices")

highlight_slide(prs,
    "DEFINITION",
    "Algorithmic bias is the tendency of an AI model\n"
    "to produce systematically skewed results\n"
    "that favor or disadvantage certain groups.",
    "AI does not 'choose' to discriminate: it reflects the prejudices present in the training data.")

content_slide(prs, "Where does bias come from?", [
    "1. FROM THE TRAINING DATA",
    "   The internet is not neutral: it contains stereotypes, under-representations,",
    "   and dominant cultural perspectives (Anglocentrism, etc.)",
    "",
    "2. FROM THOSE WHO SELECT THE DATA",
    "   Choices about what to include or exclude introduce distortions",
    "",
    "3. FROM HUMAN FEEDBACK",
    "   The human evaluators used to refine models bring their own biases",
    "",
    "4. FROM THE PROMPT ITSELF",
    "   How we phrase the question can steer the answer",
])

content_slide(prs, "Real-world examples of AI bias", [
    "Amazon: a resume-screening system penalized female applicants",
    "   >>> Trained on 10 years of predominantly male hiring data",
    "",
    "Image generation: 'CEO' predominantly generates white men",
    "   >>> Reflects the imbalance present in online images",
    "",
    "Translation: gender-neutral languages translated with stereotypes",
    "   'O bir doktor' (Turkish, neutral) translated as 'He is a doctor'",
    "",
    "Chatbots: different responses depending on the user's name",
    "   'Ethnic' names sometimes receive less detailed answers",
])

content_slide(prs, "How to mitigate bias in everyday use", [
    "1. AWARENESS: knowing that bias exists is the first step",
    "",
    "2. INCLUSIVE PROMPTS: avoid specifying gender/ethnicity when unnecessary",
    "",
    "3. CHECK THE OUTPUTS: if the AI produces lists of names, profiles, examples,",
    "   verify they are diverse and representative",
    "",
    "4. TEST WITH VARIATIONS: change the name, gender, or origin",
    "   in the prompt and check whether the response changes unfairly",
    "",
    "5. REPORT: major providers have channels for reporting bias",
    "   (feedback features in their products)",
])

# ── 4. SECTION 3 — PRIVACY ────────────────────────────────
section_slide(prs, 3, "Privacy and Sensitive Data",
              "What happens to the data you enter into AI?")

content_slide(prs, "What happens to your data?", [
    "When you enter text into ChatGPT, Claude, or other tools:",
    "",
    "1. The data is SENT to the provider's servers (USA or Europe)",
    "",
    "2. It may be USED TO TRAIN the model (depends on the plan)",
    "   - ChatGPT Free: YES, by default (can be turned off)",
    "   - ChatGPT Plus/Enterprise: NO",
    "   - Claude Free: may use data for service improvement",
    "   - Claude Pro: no training",
    "",
    "3. Data is RETAINED for a variable period (logs, debugging, security)",
    "",
    "4. Provider staff MAY view it (quality/security review)",
])

content_slide(prs, "Data you must NEVER enter into AI", [
    "PERSONALLY IDENTIFIABLE DATA",
    "   Social security numbers, credit card numbers, passwords, health records",
    "",
    "CONFIDENTIAL BUSINESS DATA",
    "   Strategic plans, non-public financial data, contracts",
    "",
    "CUSTOMER DATA",
    "   Names + sensitive data, emails with personal information",
    "",
    "PROPRIETARY SOURCE CODE",
    "   Core algorithms, credentials, API keys",
    "",
    "PRIVILEGED LEGAL INFORMATION",
    "   Ongoing litigation, NDA agreements, confidential documents",
])

table_slide(prs, "Privacy policies of major providers",
    ["Aspect", "ChatGPT Free", "ChatGPT Enterprise", "Claude Pro"],
    [
        ["Training on user data", "Yes (can be disabled)", "No", "No"],
        ["Data retention", "30 days", "30 days", "30 days"],
        ["Human review", "Possible", "No", "Possible (security)"],
        ["Data location", "USA", "USA/EU (option)", "USA"],
        ["GDPR compliance", "Partial", "Yes", "Partial"],
        ["Encryption", "In transit", "In transit + at rest", "In transit + at rest"],
    ])

content_slide(prs, "GDPR and AI: what you need to know", [
    "The GDPR (General Data Protection Regulation) also applies to AI",
    "",
    "Key points:",
    "   - Entering third-party personal data into AI requires a legal basis",
    "   - The company is RESPONSIBLE for data entered by its employees",
    "   - Right to erasure: you can request the deletion of your data",
    "   - Automated profiling: right not to be subject to decisions",
    "     based solely on automated processing",
    "",
    ">>> When in doubt, consult your organization's DPO (Data Protection",
    "    Officer) BEFORE using personal data with AI",
])

content_slide(prs, "Best practices for privacy", [
    "1. ANONYMIZE: replace real names with fictitious ones before pasting",
    "   'John Smith, SSN 123-45-6789' >>> 'Client A, SSN XXXXXXXXX'",
    "",
    "2. GENERALIZE: remove identifying details that are not necessary",
    "   'Order #45231 from 15 Main St, Boston' >>> 'Customer order, northeast city'",
    "",
    "3. SEGMENT: send only the portion of data strictly necessary",
    "",
    "4. CHECK YOUR SETTINGS: disable training on your data",
    "   (ChatGPT: Settings > Data controls > Improve the model)",
    "",
    "5. USE ENTERPRISE PLANS whenever possible for business data",
])

# ── 5. SECTION 4 — COPYRIGHT ──────────────────────────────
section_slide(prs, 4, "Copyright and Intellectual Property",
              "Who owns what AI produces?")

content_slide(prs, "Who owns AI output?", [
    "The legal landscape is still EVOLVING globally",
    "",
    "Current positions:",
    "   USA: pure AI output is not patentable/copyrightable",
    "        (significant human input may make the work protectable)",
    "   EU: situation being defined under the AI Act",
    "   Other jurisdictions: no specific legislation yet in many countries",
    "",
    "In practice for business use:",
    "   - AI output is a STARTING POINT, not a finished product",
    "   - If you substantially modify it, your work is protected",
    "   - Providers (OpenAI, Anthropic) do not claim rights over the output",
])

content_slide(prs, "Legal risks to be aware of", [
    "1. UNINTENTIONAL PLAGIARISM: the model can reproduce protected texts",
    "   If it publishes material too similar to existing sources, you risk disputes",
    "",
    "2. TRADEMARKS AND LOGOS: do not use AI to create logos similar to existing trademarks",
    "",
    "3. ATTRIBUTION: if you use AI to write official articles/reports,",
    "   your organization may require disclosure",
    "",
    "4. LIABILITY: AI output containing errors is YOUR RESPONSIBILITY",
    "   If you publish false information generated by AI, you are accountable",
    "",
    ">>> AI generates, YOU verify and assume responsibility",
])

content_slide(prs, "Guidelines for copyright-safe use", [
    "1. Do not publish AI output without human review and editing",
    "2. Always check that the output is not too similar to known sources",
    "3. When required, disclose the use of AI in content creation",
    "4. Do not use AI to circumvent paywalls or reproduce protected content",
    "5. For critical content (legal, medical, financial), have experts validate it",
    "6. Keep the prompts you used as documentation of the creative process",
    "",
    "PRACTICAL RULE: if you would not sign it with your name,",
    "do not publish it. AI is an assistant, not an author.",
])

# ── 6. SECTION 5 — EU AI ACT ──────────────────────────────
section_slide(prs, 5, "EU AI Act",
              "The European regulation on Artificial Intelligence")

highlight_slide(prs,
    "EU AI ACT (2024)",
    "The first law in the world that comprehensively\n"
    "regulates Artificial Intelligence.\n"
    "Phased implementation from 2025 to 2027.",
    "It applies not only to AI producers but also to those who USE it in professional contexts.")

content_slide(prs, "Risk classification", [
    "The AI Act classifies AI systems into 4 risk levels:",
    "",
    "UNACCEPTABLE RISK (PROHIBITED)",
    "   Social scoring, subliminal manipulation, mass biometric surveillance",
    "",
    "HIGH RISK (REGULATED)",
    "   Personnel selection, credit, healthcare, justice, education",
    "",
    "LIMITED RISK (TRANSPARENCY OBLIGATIONS)",
    "   Chatbots, deepfakes, generated content >>> must disclose AI use",
    "",
    "MINIMAL RISK (NO OBLIGATIONS)",
    "   Spam filters, video games, product recommendations",
])

content_slide(prs, "Practical impacts for businesses", [
    "What changes for those who USE AI in business (not just producers):",
    "",
    "1. TRANSPARENCY: you must inform when content is generated by AI",
    "   Example: a customer service chatbot must disclose it is AI",
    "",
    "2. HUMAN OVERSIGHT: high-impact decisions require human review",
    "   Example: resume screening with AI requires validation by a human HR",
    "",
    "3. DOCUMENTATION: keep records of how and why AI is used",
    "",
    "4. TRAINING: employees who use AI must be trained",
    "   (and this course is a first step!)",
    "",
    ">>> Penalties can reach up to 7% of global annual revenue",
])

# ── 7. SECTION 6 — LAB ────────────────────────────────────
section_slide(prs, 6, "Hands-on Lab",
              "Creating a corporate AI usage policy")

content_slide(prs, "Why do you need a corporate policy?", [
    "Without a clear policy, every employee decides on their own:",
    "   - What data to enter (privacy risk)",
    "   - How to use the output (quality risk)",
    "   - Whether to disclose AI use (transparency risk)",
    "   - Which tools to use (security risk)",
    "",
    "A corporate policy:",
    "   - Protects the company from legal risks",
    "   - Gives clear guidelines to employees",
    "   - Enables responsible and productive AI use",
    "   - Demonstrates regulatory compliance (AI Act)",
])

content_slide(prs, "Template: sections of an AI policy", [
    "1. PURPOSE AND SCOPE: who it applies to, for which activities",
    "2. AUTHORIZED TOOLS: list of approved tools and permitted plans",
    "3. PROHIBITED DATA: clear list of what NOT to enter into AI",
    "4. OUTPUT VERIFICATION: mandatory human review before publication",
    "5. TRANSPARENCY: when and how to disclose AI use",
    "6. TRAINING: minimum requirements for employees",
    "7. RESPONSIBILITY: who is accountable for errors in AI output",
    "8. REVIEW: how often the policy should be updated",
    "",
    ">>> Use ChatGPT or Claude to create an initial draft, then customize it!",
])

content_slide(prs, "Exercise: write your own policy", [
    "In groups of 2-3 people:",
    "",
    "1. Choose a sample company (yours or a fictitious one)",
    "2. Use the template from the previous slide",
    "3. Ask Claude or ChatGPT to generate an initial draft:",
    "   'Create a corporate policy for the use of generative AI in",
    "    a [sector] company with [N] employees. The policy must",
    "    cover: authorized tools, prohibited data, verification obligation,",
    "    transparency, training. Formal tone, max 1 page.'",
    "4. Review and customize the draft",
    "5. Present your policy to the group (5 minutes)",
])

content_slide(prs, "Discussion: comparing policies", [
    "After the presentations, let's discuss together:",
    "",
    "- Which elements are COMMON to all policies?",
    "- What differences emerged between different sectors?",
    "- Was the AI-generated draft already good or did it require a lot of work?",
    "- What would you add after this discussion?",
    "",
    "TAKEAWAY: a good policy is a LIVING DOCUMENT",
    "that must be updated as technology evolves.",
    "Plan a review at least every 6 months.",
])

# ── 8. CLOSING ─────────────────────────────────────────────
recap_slide(prs, [
    "Hallucinations are inevitable: ALWAYS VERIFY before trusting",
    "Bias exists in the data and is reflected in AI: be aware",
    "Never enter personal, confidential, or sensitive data into AI",
    "AI output is YOUR RESPONSIBILITY: AI assists, you decide",
    "The EU AI Act mandates transparency, oversight, and training",
    "A clear corporate policy protects you and your organization",
])

next_module_slide(prs,
    "Module 8: Final Project\n"
    "Put everything you have learned into practice")

question_slide(prs)

# ── SAVE ───────────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__),
                   "modulo_07_responsible_ai", "slides",
                   "Module_07_Responsible_AI.pptx")
salva(prs, out)
