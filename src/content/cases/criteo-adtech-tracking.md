---
title: "Criteo €40M Fine: France's CNIL Holds AdTech Retargeters Accountable for Cookie Consent"
case_name: "Délibération SAN-2023-009 (Société CRITEO)"
popular_name: "Criteo €40M AdTech Retargeting Sanction"
dpa: "Commission Nationale de l'Informatique et des Libertés (CNIL)"
country: "France"
jurisdiction: "EU GDPR"
fine_amount: "€40,000,000"
fine_magnitude: "€40 Million"
decision_date: "2023-06-15"
year: 2023
articles_cited: ["Article 7", "Article 12", "Article 13", "Article 15", "Article 17"]
exam_domain: "Accountability & Data Subject Rights in AdTech (Articles 7, 15, 17)"
tldr: "France's CNIL sanctioned adtech giant Criteo €40 Million for collecting behavioral tracking data from 370 million internet users without verifying that publisher websites had gathered valid prior consent."
is_top_5: false
category: "adtech-and-cookies"
source_url: "https://www.cnil.fr/fr/sanction-de-40-millions-deuros-lencontre-de-la-societe-criteo"
verified: true
---

## The Case at a Glance

In June 2023, the French **CNIL** imposed a decisive **€40,000,000** fine on **Criteo**, one of the world's largest adtech companies specializing in programmatic behavioral retargeting. 

Criteo provides code snippets that publishers embed on commercial websites. When users browse products, Criteo places cookies, builds browsing histories, and displays personalized banner ads across other sites. The CNIL ruled that Criteo could not rely on publishers to get consent without active verification, and penalized Criteo for obstructing user rights to erasure and access.

---

## How Criteo Got Caught

Following complaints filed by digital rights groups Privacy International and None of Your Business (noyb), the CNIL conducted audits of Criteo's data collection pipeline.

The audit revealed:
1. **No Proof of Consent**: When Criteo dropped its tracker cookie and collected user browsing events, it failed to verify that the host website had actually displayed a compliant cookie banner or obtained valid consent.
2. **Phantom Erasure**: When internet users exercised their Right to Erasure (Article 17) or Right to Object (Article 21), Criteo merely ceased displaying targeted ads to that identifier, but retained the historical behavioral dataset.
3. **Empty Right of Access**: When data subjects requested copies of their personal data under Article 15, Criteo provided incomplete technical dumps that omitted the full scope of behavioral profiling.

---

## Legal Analysis

### 1. Joint Controllership & Vendor Accountability (Article 7(1))
The CNIL reiterated that an adtech vendor acting as a joint controller or independent controller cannot hide behind its commercial partners. If an adtech provider processes tracking data, it must be able to demonstrate that valid consent preceded the processing.

### 2. Erasure Means Complete Deletion (Article 17)
Disabling ad delivery while retaining the underlying browsing events does **not** satisfy Article 17. Regulators require permanent, unrecoverable deletion or irreversible anonymization of the personal data.

---

## Compliance Takeaways

* **AdTech Vendors Must Audit Publishers**: Ad networks cannot operate on blind faith; automated audits of publisher CMPs (Consent Management Platforms) are legally mandatory.
* **DSAR Automation Must Include Profiling Logs**: Subject access requests must provide all behavioral events tied to the individual's advertising IDs.
