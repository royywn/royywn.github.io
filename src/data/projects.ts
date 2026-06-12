// Typed project data for the landing cards and /projects (PLAN Phase 2).
// Names and badge statuses are approved in DESIGN.md zone 3; descriptions,
// tags, and repo links await content-sources/projects.md (BLOCKERS B-07) —
// never invent them.
import type { BadgeStatus } from '../components/badge-status';

export interface Project {
  name: string;
  description: string;
  status: BadgeStatus;
  tags: string[];
  repo?: string;
  writeup?: string;
}

export const projects: Project[] = [
  {
    name: 'QuantPulse',
    // TODO:ROY one-liner, tech tags, repo link from content-sources/projects.md (B-07)
    description: '',
    status: 'backtested',
    tags: [],
  },
  {
    name: 'Agentic coding framework',
    // TODO:ROY one-liner, tech tags, repo link from content-sources/projects.md (B-07)
    description: '',
    status: 'daily driver',
    tags: [],
  },
  {
    name: 'Local AI infrastructure',
    // TODO:ROY one-liner, tech tags, repo link from content-sources/projects.md (B-07)
    description: '',
    status: 'researching',
    tags: [],
  },
];
