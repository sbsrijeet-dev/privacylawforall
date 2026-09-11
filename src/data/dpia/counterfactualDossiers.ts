export interface CounterfactualDossier {
  slug: string;
  company: string;
  industry: string;
  fineAmount: string;
  issuingDpa: string;
  decisionYear: number;
  systemName: string;
  fatalFlawSummary: string;
  regulatoryViolations: string[];
  actualOutcome: string;
  counterfactualDpia: {
    systemOverview: string;
    unmitigatedRisksIdentified: string[];
    mandatorySafeguardsOmitted: string[];
    compliantArchitectureDpiaSolution: string;
    dpoVerdict: string;
  };
}

export const COUNTERFACTUAL_DOSSIERS: CounterfactualDossier[] = [
  {
    slug: 'meta-cross-border-transfers',
    company: 'Meta Platforms Ireland Ltd',
    industry: 'Social Media & Global AdTech',
    fineAmount: '€1.2 Billion',
    issuingDpa: 'Data Protection Commission (DPC, Ireland) & EDPB Binding Decision 1/2023',
    decisionYear: 2023,
    systemName: 'EU-US User Data Transfer Pipeline (Facebook & Instagram)',
    fatalFlawSummary: 'Transferring hundreds of millions of European users\' personal data, messages, and photos to US cloud servers based on Standard Contractual Clauses (SCCs) without implementing supplementary technical measures capable of shielding data from US intelligence surveillance (FISA Section 702 and Executive Order 12333).',
    regulatoryViolations: ['Article 44 GDPR (General principle for transfers)', 'Article 46(1) GDPR (Transfers subject to appropriate safeguards)'],
    actualOutcome: 'Historic €1.2B fine, order to suspend all future EU-US transfers, and mandate to bring processing into compliance within 6 months.',
    counterfactualDpia: {
      systemOverview: 'Global social networking platform transmitting EU customer profile attributes, behavioral graphs, private communications, and IP telemetry to US parent infrastructure for distributed processing.',
      unmitigatedRisksIdentified: [
        'Mass surveillance and interception by US intelligence agencies under FISA 702 without judicial redress for EU data subjects (Schrems II violation)',
        'Compelled disclosure of encryption keys to foreign national security authorities',
        'Direct infringement of Charter of Fundamental Rights Articles 7 (Privacy) and 47 (Effective Judicial Protection)'
      ],
      mandatorySafeguardsOmitted: [
        'End-to-end client-side encryption where encryption keys are generated and held exclusively within the EU/EEA',
        'Data localization / sovereign EU hosting architecture for European citizen telemetry and messaging',
        'Pseudonymization split-key architecture ensuring US nodes receive only un-linkable cryptographic tokens'
      ],
      compliantArchitectureDpiaSolution: 'A compliant Transfer Impact Assessment (TIA) / DPIA would have acknowledged that standard contractual commitments alone cannot bind US foreign intelligence agencies. The DPIA would have mandated an EU Sovereign Cloud architecture where all identifiable personal data remains hosted on EU soil, and any cross-border analytics pipeline utilizes end-to-end homomorphic or split-key encryption with keys under exclusive EU custody.',
      dpoVerdict: 'REJECT / MANDATE SOVEREIGN ENCLAVE: Standard Contractual Clauses (Module 2) cannot establish legal adequacy in the US without unbreakable technical supplementary measures. Transfer pipeline cannot launch without EU key isolation.'
    }
  },
  {
    slug: 'google-france-cookie-refusal',
    company: 'Google LLC & Google Ireland Ltd',
    industry: 'Search, Video & Programmatic Advertising',
    fineAmount: '€150 Million (€90M Google LLC + €60M Google Ireland)',
    issuingDpa: 'Commission Nationale de l\'Informatique et des Libertés (CNIL, France)',
    decisionYear: 2021,
    systemName: 'Consent Management Platform (CMP) on google.fr & youtube.com',
    fatalFlawSummary: 'Architecting cookie consent banners that allowed users to "Accept All" cookies with a single prominent click, while requiring multiple clicks and navigating through obscure sub-menus to "Reject All"—violating the fundamental "Asymmetry of Effort" doctrine.',
    regulatoryViolations: ['Article 82 French Data Protection Act (transposing Article 5(3) ePrivacy Directive)', 'Article 7 GDPR (Conditions for consent)'],
    actualOutcome: '€150M in combined fines, daily penalty of €100,000 for non-compliance, and order to provide a 1-click "Reject All" button across all French surfaces.',
    counterfactualDpia: {
      systemOverview: 'Web-wide Consent Management Platform (CMP) presented to visitors on Google search and YouTube domains before setting persistent tracking cookies and advertising identifiers.',
      unmitigatedRisksIdentified: [
        'Behavioral nudging / dark patterns coercing users into unwanted tracking due to UX friction',
        'Invalidation of consent under GDPR Article 4(11) and Article 7 due to lack of freely given choice',
        'Mass unconsented profiling of user interests, viewing habits, and search history for AdTech retargeting'
      ],
      mandatorySafeguardsOmitted: [
        'Symmetric UX architecture offering equal visual prominence for "Accept All" and "Reject All" on the first layer',
        'Zero tracking script execution prior to affirmative, unambiguous positive consent action',
        'Automated consent registry recording verifiable proof of granular consent'
      ],
      compliantArchitectureDpiaSolution: 'A compliant DPIA would have evaluated the consent banner through the lens of Article 7(3) GDPR: "It shall be as easy to withdraw as to give consent." The DPIA would have tested user interaction friction and established a strict design requirement: identical single-click buttons on the first layer ("Tout accepter" vs "Tout refuser") with identical visual weight and zero tracking scripts fired before choice.',
      dpoVerdict: 'CONDITIONAL APPROVAL SUBJECT TO ASYMMETRY REMOVAL: The current multi-click rejection workflow violates French CNIL guidelines and GDPR Article 7. Deploy 1-click "Reject All" button immediately before public rollout.'
    }
  },
  {
    slug: 'hm-germany-employee-monitoring',
    company: 'H&M Hennes & Mauritz Online Shop AB & Co. KG',
    industry: 'Retail & Customer Service Center',
    fineAmount: '€35.3 Million (€35,258,708)',
    issuingDpa: 'Hamburg Commissioner for Data Protection (HmbBfDI)',
    decisionYear: 2020,
    systemName: 'Nuremberg Service Center "Welcome Back" Employee Profiling Archive',
    fatalFlawSummary: 'Conducting systematic "Welcome Back Talks" following employee absences, covertly recording intimate details of illnesses, medical diagnoses, family disputes, and religious convictions in unencrypted network shares accessible to up to 50 managers to evaluate performance and employment decisions.',
    regulatoryViolations: ['Article 5(1)(a) & (c) GDPR (Lawfulness, fairness, data minimization)', 'Article 6(1) GDPR (Lack of lawful basis)', 'Article 9(1) GDPR (Unlawful processing of health/sensitive data)', '§ 26 BDSG (German Federal Data Protection Act)'],
    actualOutcome: '€35.3M fine (second largest GDPR fine in Germany), mandatory restitution payments to affected staff, and complete purge of the surveillance dossiers.',
    counterfactualDpia: {
      systemOverview: 'Internal HR management system and shared network drive storing managerial interview logs, absence records, and performance metrics across hundreds of customer care employees.',
      unmitigatedRisksIdentified: [
        'Mass processing of Article 9 special category health and religious data without an Article 9(2) exception',
        'Workplace power imbalance rendering employee consent invalid under EDPB Criterion 7 and § 26 BDSG',
        'Excessive managerial access leading to discrimination, workplace harassment, and severe chilling effect'
      ],
      mandatorySafeguardsOmitted: [
        'Role-Based Access Control (RBAC) restricting absence records strictly to certified occupational health staff',
        'Strict data minimization prohibiting collection of personal life, family dispute, or religious information',
        'Mandatory Works Council (Betriebsrat) co-determination agreement under German BetrVG § 87'
      ],
      compliantArchitectureDpiaSolution: 'A compliant DPIA would have identified employees as vulnerable subjects under EDPB Criterion 7. It would have immediately blocked the recording of medical diagnoses or family background, established that return-to-work discussions must only record date of return and work capacity fitness, mandated Works Council co-determination, and restricted access to certified occupational health doctors under medical confidentiality.',
      dpoVerdict: 'CRITICAL FAILURE / HALT PROCESSING: Collection of private life details and medical histories lacks any lawful basis under GDPR Article 6/9 and § 26 BDSG. Shared drive files must be securely shredded immediately.'
    }
  },
  {
    slug: 'deutsche-wohnen-data-retention',
    company: 'Deutsche Wohnen SE',
    industry: 'Real Estate & Property Management',
    fineAmount: '€14.5 Million (€14,500,000)',
    issuingDpa: 'Berlin Commissioner for Data Protection (BlnBDI)',
    decisionYear: 2019,
    systemName: 'Central Tenant Property Management ERP Archive System',
    fatalFlawSummary: 'Operating an electronic archive system for residential property management that lacked any automated deletion concept or filtering mechanism, permanently retaining legacy tenant salary slips, tax records, employment contracts, and health insurance certificates years after leases were terminated.',
    regulatoryViolations: ['Article 25(1) GDPR (Data Protection by Design and by Default)', 'Article 5(1)(e) GDPR (Storage limitation principle)'],
    actualOutcome: '€14.5M fine imposed by Berlin DPA for structural architectural failure to implement an automated deletion concept (Löschkonzept).',
    counterfactualDpia: {
      systemOverview: 'Enterprise Resource Planning (ERP) database archiving tenant applications, credit reports, lease agreements, banking details, and maintenance requests across decades of residential operations.',
      unmitigatedRisksIdentified: [
        'Permanent retention of sensitive financial and tax documents decades past statutory limitation periods',
        'Systemic violation of Article 25(1) Privacy by Design due to monolithic legacy database architecture',
        'Extreme blast radius in the event of ransomware or credential compromise of the central ERP server'
      ],
      mandatorySafeguardsOmitted: [
        'Technical Deletion Concept (Löschkonzept) compliant with DIN 66398 data deletion standards',
        'Automated lifecycle tiering: Active Tenant -> Statutory Retention (Tax/Commercial) -> Permanent Purge',
        'Database schema partitioning separating active rental operations from historical accounting archives'
      ],
      compliantArchitectureDpiaSolution: 'A compliant DPIA would have audited the database architecture against Article 25(1) before system deployment. It would have mandated an automated data lifecycle scheduler: upon tenant lease termination, all salary slips and identity proofs are purged within 6 months; tax-relevant payment ledgers are moved to an isolated, read-only accounting silo with an automated 10-year hard deletion trigger under German HGB § 257.',
      dpoVerdict: 'ARCHITECTURAL REJECTION: Monolithic ERP system violates Article 25(1) and Article 5(1)(e). System cannot be approved until automated data tiering and irreversible scheduled deletion are engineered and tested.'
    }
  },
  {
    slug: 'criteo-adtech-consent-chains',
    company: 'Criteo SA',
    industry: 'Programmatic Advertising & Behavioral Retargeting',
    fineAmount: '€40 Million (€40,000,000)',
    issuingDpa: 'Commission Nationale de l\'Informatique et des Libertés (CNIL, France)',
    decisionYear: 2023,
    systemName: 'Criteo Cross-Site Behavioral Retargeting & Cookie Graph',
    fatalFlawSummary: 'Building behavioral profiles on over 370 million internet users across thousands of partner websites via tracking cookies without independently verifying that partner websites had actually collected valid user consent, while failing to honor user erasure and objection requests across the cookie graph.',
    regulatoryViolations: ['Article 7(1) GDPR (Demonstrating consent)', 'Article 12(1) & 13 GDPR (Transparency and notice)', 'Article 17(1) GDPR (Right to erasure)', 'Article 21(1) GDPR (Right to object)'],
    actualOutcome: '€40M fine by CNIL for failure to demonstrate valid consent chain verification and failure to respect data subject rights in real-time bidding.',
    counterfactualDpia: {
      systemOverview: 'Algorithmic retargeting infrastructure processing real-time bidding (RTB) bid requests, device fingerprints, and browsing history to display personalized banner ads across partner publisher sites.',
      unmitigatedRisksIdentified: [
        'Mass covert profiling without verifiable consent, relying on blind contractual assumptions with publishers',
        'Failure to propagate Article 17 erasure signals across the graph, retaining historical user interest tags',
        'Severe lack of transparency where individuals had no insight into how their identities were matched across domains'
      ],
      mandatorySafeguardsOmitted: [
        'Real-time automated Consent String verification before bidding on or processing any partner cookie event',
        'Contractual audit mechanisms and technical sampling to verify publisher CMP compliance',
        'Instantaneous global revocation pipeline syncing opt-outs across the Criteo Identity Graph'
      ],
      compliantArchitectureDpiaSolution: 'A compliant DPIA would have recognized that joint responsibility / processor chains require active verification of consent (Article 7(1)). The DPIA would have engineered an automated gatekeeper: bid requests lacking a cryptographically valid IAB TCF consent string are immediately dropped with zero processing. Furthermore, an automated subject rights portal would instantly purge cookie IDs across all downstream DSP nodes upon receipt of an opt-out.',
      dpoVerdict: 'HALT UNTIL VERIFICATION GATEWAY DEPLOYED: Processing cannot rely on unverified publisher promises. Consent verification gateway and automated graph-wide erasure API must be fully operational prior to production bidding.'
    }
  }
];
