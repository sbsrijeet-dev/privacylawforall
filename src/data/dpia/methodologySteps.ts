export interface MethodologyPart {
  partNumber: number;
  statutoryAnchor: string;
  title: string;
  subtitle: string;
  coreObjective: string;
  mandatoryDeliverables: string[];
  keyQuestions: string[];
  fatalPitfalls: string[];
  regulatoryCheck: string;
}

export const DPIA_METHODOLOGY_STEPS: MethodologyPart[] = [
  {
    partNumber: 1,
    statutoryAnchor: 'Article 35(7)(a) GDPR',
    title: 'Systematic Description of the Processing',
    subtitle: 'Context, Nature, Scope, Purposes & Data Flows',
    coreObjective: 'Establish an end-to-end, technical and operational picture of what happens to personal data from initial ingestion to final destruction.',
    mandatoryDeliverables: [
      'Comprehensive data flow diagram showing ingress, internal microservices, third-party APIs, and egress points',
      'Granular data inventory categorized by Article 6 personal data and Article 9 special categories',
      'Identification of all actors: Data Controller, Joint Controllers, Data Processors, Sub-processors',
      'Geographical map of all physical data center locations and cross-border transfer mechanisms'
    ],
    keyQuestions: [
      'What specific categories of personal data are collected, and through what technical channels?',
      'Who has read, write, and export access to the dataset across internal teams and external vendors?',
      'How long is each category of data stored, and what triggers its physical deletion?'
    ],
    fatalPitfalls: [
      'High-level hand-waving descriptions ("we collect user info to improve services")',
      'Ignoring data processor sub-flows, background analytics SDKs, and error logging services',
      'Omitting third-country server locations and cloud provider fallback zones'
    ],
    regulatoryCheck: 'Under EDPB WP248, a DPIA that lacks a concrete architecture and data flow diagram is prima facie incomplete.'
  },
  {
    partNumber: 2,
    statutoryAnchor: 'Article 35(7)(b) GDPR',
    title: 'Necessity & Proportionality Assessment',
    subtitle: 'Lawful Basis, Data Minimization & Subject Rights',
    coreObjective: 'Demonstrate that the chosen processing is legally justifiable under Article 6 and that the same objectives cannot be achieved using less intrusive means.',
    mandatoryDeliverables: [
      'Explicit lawful basis mapping under Article 6(1)(a)-(f) for every individual processing purpose',
      'Documented Article 9(2) exception if processing special category biometric, health, or sensitive data',
      'Proportionality balancing test (especially when relying on Article 6(1)(f) Legitimate Interests)',
      'Data minimization justification explaining why each collected data field is strictly necessary'
    ],
    keyQuestions: [
      'Can the stated business goal be achieved with anonymized or aggregated data instead?',
      'Is consent freely given, granular, and as easy to withdraw as to give (as mandated by CNIL/AEPD)?',
      'What automated mechanism allows individuals to exercise their rights (access, erasure, objection)?'
    ],
    fatalPitfalls: [
      'Claiming "Legitimate Interests" without conducting and documenting a formal 3-part Legitimate Interest Assessment (LIA)',
      'Bundling consent for core service delivery with marketing or third-party behavioral tracking',
      'Failing to establish a lawful basis for secondary processing purposes (Article 5(1)(b))'
    ],
    regulatoryCheck: 'The CJEU (Meta v. Bundeskartellamt C-252/21) ruled that behavioral advertising cannot be shoehorned into "contractual necessity" (Art 6(1)(b)).'
  },
  {
    partNumber: 3,
    statutoryAnchor: 'Article 35(9) GDPR',
    title: 'Stakeholder & Subject Consultation Strategy',
    subtitle: 'Gathering Views of Affected Individuals & Workers',
    coreObjective: 'Document meaningful consultation with data subjects, employee representatives, and internal engineering stakeholders before deployment.',
    mandatoryDeliverables: [
      'Record of consultation with data subjects or their legitimate representatives (or documented justification if consultation is deemed inappropriate)',
      'Works Council (Betriebsrat) consultation agreement if deploying workplace tech in Germany (§ 26 BDSG / BetrVG § 87)',
      'Customer feedback surveys, UX testing records, or consumer advocacy panel reviews'
    ],
    keyQuestions: [
      'Have the individuals whose data will be monitored or profiled been given a forum to raise concerns?',
      'If consultation was not performed, what specific commercial or security rationale justifies the omission?',
      'Did employee representatives participate in defining monitoring thresholds and access controls?'
    ],
    fatalPitfalls: [
      'Treating consultation as an afterthought or skipping it entirely without documented justification',
      'Deploying workplace surveillance tools without Works Council co-determination in Germany',
      'Ignoring feedback from vulnerable user groups (minors, elderly, patients)'
    ],
    regulatoryCheck: 'Hamburg DPA fined H&M €35.3M partly because covert employee profiling completely bypassed employee representatives and worker scrutiny.'
  },
  {
    partNumber: 4,
    statutoryAnchor: 'Article 35(7)(c) GDPR',
    title: 'Comprehensive Risk Identification & Assessment',
    subtitle: 'Severity, Likelihood & Impact on Rights and Freedoms',
    coreObjective: 'Identify specific, plausible threat scenarios that could infringe upon the fundamental rights and freedoms of individuals, evaluating likelihood vs severity.',
    mandatoryDeliverables: [
      'Risk Matrix (4x4 or 5x5) evaluating Likelihood (Rare to Probable) against Severity (Negligible to Critical)',
      'Detailed harm scenarios: discrimination, financial loss, identity theft, loss of confidentiality, reputation damage, psychological stress, chilling effect on freedom of expression',
      'Specific threat modeling: unauthorized access, insider misuse, data corruption, vendor breach, mission creep'
    ],
    keyQuestions: [
      'What is the worst-case real-world harm to an individual if this dataset is leaked, corrupted, or abused?',
      'How likely is an insider or malicious actor to compromise the security perimeter?',
      'Does the processing create algorithmic bias or disparate impact against protected classes?'
    ],
    fatalPitfalls: [
      'Vague, generic risk descriptions ("there is a risk of a data breach")',
      'Conflating business risk to the company (fines, PR damage) with risks to the rights of natural persons',
      'Downplaying high-severity harms by claiming likelihood is low without verifiable technical evidence'
    ],
    regulatoryCheck: 'Article 35 focuses on risks to the "rights and freedoms of natural persons", NOT commercial or financial risk to the corporation.'
  },
  {
    partNumber: 5,
    statutoryAnchor: 'Article 35(7)(d) GDPR',
    title: 'Mitigating Technical & Organizational Safeguards',
    subtitle: 'Controls, Architecture, Encryption & Deletion Concepts',
    coreObjective: 'Specify concrete, actionable technical and organizational safeguards designed to eliminate risks or reduce them to an acceptable residual level.',
    mandatoryDeliverables: [
      'Cryptographic architecture: Encryption at rest (AES-256), in transit (TLS 1.3), and key management isolation',
      'Strict Role-Based Access Control (RBAC) and Least-Privilege administrative policies',
      'Pseudonymization and tokenization pipelines separating direct identifiers from analytical attributes',
      'Automated technical deletion concept (Löschkonzept) enforcing strict data retention caps'
    ],
    keyQuestions: [
      'Does each identified risk have at least one dedicated, verifiable mitigating control?',
      'Are safeguards already implemented in code, or merely aspirational roadmap promises?',
      'Are vendor processors bound by strict Article 28 DPAs with contractual audit rights?'
    ],
    fatalPitfalls: [
      'Vague mitigation statements ("we will implement reasonable security measures")',
      'Promising future safeguards that do not exist at the time the system is deployed',
      'Failing to implement automated data deletion, leading to permanent archive bloat (Deutsche Wohnen €14.5M)'
    ],
    regulatoryCheck: 'Berlin DPA fined Deutsche Wohnen €14.5M because holding tenant data in monolithic systems without a technical deletion concept violated Article 25.'
  },
  {
    partNumber: 6,
    statutoryAnchor: 'Article 35 & EDPB Precedents',
    title: 'Regulatory Precedent & Enforcement Cross-Referencing',
    subtitle: 'Grounding the Assessment in European Case Law',
    coreObjective: 'Benchmarking the proposed processing against relevant published enforcement decisions and DPA guidance to identify established legal red lines.',
    mandatoryDeliverables: [
      'Cross-reference against relevant CJEU rulings (Schrems II C-311/18, Google Spain C-131/12, Fashion ID C-40/17)',
      'Cross-reference against landmark national DPA fines (Meta €1.2B, Amazon €746M, H&M €35.3M, Criteo €40M)',
      'Review against national DPA Article 35(4) Blacklists (DSK, CNIL, AEPD, Garante, ICO)'
    ],
    keyQuestions: [
      'Has a European DPA previously sanctioned an identical or similar processing activity?',
      'What specific operational failures led to penalties in peer industry cases?',
      'How does this system prove it avoids the specific legal pitfalls identified in regulatory rulings?'
    ],
    fatalPitfalls: [
      'Conducting a DPIA in a regulatory vacuum without reviewing published DPA enforcement cases',
      'Ignoring cross-border transfer implications after CJEU Schrems II',
      'Assuming that competitor industry practices are legally compliant without checking DPA opinions'
    ],
    regulatoryCheck: 'Referencing published supervisory authority enforcement decisions and peer fines demonstrates rigorous regulatory due diligence.'
  },
  {
    partNumber: 7,
    statutoryAnchor: 'Article 35(2) GDPR',
    title: 'Data Protection Officer (DPO) Formal Opinion',
    subtitle: 'Independent Advice, Recommendations & Consultation Audit',
    coreObjective: 'Seek, record, and integrate the formal written opinion of the Data Protection Officer regarding whether the processing should proceed and under what conditions.',
    mandatoryDeliverables: [
      'Formal written DPO Assessment stating whether the DPIA is complete, accurate, and legally sound',
      'Documented DPO recommendations for additional technical or organizational safeguards',
      'Controller response: explicit acceptance of recommendations or documented executive rationale for divergence',
      'Determination of whether residual risk triggers mandatory Prior Consultation with the DPA under Article 36'
    ],
    keyQuestions: [
      'Was the DPO involved from the project inception, or brought in at the last minute to rubber-stamp?',
      'Did the DPO identify any unmitigated high risks that require supervisory authority consultation?',
      'If management overruled a DPO recommendation, is the detailed commercial and legal rationale formally logged?'
    ],
    fatalPitfalls: [
      'Omitting the DPO consultation record entirely',
      'Treating the DPO as a rubber stamp without giving them full architectural visibility',
      'Failing to initiate Article 36 Prior Consultation when unmitigated high risks remain'
    ],
    regulatoryCheck: 'Under Article 38(3), the DPO must report directly to the highest management level, and their advice must be formally documented.'
  },
  {
    partNumber: 8,
    statutoryAnchor: 'Article 35(11) GDPR',
    title: 'Sign-Off, Residual Risk Acceptance & Review Schedule',
    subtitle: 'Living Document Governance & Executive Accountability',
    coreObjective: 'Formal executive sign-off accepting residual risk, combined with a defined trigger schedule to review and update the DPIA as the system evolves.',
    mandatoryDeliverables: [
      'Formal signature block: Project Lead, Information Security Officer (CISO), and Data Controller Executive',
      'Residual Risk Summary table showing Initial Risk vs Residual Risk after safeguards',
      'Periodic review schedule (at least every 24 months, or immediately upon major architectural changes)',
      'Defined trigger events requiring an immediate DPIA review (new vendor, new data fields, AI model retrain)'
    ],
    keyQuestions: [
      'Who in senior management is formally accepting the residual risk on behalf of the legal entity?',
      'What technical monitoring flags when the processing drifts beyond the parameters described in this DPIA?',
      'When is the next mandatory audit of this DPIA scheduled?'
    ],
    fatalPitfalls: [
      'Treating the DPIA as a "one-and-done" static compliance exercise that is filed away and forgotten',
      'Failing to update the DPIA when introducing new algorithms, third-party integrations, or user bases',
      'Lack of executive sign-off leaving accountability ambiguous'
    ],
    regulatoryCheck: 'Article 35(11) explicitly mandates controllers to carry out a review when there is a change of the risk represented by processing operations.'
  }
];
