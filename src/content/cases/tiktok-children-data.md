---
title: "TikTok's €345M Penalty: Dark Patterns and Kids' Account Defaults Exposed"
case_name: "TikTok Technology Limited - Processing of Children's Personal Data (DPC Decision IN-21-9-1)"
popular_name: "TikTok €345M Child Privacy Fine"
dpa: "Data Protection Commission"
country: "Ireland"
jurisdiction: "EU GDPR"
fine_amount: "€345,000,000"
fine_magnitude: "345M"
decision_date: "2023-09-01"
year: 2023
articles_cited: ["Article 5(1)(a)", "Article 5(1)(c)", "Article 24(1)", "Article 25(1)", "Article 25(2)"]
exam_domain: "Fairness, Dark Patterns & Minors (CIPP/E Domain II & IV)"
tldr: "TikTok was fined €345 Million for setting children's accounts to public by default, allowing strangers to duet with kids, and using manipulative dark patterns to push public sharing."
is_top_5: true
top_5_rank: 4
category: "children-privacy"
source_url: "https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-345-million-euro-fine-tiktok"
verified: true
---

## At a Glance

* **The Offender:** TikTok Technology Limited
* **The Authority:** Irish Data Protection Commission (DPC)
* **The Penalty:** €345,000,000 (€345 Million) + reprimand and compliance order
* **The Core Issue:** Children's accounts defaulted to public, dangerous "Family Pairing" loopholes, and deceptive UI nudges ("dark patterns") steering kids away from privacy.

---

## 1. The TL;DR in Plain English

When a 13-to-17-year-old created an account on TikTok, the app defaulted their videos, comments, and duets to be visible to anyone in the world. Anyone could download a teenager's videos or stitch them without permission. 

Even more alarming, TikTok's "Family Pairing" feature allowed *any adult* to link their account to a child's account without verifying if they were actually the child's parent or legal guardian. The Irish regulator imposed a **€345 Million fine** for systematically failing to safeguard young users.

---

## 2. The Story: What Happened?

In September 2021, the Irish DPC initiated an extensive investigation into TikTok's handling of children aged 13–17 between July 31, 2020, and December 31, 2020.

The inquiry revealed multiple severe safety and privacy vulnerabilities:
1. **Public by Default:** Anyone on or off TikTok could view videos posted by child users.
2. **Duet and Stitch Enabled:** The default settings enabled anyone on TikTok to create "Duets" and "Stitches" using a child's video content.
3. **Unverified Family Pairing:** An adult could link their account to a child's profile to control privacy settings, but TikTok never verified that the adult was a legitimate guardian, opening the door for bad actors to manipulate a minor's profile.

---

## 3. What Caught Them: Deceptive Dark Patterns

One of the most consequential findings of the TikTok investigation was the regulator's stance on **dark patterns**—deceptive user interface designs that manipulate user choices.

When children were prompted to decide whether their videos should be public or private, TikTok's interface presented a pop-up:
* The "Post Now" button (keeping the video public) was prominently colored and styled.
* The "Cancel" or "Privacy settings" link was muted and low-contrast.
* The copy subtly nudged the minor toward public exposure by emphasizing that choosing private meant followers wouldn't see their creative work.

The DPC and the European Data Protection Board (EDPB) determined that this violated the fundamental principle of **Fairness** under Article 5(1)(a).

---

## 4. The Legal Violation: Why the Fine Happened

The DPC's decision cited violations across multiple articles:

### Article 25(1) & (2) (Data Protection by Design & Default)
TikTok failed to build privacy into the core software architecture. By defaulting child profiles to public and exposing their content to unverified strangers, TikTok violated the obligation to implement the strictest privacy settings by default.

### Article 5(1)(a) (Principle of Fairness)
Using UI nudges to steer children toward selecting privacy-intrusive options is fundamentally unfair and deceptive under GDPR rules.

---

## 5. What This Means for Privacy Teams & CIPP/E Students

1. **Dark Patterns Are Now Strictly Enforced:** Subtle UI nudging, asymmetric button styling, and deceptive copy are explicit GDPR violations, especially when applied to vulnerable users like children.
2. **Identity Verification in Guardian Controls:** If your application offers parental controls or account linking, you must implement reasonable verification steps to confirm parental responsibility.
3. **Opt-In vs. Opt-Out for Social Features:** For users under the age of majority, social sharing features (comments, stitching, downloads) must be strictly opt-in.
