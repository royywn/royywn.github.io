import { defineCollection, z } from 'astro:content';

// Schemas are contracts (CLAUDE.md rule 5): changing them requires a DECISIONS.md
// entry and migration of all existing content in the same commit.

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

const strategies = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum(['trend', 'mean reversion', 'optimization', 'risk', 'infra']),
    tags: z.array(z.string()).default([]),
    status: z.enum(['idea', 'researching', 'backtested', 'paper-trading']),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    repo: z.string().url().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog, strategies };
