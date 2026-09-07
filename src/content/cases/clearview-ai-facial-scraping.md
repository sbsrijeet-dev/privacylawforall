---
title: "Clearview AI £7.55M Fine: UK ICO Outlaws Scraping Social Media for Biometric Surveillance"
case_name: "Enforcement Notice & Penalty COM0849310 (Clearview AI Inc.)"
popular_name: "Clearview AI £7.55M Facial Scraping Ban"
dpa: "Information Commissioner's Office (ICO)"
country: "United Kingdom"
jurisdiction: "UK GDPR"
fine_amount: "£7,552,800"
fine_magnitude: "£7.55 Million"
decision_date: "2022-05-23"
year: 2022
articles_cited: ["Article 5", "Article 6", "Article 9"]
exam_domain: "Special Category Biometric Data & Fairness (Articles 5, 6 & 9)"
tldr: "The UK ICO fined Clearview AI £7.55M and ordered the deletion of all UK citizen photos after finding that scraping 20+ billion web images to create commercial facial recognition models is completely illegal."
is_top_5: false
category: "ai-and-biometrics"
source_url: "https://ico.org.uk/action-weve-taken/enforcement/clearview-ai-inc/"
verified: true
---

## The Case at a Glance

In May 2022, the UK's **Information Commissioner's Office (ICO)** issued a landmark enforcement notice and a monetary penalty of **£7,552,800** against **Clearview AI Inc.** In addition to the fine, the ICO ordered the American company to cease processing the personal data of UK residents and to delete all existing UK biometric records from its systems.

The decision sent shockwaves through the artificial intelligence industry, establishing that scraping public internet photos to build biometric identification engines violates core principles of fairness, transparency, and purpose limitation.

---

## How Clearview AI Operated

Clearview AI built a database containing more than **20 billion images** of human faces by deploying automated web scrapers across social media platforms (Facebook, Instagram, LinkedIn, YouTube) and public web pages worldwide.

The company extracted biometric facial vectors from each photograph, creating a searchable facial recognition engine marketed to law enforcement agencies and commercial clients. A user could upload a snapshot of a stranger and instantly receive links to that person's online profiles, names, and home addresses.

The ICO established three critical breaches:
1. **Mass Unlawful Processing of Biometrics (Article 9)**: Facial templates are special category biometric data. Processing them requires an explicit legal exception under Article 9(2), none of which Clearview possessed.
2. **Total Lack of Fairness & Reasonable Expectations (Article 5(1)(a))**: People posting photos to social media do not reasonably expect their biometric templates to be harvested for police surveillance databases.
3. **Obstructing Data Subject Rights**: Clearview required individuals who submitted deletion requests to upload a government photo ID and another clear selfie, placing an unreasonable, unlawful barrier on their privacy rights.

---

## Legal Principles Breakdown

### 1. "Publicly Available" Does Not Mean "Free to Exploit"
A fundamental principle reaffirmed by the ICO: the fact that personal information is accessible on a public website does **not** strip it of data protection safeguards. Scraping public data without a lawful basis remains illegal.

### 2. Extraterritorial Jurisdiction (Article 3(2))
Even though Clearview AI was incorporated in the United States and had no physical UK office, it was subject to UK GDPR because it monitored the behavior of UK citizens on the internet.

---

## Critical Lessons for AI & Machine Learning Developers

* **Web Scraping Faces is Prohibited**: Model training datasets cannot contain scraped biometric images without explicit consent or statutory authorization.
* **The EU AI Act Synergy**: This ruling aligns directly with the EU AI Act's total prohibition on untargeted scraping of facial images from the internet or CCTV footage.
