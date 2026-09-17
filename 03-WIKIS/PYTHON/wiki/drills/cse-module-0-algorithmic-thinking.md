---
type: drill
stage: 00
status: live
concepts: ["algorithmic-thinking", "trace-and-predict", "pseudocode", "desk-check", "decomposition"]
difficulty: beginner
solution_included: false
timeline: now
created: 2026-08-30
tags: [programming, school, cse-1321]
---

# Drill: Module 0 Algorithmic Thinking — CSE course overlay, un-gated

> **Why this page exists and why it ignores the stage gates.** The hub has carried this
> mismatch since 2026-07-25: Module 0 (decomposition, algorithms, abstraction) is taught in
> **lecture week 1** but its drill lives at Stage 7, and Chris is at Stage 4b. On 2026-08-29
> the instructor assigned exactly this work and the vault had no home for it. **This is a
> course-overlay drill: it follows the lecture, not the spine.** It supersedes nothing —
> [[stage-07-decompose-a-problem]] stays where it is for the spine's own arc.
>
> **Targets:** Quiz 1 (Sun Sep 6, LockDown Browser) · Test 1 (Mon Oct 5, Modules 1–2).

## Integrity boundary

CSE prohibits AI on submitted work. Every prompt here is **fresh private practice** — no
lab, assignment, or quiz content, ever. AI may generate new problems on these patterns and
check Chris's reasoning; it may not touch anything submitted.

## The three rep types — matched to what the course grades

### A — Trace and predict (the quiz format)

Given a short pseudocode or Python fragment: **write the final value of every variable
before anything runs.** Use a desk-check table — one column per variable, one row per loop
pass. The rep is cold; the table is the work product.

**Pass bar:** the predicted values match execution, *and* the table shows every intermediate
state — a right answer with skipped rows is a partial pass.

### B — Pseudocode from a word problem (the lecture's assigned skill)

Given a plain-language task (counting, accumulating, filtering a list): write numbered
pseudocode — inputs, outputs, decisions, loops, edge cases — with **no Python syntax**.

**The one lesson week 1 already taught, kept in front of every rep:** *procedure, not
narration.* On 2026-08-29 Chris caught, unprompted, that his own `unless piece < desired`
clause was narration — the `while` condition already handled it. That catch is the skill.
Every line of pseudocode must be something a machine could execute; a line that describes
intent without changing state gets struck.

**Pass bar:** another person (or a later Chris) could implement it without asking questions.

### C — Boundary and initialization selection (where the marks leak)

Short forced-choice reps, one decision each, cold:

- `>=` or `>` at a stated boundary — and *why*, in one sentence.
- `//` or `%` or `/` for a stated need — compute both against a worked number before
  answering (the 2026-08-29 rep landed this after one cue).
- Where does the counter/accumulator initialize, and what breaks if it doesn't.
- **Scope and local-variable lifetime** — marked *not yet secure* on 2026-08-01 and
  unrechecked since, with Test 1 (Mon Oct 5) covering it. First C-rep block should hit
  this: predict what a name inside a function is worth after the function returns.

## The closing move on every rep — the reasonableness check

**End every rep by stating the expected result from your own stated procedure, then
checking the two agree.** This is the standing habit from `04-SCHOOL\miss-log.md` — it
appeared in CSE on 2026-08-29 (a closing "counter needs to equal 4" that contradicted the
procedure stated one clause earlier: `10 // 3` is 3). The habit closes by **firing
unprompted three times**, not by being re-explained. Sessions: watch for it, count it,
never prompt it.

### Open item carried in

- **The unfinished `4`.** The 2026-08-29 rep (count cut pieces from board lengths) closed
  with that unresolved contradiction. First A-rep of the next block: re-run the same
  numbers cold and let the desk-check table settle it. *Not logged as a miss — the rep was
  unfinished, not failed.*

## Cadence

One block ≈ 20 minutes: 2 × A, 1 × B, 3 × C. Before Quiz 1 (Sep 6), A-reps lead. After
Module 1 posts, pull C-rep vocabulary from the module's own construct list — capped by
D2L, per the lead rule (`04-SCHOOL\semester-workload-plan.md` § The lead).

## Answer policy

No solutions on this page. AI checks reasoning live, after Chris commits to an answer —
never before.
