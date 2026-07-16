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
- **Current study stage: Stage 3 — Loops.** `wiki/stages/stage-03-*.md`.
- **Stages 3-10 are generated but not yet mastered.** Their packets exist and are ready, but Chris has not worked through or demonstrated mastery of any of them yet. Do not treat their existence as progress.

**This page must never be read as "Chris should start at Stage 10."** Stages 0-2 are complete. His next action is to open Stage 3 and begin loops.

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

## Learning Design Requirements

- Glossary-first.
- Flashcard-ready.
- Sequential reading path.
- Small drills.
- Explain-back prompts.
- Physical-world anchors when useful.
- Park advanced topics.
- Teach computer-science thinking and Python mechanics together.

## Academic Integrity Notes

- **CSE 1321 and CSE 1321L are `ai-restricted`.** Both official Fall 2026 PDFs
  explicitly prohibit submitted content created or assisted by generative AI.
- AI may support private concept learning and ungraded practice. It must not draft,
  solve, rewrite, or debug submitted course work. Stop and ask whenever graded status
  is unclear. See [[syllabus-alignment]].

## School Alignment (official PDFs verified 2026-07-15)

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

Stage 2 is closed. Chris's next action is to **open Stage 3 (Loops)**:
`wiki/stages/stage-03-*.md`. All later packets remain content readiness, not
study progress until worked and verified the same way Stage 2 was.
