export interface StatutoryTrigger {
  id: string;
  article: string;
  title: string;
  description: string;
  examples: string[];
  severity: 'automatic_mandatory';
}

export interface EdpbCriterion {
  id: string;
  number: number;
  name: string;
  guidelineAnchor: string;
  description: string;
  example: string;
  riskFactor: string;
}

export const ARTICLE_35_3_TRIGGERS: StatutoryTrigger[] = [
  {
    id: 'art35_3_a',
    article: 'Article 35(3)(a) GDPR',
    title: 'Systematic & Extensive Profiling with Significant Effects',
    description: 'A systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based that produce legal effects concerning the natural person or similarly significantly affect the natural person.',
    examples: [
      'Automated credit scoring or loan refusal systems',
      'AI-driven candidate pre-screening and CV rejection in hiring',
      'E-recruitment algorithms predicting performance or churn',
      'Dynamic behavioral price discrimination systems'
    ],
    severity: 'automatic_mandatory'
  },
  {
    id: 'art35_3_b',
    article: 'Article 35(3)(b) GDPR',
    title: 'Large-Scale Processing of Special Category or Criminal Data',
    description: 'Processing on a large scale of special categories of data referred to in Article 9(1) (health, biometric, genetic, religious, political, ethnic, sexual orientation) or of personal data relating to criminal convictions and offences referred to in Article 10.',
    examples: [
      'Hospital central patient records management systems',
      'Mass facial recognition or biometric authentication databases',
      'Genetic testing and direct-to-consumer ancestry profiling platforms',
      'Background check databases consolidating criminal records'
    ],
    severity: 'automatic_mandatory'
  },
  {
    id: 'art35_3_c',
    article: 'Article 35(3)(c) GDPR',
    title: 'Systematic Monitoring of Publicly Accessible Areas on a Large Scale',
    description: 'A systematic monitoring of a publicly accessible area on a large scale.',
    examples: [
      'City-wide smart CCTV networks with automated vehicle license plate recognition (ALPR)',
      'Drone-based aerial surveillance over public plazas or transport hubs',
      'Wi-Fi or Bluetooth tracking beacons in shopping malls and transit stations',
      'In-store foot-traffic behavioral tracking using computer vision'
    ],
    severity: 'automatic_mandatory'
  }
];

export const EDPB_NINE_CRITERIA: EdpbCriterion[] = [
  {
    id: 'criterion_1',
    number: 1,
    name: 'Evaluation or Scoring',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 1',
    description: 'Profiling, predicting, and scoring aspects of performance, economic situation, health, personal preferences, reliability, behavior, or location.',
    example: 'Financial institution scoring customer creditworthiness or marketing platform building predictive behavioral personas.',
    riskFactor: 'High likelihood of discrimination, denial of services, or covert tracking.'
  },
  {
    id: 'criterion_2',
    number: 2,
    name: 'Automated Decision-Making with Legal or Similar Effect',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 2',
    description: 'Processing that aims to take decisions on data subjects producing legal effects or significantly affecting them, outside Article 35(3)(a).',
    example: 'Automated cancellation of insurance coverage or programmatic exclusion from public benefits.',
    riskFactor: 'Subject alienation, lack of human oversight, and algorithmic bias.'
  },
  {
    id: 'criterion_3',
    number: 3,
    name: 'Systematic Monitoring',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 3',
    description: 'Processing used to observe, monitor, or control data subjects continuously, including data collected through networks or public spaces.',
    example: 'Workplace employee monitoring software (keystroke logging, webcam snapshots) or connected vehicle telematics.',
    riskFactor: 'Severe psychological pressure, loss of autonomy, and constant surveillance.'
  },
  {
    id: 'criterion_4',
    number: 4,
    name: 'Sensitive Data or Highly Personal Data',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 4',
    description: 'Article 9 special category data, Article 10 criminal data, as well as data of a highly personal nature such as financial records, electronic communication metadata, or precise location data.',
    example: 'Dating apps processing sexual preferences, mobile apps tracking real-time GPS coordinates, or financial budgeting apps.',
    riskFactor: 'Permanent stigma, identity theft, and severe invasion of the private sphere.'
  },
  {
    id: 'criterion_5',
    number: 5,
    name: 'Data Processed on a Large Scale',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 5',
    description: 'Evaluating scale via 4 factors: number of data subjects, volume/range of data items, duration/permanence of processing, and geographical extent.',
    example: 'Nationwide telecom logging customer metadata or social media platform tracking millions of daily users.',
    riskFactor: 'Mass systemic exposure in case of security breaches or abuse.'
  },
  {
    id: 'criterion_6',
    number: 6,
    name: 'Matching or Combining Datasets',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 6',
    description: 'Originating from two or more data processing operations performed for different purposes or by different controllers in a way that exceeds reasonable expectations.',
    example: 'Data brokers matching offline retail transaction records with online browsing behavior.',
    riskFactor: 'Total loss of context, breach of purpose limitation (Article 5(1)(b)), and covert re-identification.'
  },
  {
    id: 'criterion_7',
    number: 7,
    name: 'Data Concerning Vulnerable Subjects',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 7',
    description: 'Where an increased power imbalance exists between the subject and controller, making free consent or resistance difficult (children, employees, patients, elderly, asylum seekers).',
    example: 'School ed-tech platforms tracking student performance or employer logging employee sickness patterns.',
    riskFactor: 'Inability to give freely given consent, risk of exploitation or institutional retaliation.'
  },
  {
    id: 'criterion_8',
    number: 8,
    name: 'Innovative Use or Applying New Technological Solutions',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 8',
    description: 'Combining new technology (or novel forms of using existing tech) with personal data where personal and social consequences are not yet fully understood.',
    example: 'Deploying Large Language Models (LLMs) on customer communications or smart home IoT voice assistants.',
    riskFactor: 'Unpredictable emergent risks, hallucinations, and lack of established regulatory guardrails.'
  },
  {
    id: 'criterion_9',
    number: 9,
    name: 'Processing that Prevents Exercising a Right or Using a Service',
    guidelineAnchor: 'EDPB WP248 rev.01 - Criterion 9',
    description: 'Processing operations that aim at allowing, modifying, or refusing data subjects access to a service or into a contract.',
    example: 'Screening bank customers against an anti-fraud database before allowing account creation.',
    riskFactor: 'Complete exclusion from essential financial, employment, or civic opportunities.'
  }
];
