---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5D — CASTLE Action Frontier

## Outcome

CASTLE's nine action pages use metadata v2 with timeline decisions grounded in
live July 15 truth rather than copied legacy tags. Static roadmap stage and artifact
status remain separate, and the CASTLE router exposes a complete current-page query
without replacing `NOW.md` as the system-wide daily authority.

## Evidence baseline

- Approved Phase 5C checkpoint: `784e3a9`.
- Live dry run: 245 safe complete conversions; 620 reviewed findings; 0 schema;
  0 new baseline debt.
- `NOW.md` names current work in tracker/SQL, one live workflow observation/VSM,
  school preparation, and two active opportunity-queue tests.
- CASTLE `current-position.md` confirms SQL as the top gap, tracker real-data entry
  around July 25, observation/VSM unproven, and Phase 1 pre-semester work active.
- Legacy tags put Phases 2–4 all at `next`. Their windows/actions differ: Phase 2
  has a current pre-semester observation; Phase 3 is the on-deck November data
  pipeline; Phase 4 is deferred until February 2027.

## Owned action manifest — exactly nine files

All paths are under `00-BRAIN\CASTLE\wiki`:

- `opportunity-queue.md` → `timeline: now`, preserve `status: live`.
- `phases\phase-0-current-position-and-baseline.md` → `timeline: now`,
  `stage: phase-0`, preserve `status: active`.
- `phases\phase-1-school-core-technical-foundation.md` → `timeline: now`,
  `stage: phase-1`, preserve `status: planned`.
- `phases\phase-2-audit-methodology-foundation.md` → `timeline: now`,
  `stage: phase-2`, preserve `status: planned`.
- `phases\phase-3-data-and-workflow-systems-foundation.md` → `timeline: next`,
  `stage: phase-3`, preserve `status: planned`.
- `phases\phase-4-first-offer-readiness.md` → `timeline: later`,
  `stage: phase-4`, preserve `status: planned`.
- `proof-projects\ksu-academic-tracker.md` → `timeline: now`,
  `stage: phase-0`, preserve `status: active`.
- `skills\field-observation.md` → `timeline: now`, `stage: phase-2`, preserve
  `status: building`.
- `skills\sql.md` → `timeline: now`, preserve `status: building`; no single stage
  is assigned because the page explicitly spans Phases 0, 1, and 3.

Dependent user interface: `wiki\README.md` may replace its transition warning with
a complete CASTLE `[timeline:now]` query only after validation proves no legacy
`now`/`next` action tags remain.

## Decision rules

- `now`: a named action or review is current in `NOW.md`, the page's next action,
  or a dated live queue item.
- `next`: on deck after current work, with a named activation condition.
- `later`: deliberately deferred beyond the on-deck horizon.
- `stage`: static roadmap association; it never decides when to act.
- `status`: artifact/skill/phase condition; `planned` may coexist with `now` when
  preparation is current before the formal phase window.

## Exclusions

- No completion claim, checklist change, opportunity-row change, project expansion,
  outreach, approval, pricing, or external action.
- No CASTLE reference page except the dependent README route and the required
  append-only `wiki\log.md` entry.
- No Session Log except this report; no subject wiki, Library, school source file,
  raw, Journal, archive, client content, or Claude-owned DAILY/PHYSICS file.
- Body changes are limited to two short planned-vs-current explanations, three
  Phase 0 truth corrections, the router transition completion, and the required
  append-only CASTLE log entry.

## Acceptance tests

1. Exactly nine action files match the frozen decisions: 7 now, 1 next, 1 later.
2. Seven phase/proof/skill associations receive the stated `stage` values; SQL
   remains multi-phase without a misleading single stage.
3. All types, statuses, categories, created dates, topic tags, queue rows, next
   actions, and body evidence remain unchanged except documented corrections.
   Checklist truth is preserved while two already-complete Phase 0 criteria are
   normalized from unchecked boxes plus `✓` to standard checked boxes.
4. CASTLE contains zero legacy `now`/`next` action tags after migration; its
   `[timeline:now]` query returns the full v2 current set.
5. README distinguishes CASTLE current pages from system-wide daily priority in
   `.ROOT\NOW.md`.
6. Safe conversions fall exactly 245 → 236; all 620 finding identities and zero
   schema debt remain unchanged.
7. Canonical health, both whitespace scopes, text/link integrity, and Claude's
   three-file boundary do not regress.

## Loop contract

- Pass 1 applies the frozen metadata and the minimum planned-vs-current notes.
- Loop 1 challenges every timeline against dates, next actions, and `NOW.md`.
- Loop 2 tests query completeness, body preservation, migration delta, health, and
  the Claude boundary.
- Correctness failures are fixed regardless of percentage; otherwise avoid
  inventing work or rewriting action-page content.

## Rollback and review boundary

The diff begins at `784e3a9`. Phase 5D remains uncommitted until Chris reviews the
final report. Approval authorizes only this twelve-file checkpoint (nine action
pages, README, CASTLE log, and this report) and design of the next bounded Phase 5
chunk.

## Pass record

### Pass 0 — baseline

- Owned v2 action pages: 0/9.
- Legacy decisions: 4 now, 5 next.
- Live semantic decision: 7 now, 1 next, 1 later.
- Live safe conversions: 245.
- Reviewed findings: 620; schema findings: 0; new findings: 0.
- Working tree outside this report: Claude's DAILY and two PHYSICS files only.

### Pass 1 — frozen migration

- Migrated all nine owned action pages: 7 now, 1 next, 1 later.
- Added all seven frozen `stage` associations; SQL remains explicitly multi-phase.
- Removed every legacy `now`/`next` control tag from CASTLE while preserving topic
  tags, types, statuses, categories, dates, checklists, queue rows, and next actions.
- Added only the two planned-vs-current explanations authorized above.
- Safe conversions fell exactly 245 → 236; reviewed findings remained 620 with
  620/620 identities covered and no target file written by the planner.

### Loop 1 — semantic challenge

- Phase 0, the tracker, SQL, and the opportunity queue remain current against
  their live July actions.
- Phase 1 is current preparation for August 24 while its formal phase stays
  planned; Phase 2 is current because the first live observation/VSM is due now
  while its formal September phase stays planned.
- Phase 3 remains the on-deck November data pipeline (`next`); Phase 4 remains the
  February 2027 offer build (`later`). No date or next-action conflict was found.
- Because the semantic decisions held, no extra prose or scope was invented.

### Loop 2 — interface, preservation, and health

- CASTLE now has zero legacy `now`/`next` tags. The complete
  `path:"00-BRAIN/CASTLE/wiki" [timeline:now]` result is eight pages: the seven
  current action pages plus `current-position.md`.
- README now separates that CASTLE result from `.ROOT\NOW.md`, which remains the
  complete system-wide daily authority.
- Diff review proves six action bodies are unchanged. Phase 1 and Phase 2 contain
  only the two documented metadata notes; Phase 0 contains only the documented
  shipped-truth and checkbox corrections. README and the append-only CASTLE log are
  the two dependent interface/history edits.
- Metadata self-test passed with deterministic plan hash
  `1a9ebcceb5e817ddbade47bc98fa3c5d344972f31d772f5976bd24cd52ba2688`,
  620/620 finding identities covered, and zero target writes.
- Canonical health: **PASS WITH DEBT** — 0 link blockers, 4 wiki review items,
  620 metadata findings, 0 new baseline debt; shared skills, boot/governance,
  staged/unstaged whitespace, and live Markdown text integrity pass.
- Claude's DAILY and two PHYSICS files remain unstaged, unedited by this phase,
  and outside its twelve-file approval boundary.

### Final correction loop — user-facing and close-contract challenge

- Corrected README's label from “Current CASTLE action pages” to “Current CASTLE
  pages” because the query also returns `current-position.md`.
- Corrected Phase 0's stale “ships this month” line to the verified July 8 shipment
  and normalized its two completed baseline criteria to `[x]` without changing
  completion truth.
- Added the required append-only CASTLE log entry covering Phases 5A–5D and verified
  that `NOW.md` needs no priority change from this metadata-only correction.
- Expanded the approval boundary from eleven to twelve files; Claude's three
  concurrent education files remain excluded.
- Post-correction validation: 7 now / 1 next / 1 later; zero CASTLE legacy
  `now`/`next` tags; 236 safe conversions; 620/620 finding identities covered;
  zero target writes; deterministic metadata self-test passed.
- Canonical health remains **PASS WITH DEBT**: 0 blockers, 4 unrelated wiki-review
  items, 620 reviewed metadata findings, and 0 new or resolved baseline debt;
  boot/governance, shared skills, both whitespace scopes, and live Markdown text
  integrity pass.

## Human checkpoint

Phase 5D is complete and intentionally uncommitted. Review the nine action-page
decisions, README wording, and append-only CASTLE log entry. Approval authorizes an
exact twelve-file commit; Claude's concurrent three files remain excluded. The
health gate does not evaluate semantic freshness outside this reviewed CASTLE set,
review-cadence completion, source ownership/duplicate disposition, or ordinary
direct-path prose.
