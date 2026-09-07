---
title: "Marriott £18.4M Fine: UK ICO Penalizes Negligent M&A Cybersecurity Due Diligence"
case_name: "Penalty Notice COM0783543 (Marriott International, Inc.)"
popular_name: "Marriott £18.4M Starwood Breach Decision"
dpa: "Information Commissioner's Office (ICO)"
country: "United Kingdom"
jurisdiction: "UK GDPR"
fine_amount: "£18,400,000"
fine_magnitude: "£18.4 Million"
decision_date: "2020-10-30"
year: 2020
articles_cited: ["Article 5", "Article 32"]
exam_domain: "Security of Processing & M&A Due Diligence (Article 32)"
tldr: "The UK ICO fined Marriott £18.4M after hackers compromised 339 million guest records via an undetected Starwood vulnerability inherited during a 2016 corporate acquisition."
is_top_5: false
category: "cybersecurity-and-breaches"
source_url: "https://ico.org.uk/action-weve-taken/enforcement/marriott-international-inc/"
verified: true
---

## The Case at a Glance

In October 2020, the UK's **Information Commissioner's Office (ICO)** issued an **£18,400,000** fine against global hospitality leader **Marriott International, Inc.** The penalty resolved a massive data breach that exposed an estimated **339 million hotel guest records** globally, including roughly 7 million UK residents.

The decision established a critical international legal precedent: **corporate acquirers inherit the data protection liabilities and cybersecurity shortcomings of the companies they buy.**

---

## What Happened: The Starwood Legacy Breach

In 2014, an unknown threat group compromised the IT network of the Starwood hotel group by installing a remote access trojan (RAT) and memory-scraping malware.

In 2016, Marriott acquired Starwood for $13.6 billion. However, during the acquisition process:
1. **Inadequate Technical Due Diligence**: Marriott failed to perform an exhaustive, independent cybersecurity audit of Starwood's legacy database systems.
2. **Undetected Presence for 4 Years**: The attackers remained inside the Starwood guest reservation database for over four years, undetected, siphoning unencrypted passport numbers, credit card expiry dates, and travel itineraries.
3. **Flawed Access Controls**: The database contained unsegmented guest records, weak server administrator passwords, and unencrypted sensitive data fields.

The breach was only discovered in September 2018 when an automated database security alert was triggered—two years after Marriott completed the acquisition.

---

## Key Legal Findings Under GDPR Article 32

### 1. Multi-Factor Authentication & Account Monitoring
The ICO found that Marriott had failed to enforce multi-factor authentication (MFA) on critical administrative endpoints within the Starwood network, allowing attackers to move laterally with compromised service accounts.

### 2. Failure of Ongoing Database Encryption
Although credit card numbers were protected by encryption, the decryption keys were stored on the exact same server cluster, rendering the protection useless once the host was compromised.

---

## Strategic Takeaways for Executives & Privacy Architects

* **Cybersecurity Due Diligence is Mandatory in M&A**: Buyers must conduct deep forensic penetration tests and architecture reviews of target companies before completing acquisitions.
* **Separate Decryption Keys**: Never store private decryption keys in the same physical or logical environment as encrypted customer databases.
* **CIPP/E / CIPT Focus**: Article 32 requires security measures appropriate to risk. Storing hundreds of millions of passports without strict network segmentation is an automatic breach of duty.
