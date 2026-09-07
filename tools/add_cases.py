# tools/add_cases.py
import sys
from pathlib import Path

cases_dir = Path(__file__).resolve().parent.parent / "src" / "content" / "cases"

cases = [
    {
        "filename": "caixabank-customer-consent.md",
        "content": """---
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
category: "Financial & Consent Architecture"
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
"""
    },
    {
        "filename": "bbva-spain-consent-fine.md",
        "content": """---
title: "BBVA €5M Penalty: Forced Consent & Opaque Privacy Notices Under Spanish Law"
case_name: "Procedimiento Nº: PS/00060/2020 (Banco Bilbao Vizcaya Argentaria, S.A.)"
popular_name: "BBVA €5M Forced Consent Sanction"
dpa: "Agencia Española de Protección de Datos (AEPD)"
country: "Spain"
jurisdiction: "EU GDPR"
fine_amount: "€5,000,000"
fine_magnitude: "€5 Million"
decision_date: "2020-12-11"
year: 2020
articles_cited: ["Article 6", "Article 13", "Article 14"]
exam_domain: "Principles & Transparency (Articles 6, 13 & 14)"
tldr: "The AEPD fined Banco Bilbao Vizcaya Argentaria (BBVA) €5 Million for coercing bank account holders into accepting omnibus data processing and providing vague, legalistic privacy statements."
is_top_5: false
category: "Banking & Consent Architecture"
source_url: "https://www.aepd.es/es/documento/ps-00060-2020.pdf"
verified: true
---

## The Case at a Glance

In December 2020, Spain's **Agencia Española de Protección de Datos (AEPD)** issued a landmark **€5,000,000** fine against **BBVA (Banco Bilbao Vizcaya Argentaria)**. The sanction targeted the financial institution's customer onboarding documents, which used unbundled consent formulas and imprecise language regarding how customer transactions were monitored for commercial cross-selling.

The fine comprised:
* **€3,000,000** for violating **Article 6 GDPR** (unlawful processing without valid consent).
* **€2,000,000** for violating **Articles 13 and 14 GDPR** (inadequate and opaque information provided to data subjects).

---

## What Happened & How BBVA Got Caught

Spanish privacy advocates and consumers lodged complaints detailing that BBVA's customer onboarding forms forced signatories to agree to comprehensive commercial data usage. 

Upon investigation, the AEPD established that BBVA:
1. **Employed Formulaic Consent**: Checkboxes were presented in a manner that gave users no granular control over distinct processing operations (e.g., credit scoring, direct telephone marketing, and cross-border group transfers).
2. **Used Vague Terminology**: Privacy policies described processing goals using terms such as *"to offer products you may find interesting"* and *"to improve your banking experience"*, failing to specify the concrete categories of data utilized.
3. **Misapplied Legitimate Interest**: BBVA claimed legitimate interest for transmitting customer profiles to group companies for advertising, ignoring the stringent three-part test (purpose, necessity, balancing test) mandated under EDPB guidelines.

---

## Legal Principles Breakdown

### 1. Specificity & Granularity (Article 6 & Recital 32)
Consent cannot be omnibus. If processing has multiple distinct aims (e.g., fraud prevention vs. telemarketing vs. third-party sharing), data subjects must have the ability to accept or decline each purpose individually.

### 2. Plain, Intelligible Language (Article 12 & 13)
The AEPD emphasized that transparency requires plain English (or Spanish), intelligible to everyday consumers without a law degree. Hiding commercial tracking behind vague corporate buzzwords violates the principle of transparency.

---

## Key Lessons for Organizations

* **Audit Onboarding Flows**: Checkboxes pre-ticked or bundled into master service agreements are deemed unlawful by regulators across Europe.
* **Define Legal Bases Clearly**: Never cite consent and legitimate interest interchangeably for the same processing activity.
"""
    },
    {
        "filename": "criteo-adtech-tracking.md",
        "content": """---
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
category: "AdTech & Behavioral Retargeting"
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
"""
    },
    {
        "filename": "carrefour-france-cookies.md",
        "content": """---
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
category: "Retail & e-Commerce"
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
"""
    },
    {
        "filename": "tim-telemarketing-italy.md",
        "content": """---
title: "TIM €27.8M Sanction: Italy's Garante Dismantles Mass Telemarketing Without Consent"
case_name: "Ordinanza Ingiunzione n. 9276559 (Telecom Italia S.p.A.)"
popular_name: "TIM €27.8M Telemarketing Landmark Fine"
dpa: "Garante per la protezione dei dati personali"
country: "Italy"
jurisdiction: "EU GDPR"
fine_amount: "€27,800,000"
fine_magnitude: "€27.8 Million"
decision_date: "2020-01-15"
year: 2020
articles_cited: ["Article 5", "Article 6", "Article 17", "Article 21"]
exam_domain: "Direct Marketing, Right to Object & Accountability (Articles 5, 6, 21)"
tldr: "Italy's Garante penalized telecom leader TIM €27.8 Million for millions of unlawful marketing calls, failing to manage opt-out registries, and retaining massive lead databases without consent."
is_top_5: false
category: "Telemarketing & Outbound Sales"
source_url: "https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9276559"
verified: true
---

## The Case at a Glance

In January 2020, the Italian Data Protection Authority (**Garante per la protezione dei dati personali**) delivered one of its most severe sanctions to date: a **€27,800,000** fine against telecommunications giant **TIM (Telecom Italia)**.

The Garante found that TIM had engaged in years of uncontrolled, aggressive outbound telemarketing campaigns, bombarding millions of Italian consumers with unwanted calls without consent, including individuals listed on the national Public Opt-Out Registry (*Registro delle Opposizioni*).

---

## How TIM Got Caught

The Garante received hundreds of individual citizen complaints and conducted extensive inspections at TIM facilities and partner call centers. The investigation uncovered:

1. **Millions of Unsolicited Calls**: Between 2017 and 2019, millions of promotional calls were placed to individuals who had never given consent, or who had explicitly withdrawn it. One single customer was called 155 times in a single month.
2. **Broken Blacklist Synchronisation**: TIM maintained fragmented internal blacklists. When a consumer told an agent to stop calling, that preference was recorded locally but never synced across TIM's central marketing CRM.
3. **Purchasing Non-Compliant Lead Lists**: TIM purchased vast lists of telephone numbers from third-party lead generation firms without verifying that the data subjects had consented to receive communications from telecommunications providers.
4. **App Privacy Violations**: TIM forced users of its "MyTIM" mobile customer portal to accept promotional profiling as a condition of accessing their monthly phone bills.

---

## Core Legal Violations

### 1. The Absolute Right to Object (Article 21(2))
Under GDPR Article 21(2), the right to object to direct marketing is absolute. Controllers have zero discretion to balance their legitimate commercial interests against the objection. When an objection is voiced, all promotional processing must halt immediately.

### 2. Accountability in Outsourcing (Article 5(2) & 24)
TIM attempted to shift blame to external call center agencies. The Garante rejected this unequivocally: controllers bear strict accountability for monitoring and auditing the third-party processors they hire to conduct sales.

---

## Recommendations for Compliance Officers

* **Centralize Suppression Lists**: Ensure customer opt-outs propagate in real-time across all sales channels, call centers, and affiliates.
* **Lead Generation Due Diligence**: Refuse third-party lead databases that cannot produce cryptographically verifiable proof of consent for your specific industry.
"""
    },
    {
        "filename": "enel-energia-italy-spam.md",
        "content": """---
title: "Enel Energia €26.5M Fine: Italy Punishes Rogue Telemarketing & Illicit Lead Generation"
case_name: "Ordinanza Ingiunzione n. 9723222 (Enel Energia S.p.A.)"
popular_name: "Enel Energia €26.5M Rogue Telemarketing Fine"
dpa: "Garante per la protezione dei dati personali"
country: "Italy"
jurisdiction: "EU GDPR"
fine_amount: "€26,500,000"
fine_magnitude: "€26.5 Million"
decision_date: "2021-11-11"
year: 2021
articles_cited: ["Article 5", "Article 6", "Article 24", "Article 32"]
exam_domain: "Processor Governance, Security & Lawful Processing (Articles 5, 24, 32)"
tldr: "Italy's Garante issued a €26.5M penalty against energy titan Enel Energia for acquiring new electricity contracts through an illicit network of subcontracted telemarketers who operated without oversight."
is_top_5: false
category: "Energy & Telemarketing"
source_url: "https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9723222"
verified: true
---

## The Case at a Glance

In November 2021, the Italian **Garante per la protezione dei dati personali** levied a monumental **€26,500,000** fine against Italy's leading electricity and gas supplier, **Enel Energia S.p.A.**

The penalty concluded an in-depth investigation into a pervasive "shadow telemarketing" phenomenon, where unregulated subcontracted call centers used pirated databases to aggressively pressure consumers into signing utility contracts.

---

## What Happened & How They Got Caught

Italian law enforcement (*Guardia di Finanza*) and Garante investigators conducted joint raids on call centers across Italy. They uncovered:

1. **Unregistered Subcontractors**: Enel Energia engaged primary marketing agencies, who then unlawfully subcontracted work to dozens of unauthorized call centers operating completely off the regulatory radar.
2. **Illicit Contact Lists**: These rogue agencies dialed phone numbers scraped from online classifieds, leaked customer registries, and unauthorized databases.
3. **Forged Consents**: When consumers signed up for electricity contracts over the phone under high-pressure sales tactics, call records and consent signatures were routinely falsified to earn agent commissions.
4. **Lack of Internal Auditing**: Enel Energia's internal systems failed to track the origin of the leads that generated millions of Euros in new energy contracts.

---

## Key Legal Findings

### 1. Inadequate Organizational & Technical Measures (Article 32)
Controllers must implement technical safeguards that prevent illicitly obtained data from entering corporate systems. Enel Energia accepted new contracts into its billing system without verifying that valid consent logs accompanied the customer IDs.

### 2. Controller Responsibility (Article 24)
A large enterprise cannot benefit commercially from contract acquisitions while remaining willfully blind to how those sales leads were procured. The Garante held Enel Energia directly accountable for failing to supervise its agency network.

---

## Practical Lessons for Enterprise Sales Teams

* **Enforce Subcontracting Bans**: Vendor agreements must strictly prohibit secondary outsourcing without prior written authorization from the primary controller.
* **Automated Lead Validation**: No outbound lead should be dialled without cryptographic timestamp verification proving that the citizen opted in.
"""
    },
    {
        "filename": "marriott-guest-reservation-breach.md",
        "content": """---
title: "Marriott £18.4M Fine: UK ICO Penalizes Negligent M&A Cybersecurity Due Diligence"
case_name: "Penalty Notice COM0783543 (Marriott International, Inc.)"
popular_name: "Marriott £18.4M Starwood Breach Decision"
dpa: "Information Commissioner's Office (ICO)"
country: "United Kingdom"
jurisdiction: "UK GDPR"
fine_amount: "£18,400,000"
fine_magnitude: "£18.4 Million"
decision_date: "2020-10-30"
year: 2020
articles_cited: ["Article 5", "Article 32"]
exam_domain: "Security of Processing & M&A Due Diligence (Article 32)"
tldr: "The UK ICO fined Marriott £18.4M after hackers compromised 339 million guest records via an undetected Starwood vulnerability inherited during a 2016 corporate acquisition."
is_top_5: false
category: "Cybersecurity & M&A Due Diligence"
source_url: "https://ico.org.uk/action-weve-taken/enforcement/marriott-international-inc/"
verified: true
---

## The Case at a Glance

In October 2020, the UK's **Information Commissioner's Office (ICO)** issued an **£18,400,000** fine against global hospitality leader **Marriott International, Inc.** The penalty resolved a massive data breach that exposed an estimated **339 million hotel guest records** globally, including roughly 7 million UK residents.

The decision established a critical international legal precedent: **corporate acquirers inherit the data protection liabilities and cybersecurity shortcomings of the companies they buy.**

---

## What Happened: The Starwood Legacy Breach

In 2014, an unknown threat group compromised the IT network of the Starwood hotel group by installing a remote access trojan (RAT) and memory-scraping malware.

In 2016, Marriott acquired Starwood for $13.6 billion. However, during the acquisition process:
1. **Inadequate Technical Due Diligence**: Marriott failed to perform an exhaustive, independent cybersecurity audit of Starwood's legacy database systems.
2. **Undetected Presence for 4 Years**: The attackers remained inside the Starwood guest reservation database for over four years, undetected, siphoning unencrypted passport numbers, credit card expiry dates, and travel itineraries.
3. **Flawed Access Controls**: The database contained unsegmented guest records, weak server administrator passwords, and unencrypted sensitive data fields.

The breach was only discovered in September 2018 when an automated database security alert was triggered—two years after Marriott completed the acquisition.

---

## Key Legal Findings Under GDPR Article 32

### 1. Multi-Factor Authentication & Account Monitoring
The ICO found that Marriott had failed to enforce multi-factor authentication (MFA) on critical administrative endpoints within the Starwood network, allowing attackers to move laterally with compromised service accounts.

### 2. Failure of Ongoing Database Encryption
Although credit card numbers were protected by encryption, the decryption keys were stored on the exact same server cluster, rendering the protection useless once the host was compromised.

---

## Strategic Takeaways for Executives & Privacy Architects

* **Cybersecurity Due Diligence is Mandatory in M&A**: Buyers must conduct deep forensic penetration tests and architecture reviews of target companies before completing acquisitions.
* **Separate Decryption Keys**: Never store private decryption keys in the same physical or logical environment as encrypted customer databases.
* **CIPP/E / CIPT Focus**: Article 32 requires security measures appropriate to risk. Storing hundreds of millions of passports without strict network segmentation is an automatic breach of duty.
"""
    },
    {
        "filename": "clearview-ai-facial-scraping.md",
        "content": """---
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
category: "Biometrics & Web Scraping"
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
"""
    }
]

for item in cases:
    fpath = cases_dir / item["filename"]
    fpath.write_text(item["content"].strip() + "\n", encoding="utf-8")
    print(f"Created case: {fpath.name}")

print(f"Finished writing {len(cases)} new case articles.")
