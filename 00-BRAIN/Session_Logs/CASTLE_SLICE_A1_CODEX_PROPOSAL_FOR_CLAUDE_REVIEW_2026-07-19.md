---
type: report
timeline: now
status: awaiting-review
tags: [castle, governance, codex, claude-review]
---

# CASTLE Slice A1 — Codex Proposal for Claude Review

**Date:** July 19, 2026  
**Prepared by:** Codex  
**Decision owner:** Chris  
**Implementation status:** Not started; exact wording awaits Chris's approval after Claude's independent challenge

## Review Request

Run this proposed Slice A1 through the live CASTLE contract and challenge it before implementation.

The governing question is:

> What is the highest-value next action; who owns it; what proof closes it; and where does the result return?

Review against:

1. `00-BRAIN\AGENT.md`
2. `00-BRAIN\CLAUDE.md`
3. `00-BRAIN\CHRIS_CORE.md`
4. `01-NORTH_STAR\NORTH_STAR.md`
5. `00-BRAIN\CASTLE\OPERATIONS.md`
6. The four live targets named below

Do not implement the proposal during the review. Return an evidence-based `KEEP`, `MODIFY`, or `REJECT` verdict for each file and identify any wording that duplicates authority, narrows Chris's destination, creates maintenance burden, or misstates a live path.

## CASTLE Verdict from Codex

**Proceed with Slice A1, subject to Claude's challenge and Chris's exact-wording approval.**

The July 19 North Star and `OPERATIONS.md` are aligned. The four entrance files remain the highest-value synchronization point because they still expose outdated autonomy, daily-authority, maintenance, and boot-summary language.

This proposal makes the entrance layer smaller and pointer-based:

- `HOW_TO_USE.md` routes questions without redefining operating rules.
- `wiki\README.md` presents `NOW.md` as a current-action interface rather than authority.
- `CLAUDE.md` visibly completes the person-contract step in the local pointer.
- `wiki\index.md` inventories verified live pages and templates without copying current state or speculative pages.

## Scope and Boundaries

### In scope

- `00-BRAIN\CASTLE\HOW_TO_USE.md`
- `00-BRAIN\CASTLE\wiki\README.md`
- `00-BRAIN\CASTLE\CLAUDE.md`
- `00-BRAIN\CASTLE\wiki\index.md`

### Explicitly out of scope

- No change to `NORTH_STAR.md` or `OPERATIONS.md`.
- No change to `NOW.md`, core maps, phase pages, skill pages, templates, source summaries, decision rules, or logs.
- No new dashboard, phase, skill, or status page.
- No implementation before Chris approves the post-review wording.

## Correction Made During Live Verification

The conversational preview used simplified phase and source filenames while illustrating the proposed index. Live `rg --files 00-BRAIN\CASTLE` verification showed those names were not exact. This packet corrects the proposal before implementation: the index below uses only verified live filenames and does not present `CURRENT_STRATEGY.md` as a CASTLE-root file.

## Proposed Exact Replacement 1 — `HOW_TO_USE.md`

```markdown
---
type: guide
timeline: reference
tags: []
---

# HOW TO USE — CASTLE

### User router for decisions, sequencing, ownership, and proof

**Last updated:** July 19, 2026 — synchronized to `OPERATIONS.md`

## What CASTLE Answers

CASTLE is the current decision, sequencing, and proof-status cockpit.

> What is the highest-value next action; who owns it; what proof closes it; and where does the result return?

Durable direction belongs to `01-NORTH_STAR\NORTH_STAR.md`. Rules and authority belong to `OPERATIONS.md`. Domain work and evidence remain with their owning systems.

## Start Here

- **Current action:** open `.ROOT\NOW.md`
- **Position on the path:** open `wiki\current-position.md`
- **Long-range sequence:** open `wiki\north-star-roadmap.md`
- **Operating rules:** open `OPERATIONS.md`
- **Full page inventory:** open `wiki\index.md`

## Ask the Right Owner

| Question | Open |
|---|---|
| What should I do now? | `.ROOT\NOW.md` |
| Where am I on the path? | `wiki\current-position.md` |
| What phase am I in? | `wiki\phase-map.md` |
| What capabilities need proof? | `wiki\skill-map.md` |
| What is the current business strategy? | `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` |
| Should a new opportunity enter the system? | `wiki\decision-rules\adding-a-profit-skill.md` |
| What external signal needs evaluation? | Evidence owner → radar → CASTLE gate |

## From Decision to Proof

A material CASTLE decision identifies why it matters now, who owns the work, the next action, the proof required, and where the result returns. The formal definitions and update rules live in `OPERATIONS.md` and the North Star system contracts.

Work is performed in the owning realm. Verified results return to CASTLE only when they change sequence, proof status, or the live operating picture.

## Retrieve

Use `wiki\index.md` for direct navigation.

Useful Obsidian searches:

- `tag:#castle`
- `path:"00-BRAIN/CASTLE"`
- `type:map`
- `type:proof-project`

## Boundaries

CASTLE routes work; it does not replace the systems that teach, research, build, schedule, or preserve evidence.

Chris owns direction, timing, capacity, and consequential decisions.

CASTLE does not copy owner truth. It points to the authoritative source and records only the decision or proof state needed to steer the system.
```

### Intended effect

Remove duplicated operating mechanics, `FULL OPERATOR` language, universal file-update mandates, forced `NOW.md` refreshes, rigid stub prohibition, dated capacity assumptions, and command examples that can drift from the contract.

## Proposed Exact Replacement 2 — `wiki\README.md`

```markdown
---
type: guide
timeline: reference
reference_priority: core
tags: []
---

# CASTLE Wiki — User Router

Use this page to find the correct CASTLE view without loading the entire cockpit.

## Start

When beginning active work, open `.ROOT\NOW.md` for the current-action interface.

For a cold entry:

1. Open [[north-star-roadmap]] for the long-range sequence.
2. Open [[current-position]] for the latest baseline and proof state.
3. Open `..\HOW_TO_USE.md` for question routing.
4. Open `..\OPERATIONS.md` when operating rules or authority matter.

CASTLE helps answer:

> What is the highest-value next action; who owns it; what proof closes it; and where does the result return?

Durable direction lives in `01-NORTH_STAR\NORTH_STAR.md`. The current business strategy lives in `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md`.

## Core Views

| Need | Page |
|---|---|
| Current action | `.ROOT\NOW.md` |
| Long-range sequence | [[north-star-roadmap]] |
| Current baseline and proof | [[current-position]] |
| Phase structure | [[phase-map]] |
| Capability structure | [[skill-map]] |
| Evidence supporting roadmap decisions | [[source-map]] |
| Complete CASTLE inventory | [[index]] |

## Find a Layer

- **Reference maps:** `path:"00-BRAIN/CASTLE/wiki" [timeline:reference] [reference_priority:core]`
- **Supporting rules and evidence:** `path:"00-BRAIN/CASTLE/wiki" [timeline:reference] [reference_priority:supporting]`
- **Current CASTLE pages:** `path:"00-BRAIN/CASTLE/wiki" [timeline:now]`

`reference_priority` identifies durable orientation documents. `timeline` identifies action horizon.

`.ROOT\NOW.md` is the current-action interface, not the source of durable authority.
```

### Intended effect

Remove both claims that `NOW.md` is complete system-wide daily authority, stop prescribing a morning schedule, and retain a concise entry router.

## Proposed Exact Replacement 3 — `CLAUDE.md`

```markdown
---
type: pointer
timeline: reference
tags: []
---

# CLAUDE.md — CASTLE Claude Auto-Load Pointer

Claude sessions working inside CASTLE follow this chain:

1. **Boot:** `C:\Users\chris\.ROOT\00-BRAIN\AGENT.md` — complete its universal orientation chain.
2. **Surface:** `C:\Users\chris\.ROOT\00-BRAIN\CLAUDE.md`
3. **Person:** `C:\Users\chris\.ROOT\00-BRAIN\CHRIS_CORE.md`
4. **Local operations:** `C:\Users\chris\.ROOT\00-BRAIN\CASTLE\OPERATIONS.md`

The original CASTLE build prompt was archived July 6, 2026 at `.ROOT\99-ARCHIVE\ARCHIVED_2026-07-06_CASTLE_BUILD_PROMPT.md`.

Do not duplicate operating rules here. `OPERATIONS.md` is CASTLE's local contract.
```

### Intended effect

Make the person-contract step visible without recreating the universal boot chain or adding rules to the pointer.

## Proposed Exact Replacement 4 — `wiki\index.md`

```markdown
---
type: map
timeline: reference
reference_priority: core
tags: []
---

# Index — Every Live Page in CASTLE

### Updated: July 19, 2026 — Slice A1 contract-consumer synchronization

This is a discovery index, not a second current-state dashboard. Live action belongs to `.ROOT\NOW.md`; baseline and proof state belong to [[current-position]] and the owning domain systems.

## CASTLE Root Files

- `OPERATIONS.md` — local operating contract; complete the universal `AGENT.md` orientation chain first
- `HOW_TO_USE.md` — user question and navigation router
- `CLAUDE.md` — Claude auto-load pointer
- `CODEX.md` — Codex cross-surface pointer

## External Direction and Action Interfaces

- `.ROOT\NOW.md` — current-action interface
- `01-NORTH_STAR\NORTH_STAR.md` — durable direction
- `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` — current business strategy under test

## Wiki Entrance and Core Maps

- [[README]] — wiki entry router
- [[north-star-roadmap]] — long-range sequence
- [[current-position]] — monthly baseline and proof state
- [[phase-map]] — phase structure and exit logic
- [[skill-map]] — capability and proof structure
- [[source-map]] — roadmap-shaping evidence
- [[opportunity-queue]] — opportunities moving from evidence to test or harvest
- [[log]] — append-only CASTLE history

## Phase Pages

- [[phase-0-current-position-and-baseline]]
- [[phase-1-school-core-technical-foundation]]
- [[phase-2-audit-methodology-foundation]]
- [[phase-3-data-and-workflow-systems-foundation]]
- [[phase-4-first-offer-readiness]]

## Proof Projects

- [[ksu-academic-tracker]] — school-serving Python and SQLite proof project

## Skill Pages

- [[sql]]
- [[field-observation]]

## Source Summaries

- [[claude-code-docs-pack-2026-07]]
- [[openai-platform-docs-pack-2026-07]]

## Decision Rules

- [[adding-a-profit-skill]] — gate for new profit-skill and opportunity ideas

## Templates

- `..\templates\decision-rule-template.md`
- `..\templates\evidence-template.md`
- `..\templates\phase-template.md`
- `..\templates\project-template.md`
- `..\templates\service-capability-template.md`
- `..\templates\skill-template.md`
- `..\templates\source-summary-template.md`
```

### Intended effect

Remove the stale copied command-center state, remove non-existent planned pages from a live-page inventory, complete discovery for `CODEX.md` and all seven templates, and replace volatile status claims with stable descriptions.

## Codex Challenge Notes for Claude

1. **Thin-router test:** Does `HOW_TO_USE.md` still repeat too much of `OPERATIONS.md`, especially the five-field decision description?
2. **Authority test:** Does any wording imply that `NOW.md`, README, or the index governs direction rather than routing to its owner?
3. **Chris-owned-time test:** Does any sentence prescribe when Chris must work rather than helping him orient when he chooses to work?
4. **Path test:** Do all filenames and relative paths resolve from their proposed file locations?
5. **Index test:** Is removing the Planned section correct, or does CASTLE have a demonstrated discovery need that cannot be served by `phase-map.md` and `skill-map.md`?
6. **Boundary test:** Does the packet keep CASTLE as cockpit rather than scheduler, domain wiki, project tracker, or copied dashboard?
7. **Compression test:** Can any sentence be removed without reducing orientation, safety, or retrieval value?

## Required Claude Return

Return a table with:

| Target | Verdict | Live evidence | Exact modification, if any |
|---|---|---|---|

Then answer:

1. Is Slice A1 safe to implement as one coherent commit?
2. Does it fully synchronize the four entrances with the July 19 North Star and `OPERATIONS.md`?
3. Did Codex accidentally narrow the Advisor-Builder destination or over-abstract the practical technology/workflow goal?
4. Are there any controlling entrance conflicts still outside these four files that should join A1 rather than wait for A2?
5. What exact validation should run after implementation?

## Proposed Post-Approval Validation

1. Verify the four-file diff contains no unrelated changes.
2. Confirm these phrases return zero live hits under `00-BRAIN\CASTLE`:
   - `FULL OPERATOR`
   - `daily authority`
   - `Every session that changes files`
   - `Refresh NOW after any working session`
3. Verify every index entry resolves to a live file.
4. Run frontmatter audit and canonical `.ROOT` health gate.
5. Append `wiki\log.md` only when the approved implementation changes CASTLE state; refresh `NOW.md` only if the live operating picture materially changes.

## Return Packet

1. **Current state:** Slice A0 is committed and pushed. Slice A1 is drafted but not implemented.
2. **Open question:** whether Claude finds any authority duplication, path error, missing entrance conflict, or wording that should be compressed before Chris approves the edit.
3. **Next exact action:** Claude completes the independent review above and returns per-file verdicts; Chris then approves or modifies the exact A1 wording.
4. **Fragile detail:** use the verified filenames in this report, not the simplified filenames from the earlier conversational preview. Do not edit A1 during the challenge pass.

---

*Prepared for independent Claude review. Chris retains final authority over the wording and implementation.*
