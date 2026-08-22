---
type: report
timeline: log
status: proposed
tags: [education, methods, measurement, governance]
created: 2026-08-17
author: Claude Code (Operator hat)
approval: REQUIRED — not implemented
---

# Education Session Measurement — audit and proposed instrument

### Requested by Chris 2026-08-17: a report procedure covering how Chris performed in every
### education session, how the AI performed as teacher, and which measurable changes will
### support later optimization — speed, retention, and method fit.

**Status: proposal. Nothing in this file is implemented.** It adds a required step to
`HAT_EDUCATOR.md` § Session close, which is a governance change; `AGENT.md` § System Evolution
Authority requires Chris's approval before implementation.

---

## 1. Audit — what exists today

| Piece | Location | Side | Since | State |
|---|---|---|---|---|
| Six-check hat rubric | `03-WIKIS\EDUCATION\wiki\methods\hat-performance-log.md` | AI | 2026-08-17 | Live, 3 rows, binary ✓/✗ + prose |
| Learner narrative logs | `PHYSICS\wiki\log.md`, `PYTHON\wiki\log.md` | Chris | 2026-06 | Rich prose, no fixed fields |
| Durability check table | `PHYSICS\wiki\current-position.md` | retention | 2026-08-17 | 2 rows owed Aug 18–20 |
| Measurement design | `PYTHON\wiki\teaching-loop.md` § Two things to keep measuring | speed + support | 2026-07-25 | Adopted, **never applied** |
| Encoding/retrieval theory | `EDUCATION\wiki\methods\learning-how-to-learn-principles.md` | frame | 2026-07-12 | Reference, no instrument |

**There is no plan.** Two of the five pieces were built the same day this audit ran, and
nothing joins any of them.

### The six gaps

1. **No join key.** The two-record separation (learner truth in the hub · hat behaviour in
   EDUCATION) is correct doctrine and must stay. But with no shared session identifier, the
   teaching move and the learning outcome cannot be lined up. *Which move produced the durable
   pass* is currently unanswerable by construction.
2. **Nothing is a number.** Prose does not trend. The only two figures in the whole record —
   pace `2.5/5` and a 6-minute assistance decay — are from one session (2026-07-21) and were
   never taken again.
3. **Speed has no instrument.** No session clock, no per-rep timing. The 6-minute decay figure
   was reconstructed from file modification timestamps by accident (`practice2.py` 15:08 →
   `practice3.py` 15:14), not measured.
4. **Retention is one hub deep and one day old.** PHYSICS 48–72 h only. PYTHON's 2026-08-01
   quiz surfaced two real regressions, wrote "add as explicit spaced-retrieval items," and
   nothing scheduled them — the same failure the PHYSICS table was built to fix.
5. **The best existing mechanism is dormant.** `teaching-loop.md` requires Chris to rate his own
   support level separately from the AI's, because the 2026-07-25 review found the two accounts
   disagreeing on five files. **No session on record contains both ratings.**
6. **Method firing is prose, not data.** "Two-pass pace rule — not exercised" is the right
   observation in a format that can never be counted.

### What already works and must be preserved

**Error classification.** The 2026-08-01 PYTHON entry cleanly separates *regression* from
*fresh gap* from *arithmetic slip* from *answer-flip under timed pressure*, and reclassifies two
misses on Chris's self-report. The vocabulary exists in practice. It needs controlling, not
inventing.

---

## 2. Design constraints — why this is small

1. **Chris's close cost must be near zero.** Semester starts Aug 24: 13 credits, five courses.
   An instrument costing more than ~60 seconds at close will be abandoned, and an abandoned
   instrument is worse than none because it produces gaps that read as data.
2. **The two-record rule is doctrine and does not merge.** `HAT_EDUCATOR.md` § Session close:
   learner truth and hat behaviour "are different evidence and must not be merged." They get a
   shared key, not a shared file.
3. **Replace prose, do not add to it.** The AI currently spends 300+ words narrating what twelve
   fields would carry. Net writing goes *down*; the prose keeps only what is genuinely novel.
4. **One new file maximum.** `EDUCATION\OPERATIONS.md`: do not build scaffolding around nothing.
   The analysis/rollup page is not created until there are rows to analyse.
5. **No learning-style labels.** `HAT_EDUCATOR.md`: "Techniques are real; 'learning styles' are
   not." The measurable question is which *delivery moves and standing methods* correlate with
   durable passes — never a modality identity.

---

## 3. The instrument — one Session Scorecard, two homes, one key

A fixed-field block written at session close. Split across the two existing record homes by the
two-record rule, joined by `session_id`.

**`session_id` format:** `YYYY-MM-DD-SUBJ-N` (e.g. `2026-08-19-PHYS-1`). N increments per
subject per day.

### 3a. Learner block → appended in the hub's `log.md` (PHYSICS / PYTHON / EDUCATION)

```yaml
session_id: 2026-08-19-PHYS-1
mode: breadth | depth | drill | gate | durability-check
clock_min: 47                      # wall time, start to stop
ttfio_min: 9                       # time to first independent output (see below)
reps: 3                            # independent attempts Chris produced
support_ai: cue                    # none | cue | worked-step — highest level used
support_chris: worked-step         # Chris's own rating — DIVERGENCE IS THE FINDING
decay: yes @ 22min                 # did support level fall within the session
cold_open: 4/5                     # unannounced opening term check
misses:
  - class: regression              # regression | fresh-gap | arithmetic | pressure-flip | form-missing
    item: constant of integration
durability_due: 2026-08-21
durability_result: —               # proven | reopened | overdue
methods_fired: [skeleton, term-anchor, explain-back, cold-check]
```

### 3b. AI block → new columns on the `hat-performance-log.md` scorecard

Existing six checks stay **verbatim** (the page says do not reword). Added:
`session_id` · `ttfio_min` (grades check 2 with a number instead of a judgment) ·
`moves_used` (which delivery-contract moves carried the block) · `ai_defect` (one line or none).

### 3c. Field rationale — every field earns its place

| Field | Answers | Why this one |
|---|---|---|
| `clock_min` | speed | The base unit. Currently uncaptured entirely |
| **`ttfio_min`** | speed | **Minutes from block open to Chris producing something unscaffolded.** The best single speed number — it isolates orientation cost from session length, and converts hat check 2 ("fast orientation") from a binary judgment into a trendable number |
| `reps`, derived `min_per_rep` | speed | Throughput, comparable across subjects |
| `support_ai` / `support_chris` | learning rate | The dormant mechanism, activated. Two independent ratings; divergence is the finding, per `teaching-loop.md` |
| `decay` | learning rate | The strongest signal ever recorded here (Jul 21, 6 min). Currently only recoverable by accident |
| `cold_open` | retention | This check **already fires every continuing session** per `HAT_EDUCATOR` § Cold Checks. It is simply never scored. Free data |
| `misses[].class` | retention | **`regression` vs `fresh-gap` is the retention signal.** Vocabulary already proven in the Aug 1 PYTHON entry |
| `durability_due` / `_result` | retention | Extends the PHYSICS table to every subject. `proven (durable)` vs `passed (immediate)` stays the doctrine |
| derived `interval_days` | retention | 48–72 h is a *guess*. With 20 rows the optimal interval becomes measurable instead of assumed |
| `methods_fired` / `moves_used` | method fit | The optimization payload. Checkboxes, not prose |
| `ai_defect` | AI quality | What makes the log self-correcting — today's three-times-asked-for-an-unmodelled-output entry is the model |

**Chris's total input: one word (`support_chris`) and a glance at the clock.** Everything else the
AI already knows at close and currently writes as paragraphs.

---

## 4. What this buys — the optimization questions it makes answerable

None of these are answerable today. All become answerable at ~15–20 rows.

1. **Speed.** Is `ttfio_min` falling? A rising `ttfio` with a flat `clock_min` means orientation
   cost is growing — a system defect, not a learner one.
2. **Learning rate.** Does `support_ai` fall across reps on the same topic? That is the July 21
   claim, finally testable at scale rather than on one file-timestamp coincidence.
3. **Calibration.** How often does `support_chris` exceed `support_ai`? Persistent divergence
   means the AI is systematically under-reading how much help it is giving — the exact defect
   the 2026-07-25 review caught and could not quantify.
4. **Retention.** What share of `passed (immediate)` reps reach `proven (durable)`? What is the
   regression rate by subject? **Is 48–72 h the right interval, or should it be 24 h or 5 days?**
5. **Method fit — the legitimate form of the "learning style" question.** Cross-tabulate
   `methods_fired` against `durability_result`. Which of the seven standing methods appear in
   durable passes and which appear in reopened ones? Which delivery moves precede a low `ttfio`?
   This is a measured answer about *techniques*, and it is the only defensible version of the
   question.
6. **Load.** Which subject costs the most minutes per durable rep — the real input to the course
   weighting (PHYS → CSE → TCOM → ECON → ENGR), which is currently ranked by judgment alone.

### Two confounds to state up front

- **The two-pass pace rule (breadth → depth) is still unconfirmed by Chris** and is flagged as
  such in `HAT_EDUCATOR.md`. `mode:` captures which pass a session ran so the rule can finally be
  graded against outcomes instead of impression.
- **Hat-log check 1 is `n/v` on all three existing rows** because those sessions knew the routing
  chain before the subject came up. A clean check-1 reading still requires a fresh session opening
  cold on a subject. The scorecard does not fix this; only the rehearsal schedule can.

---

## 5. Placement

| Artifact | Home | Action |
|---|---|---|
| Field spec, controlled vocabularies, error-class list, support scale | `03-WIKIS\EDUCATION\wiki\methods\session-measurement-spec.md` | **The one new file.** EDUCATION half A owns reusable learning methods — this is exactly its job |
| Learner scorecard rows | each hub's `log.md` | Append at the top of the entry. No new file; hub owns learner truth |
| AI scorecard rows | `EDUCATION\wiki\methods\hat-performance-log.md` | Extend the existing table. Six checks unchanged |
| Close obligation | `HAT_EDUCATOR.md` § Session close | One added line. **This is the governance change requiring approval** |
| Index entry | `EDUCATION\wiki\index.md` | One line under Shared learning methods |
| Rollup / analysis | *not yet* | Created at ≥15 rows, per `OPERATIONS.md`: do not build scaffolding around nothing |

`PYTHON\wiki\teaching-loop.md` is **not** replaced — it is the source of the support-rating design
and stays as the hub's method page. The spec generalizes it; the scorecard is what finally applies it.

---

## 6. Rollout, with a real stop rule

| When | Step |
|---|---|
| **Aug 18–20** | **Pilot, 3 sessions.** The combined PHYS rows 2+3 durability rep, the CSE Module 0 resume, and one TCOM or ECON block. No new mechanism — just fill the fields on work already scheduled |
| **Aug 22** | **Dress rehearsal, full timetable.** The only honest test of whether the close cost is real under a full day |
| **Aug 23** | **Keep/cut at the pre-semester review.** Stop rule below |
| **Aug 24** | Field set locks for the semester |
| **~Sep 20** | First rollup at the September monthly review, at 15–20 rows |

### Stop rule — binding, not advisory

> **Any field left blank or guessed in more than one of the four pilot sessions is deleted on
> Aug 23, not "reminded about."**

A field nobody fills is not a measurement, it is a gap that reads as data. This is the same
failure mode as the durability obligation that lived in prose and went unscheduled — recorded in
`PHYSICS\wiki\current-position.md` § Open Durability Checks.

**`check_at`:** Aug 23 (keep/cut) and the September monthly review (first rollup, keep/modify/revert).
**Owner:** Claude Code implements; Chris approves and rates `support_chris`.

---

## 7. What is needed from Chris

**One approval:** add the scorecard as a required step in `HAT_EDUCATOR.md` § Session close, and
create `session-measurement-spec.md`. Everything else follows without further gates.

**Two decisions inside it, if he wants to steer:**

1. **Field count.** The block above is 12 learner fields. A leaner cut — drop `reps`, `decay`,
   `mode` — costs the throughput and pace-rule questions but nothing in speed, retention, or
   method fit. Recommendation: run all 12 in the pilot and let the Aug 23 stop rule cut them on
   evidence rather than guessing now.
2. **Does the pilot start before Aug 24 or at it?** Recommendation: **before.** Rehearsal week is
   precisely when the close cost should be measured, and three of the four pilot sessions are
   already on the calendar.

---

## 8. Return packet

- **Outcome:** EDUCATION measurement audited; no plan found; five disconnected pieces inventoried
  with six named gaps; a 12-field, two-home, one-key instrument specified with rollout and stop rule.
- **Evidence:** direct reads of `EDUCATION\OPERATIONS.md`, `current-position.md`, `index.md`, all
  three `methods\` pages, `HAT_EDUCATOR.md` + playbooks, `PHYSICS\OPERATIONS.md` teaching contract,
  `PHYSICS\wiki\current-position.md` + `log.md`, `PYTHON\wiki\teaching-loop.md` + `log.md`, and
  `claude_report_2026-08-13_teaching_layer_rebuild.md` §4 (rubric source).
- **Capability/status movement:** none claimed. No file was modified. This is a proposal.
- **Reusable-asset candidate:** the instrument itself — a two-home/one-key scorecard is the general
  pattern for any place `.ROOT` must measure two separated evidence classes against each other.
- **System-learning candidate (filed, not promoted):** *a measurement obligation written only in
  prose is not a measurement.* Third instance — the durability check (2026-08-17), PYTHON's
  unscheduled spaced items (2026-08-01), and the dormant support-rating pair (2026-07-25). Three
  instances is past the evidence threshold in `AGENT.md` § System Evolution Authority; this one is
  ready for `SYSTEM_LEARNINGS.md` on Chris's word.

---

*Displacement recorded: this ran on a Monday of rehearsal week with CSE Module 0 paused mid-block
at the lecture-vs-lab distinction, on Chris's direct request. `AGENT.md` Execution Discipline 2 —
recorded once, no resistance.*
