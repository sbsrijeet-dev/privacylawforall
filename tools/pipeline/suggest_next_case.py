#!/usr/bin/env python3
"""
3-Day Case Expansion Pipeline Tool for PrivacyLawForAll.free.
Scans existing published cases, queries the local ChromaDB database (63,000+ records),
and suggests high-value new privacy law enforcement decisions ready to be explained.

Usage:
    python tools/pipeline/suggest_next_case.py [--count 5] [--country Spain] [--generate SLUG]
"""

import sys
import os
import re
import argparse
import sqlite3
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CASES_DIR = BASE_DIR / "src" / "content" / "cases"
CHROMA_DB = Path(r"C:\Users\USER\OneDrive\Documents\legal-scraper\chroma_db\chroma.sqlite3")


def parse_frontmatter_case_names() -> set[str]:
    """Extract known case names, entity tokens, and slugs already published."""
    published_entities = set()
    if not CASES_DIR.exists():
        return published_entities

    for file_path in CASES_DIR.glob("*.md"):
        published_entities.add(file_path.stem.lower())
        content = file_path.read_text(encoding="utf-8")
        if "---" in content:
            parts = content.split("---", 2)
            if len(parts) >= 3:
                for line in parts[1].splitlines():
                    if line.startswith("case_name:"):
                        name = line.split(":", 1)[1].strip().strip('"').strip("'").lower()
                        published_entities.add(name)
                        for word in re.findall(r"[a-z0-9]{4,}", name):
                            published_entities.add(word)
                    elif line.startswith("title:"):
                        title = line.split(":", 1)[1].strip().strip('"').strip("'").lower()
                        for word in re.findall(r"[a-z0-9]{4,}", title):
                            published_entities.add(word)

    generic = {"data", "privacy", "protection", "commission", "authority", "ireland", "spain", "france", "italy", "united"}
    return {e for e in published_entities if e not in generic}


def get_db_connection() -> sqlite3.Connection:
    """Connect read-only to ChromaDB SQLite."""
    if not CHROMA_DB.exists():
        raise FileNotFoundError(f"ChromaDB SQLite not found at {CHROMA_DB}")
    return sqlite3.connect(f"file:{CHROMA_DB.as_posix()}?mode=ro", uri=True)


def fetch_candidate_cases(country_filter: str = None, min_fine_chars: int = 4) -> list[dict]:
    """Query ChromaDB embedding_metadata for unique cases with fines and DPAs."""
    con = get_db_connection()
    cur = con.cursor()

    query = """
        SELECT 
            m_title.id,
            m_title.string_value AS title,
            m_fine.string_value AS fine,
            m_dpa.string_value AS dpa,
            m_country.string_value AS country,
            m_art.string_value AS article,
            m_url.string_value AS source_url
        FROM embedding_metadata m_title
        JOIN embedding_metadata m_fine ON m_title.id = m_fine.id AND m_fine.key = 'fine'
        LEFT JOIN embedding_metadata m_dpa ON m_title.id = m_dpa.id AND m_dpa.key = 'dpa'
        LEFT JOIN embedding_metadata m_country ON m_title.id = m_country.id AND m_country.key = 'country'
        LEFT JOIN embedding_metadata m_art ON m_title.id = m_art.id AND m_art.key = 'article'
        LEFT JOIN embedding_metadata m_url ON m_title.id = m_url.id AND m_url.key = 'source_url'
        WHERE m_title.key IN ('case_title', 'title')
          AND m_fine.string_value IS NOT NULL
          AND length(m_fine.string_value) >= ?
    """
    params = [min_fine_chars]

    if country_filter:
        query += " AND (m_country.string_value LIKE ? OR m_dpa.string_value LIKE ?)"
        params.extend([f"%{country_filter}%", f"%{country_filter}%"])

    query += " LIMIT 300"
    cur.execute(query, params)
    rows = cur.fetchall()
    con.close()

    candidates = []
    seen_titles = set()

    for row in rows:
        cid, title, fine, dpa, country, article, url = row
        title_str = (title or "").strip()
        if not title_str or len(title_str) < 4:
            continue
        
        clean_key = re.sub(r"[^a-zA-Z0-9]", "", title_str.lower())[:30]
        if clean_key in seen_titles:
            continue
        seen_titles.add(clean_key)

        candidates.append({
            "id": cid,
            "title": title_str,
            "fine": fine or "Fine Issued",
            "dpa": dpa or "Data Protection Authority",
            "country": country or "EU Jurisdiction",
            "article": article or "Articles 5, 6",
            "url": url or "Official Enforcement Gazette"
        })

    return candidates


def filter_uncovered(candidates: list[dict], published_entities: set[str]) -> list[dict]:
    """Filter out candidates whose title or entity is already in published cases."""
    uncovered = []
    for cand in candidates:
        cand_lower = cand["title"].lower()
        tokens = [t for t in re.findall(r"[a-z0-9]{4,}", cand_lower) if t not in ("fine", "penalty", "gdpr", "euro", "decision", "order", "against", "breach")]
        already_covered = False
        for token in tokens:
            if token in published_entities:
                already_covered = True
                break
        
        if not already_covered:
            uncovered.append(cand)
    return uncovered


def generate_case_template(case: dict) -> str:
    """Generate ready-to-use Astro/Markdown frontmatter and skeleton structure."""
    slug = re.sub(r"[^a-z0-9]+", "-", case["title"].lower()).strip("-")
    return f"""---
title: "{case['title']}: Key Takeaways & Compliance Breakdown"
case_name: "{case['title']}"
dpa: "{case['dpa']}"
jurisdiction: "{case['country']}"
fine_amount: "{case['fine']}"
date_decided: "2024-01-15"
articles_cited: ["Article {case['article']}"]
category: "transparency-and-notice"
tldr: "The {case['dpa']} imposed a {case['fine']} penalty for unlawful data processing and non-compliance with transparency mandates."
published_at: "2026-09-10"
featured: false
---

## Executive Overview
On {case['country']} enforcement proceedings, the **{case['dpa']}** issued a penalty of **{case['fine']}** regarding {case['title']}.

## What Happened?
Detailed factual breakdown of the processing activity and subsequent investigation.

## The Legal Infringement
The authority established non-compliance with **Article {case['article']}**:
- Absence of valid legal basis
- Insufficient organizational and technical safeguards

## Practical Takeaways for Compliance Teams
1. **Auditing processing activities:** Ensure accurate records of processing.
2. **Reviewing legal grounds:** Validate lawful bases prior to collection.
"""


def main():
    parser = argparse.ArgumentParser(description="PrivacyLawForAll.free 3-Day Case Expansion Helper")
    parser.add_argument("--count", type=int, default=5, help="Number of suggestions (default: 5)")
    parser.add_argument("--country", type=str, default=None, help="Filter by country (e.g. Germany, Spain, Italy)")
    parser.add_argument("--generate", type=int, default=None, help="Index of suggestion to generate template for (1-based)")
    args = parser.parse_args()

    print("=" * 72)
    print("  PrivacyLawForAll.free - 3-Day Case Expansion Suggester")
    print("  Scans 63,000+ enforcement records in database against published cases")
    print("=" * 72)

    published = parse_frontmatter_case_names()
    print(f"[*] Found {len(published)} entity tokens across currently published cases.")
    
    candidates = fetch_candidate_cases(country_filter=args.country)
    uncovered = filter_uncovered(candidates, published)
    
    print(f"[*] Found {len(uncovered)} candidate cases not yet written on the website.")
    print("-" * 72)

    top_picks = uncovered[:args.count]

    for i, c in enumerate(top_picks, 1):
        print(f"\n[{i}] {c['title']}")
        print(f"    Authority:   {c['dpa']} ({c['country']})")
        print(f"    Fine / Act:  {c['fine']}")
        print(f"    Articles:    {c['article']}")
        print(f"    Source URL:  {c['url']}")

    if args.generate and 1 <= args.generate <= len(top_picks):
        chosen = top_picks[args.generate - 1]
        print("\n" + "=" * 72)
        print(f"  Markdown Template for Selection #{args.generate}: {chosen['title']}")
        print("=" * 72)
        print(generate_case_template(chosen))
    else:
        print("\n[TIP] Run with `--generate 1` to print the ready-to-use markdown file skeleton.")
        print("=" * 72)


if __name__ == "__main__":
    main()
