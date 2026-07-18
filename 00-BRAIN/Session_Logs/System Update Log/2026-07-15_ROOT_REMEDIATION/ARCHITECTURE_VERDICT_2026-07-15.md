---
type: report
timeline: log
tags: [governance, system-review, architecture]
---

# Architecture Verdict — July 15, 2026 (Claude, Chunk 0 of the system-design lane)

## Outcome

**FREEZE CONFIRMED for every structural element. GO for Codex Phases 5–7 as sequenced.**

Chris granted an open-redesign license for this review. Under that license, with
falsifiable criteria fixed before looking, no structural element of `.ROOT` earned a
change. Every defect found is pointer- or interface-level and is already owned by a
planned chunk or handed to Codex Phase 6 below. Redesign license exercised; redesign
not warranted.

## Criteria (fixed before evidence was gathered)

A structural change is justified only if ALL three hold:

1. A repeated, evidenced retrieval/navigation/behavior failure traces to the folder or
   realm structure itself — not to pointers, indexes, or stale interfaces.
2. The failure demonstrably cannot be fixed at pointer/index level.
3. The evidenced ongoing cost exceeds the migration cost (re-doing Codex's committed
   metadata realms, link repair across ~1,150 live pages, retraining fresh-session
   discoverability).

Indecision defaults to the July 14 direction review's "do not rebuild" ruling.

## Evidence Base

1. **Health gate baseline** (`root_health.py`, this session): `PASS WITH DEBT` — 0
   blockers; 618 reviewed baseline metadata findings; 773 expected wiki review items;
   boot/governance, skills mirrors, and text integrity all PASS.
2. **Flag-history sweep**: across 75+ numbered flags plus the June ledger, zero flags
   attribute a failure to folder structure. The recurring failure class is semantic
   interface drift (stale claims, pointer mismatches — flag #74 is the archetype), and
   every instance was fixed at pointer/index level. The one relocation in the record
   (school → `02-LIBRARY\00-SCHOOL`, flag #61) happened inside the skeleton.
3. **Three independent cold-boot probes** (fresh agents given only the root entry
   pointer, forced to navigate by in-file pointers alone):
   - **School realm** (Python learner truth): answered fully at hop 4–5; zero
     contradictions; current-position/learning-path/flag #74 triple-agree on Stage 2.
   - **Business decision** (new profit idea): owning gate reached in 2 hops; five-gate
     test, recording home, and AI-vs-Chris authority all answerable from files.
   - **System evolution** (repeated friction → approved change → verified outcome):
     all four questions answerable from files; the loop's full picture lives in
     `ROOT_CAPABILITY_CONTRACT.md` §8; weaknesses are distribution and naming, not
     absence.

## Verdict Per Structural Element

| Element | Verdict | Basis |
|---|---|---|
| Root realm layout (00-BRAIN / 01-NORTH_STAR / 02-LIBRARY / 03-WIKIS / 05-BUSINESS / `...projectSuccess` / NOW / 77 / 88 / 99) | **KEEP (freeze confirmed)** | Probes reached every owner in 2–5 pointer hops with no dead ends; no flag in history traces failure to realm layout |
| `03-WIKIS` hub pattern (raw/ → wiki/, per-hub contracts) | **KEEP** | School probe: truth triple-confirmed, generated-vs-proven defense held; July 14 review's retrieval-first rule for SYSTEMS stands |
| CASTLE internal layout (wiki/ maps, phases, skills, decision-rules, templates) | **KEEP** — with 2 named pointer defects (below) | Business probe reached the gate in 2 hops; defects are index-level |
| 00-BRAIN governance layer (AGENT.md + profiles + FLAGS/LEARNINGS) | **KEEP** — semantic unification needed, in existing files | Evolution probe answered everything; the cost is three vocabularies for one loop, which is Chunk 1's job, not a structure problem |
| `...projectSuccess` two-file Watchtower | **KEEP** | Standardized July 15 (Phase 5H committed); live test window per the July 14 review |

**Migration-cost note:** any structural change now would invalidate portions of
Codex's committed Phase 5A–5H realms, the 618-item reviewed baseline, and pointer
paths across ~1,150 live pages — against zero observed structural failures. Criterion
3 alone fails every candidate change; criteria 1–2 also found no candidate.

## GO / NO-GO for Codex Phases 5–7

**GO, unchanged order.** The skeleton the metadata migration is being applied to is
confirmed; none of that work is at risk of being redone. One input for Phase 6
(links/paths/navigation repair) — the probes surfaced four pointer defects in its
lane:

1. **Parking-sink contradiction:** `CASTLE\wiki\decision-rules\adding-a-profit-skill.md`
   sends failed ideas to `parked-advanced/`; `CASTLE\wiki\skill-map.md` sends them to
   `[[parking-lot]]`. Neither page exists. One canonical sink needs choosing (Chris
   or CASTLE call), then both pointers aligned.
2. **Opportunity-queue reachability:** `AGENT.md`'s profit-idea line routes only to the
   skill decision rule; nothing on that path says "check
   `CASTLE\wiki\opportunity-queue.md` for an existing row first." A cold session
   applying the gate to an idea already captured (e.g. OPP-20260714-01) would create a
   duplicate. Smallest fix: one search-before-create line in the decision rule.
3. **PYTHON hub folder list omission:** `03-WIKIS\PYTHON\CLAUDE.md`'s folder-structure
   section does not list `HOW_TO_USE.md`, which exists; a cold reader concludes the
   routing tables point at a missing file.
4. **Session Start Protocol vs progressive loading:** AGENT.md's start protocol and the
   capability contract's "smallest authoritative chain" rule pull in slightly
   different directions for non-daily questions. One clarifying line in whichever file
   Codex's Phase 6 already touches.

## Findings Owned by the Claude Lane (already-planned chunks)

- **Chunk 1 targets, now evidence-backed:** the self-improvement loop has three
  vocabularies (AGENT.md "System Evolution Authority" / contract §8 "Ratchet" /
  SYSTEM_LEARNINGS "Lifecycle") and its validation step is described four different
  ways; "Ratchet" is overloaded (system loop vs North Star strategy review). The
  canonical loop section in `ROOT_CAPABILITY_CONTRACT.md` must give the loop one name,
  one diagram, one validation statement — and distinguish it from the North Star
  Ratchet by name.
- **Chunk 3 target, confirmed:** "did the change actually help" currently has no single
  owner (split across FLAGS re-raise, LEARNINGS check-at, review cadence, acceptance
  check) — the check_at/outcome discipline closes exactly this.
- **Accepted cost, no action:** depth-to-first-signal (~4–5 governance files before
  domain truth appears) is the price of the progressive-loading design and is working
  as intended; NOW.md covers the human fast path.

## Chunk 0 Self-Review (per the shared phase-loop protocol)

- Tested the skeleton, not its self-description: three independent cold-boot probes +
  flag-history sweep + deterministic gate; no verdict rests on documentation alone.
- Every KEEP cites observed navigation success or absence of structural failure in the
  record; no CHANGE was proposed, so no migration math was needed beyond criterion 3.
- Plan alignment: Chunk 0 deliverable complete; Chunks 1 and 3 gained named,
  evidence-backed targets; four pointer defects handed to Codex Phase 6; no new
  pointer created that a later chunk must update.
- Read-only discipline held: this file and the DAILY block are the only writes.

## Decision Needed (human checkpoint)

1. Approve this verdict (freeze confirmed, GO for Codex Phases 5–7).
2. Approve handing the four Phase 6 pointer defects to Codex via the DAILY/handoff.
3. Approve proceeding to Chunk 1 (canonical loop + return packet in
   `ROOT_CAPABILITY_CONTRACT.md`, one pointer line in AGENT.md).

No commit until Chris approves, per the phase-loop protocol.
