---
type: log
timeline: now
status: active
tags: [education, methods, hats, evidence]
created: 2026-08-17
---

# Hat Performance Log

### Append-only evidence on how the teaching hats actually behave in live sessions.

**Why this exists.** The six-point rubric was written into a dated one-off report
(`System Update Log\2026-08-12_ROOT_UPDATE\claude_report_2026-08-13_teaching_layer_rebuild.md`)
and had **no live home**, so every observation about hat behaviour died in the DAILY it was
written in. Chris named the gap on 2026-08-17: *"the more reports we have on how the hats
worked the better."* One session is an anecdote; twenty rows is a signal about which hat rule
works and which one only reads well.

**This page holds AI-behaviour evidence, not learner truth.** Learner progress lives in each
hub's `current-position.md` and `log.md`. A hat can perform well in a session where Chris
misses, and badly in one where he passes — do not conflate them.

## The six checks — adopted verbatim, do not reword

| # | Check |
|---|---|
| 1 | **Correct hat + live owner loaded** |
| 2 | **Fast orientation** |
| 3 | **Chris retains control of pace** |
| 4 | **Real retrieval produced, not recognition** |
| 5 | **Boundaries respected** |
| 6 | **Correct close and resume point** |

**Grade check 1 honestly or not at all.** It tests whether the session found the right chain
*on its own*. A session that read the boot chain for other reasons before the subject came up
cannot be graded on it — mark it `n/v` (not valid), never `pass`. A contaminated check scored
as a pass is worse than no data.

## Scorecard

`✓` pass · `✗` fail · `n/v` not validly testable · `—` not exercised

| Date | Subject | Session type | 1 | 2 | 3 | 4 | 5 | 6 | Headline |
|---|---|---|:-:|:-:|:-:|:-:|:-:|:-:|---|
| 2026-08-16 night | PHYS (math row 2) | hour ~6 of a system session | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | Shortcut to the most specific hat: loaded `HAT_EDUCATOR` + `HAT_PHYSICS_MATH`, **skipped `HAT_PHYSICS` and the hub `OPERATIONS.md`** |
| 2026-08-17 midday | PHYS (math row 3) | hour ~4 of a system session | n/v | ✓ | ✓ | ✓ | ✓ | ✓ | Full chain loaded incl. both previously-skipped files — but check 1 is **not valid**, see entry |
| 2026-08-17 evening | CSE Module 0 | continuing Codex thread after system audit | n/v | ✓ | ✓ | ✓ | ✓ | ✓ | Correct live chain reloaded; ungraded-practice boundary held; clean pickup handoff |
| 2026-08-18 afternoon | PHYS (row 2 durability) | hour ~4 of a system/CASTLE session | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Row 2 passed durable. **AI defect: one question was unparseable and asked twice before Method 3 fired** — and this session then mis-diagnosed the skip as a learner verification gap. Chris corrected both |
| 2026-08-21 morning | PHYS (row 3 + circular motion) | user-requested teaching session | n/v | ✓ | ✓ | ✓ | ✓ | ✓ | Full chain loaded; two misses classified honestly; switched from cold gate to lesson when six-month recall gap surfaced; terminal-math rendering defect fixed |

---

## 2026-08-16 (night) — PHYS math-readiness row 2

**Failure worth keeping: the session shortcut to the most specific hat.** `AGENT.md`'s routing
table sends PHYS to `HAT_PHYSICS` → hub `OPERATIONS.md` → `current-position.md`, with
`HAT_PHYSICS_MATH` added **"also"** — additive, not substitute. The session loaded
`HAT_EDUCATOR` + `HAT_PHYSICS_MATH` and skipped the other two.

**Why it matters beyond tidiness:** the hub `OPERATIONS.md` carries the teaching contract,
including the **48–72 h durability check**. Skipping it is how row 2's pass was recorded with
no durability obligation attached to it — see the 2026-08-17 entry, where that omission
surfaced a full day later.

**Not a clean test either** — it was hour six of a system session, not a fresh opening.
Recorded in `DAILY_2026-08-16.md`.

## 2026-08-17 (midday) — PHYS math-readiness row 3

**Check 1 marked `n/v`, deliberately.** The full chain *was* loaded — `HAT_EDUCATOR` →
`HAT_PHYSICS` → `HAT_PHYSICS_MATH` → hub `OPERATIONS.md` → `current-position.md` →
`math-readiness-path.md`, including the two files skipped on Aug 16. But this session had
already read `AGENT.md` end-to-end hours earlier for unrelated system work, so it knew the
routing table before physics was ever mentioned. **It did not discover the route; it
remembered it.** Scoring that as a pass would manufacture evidence the rehearsal exists to
collect. A clean check-1 test needs a fresh session that opens on a subject.

**Checks 2–6 are validly gradeable and all passed:**

- **2 — fast orientation.** The block opened with a frame and a skeleton in one turn.
- **3 — Chris retains control.** He skipped the four cold-check questions and went straight to
  the rebuild; the session followed without re-arguing the original order.
- **4 — real retrieval.** Cold rebuild from `a = const` with no formula sheet, plus a cold
  transfer problem. Not recognition.
- **5 — boundaries.** AI-prohibited status honoured; practice only. Also **declined to
  over-claim**: flagged before the rep that ~15 h is inside the 48–72 h window, so the pass
  could not be banked as durability evidence.
- **6 — close and resume.** Logged to `PHYSICS\wiki\log.md`, row 3 marked in
  `math-readiness-path.md`, resume point moved to row 4 in `NOW.md`, durability check recorded
  as owed.

### 🔎 AI-side defect — the session asked three times for an output it had never modelled

**This is the most useful thing in the entry and it is a failure of the hat's own delivery
contract.** The session asked Chris for a reasonableness check, got a skip, asked again, got a
skip, asked a third time and got *"sounds about right to me"* — **and only then** taught what a
reasonableness check actually is (arriving at the same number by a different road).

`HAT_EDUCATOR` § delivery contract rule 2 is **"Skeleton before blank page."** Asking for an
output whose *form* Chris has never been shown is a blank page. The correct move was to model
it once at the **first** miss, not the third.

**Consequence for the learner record:** row 3's log entry attributes the dropped
reasonableness check to *missing form, not carelessness* — and that diagnosis is only credible
because the session eventually noticed its own contribution. **If the check drops a fourth time
on row 4, the "missing form" explanation is dead and the cause is elsewhere.**

**Candidate hat amendment, not yet approved:** `HAT_EDUCATOR` § Short Corrections could carry a
trigger — *"if Chris skips a requested output twice, the problem is the request, not the
answer: model the output once, then ask again."* Do not implement without Chris's approval.

### Not exercised this session

- **Two-pass pace rule** (breadth → depth) — single depth pass on one topic. Still unconfirmed;
  only Chris can grade it.
- **Deliberate fact conflict** — not presented.

### Exercised and held

- **Words before symbols on the constant of integration** — third consecutive session,
  unprompted. This was the July 30 diagnosed gap and it is now behaving like a closed one.
  Worth a formal call after one more cold rep.

## 2026-08-17 (evening) — CSE Module 0, paused for school pickup

**Check 1 is `n/v`.** The correct Educator → Python → hub chain was reloaded before teaching,
but this continuing thread had already inspected the boot and hat system during the readiness
audit. It did not discover the route cold.

**Checks 2–6 passed:** the session opened from CASTLE's exact task and gave one visible map;
Chris controlled the pace through successive explain-backs; retrieval used a fresh
three-test-average problem rather than recognition; the CSE AI-prohibition boundary held; and
the pickup interruption closed with the exact next question recorded across NOW, the weekly
plan, the learner log, DAILY, and handoff.

The session also corrected a plan/source overlap: formal abstraction stays with Wednesday's
Module 1 Part 1 because the Module 0 transcript only lightly supports it. The breadth/depth
rule was not fully tested because the block paused early.

## 2026-08-18 (afternoon) — PHYS math row 2, durability check

**Check 1 is a genuine `✓` this time.** The full chain was loaded cold on the course→hat
routing rule — `HAT_EDUCATOR` → `HAT_PHYSICS` → hub `OPERATIONS.md` → `current-position.md` —
including the two files the Aug 16 session skipped, and the hat was named before the first
teaching move without Chris naming it. Unlike Aug 17, this session had **not** previously
inspected the hat system in-context, so the check is validly testable.

**Checks 2–6 passed.** The rep was handed over cold with no teaching first, which is what a
durability check requires; retrieval was a genuine transfer (`a(t) = 12t − 4`, fresh from the
Aug 16 `a(t) = 6t`) rather than recognition; the PHYS §54 tutor-permitted / submitted-work
prohibited boundary held with no graded material touched; and the close named row 3's exact
hour and the alternative row 4 entry point.

### ✗ AI-side defect — a question Chris could not parse, asked twice

The units question ("units on every term of your `x(t)`") was skipped twice. This session read
the second skip as evidence of a learner pattern — *"has the understanding but doesn't produce
the verification move"* — and said so.

**Chris corrected it:** *"on not producing the move I did not understand the question, so I
didn't even think that was what you were on about."*

Two failures, one of them the more serious:

1. **The question was ambiguous.** "Units on every term" was heard as the `a → v → x` chain,
   which Chris answered correctly and which is a reasonable reading. The intended question was
   units on the *coefficients inside* `x(t)`. The phrasing never distinguished them.
2. **The diagnosis was built on the ambiguity.** Generalising a learner defect from a question
   the learner could not parse is the worse error, because it would have propagated into the
   record as durable learner truth. It is corrected in `PHYSICS\wiki\log.md` 2026-08-18.

`HAT_PHYSICS` Method 3 — *"if Chris skips a requested output twice, the problem is the request,
not the answer"* — **fired and was correct.** It should have fired one ask earlier, and when it
fired the session should have suspected the question rather than the learner. **Method 3 needs
a companion clause: when a skip triggers it, re-read the question before forming any inference
about the learner.**

### ✓ Format that worked — reusable

Once Method 3 fired, the repair was: **model one term completely, show that the units live in
the coefficient rather than the variable, then ask for the remaining terms.** Chris produced
all three instantly and correctly, and reported: *"that explanation from above on the units was
perfect for me for understanding."*

This is the hub's own `skeleton → guided rep → transfer` loop applied at the smallest possible
grain — one term, not one problem. Worth reaching for whenever an abstract requirement is being
asked for rather than shown.

### Learner-owned correction, recorded not adjudicated

Chris also overrode the Aug 17 *"missing form, not carelessness"* attribution on the
reasonableness check: *"my form is 100% careless… I can't count the amount of times I dropped a
value and gotten an answer wrong."* Both accounts stay on record; his is operative. The
consequence is in the PHYSICS log — it raises the habit's value rather than lowering it,
because dropped values are precisely what a second-road check catches.

## 2026-08-19 — HAT_TCOM, session 1 (Claude Code)

**Six-point rubric.**

| # | Check | Score | Note |
|---:|---|:--:|---|
| 1 | Correct hat + live owner | **n/v** | Chris named TCOM in his opening message, so the hat was not discovered — it was handed over. Not a valid test of the Aug 16 course→hat routing rule |
| 2 | Fast orientation | ✅ | Full boot chain + hat chain + the §04 syllabus read end to end before the first teaching move |
| 3 | Chris retains control | ✅ | Opinion given when asked, recommendation made, no argument when he redirected to the artifact build |
| 4 | Real retrieval, not recognition | ✅ | Opened with 8 cold questions before any teaching. The diagnostic produced the session's most valuable finding |
| 5 | Boundaries respected | ✅ | Declined to draft or outline the Week 1 instructor email under §04's blanket AI-drafting prohibition; stated the permitted lane once and stayed in it |
| 6 | Correct close and resume point | ✅ | Recorded below and in the hub log |

### ✅ What worked — reusable

**Cold diagnostic before teaching, on recall material.** Eight questions cost about two minutes
and produced more than a syllabus re-read would have: not just *which* facts were missing but
**that the confident wrong answers were correct rules borrowed from another course.** A reading
block would have shown neither. **On multi-course recall material, diagnose before teaching —
the error pattern is the finding, not the score.**

**Naming the misfire as a strength rather than a deficit.** Chris generated filenames from a
category taxonomy. That is the Numerical-Detective/systems instinct doing its normal job on
material with no generating rule. Saying so — *"there is no rule, and reaching for one is how
the points go"* — landed better than a correction would have, and it generalises: the same pull
will appear on her rubrics.

### 🔴 AI defect found — the hub's own study aids were teaching the wrong rule

Logged here per the Aug 17 direction to record AI defects, not only Chris's misses.

Two pages built 2026-08-13 (`common-errors`, `flashcards`) asserted
`LastName_04_AssignmentName.docx` as the **required** TCOM naming pattern. It is a fallback,
and every string the syllabus actually prints breaks it. **Chris's failed reps reproduced the
vault's own error**, which is the strongest possible evidence that a study aid can teach a
defect straight through to performance.

**Root cause:** those pages were written from the syllabus's *calendar tables* and never from
its *policy and directory sections* — half a source, read as the whole. Both corrected the
same session; authoritative version now at
[[../courses/tcom-2010/concepts/course-policies-and-file-naming]].

**Candidate standing rule, offered not adopted:** *a study aid derived from part of a source
names which part.* Two instances now (this, and the 2026-08-18 semester-map claim written from
memory of a sibling page). One more and it earns a place in `WIKI_SHARED_LAYER.md`.

### Resume point

TCOM Part B — the ~8 uncued policy facts — then a spaced re-rep of the four filename strings
before Tue Aug 25.

## 2026-08-21 — HAT_PHYSICS, row 3 and circular motion (Codex)

**Six-point rubric.**

| # | Score | Evidence |
|---|:---:|---|
| 1 | n/v | Chris explicitly requested PHYS work, so discovery was not validly testable; the full `HAT_EDUCATOR` → `HAT_PHYSICS` → hub owner chain was still loaded. |
| 2 | ✓ | The session resumed at the exact Row 3 and Stage 4 frontiers and used source-verified textbook pages. |
| 3 | ✓ | Chris controlled the pace, corrected his own algebra/equation choice, and requested the switch from cold drilling to reading and lesson. |
| 4 | ✓ | Row 3 and circular-motion Problem 1 began cold; first responses were preserved as evidence rather than replaced by corrected answers. |
| 5 | ✓ | No graded WebAssign answer was produced; the work stayed in tutoring, fresh examples, and study-material preparation. |
| 6 | ✓ | Both misses, error classes, fresh-transfer rules, reading route, durability window, and printable study asset were recorded. |

### AI defect and repair

LaTeX-style equations were unreadable in Chris's terminal. The session had used a
document-quality math format on a surface that did not render it. `00-BRAIN\CODEX.md`
now requires plain-text equations in terminal or CLI conversation and reserves rendered
mathematical notation for files, artifacts, and interfaces that support it. The printable
formula sheet deliberately uses conventional typeset notation because that is the requested
document surface.


---

*Method owner: `03-WIKIS\EDUCATION`. Consumed by `00-BRAIN\HATS\HAT_EDUCATOR.md`. Rubric source:
`00-BRAIN\Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\claude_report_2026-08-13_teaching_layer_rebuild.md` §4.
Companion: [[learning-how-to-learn-principles]], [[memory-techniques]].*
