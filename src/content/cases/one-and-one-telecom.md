---
title: "1&1 Telecom €9.55M Fine: How Weak Call Center Authentication Breached Article 32 Security"
case_name: "1&1 Telecom GmbH (BfDI)"
popular_name: "1&1 Telecom Call Center Authentication"
dpa: "BfDI (Federal)"
country: "Germany"
jurisdiction: "EU GDPR"
fine_amount: "€9,550,000"
fine_magnitude: "€9.55M (Reduced to €900k)"
decision_date: "2019-12-09"
year: 2019
articles_cited: ["Article 32"]
exam_domain: "Authentication Architecture & Call Center Security (CIPP/E Domain IV / Article 32)"
tldr: "Germany's Federal Commissioner (BfDI) fined 1&1 Telecom €9.55M after finding call center agents disclosed full customer account details to anyone who merely provided the customer's name and birth date, a penalty later reduced to €900k by the Bonn Regional Court."
is_top_5: false
category: "cybersecurity-and-breaches"
source_url: "https://www.bfdi.bund.de/SharedDocs/Pressemitteilungen/DE/2019/27_Bussgeld-1und1.html"
verified: true
---

## At a Glance

* **The Offender:** 1&1 Telecom GmbH (a leading German telecommunications provider, subsidiary of United Internet AG)
* **The Authority:** Federal Commissioner for Data Protection and Freedom of Information (BfDI, Ulrich Kelber) / Regional Court of Bonn (*Landgericht Bonn*)
* **The Penalty:** €9,550,000 originally imposed by BfDI; reduced on judicial appeal to €900,000 by LG Bonn (Case 29 OWi 1/20)
* **The Core Issue:** Inadequate customer authentication in customer service call centers, relying solely on publicly discoverable identifiers (name and date of birth) without secondary authentication factors.

---

## Executive Summary & TL;DR

In December 2019, Germany's Federal Commissioner for Data Protection and Freedom of Information (BfDI), Ulrich Kelber, announced a major administrative fine of **€9,550,000** against 1&1 Telecom GmbH. The penalty was the first multi-million euro enforcement action levied by the German federal privacy regulator under the GDPR, sending shockwaves through the telecommunications and financial services sectors.

The investigation originated from a serious real-world stalking incident. An estranged former partner called 1&1 customer support, provided the victim's name and date of birth, and was readily given the victim's new, unlisted mobile telephone number and updated contract details. A regulatory inquiry revealed that 1&1's standard operating procedure across all inbound customer support hotlines required agents to authenticate callers using only two basic data points: the customer's full name and their date of birth. Callers were never required to provide a secret PIN, contract password, customer ID, or one-time verification token.

1&1 appealed the fine to the Regional Court of Bonn (*Landgericht Bonn*, judgment of November 11, 2020, 29 OWi 1/20). In a pivotal judgment for European cybersecurity jurisprudence, the court upheld the BfDI's finding that single-factor authentication based on public knowledge constitutes an objective breach of **Article 32 GDPR (Security of Processing)**. However, the court drastically slashed the fine by over 90% to **€900,000**, establishing that prompt remediation, immediate roll-out of multi-factor PIN systems, and complete transparency with the supervisory authority provide powerful statutory mitigation under Article 83(2) GDPR.

---

## Factual Background & Investigation Details

### The Scale of 1&1 Customer Service Operations

1&1 Telecom GmbH is one of Germany's largest telecommunications operators, providing DSL broadband, fiber connectivity, mobile phone services, and web hosting to millions of private consumers and commercial enterprises.

To manage high call volumes across its national customer base, 1&1 operated extensive internal and outsourced customer service call centers handling tens of thousands of inbound calls every day. Customer service representatives possessed broad read and write access to centralized customer relationship management (CRM) portals containing:
* Contract details, active services, tariffs, and monthly invoices.
* Home addresses, billing addresses, and bank account numbers (IBAN).
* Itemized call records (*Einzelverbindungsnachweise*), connection metadata, and unlisted mobile telephone numbers.

### The Authentication Architecture Flaw

For years prior to the GDPR, 1&1 customer service workflows prioritized speed and friction-free customer experiences:
* **The Standard Verification Protocol:** When a customer dialed customer support, the call center agent asked only two verification questions: *"May I have your first and last name?"* and *"What is your date of birth?"*
* **No Secret Knowledge Factor:** Callers were never asked for a secret security phrase, a contract password, a customer account number, or a dynamic verification code sent via SMS.
* **Public Nature of the Identifiers:** As the BfDI emphasized, a person's full name and date of birth are semi-public data points. They are routinely shared with employers, displayed on social media profiles (LinkedIn, Facebook, Instagram), visible on commercial register filings, or discoverable through casual social engineering.

### The Stalking Incident and Regulatory Escalation

The severe vulnerability of this verification workflow became apparent when an individual seeking to locate an ex-partner dialed 1&1 customer support. By providing the victim's name and date of birth, the caller successfully impersonated the subscriber. 

The support agent promptly disclosed the victim's confidential, unlisted mobile phone number and confirmed her new residence address. The caller subsequently used this information to stalk and harass the victim.

The victim filed an urgent complaint with the Federal Commissioner for Data Protection and Freedom of Information (BfDI), which exercises federal jurisdiction over telecommunications providers in Germany.

BfDI Commissioner Ulrich Kelber initiated a comprehensive security audit of 1&1's customer support operations:
1. **Systemic Vulnerability:** The BfDI established that the weak authentication protocol was not an isolated error by a rogue agent, but the official, documented corporate guideline applied to the entire customer base.
2. **Failure of State-of-the-Art Safeguards:** The regulator determined that telecommunications data is highly sensitive and subject to statutory telecommunications secrecy. Allowing access to account records without verifying a secret knowledge factor breached the state-of-the-art security obligations of Article 32 GDPR.
3. **The €9.55M Fine Calculation:** On December 9, 2019, the BfDI issued a €9.55M fine. The penalty was calculated using the German Data Protection Conference's (DSK) standardized fine model, which heavily weighted the consolidated global annual turnover of 1&1's corporate parent, United Internet AG (over €5 billion).

### The Bonn Regional Court Appeal (LG Bonn 29 OWi 1/20)

1&1 appealed the penalty notice to the Regional Court of Bonn (*Landgericht Bonn*). The resulting trial represented the first extensive judicial review of a GDPR administrative fine in Germany:

1. **Confirmation of the Infringement:** The court unequivocally agreed with the BfDI that 1&1 had infringed Article 32(1) GDPR. The court ruled that authenticating callers solely through name and birth date created an unacceptable risk of unauthorized disclosure to third parties and social engineers.
2. **Rejection of the DSK Fine Model as Binding:** The court affirmed that the DSK's turnover-driven fine calculation model is merely non-binding administrative guidance. Courts must independently evaluate the individual culpability and proportionality of the sanction.
3. **Slashing the Penalty to €900,000:** The court reduced the fine from €9.55 million to €900,000, identifying significant mitigating circumstances under Article 83(2) GDPR:
   * **Negligence Rather Than Intent:** 1&1 had not acted deliberately to cut security costs; the protocol was a legacy workflow maintained in good faith.
   * **Isolated Verified Damage:** Beyond the initial stalking complaint, there was no evidence of widespread, systematic fraudulent data harvesting by third parties.
   * **Exemplary Cooperation:** 1&1 cooperated transparently with the BfDI from the first day of the inquiry.
   * **Immediate Technical Remediation:** Within weeks of the BfDI's notice, 1&1 designed and rolled out a mandatory multi-factor customer service PIN across all call centers, significantly elevating the security posture of the German telecommunications industry.

---

## Core Legal Violations

The 1&1 Telecom decision is the foundational European precedent governing call center cybersecurity and remote customer authentication:

### 1. Article 32(1) GDPR — Breach of Security of Processing

Article 32(1) GDPR mandates that controllers implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk. This requires ensuring the ongoing confidentiality, integrity, availability, and resilience of processing systems.

In evaluating authentication systems under Article 32:
* **The Role of Risk Assessment:** Telecommunications providers process sensitive communication metadata, unlisted phone numbers, and banking details. The risk of unauthorized disclosure is high, demanding robust authentication controls.
* **Failure of Single-Factor Public Identifiers:** A valid authentication mechanism must verify identity through at least one piece of secret information known only to the authorized user (something you know, something you have, or something you are). Relying solely on public or semi-public identifiers fails to provide an appropriate level of security against trivial social engineering attacks.

### 2. Article 5(1)(f) GDPR — Violation of Integrity and Confidentiality

Personal data must be processed in a manner that ensures appropriate security, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage.

By designing customer service workflows that permitted unauthorized third parties to query subscriber databases upon presenting public knowledge, 1&1 failed to safeguard the confidentiality of its subscribers' personal data.

### 3. German Telecommunications Law & Secrecy

Under the German Telecommunications Act (*Telekommunikationsgesetz - TKG*) and the Telecommunications-Telemedia Data Protection Act (*TDDDG*), telecommunications providers are bound by statutory telecommunications secrecy (*Fernmeldegeheimnis*, Article 10 of the German Basic Law). 

Telecommunications providers are legally obligated to maintain heightened technical safeguards to prevent subscriber telephone numbers and connection records from falling into unauthorized hands.

### 4. Article 83(2) GDPR — Judicial Sentencing and Mitigation Precedent

The Bonn Regional Court's judgment established a key benchmark for applying the statutory sentencing factors under Article 83(2) GDPR:
* **Article 83(2)(a) (Gravity of Infringement):** An architectural vulnerability affecting millions is serious, but absence of financial exploitation or widespread harm tempers severity.
* **Article 83(2)(b) (Intent vs. Negligence):** Gross negligence can be heavily mitigated if an enterprise promptly remedies the underlying defect.
* **Article 83(2)(c) & (f) (Action to Mitigate & Cooperation):** Swift, proactive deployment of robust security measures (such as the 1&1 service PIN) and complete cooperation with the regulator can justify a dramatic reduction in administrative sanctions.

---

## Practical Takeaways & Compliance Checklist

The 1&1 decision permanently altered customer support operations, authentication architecture, and vendor security protocols across the telecommunications, banking, and e-commerce industries.

### For Call Center Architects & Identity Engineers

- [ ] **Eliminate Public Identifiers as Authentication Factors:** Never authenticate users by asking for names, dates of birth, postal addresses, or email addresses. These are routing attributes, not authentication secrets.
- [ ] **Implement Dedicated Support PINs:** Provide customers with a customer-selected, salted, and hashed 5-to-6-digit Customer Service PIN in their secure account portal. Require callers to provide this PIN before any account details are revealed.
- [ ] **Deploy Out-of-Band Verification (Push / OTP):** When callers cannot remember their service PIN, trigger an out-of-band verification challenge: send a temporary one-time password (OTP) via SMS, authenticated mobile app push notification, or email to the verified contact method on file.
- [ ] **Mask Sensitive Fields in Agent CRM Interfaces:** Redact unlisted telephone numbers, full IBANs, and itemized billing logs in call center dashboards until the caller's identity has been programmatically validated through the interactive voice response (IVR) or cryptographic PIN verification.

### For DPOs, Legal Counsel & Customer Operations Leads

- [ ] **Establish High-Risk Account Flagging for Domestic Abuse & Stalking Victims:** Create specialized handling protocols for vulnerable customers. High-risk profiles should require strict multi-party authorization or in-person identity verification before any contact information can be updated or disclosed.
- [ ] **Audit Third-Party Call Center Vendors:** Extend authentication standards to external, outsourced customer support agencies through binding Data Processing Agreements (DPAs under Article 28) and regular mystery-caller penetration tests.
- [ ] **Conduct Social Engineering Training for Support Staff:** Train agents to recognize social engineering pretexts: callers claiming emergencies, pretending to be distracted spouses, or pressuring agents to bypass security protocols.
- [ ] **Document Remediation Speed for Regulatory Mitigation:** In the event of a security investigation, prepare an immediate technical remediation plan. As established by LG Bonn, rapid deployment of enhanced security safeguards can reduce potential GDPR fines by over 90%.
