---
type: runbook
timeline: log
status: complete-phases-4-5-retired
tags: [architecture, implementation, validation, rollback]
created: 2026-07-24
---

# `.ROOT` Architecture Update — Implementation Runbook

> **Status banner — 2026-07-25.** Phases 0–3 are **complete**. Phases 4–5 (the
> read-only CASTLE impact report and the migration slice) are **retired** —
> the relocation hypothesis was declined and CASTLE stays at
> `00-BRAIN\CASTLE\`. Do not execute Phases 4–5 or the rollback triggers below;
> they describe a migration that will not happen. Retained for traceability.
> See `SESSION_INDEX.md § Relocation gate — CLOSED 2026-07-25`.
>
> Phase 2's fixture suite and the four-check validator split are **parked**
> until after the school-simulation week — they were scoped to de-risk the
> move, and their remaining value is ordinary stale-reference protection.

## Phase 0 — Before-state

1. Record Git status and unrelated user changes.
2. Confirm `88-JOURNAL`, every `raw/`, and unrelated work remain untouched.
3. Confirm the packet index and current design references resolve.
4. Run the baseline audit and record file count, runtime, baselined count, and
   unbaselined count.

## Phase 1 — Design and interfaces

1. Finalize `vault-skeleton-design.md` sections 2–9 against the roadmap.
2. Keep `newvaultstructureclaude.md` as a synopsis pointing to the roadmap.
3. Preserve the shared scanner with four independent checks:
   move references, link/anchor integrity, canonical copies, and register lint.
4. Keep separate issue categories and exit results; never collapse all errors
   into one opaque pass/fail.

## Phase 2 — Fixtures

Create test-boundary fixtures for the three stale-reference incidents, the
flag-#83 heading/register regression, historical references, duplicate files,
byte-identical files, hub-scoped links, and an explicit abstain case.

Acceptance: all expected failures are detected, accepted historical cases are
classified, and current-vault runtime remains under 10 seconds.

## Phase 3 — Routing and register pilot

Test representative artifacts across all ten roles, entry surfaces,
generated/transient content, CASTLE-owned state, Watchtower signals, and
domain-owner truth. Require an explicit unresolved/escalate result for
ambiguous cases. Target at least 95% unambiguous first-pass routing.

Pilot `register:` only on a bounded governance/instruction cohort. Do not
create companion files automatically.

## Phase 4 — Read-only CASTLE impact report — RETIRED 2026-07-25 (do not execute)

Inventory every active reference to `00-BRAIN\CASTLE`, Watchtower, intake
locations, anchors, generated interfaces, scripts, graph/icon mappings, local
guides, and boot-chain pointers. Classify each as active, historical,
generated, or obsolete. Produce the exact affected-file list and a
fresh-session navigation comparison. Do not move files.

## Phase 5 — Approval and migration slice — RETIRED 2026-07-25 (do not execute)

Only after Gate 3 approval:

- snapshot the before-state and write the rollback map;
- move CASTLE only;
- update active consumers and preserve historical narrative;
- leave Watchtower naming/location unchanged;
- run all acceptance checks;
- observe through the next weekly review.

## Rollback triggers

Rollback immediately on any unresolved active reference, duplicate CASTLE
authority, boot failure, new health blocker caused by the change, inaccessible
owner truth, missing return path, or operator burden exceeding measured benefit.
