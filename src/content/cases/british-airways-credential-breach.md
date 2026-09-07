---
title: "The 22-Line Script That Cost British Airways £20 Million: The Article 32 Security Deep Dive"
case_name: "British Airways Plc - Data Breach Investigation (ICO Penalty Notice COM0783542)"
popular_name: "British Airways £20M Security Breach"
dpa: "ICO"
country: "United Kingdom"
jurisdiction: "UK GDPR"
fine_amount: "£20,000,000"
fine_magnitude: "20M"
decision_date: "2020-10-16"
year: 2020
articles_cited: ["Article 5(1)(f)", "Article 32", "Article 83"]
exam_domain: "Security of Processing & Incident Response (CIPP/E Domain IV)"
tldr: "Hackers injected a tiny 22-line JavaScript script into British Airways' website, harvesting 400,000 customers' credit cards for over two months because BA failed to implement multi-factor authentication."
is_top_5: false
category: "cybersecurity-and-breaches"
source_url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2020/10/ico-fines-british-airways-20m-for-data-breach-affecting-more-than-400-000-customers/"
verified: true
---

## At a Glance

* **The Offender:** British Airways Plc
* **The Authority:** Information Commissioner's Office (ICO), United Kingdom
* **The Penalty:** £20,000,000 (~€22 Million), reduced from an initial notice of £183M due to COVID-19 economic impact
* **The Core Issue:** Failing to secure technical infrastructure with multi-factor authentication (MFA), allowing hackers to siphon customer payment data for over 60 days undetected.

---

## 1. The TL;DR in Plain English

In the summer of 2018, attackers gained access to a British Airways employee account. Using compromised credentials, they moved laterally across BA's network and injected just 22 lines of malicious code into the BA payment page. 

Every time a customer entered their name, address, credit card number, and CVV code to book a flight, the data was secretly copied and sent to a fraudulent website. Over 400,000 travelers were compromised. Even worse: British Airways didn't discover the breach themselves—a third-party cybersecurity researcher alerted them two months later. The ICO imposed a **£20 Million penalty**.

---

## 2. The Story: What Happened?

The attack was a classic **Magecart** digital supply chain and payment skimming intrusion:

1. **Initial Breach:** In June 2018, attackers compromised the login credentials of an employee belonging to a third-party catering and supply company.
2. **No Multi-Factor Authentication:** British Airways did not require multi-factor authentication (MFA) on its remote access gateway. The single compromised password gave attackers entry into BA's internal network.
3. **Privilege Escalation & Plaintext Secrets:** The attackers found administrator credentials stored in plaintext files on internal servers, allowing them to modify the live JavaScript code running on `ba.com` and the mobile app.
4. **The Skimmer:** Attackers injected code that silently routed payment card entries to an external domain (`baways.com`) registered by the hackers.

---

## 3. What Caught Them: External Notification & Basic Hygiene Failures

The ICO's forensic audit highlighted that British Airways' cybersecurity defenses failed the most basic standards of hygiene:

* **No File Integrity Monitoring (FIM):** The malicious script altered production code on the checkout page, yet no automated system detected the unauthorized file change.
* **No Network Whitelisting:** The payment page was allowed to transmit data to an unknown external server without triggering firewall alarms.
* **Failure to Detect:** The skimmer ran silently from June 22 to September 5, 2018. If a third-party security firm had not contacted BA, the breach could have continued indefinitely.

---

## 4. The Legal Violation: Why the Fine Happened

The ICO grounded the penalty in fundamental security obligations:

### Article 32 (Security of Processing)
Controllers must implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk. The ICO noted that measures like MFA, whitelisting, and code auditing are low-cost, industry-standard protections that BA simply neglected.

### Article 5(1)(f) (Integrity and Confidentiality)
Personal data must be processed in a manner that ensures appropriate security, including protection against unauthorised or unlawful processing, accidental loss, or destruction.

---

## 5. What This Means for Privacy Teams & CIPP/E Students

1. **MFA is Legally Non-Negotiable:** Regulators view multi-factor authentication on remote gateways as basic due diligence. Failing to implement MFA virtually guarantees liability in a credential-based breach.
2. **Supply Chain & Third-Party Access:** Third-party vendor credentials must be segregated with least-privilege permissions and tight network access controls.
3. **Detection Speed Directly Influences Fine Size:** Failing to detect an ongoing data breach internally for months demonstrates inadequate technical monitoring and significantly aggravates the penalty under Article 83(2).
