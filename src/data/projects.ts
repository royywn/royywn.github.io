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

// Repo links are placeholders pointing at the GitHub profile until Roy
// confirms the exact repository URLs (B-07).
export const projects: Project[] = [
  {
    name: 'QuantPulse',
    // TODO:ROY one-liner + tech tags from content-sources/projects.md (B-07)
    description: '',
    status: 'backtested',
    tags: [],
    repo: 'https://github.com/royywn', // TODO:ROY replace with the QuantPulse repo URL
  },
  {
    name: 'Agentic coding framework',
    // TODO:ROY one-liner + tech tags from content-sources/projects.md (B-07)
    description: '',
    status: 'daily driver',
    tags: [],
    repo: 'https://github.com/royywn', // TODO:ROY replace with the framework repo URL
  },
  {
    name: 'Local AI infrastructure',
    // TODO:ROY one-liner + tech tags from content-sources/projects.md (B-07)
    description: '',
    status: 'researching',
    tags: [],
    repo: 'https://github.com/royywn', // TODO:ROY replace with the infra repo URL
  },
];
