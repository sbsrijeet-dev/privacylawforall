---
title: "Carrefour France €3.05M Fine: Excessive Retention & Cookie Tracking Violations"
case_name: "Délibération SAN-2020-008 (Carrefour France & Carrefour Banque)"
popular_name: "Carrefour €3.05M Cookie & Retention Sanction"
dpa: "Commission Nationale de l'Informatique et des Libertés (CNIL)"
country: "France"
jurisdiction: "EU GDPR"
fine_amount: "€3,050,000"
fine_magnitude: "€3.05 Million"
decision_date: "2020-11-18"
year: 2020
articles_cited: ["Article 5", "Article 13"]
exam_domain: "Storage Limitation, Transparency & ePrivacy Cookies"
tldr: "The CNIL fined Carrefour France €2.25M and Carrefour Banque €800k for dropping tracking cookies before consent, storing millions of dormant loyalty accounts, and ignoring customer unsubscribe requests."
is_top_5: false
category: "adtech-and-cookies"
source_url: "https://www.cnil.fr/fr/sanctions-carrefour-france-et-banque"
verified: true
---

## The Case at a Glance

In November 2020, France's **CNIL** sanctioned retail giant **Carrefour France** (€2,250,000) and its financial affiliate **Carrefour Banque** (€800,000), totaling **€3,050,000**. The enforcement action highlighted widespread non-compliance across retail websites, loyalty programs, and online credit platforms.

---

## What Triggered the Investigation

Between 2019 and 2020, the CNIL carried out online audits of carrefour.fr and on-site inspections at Carrefour headquarters, identifying multiple systemic GDPR and ePrivacy infractions:

1. **Automatic Cookie Dropping**: Visiting the carrefour.fr homepage instantly deposited dozens of advertising and behavioral tracking cookies onto user devices before the cookie banner was even touched.
2. **Dormant Loyalty Data Hoarding**: Carrefour maintained personal data belonging to over 28 million loyalty program members, including accounts inactive for over five to ten years, directly breaching the principle of storage limitation.
3. **Disregard for Unsubscribe Requests**: Customers who clicked unsubscribe links in marketing newsletters or requested data deletion continued to receive commercial solicitations.
4. **Opaque Credit Card Biometric & Financial Terms**: Carrefour Banque failed to provide clear, upfront information regarding interest rate terms and personal data sharing during in-store credit card signups.

---

## Regulatory Principles Enforced

### 1. Storage Limitation (Article 5(1)(e))
Data must be retained only for the duration necessary to achieve the purpose of processing. Storing customer addresses and transaction histories for a decade without any commercial interaction is a grave violation of data minimization.

### 2. Prior Consent for Non-Essential Cookies (ePrivacy)
Non-functional tracking mechanisms must remain blocked until an explicit affirmative act is performed by the visitor. Pre-loading advertising scripts on initial page request is strictly prohibited.

---

## Practical Checklist for e-Commerce Platforms

* **Cookie Scripts Must Default to Off**: Ensure Google Analytics, Meta Pixel, and ad network tags are blocked prior to user consent.
* **Automated Data Purge Routines**: Implement scheduled cron jobs to archive or delete inactive accounts after defined inactivity periods (e.g., 24–36 months).
