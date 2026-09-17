---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [north-star, goals, milestones]
created: 2026-07-24
---

# GOALS_AND_MILESTONES — OPERATIONS

## Authority

`..\NORTH_STAR.md` controls permanent direction, fixed commitments, authority,
priority order, and the Ratchet. This folder controls adaptive outcomes only.
No file here may override the law, duplicate an owner's live state, or turn an
idea into a commitment without the required authority.

## Artifact contract

Every live goal or milestone MUST state:

1. `outcome` — the observable condition sought;
2. `why_now` — the constraint or opportunity that makes it active;
3. `owner` — the single file or realm holding live truth;
4. `proof` — evidence required to call the outcome achieved;
5. `review_trigger` — date or event requiring review;
6. `status` — proposed, active, achieved, changed, parked, or superseded;
7. `next_decision` — the decision unlocked by the proof.

## Rules

- Targets and proof bars live here; execution detail lives with CASTLE.
- Domain state, learner position, and research truth live with the owning wiki.
- Project state lives with the project.
- Evidence is linked, not copied.
- A missed target MUST be diagnosed before it is changed.
- Material goal changes require evidence review and Chris's approval.
- AI MAY update ordinary status or evidence pointers when authorized by the
  owning workflow. AI MUST NOT create or materially change a goal, milestone,
  target, or strategy without Chris's explicit approval.
- AI MUST NOT write to `NORTH_STAR.md` or any `raw\` folder without the
  approval required by the North Star law.
- Superseded artifacts MUST be archived; never deleted.

## Routing

| Artifact | Owner |
|---|---|
| Current business vehicle and its assumptions | `CURRENT_STRATEGY.md` |
| Semester-level academic outcome | named semester file |
| Cross-domain capability outcome | named capability goal |
| Economic-value outcome | named value-production goal |
| Weekly execution plan | CASTLE |
| Retrospective review | `00-BRAIN\Session_Logs\` |
| Domain progress | owning `03-WIKIS` hub |
| Current action | `.ROOT\NOW.md` |

## Validation

A change is incomplete until owner paths resolve, duplicate authority is absent,
frontmatter is valid, affected references are updated, and the result can be
retrieved in a fresh session without oral context.
