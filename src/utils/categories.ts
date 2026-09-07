// src/utils/categories.ts
export interface CategoryMeta {
  slug: string;
  name: string;
  shortName: string;
  icon: string;
  description: string;
  examDomain: string;
}

export const CATEGORIES: CategoryMeta[] = [
  {
    slug: 'ai-and-biometrics',
    name: 'AI, Biometrics & Facial Recognition',
    shortName: 'AI & Biometrics',
    icon: '🤖',
    description: 'Enforcement actions targeting AI model training data, biometric surveillance, facial recognition scraping, and the EU AI Act risk tiers.',
    examDomain: 'AI Governance, Biometric Special Category Data (Article 9)',
  },
  {
    slug: 'adtech-and-cookies',
    name: 'AdTech, Cookies & Profiling',
    shortName: 'AdTech & Cookies',
    icon: '🍪',
    description: 'Decisions cracking down on asymmetric cookie rejection dark patterns, real-time bidding (RTB) behavioral tracking, and pre-checked consent.',
    examDomain: 'ePrivacy Directive, Freely Given Consent & Profiling (Articles 4, 7, 21)',
  },
  {
    slug: 'telemarketing-and-spam',
    name: 'Telemarketing & Cold Outreach Spam',
    shortName: 'Telemarketing & Spam',
    icon: '📞',
    description: 'High-volume penalties for unverified marketing databases, ignoring national opt-out registries (Lista Robinson), and rogue lead procurement.',
    examDomain: 'Direct Marketing, Right to Object & Processor Audits (Articles 6, 21, 28)',
  },
  {
    slug: 'cybersecurity-and-breaches',
    name: 'Cybersecurity & Data Breaches',
    shortName: 'Cybersecurity & Breaches',
    icon: '🛡️',
    description: 'Multi-million-euro sanctions for Magecart supply-chain script injections, undetected M&A legacy breaches, and inadequate multi-factor authentication.',
    examDomain: 'Security of Processing & Incident Response (Articles 32, 33, 34)',
  },
  {
    slug: 'children-privacy',
    name: "Children & Teen Data Protection",
    shortName: "Children's Privacy",
    icon: '👶',
    description: 'Landmark penalties for public-by-default teen accounts, dark patterns in family pairing, and failure to enforce age-appropriate design standards.',
    examDomain: "Children's Consent & Fairness (Articles 5, 8, 12, 25)",
  },
  {
    slug: 'cross-border-transfers',
    name: 'Cross-Border Data Transfers',
    shortName: 'Cross-Border Transfers',
    icon: '🌐',
    description: 'The monumental €1.2B Meta transfer decision, Standard Contractual Clauses (SCCs), Schrems II jurisprudence, and US surveillance conflicts.',
    examDomain: 'Transfers of Personal Data to Third Countries (Chapter V, Articles 44–49)',
  },
  {
    slug: 'consent-and-banking',
    name: 'Consent Architecture & Financial Services',
    shortName: 'Consent & Banking',
    icon: '🏦',
    description: 'Supervisory rulings against bundled banking contracts, coerced credit profiling, and vague, pre-ticked omnibus consent mechanisms.',
    examDomain: 'Conditions for Consent & Granularity (Articles 6, 7)',
  },
  {
    slug: 'transparency-and-notice',
    name: 'Transparency & Vague Privacy Notices',
    shortName: 'Transparency & Notice',
    icon: '📜',
    description: 'Penalties for opaque multi-layered privacy policies, failure to disclose data sharing partners, and non-compliance with statutory notice duties.',
    examDomain: 'Transparent Information, Communication & Modalities (Articles 12, 13, 14)',
  },
];

export function getCategoryBySlug(slug: string): CategoryMeta | undefined {
  return CATEGORIES.find((c) => c.slug === slug);
}
