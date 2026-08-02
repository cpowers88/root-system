---
type: tracker
timeline: now
tags: [programming]
---

# Current Position

## Status

Active Python beginner pathway.

## Content Generation Progress (what exists in the vault)

Generated curriculum: **Stages 0-10 complete.** Every stage from `wiki/stages/stage-00-setup-and-orientation.md` through `wiki/stages/stage-10-application-thinking.md` has a full packet (concept pages, glossary, flashcards, code patterns, drills, mini-projects, common-errors pages). This describes what has been *built*, not what Chris has *studied*.

## Chris's Actual Study Progress (where Chris is)

- **Stage 0 — satisfied.** Chris meets every Stage 0 setup/orientation item already (see Learner Baseline below).
- **Stage 1 — satisfied (2026-07-13).** Chris worked Stage 1 independently with Codex on 2026-07-12 (files: `02-LIBRARY\00-SCHOOL\01-CSE-Python\Stages\Stage-01-python-atoms\{starter_prompt,variables,expressions,types}.py`) — real code, not generated-and-untouched. Verified in this session, not assumed from the code alone: explained why `int()`/`float()` conversions were needed before use, correctly predicted then confirmed a `TypeError` from `age + 5` on an unconverted string, and correctly reasoned through `+`-concatenation vs. f-string mechanics after one correction. `starter_prompt.py` satisfies the About Me mini-project spec (input, conversion, calculation, formatted output). `variables.py` also demonstrated early reassignment/accumulator patterns (Stage 3 territory) with no issues.
- **Stage 2 — satisfied (2026-07-16).** `S2P1.py`, `S2P2.py`, `S2P3.py`, and
  `Story.py` exist under `02-LIBRARY\00-SCHOOL\01-CSE-Python\Stages\Stage-02-python_wiki\`.
  Cold explain-back completed: Chris correctly explained why `Story.py` uses
  `elif` for mutually exclusive tunnel/bridge paths and `or` for the two
  equivalent bridge choices (spikes/snakes). `S2P3.py`'s grading rule was
  independently corrected (removed the stray `D` band, `else` now prints `F`
  for anything below 70) and verified. See `wiki/log.md` 2026-07-16.
- **Stage 3 — satisfied (2026-07-26).** Stage 3 loop tracing Part A is complete. On July 22,
  Chris independently constructed and explained the fresh password-controlled
  `while` transfer, corrected a divisible-by-7 counter after one focused counter
  cue, and built the limited-attempt guessing-game through staged live guidance;
  its fifth-guess win and five-miss loss boundaries both passed. On July 23, he
  successfully ran and traced the saved `for.py` attempt, explained the correct
  first match and `break` termination, completed a clean nearby `for` transfer,
  and independently built a multi-part loop that counted values matching an
  `or` condition. On July 26, `Code/stage3_gate.py` supplied the final fresh
  construction gate: one five-day input loop, running-total accumulator,
  above-30 counter, average, and process pseudocode. The first run exposed a
  denominator-order error and inclusive boundary; Chris corrected both and
  passed normal (`125 / 2 / 25.0`), exact-30 (`30 / 0 / 6.0`), and decimal
  (`31 / 1 / 6.2`) tests. Verdict: PASS WITH CORRECTION.
- **Current study stage: Stage 4 — Functions.**
  `wiki/stages/stage-04-functions-parameters-return.md`.
- **Stage 4 cold baseline — PASS WITH CORRECTION (2026-07-27).** Chris wrote
  and ran `add_this(a, b)` and `greet(name)` cold
  (`02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\{function,greet}.py`).
  First explain-back pass conflated parameter/argument and described `def` as
  a "label generator." After one physical anchor (mail slot: `def` labels an
  empty slot = parameter; the call drops a real value in = argument), a fresh
  transfer on `greet(name)` / `greet("Chris")` correctly identified `name` as
  the parameter and `"Chris"` as the argument in both directions. One residual
  correction given, not yet re-tested: `return` sends the computed value back
  out to the caller, it does not "hold" the argument.
- **Stage 4 reading complete (2026-07-27/28).** *Think Python* pp. 43-52
  (Monday, after the cold baseline) and pp. 83-87 (Tuesday morning) both
  read.
- **Function Lab A — PASS WITH CORRECTION (2026-07-28).** Chris built
  `is_even(x)` and `fahrenheit_to_celsius(f)` cold from a blank file
  (`02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\{is_even,
  degreesF_toC}.py`), both returning rather than printing. Real first-
  attempt failure caught and corrected: the first `fahrenheit_to_celsius`
  truncated with `int((f - 32) * 5) / 9` — applying `int()` before dividing
  by 9. Chris predicted the function's output by hand for both the buggy
  order (36.888888...) and the corrected order (36.944444444), then fixed
  it to `c = float(float(f - 32) * 5) / 9`, matching the predicted correct
  value. Also worked through: functions must `return` (not print a
  formatted string) so callers can still do math with the result; display
  formatting belongs at the call site. Full record:
  `wiki/log.md` 2026-07-28.
- **Drill complete (2026-07-28 evening).** `shout(a)` built — void, prints
  `a.upper() + "!!!"`, called twice with different arguments. Explain-back
  on why it doesn't need `return`: Chris's first answer correctly identified
  that nothing outside the function needs to use a result (printing finishes
  the job), but described this as "no loop to exit" — a `return`/`break`
  conflation, corrected (`return` hands a value back to the caller; it has
  no relationship to loops). PASS WITH CORRECTION. All three drill
  functions now done: `fahrenheit_to_celsius`, `is_even`, `shout`.
- **Function Toolbox mini-project — PASS WITH CORRECTION (2026-07-29).**
  Chris built `percent_of(t, p)`, `add_tax(a, b)` (refactored unprompted to
  call `percent_of` internally), and `bill_calculator(x, y, z)` (calls
  `add_tax`, returns a formatted receipt string) — all cold, all correct,
  chained across two levels of "one function uses another's return value."
  Caught and self-fixed a real percentage-vs-decimal input bug via
  predict-before-run. Execution-order explain-back (the mini-project's actual
  gate item) passed unprompted. One recurring correction given twice: calling
  a `percent_of`-style return value "a percentage" when it's an amount — the
  rate is always the input, never the output; worth a cold re-check next
  occurrence. Full record: `wiki/log.md` 2026-07-29.
- **Common-error debug item — PASS, independently verified (2026-07-29
  evening).** After an earlier invalid attempt (editing the reference page's
  examples instead of writing real code — reverted, not counted), Chris
  wrote `code/error4.py` cold: reproduced the NameError out-of-scope pattern
  and fixed it by calling `square(5)` and printing its return instead of the
  undefined bare `n`. Explain-back was correct and went further than asked —
  he identified that `n` unquoted triggers a name lookup that fails because
  `n` was never bound at module scope, and separately that `"n"` in quotes
  would just print a literal character with no lookup at all. Follow-up
  question confirmed the concept cleanly: correctly reasoned that
  `square(n)` would *also* fail, since argument evaluation happens before
  the call and `n` still isn't defined in the caller's scope — a parameter
  name is a local label, not a variable exposed anywhere outside the
  function. Full record: `wiki/log.md` 2026-07-29 (evening).

## Stage 4 — CLOSED (2026-07-29)

Cold baseline, three-function drill, Function Toolbox mini-project, and the
common-error debug rep are all independently verified. Stage 4b (Python
libraries) is next.

**Both open retest items closed (2026-08-01, off-plan Saturday check —
weekly plan marked the day no-school; Chris redirected).** Fresh cold
function (`discount_amount.py`, calling the existing `percent_of.py`):
(1) return-value framing — correct unprompted explanation, including that
`return` also exits the function; (2) rate-vs-amount — tracked cleanly
through the whole rep, no recurrence of the "percentage" mislabel. A new,
different miss surfaced and self-corrected on one pointer: first draft
returned the discounted *total* (60) instead of the discount *amount* (20)
the spec's own worked example named — fixed immediately once pointed back
at the example, then unprompted renamed a variable that shadowed the
function's own name. Full record: `wiki/log.md` 2026-08-01.

**Friday's un-run Test Day timed quiz taken late, off-plan (2026-08-01).**
Closed-book, one attempt, six questions covering the Mastery Checklist.
**Score: 2 clean PASS, 1 partial, 3 MISS — recorded honestly before any
correction**, per the plan's own rule. Two of the three misses were
regressions on items already independently verified PASS earlier in the
week (parameter/argument, 07-27; the `error4.py` scope/NameError concept,
07-29) — a real signal that those explain-back verdicts were not fully
durable under timed closed-book pressure. Chris self-reported after
scoring that his original written answers for both were correct and he
changed them before submitting — re-diagnoses the failure as **answer-
flipping under pressure, not a conceptual gap**, though the submitted
score stands unchanged (same rule as a real quiz). Immediate retest:
parameter/argument corrected fast and clean on one restated question
(concept-cue level, holds). Scope/local-variable-lifetime needed a full
worked-step correction (not just a concept cue) before a clean "no" landed
on a fresh check — treat this as **not yet secure**, worth a real cold
recheck next time it comes up naturally, not assumed fixed by one correct
answer immediately after the explanation. The fourth item (Q4, print vs.
return) was a genuine misjudgment, not a flip — the real rule is about
whether the caller needs to reuse the result, not about data type. Full
record: `wiki/log.md` 2026-08-01.

- **Exact learner frontier:** Stage 4b — [[stages/stage-04b-python-libraries]].
  Nothing read yet; unlocks now that Stage 4 is closed.
- **Code evidence in the MCP Bootcamp workbench:** `Code/for.py` records the
  recovered first-match trace; `Code/for2.py` records the nearby divisible-by-7
  transfer; `Code/PT.py` records the independent multi-part `or` condition plus
  count (`10`); and `Code/stage3_gate.py` records the final loop/accumulator
  gate. Supporting reps are `count.py`, `practice2.py`, `practice3.py`,
  `practice4.py`, `password.py`, and `secret#.py`. The MCP
  infrastructure files (`mcp_contracts.py` and `server.py`) belong to Claude's
  separate integration lane and do not count as Python mastery proof.
- **Stages 4-10 are generated but not yet mastered.** Their packets exist and
  are ready, but Chris has not worked through or demonstrated mastery of any of
  them yet. Do not treat their existence as progress.

**This page must never be read as "Chris should start at Stage 10."** Stages 0-3
are complete. Resume at the exact Stage 4 frontier above.

## Current Learner Baseline

### Confident

- Create `.py` files.
- Run `.py` files in VS Code.
- Run `.py` files from terminal when file location is known.
- Use `print()`.
- Understand strings as text.

### Developing

- Variables: can create them, but needs fluency with references, reassignment, and use cases.
- Integers/floats: knows decimal vs. non-decimal, needs operational practice.
- `input()`: can collect input, needs conversion/storage practice.
- `if` / `elif` / `else`: knows what they do, needs "when to use" instinct.
- Comparison operators: recognizes them, needs decision practice.
- Boolean logic: recognizes `and`, `or`, `not`, needs repetition.
- Functions: recognizes `def` and function calls, weak on parameters and return values.
- Loops: recognizes `for` and `while`, gets confused writing them.
- Lists: knows they exist.

### Not yet confident

- Function parameters.
- Function return values.
- Dictionaries.
- Reading error messages / tracebacks reliably; debugging from error messages.
- Choosing the correct code tool for the problem.

*(This page is the ONLY home of the learner baseline as of July 11, 2026 — the copy formerly in CLAUDE.md was merged here during the slim pass.)*

## Primary Bottlenecks

1. Vocabulary retention and recall.
2. Knowing when to use each code construct.
3. Writing loops confidently.
4. Understanding function parameters and return values.
5. Reading/debugging tracebacks.
6. Avoiding advanced-material overload.

## Semester Competency Target

For Fall 2026, optimize this hub for independent **code reading and code reasoning**:
locate inputs/state/control flow, trace execution, predict output, explain construct
choice, write pseudocode and skeletons, then implement and debug course-level Python
without AI assistance. Vibe coding and AI-generated implementation are out of scope
for this hub and cannot count as learner proof.

## Current Reading Queue

- **Read now:** nothing new. Drill and Toolbox mini-project are both complete;
  go straight to [[errors/stage-04-common-errors]] for the last Stage 4 gate
  item (one debug rep, no help).
- **Do not read yet:** standard library ([[stages/stage-04b-python-libraries]] —
  unlocks only after the Stage 4 functions gate closes), collections,
  searching/sorting, OOP, or Java. Their exact unlock triggers and semester
  reminders live in [[syllabus-alignment]].

## Stage Structure — realigned to the syllabi 2026-07-25

Stage 4 and Stage 5 each carried two course modules, so their gates could not close
against a single week of course work. Split, with **no stage renumbered and no file
renamed**, so every existing link still resolves:

| Course module | Assessed | Stage |
|---|---|---|
| M3 — Functions | Lecture Wk 7–8, Quiz 4; Lab 7 + A4 | [[stages/stage-04-functions-parameters-return]] |
| M4 — Python Libraries | Lecture Wk 9, Quiz 5; Lab 8 | [[stages/stage-04b-python-libraries]] |
| M5.1 + dictionaries | Lecture Wk 10–11; Labs 9–10 | [[stages/stage-05-data-shapes]] |
| M5.2 — searching & sorting | Lecture Wk 11, Quiz 6; Lab 10 | [[stages/stage-05b-searching-and-sorting]] |

Still open from that review, not yet actioned: Module 0 (decomposition, algorithms,
abstraction) is taught in **lecture Week 1** but lives at Stage 7; Module 7 (intro
to Java, graded as Lab 13 + Assignment 7) has no vault home; and Stages 6, 9, 10
are not in either syllabus and should be labelled a beyond-course track rather than
read as prerequisites Chris is behind on.

## Teaching Method

Sessions run the loop in [[teaching-loop]] — cold attempt before instruction,
support escalated only as far as the observed error requires, explain-back, fresh
transfer. Adopted 2026-07-25 on the Stage 3 evidence; **Chris rates the support
level he needed at the end of each rep**, alongside pace and depth.

## Learning Design Requirements

- Glossary-first.
- Flashcard-ready.
- Sequential reading path.
- Small drills.
- Explain-back prompts.
- Physical-world anchors when useful.
- Park advanced topics.
- Teach computer-science thinking and Python mechanics together.
- Start every meaningful session with `Read now`, `Read next after proof`, and
  `Do not read yet`; move the queue only from actual proof or the live course module.

## Academic Integrity Notes

- **CSE 1321 and CSE 1321L are `ai-restricted`.** Both official Fall 2026 PDFs
  explicitly prohibit submitted content created or assisted by generative AI.
- AI may support private concept learning and ungraded practice. It must not draft,
  solve, rewrite, or debug submitted course work. Stop and ask whenever graded status
  is unclear. See [[syllabus-alignment]].

## School Alignment (official syllabi verified 2026-07-15; raw/ replaced 2026-07-27 with fresh captures)

- **Instructors confirmed 2026-07-27:** CSE 1321 lecture — Eun Sik Kim, meets
  Mon/Wed 4:10–5:30 PM (Academic Building Rm 203, in-person). CSE 1321L lab —
  Muhammad Usman, meets Tue 5:45–7:35 PM (Atrium Building Rm 2120, in-person).
  No conflict with Physics lecture (MWF 9:10–10:05 AM) or Chris's Tuesday
  4–5 PM therapy.
- Course schedule covers ~13-15 weeks: decomposition/abstraction → data types/operators/Boolean → selection → iteration/loops → functions/parameters/arguments → Python libraries → tuples/lists → dictionaries/searching/sorting → OOP → (lab only) intro to Java.
- Topics Chris must master before class begins: vault Stages 1-4 (atoms, decisions, loops, functions) — matches Weeks 1-4 of the existing 8-Week Python Foundation Plan.
- *Think Python* is the recommended, no-cost course text and is already the Stage
  1-8 spine.
- Lecture: 10 quizzes and 3 exams; fall/spring weighting is 25% each for quiz
  average, Test 1, Test 2, and final. Lab: 13 labs and 7 assignments; weighting is
  40% assignments, 10% labs, 20% midterm, 30% final.
- The path now includes a small standard-library bridge at the end of Stage 4 so
  "Python Libraries" is learned in syllabus order before Stage 5 data shapes.
- Full outcome, policy, assessment, and schedule-anomaly details: [[syllabus-alignment]].

## Spine Source

**Think Python, 2nd Ed. (Allen Downey)** — selected 2026-06-24 as active spine for Stages 1-8. See `wiki/source-map.md` for the chapter-to-stage mapping.

**Automate the Boring Stuff, 3rd Ed. (Al Sweigart)** — added 2026-06-24 as active spine for Stages 9-10 (automation bridge, application thinking), resolving the gap left by Think Python. Chapters 1-9 also usable as support/practice for Stages 1-6. Chapter 10 (Reading and Writing Files) added 2026-06-24, filling the earlier gap.

**Python Crash Course, 3rd Ed. (Eric Matthes)** — added 2026-06-24 as support/practice for Stages 1-7, valued for its dense numbered exercises (good fit for Chris's explain-example-drill learning profile) and for being the first source to cover automated testing (Ch.11, `pytest`). Part II project chapters (Pygame game, data visualization, likely a web app) parked for Stage 10.

**Grokking Algorithms, 2nd Ed. (Aditya Bhargava)** — added 2026-06-24 as support/practice for Stage 8's algorithms portion (Ch.1-5: intro, selection sort, recursion, quicksort, hash tables — matches syllabus Week 11 "searching and sorting"). Visual style fits Chris's "visual structure is critical" learning need. Ch.6-13 (trees, Dijkstra, dynamic programming, k-NN, etc.) parked — beyond syllabus scope.

**Think Like a Programmer (V. Anton Spraul)** — added 2026-06-24. Flagged: code examples are in C++, not Python (stated prerequisite is C++ fluency). Usable only as a strategy/discussion support source at Stage 7 — read the problem-solving narrative, not the code. Not a spine, not a code-reading source for Chris yet.

**A Common-Sense Guide to Data Structures and Algorithms, 2nd Ed. (Jay Wengrow)** — added 2026-06-24 as Stage 8 support, complementing Grokking Algorithms with Big O rigor and extra structures (stacks/queues, linked lists, BSTs). Code language not yet confirmed — verify before treating as a Python code source.

**Invent Your Own Computer Games with Python, 4th Ed. (Al Sweigart)** — added 2026-06-24. **Primary mini-project source**, spanning Stages 2-8 and into Stage 10. Includes a flowchart-based decomposition chapter (Ch.7, Hangman) that directly models Stage 7's program-design goal.

**Python Workout, 2nd Ed. (Reuven M. Lerner)** — added 2026-06-24 as a drill bank (200 short exercises) spanning Stages 1, 4, 5, 6, 8, 9-10. Directly serves the vault's Drill Rule.

### Source Intake Checkpoint — Classified and Controlled

The active spine and support roster is mapped across all 11 stages (0-10), and
later arrivals are classified in `wiki/source-map.md`. Do not use the old
"two syllabi + six books" count as a control total; the hub now contains additional
classified books, official documentation, and parked data/SQL strands. Intake stays
closed unless a specific learning gap justifies reopening it.

## Current Next Action

Stages 0-4 are closed (Stage 4 closed 2026-07-29: cold baseline, three-function
drill, Function Toolbox mini-project, and the common-error debug rep all
independently verified; both retest items and Friday's Test Day quiz closed
off-plan 2026-08-01). **Next action: Stage 4b — Python libraries**
([[stages/stage-04b-python-libraries]]) — nothing read yet, unlocked now that
Stage 4 is closed. All later packets remain content readiness, not study
progress until worked and verified.
