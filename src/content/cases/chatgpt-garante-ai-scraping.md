---
title: "When Italy Blocked ChatGPT: The Landmark AI Training & Scraping Standoff"
case_name: "OpenAI L.L.C. - ChatGPT Processing of Italian Users' Data (Garante Decision 9870832)"
popular_name: "Garante Italy ChatGPT AI Ban"
dpa: "Garante"
country: "Italy"
jurisdiction: "EU GDPR"
fine_amount: "Compliance Order & Formal Warning"
fine_magnitude: "Pending"
decision_date: "2023-03-30"
year: 2023
articles_cited: ["Article 5(1)(a)", "Article 6", "Article 8", "Article 13"]
exam_domain: "AI Governance & Data Subject Rights (AIGP & CIPP/E)"
tldr: "Italy's Garante made global headlines by temporarily blocking ChatGPT across Italy, citing mass web-scraping for AI training without legal basis and a complete absence of age verification."
is_top_5: false
category: "ai-and-biometrics"
source_url: "https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9870832"
verified: true
---

## At a Glance

* **The Offender:** OpenAI L.L.C.
* **The Authority:** Garante per la Protezione dei Dati Personali (Italy)
* **The Penalty:** Immediate nationwide limitation of processing (temporary block) + compliance injunction
* **The Core Issue:** Mass scraping of personal data to train Large Language Models (LLMs) without a lawful basis, inaccurate AI hallucinations about real people, and zero age gating for minors.

---

## 1. The TL;DR in Plain English

In March 2023, Italy became the first Western nation to temporarily shut down ChatGPT. The Italian Data Protection Authority (*Garante*) issued an emergency order stopping OpenAI from processing Italian citizens' personal data.

Regulators asked OpenAI a fundamental question: **What legal basis gives you the right to scrape personal information, blog posts, social media comments, and emails of millions of living people off the open web to train a commercial AI model?** When OpenAI could not produce a valid justification or show that it verified users' ages, Italy pulled the plug until OpenAI met strict compliance demands.

---

## 2. The Story: What Happened?

The immediate trigger was a data breach in March 2023 where a bug in ChatGPT's open-source library exposed users' conversation titles and payment details. 

However, when the Italian Garante began investigating, they uncovered systemic GDPR conflicts at the very core of Generative AI technology:
1. **No Privacy Notice:** OpenAI provided no notice to people whose articles, biographies, or online comments were used to train GPT models.
2. **No Lawful Basis for Training:** OpenAI had neither asked for consent from the billions of internet users whose data was scraped, nor demonstrated a balanced "legitimate interest."
3. **AI Hallucinations Violate the "Accuracy" Principle:** ChatGPT routinely hallucinated defamatory or incorrect biographical information about living citizens, violating the GDPR guarantee that personal data must be accurate.
4. **No Age Verification:** Children under 13 could sign up freely, exposing them to potentially inappropriate content.

---

## 3. The 30-Day Compliance Ultimatum

Instead of simply abandoning the Italian market, OpenAI engaged in high-stakes negotiations with the Garante. To lift the ban within a month, OpenAI was forced to:
* Publish a transparent information notice explaining how personal data is collected to train algorithms.
* Implement an age-gate on signup in Italy.
* Create a dedicated web form allowing European citizens to exercise their **Right to Object (Article 21)** to having their data used to train OpenAI models.
* Enable users to opt out of having their chat histories used for future model training.

---

## 4. The Legal Violation: Why the Authority Stepped In

The Garante's order applied core GDPR provisions directly to Generative AI architectures:

### Article 6 (Lawfulness of Processing)
Every data processing activity—including scraping text for dataset preparation and matrix multiplication during model pre-training—requires an identifiable legal basis under Article 6.

### Article 5(1)(d) (The Principle of Accuracy)
Controllers must take all reasonable steps to ensure personal data is accurate. When an LLM generates false criminal allegations or fake biographical claims about an individual, it breaches the accuracy principle.

### Article 8 (Children's Consent)
In the absence of filtering or age gating, young children were exposed to processing without parental authorization.

---

## 5. What This Means for Privacy Teams & AIGP / CIPP/E Students

1. **AI Training Data is Subject to GDPR:** You cannot claim that "public internet data" is exempt from data protection law. Scraping is personal data processing.
2. **The "Right to Object" Must Be Actionable:** AI developers must build mechanisms that allow individuals to exclude their data from future training runs and retrieval-augmented systems.
3. **Accuracy & Hallucinations:** As the EU AI Act comes into force alongside GDPR, training an AI system that generates factual claims about individuals without verification mechanisms poses severe regulatory liability.
