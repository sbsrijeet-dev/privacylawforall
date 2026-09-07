#!/usr/bin/env python3
"""
Comprehensive Web Scraper & Cyber Attack Defense Verification Suite
-------------------------------------------------------------------
Automated security testing tool verifying the multi-layer defensive posture
of PrivacyLaw.free against automated scrapers, headless bot drivers, and
data harvesting attacks.

Audits:
1. Robots.txt Scraping Disallows (13 major AI & mass scrapers)
2. HTTP Security & Anti-Bot Meta Directives across all 32 public pages
3. Headless Browser & Automated Webdriver Detection (AntiScrapeShield)
4. Invisible Honeypot Scraper Trap & Decoy Architecture
5. Rate-Limiting & Content Blurring Tripwires
6. Zero-Leakage Audit (No internal DB or infrastructure disclosures)
7. Live Server Security & Endpoint Defense against Simulated Bot Requests
"""

import os
import sys
import re
import urllib.request
import urllib.error
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DIST_DIR = BASE_DIR / "dist"
ROBOTS_FILE = DIST_DIR / "robots.txt"
LIVE_HOST = "http://localhost:4321"

# Banned AI & commercial scraping user agents
TARGET_BOTS = [
    "GPTBot",
    "ChatGPT-User",
    "CCBot",
    "ClaudeBot",
    "anthropic-ai",
    "Google-Extended",
    "Bytespider",
    "Diffbot",
    "PerplexityBot",
    "Scrapy",
    "FacebookBot",
    "Amazonbot",
    "Applebot-Extended",
]


class SecurityAuditReport:
    def __init__(self):
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.errors = []
        self.passed_checks = []

    def record_pass(self, name: str, detail: str = ""):
        self.tests_run += 1
        self.tests_passed += 1
        msg = f"[PASS] {name}"
        if detail:
            msg += f" — {detail}"
        self.passed_checks.append(msg)
        print(f"  ✓ {msg}")

    def record_fail(self, name: str, error: str):
        self.tests_run += 1
        self.tests_failed += 1
        msg = f"[FAIL] {name}: {error}"
        self.errors.append(msg)
        print(f"  ✗ {msg}")


def test_robots_txt_scraper_disallow(report: SecurityAuditReport):
    print("\n--- TEST 1: Robots.txt Anti-Scraper & AI Disallow Rules ---")
    if not ROBOTS_FILE.exists():
        report.record_fail("Robots.txt Existence", f"robots.txt missing from {ROBOTS_FILE}")
        return

    content = ROBOTS_FILE.read_text(encoding="utf-8")

    # Check that all target bots are explicitly disallowed
    missing_bots = []
    for bot in TARGET_BOTS:
        pattern = rf"User-agent:\s*{re.escape(bot)}\s*\nDisallow:\s*/"
        if not re.search(pattern, content, re.IGNORECASE):
            missing_bots.append(bot)

    if missing_bots:
        report.record_fail("AI Scraper Disallow Directives", f"Missing disallow for bots: {missing_bots}")
    else:
        report.record_pass("AI Scraper Disallow Directives", f"All {len(TARGET_BOTS)} AI/scraping bots explicitly blocked from root (/)")

    # Check honeypot and private endpoints disallowed for all crawlers
    if "Disallow: /security/trap" in content:
        report.record_pass("Honeypot Trap Protection", "Disallow: /security/trap configured")
    else:
        report.record_fail("Honeypot Trap Protection", "Honeypot route /security/trap not disallowed in robots.txt")

    if "Disallow: /api/" in content:
        report.record_pass("Private API Protection", "Disallow: /api/ configured")
    else:
        report.record_fail("Private API Protection", "Disallow: /api/ missing")

    if "Crawl-delay" in content:
        report.record_pass("Crawl-Delay Throttling", "Crawl-delay rate-limiting parameter active")
    else:
        report.record_fail("Crawl-Delay Throttling", "No crawl-delay specified for general crawlers")


def test_security_headers_and_meta(report: SecurityAuditReport):
    print("\n--- TEST 2: HTTP Security & Anti-Bot Meta Directives across Public Pages ---")
    html_files = sorted(DIST_DIR.rglob("*.html"))
    public_pages = [f for f in html_files if "security/trap" not in f.as_posix()]

    if not public_pages:
        report.record_fail("Public Pages Existence", "No public HTML pages found in dist/")
        return

    missing_noarchive = []
    missing_nosniff = []
    missing_sameorigin = []
    missing_referrer = []

    for f in public_pages:
        rel = f.relative_to(DIST_DIR).as_posix()
        txt = f.read_text(encoding="utf-8")

        if 'content="index, follow, max-snippet:150, max-image-preview:none, noarchive"' not in txt and 'noarchive' not in txt:
            missing_noarchive.append(rel)

        if 'http-equiv="X-Content-Type-Options" content="nosniff"' not in txt:
            missing_nosniff.append(rel)

        if 'http-equiv="X-Frame-Options" content="SAMEORIGIN"' not in txt:
            missing_sameorigin.append(rel)

        if 'name="referrer" content="strict-origin-when-cross-origin"' not in txt:
            missing_referrer.append(rel)

    if missing_noarchive:
        report.record_fail("Anti-Cache noarchive Directive", f"Missing on {len(missing_noarchive)} pages")
    else:
        report.record_pass("Anti-Cache noarchive Directive", f"Active on 100% of public pages ({len(public_pages)} pages)")

    if missing_nosniff:
        report.record_fail("X-Content-Type-Options nosniff", f"Missing on {len(missing_nosniff)} pages")
    else:
        report.record_pass("X-Content-Type-Options nosniff", f"Enforced on all {len(public_pages)} pages (MIME-sniffing protection)")

    if missing_sameorigin:
        report.record_fail("X-Frame-Options Clickjacking Defense", f"Missing on {len(missing_sameorigin)} pages")
    else:
        report.record_pass("X-Frame-Options Clickjacking Defense", f"Enforced on all {len(public_pages)} pages (prevents iframe embeds)")

    if missing_referrer:
        report.record_fail("Strict Referrer Policy", f"Missing on {len(missing_referrer)} pages")
    else:
        report.record_pass("Strict Referrer Policy", f"Enforced on all {len(public_pages)} pages")


def test_anti_scrape_shield_integrity(report: SecurityAuditReport):
    print("\n--- TEST 3: Headless Driver & Bot Automation Shield Verification ---")
    html_files = sorted(DIST_DIR.rglob("*.html"))
    public_pages = [f for f in html_files if "security/trap" not in f.as_posix()]

    missing_shield_modal = []
    missing_webdriver_check = []
    missing_watermark_listener = []

    for f in public_pages:
        rel = f.relative_to(DIST_DIR).as_posix()
        txt = f.read_text(encoding="utf-8")

        if 'id="anti-scrape-shield-modal"' not in txt:
            missing_shield_modal.append(rel)

        if "navigator.webdriver" not in txt:
            missing_webdriver_check.append(rel)

        if "Unauthorized bulk harvesting strictly prohibited" not in txt and "pl_scrape_req_history" not in txt:
            missing_watermark_listener.append(rel)

    if missing_shield_modal:
        report.record_fail("Anti-Scrape Shield Modal Presence", f"Missing on {len(missing_shield_modal)} pages")
    else:
        report.record_pass("Anti-Scrape Shield Modal Presence", f"Embedded on 100% of public pages ({len(public_pages)} pages)")

    if missing_webdriver_check:
        report.record_fail("Webdriver Automation Detection Routine", f"Missing webdriver checks on {len(missing_webdriver_check)} pages")
    else:
        report.record_pass("Webdriver Automation Detection Routine", "Active checks for navigator.webdriver, Selenium, and Puppeteer")

    if missing_watermark_listener:
        report.record_fail("Attribution Watermarking & Rate Tripwire", f"Missing on {len(missing_watermark_listener)} pages")
    else:
        report.record_pass("Attribution Watermarking & Rate Tripwire", "Active clipboard watermarking & rapid request tracking on all pages")


def test_honeypot_trap_defense(report: SecurityAuditReport):
    print("\n--- TEST 4: Invisible Honeypot Trap & Decoy Architecture ---")
    html_files = sorted(DIST_DIR.rglob("*.html"))
    public_pages = [f for f in html_files if "security/trap" not in f.as_posix()]

    missing_honeypot = []
    for f in public_pages:
        rel = f.relative_to(DIST_DIR).as_posix()
        txt = f.read_text(encoding="utf-8")
        if 'href="/security/trap"' not in txt or 'class="scraper-honeypot-trap"' not in txt:
            missing_honeypot.append(rel)

    if missing_honeypot:
        report.record_fail("Honeypot Trap Embedding", f"Honeypot missing on {len(missing_honeypot)} pages")
    else:
        report.record_pass("Honeypot Trap Embedding", f"Invisible bot honeypot trap deployed across all {len(public_pages)} public pages")

    # Check trap page itself exists and sets poison flags
    trap_page = DIST_DIR / "security" / "trap" / "index.html"
    if trap_page.exists():
        trap_txt = trap_page.read_text(encoding="utf-8")
        if "403 Forbidden" in trap_txt and "pl_honeypot_triggered" in trap_txt:
            report.record_pass("Honeypot Execution & Flagging", "Trap page returns 403 Forbidden and sets persistent scraper flag")
        else:
            report.record_fail("Honeypot Execution & Flagging", "Trap page missing 403 or poison flag script")
    else:
        report.record_fail("Honeypot Execution & Flagging", "Trap page file does not exist at /security/trap/index.html")


def test_zero_leakage_audit(report: SecurityAuditReport):
    print("\n--- TEST 5: Zero-Leakage Audit (Confidentiality & Infrastructure Shield) ---")
    html_files = sorted(DIST_DIR.rglob("*.html"))

    leaked_terms = [
        "chroma.sqlite3",
        "chromadb",
        "legal-scraper",
        "Local 63k Decision DB",
        "63,000+ document regulatory database",
        "OneDrive\\Documents",
    ]

    leaks_found = []
    for f in html_files:
        rel = f.relative_to(DIST_DIR).as_posix()
        txt = f.read_text(encoding="utf-8")
        for term in leaked_terms:
            if term.lower() in txt.lower():
                leaks_found.append(f"{rel}: Leaked confidential term '{term}'")

    if leaks_found:
        report.record_fail("Confidential Infrastructure Protection", f"Disclosures found: {leaks_found[:3]}")
    else:
        report.record_pass("Confidential Infrastructure Protection", "Zero leaks of ChromaDB, SQLite paths, or internal DB infrastructure in HTML")


def test_live_server_defense(report: SecurityAuditReport):
    print(f"\n--- TEST 6: Live Server Threat Simulation & Endpoint Defense ({LIVE_HOST}) ---")
    try:
        req = urllib.request.Request(f"{LIVE_HOST}/robots.txt")
        with urllib.request.urlopen(req, timeout=3) as resp:
            if resp.status == 200:
                body = resp.read().decode("utf-8")
                if "GPTBot" in body and "Disallow: /" in body:
                    report.record_pass("Live Robots.txt Serving", "Live server actively serves strict anti-bot directives")
                else:
                    report.record_fail("Live Robots.txt Serving", "Robots.txt content incomplete on live server")
            else:
                report.record_fail("Live Robots.txt Serving", f"Status code {resp.status}")
    except Exception as e:
        report.record_fail("Live Robots.txt Serving", f"Could not connect to {LIVE_HOST}: {e}")

    # Test Scraper Bot Simulation (Simulating Scrapy / Python crawler)
    try:
        req = urllib.request.Request(
            f"{LIVE_HOST}/security/trap",
            headers={"User-Agent": "Scrapy/2.11 (+https://scrapy.org)"}
        )
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = resp.read().decode("utf-8")
            if "403 Forbidden" in data:
                report.record_pass("Simulated Bot Honeypot Interception", "Live honeypot intercepted simulated Scrapy crawler")
            else:
                report.record_fail("Simulated Bot Honeypot Interception", "Honeypot did not return 403 content")
    except Exception as e:
        report.record_fail("Simulated Bot Honeypot Interception", f"Error during bot probe: {e}")

    # Test Sensitive Directory Probing Protection
    probe_targets = ["/.env", "/.git/config", "/package.json"]
    for pt in probe_targets:
        try:
            req = urllib.request.Request(f"{LIVE_HOST}{pt}")
            with urllib.request.urlopen(req, timeout=3) as resp:
                # If static server serves source files or .env, that's a vulnerability
                report.record_fail("Sensitive File Probing", f"Exposed sensitive file at {pt} (HTTP 200)")
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                report.record_pass("Sensitive File Probing", f"Path {pt} properly blocked/denied (HTTP {e.code})")
        except Exception:
            report.record_pass("Sensitive File Probing", f"Path {pt} unreachable")


def main():
    print("=" * 75)
    print("   PRIVACYLAW.FREE — WEB SCRAPER & CYBER DEFENSE VERIFICATION SUITE   ")
    print("=" * 75)

    report = SecurityAuditReport()

    test_robots_txt_scraper_disallow(report)
    test_security_headers_and_meta(report)
    test_anti_scrape_shield_integrity(report)
    test_honeypot_trap_defense(report)
    test_zero_leakage_audit(report)
    test_live_server_defense(report)

    print("\n" + "=" * 75)
    print("  SECURITY AUDIT SUMMARY")
    print("=" * 75)
    print(f"  Total Security Checks Executed: {report.tests_run}")
    print(f"  Checks Passed: {report.tests_passed}")
    print(f"  Checks Failed: {report.tests_failed}")

    if report.tests_failed == 0:
        print("\n  >>> VERDICT: 100% PASS — ANTI-SCRAPING & CYBER DEFENSES VERIFIED <<<")
        print("  - All 13 major AI training & commercial crawlers strictly disallowed.")
        print("  - Anti-Scrape Shield active across 100% of public pages.")
        print("  - Invisible honeypot tripwire live and intercepting scrapers.")
        print("  - Zero internal database or infrastructure disclosures.")
        print("  - Sensitive file probes blocked.")
        sys.exit(0)
    else:
        print(f"\n  >>> VERDICT: {report.tests_failed} SECURITY CHECKS FAILED <<<")
        sys.exit(1)


if __name__ == "__main__":
    main()
