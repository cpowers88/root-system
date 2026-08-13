---
type: report
timeline: now
register: system-review
status: in-progress
tags: [update, wiki, conformance, semantic-freshness, codex-review]
created: 2026-08-12
---

# Codex Priority 2 — wiki material review

## Verdict first

The shared layer is present but not yet demonstrated as a shared operating
mechanism. All eight hubs have an `OPERATIONS.md`, but only PYTHON, SYSTEMS, and
TECHNOLOGY explicitly point back to `WIKI_SHARED_LAYER.md`. The other five
mostly duplicate selected rules and omit the shared session-start minimum. That
means conformance currently depends on the global loader being noticed and
obeyed; the hub contract itself does not make the dependency discoverable.

W3 found a second, different issue: only EDUCATION, PHYSICS, and PYTHON own a
`wiki/current-position.md`. The absence is intentional in some other hubs, so
"missing file" is not the test. The correct test is whether each hub names a
single live state owner and whether that owner still matches current truth.

No fixes were applied. No `raw\` content was modified, moved, hashed, or
deduplicated. `88-JOURNAL\` was not accessed.

## W2 — shared-layer conformance

Legend: **D** = direct local implementation or explicit dependency; **P** =
partial/local analogue; **G** = relies only on the global shared-layer load;
**?** = no functional evidence established in this pass.

| Hub | Raw immutable | Chunking | Start: index + last 3 logs + goal | Close: log/index/next | Update over create | Claim changes classified | Recency markers | Lint + frontmatter gate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AI_AUTOMATION_SYSTEMS | D | D | G | P | D | P | D | P |
| BUSINESS | D | D | D except goal | P | D | D | G | P |
| EDUCATION | D | D | G | P | D | P | G | P |
| PHYSICS | D | D | G | D | D | P | G | P |
| PYTHON | D | D | D via shared pointer/protocols | D | D | D via shared pointer | D via shared pointer | D via shared pointer |
| REVENUE_LAB | D | D | G | D | D | D | G | P |
| SYSTEMS | D | D | D via shared pointer | D | D | D via shared pointer | D via shared pointer | D via shared pointer |
| TECHNOLOGY | D | D | D via shared pointer | D via shared pointer | D | D via shared pointer | D | D via shared pointer |

### W2 findings

1. **The shared dependency is locally discoverable in only 3 of 8 hubs.**
   PYTHON, SYSTEMS, and TECHNOLOGY explicitly state that all eight rules live in
   `00-BRAIN/WIKI_SHARED_LAYER.md`. AI_AUTOMATION_SYSTEMS, BUSINESS, EDUCATION,
   PHYSICS, and REVENUE_LAB do not.
2. **Session start is the weakest rule.** BUSINESS alone directly requires the
   index and three newest log entries, but it does not require the one-sentence
   session goal. Other hubs commonly direct queries through an index or
   current-position page, which is not equivalent to the shared minimum.
3. **Session close is widely implemented in local variants.** PHYSICS, PYTHON,
   REVENUE_LAB, and SYSTEMS name log/state/next-action behavior directly. Other
   hubs describe completion but do not reproduce the exact shared minimum.
4. **The frontmatter half of rule 8 is not locally visible in five hubs.** A
   generic `LINT` section is not evidence that
   `frontmatter_audit.py --baseline ...` will run after frontmatter edits.
5. This matrix evaluates the live contracts, not historical compliance. A
   follow-up trace sample is still needed to prove that recent sessions actually
   read the last three log entries, recorded chunk ranges, and ran the required
   post-frontmatter check.

## W3 — semantic freshness and current project truth

| Hub | State owner found | Preliminary freshness verdict |
|---|---|---|
| AI_AUTOMATION_SYSTEMS | No `current-position.md`; index/log and proposal owners | **Needs owner-path verification.** Absence is not explained as explicitly as SYSTEMS/TECHNOLOGY. |
| BUSINESS | No `current-position.md`; strategy/CASTLE own live vehicle and sequencing | **Structurally plausible; needs owner-path verification.** |
| EDUCATION | `wiki/current-position.md` | **STALE.** It says the next review is August 1 and repeatedly frames D2L as not yet open. It also mixes meta-learning state with ECON/TCOM/ENGR course-container state. |
| PHYSICS | `wiki/current-position.md` | **STALE and internally burdened.** It says the official registration record lists no instructor, while the live system record confirms Farhan Islam from the Outlook registration confirmation plus the online listing. It retains superseded July 26–August 1 and August 3–8 plans inside the live tracker, obscuring the current frontier. The learner frontier itself remains Stage 4 and agrees with NOW. |
| PYTHON | `wiki/current-position.md` | **Current on learner truth.** It ends at Stage 4b, matching NOW. Not repeating the vault PAUSE is correct because NOW owns sequencing and the hub owns learner truth. |
| REVENUE_LAB | No `current-position.md`; CASTLE opportunity queue owns live lane status | **Intentional external owner; needs queue-to-index retrieval test.** |
| SYSTEMS | Explicitly says no `current-position.md` should exist until staged instruction begins | **Intentional and documented.** Coverage ledger/index are the present state owners. |
| TECHNOLOGY | Explicitly rejects `current-position.md`; `TECHNOLOGY_LIBRARY_STRATEGY.md § Current State` owns the landscape frontier | **Intentional and documented; owner freshness still to be checked.** |

### W3 findings

1. EDUCATION and PHYSICS fail semantic freshness even though their files exist
   and pass structural health checks. This confirms the blind spot named by
   `root_health.py`.
2. PYTHON demonstrates the desired ownership separation: learner truth remains
   local; the system-wide PAUSE remains in NOW.
3. A universal requirement for `current-position.md` would be wrong. The repair
   target is a verified, discoverable state owner per hub, not eight identically
   named files.

## W1 — four review-debt items

The four reported items reduce to two underlying pages:

- `CASTLE/wiki/weekly-plans/weekly-plan-2026-08-10-to-2026-08-16.md`
- `CASTLE/wiki/weekly-plans/weekly-plan-2026-08-17-to-2026-08-23.md`

Each page is counted twice: once as missing from CASTLE's exhaustive index and
once as an orphan. The proposed fix is one index/navigation update covering
both pages; that should remove all four counts. No fix was applied because
CASTLE and its weekly-plan surface are on the Thursday collision boundary.

## W4 — EDUCATION's dual identity

The dual identity is real and visible in its own contract:

- Function: reusable support for subjects without a dedicated wiki.
- Structure: ECON, TCOM, and ENGR course folders plus shared learning methods
  and education-system research.
- State: one `current-position.md` combines exact-section course readiness,
  D2L/source gaps, pre-semester scheduling, and general learning support.

Recommended separation for later approval:

1. Keep EDUCATION as the meta-learning and education-research hub: methods,
   learning science, cross-course support conventions, and education-system
   reference.
2. Move course-specific ownership to a clearly named course-support layer under
   `04-SCHOOL` or a deliberately named sub-hub interface; do not move TCOM during
   Thursday's work and do not duplicate official sources.
3. Replace EDUCATION's mixed current-position with either a meta-learning state
   owner or no current-position at all; exact course truth stays with each course
   owner and `SYLLABUS_STATUS.md`.
4. Preserve the graduation rule: a subject with durable staged material can
   become its own wiki, while temporary course support does not automatically
   become permanent domain knowledge.

## Remaining work before final status

- Sample recent log traces per hub to distinguish written conformance from
  performed conformance, especially chunk coverage and session-start behavior.
- Verify the live alternate state owners for AI_AUTOMATION_SYSTEMS, BUSINESS,
  REVENUE_LAB, SYSTEMS, and TECHNOLOGY against their indexes/logs/CASTLE owners.
- Turn W4 into an exact no-collision file-boundary proposal after Thursday's TCOM
  structure is stable.

## Maintenance packet prepared during the finding freeze

Two replacement drafts now sit beside this report. They are proposals only and
do not alter live hub behavior:

1. `PROPOSED_WIKI_SHARED_LAYER_REPLACEMENT.md` — converts the eight shared rules
   into four executable phases with completion criteria, adds a state-owner
   contract, and gives every hub one compact local dependency declaration.
2. `PROPOSED_EDUCATION_OPERATIONS_REPLACEMENT.md` — resolves EDUCATION's dual
   identity at the authority level: EDUCATION owns reusable methods/research;
   exact course facts, learner truth, and sequencing stay with their existing
   owners. It explicitly leaves current TCOM/ECON/ENGR files unmoved until a
   separately approved migration exists.

### Recommended low-risk maintenance order after review

1. Approve or revise the shared-layer replacement.
2. Add the one-line shared-layer/state-owner declaration to each hub contract;
   do not copy the rules into eight files.
3. Correct stale EDUCATION and PHYSICS state claims against their live owners.
4. Add the two CASTLE weekly plans to the exhaustive index, clearing all four
   review-debt counts.
5. Run fresh-session retrieval checks per hub, then `wiki_lint.py`, the
   frontmatter audit, boot validation, and `root_health.py`.

The documentation skill influenced this packet by keeping the report as the
decision surface and linking to replacement drafts instead of embedding three
copies of the same instructions. The writing-for-agents skill influenced the
drafts by sharpening triggers, naming state owners, and making each phase end
on a checkable completion criterion.
