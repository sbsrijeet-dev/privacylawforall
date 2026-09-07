---
title: "CaixaBank €6M Fine: Spain Cracks Down on Bundled Consent Architecture"
case_name: "Procedimiento Nº: PS/00070/2019 (CaixaBank, S.A.)"
popular_name: "CaixaBank €6M Consent Architecture Decision"
dpa: "Agencia Española de Protección de Datos (AEPD)"
country: "Spain"
jurisdiction: "EU GDPR"
fine_amount: "€6,000,000"
fine_magnitude: "€6 Million"
decision_date: "2021-01-18"
year: 2021
articles_cited: ["Article 6", "Article 13", "Article 14"]
exam_domain: "Principles & Lawfulness of Processing (Consent Bundling & Granularity)"
tldr: "Spain's AEPD imposed a €6M fine on CaixaBank for non-compliant consent frameworks, forced bundling of commercial profiling with banking services, and opaque intra-group data transfers."
is_top_5: false
category: "consent-and-banking"
source_url: "https://www.aepd.es/es/documento/ps-00070-2019.pdf"
verified: true
---

## The Case at a Glance

In January 2021, the **Agencia Española de Protección de Datos (AEPD)** delivered a decisive ruling against CaixaBank, issuing a total financial sanction of **€6,000,000**. The decision dismantled the common banking practice of using multi-tiered, complex customer agreements to obtain blanket consent for profiling, direct marketing, and cross-subsidiary data transfers.

The penalty was structured into two core violations:
1. **€4,000,000** for infringement of **Article 6 GDPR** (unlawful processing through forced, unbundled consent mechanisms).
2. **€2,000,000** for infringement of **Articles 13 and 14 GDPR** (defective and contradictory privacy notices).

---

## What Happened & How CaixaBank Got Caught

The investigation originated from complaints filed by bank clients who discovered that opening a standard checking account required agreeing to comprehensive profiling and data-sharing across the entire CaixaBank Group (insurance, consumer credit, and marketing affiliates). 

When the AEPD audited CaixaBank's digital onboarding flows and paper contracts, it uncovered three systemic failures:

1. **Take-It-or-Leave-It Architecture**: Clients were presented with a single declaration of consent. Opting out of commercial profiling or third-party data sharing was either impossible or hidden deep within subsequent branch procedures.
2. **Conflating Legal Bases**: CaixaBank argued that certain data sharing was justified by its *"legitimate interests"* or necessary for *"contractual performance."* The AEPD rejected this defense, noting that marketing credit cards from an affiliate is neither necessary to run a checking account nor a valid legitimate interest overriding individual rights.
3. **Information Asymmetry**: Disclosures about what personal data was collected, how long it would be retained, and who received it were split across fragmented documents with contradictory legal wording.

---

## Key Legal Violations (In Plain English)

### 1. Freely Given Consent Means Granular Choice (Article 6)
Under GDPR Recital 43 and Article 7(4), consent is presumed **not** to be freely given if the contract forces data subjects to accept processing of personal data that is not necessary for the execution of that contract. CaixaBank tied core banking services to commercial advertising consent, invalidating the legal basis for millions of customer records.

### 2. The Rule Against Layered Confusion (Articles 13 & 14)
While GDPR allows layered privacy policies (a summary overview followed by detailed terms), CaixaBank's layers contradicted each other. One layer stated data was used solely for security, while the deep layer permitted behavioral tracking across digital banking portals.

---

## Practical Takeaways for Privacy Professionals & Certification Candidates

* **Banking Apps Cannot Force Marketing Opt-ins**: Core account functionality must never be conditional upon accepting advertising or partner profiling.
* **Separation of Affiliates**: A corporate group cannot treat customer data as a shared communal pool. Each transfer between subsidiaries requires an independent, verifiable legal basis.
* **CIPP/E Exam Alert**: Remember that consent under Article 4(11) must be *specific, informed, unambiguous, and granular*. Bundling multiple purposes into one toggle renders the entire consent void.
