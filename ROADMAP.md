# ROADMAP.md — PrivacyLawForAll Strategic Vision & Backlog

> **Vision:** The comprehensive, open-access, plain-English encyclopedia of global privacy law and AI regulation.

---

## 1. Immediate Next Milestone: The DPIA Studio (`/mock-dpia` / `/dpia`)
**Status:** In Progress (Execution scheduled next session)  
**Goal:** Launch a complete interactive Data Protection Impact Assessment (DPIA) laboratory under GDPR Article 35.

### Key Components:
- **Interactive DPIA Assessment Wizard:**
  - Article 35(3) mandatory screening (systematic profiling, special category data on large scale, public systematic monitoring).
  - EDPB Guidelines 248/17 9-criteria risk threshold engine.
  - Step-by-step risk mitigation and technical safeguards planner (encryption, pseudonymization, data minimization, retention caps).
  - DPO recommendation and residual risk sign-off workflow.
- **Pre-Built Counterfactual DPIA Dossiers:**
  - Pre-engineered, publication-grade DPIA dossier breakdowns for landmark fined systems:
    1. *Meta Cross-Border Data Transfers* (FISA 702 risk, SCC supplementary measures).
    2. *Google France Cookie Tracking* (Asymmetry of effort, refusal dark patterns).
    3. *H&M Nuremberg Employee Surveillance* (Special category health/religious data, § 26 BDSG).
    4. *Deutsche Wohnen Rental Archives* (Automated archiving, deletion concept *Löschkonzept*).
    5. *Criteo Behavioral AdTech* (Identity resolution, vendor consent passthrough).
- **Navigation & Aliasing:**
  - First-class link in `Header.astro` ("DPIA Studio").
  - URL alias redirect in `astro.config.mjs`: `/dpia` -> `/mock-dpia`.

---

## 2. Near-Term Feature Backlog

### A. Landmark Cases Expansion (Target: 30+ Landmark Cases)
- **Clearview AI Biometrics:** Landmark bans and fines across France, Italy, Greece, and the UK for facial recognition scraping without consent.
- **Amazon Luxembourg (€746M):** Targeted behavioral advertising and profiling algorithm violation.
- **Meta Behavioral Advertising Fines (€390M):** The death of the "contractual necessity" lawful basis for targeted ads.

### B. United States & California Privacy Hubs (CCPA / CPRA & PRA)
- **California Regional Hub (`/privacy/california`):** Explaining CCPA / CPRA consumer rights (Do Not Sell/Share, Right to Limit Sensitive Data, Opt-Out Preference Signals / GPC).
- **US Federal & FTC Enforcement Hub (`/privacy/us-ftc`):** Section 5 unfair/deceptive practices, health data breaches (GoodRx, BetterHelp), and COPPA child privacy.
- **US Privacy Risk Assessment (PRA) Studio:** Leveraging `pra-mcp` for statutory risk assessments under CPRA § 1798.185(a)(15) and FTC consent order frameworks.

### C. Searchable Enforcement Tracker (`/tracker`)
- Upgrade `/top-5` into a client-side searchable, filterable enforcement directory across all 84,000+ scraped regulatory records.
- Instant search by company name, issuing DPA, statutory article, or fine range.

### D. Exportable Compliance Dossiers
- Enable one-click export of DPIA drafts and case briefing summaries into print-ready PDF and Markdown format for DPOs, consultants, and law students.

---

## 3. Medium-to-Long-Term Regulatory Roadmap

### A. EU AI Act Rollout (2026 – 2028)
- Comprehensive interactive compliance checker for AI Deployers and Providers.
- Prohibited Practices guide (Article 5: social scoring, cognitive manipulation, untargeted facial scraping).
- High-Risk AI obligations (Article 6 & Annex III: fundamental rights impact assessments, data governance, logging).

### B. India DPDPA Full Implementation (2026 – 2027)
- Expansion of the DPDPA hub as the Digital Personal Data Protection Board and implementation rules are officially notified.
- Consent Manager framework, Significant Data Fiduciary (SDF) obligations, and child consent mechanisms.

### C. Custom Domain Acquisition & Public Launch
- Secure custom domain (`privacylawforall.com` / `privacylaw.free`).
- Strategy for public launch on Reddit (r/privacy, r/gdpr, r/webdev, r/sysadmin), Hacker News Show HN, and LinkedIn privacy communities.
