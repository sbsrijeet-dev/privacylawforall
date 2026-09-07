import { defineCollection, z } from 'astro:content';

const casesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    case_name: z.string(),
    popular_name: z.string(),
    dpa: z.string(),
    country: z.string(),
    jurisdiction: z.string(), // "EU GDPR", "India DPDPA", "EU AI Act", "UK GDPR"
    fine_amount: z.string(),
    fine_magnitude: z.string().optional(),
    decision_date: z.string(),
    year: z.number(),
    articles_cited: z.array(z.string()),
    exam_domain: z.string(),
    tldr: z.string(),
    is_top_5: z.boolean().default(false),
    top_5_rank: z.number().optional(),
    category: z.string(),
    source_url: z.string().optional(),
    verified: z.boolean().default(true),
  }),
});

export const collections = {
  cases: casesCollection,
};
