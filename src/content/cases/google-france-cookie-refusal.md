---
title: "The Cookie Trap: Why France's CNIL Fined Google €150 Million Over One Single Button"
case_name: "Google LLC & Google Ireland - Cookie Refusal Dark Patterns (CNIL Decision SAN-2021-023)"
popular_name: "Google €150M Cookie Button Fine"
dpa: "CNIL"
country: "France"
jurisdiction: "EU GDPR"
fine_amount: "€150,000,000"
fine_magnitude: "150M"
decision_date: "2021-12-31"
year: 2021
articles_cited: ["Article 82 (French Data Protection Act)", "Article 7(3) GDPR", "Article 4(11) GDPR"]
exam_domain: "ePrivacy & Cookies (CIPP/E Domain II)"
tldr: "Google made accepting tracking cookies a single click, but buried the 'Reject' option behind multiple confusing menus. France ruled that saying 'No' must be just as easy as saying 'Yes'."
is_top_5: false
category: "adtech-and-cookies"
source_url: "https://www.cnil.fr/en/cookies-cnil-fines-google-total-150-million-euros"
verified: true
---

## At a Glance

* **The Offender:** Google LLC (€90M) & Google Ireland Limited (€60M)
* **The Authority:** Commission Nationale de l'Informatique et des Libertés (CNIL), France
* **The Penalty:** €150,000,000 (€150 Million) + daily penalty of €100,000 for delays
* **The Core Issue:** Asymmetric consent banners where accepting cookies took one instant click, while rejecting cookies required multiple clicks and confusing navigation.

---

## 1. The TL;DR in Plain English

Have you ever visited a website where a giant banner said "Accept All Cookies" in bright blue, but to decline cookies you had to click "Options," scroll through fifty checkboxes, and click "Save Choices"?

In France, the CNIL inspected Google.fr and YouTube. They found that users could accept tracking in one second with a single click on "Accept all," but refusing cookies required multiple clicks through deep sub-menus. The French regulator ruled that manipulative cookie designs violate the law and fined Google **€150 Million**.

---

## 2. The Story: What Happened?

Under European rules (the ePrivacy Directive Article 5(3) implemented in national law, read together with GDPR consent standards), storing or accessing information on a user's terminal device (like cookies or device fingerprints) requires the user's prior, freely given, and informed consent.

During online inspections conducted in 2021, the CNIL noticed that on both Google Search and YouTube:
* The consent banner offered a prominent, direct button: **"J'accepte" (I accept)**.
* There was **no equivalent "Reject all" button** on the initial banner.
* To refuse cookies, French visitors had to click "Personnaliser" (Customize), which navigated to a second screen with complex descriptions and a secondary button to confirm preferences.

---

## 3. What Caught Them: "Asymmetry of Effort"

The CNIL established a simple, groundbreaking legal doctrine: **Asymmetry of Effort**.

When refusing cookies requires more time, more clicks, and more mental effort than accepting them, the consent is no longer freely given. The user interface actively nudges and fatigues the user into clicking "Accept All" just to get rid of the annoying banner.

The CNIL gave Google 3 months to introduce a simple, direct **"Refuse all" (Tout refuser)** button on the very first layer of the banner, backed by a €100,000 daily penalty for non-compliance.

---

## 4. The Legal Violation: Why the Fine Happened

The decision was issued under Section 82 of the French Data Protection Act (transposing the ePrivacy Directive), interpreted in light of GDPR consent rules:

### Article 4(11) & Article 7(3) GDPR (Conditions for Consent)
Consent must be freely given. Article 7(3) explicitly stipulates that **it shall be as easy to withdraw as to give consent**. By extension, the initial refusal of consent must be just as direct and accessible as granting it.

### Freedom of Choice
Nudging mechanisms compromise the genuine freedom of choice of users who want to search the internet without being followed by ad-tracking beacons across the web.

---

## 5. What This Means for Privacy Teams & CIPP/E Students

1. **Equal Prominence on Cookie Banners:** Your "Reject All" button must be on the **first layer**, with the **same color weight, font size, and visual prominence** as "Accept All."
2. **ePrivacy vs. GDPR Jurisdiction:** Cookie violations often fall under the ePrivacy Directive. This allows individual national authorities like France's CNIL to issue fines directly without going through the GDPR's "One-Stop-Shop" mechanism.
3. **No "Legitimate Interest" for Tracking:** Ad-tech cookies, analytics cookies, and marketing pixels can never rely on legitimate interest; prior opt-in consent is strictly mandatory.
