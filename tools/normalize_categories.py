#!/usr/bin/env python3
"""Normalize categories in case explainer markdown files."""
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CASES_DIR = BASE_DIR / "src" / "content" / "cases"

MAPPING = {
    "amazon-luxembourg-profiling.md": "adtech-and-cookies",
    "chatgpt-garante-ai-scraping.md": "ai-and-biometrics",
    "british-airways-credential-breach.md": "cybersecurity-and-breaches",
    "whatsapp-transparency.md": "transparency-and-notice",
    "bbva-spain-consent-fine.md": "consent-and-banking",
    "india-dpdpa-consent-fiduciary.md": "transparency-and-notice",
    "eu-ai-act-biometric-categorization.md": "ai-and-biometrics",
    "google-france-cookie-refusal.md": "adtech-and-cookies",
    "carrefour-france-cookies.md": "adtech-and-cookies",
    "caixabank-customer-consent.md": "consent-and-banking",
    "meta-ireland-data-transfers.md": "cross-border-transfers",
    "enel-energia-italy-spam.md": "telemarketing-and-spam",
    "vodafone-spain-telemarketing.md": "telemarketing-and-spam",
    "marriott-guest-reservation-breach.md": "cybersecurity-and-breaches",
    "tiktok-children-data.md": "children-privacy",
    "tim-telemarketing-italy.md": "telemarketing-and-spam",
    "instagram-teen-privacy.md": "children-privacy",
    "clearview-ai-facial-scraping.md": "ai-and-biometrics",
    "criteo-adtech-tracking.md": "adtech-and-cookies",
}

for fname, cat in MAPPING.items():
    f = CASES_DIR / fname
    if not f.exists():
        print(f"File not found: {fname}")
        continue
    content = f.read_text(encoding="utf-8")
    new_content = re.sub(r'category:\s*["\'][^"\']+["\']', f'category: "{cat}"', content)
    if new_content == content:
        # try without quotes
        new_content = re.sub(r'category:\s*[^\n]+', f'category: "{cat}"', content)
    f.write_text(new_content, encoding="utf-8")
    print(f"Updated {fname} -> category: \"{cat}\"")

print("All 19 cases normalized.")
