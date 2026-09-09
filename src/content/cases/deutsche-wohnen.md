---
title: "Deutsche Wohnen €14.5M Fine: The Landmark Precedent on Archival Data Retention & Corporate Liability"
case_name: "Deutsche Wohnen SE (BlnBDI)"
popular_name: "Deutsche Wohnen Structural Data Retention"
dpa: "BlnBDI (Berlin)"
country: "Germany"
jurisdiction: "EU GDPR"
fine_amount: "€14,500,000"
fine_magnitude: "€14.5 Million"
decision_date: "2019-11-05"
year: 2019
articles_cited: ["Article 5", "Article 25"]
exam_domain: "Data Protection by Design & Storage Limitation (CIPP/E Domain II / Article 25)"
tldr: "Berlin's DPA fined housing giant Deutsche Wohnen €14.5M for storing tenant financial, social security, and health records indefinitely in an electronic archive system lacking an automated deletion concept, sparking the historic CJEU C-807/21 ruling on corporate liability."
is_top_5: false
category: "transparency-and-notice"
source_url: "https://www.datenschutz-berlin.de/infothek-und-service/pressemitteilungen/detail/berliner-beauftragte-fuer-datenschutz-und-informationsfreiheit-verhaengt-bussgeld-gegen-deutsche-wohnen-se"
verified: true
---

## At a Glance

* **The Offender:** Deutsche Wohnen SE (one of Germany's largest private real estate holding companies, managing over 160,000 residential units)
* **The Authority:** Berlin Commissioner for Data Protection and Freedom of Information (BlnBDI, Maja Smoltczyk)
* **The Penalty:** €14,500,000 (€14.5 Million)
* **The Core Issue:** Maintaining a legacy corporate electronic archiving system without an automated deletion concept (*Löschkonzept*), storing tenant financial, medical, and personal documents indefinitely in violation of Storage Limitation and Privacy by Design.

---

## Executive Summary & TL;DR

In November 2019, the Berlin Commissioner for Data Protection and Freedom of Information (BlnBDI) imposed an administrative fine of **€14,500,000** against Deutsche Wohnen SE. The enforcement action became one of the most consequential in European legal history: it established that keeping personal data indefinitely in an electronic archive without automated deletion capabilities directly breaches the GDPR, even in the complete absence of a data breach or external hacker intrusion.

The supervisory authority found that Deutsche Wohnen utilized an enterprise resource planning (ERP) archiving database that functioned as an append-only digital warehouse. Personal records of hundreds of thousands of tenants—including payslips, self-disclosure questionnaires, bank account statements, tax filings, social security records, and health certificates—were retained permanently. The software architecture provided no technical mechanism to filter expired documents, distinguish active tenants from former tenants, or execute automated purges.

Deutsche Wohnen challenged the fine in German criminal and administrative courts, arguing that German misdemeanor law (*§ 30 OWiG*) prohibited fining a legal entity unless the authorities could prove that a specific, identified natural executive had committed the offense. This defense sparked a four-year judicial battle that escalated to the Grand Chamber of the Court of Justice of the European Union (CJEU). In its landmark judgment in **Case C-807/21 (December 2023)**, the CJEU definitively ruled that corporations can be held directly liable for GDPR administrative fines without proving the personal fault of an individual corporate director, importing the European antitrust undertaking principle directly into data protection enforcement.

---

## Factual Background & Investigation Details

### The Archival Architecture of a Real Estate Behemoth

Deutsche Wohnen SE is a major publicly traded European real estate company. At the time of the investigation, it managed an extensive commercial and residential portfolio comprising more than 160,000 residential apartments, primarily in Berlin and other German metropolitan areas.

To manage its vast tenant base, Deutsche Wohnen deployed a centralized electronic archiving system embedded within its SAP ERP landscape. Whenever prospective tenants applied for housing or existing tenants signed leases, submitted maintenance requests, or contested utility bills, company staff scanned and uploaded their documentation into this system:

* **Financial & Economic Profiles:** Monthly pay stubs, bank statements showing transactional histories, credit agency scoring extracts (SCHUFA), tax assessment notices, and employer verification letters.
* **Social & Family Records:** Marriage certificates, child custody decrees, social security and housing benefit (*Wohngeld*) entitlement certificates.
* **Special Category & Health Data:** Medical disability certificates provided to justify accessibility modifications, proof of illness for lease transfers, and religious identity declarations extracted from historical tax cards.

### The Architectural Defect: Storing Everything Indefinitely

During normal operations, landlords are legally permitted to process tenant data to evaluate creditworthiness before lease signing and to execute the lease agreement. Once a tenancy concludes, certain records must be retained temporarily to defend against potential civil claims (e.g., security deposit disputes subject to a 3-year statutory limitation under the German Civil Code, *BGB § 195*) or to satisfy fiscal and commercial accounting obligations (6 to 10 years under *HGB § 257* and *AO § 147*).

However, Deutsche Wohnen's archiving infrastructure possessed a fatal technical limitation:
1. **No Granular Deletion Function:** The software could not execute selective deletions based on individual document types, tenant IDs, or date thresholds.
2. **No Data Segregation:** Documents whose processing purpose had ended remained in the active production database, accessible to leasing agents and administrative staff alongside current tenant files.
3. **Infinite Retention by Default:** Personal data of tenants who had vacated apartments years or even decades earlier remained stored in plain text, indefinitely retrievable.

### The Regulatory Audits (2017–2019)

The Berlin Data Protection Authority first identified these structural deficiencies during an on-site audit in **June 2017**, under the pre-GDPR Federal Data Protection Act. The BlnBDI explicitly notified Deutsche Wohnen that its electronic archiving system violated data protection principles and formally advised the company to implement a comprehensive technical deletion concept (*Löschkonzept*) before the GDPR became enforceable on May 25, 2018.

In **March 2019**, the BlnBDI conducted a comprehensive follow-up inspection to determine whether Deutsche Wohnen had remedied the situation. The audit revealed that:
* The company had still not implemented any automated deletion routine or segregated archival storage.
* Deutsche Wohnen claimed it had commenced planning a software migration, but cited technical complexity, system dependencies, and high implementation costs as reasons for the continued non-compliance.
* In practice, the system continued to accumulate and retain the personal data of tens of thousands of former tenants without legal basis.

Concluding that Deutsche Wohnen had knowingly maintained a non-compliant data processing system for nearly two years after the initial regulatory warning, Berlin Data Protection Commissioner Maja Smoltczyk issued the €14.5M fine on November 5, 2019.

### The Procedural Saga & Historic CJEU Grand Chamber Ruling (C-807/21)

Deutsche Wohnen filed an objection against the administrative penalty notice (*Bußgeldbescheid*), bringing the case before the Regional Court of Berlin (*Landgericht Berlin*).

1. **The Landgericht Berlin Dismissal (February 2021):** The regional court terminated the fine proceedings (order of 18 February 2021, 526 OWiLG 212 Js-OWi 1/20). The court held that under Section 30 of the German Administrative Offences Act (*Gesetz über Ordnungswidrigkeiten - OWiG*), an administrative fine can only be levied against a corporate entity if an identified natural person in a leadership or executive role committed a proven infraction. Because the BlnBDI had fined the corporate legal person directly without establishing individual managerial culpability, the court declared the fine notice invalid.
2. **The Referral to Luxembourg:** The Berlin Public Prosecutor appealed to the Berlin Court of Appeal (*Kammergericht Berlin*), which recognized a fundamental conflict between German national misdemeanor jurisprudence and the autonomous enforcement doctrine of EU law. The Kammergericht stayed proceedings and referred preliminary questions to the CJEU under Article 267 TFEU.
3. **CJEU Judgment C-807/21 (5 December 2023):** In a historic Grand Chamber decision, the European Court of Justice completely rejected the German court's theory:
   * **Direct Corporate Liability:** The CJEU ruled that GDPR Articles 4(7), 58, and 83 must be interpreted as meaning that an administrative fine can be imposed directly on a legal person (the "undertaking" within the meaning of Articles 101 and 102 TFEU) for an infringement committed by its operations, **without requiring prior attribution to an identified natural person**.
   * **The Mental Element (Intent or Negligence):** An undertaking can be sanctioned whenever the infringement was committed intentionally or negligently—which is satisfied when the enterprise could not have been unaware of the anti-competitive or infringing nature of its data processing operations.

---

## Core Legal Violations

The Deutsche Wohnen decision serves as the premier European legal authority on data retention limits and structural privacy engineering:

### 1. Article 5(1)(e) GDPR — Breach of Storage Limitation

Personal data must be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed.

Deutsche Wohnen fundamentally violated this principle by preserving tenant financial dossiers indefinitely:
* Once a tenancy agreement terminates and the security deposit is accounted for, the primary contractual purpose under Article 6(1)(b) expires.
* While certain accounting records must be kept to satisfy statutory tax obligations, such obligations do not justify retaining an entire tenant file (such as intimate salary statements, credit bureau scores, or copies of medical certificates).
* Maintaining personal data indefinitely on the speculative possibility that it might be helpful in future unasserted legal claims violates the proportionality required by Article 5(1)(e).

### 2. Article 25(1) GDPR — Failure of Data Protection by Design and by Default

Under Article 25(1) GDPR, the controller must, both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and organizational measures (such as pseudonymisation and automated deletion mechanisms) designed to implement data protection principles effectively.

The BlnBDI's enforcement confirmed that Article 25(1) imposes an affirmative, proactive engineering duty:
* A data controller cannot deploy or operate software that physically lacks the capacity to comply with GDPR principles.
* Deploying an archiving system that possesses no deletion interface, no automated data expiration timers, and no ability to segregate expired records is an inherent, ongoing violation of Privacy by Design.
* Commercial inconvenience, legacy software debt, or licensing costs do not exempt an organization from its statutory duty to engineer systems capable of timely data disposal.

### 3. Article 5(2) GDPR — Violation of the Accountability Principle

Article 5(2) places the burden of proof squarely upon the controller to demonstrate compliance with the data protection principles outlined in Article 5(1).

Because Deutsche Wohnen could neither present a documented deletion concept (*Löschkonzept*) nor demonstrate that expired records were being purged or anonymized in practice, it committed a standalone breach of its accountability obligations.

---

## Practical Takeaways & Compliance Checklist

The Deutsche Wohnen case is a mandatory case study for data architects, ERP administrators, enterprise engineering leads, and Data Protection Officers.

### For Enterprise Software Engineers & Database Architects

- [ ] **Implement Programmatic Deletion APIs:** Ensure every database and document storage repository (AWS S3, Azure Blob, SharePoint, SAP, relational databases) supports automated, granular programmatic deletion based on record type and tenant identifier.
- [ ] **Enforce Automated Time-to-Live (TTL) & Retention Rules:** Configure automated retention policies that automatically transition records from active hot storage to restricted legal archives, and trigger cryptographic shredding or permanent deletion upon expiration.
- [ ] **Architect Storage Segregation:** Decouple operational production databases from statutory compliance archives. Once a customer relationship ends, move required tax documents to restricted, access-controlled archival stores and permanently purge all non-essential personal data.
- [ ] **Prohibit Append-Only Architecture for Personal Data:** Eliminate immutable, append-only designs (including improper blockchain or non-deletable document archives) for personal data unless a statutory exemption explicitly mandates non-alteration.

### For DPOs, Legal Counsel & Records Managers

- [ ] **Establish a Formal DIN 66398 Deletion Concept (*Löschkonzept*):** Document standard retention classes across all corporate data categories. Clearly define retention triggers (e.g., termination of contract), statutory retention periods, and maximum deletion deadlines.
- [ ] **Differentiate Tax/Commercial Retention from General PII:** Distinguish invoices and tax-relevant payment vouchers (retained for 6 to 10 years under commercial law) from supporting personal documents such as credit checks, payslips, and applicant CVs (which must be purged within months of lease execution or applicant rejection).
- [ ] **Eliminate "Technical Burden" as a Compliance Strategy:** Documented system migrations must include concrete interim safeguards, manual purging schedules, and firm completion deadlines. DPAs will not tolerate multi-year inaction masked as "in-progress migration."
- [ ] **Align Enterprise Risk Models with CJEU C-807/21:** Recognize that European regulators can fine the corporate parent directly based on consolidated global turnover. Enterprise risk models must treat archival data debt as a top-tier balance sheet liability.
