---
type: map
timeline: reference
tags: [programming, governance, education]
---

# CSE 1321 / 1321L Semester Pathway

## Purpose and Authority

This page is the authoritative bridge between Chris's exact Fall 2026 lecture/lab
syllabi and the staged Python path. It owns course alignment and the semester
operating pathway. [[current-position]] remains the only owner of actual mastery and
the exact next drill; [[learning-path]] remains the durable Stage 0–10 curriculum.

Active sources (canonical, immutable — this hub's `raw/` folder per `CLAUDE.md` §
Folder Structure):

- `03-WIKIS\PYTHON\raw\syllabi\CSE 1321 BF (81262) Fall 2026 Syllabus.md`
  — lecture, Section BF, CRN 81262, instructor Eun Sik Kim.
- `03-WIKIS\PYTHON\raw\syllabi\CSE 1321L 04 (86703) Fall 2026 Syllabus.md`
  — lab, Section 04, CRN 86703, instructor Muhammad Usman.

Both are direct Simple Syllabus captures from July 21, 2026, and both are
byte-identical to a working duplicate Chris also keeps at
`04-SCHOOL\01-CSE-Python\` for his own coursework use — that copy is
Chris's personal workspace, not wiki-governed, and is not the citation target.
`raw\syllabi\CSE_lecture_syllabus.md` and `raw\syllabi\CSE_lab_syllabus.md` are a
separate, older pair of schedule-only quick extracts (topic order only, no policy/
grading/AI-restriction content) predating the July 21 full captures; they still
exist for that narrower purpose but are superseded as the policy/grading source by
the two full syllabus files above. (sources: both active syllabus files, frontmatter
and course sections)

## The Outcome Chris Actually Wants

The course goal is not merely “write Python without help.” Chris wants to become a
strong **code reader and code reasoner** who can independently inspect, trace,
explain, structure, write, and debug the Python used in this course.

By semester end, the target is that Chris can take a short beginner program he has
not seen before and:

1. State its purpose, inputs, outputs, and assumptions.
2. Mark the data, decisions, loops, function calls, and object boundaries.
3. Trace important variables by hand and predict output before execution.
4. Explain why each major construct was selected and name a reasonable alternative.
5. Find the likely failure point from behavior, a traceback, or a failed test.
6. Write pseudocode plus a function/class skeleton before implementation.
7. Make one bounded change and predict what else the change could affect.
8. Build and debug the course-level implementation independently from the skeleton.

This is a local learning target derived from Chris's stated direction; it is not a
claim that the syllabus uses the phrase “code reader.” It supports the syllabus's
actual outcomes in computational problem solving, data and expressions, control
flow, collections, functions, classes, debugging, testing, documentation, and
correct-code/security awareness. (sources: both active syllabi, course information
and learning-outcomes sections)

## Non-Negotiable AI Boundary

Both syllabi prohibit submitted work that was created or assisted by generative AI.
The prohibition applies even if Chris understands the generated result afterward.

| Activity in this hub | AI boundary | Chris's required ownership |
|---|---|---|
| CSE 1321/1321L submitted work, quizzes, labs, assignments, or exams | **AI prohibited.** Do not draft, solve, rewrite, or debug it with AI. | Read, plan, code, test, and debug independently, using only resources the course permits. |
| Private concept study | AI may teach the concept, ask questions, or create a fresh ungraded drill that is not derived from an active assignment. | Attempt first, predict before running, write the code, explain back, and complete a fresh transfer. |
| Vibe coding or AI-generated implementation | **Out of scope for this hub.** Do not place it in the CSE pathway or use it as mastery evidence. | Any future AI-generated build belongs in a separate permitted project context. |

When graded status is unclear, stop and ask. Never paste a live course prompt or
course code into AI for debugging. A safe help request is concept-level—for example,
“teach me accumulator loops with a fresh example”—not “fix my Lab 6 program.”
(sources: both active syllabi, AI-use policy sections)

## Course Controls and Data-Quality Warnings

### Lecture — CSE 1321

- Three credit hours with CSE 1321L as a concurrent prerequisite.
- *Think Python*, 2nd edition, is the recommended no-cost text and the Stage 1–8
  spine in this hub.
- Ten quizzes and three exams are delivered through D2L. The syllabus identifies
  the Fall/Spring weighting as quiz average 25%, Test 1 25%, Test 2 25%, and final
  25%; the lowest quiz is dropped.
- The same capture also contains a second, unlabeled 40% quiz / 20% midterm / 40%
  final table. Treat the 25/25/25/25 Fall/Spring table as the current working model,
  but verify the actual D2L gradebook or instructor statement once the course opens.
- Exams require Respondus LockDown Browser, webcam, microphone, and reliable
  internet. A technical make-up request requires a UITS ticket plus instructor
  contact within 24 hours.
- Up to ten CCSE Tutoring Center visits add 0.5% each to both lecture and lab final
  exam scores, for a maximum 5% addition.
- Calendar anomalies: the otherwise Fall-aligned table lists the Week 1
  syllabus/policy quizzes as due December 7 and mentions May 4, 2026 in the final
  review row. D2L/FYE/instructor dates control where the capture conflicts.

(source: lecture syllabus, course materials, requirements, grading, calendar,
course-policy, and technology-resource sections)

### Lab — CSE 1321L

- One credit hour with CSE 1321 as concurrent prerequisite.
- Thirteen labs and seven assignments are submitted through Gradescope.
- Assignments are 40%, lab exercises 10%, midterm 20%, and final 30%; the lowest
  assignment and lowest lab exercise are dropped.
- The midterm and final are in class, closed book, closed notes, with no outside
  resources. That makes cold reading, tracing, and skeleton construction essential,
  not optional enrichment.
- Gradescope regrade requests must be made per question within three business days
  after grades publish.
- The lab calendar is a recycled January–May/Spring schedule despite the Fall 2026
  title. Use its topic order and assessment pattern only. Do not use any printed lab
  date until D2L or the instructor supplies the real Fall schedule.

(source: lab syllabus, course requirements, grading, calendar, and AI-policy sections)

### Lab and assignment sequence — module map (added 2026-08-18)

Derived **from filenames only** in `raw/lab_instructions/` and `raw/assignments_lab/`, which
Chris captured from the course site on 2026-08-18. This records *what order the work arrives
in*, which is the topic-order extraction § INGEST permits. **No prompt content is reproduced
here, and none was read into the wiki** — see the boundary note below.

| Course module | Labs | Assignments | Vault stage this leans on |
|---|---|---|---|
| M0 — setup | Lab 1 installations | — | Stage 0 |
| M1 — type systems | Labs 2, 3 | Assignment 1 | Stage 1 |
| M2 — flow control | Labs 4, 5, 6 | Assignments 2, 3 | Stages 2–3 |
| M3 — methods | Lab 7 | Assignment 4 | Stage 4 |
| M4 — libraries | Lab 8 | — | Stage 4 (stdlib bridge) |
| M5 — sequence types | Labs 9, 10 | Assignment 5 | Stage 5 |
| M6 — object-oriented programming | Labs 11, 12 | Assignment 6 | Stage 8 |
| M7 — Java | Lab 13 | Review assignment 7 | out of scope for this Python hub |

**Three things this map makes visible that the syllabus prose did not:**

1. **Flow control is the heaviest block** — three labs and two assignments on one topic,
   more than any other module. It maps to vault Stages 2–3, and **Stage 3 is exactly where the
   frontier has been stuck since July** (circular-motion drills are PHYS; here it is loops).
   The course spends its largest single block where Chris is already weakest.
2. **M4 libraries has a lab but no assignment**, and M0 has a lab but no assignment — so the
   seven assignments concentrate in M1, M2 (×2), M3, M5, M6, plus the M7 review.
3. **Java appears only in the final lab and the review assignment**, confirming the existing
   note that Lab 13 is the sole Java contact point.

**Dates are unusable, sequence is sound.** Every file is versioned `sp26`/`spr26` — Spring 2026
— consistent with the recycled-calendar warning above. Lab 1's body prints `# Term: ...` as a
blank for the student to fill, so the material is term-agnostic by construction. **Confirm the
live Fall dates in D2L from Aug 24.**

**Boundary note, recorded deliberately.** These 20 documents are live graded work — assignments
40%, lab exercises 10%, submitted through Gradescope with an autograder. Per § Non-Negotiable AI
Boundary and `OPERATIONS.md` § Academic integrity, their prompts were **not** ingested, summarised,
paraphrased, or converted into drills, and must not be later. Chris reads the prompts; the wiki
holds the sequence. If a future session needs practice for a module, it authors a **fresh**
exercise from the concept pages — never one derived from an active prompt.

(source: `raw/lab_instructions/` and `raw/assignments_lab/` filenames, captured 2026-08-18;
Lab 1 body read only far enough to confirm graded status and term-agnosticism)

## Code-Reader Competency Ladder

Each course module should move through the same ladder. A topic is not secure merely
because Chris can recognize its syntax.

| Level | Capability | Evidence |
|---|---|---|
| R1 — Locate | Identify inputs, outputs, state, decisions, repetition, functions, and data structures. | Annotate an unseen short program without running it. |
| R2 — Trace | Follow execution order and record variable changes. | Produce a correct trace table and output prediction. |
| R3 — Explain | Explain purpose, construct choice, boundaries, and common failure modes. | Plain-English explain-back without reading the lesson. |
| R4 — Skeleton | Turn a requirement into pseudocode, function signatures, control-flow placeholders, and tests. | Write the structure before implementation. |
| R5 — Modify/debug | Make a bounded change or identify a defect without destabilizing unrelated behavior. | Prediction, edit, test, and post-change explanation. |

The expected semester progression is R1–R2 during atoms/selection/loops, R3–R4
during functions and collections, and R5 during searching/sorting and OOP.

## Code-Reading Markup Key

Use the same labels every time so a new program does not require inventing a new
reading method:

- **Contract:** what the program or function promises to do.
- **Input:** values entering through literals, `input()`, parameters, or files.
- **State:** variables or object attributes that can change.
- **Control:** decisions, loops, early exits, and execution order.
- **Calls:** where execution enters another function or method and later returns.
- **Data shape:** string, list, tuple, dictionary, object, or other structure.
- **Output:** printed, returned, written, or mutated results.
- **Failure:** assumptions, boundary cases, and the first line that can break.

For a trace, use five columns: `step/line`, `condition or operation`, `values before`,
`values after`, and `output`. Keep the table on paper or in private practice notes;
the goal is accurate execution reasoning, not decorative documentation.

## The Repeated Study Unit

For every module, use this sequence on private, non-graded material:

1. **Vocabulary retrieval:** define the week's terms before opening notes.
2. **Cold read:** inspect a fresh program and mark input → state → control flow →
   output without executing it.
3. **Trace:** predict execution and variable changes by hand.
4. **Run and compare:** execute only after the prediction; explain any mismatch.
5. **Skeleton:** write pseudocode and structural placeholders from a fresh prompt.
6. **Independent completion:** fill the smallest working version without AI.
7. **Debug:** diagnose one planted syntax, runtime, or logic error.
8. **Explain-back:** state what the program does, why its constructs fit, what could
   break, and how one change would propagate.

This loop is capacity-sized; it is not a rigid weekly calendar. Course deadlines
still outrank private practice.

## Reading Reminder System

Chris should never have to scan the whole vault to decide what to read. At the start
of every meaningful Python session, the AI states four lines before teaching:

```text
Course module / vault stage:
Read now:
Read next, after this proof:
Do not read yet:
```

The reminder follows these rules:

1. **Read just ahead, not months ahead.** Unlock the next module's required reading
   after the current proof or when the live course begins that module.
2. **Local map first.** Read the stage page and named concept pages before the book
   chapter so Chris knows what to look for.
3. **Required before support.** Use *Think Python* as the spine. Open a support book
   only when the spine explanation or the first fresh attempt does not land.
4. **Attempt before rereading.** If a concept has already been studied, run cold
   retrieval first; reread only the failed portion.
5. **Live dates win.** When D2L publishes the real topic/deadline, move the reminder
   to that module even if the captured calendar differs.
6. **Close the loop.** After reading, the next action is always trace, skeleton,
   drill, or explain-back—not more reading.

The volatile “read now” item is kept in [[current-position]]. The full semester
queue below is the durable reminder map.

## Semester Reading Queue

| Unlock trigger | Read first in this hub | Required spine reading | Support only if needed | Read-result check |
|---|---|---|---|---|
| Course Week 1 / Module 0 opens | [[stages/stage-00-setup-and-orientation]] plus [[concepts/decomposition-and-pseudocode]] | *Think Python* Ch. 1 “Running Python” and “The First Program”; Ch. 4 “A Development Plan” only | *Invent Your Own Computer Games* Ch. 7 flowchart discussion after the local page, not the project code | Mark input→process→output and turn one requirement into ordered steps. |
| Lecture Module 1 opens | [[stages/stage-01-python-atoms]] and its linked concept pages; use retrieval before rereading | *Think Python* Ch. 1 values/types/operators; Ch. 2 assignment, variables, expressions, order, strings, comments; Ch. 5 “Keyboard Input” only | *Python Crash Course* Ch. 2 or *Automate the Boring Stuff* Ch. 1 | Trace types/value changes and write an input→conversion→processing→output skeleton. |
| Lecture selection module opens | [[stages/stage-02-decisions-and-boolean-logic]] and its linked decision pages; use retrieval first | *Think Python* Ch. 5 Boolean expressions, logical operators, conditional/alternative/chained/nested execution; skip recursion | *Python Crash Course* Ch. 5 or *Automate the Boring Stuff* Ch. 2 | Build a branch table, predict the path, and explain chained vs. independent decisions. |
| Current pre-semester Stage 3 frontier or lecture repetition module opens | [[stages/stage-03-loops-and-repetition]], then [[concepts/while-loops]] and [[concepts/counters-and-accumulators]] only after a failed cold attempt; read [[concepts/modulo-and-divisibility]] immediately before the divisible-by-7 proof if `%` cannot be explained | *Think Python* Ch. 7: reassignment, updating variables, `while`, `break`, algorithms; Ch. 5 “Floor Division and Modulus” only as needed; Ch. 8 “A String Is a Sequence,” `len`, and “Traversal with a for Loop” only | *Automate the Boring Stuff* Ch. 3 or *Python Crash Course* Ch. 7/4 | Trace loop state, explain `number % 7 == 0`, and complete the fresh `while`, counter, and guessing-game proofs. |
| Stage 3 closes or lecture Module 3 begins | [[stages/stage-04-functions-parameters-return]], [[concepts/defining-and-calling-functions]], [[concepts/parameters-and-arguments]], [[concepts/return-values]] | *Think Python* Ch. 3: calls, definitions, flow, parameters/arguments, local variables, stack diagrams, fruitful/void; Ch. 6: return values, incremental development, composition, Boolean functions | *Python Crash Course* Ch. 8; *Automate the Boring Stuff* Ch. 4; *Python Workout* Ch. 7 | Trace caller→function→return and produce a function skeleton before bodies. |
| Stage 4 core closes or lecture Python Libraries week begins | [[concepts/standard-library-basics]], [[code-patterns/import-and-call-standard-library]], [[drills/stage-04-library-basics]] | Official Python documentation for the one selected standard-library function; no broad library survey | None unless the official documentation is too terse | State the imported function's input/output contract and use it behind one wrapper. |
| Lecture Module 5.1 or Stage 5 begins | [[stages/stage-05-data-shapes]], then [[concepts/strings-as-sequences]], [[concepts/lists]], and [[concepts/tuples-and-sets]] | Selected *Think Python* Ch. 8 string sections; Ch. 10 lists; Ch. 12 “Tuples Are Immutable” and “Tuple Assignment” only | *Python Crash Course* Ch. 3–4; *Automate the Boring Stuff* Ch. 6 | Trace indices, slices, mutation, traversal, and aliasing; defend list vs. tuple. |
| Lecture Module 5.2 begins | [[concepts/dictionaries]], [[concepts/sorting-and-searching]], then the Stage 8 course subset in [[stages/stage-08-think-python-readiness]] | Selected *Think Python* Ch. 11 dictionary sections; use the local sorting/searching page for the required algorithm bridge | *Grokking Algorithms* Ch. 1–2 and Ch. 5 for visual search/sort/hash-table support | Trace a dictionary lookup plus one search and one simple sort by hand. |
| Lecture Module 6 begins | Stage 8 course subset, [[concepts/classes-and-objects]], [[code-patterns/class-with-init-and-method]] | *Think Python* Ch. 15 programmer-defined types/attributes and selected Ch. 17 `__init__`/printing-object sections; skip Ch. 16 and inheritance depth unless the live course requires them | *Python Crash Course* Ch. 9; *Python Workout* Ch. 10 | Map class→instance→attributes→methods and write a class skeleton independently. |
| Exception handling appears in class or a traceback gap blocks progress | [[stages/stage-06-files-errors-debugging]], [[concepts/exceptions-and-tracebacks]], [[concepts/debugging-process]] | *Think Python* Ch. 20 debugging sections; Ch. 14 exception sections as needed | *Python Crash Course* Ch. 10; *Automate the Boring Stuff* Ch. 5 | Read the traceback bottom-up, name the error class, failing line, and repair hypothesis. |
| Lab Java introduction is confirmed live | No broad Java packet yet; use instructor/FYE material first and map concepts back to the Python Stage pages | Only the assigned/authorized course reading | None until a specific gap appears | Explain how one familiar construct changes notation without starting a second curriculum. |
| Review/final period | Current-position weak spots, stage mastery checklists, flashcards, and recorded error pages | Reread only failed *Think Python* sections | The support source that previously resolved the exact gap | Complete a mixed cold read, trace, skeleton, and debug set; no new chapters. |

The chapter list is a **when-to-read map**, not a demand to read all chapters now.
Each row unlocks only when its trigger is true.

## Topic-to-Path Map

| Official topic or outcome | Primary path coverage | Code-reader emphasis |
|---|---|---|
| IDE, compile/run/debug/test | Stage 0; debugging deepens in Stage 6 | Predict before run; distinguish syntax, runtime, and logic failures. |
| Decomposition, algorithms, abstraction | Planning habit begins now; full packet in Stage 7 | Translate prose into named steps and visible boundaries. |
| Input/output, variables, types, operators, expressions | Stage 1 | Track types and value changes; identify conversions and precedence. |
| Selection / branching | Stage 2 | Build branch tables; find mutually exclusive vs. independent decisions. |
| Repetition / loops | Stage 3 | Trace iteration state; identify stop condition, update, counter, accumulator. |
| Functions, parameters, arguments | Stage 4 | Trace call/return flow; separate interface, local state, and returned value. |
| Python libraries | Stage 4 standard-library bridge | Read import/call structure and consult documentation for a function contract. |
| Tuples and lists | Stage 5 | Track indices, mutation, traversal, and aliasing. |
| Dictionaries | Stage 5 | Track key/value access, missing-key risk, and structure choice. |
| Searching and sorting | Stage 8 course subset | Trace comparisons/swaps and state the algorithm's contract. |
| Classes / OOP | Stage 8 course subset | Map class → instance → attributes → methods → state change. |
| Exception handling | Stage 6 | Read traceback bottom-up; identify protected operation and recovery boundary. |
| Arrays | Stage 5 terminology bridge | Treat Python lists as the beginner collection; keep NumPy parked. |
| Documentation, correct code, security | Stages 1, 6, and 7; used throughout | State assumptions, validate input, test boundaries, and distrust unexplained success. |
| Intro to Java (lab only) | Small post-OOP bridge | Compare concepts and structure; do not start a parallel Java curriculum early. |

## Pre-Semester Gate — Now Through August 23

The preparation target is not “finish every generated page.” It is to enter Week 1
with the course's first half already readable.

1. Finish the current Stage 3 proof: fresh password-controlled `while` transfer,
   divisible-by-7 counter, guessing-game mini-project, cold `break` retest, and
   explain-back.
2. Complete Stage 4 functions: parameters, arguments, return values, scope, and the
   standard-library bridge.
3. Run a mixed cold-read gate containing atoms, branching, loops, and functions.
4. Write one pseudocode/function-skeleton response before any implementation.
5. Confirm D2L, Gradescope, Respondus, webcam/microphone, and the actual Fall lab
   calendar when the course shells populate.

Stages 1–2 are already satisfied; Stage 3 remains active. This gate does not advance
mastery by documentation alone—evidence belongs in [[current-position]].

## Whole-Semester Pathway

The lecture dates below come from the Fall-aligned calendar, subject to the anomaly
warnings above. Lab entries preserve only the syllabus's topic order because its
printed dates are unusable. D2L/instructor truth supersedes this table.

| Lecture week | Official lecture focus / assessment signal | Lab-order companion | Vault route | Private code-reading and skeleton proof |
|---|---|---|---|---|
| 1 — Aug 24–30 | Module 0: syllabus, decomposition, algorithms, abstraction, computers/programs | Intro, IDE, Gradescope | Stage 0 + Stage 7 planning habit | Annotate one input→process→output program; turn a plain-English task into 5–8 steps without coding. |
| 2 — Aug 31–Sep 6 | Module 1: I/O, types, operators, arithmetic, Boolean expressions, assignment; Quiz 1 listed Sep 6 | I/O and variables, then types/operators/expressions | Stage 1 retrieval plus the Boolean-expression subset of [[stages/stage-02-decisions-and-boolean-logic]] | Trace types and values line by line; explain every conversion; write an I/O skeleton from a fresh prompt. |
| 3 — Sep 7–13 | Selection / branching | Selection | Stage 2 retrieval | Build a truth/branch table; predict exactly one executed path; mark independent vs. mutually exclusive tests. |
| 4 — Sep 14–20 | Selection continues; Quiz 2 listed Sep 20 | Selection practice | Stage 2 consolidation | Cold-read nested and chained decisions; rewrite only the pseudocode structure; debug one unreachable/wrong branch. |
| 5 — Sep 21–27 | Repetition / loops | Repetition I | Stage 3 | Mark initialization, condition/sequence, update, and exit; trace counters and accumulators. |
| 6 — Sep 28–Oct 4 | Repetition continues; Quiz 3 listed Oct 4 | Repetition II | Stage 3 mastery/retrieval | Cold-write loop skeletons; diagnose off-by-one and infinite-loop defects; explain `break` vs. `continue`. |
| 7 — Oct 5–11 | Test 1 over Modules 1–2; functions begin | Functions | Stage 4 | Closed-resource retrieval for atoms/decisions/loops; then trace call, parameter binding, local state, and return. |
| 8 — Oct 12–18 | Functions continue; Quiz 4 listed Oct 18 | Functions / lab midterm vicinity by order | Stage 4 | Derive three function signatures from prose; separate calculation from I/O; build a multi-function skeleton. |
| 9 — Oct 19–25 | Python libraries; Quiz 5 listed Oct 25 | Python libraries | Stage 4 library bridge | Read import→module→function calls; extract a function contract from documentation; wrap it behind one named function. |
| 10 — Oct 26–Nov 1 | Tuples and lists | Tuples/lists | Stage 5 | Trace indices, slices, mutation, traversal, and aliasing; choose tuple vs. list and defend the choice. |
| 11 — Nov 2–8 | Dictionaries, searching, sorting; Quiz 6 listed Nov 8 | Dictionaries/search/sort | Stage 5 + Stage 8 course subset | Map keys/values; trace a search and a simple sort; state inputs, stopping rule, result, and edge cases. |
| 12 — Nov 9–15 | Test 2 over Modules 1–5; OOP begins | OOP I | Stage 8 course subset | Mixed closed-read review, then map class, instance, attributes, methods, and constructor flow. |
| 13 — Nov 16–22 | OOP continues; Quizzes 7–8 listed Nov 19 | OOP II | Stage 8 course subset | Trace object state across method calls; write a class skeleton with `__init__` and one behavior; explain `self`. |
| Fall break — Nov 23–29 | No classes | — | Retrieval only if capacity allows | One light mixed-code read; no speculative new module. |
| 14 — Nov 30–Dec 6 | Lecture topic TBD; Quiz 9 listed Dec 6 | Java introduction appears last in lab order | Evidence-selected repair + tiny Java bridge if confirmed | Repair the weakest measured Python reading skill; compare Python/Java concepts only after the instructor confirms the bridge. |
| 15 — Dec 7 | Review; Quiz 10 listed Dec 7 | Lab final vicinity in the recycled order | Mixed-course retrieval | Cold-read a mixed program, draw its code map, trace a critical path, write a skeleton, and explain two failure modes. |
| Final-exam period | Lecture final; lab final scheduled from live course data | Closed-book lab final | No new content | Retrieval, tracing, and independent construction under the exact permitted-resource rules. |

(source: both active syllabi, calendar tables; the pathway/proof column is this
wiki's learning design and uses the existing Stage 0–8 packets)

## Module Playbooks

### Module 0 — Decomposition, algorithms, and abstraction

- **Read:** purpose, input, output, and the sequence of steps.
- **Trace:** follow one concrete example through the steps.
- **Skeleton:** comments or pseudocode only; name the parts before syntax.
- **Proof:** Chris can explain which details are essential and which are hidden by
  the abstraction.

### Module 1 — Values, types, expressions, and I/O

- **Read:** label every value's type and every assignment's effect on state.
- **Trace:** calculate expression order and conversion before execution.
- **Skeleton:** input → conversion → processing → formatted output.
- **Proof:** identify a type mismatch and explain why `input()` begins as text.

### Module 2A — Selection

- **Read:** convert code into a branch table.
- **Trace:** evaluate conditions in order and mark which branch executes.
- **Skeleton:** conditions and branch names before branch bodies.
- **Proof:** choose `if`/`elif`/`else` vs. separate `if` statements and explain why.

### Module 2B — Repetition

- **Read:** identify repeated body, controlling state, update, and stop condition.
- **Trace:** use a table for iteration number and changed variables.
- **Skeleton:** initialization → loop header → body → update → post-loop result.
- **Proof:** diagnose off-by-one, unchanged-state, `break`, and accumulator errors.

### Module 3 — Functions

- **Read:** identify caller, arguments, parameter binding, local work, and return.
- **Trace:** keep caller state separate from function-local state.
- **Skeleton:** function name, parameters, doc/purpose comment, return placeholder,
  then the calling code.
- **Proof:** explain parameter vs. argument and `return` vs. `print()`.

### Module 4 — Python libraries

- **Read:** separate code Chris owns from imported capability.
- **Trace:** follow the imported function's documented input/output contract rather
  than pretending to know its internals.
- **Skeleton:** import, one wrapper function, validation, and call site.
- **Proof:** use one standard-library function and explain import vs. installation.

### Module 5 — Collections, searching, and sorting

- **Read:** identify data shape, indices/keys, mutation points, and traversal.
- **Trace:** record collection state after each meaningful operation.
- **Skeleton:** choose structure first, then operations, then loop/search behavior.
- **Proof:** defend list vs. tuple vs. dictionary and trace one search/sort by hand.

### Module 6 — Object-oriented programming

- **Read:** distinguish class blueprint, instance, attributes, methods, and state.
- **Trace:** follow constructor and method calls across one object's lifetime.
- **Skeleton:** class name → `__init__` → attributes → one behavior → test instance.
- **Proof:** explain `self`, instance state, and why a class is or is not justified.

### Module 7 — Java bridge, if the Fall course confirms it

- Map familiar concepts—variables, branches, loops, functions/methods, collections,
  and classes—before focusing on new punctuation or type declarations.
- Keep this bounded to the course's confirmed introduction. Do not start an
  independent Java path before Python OOP is secure.

## Assessment Operating Plan

- **Lecture quizzes:** use short retrieval, terminology, trace tables, and output
  prediction. The quiz average is a quarter of the working grade model.
- **Lecture Tests 1 and 2:** run one mixed closed-resource reading set before each
  test, then repair only errors shown by that evidence.
- **Lecture final:** cumulative code-map and trace practice; verify the actual
  permitted-resource and Respondus requirements before exam day.
- **Lab exercises/assignments:** Chris works independently. AI can teach the concept
  later with a different prompt, but cannot inspect or repair the submitted task.
- **Lab midterm/final:** practice cold because the syllabus says closed book, closed
  notes, and no outside resources. Skeleton writing and trace accuracy are the main
  preparation measures.
- **Feedback loop:** record the concept/error class, not protected question content.
  Use Gradescope's three-business-day regrade window when a grading issue exists.
- **Tutoring:** use the human tutoring center for course-authorized help and the
  final-exam extra-credit path; confirm visit-credit procedure before relying on it.

## Required vs. Enrichment

Explicit course scope includes types/expressions, selection, repetition,
collections, functions, Python libraries, searching/sorting, classes, exception
handling, IDE/debug/run/test habits, documentation, and basic security awareness.

Recursion, Big O, regex, `pytest`, automation, APIs, SQL, pandas, web applications,
and deeper Java are helpful enrichment, not syllabus mandates. Keep them at their
existing prerequisites unless the live course explicitly requires them.

## Update Triggers

Update this page when any of the following becomes available:

- D2L's real Fall lecture/lab schedules and deadlines.
- Confirmation of the lecture weighting table.
- Corrected Week 1 or Week 15 lecture dates.
- The real lab midterm/final dates or Fall lab calendar.
- Any instructor clarification of permitted resources or AI policy.
- Evidence that the code-reader ladder is too easy, too hard, or failing to transfer.

Do not copy actual learner progress here. Return proof to [[current-position]] and
append the session evidence to [[log]].
