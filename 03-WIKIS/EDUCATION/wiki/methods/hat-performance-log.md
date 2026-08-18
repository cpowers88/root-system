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

---

*Method owner: `03-WIKIS\EDUCATION`. Consumed by `00-BRAIN\HATS\HAT_EDUCATOR.md`. Rubric source:
`00-BRAIN\Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\claude_report_2026-08-13_teaching_layer_rebuild.md` §4.
Companion: [[learning-how-to-learn-principles]], [[memory-techniques]].*
