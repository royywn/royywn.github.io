// Status badge vocabulary + fixed color mapping (DESIGN.md color rule 3):
// green = validated (backtested), honey = in active use (daily driver / live /
// paper-trading), taupe = in progress (researching / idea).
export type BadgeStatus =
  | 'idea'
  | 'researching'
  | 'backtested'
  | 'paper-trading'
  | 'daily driver'
  | 'live';

export const badgeColorClass: Record<BadgeStatus, string> = {
  backtested: 'badge-green',
  'daily driver': 'badge-honey',
  live: 'badge-honey',
  'paper-trading': 'badge-honey',
  researching: 'badge-taupe',
  idea: 'badge-taupe',
};
