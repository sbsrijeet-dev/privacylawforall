# AGENTS.md — Contributor & AI Agent Operating Principles

> **Project:** PrivacyLawForAll.free  
> **Mission:** *"Privacy law, made accessible to all for free, in one place."*  
> **Repository:** `C:\Users\USER\.gemini\antigravity\scratch\privacy-law-explainer`  
> **Live Site:** `https://privacylawforall.sbsrijeet.workers.dev/`

This document defines the core working habits, technical conventions, operating standards, and strict constraints for anyone (human or AI agent) modifying this codebase.

---

## 1. Working Style & Preferences

* **Direct & Conversational:** Keep interactions frank, honest, and practical. No corporate filler or empty sycophancy.
* **Solo Execution as Default:** Work lean, direct, and fast. The primary agent handles design, content, components, builds, testing, and deployment directly in the main thread.
* **Avoid Multi-Agent Swarms (`teamwork_preview`):** Do NOT spin up runaway subagent hierarchies or multi-tiered agent swarms for standard features, UI tweaks, or page generation. They create immense token overhead, add coordination delay, and quickly trigger `429 RESOURCE_EXHAUSTED` quota errors.
* **When to Use Subagents:**
  * **Noisy/Heavy Data Ingestion:** Writing and running web scrapers, parsing bulk regulatory PDFs, or ingesting records into ChromaDB. Running these in an isolated subagent sandbox keeps raw HTML, retry traces, and chunking logs out of the main chat context, preventing context window bloat.
  * **Adversarial Code Auditing:** Occasional pre-release independent auditing (`DeepInvestigator`) to stress-test links, regex patterns, and security headers.
* **Proactive Candor:** If a proposed command, prompt, or workflow is inefficient, over-engineered, or risks burning unnecessary API tokens, speak up directly (*"Nah, we don't need a subagent swarm for that — I can knock it out directly in 3 minutes"*).

---

## 2. Website Standards & Technical Conventions

### The "Wikipedia Standard" (Aesthetic Rules)
* **Pure White Background (`#ffffff`):** The site must always feel clean, authoritative, academic, and readable—like a polished modern encyclopedia.
* **No Dark Mode:** Dark mode, neon accents, and purple/cyberpunk gradients are strictly prohibited.
* **Typography:**
  * **Headings:** Academic, high-legibility serif (`font-serif`, `text-slate-900`).
  * **Body:** Clean, neutral sans-serif (`text-slate-600` to `text-slate-700` with generous line-height).
  * **Code / Articles:** Sharp monospace (`font-mono`, `text-xs`) for statutory articles (e.g. `Article 5(1)(a)`).
* **Color Palette:**
  * Primary Text: Deep slate (`#0f172a`, `text-slate-900`)
  * Subtle Borders: Light slate (`#e2e8f0`, `border-slate-200`)
  * Accent & Branding: Scholarly burgundy/crimson (`#7f1d1d`, `text-red-900`, `bg-red-50`)
  * Badges & Highlights: Soft amber (`#78350f`, `bg-amber-100`, `border-amber-300`) for fines and support

### Legal & Educational Voice
* **"Disclaimer", NEVER "Warning":** Every public page must display the prominent educational notice at the top. The label is always **"Educational & Informational Resource Only — Non-Legal Advice Notice"** (never "WARNING", which is off-putting).
* **Grounding in Real Decisions:** Never fabricate fine figures, dates, or legal articles. Every explainer must map directly to verified DPA decisions and official statutes.

### Monetization & Creator Support
* **Buy Me a Coffee:** Support links (`buymeacoffee.com/sbsrijeet`) are cleanly integrated into the Header, mobile menu, and Footer.
* **Ethical Ad Slots:** Non-intrusive `AdSlot.astro` slots are placed at top and bottom of content pages, with a valid `public/ads.txt`.

### Mobile & Responsive Design
* Mobile-first responsive navigation via hamburger menu (`Header.astro`).
* Touch-friendly targets (`min-h-[44px]`).
* Zero horizontal scroll or broken layout overflows.

---

## 3. Standard Update Protocol (Checklist)

Whenever adding a case, updating a hub, or modifying site features, follow this sequence:

1. **Schema Compliance:** If authoring a case in `src/content/cases/`, ensure all frontmatter fields conform to `src/content/config.ts` (`title`, `case_name`, `popular_name`, `dpa`, `country`, `jurisdiction`, `fine_amount`, `decision_date`, `year`, `articles_cited`, `exam_domain`, `tldr`, `category`, `verified`).
2. **Deterministic Fact-Verification:**
   ```bash
   python tools/verifier/verify_article.py
   ```
   Must pass 100% against the local ChromaDB database in `OneDrive\Documents\legal-scraper\chroma_db\chroma.sqlite3`.
3. **Static Build Test:**
   ```bash
   npm.cmd run build
   ```
   Must generate all static routes with 0 errors and 0 warnings.
4. **Comprehensive Test Suite & Link Audit:**
   ```bash
   python tools/verifier/test_suite.py
   ```
   Must pass Phase 1 (20x benchmark against ChromaDB) and Phase 2 (audit of all HTML pages, disclaimer presence, anti-scraping modals, and **zero broken internal links**).
5. **Git Commit & Deployment:**
   ```bash
   git add .
   git commit -m "feat(scope): descriptive message"
   git push origin main
   ```
   Pushing to `main` automatically triggers Cloudflare Pages build and edge distribution.
6. **Live Edge Verification:**
   Verify the live endpoint on `https://privacylawforall.sbsrijeet.workers.dev/` to confirm HTTP 200 and edge cache update.

---

## 4. Strict Negative Constraints

* **NEVER** introduce dark mode or dark-themed styling.
* **NEVER** allow broken internal links (the test suite enforces 0 broken links).
* **NEVER** guess or invent fine figures, articles, or dates—all must verify against the database.
* **NEVER** run destructive `rm` or `git clean` commands without explicit verification.
* **NEVER** spin up multi-agent hierarchies for standard website edits.
* **NEVER** alter the database path from `C:\Users\USER\OneDrive\Documents\legal-scraper\chroma_db\chroma.sqlite3` without confirmation.
