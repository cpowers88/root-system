---
type: reference
timeline: reference
tags: [governance, ai-automation]
---

# SYSTEM_LEARNINGS — Durable Evidence-Based Lessons

## Purpose

This is an on-demand registry for reusable lessons about how `.ROOT` should
operate. It is not a task list, a session log, or a replacement for
`SYSTEM_FLAGS.md`.

## Promotion Rule

An ordinary flag remains a flag. Create a learning only when at least **two
unrelated flags or incidents** establish the same general pattern, or when
two incidents materially contradict an existing active learning. Read the
cited evidence before promotion; one bad outcome is not a pattern.

## Required Entry Shape

```markdown
## L-YYYY-NN — <declarative lesson>
**Status:** active | superseded
**Evidence:** flag/incident references (at least two unrelated)
**Check at:** YYYY-MM-DD

<The general lesson, independent of one file or fix.>

**Behavior proposal:** <linked approved/rejected proposal, or none>
**Outcome:** <added at check-at review>
```

## Lifecycle

`flag or incident → repeated evidence → learning → proposal → Chris-approved
change → check_at review`

Rejected proposals retain their reason. Accepted changes are committed with
their proposal/rationale. A learning may remain active without requiring a
behavior change.

## Active Learnings

## L-2026-01 — A copied-state table named "live truth" is a second status home, and it will freeze

**Status:** active
**Evidence:** three instances of one pattern — (1) `PRE-SEMESTER_PREP_PLAN.md`, found
2026-07-19: copied learner stages ("Physics Stage 3 / Python Stage 2") went stale because
the weekly reconciliation they depended on never ran; (2) finding N4, 2026-08-17:
`CASTLE\wiki\current-position.md` corrected against owner truth after its copied Python
row sat wrong for 19 days; (3) flag #103, 2026-08-19: the ownership loop —
skill-map ↔ current-position ↔ capability goal each naming another as authority — froze
all four CASTLE core maps for a month, measured 21 days wrong on Python. Instances 1 and
3 share a birthday: the July 19 review prescribed the cure (*"gates + pointers, no copied
state"*) and planted instance 3's defect (*"skill-map's register is live truth"*) in the
same document, as an "optional polish."
**Check at:** 2026-09-23 (first monthly review after #103's Aug 23 close check)

State may live in exactly one file per object, and that file must be the one the daily
read path already touches — **the read path and the authority path must be the same
file.** A second table that copies state and a pointer that declares some *other* file
"live truth" are the same defect in different costumes: both create a home that no
session's ordinary work ever opens, so it rots silently, and its staleness is discovered
by accident rather than by instrument. Any quoted fact from another owner carries its
as-of date and owner link; stage numbers and statuses are cited, never restated bare.
A "single home" declaration is not enough on its own — flag #103's skill-map *declared*
itself the only home while a sibling file contradicted it. The declaration must be
paired with a mechanical staleness check on the declared home, or it is prose.

**Behavior proposal:** implemented and Chris-ratified 2026-08-19 with flag #103's repair —
single home ruled (`current-position.md`), the competing pointers deleted or reworded,
and `castle_freshness.py` measuring the declared home's staleness in every morning brief.
**Outcome:** *(due at the 2026-09-23 check: has any new copied-state table or "live
truth" pointer appeared, and did the freshness gate catch the Aug 23 / Sep reconciliations
honestly?)*
