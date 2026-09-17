---
type: roadmap
timeline: log
status: complete-gates-2-5-retired
tags: [architecture, castle, watchtower, migration, machine-learning]
created: 2026-07-24
---

# Final `.ROOT` Architecture Update Roadmap

> **Status banner — 2026-07-25.** Gate 1 (meta layer) is **complete**. Gates
> 2–5 existed only to evaluate and execute a physical CASTLE relocation. That
> hypothesis is **retired** — CASTLE stays at `00-BRAIN\CASTLE\`. Gates 2–5 are
> **not pending work**; they are retained for traceability and must not be
> executed. See `SESSION_INDEX.md § Relocation gate — CLOSED 2026-07-25`.
> The locked architecture decisions and ML-derived operating requirements below
> remain live and apply to any future structural change.

## Destination

`.ROOT` keeps its current physical tree while adopting the validated logical
model below:

1. `00-BRAIN` — AI governance and coordination.
2. `01-NORTH_STAR` — durable direction and contracts.
3. CASTLE — decision, sequencing, proof status, and integration pointers.
4. Watchtower — external sensing and materiality-qualified signals.
5. `03-WIKIS` — bounded research and learner truth.
6. `02-LIBRARY` — reference, course files, and deliverable-bearing projects.
7. `05-BUSINESS` — sanitized reusable business assets.
8. `77-INBOX` — sole external arrival door.
9. `88-JOURNAL` — private and inaccessible to AI.
10. `99-ARCHIVE` — preserved inactive history.

Root entry surfaces remain interfaces, not a new content role.

## Locked architecture decisions

- Ten roles are logical responsibilities, not a requirement for ten folders or
  agents.
- CASTLE may write its own maps, decisions, logs, proof status, indexes,
  `NOW.md`, and approved return packets.
- CASTLE may not silently rewrite North Star, governance, owner truth,
  immutable `raw/`, private material, or another realm's content.
- Watchtower remains separately observable and non-acting. Its handoff contains
  evidence home, affected choice, consequence/test, and review trigger.
- Wiki `raw/` folders are immutable owned-evidence boundaries. CASTLE `raw/`,
  if retained, is internal decision staging—not an external arrival door.
- `77-INBOX` is the single external arrival door.

## ML-derived operating requirements

The update must preserve stable identifiers through moves, checkpoints and
rollback points, bridged schemas during transitions, explicit abstain/escalate
classification, human/heuristic baselines, versioned instruction interfaces,
dependency-aware generated-output checks, and fresh-session reproducibility.

Every consequential change records runtime, false positives, misses, operator
burden, owner, `check_at`, and a keep/modify/revert outcome.

## Implementation gates

### Gate 1 — Meta layer — COMPLETE 2026-07-25

Finalize the skeleton, synopsis, packet, validator interfaces, baseline rules,
and routing fixtures. No physical move.

### Gate 2 — Evidence — RETIRED 2026-07-25 (do not execute)

Produce a read-only CASTLE impact report with active/historical/generated/
obsolete references, ownership ambiguity, dependency blast radius, navigation
comparison, and measurable benefit beyond pointers.

### Gate 3 — Human approval — ANSWERED 2026-07-25

Chris approves or rejects the logical model, Watchtower handoff, validator
suite, and any proposed physical move.

**Result:** logical model accepted; Watchtower stays separate; validator kept
read-only and parked; **physical move declined.**

### Gate 4 — Migration — RETIRED 2026-07-25 (do not execute)

If approved, move CASTLE only. Watchtower rename, metadata rollout, source
ledgers, and unrelated cleanup remain separate changes.

### Gate 5 — Acceptance — RETIRED 2026-07-25 (do not execute)

Run validators, boot-chain checks, wiki lint, frontmatter audit, root health,
fresh-session navigation, and the weekly observation review.

## Reversal standard

Revert if the move creates an unresolved active reference, duplicate authority,
boot failure, new health blocker, inaccessible owner truth, unclear return path,
or greater operator burden than the measured benefit.
