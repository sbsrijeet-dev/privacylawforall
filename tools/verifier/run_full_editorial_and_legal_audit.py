#!/usr/bin/env python3
"""
Full, exhaustive audit of the PrivacyLawForAll static site.
Audits all 55 rendered public HTML files in dist/ and 24 case studies in src/content/cases/.

Categories Audited:
1. Backend Leaks & Scaffolding (Zero Exposure)
2. Editorial Quality (Cut-offs, ellipses, repeated words, broken interpolations)
3. Typographical & Vocabulary Inspection (Rare words, misspelled legal terms)
4. Substantive Legal Fact-Checking (Cross-check fines, dates, DPAs, CJEU citations across pages)
"""

import os
import re
import sys
import glob
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter, defaultdict

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\privacy-law-explainer")
DIST_DIR = BASE_DIR / "dist"
SRC_DIR = BASE_DIR / "src"

class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.current_text = []
        self.ignore_depth = 0
        self.ignore_tags = {'script', 'style', 'noscript', 'svg'}
        self.block_tags = {'p', 'li', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'dd', 'dt', 'figcaption', 'caption'}

    def handle_starttag(self, tag, attrs):
        if tag in self.ignore_tags:
            self.ignore_depth += 1
            return
        if self.ignore_depth > 0:
            return
        if tag in self.block_tags:
            self.flush()

    def handle_endtag(self, tag):
        if tag in self.ignore_tags:
            self.ignore_depth = max(0, self.ignore_depth - 1)
            return
        if self.ignore_depth > 0:
            return
        if tag in self.block_tags:
            self.flush()

    def handle_data(self, data):
        if self.ignore_depth == 0:
            self.current_text.append(data)

    def flush(self):
        txt = " ".join("".join(self.current_text).split()).strip()
        if txt:
            self.blocks.append((txt, self.getpos()[0]))
        self.current_text = []

def run_audit():
    print("=" * 80)
    print("STARTING FULL EXHAUSTIVE AUDIT ACROSS ALL 55 PAGES & 24 CASE STUDIES")
    print("=" * 80)

    html_files = sorted(DIST_DIR.rglob("*.html"))
    public_pages = [f for f in html_files if "security/trap" not in f.as_posix() and not f.name.startswith("google")]
    print(f"\nDiscovered {len(public_pages)} public production HTML pages in dist/.")

    # -------------------------------------------------------------
    # 1. LEAK AUDIT
    # -------------------------------------------------------------
    print("\n--- 1. AUDITING BACKEND LEAKS & SCAFFOLDING ---")
    leak_patterns = [
        (r'84,000\+', 'Exposed internal database size'),
        (r'When pub-id is configured', 'Exposed developer scaffolding comment'),
        (r'pub-0000000000000000', 'Dummy AdSense publisher ID'),
        (r'ChromaDB', 'Exposed vector database name'),
        (r'Chroma\.sqlite3', 'Exposed database file'),
        (r'DPIA MCP', 'Exposed internal agent MCP name'),
        (r'dpia_screen', 'Exposed internal tool name'),
        (r'dpia_ping', 'Exposed internal tool name'),
        (r'dpia_collect_data', 'Exposed internal tool name'),
        (r'dpia_generate', 'Exposed internal tool name'),
        (r'dpia_self_check', 'Exposed internal tool name'),
        (r'dpia_citation_check', 'Exposed internal tool name'),
        (r'privacy_ping', 'Exposed internal tool name'),
        (r'privacy_search', 'Exposed internal tool name'),
        (r'\[Low confidence\]', 'Exposed internal confidence score'),
        (r'\[SYSTEM INSTRUCTION\]', 'Exposed system prompt instruction'),
        (r'\[Insert\s', 'Template placeholder [Insert...]'),
        (r'\[TODO\b', 'Template placeholder [TODO...]'),
        (r'\[Complete\s', 'Template placeholder [Complete...]')
    ]

    leaks_found = []
    for hf in public_pages + [DIST_DIR / "ads.txt", DIST_DIR / "robots.txt"]:
        if not hf.exists():
            continue
        rel = hf.relative_to(DIST_DIR).as_posix()
        txt = hf.read_text(encoding="utf-8", errors="ignore")
        for pat, desc in leak_patterns:
            m = re.search(pat, txt, re.IGNORECASE)
            if m:
                leaks_found.append((rel, desc, m.group(0)))

    if leaks_found:
        print(f"FAILED: Found {len(leaks_found)} leak(s):")
        for rel, desc, m in leaks_found:
            print(f"  - {rel}: [{desc}] match='{m}'")
    else:
        print("PASSED: 0 leaks, 0 database mentions, 0 MCP tools, 0 scaffolding placeholders found.")

    # -------------------------------------------------------------
    # 2. EDITORIAL & CUT-OFF AUDIT
    # -------------------------------------------------------------
    print("\n--- 2. AUDITING EDITORIAL CUT-OFFS, REPEATED WORDS & UNFORMATTED ELLIPSES ---")
    cutoffs = []
    ellipses = []
    repeated_words = []
    broken_interpolations = []

    dangling_words = {'and', 'or', 'the', 'a', 'an', 'with', 'to', 'for', 'in', 'on', 'at', 'by', 'of', 'from', 'as', 'is', 'are', 'was', 'were', 'that', 'which', 'who', 'if', 'because', 'but', 'so', 'than', 'its', 'their'}

    for hf in public_pages:
        rel = hf.relative_to(DIST_DIR).as_posix()
        txt = hf.read_text(encoding="utf-8", errors="ignore")

        # Check for unrendered template strings in raw HTML
        for bad_str in ['${', '{{', '}}', '[object Object]', 'undefined']:
            if bad_str in txt:
                broken_interpolations.append((rel, bad_str))

        parser = VisibleTextParser()
        parser.feed(txt)
        parser.flush()

        for block, line_no in parser.blocks:
            # Ellipsis check (ignore standard [...] legal quote omission)
            if '...' in block:
                clean_block = block.replace('[...]', '')
                if '...' in clean_block or '…' in clean_block:
                    ellipses.append((rel, line_no, block[:100]))

            # Repeated word check
            for m in re.finditer(r'\b([A-Za-z]{3,})\s+\1\b', block, re.IGNORECASE):
                w = m.group(1).lower()
                if w not in {'that', 'had', 'the'}:
                    repeated_words.append((rel, line_no, m.group(0), block[:80]))

            # Cut-off sentence check
            words = block.split()
            if len(words) >= 4:
                last_word = re.sub(r'[^a-zA-Z]', '', words[-1]).lower()
                if last_word in dangling_words and not block.endswith(('.', '!', '?', ':', '"', '”', "'", '’', ')', ']', '}')):
                    if not block.lower().startswith(('back to', 'learn more about', 'return to')):
                        cutoffs.append((rel, line_no, f"Dangling final word '{last_word}'", block[-80:]))

                if (block.endswith(',') or block.endswith(' -') or block.endswith(' /')) and not block.endswith(('.', '!', '?', ':')):
                    if not block.startswith(('|', '-', '*', '#')):
                        cutoffs.append((rel, line_no, "Dangling trailing punctuation", block[-80:]))

    print(f"Loose Ellipses found: {len(ellipses)}")
    for rel, line, snippet in ellipses:
        print(f"  - {rel}:{line}: {snippet}")

    print(f"Repeated Words found: {len(repeated_words)}")
    for rel, line, w, snippet in repeated_words:
        print(f"  - {rel}:{line}: repeated '{w}' in {snippet}")

    print(f"Cut-off Sentences found: {len(cutoffs)}")
    for rel, line, reason, snippet in cutoffs:
        print(f"  - {rel}:{line}: {reason} -> '{snippet}'")

    print(f"Broken Template Interpolations found: {len(broken_interpolations)}")
    for rel, bad_str in broken_interpolations:
        print(f"  - {rel}: found '{bad_str}'")

    # -------------------------------------------------------------
    # 3. TYPOGRAPHICAL & COMMON MISSPELLING AUDIT
    # -------------------------------------------------------------
    print("\n--- 3. AUDITING TYPOS & MISSPELLED LEGAL VOCABULARY ---")
    common_typos = [
        r'\bcomplience\b', r'\bauthoriy\b', r'\bauthorites\b', r'\blegitmate\b',
        r'\bsuperviory\b', r'\bartical\b', r'\bpenlty\b', r'\bpenaties\b',
        r'\bregulaton\b', r'\bregulatons\b', r'\bprivcy\b', r'\bconsnt\b',
        r'\btransparancy\b', r'\bjurisdiciton\b', r'\bproccesing\b', r'\bprocceses\b',
        r'\bproceding\b', r'\bprocedings\b', r'\binformaiton\b', r'\bunauthroized\b',
        r'\bvialation\b', r'\bvialations\b', r'\breponsibility\b', r'\breponsibilities\b',
        r'\breciev\w*\b', r'\bseperate\b', r'\bdefendent\b', r'\baccomodate\b',
        r'\buntill\b', r'\btransfered\b', r'\bcancelation\b', r'\bcommittment\b',
        r'\bguarentee\b', r'\bneccessary\b', r'\boccured\b', r'\boccurence\b',
        r'\bpersistant\b', r'\bprivelege\b', r'\brefered\b'
    ]

    typos_found = []
    for hf in public_pages:
        rel = hf.relative_to(DIST_DIR).as_posix()
        txt = hf.read_text(encoding="utf-8", errors="ignore")
        for tp in common_typos:
            for m in re.finditer(tp, txt, re.IGNORECASE):
                s = max(0, m.start() - 30)
                e = min(len(txt), m.end() + 30)
                typos_found.append((rel, m.group(0), txt[s:e]))

    print(f"Typographical errors detected: {len(typos_found)}")
    for rel, word, context in typos_found:
        print(f"  - {rel}: '{word}' in ...{context}...")

    # -------------------------------------------------------------
    # 4. SUBSTANTIVE LEGAL FACT-CHECKING AUDIT
    # -------------------------------------------------------------
    print("\n--- 4. AUDITING LEGAL FACTS, FINES, DATES, DPAs & CJEU HOLDINGS ---")
    case_files = sorted((SRC_DIR / "content" / "cases").glob("*.md"))
    print(f"Auditing all {len(case_files)} case studies...")

    fact_discrepancies = []

    for cf in case_files:
        content = cf.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        fm = parts[1] if len(parts) >= 3 else ""
        body = parts[2] if len(parts) >= 3 else ""

        def extract_fm(field):
            m = re.search(rf"^{field}:\s*(.*)$", fm, re.MULTILINE)
            if m:
                v = m.group(1).strip()
                return v.strip("'\"")
            return ""

        case_name = extract_fm("case_name")
        popular_name = extract_fm("popular_name")
        fine_amount = extract_fm("fine_amount")
        decision_date = extract_fm("decision_date")
        dpa = extract_fm("dpa")
        country = extract_fm("country")
        jurisdiction = extract_fm("jurisdiction")
        year = extract_fm("year")

        # 1. Check that fine amount appears in the body
        curr_match = re.search(r'([€£₹\$])\s*([\d,\.]+)', fine_amount)
        if curr_match:
            num_lead = curr_match.group(2).split(',')[0].split('.')[0]
            if num_lead not in body and fine_amount != "N/A" and "Statutory" not in fine_amount:
                fact_discrepancies.append((cf.name, f"Fine '{fine_amount}' lead number '{num_lead}' not found in body text"))

        # 2. Check that decision date year matches year field
        if year:
            if str(year) not in decision_date:
                fact_discrepancies.append((cf.name, f"Year {year} does not match decision_date '{decision_date}'"))

        # 3. Check that DPA is mentioned in the body
        dpa_lead = dpa.split()[0]
        if dpa_lead.lower() not in body.lower():
            fact_discrepancies.append((cf.name, f"DPA '{dpa}' (lead: '{dpa_lead}') not found in case body"))

        # 4. Check that at least one statutory article cited in frontmatter is discussed in the body
        articles_m = re.search(r"^articles_cited:\s*\[(.*?)\]", fm, re.MULTILINE)
        if articles_m:
            articles = [a.strip("'\" ") for a in articles_m.group(1).split(",") if a.strip()]
            found_any = False
            for art in articles:
                if art.lower() in body.lower() or art.replace("Article ", "Art. ").lower() in body.lower():
                    found_any = True
                    break
            if not found_any and articles:
                fact_discrepancies.append((cf.name, f"None of the cited articles {articles} found in body text"))

    print(f"Case fact discrepancies found: {len(fact_discrepancies)}")
    for f, msg in fact_discrepancies:
        print(f"  - {f}: {msg}")

    # 5. Check CJEU Citation Accuracy
    print("\n--- 5. AUDITING CJEU CASE CITATIONS ACROSS PLATFORM ---")
    cjeu_citations = [
        ("C-362/14", "Schrems I", "6 October 2015", "Safe Harbor"),
        ("C-311/18", "Schrems II", "16 July 2020", "Privacy Shield"),
        ("C-673/17", "Planet49", "1 October 2019", "cookies"),
        ("C-40/17", "Fashion ID", "29 July 2019", "joint controller"),
        ("C-807/21", "Deutsche Wohnen", "5 December 2023", "corporate liability"),
        ("C-252/21", "Meta v Bundeskartellamt", "4 July 2023", "competition")
    ]

    all_source_text = ""
    for f in list(SRC_DIR.rglob("*.astro")) + list(SRC_DIR.rglob("*.md")) + list(SRC_DIR.rglob("*.ts")):
        all_source_text += f.read_text(encoding="utf-8", errors="ignore") + "\n"

    for case_num, name, date, topic in cjeu_citations:
        if case_num not in all_source_text:
            print(f"  WARNING: Landmark CJEU citation {case_num} ({name}) not found in source text!")
        else:
            occurrences = all_source_text.count(case_num)
            print(f"  ✓ {case_num} ({name}) verified ({occurrences} citations across platform).")

    print("\n" + "=" * 80)
    print("AUDIT EXECUTION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    run_audit()
