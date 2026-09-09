---
title: "Knuddels.de €20k Landmark Fine: Cleartext Password Breach & The Gold Standard of DPA Cooperation"
case_name: "Knuddels.de GmbH (LfDI Baden-Württemberg)"
popular_name: "Knuddels Cleartext Password Storage"
dpa: "LfDI Baden-Württemberg"
country: "Germany"
jurisdiction: "EU GDPR"
fine_amount: "€20,000"
fine_magnitude: "€20,000"
decision_date: "2018-11-21"
year: 2018
articles_cited: ["Article 32"]
exam_domain: "Credential Security & Cooperative Remediation (CIPP/E Domain IV / Article 32)"
tldr: "Baden-Württemberg's DPA issued Germany's very first GDPR fine (€20,000) against chat platform Knuddels.de after a data breach exposed 330,000 plaintext passwords, setting an international precedent for cooperative mitigation under Article 83(2)."
is_top_5: false
category: "cybersecurity-and-breaches"
source_url: "https://www.baden-wuerttemberg.datenschutz.de/lfdi-erteilt-erstes-ds-gvo-bussgeld-in-deutschland/"
verified: true
---

## At a Glance

* **The Offender:** Knuddels.de GmbH & Co. KG (one of Germany's longest-standing social gaming and online chat platforms, based in Ettlingen, Baden-Württemberg)
* **The Authority:** State Commissioner for Data Protection and Freedom of Information Baden-Württemberg (LfDI Baden-Württemberg, Dr. Stefan Brink)
* **The Penalty:** €20,000 (Germany's first-ever GDPR administrative fine)
* **The Core Issue:** Storing approximately 330,000 user passwords in plaintext without cryptographic hashing or salting, leading to mass credential exposure following a cyber intrusion.

---

## Executive Summary & TL;DR

In November 2018, just six months after the European Union's General Data Protection Regulation (GDPR) became directly enforceable, the State Commissioner for Data Protection and Freedom of Information of Baden-Württemberg (LfDI Baden-Württemberg) issued Germany's very first GDPR administrative fine: a penalty of **€20,000** against social chat platform Knuddels.de GmbH & Co. KG.

The enforcement action arose after external attackers compromised Knuddels' server infrastructure in July 2018, exfiltrating personal data belonging to approximately 1.87 million users—including roughly **330,000 user passwords stored in unencrypted, cleartext format**. The exfiltrated database was subsequently published online on public paste sites and file-sharing hubs in September 2018.

Despite the severe nature of the technical failure, the Knuddels decision achieved worldwide prominence as the definitive international benchmark for cooperative regulatory remediation. Instead of levying a business-destroying maximum fine, the supervisory authority explicitly rewarded Knuddels for its textbook incident response: reporting the breach within 24 hours under Article 33, transparently notifying all 1.87 million users under Article 34, engaging independent forensic investigators, and completely overhauling its cryptographic architecture within seven weeks. The case established that open, proactive cooperation with data protection authorities serves as a decisive mitigating factor under **Article 83(2) GDPR**.

---

## Factual Background & Investigation Details

### The Knuddels Platform and Community

Founded in 1999 in Ettlingen, Germany, Knuddels.de developed into one of the country's most prominent and enduring digital communities. Designed around themed chat rooms, casual multiplayer games, and virtual avatars, the platform served millions of German-speaking users, including a substantial proportion of teenagers and young adults.

Over nearly two decades of continuous operation, Knuddels accumulated massive user databases. While the company progressively upgraded its primary authentication systems to incorporate password hashing, legacy technical debt remained:
* **The Legacy Credential Store:** A historical backend database table containing roughly **330,000 user accounts** retained passwords in cleartext without cryptographic salts or hashing algorithms.
* **The Active Database:** Modern user accounts incorporated password hashes, but legacy user credentials had never been forced into a mandatory re-hashing cycle upon login.

### The Cyber Intrusion and Public Leak

In **July 2018**, malicious actors exploited a vulnerability in Knuddels' web server infrastructure to gain unauthorized access to its internal databases. The attackers exfiltrated:
* Approximately 1.87 million user profile records, containing usernames, email addresses, and account registration metadata.
* Real names and physical addresses of approximately 8,000 users.
* Roughly 330,000 user passwords stored in plain, human-readable text.

In **September 2018**, the attackers leaked the stolen data onto public paste platforms and Mega file-sharing links. Security researchers and journalists quickly discovered the repository and alerted the company.

### The Gold Standard of Incident Response

Upon verifying the authenticity of the data leak on **September 7, 2018**, Knuddels management executed an exemplary incident response playbook that remains a case study in crisis management:

1. **Immediate Regulatory Reporting (Article 33 GDPR):** On **September 8, 2018**—well inside the mandatory 72-hour notification deadline—Knuddels formally notified the LfDI Baden-Württemberg of the data breach, disclosing the full scope of exposed records and the existence of plaintext passwords.
2. **Transparent User Communication (Article 34 GDPR):** Knuddels proactively notified all 1.87 million registered users via direct email and prominent on-platform alerts. The company provided clear, plain-language explanations of what had occurred, warned users about password reuse across other online services, and forcefully invalidated all active session cookies and user passwords.
3. **Independent Forensic Engagement:** Knuddels immediately engaged external cybersecurity specialists and digital forensics investigators to isolate the breached server, audit all backend codebases, and patch the exploited entry vector.
4. **Complete Cryptographic Modernization in 7 Weeks:** Working in daily, transparent coordination with the LfDI's technical audit team, Knuddels completely re-engineered its security stack:
   * Migrated all user credentials to modern, salted cryptographic hashing (utilizing memory-hard algorithms).
   * Implemented multi-factor authentication (2FA) options for user accounts.
   * Enforced TLS 1.3 encryption across all internal and external database connections.
   * Introduced microsegmentation and strict role-based access controls across backend server clusters.

### The Regulatory Sanction: Proportionality Over Punitive Destruction

On **November 21, 2018**, Baden-Württemberg Data Protection Commissioner Dr. Stefan Brink announced the final enforcement decision: an administrative fine of **€20,000**, accompanied by separate administrative costs of approximately €8,000.

In an official statement that defined modern European enforcement philosophy, Dr. Brink explained that the supervisory authority's statutory duty is to enforce compliance and improve security, not to destroy cooperative enterprises:
> *"The LfDI is not interested in entering into a competition for the highest possible fines. The primary objective is to make data processing safer. Knuddels showed exemplary transparency and cooperated with us completely. Companies that take data protection seriously and make major security investments following a breach should not be punished with disproportionate fines that threaten their economic existence."*

---

## Core Legal Violations

The Knuddels decision firmly established the legal and technical baseline for state-of-the-art credential storage under the GDPR:

### 1. Article 32(1)(a) GDPR — Breach of Security of Processing (Encryption & Pseudonymisation)

Article 32(1)(a) GDPR requires controllers to implement technical and organizational measures appropriate to the risk, specifically highlighting **"the pseudonymisation and encryption of personal data."**

In evaluating Knuddels' password storage:
* **Plaintext Storage is Per Se Unlawful:** The supervisory authority ruled that storing user passwords in plaintext, cleartext, or unencrypted form is an objective, inexcusable failure to meet the state of the art (*Stand der Technik*).
* **Foreseeability of Credential Theft:** Storing cleartext passwords creates catastrophic risks for data subjects due to credential stuffing—attackers routinely use leaked email/password pairs to compromise victims' banking, shopping, and social media accounts across the internet.
* **Duty to Salt and Hash:** Under Article 32, passwords must undergo secure, one-way cryptographic hashing utilizing unique cryptographic salts and computationally expensive, memory-hard key derivation functions (such as Argon2id, bcrypt, or PBKDF2) to resist offline dictionary and rainbow-table attacks.

### 2. Article 5(1)(f) GDPR — Violation of Integrity and Confidentiality

Personal data must be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage, using appropriate technical or organizational measures.

By maintaining 330,000 user passwords in human-readable text on production databases, Knuddels failed to safeguard the fundamental confidentiality of its users' authentication credentials.

### 3. Article 83(2) GDPR — Decisive Statutory Mitigating Factors

The €20,000 fine demonstrated the profound impact of the mitigating criteria enumerated in Article 83(2) GDPR:
* **Article 83(2)(c) (Actions Taken to Mitigate Damage):** Knuddels immediately invalidated all passwords and forced user resets, completely neutralizing the active threat of account takeovers on its platform.
* **Article 83(2)(f) (Degree of Cooperation):** Knuddels exhibited voluntary, unreserved cooperation, opening its server architecture and forensic reports to the LfDI technical investigators.
* **Article 83(2)(h) (Manner in Which Infringement Became Known):** Knuddels proactively self-reported the breach under Article 33 rather than attempting to conceal it or waiting for regulatory discovery.
* **Article 83(2)(k) (Financial Capacity and Investments):** Knuddels demonstrated that it had committed substantial financial resources to overhaul its cybersecurity infrastructure, which the DPA factored in to avoid threatening the company's financial solvency.

---

## Practical Takeaways & Compliance Checklist

The Knuddels case is the global canonical model for credential security architecture, breach response workflows, and regulatory engagement strategy.

### For Software Engineers & Backend Architects

- [ ] **Enforce Modern Cryptographic Password Hashing:** Never store plaintext passwords or use obsolete hash functions (MD5, SHA-1, or unsalted SHA-256). Implement modern, adaptive, memory-hard key derivation algorithms: **Argon2id** (recommended), **bcrypt** (work factor $\ge$ 12), or **scrypt**.
- [ ] **Implement Cryptographic Salt Generation:** Generate a cryptographically secure, unique pseudo-random salt (minimum 16 bytes) for every individual password before hashing to defeat precomputed rainbow tables.
- [ ] **Eradicate Legacy Credential Debt:** When upgrading hashing algorithms, implement automated password migration: re-hash credentials using the modern algorithm upon the user's next successful login, and force password resets for dormant accounts.
- [ ] **Screen Against Breached Passwords:** Integrate breached credential detection into registration and password change forms (e.g., querying the *Have I Been Pwned* k-Anonymity API) to prevent users from selecting known compromised passwords.

### For DPOs, Incident Responders & Executive Leadership

- [ ] **Master the 72-Hour Article 33 Reporting Workflow:** Establish tested incident response playbooks. Report data breaches to the competent supervisory authority within 72 hours of becoming aware of the incident, providing initial facts and committing to phased updates.
- [ ] **Prioritize Transparent User Notifications (Article 34):** When a breach presents a high risk to individuals (such as exposed credentials), notify users immediately in plain, direct language. Avoid evasive PR euphemisms like "unauthorized data access" when cleartext credentials were leaked.
- [ ] **Invalidate Sessions & Force Password Resets Immediately:** In any credential breach, immediately revoke all active JSON Web Tokens (JWTs), session cookies, and API keys. Require a password reset verified via an out-of-band email or SMS link.
- [ ] **Adopt a Cooperative Posture with Regulators:** Treat data protection authorities as public safety partners during an incident. Complete architectural transparency, rapid forensic sharing, and concrete capital investments in security directly unlock Article 83(2) statutory fine mitigations.
