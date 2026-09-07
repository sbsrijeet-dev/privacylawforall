---
title: "The €405M Teen Privacy Blunder: How Instagram Leaked Children's Contact Info"
case_name: "Meta Platforms Ireland Limited - Instagram Teen Accounts (DPC Decision IN-20-8-1)"
popular_name: "Instagram €405M Child Privacy Fine"
dpa: "Data Protection Commission"
country: "Ireland"
jurisdiction: "EU GDPR"
fine_amount: "€405,000,000"
fine_magnitude: "405M"
decision_date: "2022-09-02"
year: 2022
articles_cited: ["Article 5(1)(c)", "Article 6(1)", "Article 12", "Article 24", "Article 25"]
exam_domain: "Data Protection by Design & Minors' Data (CIPP/E Domain II & IV)"
tldr: "Instagram let teenagers switch to 'business accounts' to see analytics, which automatically published their private phone numbers and email addresses to the global web."
is_top_5: true
top_5_rank: 3
category: "children-privacy"
source_url: "https://www.dataprotection.ie/en/news-media/press-releases/dpc-fines-instagram-405-million"
verified: true
---

## At a Glance

* **The Offender:** Meta Platforms Ireland Limited (Instagram)
* **The Authority:** Irish Data Protection Commission (DPC)
* **The Penalty:** €405,000,000 (€405 Million) + order to bring processing into compliance
* **The Core Issue:** Default public account settings for teenage users and exposing children's phone numbers and email addresses on "business" profiles.

---

## 1. The TL;DR in Plain English

Millions of teenagers on Instagram wanted to see cool analytics—like how many people viewed their posts or where their followers lived. To get those metrics, Instagram told them to switch from a personal account to a "business account."

What Instagram didn't make clear was that business accounts were designed for stores and influencers, meaning the account holder's real email address and phone number were displayed publicly to anyone on the internet. Furthermore, by default, all teen accounts were set to "Public." The Irish DPC issued a blistering **€405 Million fine** for failing to protect children by default.

---

## 2. The Story: What Happened?

Under the GDPR, children merit specific protection regarding their personal data, as they may be less aware of the risks, consequences, and safeguards involved.

Data scientist David Stier discovered in 2019 that Instagram was exposing the private contact details of estimated millions of users under the age of 18. When teenagers aged 13 to 17 switched their profiles to "business" status to unlock follower statistics, Instagram required a public email and phone number and displayed them openly on the profile page.

Even worse, hackers and data brokers were able to scrape these phone numbers and emails directly from the HTML source code of Instagram web pages.

---

## 3. What Caught Them?

The Irish DPC launched an inquiry focusing on two fatal flaws:
1. **Public by Default:** When any teenager registered an Instagram account, Instagram's sign-up flow defaulted their account privacy settings to "Public." Anyone in the world could see their posts, stories, followers, and comments unless the child manually navigated into deep settings menus to flip it to "Private."
2. **Exposed Business Contacts:** The business account onboarding failed to warn children in plain language that entering their real mobile number would expose it to billions of strangers.

---

## 4. The Legal Violation: Why the Fine Happened

Regulators found Instagram in direct violation of:

### Article 25 (Data Protection by Design and by Default)
Controllers must implement appropriate technical and organisational measures to ensure that, **by default**, only personal data necessary for each specific purpose is processed. Setting a minor's profile to public by default violates this principle completely.

### Article 5(1)(c) (Data Minimisation)
Requiring or encouraging teenagers to expose phone numbers and emails to anyone on the web exceeded what was adequate, relevant, and limited to operating a social profile.

### Article 12(1) (Transparent Information to Children)
Privacy policies and warnings must be concise, transparent, and written in clear and plain language that a child can easily comprehend.

---

## 5. What This Means for Privacy Teams & CIPP/E Students

1. **Child-Centric Privacy by Default:** If your service is accessible to minors, default settings *must* be set to the highest privacy tier automatically.
2. **Age-Appropriate Design Matters:** You cannot rely on complex adult legal disclaimers when onboarding teenagers.
3. **Feature Gating for Minors:** Advanced metrics and business features must not come at the expense of stripping away protective privacy guardrails for young users.
