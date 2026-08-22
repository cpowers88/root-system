---
type: plan
timeline: now
tags: [programming, education]
---

# CSE 1321 / 1321L — 17-Week-Plus A Plan

## Mission and authority

Run this plan from **Wednesday, August 19 through the end of final exams,
December 14, 2026**. It is the dated execution layer for [[syllabus-alignment]];
that page still owns course facts, [[learning-path]] owns the durable Stage 0–10
path, and [[current-position]] alone owns Chris's demonstrated mastery.

The objective is to make an A the operational target: all graded work submitted
independently and on time, course concepts readable before lecture, closed-resource
performance trained before exams, and weaknesses repaired from evidence. No plan can
guarantee the grade, but this one controls the parts Chris can control.

**Live D2L and instructor information supersedes every date here.** Reconcile this
page on August 24 and whenever a live date changes.

## What the complete review says to use

| Bucket | Material | Decision for Fall 2026 |
|---|---|---|
| Course spine | The 17 official lecture decks; exact-section lecture and lab syllabi; *Think Python*, 2nd ed. | Use in live module order. The decks add `match`, nested loops, `break`/`continue`, `random`/`time`/`math`/`os`, two-dimensional lists, bubble sort, class-versus-instance state, mutable-field hazards, and the bounded Java bridge. |
| Active wiki core | Stages 0–5b; the debugging/traceback subset of Stage 6; the decomposition habit from Stage 7; the course-core search/sort/OOP subset of Stage 8; linked concepts, patterns, flashcards, drills, mini-projects, and error pages | This is the semester mastery route. Use retrieval before rereading anything already passed. |
| Support only after a miss | *Python Crash Course*, *Automate the Boring Stuff* Chapters 1–8, *Python Workout*, *Invent Your Own Computer Games*, and selected *Grokking Algorithms* Chapters 1–2 and 5 | Open one source for the exact gap only. Never stack multiple explanations before attempting a transfer. |
| Useful but deferred | Stage 6 file persistence; Stage 8 recursion/Big O/regex; Stages 9–10; APIs, SQL, pandas, NumPy, data visualization, CLI, `pytest`, automation, databases, web apps, and deep Java | Not part of the Fall A-path unless D2L or the instructor explicitly introduces it. |
| Exercise reserve | Existing wiki drills/projects and the unprocessed w3resource captures under `raw/` | Existing wiki practice is ready. The raw captures remain an unvetted reserve with visible solutions, not the active spine. |
| Do not use | Python 2 sources, superseded duplicates, and the contents of the 13 graded labs or 7 graded assignments | Python 2 can mis-teach the course. Graded prompt content must never become AI-assisted practice. Only the permitted filename-derived topic sequence is used here. |

The learner starts this run **ahead of the opening course module but at the Stage 4b
mastery frontier**. That is useful: early course weeks become durable retrieval, not
permission to sprint into off-syllabus material.

## Non-negotiable academic-integrity boundary

- Chris completes every CSE submission, quiz, lab, assignment, and exam without AI.
- Do not paste a live prompt, submitted code, autograder message, or protected
  question into AI. AI may teach the underlying concept later using a fresh problem.
- Every program in the private bank below is an original, ungraded practice task. It
  must never be reshaped to resemble a live assignment after that assignment opens.
- If graded status is uncertain, stop and verify before discussing the material.
- Official review slides contain answers. Cover the answer slide, work the question
  cold, commit to an answer, and only then reveal it.

## The weekly operating system

The whole-semester workload model budgets **7–9 outside-class hours per week for CSE
1321 + 1321L**. This plan lives inside that budget; it is not extra work added on top.

### Ordinary-week allocation

| Work | Weekly budget | Done means |
|---|---:|---|
| Live lecture/lab work and submissions | 3–5 h | Requirements read early; work is Chris's own; submitted before the deadline; Gradescope/D2L receipt checked. |
| Read-ahead and retrieval | 60–90 min | Local page first, named spine sections second, support source only after a miss. |
| Trace, skeleton, and fresh construction | 90–120 min | One cold read/trace, one pseudocode or skeleton, and one fresh build or bounded extension. |
| Closed-resource quiz/exam preparation | 30–60 min | Timed retrieval, scored before correction, followed by a delayed fresh recheck. |
| Course administration or tutoring | 20–45 min | D2L look-ahead, gradebook check, and tutoring-credit record. |

Use the long campus gaps before adding evening work. Tuesday's final 60–90 minutes
before lab are for lab readiness or light retrieval, not a second difficult new topic.

### Default cadence

1. **Sunday — control (20 minutes):** inspect D2L seven days forward, record every
   deadline, choose the week's private proof, and reserve a tutoring visit when due.
2. **Before Monday lecture (35–45 minutes):** local stage/concept page, then the named
   deck or book sections. Write three retrieval questions.
3. **Monday after lecture (15 minutes):** close the notes and write what changed,
   what remains unclear, and one predicted quiz trap.
4. **Before Tuesday lab (30–45 minutes):** write a cold trace or skeleton from fresh
   private material. The live lab itself remains AI-free.
5. **Before/after Wednesday lecture (30 + 15 minutes):** second read-ahead, then
   explain the main construct without notes.
6. **Thursday or Friday (60–90 minutes):** complete the week's private program or
   debug rep, predict before running, and test boundaries.
7. **Weekend (35–50 minutes):** closed-resource mixed retrieval; score the first
   answer, repair the error class, and schedule a 24-hour recheck.

### Collision-week minimum

When another course or a CSE exam creates a red week, deadlines and exam preparation
win. The minimum is: two 20-minute retrieval blocks, one trace or skeleton, D2L/
Gradescope confirmation, and no optional program. Week 12 and Week 14 already invoke
this rule below.

## A-grade scorecard

Track these weekly without copying protected question content:

- **Submission control:** 100% of known CSE work started at least 48 hours before its
  deadline when the release window allows; submission receipt checked.
- **Reading control:** next lecture's deck/local page opened before class; no broad
  support-book reading without an observed gap.
- **Code-reading proof:** one unseen private snippet marked Contract/Input/State/
  Control/Calls/Data shape/Output/Failure and traced before execution.
- **Construction proof:** pseudocode or skeleton precedes code; the program is written
  by Chris and passes normal, boundary, and invalid-input tests appropriate to scope.
- **Retention proof:** an error is not closed by immediate correction. A fresh version
  must be answered correctly at least 24 hours later.
- **Assessment readiness:** reach at least 80% cold on a fresh mixed set, repair misses,
  then reach at least 90% on a different set before an exam where time permits.
- **Help control:** if blocked for 30 focused minutes, use instructor/GTA/CCSE tutoring
  rather than AI on live coursework.
- **Tutoring credit:** complete and document ten qualifying visits by December 7.
  Target Weeks 1, 2, 4, 5, 6, 8, 9, 10, 11, and 13; adjust to center availability.

## Fresh private program bank

These specifications are independent of the course's graded prompt set. Chris writes
all code. Use only the constructs unlocked by the scheduled week.

### P0 — Paint-can estimator (libraries)

- Read wall area and square-foot coverage per can.
- Write `cans_needed(area, coverage)` and use `math.ceil()` inside it.
- Keep input/output in the caller; reject non-positive values.
- Prove: exact multiple, fractional can, and invalid-value cases.

### P1 — Fuel-stop estimator (atoms and expressions)

- Read distance, vehicle MPG, and price per gallon as decimals.
- Calculate gallons and estimated cost; format only at the output boundary.
- Before running, label every value's type and write the operator-precedence order.

### P2 — Weather-gear adviser (selection)

- Use temperature, precipitation yes/no, and wind speed to select one recommendation.
- Draft a branch table first. Use an `if`/`elif`/`else` chain where outcomes are
  exclusive and a separate `if` only for an independent safety warning.
- Prove threshold values immediately below, at, and above each boundary.

### P3 — Equipment-rate classifier (selection consolidation)

- Calculate a private rental estimate from hours, membership status, and an after-hours
  flag. Write the policy yourself before coding.
- Implement once with chained conditions; explain why two independent conditions would
  or would not change the result. Add one `match`/`case` menu after the core works.

### P4 — Seven-day output analyzer (loops)

- Read seven daily values with a loop; compute total, average, and days above a target.
- Use one counter and one accumulator. Predict the exact-maximum and exact-target cases.
- No lists in the first version; lists become an extension in Week 10.

### P5 — Inspection retry controller (loop consolidation)

- Accept `pass`, `retry`, or `stop` until success or a maximum-attempt limit.
- Use `continue` for a skipped attempt and `break` for one deliberate early exit.
- Trace every iteration and distinguish normal loop termination from `break`.

### P6 — Measurement toolkit (functions)

- Write three small conversion functions with parameters and return values.
- The caller owns all input and display. No globals; no calculation-only function prints.
- Trace argument binding, local state, and returned value for one call by hand.

### P7 — Quote builder (function composition)

- Separate subtotal, discount amount, tax amount, and final-total calculations into
  functions; one function must call another.
- Return numeric values until the final display. Test zero, normal, and boundary rates.
- Explain parameter versus argument and `return` versus `print()` after a timed pause.

### P8 — Reproducible sample planner (modules/libraries)

- Use `random.seed()` and `random.choice()` or `randint()` behind Chris-authored wrapper
  functions; use `math.ceil()` for the sample count.
- Run twice with the same seed and explain why the result repeats.
- `time` or read-only `os.getcwd()` may be explored separately; do not create or change
  directories inside the governed vault for this exercise.

### P9 — Maintenance-log analyzer (sequences)

- Store readings in a list, preserve a fixed configuration in a tuple, traverse by
  element and by index, and produce count/min/max/average.
- Add, update, and remove one list item; explain mutation, aliasing, and why the tuple
  should remain immutable. Add a small list-of-lists extension only after the core passes.

### P10 — Parts catalog and search bench (mapping/search/sort)

- Map unique part IDs to descriptions or quantities in a dictionary.
- Safely retrieve, insert, update, delete, and iterate key/value pairs.
- Write and trace a linear search and bubble sort on a separate list; compare them with
  `in` and `.sort()` without claiming the built-ins use the same algorithm.

### P11 — Work-order class (OOP)

- Define `WorkOrder` with `__init__`, at least three instance attributes, and two methods
  that read or change state. Create two independent objects.
- If a list attribute is used, initialize it inside `__init__`; prove the two objects do
  not accidentally share mutable state.
- Trace constructor flow, `self`, one method call, and the resulting state change.

### P12 — Python/Java concept bridge

- Implement one tiny original input → decision → loop → output task first in Python,
  then in Java using the course's skeleton and `Scanner` pattern.
- Annotate concept equivalence: types, braces/indentation, semicolons, string equality,
  loop syntax, methods, arrays/ArrayLists, and object construction.
- This unlocks only when the live course confirms Module 7. It is not a second Java path.

## Dated 17-week-plus run

### Week 0 — Aug 19–23: close the launch gap

- **Focus:** Stage 4b standard-library bridge plus course-start readiness.
- **Read:** [[stages/stage-04b-python-libraries]], [[concepts/standard-library-basics]],
  [[code-patterns/import-and-call-standard-library]], then the exact official
  documentation for `math.ceil()` and one `random` function.
- **Practice:** [[drills/stage-04-library-basics]]; complete P0 only if the drill does
  not already consume the available proof block. Run one mixed atoms/selection/loops/
  functions trace and recheck scope plus `return` versus `print()`.
- **Exit:** import, call, and wrap one library function; state its input/output contract
  without notes. Do not open Stage 5 yet.

### Week 1 — Aug 24–30: Module 0 and system verification

- **Read:** `m0_welcome.pptx`, `m0_algorithms_and_abstraction_v3.pptx`,
  [[concepts/decomposition-and-pseudocode]], *Think Python* Chapter 1 “Running Python”/
  “The First Program,” and Chapter 4 “A Development Plan” only.
- **Practice:** identify input → process → output in three short programs; turn two
  physical tasks into precise, finite, unambiguous steps; write one 5–8 step skeleton.
- **Build:** pseudocode only for an original campus-day planner; then implement the
  smallest straight-line version if all Week 1 course controls are clean.
- **Exit/admin:** explain abstraction versus decomposition; verify D2L, Gradescope,
  Respondus practice quiz, webcam/microphone, OneCompiler access, grade weights, quiz
  anomaly, lab schedule, and tutoring-credit procedure. Tutoring visit 1.

### Week 2 — Aug 31–Sep 6: Module 1, Quiz 1

- **Read:** both M1 decks; [[stages/stage-01-python-atoms]] by retrieval; *Think Python*
  Chapters 1–2 selected values/types/operators/assignment/expressions/order/strings/
  comments plus Chapter 5 “Keyboard Input.”
- **Practice/build:** type-and-value traces, five conversion decisions, one I/O skeleton,
  P1, and [[errors/stage-01-common-errors]] only where the cold work misses.
- **Exit:** explain why `input()` starts as text, predict mixed string/numeric behavior,
  and score a cold Quiz 1 set before correction. Tutoring visit 2.

### Week 3 — Sep 7–13: Module 2 selection begins

- **Read:** `m2_selectrion_structures_v3.pptx`,
  [[stages/stage-02-decisions-and-boolean-logic]], and *Think Python* Chapter 5 Boolean,
  logical, conditional, alternative, chained, and nested sections; skip recursion.
- **Practice/build:** truth tables, branch tables, path prediction, P2, and one planted
  `=` versus `==` or wrong-boundary defect.
- **Exit:** distinguish chained from independent conditions and predict exactly which
  paths execute without running the code.

### Week 4 — Sep 14–20: selection mastery, Quiz 2

- **Read:** retrieve before rereading the selection deck; use its `match`/`case` and
  nested-selection sections plus the Chapter 5 debugging/exercise material that matches
  observed errors.
- **Practice/build:** P3, one nested decision trace, one `match` menu trace, and one
  unreachable/wrong-branch debug rep.
- **Exit:** 80%+ cold mixed selection set, then a delayed fresh recheck of every miss.
  Tutoring visit 3.

### Week 5 — Sep 21–27: Module 2 repetition begins

- **Read:** `m2_repetition_structures_v3.pptx`,
  [[stages/stage-03-loops-and-repetition]], *Think Python* Chapter 7 reassignment,
  updating variables, `while`, and `break`, plus Chapter 8 string traversal.
- **Practice/build:** loop trace tables, range boundary predictions, nested-loop reading,
  and P4. Retrieve `%` only if divisibility reasoning is weak.
- **Exit:** locate initialization, condition/sequence, update, counter, accumulator, and
  stop rule in unseen loops. Tutoring visit 4.

### Week 6 — Sep 28–Oct 4: loop mastery, Quiz 3, Test 1 sweep

- **Read:** repetition deck sections on nesting, `break`, and `continue`; Chapter 7
  algorithms/debugging; reread only failed loop sections.
- **Practice/build:** P5; diagnose off-by-one, unchanged-state, and infinite-loop errors;
  run one timed Modules 1–2 set by Friday and a different one over the weekend.
- **Exit:** at least 80% cold, every miss classified, and at least 90% on the different
  post-repair set where capacity permits. No new topic in the final 48 hours. Tutoring
  visit 5.

### Week 7 — Oct 5–11: Test 1, then Module 3 functions

- **Assessment first:** Test 1 is listed for Monday, October 5. No same-day cramming.
- **Read after the test:** `m3_methods_v3.pptx`,
  [[stages/stage-04-functions-parameters-return]], and *Think Python* Chapter 3 calls,
  definitions, flow, parameters/arguments, local variables, and fruitful/void functions.
- **Practice/build:** caller-to-function trace, three signatures from prose, then P6.
- **Exit:** explain parameter/argument, local scope, and `return`/`print()` under a short
  timer. Begin lab-midterm cold practice only after Test 1.

### Week 8 — Oct 12–18: functions, Quiz 4, lab-midterm vicinity

- **Read:** *Think Python* Chapter 6 return values, incremental development,
  composition, and Boolean functions; skip recursion. Use the M3 optional/default
  parameter and built-in/string-method sections.
- **Practice/build:** one closed-resource lab-style private construction, P7, and one
  scope/`None`/missing-return debug rep. Keep calculations separate from I/O.
- **Exit:** produce a correct multi-function skeleton before coding and pass a delayed
  function-vocabulary recheck. Treat the lab midterm as closed book/notes/resources;
  confirm its live date. Tutoring visit 6.

### Week 9 — Oct 19–25: Module 4 libraries, Quiz 5

- **Read:** `m4_python_modules_and_libraries_v3.pptx`, Stage 4b pages, and official docs
  only for the selected `random`, `time`, `math`, or read-only `os` calls.
- **Practice/build:** P8, import/call traces, inclusive versus exclusive random bounds,
  deterministic-seed reasoning, and one wrong-module/wrong-call debug rep.
- **Exit:** explain import versus installation, pseudo-random seed behavior, and the
  contract of each used function. Tutoring visit 7.

### Week 10 — Oct 26–Nov 1: Module 5 sequences

- **Read:** `m5_sequence_types_v3.pptx`, [[stages/stage-05-data-shapes]], selected
  *Think Python* Chapter 8 string sections, Chapter 10 lists, and Chapter 12 tuple
  immutability/assignment only.
- **Practice/build:** index/slice predictions, mutation versus reassignment, element-
  versus-index traversal, list-of-lists trace, tuple unpacking, and P9.
- **Exit:** defend list versus tuple, explain aliasing, and trace a mutation through two
  references. Tutoring visit 8.

### Week 11 — Nov 2–8: dictionaries/search/sort, Quiz 6, Test 2 sweep

- **Read:** `m5_mapping_type_v3.pptx`, the manual-sort section of the sequence deck,
  [[stages/stage-05b-searching-and-sorting]], [[concepts/dictionaries]], and selected
  *Think Python* Chapter 11. Use *Grokking Algorithms* only if the local trace does not
  land.
- **Practice/build:** P10 early in the week; map keys/values and missing-key risk; trace
  linear search and bubble sort. Begin the Test 2 sweep immediately, not on Sunday night.
- **Exit:** mixed Modules 1–5 set by Thursday, repaired set Saturday, light retrieval
  Sunday. Front-load because Week 12 is the semester's worst collision. Tutoring visit 9.

### Week 12 — Nov 9–15: Test 2, OOP begins, red-collision minimum

- **Assessment first:** Test 2 is listed for Monday, November 9. The TCOM report and
  other course collisions make this a minimum-week by design.
- **Read after the test:** only `m6_object_oriented_programming_v3.pptx` through class,
  instance, attributes, methods, `self`, and `__init__`; selected *Think Python* Chapter
  15 programmer-defined types/attributes.
- **Practice:** one class diagram, one constructor trace, and a P11 skeleton only. Do not
  require the full program this week.
- **Exit:** distinguish class, object, instance attribute, class attribute, and method.
  Protect every live deadline; no optional support-book reading.

### Week 13 — Nov 16–22: OOP mastery, Quizzes 7–8

- **Read:** remaining M6 sections on class/instance attributes and mutable fields;
  selected *Think Python* Chapter 17 OOP, `__init__`, and object-display sections.
- **Practice/build:** complete P11; create two objects, trace state changes, and reproduce
  then repair a shared-mutable-class-list bug using fresh private code.
- **Exit:** cold class skeleton with `__init__` and one behavior; explain `self` and prove
  two objects maintain independent state. Tutoring visit 10.

### Fall break — Nov 23–29: retain, repair, protect capacity

- **Read:** no new chapters. Use only the two weakest measured Python pages or error
  records and the flashcards for Modules 1–6.
- **Practice:** one 30–45 minute mixed cold read/trace and one delayed correction. Stop
  there unless D2L exposes an urgent CSE date.
- **Exit:** no silent regression, but Physics/final preparation and whole-semester
  recovery keep priority. Do not speculatively start Java.

### Week 14 — Nov 30–Dec 6: confirmed Module 7 bridge, Quiz 9, red collision

- **Read:** only the M7 decks the instructor actually activates: Java basics/I/O/types,
  operators, flow control/methods, arrays/ArrayLists, and classes/objects. Map each idea
  back to its Python equivalent before memorizing syntax.
- **Practice/build:** P12 only if the live module requires it and the ECON final, TCOM
  project, Lab 13, and Assignment 7 are under control. Otherwise use the course work as
  the week's construction and do one 20-minute comparison trace.
- **Exit:** explain static versus dynamic typing, Java skeleton/`Scanner`, string
  `.equals()`, loop/method syntax, arrays versus Python lists, and object construction.
  No deep Java detour.

### Week 15 — Dec 7: Quiz 10 and cumulative review

- **Read:** `m7_python_review.pptx` using attempt-before-reveal; current weak spots,
  relevant stage mastery checklists, flashcards, and error pages. No new chapters.
- **Practice:** work review questions cold in small batches; run one mixed R1–R5 set:
  locate, trace, explain, skeleton, modify/debug. Never count reading an answer as proof.
- **Exit:** final exam date and rules confirmed; final weak-point list contains no more
  than three named skills, each with a fresh rep scheduled. Last day for tutoring credit.

### Final exam period — Dec 8–14: execute, do not expand

- **Read:** only failed sections and personal error-class notes; no broad rereading.
- **Practice:** one timed mixed simulation at least 48 hours before each known CSE exam,
  then short retrieval and sleep protection. Lab-final practice remains closed resource.
- **Exit:** independently read, trace, skeleton, implement, and debug course-level work
  under the exact permitted-resource rules. Record final results afterward without
  reproducing protected questions.

## Assessment sweeps

| Assessment | Preparation window | Required evidence |
|---|---|---|
| Quiz weeks | Two short blocks in the prior 72 hours | Vocabulary retrieval plus fresh output/trace questions; first score preserved before correction. |
| Test 1 — listed Oct 5 | Sep 28–Oct 4 | Two different timed Modules 1–2 sets, delayed repair, no new content in final 48 hours. |
| Lab midterm — live date required | Begin after Test 1; expected near Week 8 by sequence only | Closed-resource trace, skeleton, construction, and debug rep in the actual allowed environment. |
| Test 2 — listed Nov 9 | Start Nov 2; finish core sweep by Nov 8 | Two different timed Modules 1–5 sets; front-load because Nov 9–15 is the semester's worst week. |
| Lab final — live date required | Begin cumulative maintenance in Week 13; full sweep after Dec 3 | Closed-resource Python construction and debugging; bounded Java only if live scope confirms it. |
| Lecture final — D2L date required | Light cumulative maintenance from Week 13; full sweep after Dec 3 | Mixed R1–R5 code-reading set and targeted repair of no more than three weakest skills. |

## August 24 D2L reconciliation checklist

Update [[syllabus-alignment]], `04-SCHOOL/SEMESTER_MAP.md`, and this plan with:

- real lecture quiz and test dates, especially the Week 1 anomaly;
- real lab release/due dates, midterm date, and final date;
- the actual lecture grade weights shown in D2L;
- Respondus setup/practice completion and the exact exam technology rules;
- OneCompiler or other required lab-exam environment;
- permitted help/resource rules and any instructor AI clarification;
- tutoring-center visit-credit procedure and how each visit is documented;
- the live Module 7 scope and whether every M7 deck is assigned.

Chris does not need to supply anything else before the course opens. The next
information needed is the live D2L truth from this checklist.

## Semester-end mastery definition

The plan is complete only when course results and independent proof support it:

1. Chris can mark and trace an unseen mixed Python program accurately before running it.
2. Chris can turn a fresh requirement into pseudocode and a function/class skeleton.
3. Chris can independently construct course-level programs using decisions, loops,
   functions, libraries, sequences, dictionaries, search/sort, and classes.
4. Chris can classify syntax/runtime/logic failures, read a traceback bottom-up, form a
   repair hypothesis, and verify the repair with boundary tests.
5. Chris can explain the bounded Python-to-Java concept map required by the live course.
6. No generated page, completed reading, tutoring visit, or corrected answer is treated
   as mastery without a later independent transfer.

## Update rule

This page changes when D2L dates land, the instructor changes scope, or evidence shows
the weekly load/proof gate is miscalibrated. Actual learner progress never moves here;
record it in [[current-position]] and append the evidence to [[log]].
