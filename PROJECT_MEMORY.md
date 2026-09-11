# PROJECT_MEMORY.md — Master Architecture & Session Memory

> **System State as of:** 2026-09-11  
> **Repository:** `C:\Users\USER\.gemini\antigravity\scratch\privacy-law-explainer`  
> **Production URL:** `https://privacylawforall.sbsrijeet.workers.dev/`  
> **Git Commit:** `d1631db` on `main` (clean working tree)

---

## 1. Current State of the Platform

### A. Published Content & Routes (53 Static Production Routes / 55 HTML Documents)
* **Flagship Master Guides & Studios:**
  * `/dpia`: **NEW** — Dedicated Article 35 DPIA Studio (two-tier screening matrix, 8-part Article 35(7) practitioner blueprint, Article 36 escalation guide, and 5 counterfactual landmark dossiers).
  * `/schrems-and-sccs`: The definitive Schrems I, II & SCCs Master Guide (CJEU rulings, FISA 702, 4 transfer modules, supplementary measures).
  * `/compliance-mistakes`: 10 Fatal GDPR Compliance Mistakes engineered with practical DPO remediation checklists.
  * `/top-5`: Top 5 Largest Fines Tracked (€2.92B+ in penalties across Meta, Amazon, Instagram, TikTok, WhatsApp).
  * `/dpdpa`: Comprehensive India Digital Personal Data Protection Act (DPDPA 2023) hub.
  * `/eu-ai-act`: EU Artificial Intelligence Act 4-tier risk categorization matrix.
  * `/gdpr/articles`: Directory of key GDPR Articles with plain-English breakdowns and dedicated Article 35 DPIA Studio banner.
* **National GDPR Hubs (6 Countries):**
  * `/gdpr/germany`: Germany Regional Hub (BfDI, 16 state DPAs, DSK, BDSG § 26 employee privacy, deletion concepts).
  * `/gdpr/france`: CNIL Hub (ePrivacy, cookie refusal asymmetry of effort, adtech).
  * `/gdpr/ireland`: DPC Hub (Lead authority for Meta, Google, TikTok, Big Tech).
  * `/gdpr/spain`: AEPD Hub (High-volume spam calls, banking consent, subcontracting).
  * `/gdpr/italy`: Garante Hub (Generative AI scraping bans, telemarketing databases).
  * `/gdpr/uk`: ICO Hub (UK GDPR, Age Appropriate Design Code, cyber breach penalties).
* **24 Landmark Case Explainers:** All 24 cases pass deterministic database verification (19 original + 5 German cases: H&M, Deutsche Wohnen, Notebooksbilliger, 1&1 Telecom, Knuddels).
* **8 Thematic Category Hubs:** AI & Biometrics, AdTech & Cookies, Telemarketing & Spam, Cybersecurity & Breaches, Children's Privacy, Cross-Border Transfers, Consent & Banking, Transparency & Notice.

### B. Infrastructure & Tooling
* **Framework:** Astro 5.4 (Static Site Generation / SSG).
* **Styling:** Tailwind CSS 3.4 with `@tailwindcss/typography`, strictly adhering to pure white `#ffffff` academic aesthetics.
* **Hosting:** Cloudflare Pages with automated deployment on `git push origin main`.
* **Testing Pipeline:**
  * `tools/verifier/verify_article.py`: Verifies all frontmatter claims against ChromaDB.
  * `tools/verifier/test_suite.py`: 20x benchmark verification (480 fact checks in 1.64s) + static HTML audit + 3,331 internal link integrity checks with **0 broken links**.
* **Databases Restored in `C:\Users\USER\OneDrive\Documents\`:**
  * `legal-scraper/chroma_db/chroma.sqlite3`: 84,099 legal documents & 13 scrapers.
  * `dpia-mcp/privacy_law_db_local/chroma.sqlite3`: 84,099 replica docs + 94 DPIA templates.
  * `pra-mcp/pra_knowledge/chroma.sqlite3`: 27 US Privacy Risk Assessment knowledge chunks.

---

## 2. Architectural Decision Records (ADRs)

### ADR 1: The "Wikipedia Standard" Pure White UI
* **Context:** Modern developer sites often use dark themes or neon accents.
* **Decision:** Enforce pure white (`#ffffff`) background, high-contrast serif headers, and neutral slate body copy across the entire site. No dark mode.
* **Rationale:** Maximizes credibility, authority, and reading comfort for legal professionals, compliance officers, and students.

### ADR 2: Static Site Generation (SSG) with Zero-JS Reading Experience
* **Context:** The site needed maximum performance, zero hosting costs, and resilience against traffic spikes.
* **Decision:** Build 100% static HTML via Astro deployed to Cloudflare's global edge network.
* **Rationale:** Global sub-50ms latency, zero server maintenance, zero database vulnerability, and optimal SEO crawling.

### ADR 3: Deterministic Fact-Checking Before Publication
* **Context:** Legal explainers cannot tolerate hallucinations in fine amounts or statutory citations.
* **Decision:** Build `verify_article.py` to cross-reference every cited DPA, fine, article, and case name against the 84,000-record ChromaDB database before any case is committed.
* **Rationale:** Guarantees 100% factual accuracy and builds unmatched user trust.

### ADR 4: Zero Broken Links Policy
* **Context:** Dead links destroy educational authority and damage SEO rankings.
* **Decision:** `test_suite.py` crawls every `<a>` tag across all generated HTML files in `dist/`. Build fails if even one broken link exists.
* **Rationale:** Total navigational integrity across all 3,300+ internal cross-links.

### ADR 5: Solo Development Over Multi-Agent Swarms
* **Context:** Multi-agent frameworks (`teamwork_preview`) introduced heavy token usage, coordination delays, and triggered API quota exhaustion (`429 RESOURCE_EXHAUSTED`).
* **Decision:** All core feature development, component creation, and page styling is executed directly by the primary agent in solo mode.
* **Rationale:** 5x faster delivery, immediate error feedback, zero token bloat, and consistent design continuity.

### ADR 6: Subagent Isolation for Data Scrapers
* **Context:** Running web scrapers and bulk PDF ingestion creates thousands of lines of raw HTML, HTTP retries, and chunking logs.
* **Decision:** Delegate scrapers to isolated single subagents (`DeepCoder`), while keeping the main conversation thread clean.
* **Rationale:** Protects the main context window from bloat and truncation.

---

## 3. Immediate Next Steps (For Next Session)

1. **Build the Mock DPIA Studio (`/mock-dpia`):**
   * Implement the interactive Article 35 screening engine and risk assessment checklist.
   * Author the 5 counterfactual landmark DPIA dossiers (Meta, Google, H&M, Deutsche Wohnen, Criteo).
   * Add prominent navigation link in `Header.astro` and route redirect `/dpia` -> `/mock-dpia`.
   * Run verification suite and deploy to production.
