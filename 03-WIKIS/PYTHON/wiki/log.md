---
type: log
tags: [programming]
timeline: log
---

# Education Wiki Log

Append every meaningful ingest, path update, teaching session, or structure change here.

## 2026-08-01 (later) — Friday's un-run Test Day quiz taken: 2 PASS / 1 partial / 3 MISS, two regressions surfaced

### Work completed
- Friday, July 31's weekly-plan "Test Day" timed quiz never ran (session
  that day was consumed by a git-casing reconciliation). Chris asked what
  was most important to get done before Sunday's review; this quiz was
  identified as the single highest-leverage missing item and run today,
  off-plan, after the retest-item cold check above.
- No pre-built quiz file exists for Stage 4 in the vault — built fresh
  against the stage's own Mastery Checklist: parameter/argument
  definitions, a predict-the-output trace (including a deliberate
  out-of-scope variable), a cold function write, a print-vs-return
  judgment call, a find-and-fix debug item, and a fruitful/void
  classification with reasoning. Closed-book, one attempt, 15-minute
  timer, scored honestly before any correction, per the weekly plan's own
  rule ("record the score honestly before reviewing anything").
- **Score: 2 clean PASS (cold function write; find-and-fix debug item), 1
  PARTIAL (fruitful/void — correct fruitful example, but the void example
  was an unfinished idea, not real code, so the actual "how do you tell
  from the def line" question went unanswered), 3 MISS.**
- **Real finding — two of the three misses are regressions**, not fresh
  gaps: (1) parameter/argument reversed (parameter described as "fed into"
  the argument) — this exact distinction passed independently 2026-07-27;
  (2) predicted `print(total)` would output `7` instead of raising
  `NameError` on a variable local to the called function — this is the
  identical scope concept from the `error4.py` debug rep that passed
  independently 2026-07-29. The third miss (Q4, print-vs-return) was a
  genuine fresh misjudgment: framed the choice as being about data type
  (strings) rather than about whether the caller needs to reuse the
  result.
- **Chris self-reported after scoring:** his original written answers for
  #1 and #2 were correct, and he changed them before submitting. This
  reclassifies those two misses as **answer-flipping under timed
  pressure, not a conceptual gap** — but the submitted score stands
  unchanged, same as a real quiz; you don't get to un-submit because you
  had the right answer first.
- **Immediate retest, one question each, first instinct:** parameter/
  argument corrected fast and clean — held at concept-cue support level
  (just restating the question sharply was enough). Scope/local-variable-
  lifetime did not land on the first restated question (still described a
  conditional "yes, if it specifically returns total" — conflating the
  returned *value* with the *name* surviving outside the function);
  required a full worked-step explanation (the "torn-down local
  workspace, only the value survives via return" framing) before a clean,
  unprompted "no" landed on a fresh check. **Treat scope/local-variable-
  lifetime as not yet secure** — worth a genuine unprompted cold recheck
  next time it comes up, not assumed fixed by one correct answer given
  immediately after its own explanation.

### Pages created/updated
`current-position.md` (quiz result and both retest diagnoses recorded).
This log.

### Vocabulary added
None new — all six items were retrieval/application of already-taught
Stage 4 vocabulary, not new introduction.

### Progress evidence
Stage 4 remains procedurally CLOSED (all four original gate items were
independently verified cold, without timed pressure). This quiz is not a
reopening of that closure — it's new evidence that two of its concepts
need a genuine spaced recheck before they're trusted as durable, which
the original untimed cold-attempt format didn't surface.

### Next action
Add parameter/argument and scope/local-variable-lifetime as explicit
spaced-retrieval items for a future cold check — genuinely unprompted,
not immediately after a fresh explanation. Stage 4b (Python libraries)
remains the frontier for new content.

## 2026-08-01 — Off-plan Saturday cold check: both Stage 4 retest items closed

### Work completed
- Weekly plan marked today (Saturday, Aug 2 week) as no-school family time;
  Chris redirected into a cold Python check anyway — displacement recorded,
  no resistance given per standing rule.
- Targeted the two items flagged "recheck cold next time it comes up" from
  the 2026-07-29 Function Toolbox session: (1) `return` sends a value back
  to the caller (vs. an earlier "holds the argument" miscue), and (2) a
  `percent_of`-style return value is an amount, never the rate — the rate
  is always the input.
- Fresh cold task, not seen before: write `discount_amount(price, rate)`
  returning the dollar amount taken off (e.g. `discount_amount(80, 0.25)`
  → `20.0`), reusing his existing `percent_of.py`.
- **Real first-attempt miss, self-corrected:** first version
  (`code/discount_amount.py`) computed `price - percent_of(price, rate)` —
  the discounted *total* (60), not the discount *amount* (20) the spec's
  own worked example named. Chris's predict-and-trace was accurate (he
  correctly walked through and got 60, and correctly explained the
  difference between "amount" and "total") but he'd built the wrong one.
  Explanation: he assumed the exercise wanted something different from
  `percent_of` rather than checking the given example first. One pointer
  back at the example ("the example is the source of truth") — fixed on
  the next attempt, first try: `da = percent_of(price, rate); return da`.
- **Unprompted improvement:** flagged (not required as a fix) that his
  first correct version's local variable was named `discount_amount`,
  shadowing the function itself. Chris renamed it to `da` anyway because
  he preferred it cleaner — not asked for, done on his own judgment.
- **Return-value framing — PASS.** Closed-book explanation, unprompted and
  more complete than the question asked: `return` sends the value back to
  the caller *and* exits the function (nothing below it runs); the call
  expression itself takes on that value, which is what `print()` receives.
- **Rate-vs-amount — PASS, clean transfer.** No recurrence of the earlier
  "return value is the percentage" mislabel anywhere in this rep, across
  both files.
- **Verdict: both flagged retest items CLOSED.** Stage 4 remains closed;
  frontier is still Stage 4b (Python libraries), untouched.

### Pages created/updated
`current-position.md` (retest items marked closed under the Stage 4 CLOSED
note). This log.

### Vocabulary added
None new — return-value mechanics and rate/amount were reinforced via
transfer, not first introduction.

### Next action
Stage 4b (Python libraries) — nothing read yet. Resume there on the next
scheduled Python block.

## 2026-07-29 (evening) — Stage 4 gate closed: common-error debug rep, PASS

### Work completed
- After an earlier invalid attempt (editing the reference page's examples
  instead of writing real code — reverted, recorded as not verified), Chris
  wrote a real script cold: `code/error4.py`, reproducing the NameError
  out-of-scope pattern (`def square(n): return n*n` then a bare `print(n)`
  at module level) and fixing it by calling `print(square(5))` instead.
  Ran clean: `25`.
- **Explain-back, unprompted, correct and more precise than asked:** Chris
  identified that `n` unquoted is a name Python tries to look up in the
  current (module) scope, fails because `n` was never bound there (only
  inside `square`'s local scope during its call), producing `NameError`.
  He then added, unprompted, the identifier-vs-string-literal distinction:
  `print("n")` would just print the literal character with no name lookup
  at all, completely unrelated to `square`'s parameter.
- **Verdict: PASS — independently verified.** Real code, real error, real
  fix, real explanation. This closes Stage 4's last open item.

### Stage 4 — CLOSED (2026-07-29)
All gate items now independently verified: cold baseline, three-function
drill, Function Toolbox mini-project, and the common-error debug rep.
Stage 4b (Python libraries) is next.

### Pages created/updated
`current-position.md` (Stage 4 closed, frontier moved to Stage 4b). This log.

### Vocabulary added
None new — scope and name resolution were reinforced via transfer, not
first introduction.

## 2026-07-29 — Function Toolbox mini-project: PASS WITH CORRECTION

### Work completed
- Chris built the Stage 4 Function Toolbox mini-project cold, in phases, with no
  code written or debugged by AI: `percent_of(t, p)` and `add_tax(a, b)`
  (Phase 1, independent fruitful functions); then unprompted refactored
  `add_tax` to call `percent_of(a, b)` internally instead of repeating the
  multiplication (Phase 2 — one function using another's return value); then
  `bill_calculator(x, y, z)` in `third.py` (Phase 2 continued — calls
  `add_tax`, computes tip on the subtotal, returns a formatted receipt string
  using `:.2f` currency formatting), driven by `bill_calculator.py`'s
  interactive input/print (Phase 3). Files:
  `code\{percent_of,add_tax,third,bill_calculator}.py`.
- Real first-attempt bug caught via predict-before-run: an early driver
  (`together.py`) took the tax rate as user input without specifying units;
  Chris predicted the trace correctly (100, 10 → 1100) but the real-world
  answer was wrong (10 was meant as 10%, not 1000%). Chris diagnosed the root
  cause himself (function expects a decimal, user naturally types a
  percentage) and fixed it by rewording the prompt to demand a decimal value,
  rather than silently converting — a deliberate, explained design choice.
- Self-corrected a naming issue mid-build: an intermediate variable computing
  `v - x` was first named `tax_rate` though it holds a dollar amount; renamed
  to `tax_amount` after one correction.
- **Explain-back (execution order, the mini-project's actual gate item):**
  Chris correctly traced the full call/return chain unprompted — driver calls
  `bill_calculator`, which calls `add_tax`, which calls `percent_of`
  (deepest/last call), and each return unwinds back up in reverse order to the
  driver's `print()`. This is the real target concept and it landed cleanly.
- **One recurring correction, given twice now:** Chris's verbal explain-back
  called `percent_of`'s return value "the tax percentage" — it's a tax
  *amount* (a dollar value); the percentage/rate is the input, never the
  output. Same confusion as the `tax_rate` naming slip earlier in the same
  session — flagged clearly both times; worth a cold re-check next time
  "percent of" or a rate-vs-amount calculation appears.
- **Verdict: PASS WITH CORRECTION.** All acceptance-checklist items met: 3
  functions (each with parameters), 3 of 3 use `return`, `add_tax`→`percent_of`
  and `bill_calculator`→`add_tax` both satisfy "one function uses another's
  return value," a driver section calls the chain and prints an f-string
  receipt, and the execution-order explain-back passed. Stage 4 gate's
  remaining item: one common-error debug rep (untouched today).

### Pages created/updated
`current-position.md` (mini-project result recorded, next action updated). This log.

### Vocabulary added
None new — amount-vs-rate was corrected via transfer, not first introduction.

## 2026-07-27 — Stage 4 cold functions baseline: PASS WITH CORRECTION

### Work completed
- Monday's week-opening proof gate. Chris wrote and ran two functions cold,
  before any Stage 4 reading:
  `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\function.py`
  (`add_this(a, b)`) and `code\greet.py` (`greet(name)`). Both ran correctly.
- First explain-back (in-code comments) conflated parameter and argument and
  described `def` as a "label generator." Escalated one physical anchor (mail
  slot: the `def` line labels an empty slot — parameter; the call drops a real
  value into it — argument) rather than a full lecture.
- Fresh transfer: asked Chris to write a new function (`greet`) and identify
  the parameter/argument pair without copying the prior example. He correctly
  named `name` (in `def greet(name):`) as the parameter and `"Chris"` (in
  `greet("Chris")`) as the argument, in both directions, unprompted.
- One residual miscue not yet re-tested: his comment described `return` as
  "letting the function know where to hold the argument" — corrected that
  `return` sends the computed value back out to the caller. Also corrected
  "script" → string literal, and confirmed his near-miss "cannotation" was
  reaching for concatenation.
- **Verdict: PASS WITH CORRECTION.** Parameter/argument — the actual target of
  this baseline — is solid on a fresh example. Stage 4 baseline closed; Chris
  moves to the Stage 4 reading next.

### Pages created/updated
`current-position.md` (baseline result recorded, next action updated). This log.

### Vocabulary added
None new — parameter/argument/return were taught via correction and transfer,
not first introduction.

### Drills or projects added
None — Chris's own cold `function.py`/`greet.py` serve as this rep's evidence.

### Progress evidence
Cold baseline passed with one correction, matching the Stage 3 gate pattern.
Return-value framing is the one item worth a light re-check next session.

### Parked material
None new.

### Next action
Stage 4 reading — *Think Python* pp. 43-52 — then the function-writing drill
and Function Toolbox mini-project per `weekly-plan-2026-07-27-to-2026-08-02.md`'s
10:00 Monday slot.

## 2026-07-16 — Stage 2 verification gate CLOSED

Both open Stage 2 gates closed in this session:
1. **Cold explain-back (`Story.py`)** — Chris explained `elif` correctly
   (chains off the same `if` gate so only one branch fires; contrasted
   correctly against stacked independent `if` statements) and `or`
   correctly after one round of tightening (spikes/snakes are two valid
   inputs mapped to one shared outcome, not an "and/or" blend).
2. **Independent code fix (`S2P3.py`)** — Chris removed the stray `D` band
   (60-69) and changed `"fail"` to `"F"` so the `else` now catches
   everything below 70 as `F`, matching the drill spec. Verified correct.

Stage 2 mastery checklist is satisfied. Chris is clear to advance to
Stage 3 (Loops) next session.

Files changed: `02-LIBRARY\00-SCHOOL\01-CSE-Python\Stages\Stage-02-python_wiki\S2P3.py` (Chris's own edit, not AI-written); this log; `current-position.md`.

Next: open Stage 3 (`wiki/stages/stage-03-*.md`) and begin loops.

## 2026-07-13 — Two misplaced books rerouted in from TECHNOLOGY raw/

`python-crash-course.pdf` and `PythonforProgramers.pdf` were sitting in
`03-WIKIS\TECHNOLOGY\raw\` (routed there from `77-INBOX` in error) — moved
to `raw\books\` here per this wiki's own System Boundary (Python
fundamentals belong here, not TECHNOLOGY). **Raw source only — not
ingested into the curriculum this session.** Chris is mid-Stage 2 (the
`choose-your-path-adventure` mini-project, per today's DAILY); per this
wiki's own Page Creation Rule, no concept pages get built ahead of the
current stage. `python-crash-course.pdf` specifically fulfills a
`[[python-crash-course]]` dead wikilink TECHNOLOGY's 2026-07-09 citation
audit already flagged as a future PYTHON-wiki target — noted here for
whenever Chris's stage reaches material this book would actually serve.

Files changed: `raw\books\python-crash-course.pdf`, `raw\books\PythonforProgramers.pdf` (new); this log.

Next: no action required now — available for a future stage's source map.

## 2026-06-24 — Initial structure created

### Work completed
- Created Education Wiki OS structure for Python-first learning.
- Separated this vault from `03-WIKIS\FORGE` business wiki.
- Established academic integrity boundary.
- Created staged Python path from setup through application thinking.

### Pages created/updated
- `CLAUDE.md`
- `README.md`
- `wiki/index.md`
- `wiki/current-position.md`
- `wiki/learning-path.md`
- `wiki/source-map.md`
- `wiki/prerequisite-map.md`
- `wiki/parking-lot.md`
- stage pages and templates

### Vocabulary added
- pending source ingest

### Drills or projects added
- pending stage generation

### Progress evidence
- Chris can create and run `.py` files, use `print()`, understand strings, and recognize core beginner constructs.

### Parked material
- advanced automation, application architecture, production deployment, `03-WIKIS\FORGE` business applications

### Next action
- Ingest syllabi first, then perform multi-book source mapping before deep extraction.

## 2026-06-24 — Syllabus ingest and school-policy alignment

### Work completed
- Read both `raw/syllabi/CSE_lecture_syllabus.md` and `raw/syllabi/CSE_lab_syllabus.md` (schedule-only files; no AI policy, textbook, or grading breakdown present in either).
- Confirmed with Chris: AI assistance is allowed for this course (not `ai-restricted`); standing rule to stop and ask before graded work still applies.
- Confirmed with Chris: course textbook not yet added to `raw/books/`, will be added later.
- Extracted and cross-compared lecture vs. lab topic order; confirmed both align with vault Stages 1-8 sequencing, with one flagged gap (Python Libraries appears before lists/dicts in the syllabus order, but vault will keep teaching data shapes first).
- Confirmed Java appears only in lab Week 13 — parked as out of scope for this Python-track vault.

### Pages created/updated
- `wiki/source-map.md` — syllabus rows marked ingested, extraction notes added, spine marked "none yet."
- `wiki/current-position.md` — academic integrity notes corrected, school alignment summary added, next action updated.
- `wiki/learning-path.md` — current-position block and "Next Required Claude Operation" updated to reflect syllabi-complete / book-pending state.

### Vocabulary added
- none yet (syllabi were policy/schedule extraction only, no new teaching terms)

### Drills or projects added
- none yet — blocked on spine source selection

### Progress evidence
- Source-map and learning-path now accurately reflect: syllabi fully ingested, course is AI-permissive, textbook pending.

### Parked material
- Java (lab Week 13 only) — out of scope for this Python-track vault unless Chris asks to bridge it later.

### Next action
- Wait for Chris to add a Python book (course textbook or otherwise) to `raw/books/`, then run the Multi-Book Evaluation Matrix and select a spine to begin Stage 1.

## 2026-06-24 — Spine selected: Think Python, 2nd Ed.

### Work completed
- Chris added `raw/books/thinkpython.pdf` (Think Python, 2nd Ed., Allen Downey) as the course textbook.
- Read front matter and full table of contents (TOC-level ingest, not deep chapter read yet).
- Scored it in the Multi-Book Evaluation Matrix and selected it as the active spine for Stages 1-8.
- Built a Stage-to-chapter mapping, since the book's own chapter order doesn't match the vault's Stage order (book teaches function calls before conditionals/loops, and bundles recursion with conditionals). Kept vault Stage order per `CLAUDE.md` and will pull sections non-sequentially.
- Flagged that the book has no automation or application/CLI/web/API content — Stages 9-10 will need a separate source later.

### Pages created/updated
- `wiki/source-map.md` — added Think Python row, evaluation matrix scores, Stage-mapping table, spine selection block.
- `wiki/current-position.md` — added Spine Source section, updated next action.
- `wiki/learning-path.md` — current-position block now points at Stage 1 (atoms), next reading set to Think Python Ch.1-2 + the input() section pulled forward from Ch.5, next required operation updated to begin Stage 1 generation.

### Vocabulary added
- none yet — Stage 1 glossary/flashcard generation not yet started, pending Chris's go-ahead

### Drills or projects added
- none yet

### Progress evidence
- Spine source locked in; Stage 1 reading assignment is now concrete and citable.

### Parked material
- Recursion (Ch.5) and OOP (Ch.15-18) held for Stage 8, per existing prerequisite map.
- Automation/application content — no source yet, flagged for later.

### Next action
- Confirm with Chris to begin Stage 1 (Python atoms) page generation: concept page, glossary entries, flashcards, code patterns, and at least one drill.

## 2026-06-24 — Official Python docs added (raw/docs/)

### Work completed
- Chris added the full CPython documentation source tree to `raw/docs/` (tutorial, library reference, howto guides, language reference, c-api, whatsnew changelogs, top-level meta pages).
- Inventoried at the subtree level (not file-by-file — far too large to deep-ingest). Classified each subtree's role per `wiki/source-map.md` rules.
- Determined this does not change the active spine or current stage: Think Python remains spine for Stages 1-8. `raw/docs/tutorial/` is a candidate support source; `raw/docs/library/csv.txt`, `datetime.txt`, and `raw/docs/howto/argparse.txt` are candidate support sources for Stages 9-10 once those stages start. Everything else (c-api, whatsnew, formal language reference, packaging) parked as advanced/out-of-scope/reference-only.

### Pages created/updated
- `wiki/source-map.md` — added "Official Python Documentation (raw/docs/)" section with subtree-level role table.

### Vocabulary added
- none

### Drills or projects added
- none

### Progress evidence
- Large doc dump classified without polluting the active beginner path or triggering unnecessary deep ingestion.

### Parked material
- `raw/docs/c-api/` — out of scope indefinitely for this track.
- `raw/docs/whatsnew/`, `raw/docs/reference/`, `raw/docs/howto/` (most), `raw/docs/library/` (most), `raw/docs/installing/`, `raw/docs/distributing/` — reference/advanced, revisit only as specific needs arise.

### Next action
- Same as before: confirm with Chris to begin Stage 1 (Python atoms) page generation from the Think Python spine.

## 2026-06-24 — Automate the Boring Stuff added, fills Stage 9-10 gap

### Work completed
- Chris provided Automate the Boring Stuff, 3rd Ed. (Al Sweigart), pre-split into chapter `.md` files, dropped loose in `raw/`.
- With Chris's approval, moved all 25 chapter/appendix files into `raw/books/automate-the-boring-stuff/` to keep `raw/` organized per folder structure rules.
- TOC-level ingest: built a full chapter-to-stage mapping. This book resolves the Stage 9 (automation bridge) and Stage 10 (application thinking) source gap flagged earlier today, since Think Python doesn't cover that material.
- Chapters 1-9 also flagged as support/practice for Stages 1-6 (parallel coverage of basics from a different angle, plus an answer key in Appendix B for self-checking).
- Found a content gap: Chapter 10 is missing from the provided files (jumps from Ch.9 Regex to Ch.11 Organizing Files). Not guessing at its content — flagged for Chris.
- Parked niche/specialized chapters (web scraping, image manipulation, OCR, keyboard/mouse automation, text-to-speech) per the Parking Lot Rule.

### Pages created/updated
- `wiki/source-map.md` — added full Automate the Boring Stuff section with chapter-to-stage mapping table.
- `wiki/parking-lot.md` — added rows for web scraping, image manipulation, OCR, keyboard/mouse automation, text-to-speech.
- `wiki/current-position.md` — added second spine source for Stages 9-10, noted the Chapter 10 gap.
- `wiki/learning-path.md` — parked-material list expanded, gap-resolved note added.

### Vocabulary added
- none yet — these chapters aren't due for glossary/flashcard generation until Stages 5-6 (practice) or Stage 9 (primary)

### Drills or projects added
- none yet

### Progress evidence
- Both previously-identified source gaps (Stage 9-10 automation/application content) are now resolved with a concrete spine.

### Parked material
- Web scraping, image manipulation/graphs, OCR, keyboard/mouse automation, text-to-speech — added to `wiki/parking-lot.md` as niche/optional, revisit at Stage 10 or only if Chris asks.

### Next action
- Ask Chris if he has Automate the Boring Stuff Chapter 10 to fill the gap.
- Still pending: confirm with Chris to begin Stage 1 (Python atoms) page generation from the Think Python spine.

## 2026-06-24 — Python Crash Course added as support/practice source

### Work completed
- Chris added Python Crash Course, 3rd Ed. (Eric Matthes) to `raw/books/PythonCrashCourse.pdf`.
- TOC-level ingest: Part I (Ch.1-11, basics through testing) fully read; Part II read through Ch.15 (Pygame game project, data visualization). Later Part II chapters not yet checked — likely a web-app project, unconfirmed.
- Assigned role: support/practice for Stages 1-7, layered alongside the Think Python spine (not replacing it — Think Python remains the assigned course textbook). PCC's dense numbered exercises are a strong match for Chris's explain-example-drill learning profile.
- Identified PCC Ch.11 (Testing Your Code, `pytest`) as the first source covering automated testing, filling the existing "testing" row in `wiki/prerequisite-map.md`.
- Parked Part II project chapters (Pygame game Ch.12-14, data visualization Ch.15, possible web-app chapters) for Stage 10.

### Pages created/updated
- `wiki/source-map.md` — added full Python Crash Course section with chapter-to-stage mapping.
- `wiki/current-position.md` — added third source note under Spine Source section.

### Vocabulary added
- none yet

### Drills or projects added
- none yet — PCC's existing exercises will be pointed to once each stage's pages are generated

### Progress evidence
- Stages 1-7 now have two teaching sources (Think Python spine + PCC support) instead of one, improving drill availability.

### Parked material
- PCC Part II: Alien Invasion (Pygame) game project, data visualization (Matplotlib/Plotly), possible web-app chapters — held for Stage 10.

### Next action
- Same as before: ask Chris about Automate the Boring Stuff Chapter 10, and confirm go-ahead to begin Stage 1 (Python atoms) page generation.

## 2026-06-24 — ATBS Chapter 10 added; two more books added (Grokking Algorithms, Think Like a Programmer)

### Work completed
- Chris added Automate the Boring Stuff Chapter 10 ("Reading and Writing Files") — resolves the gap flagged earlier today. Slots between Ch.9 (Regex) and Ch.11 (Organizing Files) as expected.
- Chris added two new books to `raw/books/`: Grokking Algorithms, 2nd Ed. (Aditya Bhargava) and Think Like a Programmer (V. Anton Spraul).
- Grokking Algorithms: TOC-level ingest. Visual, Python-based, beginner-friendly. Assigned as support/practice for Stage 8 — Ch.1-5 (intro, selection sort, recursion, quicksort, hash tables) match the syllabus's Week 11 "searching and sorting algorithms" topic directly. Ch.6-13 (BFS, trees, Dijkstra, greedy, dynamic programming, k-nearest neighbors) parked as beyond syllabus scope.
- Think Like a Programmer: intro-level ingest. **Flagged a language mismatch** — the book's stated prerequisite is C++ fluency and all code examples are in C++, not Python. Assigned as a strategy/discussion-only support source for Stage 7 (decomposition, problem-solving approach) — Chris should read the reasoning, not copy the code. Not a spine, not a code source yet.

### Pages created/updated
- `wiki/source-map.md` — ATBS Ch.10 gap marked resolved; added full sections for Grokking Algorithms and Think Like a Programmer with chapter-to-stage mapping and the C++ mismatch caveat.
- `wiki/current-position.md` — added both new sources under Spine Source section.
- `wiki/parking-lot.md` — added rows for Grokking Algorithms Ch.6-13 and for Think Like a Programmer's C++ code examples.

### Vocabulary added
- none yet

### Drills or projects added
- none yet

### Progress evidence
- All flagged source gaps from earlier sessions are now resolved or consciously parked with clear reasoning.

### Parked material
- Grokking Algorithms Ch.6-13 — beyond syllabus scope, optional enrichment.
- Think Like a Programmer code examples — C++, not usable directly; strategy narrative only, and only once Chris has enough Python fluency to re-derive the logic.

### Next action
- Confirm with Chris to begin Stage 1 (Python atoms) page generation — five sources are now mapped and waiting (Think Python spine; Automate the Boring Stuff, Python Crash Course, Grokking Algorithms, Think Like a Programmer as support across various stages). No more open source gaps.

## 2026-06-24 — Three more books added; intake checkpoint reached

### Work completed
- Chris added three more books to `raw/books/`: A Common-Sense Guide to Data Structures and Algorithms, 2nd Ed. (Jay Wengrow), Invent Your Own Computer Games with Python, 4th Ed. (Al Sweigart), and Python Workout, 2nd Ed. (Reuven M. Lerner).
- Data Structures and Algorithms: TOC-level ingest. Assigned as Stage 8 support alongside Grokking Algorithms (more Big-O rigor, plus stacks/queues/linked lists/BSTs). Code language not yet confirmed — flagged to verify before treating as a Python source.
- Invent Your Own Computer Games with Python: brief-contents ingest. This is the strongest mini-project fit found yet — assigned as the primary mini-project source spanning Stages 2-8 (and Stage 10 for the graphics/sound chapters). Ch.7 ("Designing Hangman with Flowcharts") directly models Stage 7's decomposition/planning goal.
- Python Workout: brief-contents + exercise-list ingest. Pure drill book, 200 short exercises. Assigned as a drill bank across Stages 1, 4, 5, 6, 8, 9-10, directly serving the Drill Rule.
- **Reached an intake checkpoint**: six sources have now been added in a single session on top of the syllabi. Recommended to Chris that further book intake pause here and Stage 1 generation begin, per the vault's "don't become a pile of book summaries" directive.

### Pages created/updated
- `wiki/source-map.md` — added full sections for all three new books with stage mappings.
- `wiki/current-position.md` — added all three sources under Spine Source section, plus an explicit "Source Intake Checkpoint" note.

### Vocabulary added
- none yet

### Drills or projects added
- none yet — but Python Workout and Invent Your Own Computer Games now provide ready-made drill/project material once generation starts

### Progress evidence
- Every vault stage (0 through 10) now has at least one mapped source, several have multiple (spine + support + drills + mini-projects).

### Parked material
- Data Structures and Algorithms — chapters beyond sorting/recursion/hash-tables (deep dynamic programming, BSTs) parked as enrichment beyond syllabus scope.
- Invent Your Own Computer Games Ch.17-21 (graphics/sound/animation) parked for Stage 10.
- Python Workout Ch.8 (comprehensions) and Ch.11 (iterators/generators) parked as advanced.

### Next action
- Recommend pausing further source intake. Confirm with Chris to begin Stage 1 (Python atoms) page generation: concept page, glossary entries, flashcards, code patterns, and at least one drill (now with Python Workout Ch.2-3 as ready-made drill material).

## 2026-06-24 — First generation: full 11-stage path + Stage 1 packet

### Work completed
- Chris dropped `first_generation.md` in the vault root instructing intake to close and full-path generation to begin.
- Finalized the complete staged path (Stage 0 through Stage 10) in `wiki/learning-path.md`: each stage now has purpose, prerequisites, source assignments (spine/support/mini-project), required vocabulary, code patterns, drills, mini-project, common beginner mistakes, "do not move on until" criteria, and parked material.
- Updated `wiki/prerequisite-map.md` Advanced Unlocks table with vault-stage numbers, finalized against the full source roster.
- Updated `wiki/source-map.md` with a "Status: Intake Finalized" banner pointing to the new per-stage roster table in `learning-path.md`.
- Updated `wiki/current-position.md` — current stage is now Stage 1 (packet generated), source intake checkpoint marked closed.
- Consolidated `wiki/parking-lot.md` with remaining parked items found during the full-path pass (Data Structures & Algorithms advanced chapters, Python Workout advanced chapters, deep function/OOP topics).
- Updated `wiki/index.md` to point at the active stage.
- Generated the full Stage 1 packet:
  - `wiki/stages/stage-01-python-atoms.md` (hub page)
  - 5 concept pages: `values-and-expressions`, `variables-and-assignment`, `strings`, `numbers-and-type-conversion`, `print-and-input`
  - 12 glossary entries: value, expression, variable, assignment, string, concatenation, integer, float, type-conversion, comment, print, input
  - 1 flashcard batch (13 cards) covering all Stage 1 vocabulary plus 3 decision-rule cards
  - 1 code pattern: `input-and-type-conversion`
  - 1 drill: `stage-01-input-and-conversion`
  - 1 mini-project: `stage-01-about-me-program`
  - 1 common-errors page: `stage-01-common-errors` (TypeError, NameError, SyntaxError, ValueError previews)

### Pages created/updated
- Rewritten: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/stages/stage-01-python-atoms.md`.
- Updated: `wiki/prerequisite-map.md`, `wiki/source-map.md`, `wiki/parking-lot.md`, `wiki/index.md`.
- Created: 5 concept pages, 12 glossary entries, 1 flashcard batch, 1 code pattern, 1 drill, 1 mini-project, 1 errors page (22 new files total).

### Vocabulary added
- value, expression, variable, assignment, string, concatenation, integer, float, type conversion, comment, print(), input() — all with glossary entries and flashcards.

### Drills or projects added
- Drill: input-and-conversion practice (no loops/conditionals/functions, Stage 1 tools only).
- Mini-project: "About Me" program (4+ inputs, at least one type conversion, one calculation, f-string output).

### Progress evidence
- Stage 1 is now a complete, self-contained packet Chris can work through end-to-end without Claude needing to improvise content live.

### Parked material
- Everything beyond Stage 1 atoms: conditionals, loops, functions, data structures, files/errors, and all previously-parked advanced topics (see `wiki/parking-lot.md`, consolidated this session).

### Next action
- Chris works through Stage 1. When the mastery checklist in `wiki/stages/stage-01-python-atoms.md` is met (or Chris asks to continue regardless), generate the Stage 2 (Decisions) packet using the same structure.

## 2026-06-24 — Stage 2 (Decisions) packet generated

### Work completed
- Chris approved continuing to populate stages and asked for Stage 2 specifically.
- Generated the full Stage 2 packet following the same structure as Stage 1: hub page, concept pages, glossary entries, flashcards, code pattern, drill, mini-project, common-errors page.
- Updated `wiki/learning-path.md` (current position now Stage 2, Stage 2 section marked generated), `wiki/current-position.md` (current stage updated), `wiki/index.md` (active stage pointer updated).

### Pages created/updated
- Rewritten: `wiki/stages/stage-02-decisions-and-boolean-logic.md` (was a placeholder stub from initial structure creation).
- Created: 2 concept pages (`comparisons-and-boolean-logic`, `if-elif-else`), 7 glossary entries (condition, boolean, comparison-operator, boolean-operators, if-elif-else, branch, truthy-falsy), 1 flashcard batch (9 cards), 1 code pattern (`if-elif-else-decision-chain`), 1 drill (`stage-02-decision-rules`), 1 mini-project (`stage-02-choose-your-path-adventure`), 1 errors page (`stage-02-common-errors`) — 14 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- condition, boolean, comparison operator, boolean operators (and/or/not), if/elif/else, branch, truthy/falsy — all with glossary entries and flashcards.

### Drills or projects added
- Drill: plain-English rules translated into `if`/`elif`/`else` chains (3 scenarios).
- Mini-project: Choose-Your-Path Adventure (branching text story, inspired by Invent Your Own Computer Games' Dragon Realm, no loops/functions yet).

### Progress evidence
- Stage 2 is now a complete, self-contained packet, same depth and shape as Stage 1.

### Parked material
- Recursion (Think Python Ch.5's recursion sections) explicitly flagged as NOT part of Stage 2 reading, held for Stage 8.
- `is`/`is not`, walrus operator, match/case — noted as not needed yet, don't drill.

### Next action
- Chris works through Stage 2. When ready (mastery checklist met, or just asks), generate the Stage 3 (Repetition) packet next.

## 2026-06-24 — Stage 3 (Repetition) packet generated

### Work completed
- Chris approved continuing to the next stage.
- Generated the full Stage 3 packet following the same structure as Stages 1-2: hub page, 3 concept pages, 9 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project, 1 common-errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 3 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-03-loops-and-repetition.md` (was a placeholder stub).
- Created: 3 concept pages (`for-loops`, `while-loops`, `counters-and-accumulators`), 9 glossary entries (loop, iteration, for-loop, range, while-loop, counter, accumulator, break-continue, infinite-loop), 1 flashcard batch (9 cards), 2 code patterns (`for-loop-over-range`, `while-loop-until-condition`), 1 drill (`stage-03-loop-tracing`), 1 mini-project (`stage-03-guessing-game-with-attempts`), 1 errors page (`stage-03-common-errors`) — 18 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- loop, iteration/iterable, for loop, range(), while loop, counter, accumulator, break/continue, infinite loop — all with glossary entries and flashcards.

### Drills or projects added
- Drill: loop tracing (predict-then-check) plus three write-from-scratch loop tasks.
- Mini-project: number-guessing game with a limited number of attempts, combining `while`, a counter, and `if`/`elif`/`else`.

### Progress evidence
- Stage 3 is now a complete, self-contained packet, same depth and shape as Stages 1-2.

### Parked material
- Looping over lists/dictionaries directly, nested loops over complex data — held for Stage 5.
- Recursion as a loop alternative — held for Stage 8.
- List comprehensions — held for Stage 10.

### Next action
- Chris works through Stage 3. When ready (mastery checklist met, or just asks), generate the Stage 4 (Functions) packet next.

## 2026-06-24 — Stage 4 (Functions) packet generated

### Work completed
- Chris approved continuing to the next stage.
- Generated the full Stage 4 packet following the same structure as Stages 1-3: hub page, 3 concept pages, 8 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project, 1 common-errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 4 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-04-functions-parameters-return.md` (was a placeholder stub).
- Created: 3 concept pages (`defining-and-calling-functions`, `parameters-and-arguments`, `return-values`), 8 glossary entries (function, def, call, parameter, argument, scope, return-value, fruitful-void-function), 1 flashcard batch (9 cards), 2 code patterns (`function-with-parameter`, `function-with-return-value`), 1 drill (`stage-04-function-writing`), 1 mini-project (`stage-04-function-toolbox`), 1 errors page (`stage-04-common-errors`) — 17 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- function, def, call, parameter, argument, scope, return value, fruitful/void function — all with glossary entries and flashcards.

### Drills or projects added
- Drill: write 3 functions from a plain-English spec (temperature conversion, even/odd check, a void shout function).
- Mini-project: Function Toolbox — 3+ functions, including one that calls another and uses its return value.

### Progress evidence
- Stage 4 is now a complete, self-contained packet, same depth and shape as Stages 1-3.

### Parked material
- Default/keyword arguments, `*args`/`**kwargs` — Stage 8-10 as needed.
- Recursion — Stage 8.
- Storing functions in separate modules — Stage 9.
- Decorators — beyond vault scope for now.

### Next action
- Chris works through Stage 4. When ready (mastery checklist met, or just asks), generate the Stage 5 (Data Shapes) packet next.

## 2026-06-24 — Stage 5 (Data Shapes) packet generated

### Work completed
- Chris approved continuing to the next stage. This is the biggest stage so far (strings-as-sequences, lists, dictionaries, tuples, sets, plus a dedicated structure-choice decision page).
- Generated the full Stage 5 packet: hub page, 5 concept pages, 10 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project, 1 common-errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 5 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-05-data-shapes.md` (was a placeholder stub).
- Created: 5 concept pages (`strings-as-sequences`, `lists`, `dictionaries`, `tuples-and-sets`, `choosing-a-data-structure`), 10 glossary entries (index, slice, mutable-immutable, list, aliasing, dictionary, dictionary-key-value-pair, tuple, set, nested-structure), 1 flashcard batch (10 cards), 2 code patterns (`list-loop-and-index`, `dictionary-lookup`), 1 drill (`stage-05-data-structure-practice`), 1 mini-project (`stage-05-caesar-cipher`), 1 errors page (`stage-05-common-errors`) — 21 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- index, slice, mutable/immutable, list, aliasing, dictionary, key/value, tuple, set, nested structure — all with glossary entries and flashcards.

### Drills or projects added
- Drill: list indexing/slicing/mutation, dictionary lookup (safe and unsafe), and a structure-choice reasoning exercise (no code, just justification).
- Mini-project: Caesar Cipher (encode/decode functions using string indexing and modulo wraparound), inspired by Invent Your Own Computer Games Ch.14.

### Progress evidence
- Stage 5 directly drills the vault's core "tool selection" goal via the dedicated `choosing-a-data-structure` concept page and drill section.

### Parked material
- Full sets treatment (Think Python Ch.19), list comprehensions, `Counter`/`defaultdict`, deeper nested structures, and searching/sorting on these structures — held for Stages 8 and 10 per `wiki/parking-lot.md`.

### Next action
- Chris works through Stage 5. When ready (mastery checklist met, or just asks), generate the Stage 6 (Files, Errors, Debugging) packet next.

## 2026-06-24 — Stage 6 (Files, Errors, Debugging) packet generated

### Work completed
- Chris approved continuing to the next stage.
- Generated the full Stage 6 packet: hub page, 3 concept pages, 6 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project, 1 errors page (this stage's errors page leans more on process than a fixed list, since the stage itself teaches error-reading).
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 6 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-06-files-errors-debugging.md` (was a placeholder stub).
- Created: 3 concept pages (`file-paths-and-reading-writing`, `exceptions-and-tracebacks`, `debugging-process`), 6 glossary entries (file-path, open-read-write-close, exception, traceback, try-except, syntax-runtime-semantic-error), 1 flashcard batch (8 cards), 2 code patterns (`file-read-with-context-manager`, `try-except-block`), 1 drill (`stage-06-debugging-practice`), 1 mini-project (`stage-06-note-saver`), 1 errors page (`stage-06-common-errors`) — 15 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- file path (relative/absolute), open/read/write/close, exception, traceback, try/except, syntax/runtime/semantic error — all with glossary entries and flashcards.

### Drills or projects added
- Drill: predict-the-traceback exercises plus two write-from-scratch programs (try/except for division, file read/write with line counting).
- Mini-project: Note-Saver — append-mode file writing plus FileNotFoundError handling on read.

### Progress evidence
- Stage 6 gives Chris his first systematic debugging process (the three error-type framework) rather than ad-hoc troubleshooting.

### Parked material
- JSON/pickling, databases, custom exception classes, `finally` blocks, and the `logging` module — held for Stages 9-10 per `wiki/parking-lot.md` reasoning already in place.

### Next action
- Chris works through Stage 6. When ready (mastery checklist met, or just asks), generate the Stage 7 (Program Design) packet next.

## 2026-06-24 — Stage 7 (Program Design) packet generated

### Work completed
- Chris approved continuing to the next stage.
- Generated the full Stage 7 packet: hub page, 3 concept pages, 6 glossary entries, flashcards, 1 drill, 1 mini-project (intentionally open-ended — Chris picks the problem), 1 errors page (this one covers process mistakes rather than tracebacks, since Stage 7 doesn't introduce new syntax that throws new error types).
- No new code patterns this stage — flagged explicitly in the hub page, since Stage 7 is a process skill layered on top of every pattern already learned.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 7 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-07-program-design.md` (was a placeholder stub).
- Created: 3 concept pages (`decomposition-and-pseudocode`, `flowcharts`, `incremental-development-and-testing`), 6 glossary entries (decomposition, pseudocode, flowchart, algorithm, test-case, incremental-development), 1 flashcard batch (8 cards), 1 drill (`stage-07-decompose-a-problem`), 1 mini-project (`stage-07-plan-and-build`), 1 errors page (`stage-07-common-errors`) — 13 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- decomposition, pseudocode, flowchart, algorithm, test case, incremental development — all with glossary entries and flashcards.

### Drills or projects added
- Drill: decompose two problems into pseudocode/flowchart before coding, plus building one of them incrementally against pre-written test cases.
- Mini-project: Plan-and-Build — Chris picks his own small problem, plans it fully (pseudocode/flowchart + test cases) before writing any code, then builds incrementally.

### Progress evidence
- Stage 7 is the vault's first explicitly process-focused stage — concept pages and the errors page both teach a way of working, not new syntax.

### Parked material
- Formal software engineering methodology (Agile/Scrum), design patterns — not relevant at this scale.
- Formal unit testing frameworks (`pytest`) — held for Stage 10; Stage 7's "test case" is the informal by-hand precursor to that idea.

### Next action
- Chris works through Stage 7. When ready (mastery checklist met, or just asks), generate the Stage 8 (Algorithms and Data Structures) packet next.

## 2026-06-24 — Stage 8 (Algorithms and Data Structures) packet generated

### Work completed
- Chris approved continuing to the next stage — the biggest so far, covering recursion, basic OOP, and Big O/sorting/searching/hash tables.
- Generated the full Stage 8 packet: hub page, 4 concept pages, 11 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project (Card class + hand-written sort/search), 1 errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 8 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-08-think-python-readiness.md` (was a placeholder stub).
- Created: 4 concept pages (`recursion`, `classes-and-objects`, `big-o-and-algorithm-efficiency`, `sorting-and-searching`), 11 glossary entries (recursion, base-case, class, object-instance, attribute, method, big-o, sorting, searching, hash-table), 1 flashcard batch (9 cards), 2 code patterns (`recursive-function-with-base-case`, `class-with-init-and-method`), 1 drill (`stage-08-algorithms-and-classes-practice`), 1 mini-project (`stage-08-card-collection`), 1 errors page (`stage-08-common-errors`) — 21 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- recursion, base case, class, object/instance, attribute, method, Big O, sorting, searching, hash table — all with glossary entries and flashcards.

### Drills or projects added
- Drill: hand-tracing a recursive function, writing a `Book` class, and labeling three snippets by Big O.
- Mini-project: Card Collection — a `Card` class plus hand-written selection sort and linear search over a list of instances, with explicit Big O reflection.

### Progress evidence
- Stage 8 directly covers the CS-thinking content both syllabi name explicitly (OOP, searching/sorting algorithms), confirming the vault's path stays aligned with the course.

### Parked material
- Trees, Dijkstra's algorithm, greedy algorithms, dynamic programming, k-nearest neighbors — beyond syllabus scope, optional enrichment only.
- Inheritance/polymorphism depth (Think Python Ch.18), regex beyond a light intro, Think Like a Programmer's later chapters — all held per `wiki/parking-lot.md`.

### Next action
- Chris works through Stage 8. When ready (mastery checklist met, or just asks), generate the Stage 9 (Automation Bridge) packet next.

## 2026-06-24 — Stage 9 (Automation Bridge) packet generated

### Work completed
- Chris approved continuing to the next stage. This is the first stage built primarily from Automate the Boring Stuff rather than Think Python, since Think Python doesn't cover automation.
- Generated the full Stage 9 packet: hub page, 4 concept pages, 7 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project (File Organizer), 1 errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 9 as the active stage.

### Pages created/updated
- Rewritten: `wiki/stages/stage-09-automation-bridge.md` (was a placeholder stub).
- Created: 4 concept pages (`modules-and-packages`, `organizing-files-at-scale`, `csv-and-json`, `automation-script-design`), 7 glossary entries (module, package, pip, csv, json, automation-script, scheduling), 1 flashcard batch (9 cards), 2 code patterns (`organize-files-by-extension`, `read-csv-and-process`), 1 drill (`stage-09-automation-practice`), 1 mini-project (`stage-09-file-organizer`), 1 errors page (`stage-09-common-errors`) — 17 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- module, package, pip, CSV, JSON, automation script, scheduling — all with glossary entries and flashcards.

### Drills or projects added
- Drill: folder listing by extension, CSV averaging, JSON round-trip save/load.
- Mini-project: File Organizer — sorts a test folder's files into subfolders by extension, built incrementally per Stage 7's process, tested on throwaway data before being trusted.

### Progress evidence
- Stage 9 is the first stage explicitly testing "is this code doing something genuinely useful" rather than a teaching exercise — the mini-project is a real, reusable script.

### Parked material
- Excel/Google Sheets automation, PDF/Word automation, email/text/push-notification sending, real scheduling (cron/Task Scheduler) implementation, `03-WIKIS\FORGE` business tooling — all held per `wiki/parking-lot.md`, available as stretch material if Chris wants to go further.

### Next action
- Chris works through Stage 9. When ready (mastery checklist met, or just asks), generate the Stage 10 (Application Thinking) packet next — the final stage of the original 11-stage path.

## 2026-06-24 — Stage 10 (Application Thinking) packet generated — original 11-stage path complete

### Work completed
- Chris approved continuing to the final stage of the originally-planned path.
- Generated the full Stage 10 packet: hub page, 4 concept pages, 6 glossary entries, flashcards, 2 code patterns, 1 drill, 1 mini-project (a three-track capstone — CLI tool, Pygame game, or tested module, Chris's choice), 1 errors page.
- Updated `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md` to point at Stage 10 as the active/final stage, and explicitly marked the original 11-stage path (Stage 0 through Stage 10) as fully generated.
- Flagged for future sessions: do not generate further stages speculatively once Chris finishes Stage 10 — present options (deeper practice, a `03-WIKIS\FORGE` bridge, or new advanced material) and let Chris choose.

### Pages created/updated
- Rewritten: `wiki/stages/stage-10-application-thinking.md` (was a placeholder stub).
- Created: 4 concept pages (`cli-programs-and-argparse`, `automated-testing-with-pytest`, `databases-and-sqlite`, `apis-and-web-requests`), 6 glossary entries (cli, argument-parsing, unit-test, database, api, web-request), 1 flashcard batch (8 cards), 2 code patterns (`cli-with-argparse`, `pytest-test-function`), 1 drill (`stage-10-application-practice`), 1 mini-project (`stage-10-capstone-choice`), 1 errors page (`stage-10-common-errors`) — 16 new files total.
- Updated: `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/index.md`.

### Vocabulary added
- CLI, argument parsing, unit test, database, API, web request — all with glossary entries and flashcards.

### Drills or projects added
- Drill: a CLI greeting script, palindrome-checker tests, and a basic SQLite create/insert/query exercise.
- Mini-project: Stage 10 Capstone — Chris picks one of three tracks (CLI tool, small Pygame game, or a tested module), with the explicit requirement that some core logic be pulled out into a tested, decoupled function regardless of track.

### Progress evidence
- All 11 stages of the original path (Stage 0 through Stage 10) now have complete, generated packets. This is the largest single milestone in the vault's history so far.

### Parked material
- Flask/FastAPI, SQLAlchemy, Docker, CI/CD, cloud deployment, NumPy/pandas, full web scraping, OCR, keyboard/mouse automation, text-to-speech, `03-WIKIS\FORGE` business applications — all explicitly out of scope, consolidated in `wiki/parking-lot.md`.

### Next action
- Original path is complete. Wait for Chris to work through remaining stages, then ask what's next rather than assuming: more practice/repetition, a `03-WIKIS\FORGE` bridge, or new advanced material.

## 2026-07-07 — FORGE retirement: source inventory only, no curriculum changes

### Work completed
- FORGE's `wiki\technology\` (135 pages) was being split-migrated between this vault
  and `03-WIKIS\TECHNOLOGY` per Chris's decision. Before moving anything into this
  vault, checked it against this vault's own closed-intake rule (`wiki/source-map.md`:
  "do not add more sources without a specific reason") since much of FORGE's content
  overlapped books already fully built into Stages 0-10.
- Split the 66 Python-bound pages: 22 were near-duplicates of content already fully
  built into the Stage 1-8 curriculum (Think Python chapters, general Python-mechanics
  pages) — **archived, not migrated**, to
  `99-ARCHIVE\ARCHIVED_2026-07-07_FORGE_technology_python_duplicates\`. The remaining
  44 fill a real, previously-identified gap (NumPy/pandas/APIs — see
  `wiki/parking-lot.md`, parked since 2026-06-24 for exactly this reason) — migrated
  into `wiki/source-summaries/`.
- Copied the two backing PDFs (`PythonforDataAnalysis.pdf`, `PracticalSQL.pdf`) into
  `raw/books/` from FORGE's `raw/` (FORGE's own raw/ isn't archived yet, so this is a
  copy, not a move — avoids the new source-summary pages citing a source that isn't
  physically in this vault's `raw/`).
- Updated `wiki/source-map.md` with two new source entries (Python for Data Analysis,
  Practical SQL) plus a note resolving the "Ch.16+ unconfirmed" flag on the existing
  Python Crash Course entry (two of the 44 pages turned out to be Ch.15-17 of that
  book). Updated `wiki/parking-lot.md` to note sources now exist for the NumPy/
  pandas/APIs parks.
- **Did not** touch the active Stage 0-10 curriculum, generate any new concept/
  glossary/drill/flashcard pages, or change `current-position.md`/`learning-path.md`
  — this was source inventory only, confirmed with Chris before proceeding given the
  closed-intake rule.

### Pages created/updated
- Created: `wiki/source-summaries/` gained 44 new pages (see `source-map.md` for the
  full list, grouped by source book).
- Updated: `wiki/source-map.md`, `wiki/parking-lot.md`.
- Archived (not created in this vault): 22 pages moved to `99-ARCHIVE` — see above.

### Next action
- Flag to Chris at a future session: two new candidate Stage 9-10 source strands
  ("data analysis" via pandas/NumPy, "SQL fundamentals" via Practical SQL) are now
  inventoried and ready to build into the curriculum whenever he wants to extend past
  the original 11-stage path — see `source-map.md`'s "Required Next Update" section.
  Do not build them speculatively; wait for Chris to ask.

## 2026-07-08 — Pre-launch link audit and FORGE-migration repair

### Work completed
- Full vault link audit (all 245 wiki pages: wikilinks, markdown links, backtick
  path refs) ahead of tomorrow's go-live. All breakage traced to the 2026-07-07
  FORGE retirement migration; the native Stage 0-10 curriculum had zero dead links.
- Fixed 21 dead wikilinks, all in `wiki/source-summaries/` (the 44 FORGE-migrated
  pages), in three categories:
  1. Links to the 22 pages archived as curriculum duplicates (8 beginner-Python
     pages + the `python-crash-course` book hub) — repointed to this vault's
     equivalent stage pages or to `[[source-map]]`, with archive location noted.
  2. Links to FORGE business/systems pages that never migrated to any wiki
     (`systems-strategy-hard-soft-information`, `marketing-strategy-demographics-
     psychographics`, `management-strategy-as-marketing-tool`,
     `profit-first-instant-assessment`) — converted to plain-text mentions routing
     via `03-WIKIS\BUSINESS`. Verified none exist in BUSINESS/SYSTEMS/TECHNOLOGY.
  3. Remaining flagged `[[...]]` hits are pandas/NumPy code (`df[["col"]]`) inside
     code blocks — not real links, left alone.
- Fixed a sync contradiction in `wiki/source-map.md`: both new entries said the
  PDFs were "not yet physically in raw/" but `PythonforDataAnalysis.pdf` and
  `PracticalSQL.pdf` are in `raw/books/` (copied 2026-07-07 per the prior log
  entry). Notes corrected.
- Verified: templates/ intact, stage/concept/glossary cross-links all resolve,
  "formerly FORGE" routing notes in stage 9/10, prerequisite-map, and parking-lot
  are correct as written.

### Pages created/updated
- Updated (link repairs): `source-summaries/python-for-data-analysis.md`,
  `ipython-and-jupyter-basics.md`, `numpy-ndarray-basics-and-dtypes.md`,
  `numpy-indexing-and-slicing.md`,
  `numpy-statistical-methods-sorting-and-set-operations.md`,
  `pandas-series-dataframe-fundamentals.md`, `sqlite-and-sql-with-pandas.md`,
  `sql-basic-math-and-stats.md`, `data-visualization-python.md`,
  `working-with-apis-python.md` (10 pages).
- Updated: `wiki/source-map.md` (raw/ PDF location notes).

### Vocabulary added
- None (no teaching content touched).

### Drills or projects added
- None.

### Progress evidence
- Post-fix audit re-run: 0 dead wikilinks, 0 dead markdown links, 0 dead path
  refs (excluding code-block false positives and historical log text).

### Parked material
- The 44 FORGE-migrated source-summary pages still carry FORGE-era frontmatter
  (`domain: technology`, `priority/now` tags) and FORGE section shapes ("North
  Star Connection," "Ranking," "Use / Retrieval Notes") instead of this vault's
  `templates/source-summary-template.md`. Content is accurate and links now
  resolve; reshaping 44 pages is a style migration, not breakage — parked pending
  Chris's call.

### Next action
- Vault is link-clean for go-live; Chris's study next action is unchanged — open
  `wiki/stages/stage-01-python-atoms.md` and begin Stage 1.

## 2026-07-09 — FORGE source-summary reshape, pathway-fit verification, orphan audit

### Work completed
- Reshaped all 44 FORGE-migrated pages in `wiki/source-summaries/` to vault
  conventions, per Chris's go-ahead: vault frontmatter (`type: source-summary`,
  `status: parked`, `source_role`, `difficulty`, `source_file`, tags including
  `parked` so HOW_TO_USE's `tag:#parked` graph filter picks them up); FORGE-era
  trailer sections (North Star Connection, Ranking, Use / Retrieval Notes) replaced
  with a Pathway Placement section stating role, prerequisites (linked to vault
  stage pages), and parked status. Technical content untouched.
- The two book hubs (`python-for-data-analysis.md`, `practical-sql.md`) were
  hand-reshaped to the fuller `templates/source-summary-template.md` shape (Source
  Identity, Best Use In This Vault, Difficulty Assessment, Advanced Material To
  Park, Recommended Placement In Learning Path, Notes For Future Claude).
- **Pathway-fit verification — nothing from FORGE belongs in the mapped Stage 0-10
  path:** (1) the 22 true duplicates were already archived 2026-07-07; (2) all
  pandas/NumPy/SQL/Jupyter topics are beyond the syllabus and stage scope —
  extensions of Stage 9's csv-and-json and Stage 10's databases-and-sqlite, not
  duplicates; (3) the two Python Crash Course pages (Ch. 15-17) fall under the
  Source Roster's existing "PCC Part II" Stage 10 line — support detail for an
  already-mapped source, no roster change needed. No insertions into Stages 0-10.
- Rewrote `wiki/source-summaries/README.md` as a folder index routing to the two
  hubs and stating the inventory-not-curriculum rule.
- Orphan audit across all 245 wiki pages (inbound wikilinks, markdown links, and
  path mentions; strict pass excluding log.md): **zero orphan pages.** Stage
  packets, hubs, and indexes link everything.
- Post-reshape link audit: zero real dead links (remaining hits are pandas code
  like `arr[[4, 3]]` inside code blocks).
- Updated `wiki/index.md` (hub pointers) and `wiki/source-map.md` (reshape note).

### Pages created/updated
- Updated: all 44 pages in `wiki/source-summaries/` + that folder's README,
  `wiki/index.md`, `wiki/source-map.md`.

### Vocabulary added
- None (no teaching content touched).

### Drills or projects added
- None.

### Progress evidence
- Vault link-clean and orphan-free ahead of go-live; the FORGE inheritance is now
  fully normalized to vault conventions and verifiably outside the active path.

### Parked material
- Unchanged — the data-analysis and SQL-fundamentals strands stay parked pending
  Chris's go-ahead. Empty `wiki/tool-capability-library/` flagged to Chris as the
  one structural gap (see report / next action).

### Next action
- Chris reviews the flow report; the one real gap is that
  `wiki/tool-capability-library/` has no capability pages despite being one of the
  vault's two mandated pillars — build beginner-level pages there when Chris says
  go. Study next action unchanged: Stage 1.

## 2026-07-09 — Tool-capability library built; parked-advanced and glossary nav fixed; final sort check

### Work completed
- Built the tool-capability library: 8 beginner-level capability pages following
  `templates/tool-capability-template.md`, covering CLAUDE.md's example categories
  (automate decisions, clean text, validate data, organize files, spreadsheets/CSV,
  generate reports, call APIs, build small CLI tools). Each links its home stage,
  concepts, patterns, and existing mini-projects, and parks its advanced version to
  parking-lot / the parked strands. Folder README rewritten as a capability index
  with per-page earliest-stage column.
- Rewrote `wiki/parked-advanced/README.md` to state how parking works: parking-lot
  is the tracker (topics as rows), this folder holds drafted-ahead *pages* only,
  and it is currently empty by design — the FORGE pandas/NumPy/SQL material is
  source inventory in `source-summaries/`, not drafted curriculum, so it does not
  belong here.
- Generated `wiki/glossary/index.md` — alphabetical index of all 80 entries (the
  file the Session Start Protocol looks for first).
- Final unsorted-material sweep: no loose `.py` or stray files anywhere in the
  vault; `raw/` fully organized (books/docs/syllabi/examples); `raw/examples/`
  empty and ready for Chris's practice files; every wiki page classified and
  linked. **Verdict: nothing remains unsorted — the only "loose" Python material
  was the 44 source-summary pages, which are correctly placed as parked source
  inventory, not path content and not parked-advanced pages.**
- Updated `wiki/index.md` (glossary index + capability library pointers).
- Post-build audits: 0 dead links, 0 orphans across all 253 wiki pages.

### Pages created/updated
- Created: 8 capability pages in `wiki/tool-capability-library/` +
  `wiki/glossary/index.md` (9 new files).
- Updated: `wiki/tool-capability-library/README.md`,
  `wiki/parked-advanced/README.md`, `wiki/index.md`.

### Vocabulary added
- None — capability pages deliberately reuse only already-defined terms.

### Drills or projects added
- None new; capability pages route to existing drills/mini-projects
  (file organizer, capstone choice).

### Progress evidence
- The vault now satisfies both of CLAUDE.md's mandated pillars: `wiki/stages/`
  (the sequential path) and `wiki/tool-capability-library/` (what code can solve).

### Parked material
- Each capability page names its parked advanced version (watchdog, regex, openpyxl,
  pandas, PDF/Word output, scraping, GUIs/web apps, rules engines) — all pointing
  at existing parking-lot rows or parked strands; no new parking-lot rows needed.

### Next action
- Vault complete and go-live ready. Chris's study next action unchanged: open
  `wiki/stages/stage-01-python-atoms.md` and begin Stage 1.

## 2026-07-09 — CLAUDE.md dedup (system-wide, Chris-approved)

### Work completed
- This wiki's CLAUDE.md: duplicated shared blocks (academic integrity, raw rule,
  chunking) replaced by a pointer to `00-BRAIN\AI_Agent.md § Wiki Shared Layer`;
  the expanded session protocols stay and supersede the shared minimums. No
  learning content changed. Record: `00-BRAIN\Session_Logs\DAILY_2026-07-09.md`.

### Next action
- Resume the Python path — output reps begin July 10.

## 2026-07-09 — Citation/sort audit (Chris-directed, all-wikis sweep)

### Work completed
Seventh and final hub in the hub-by-hub citation-and-sorting sweep.
Structure verified clean against this vault's own rules: the root index's
command-center + stages + working-areas layout is intact; the 596-file
raw/ tree is fully covered by source-map.md's inventory (books mapped
per-source, the CPython docs tree classified by subtree per its 2026-06-24
entry — no untracked sources). The scan's "unlinked pages" are by design
(folder-level navigation via glossary/index and the tool-capability
README); its "dead wikilinks" were pandas `df[["col"]]` code snippets
misread as links, not real links.

One real finding, fixed: **source-map.md's "Chapter 10 missing" gap note
for Automate the Boring Stuff was stale** — Chris added Chapter 10
(Reading and Writing Files) to raw/ on July 9 at 10:28. Gap note updated
to closed; the book is now complete (Ch. 0–24 + appendices).

### Pages created/updated
`source-map.md` (gap note closed). This log.

### Vocabulary added
None (no teaching content this session).

### Drills or projects added
None.

### Progress evidence
n/a — system session, not a study session. Study stage remains Stage 1.

### Parked material
None new.

### Next action
Unchanged: Stage 1 (Python atoms) output rep per current-position.md —
the sweep found nothing blocking it.

## 2026-07-11 — CLAUDE.md slim pass (Chris-approved, flag 64)

### Work completed
- CLAUDE.md slimmed 565 → ~150 lines per the Claude-docs review
  (`00-BRAIN\Session_Logs\CLAUDE_DOCS_SYSTEM_REVIEW_2026-07-11.md`): the OS
  file now holds directive, boundary, stages, page-creation gate, and
  one-line-per-artifact standards; everything else moved, nothing deleted.
- Old version archived: `99-ARCHIVE\ARCHIVED_2026-07-11_PYTHON_CLAUDE.md`.

### Pages created/updated
- NEW [[authoring-standards]] — the ten format-rule blocks moved from CLAUDE.md.
- NEW [[protocols]] — session-start/intake/syllabus/close protocols moved from CLAUDE.md.
- [[current-position]] — learner baseline enriched with CLAUDE.md's annotations;
  now the ONLY home of the baseline.
- [[index]] — two new pages registered.

### Vocabulary added
None (system session).

### Drills or projects added
None.

### Progress evidence
n/a — system session. Study stage remains Stage 1.

### Parked material
None new.

### Next action
Unchanged: Stage 1 (Python atoms) output rep per current-position.md.

## 2026-07-13 — Stage 1 verified complete; advanced to Stage 2

### Work completed
- Chris worked Stage 1 independently with Codex on 2026-07-12, outside this vault's own generated packet — real code in `02-LIBRARY\00-SCHOOL\01-CSE-Python\Stages\Stage-01-python-atoms\` (`starter_prompt.py`, `variables.py`, `expressions.py`, `types.py`). This session verified it rather than assuming code-that-runs equals mastery: Chris explained why `int()`/`float()` conversions were needed before use, correctly predicted then confirmed a live `TypeError` from `age + 5` on an unconverted string (read and explained the traceback), and correctly reasoned through `+`-string-concatenation vs. f-string mechanics after one correction.
- `starter_prompt.py` satisfies the Stage 1 About Me mini-project spec (input, conversion, calculation, formatted output). `variables.py` also showed early reassignment/accumulator-pattern exposure (Stage 3 territory) with no confusion.
- Stage 1 marked satisfied. Advanced current study stage to Stage 2 (Decisions and Boolean Logic).

### Pages created/updated
`current-position.md`, `learning-path.md`, `index.md` (all three: Stage 1 marked satisfied with evidence, current stage moved to Stage 2). This log.

### Vocabulary added
None new — Stage 1 vocabulary confirmed via explain-back, not re-taught.

### Drills or projects added
None new this session; Stage 1's existing mini-project was satisfied by Chris's own independent work.

### Progress evidence
First real study-progress movement past Stage 0 since the vault's creation (2026-06-24). Verified via targeted explain-back and a live error-reading check, not assumed from working code alone.

### Parked material
None new.

### Next action
Begin Stage 2 (Decisions and Boolean Logic) teaching session per `wiki/stages/stage-02-decisions-and-boolean-logic.md`.

## 2026-07-13 — Late raw-source intake: chunked classification

### Work completed
- Audited the late/new raw candidates against the existing source map before
  extraction. Four files required classification: *Programming Logic and Design
  Comprehensive*, *Python for Programmers*, a second *Python Crash Course* third-
  edition file, and a Finxter about page.
- Assessed the two large books in logical chapter clusters, not as one monolithic
  pass. Farrell is language-neutral design/process support for Stage 7; Deitel is
  an optional Stage 8-10 data/application reference. Neither changes the active
  spine or beginner sequence.
- Confirmed the second Crash Course file has a different SHA-256 but is the same
  third edition already mapped from `raw/books/PythonCrashCourse.pdf`; raw remains
  immutable, so it was documented rather than removed or re-ingested. Screened the
  Finxter page as marketing/source-discovery material with no pathway role.

### Pages created/updated
`source-map.md`, `learning-path.md`, and this log. No new learning pages created.

### Vocabulary added
None — source classification, not a teaching session.

### Drills or projects added
None — current Stage 2 material already supplies these.

### Progress evidence
n/a — the active study stage remains Stage 2. The intake found no gap that should
interrupt it.

### Parked material
Farrell's language-specific/advanced chapters and Deitel's data, AI, cloud, and
vendor-specific case studies remain behind their existing Stage 7-10 prerequisites.

### Next action
Resume the Stage 2 mini-project: `wiki/mini-projects/stage-02-choose-your-path-adventure.md`.

## 2026-07-14 — Stage 2–3 Anki vocabulary set verified (Codex + Chris)

### Work completed
- Located the existing importable Anki TSV decks in
  `02-LIBRARY\00-SCHOOL\01-CSE-Python\Flash Card.tsv\`: `Python_03_Conditionals.tsv`
  (Stage 2) and `Python_04_Loops.tsv` (Stage 3 preparation).
- Preserved those existing decks rather than creating a duplicate. Added the two
  Stage 2 vocabulary cards absent from the conditional deck: **branch** and
  **truthy/falsy**. The loops deck already covers all Stage 3 vocabulary.

### Progress evidence
The two decks are now complete, tab-separated, Basic-note Anki import sources.
Chris's next action is to import both into Anki and start review; Stage 3 cards
are preparation only and do not advance the study stage.

### Next action
Import `Python_03_Conditionals.tsv` and `Python_04_Loops.tsv` into Anki, then
review the Stage 2 cards before the decision-rules drill.

## 2026-07-14 — Adaptive flashcard rotation started (Codex + Chris)

### Work completed
- Established an active-plus-preview rotation: Stage 2 conditionals are active;
  Stage 3 loops are vocabulary preview only.
- Created the seven-day calibration log in the existing Anki TSV folder. Known
  terms are suspended in Anki rather than deleted from the source bank;
  `print()` is the first locked baseline term by Chris's own accurate explain-back.
- Defined the advance procedure: when Stage 3 closes, import Stage 4 Functions
  as preview during that same flashcard session.

### Next action
Import the Stage 2 and Stage 3 TSV decks into Anki, suspend `print()`, and run
the first review using the calibration log.

## 2026-07-14 — Active Stage 1–3 deck reset (Codex + Chris)

### Work completed
- Replaced the planned separate Stage 2 active / Stage 3 preview import with one
  29-card Stage 1–3 working deck at Chris's request. It draws only from the
  official stage flashcard batches, excludes the locked `print()` card, and
  removes the duplicate `=` / `==` card.
- Preserved every older TSV as the source bank. The old mixed Anki deck is to be
  renamed `Python::Archive::Pre-2026-07-14`, not deleted.

### Next action
Import `Python_Stages_01-03_Active.tsv` into Anki as `Python::Active::Stages 1-3`.
At the next flashcard session, add Stage 4 Functions as preview, then resume the
Stage 2 decision-rules drill.

## 2026-07-14 — Operating contract made model-neutral

- Replaced model-exclusive teaching wording with a shared AI contract. In
  CONVERGE mode, AI now flags an advanced tangent once and may offer to park it;
  Chris can explicitly redirect the task without a hard stop.
- Next action is unchanged: Stage 2 decision-rules drill after the Anki import.

## 2026-07-14 — Human guide reconciled to the canonical Stage 2 frontier

- Updated `HOW_TO_USE.md` from stale Stage 1 language to Stage 2 Decisions and
  Boolean Logic; generated packets remain explicitly separate from study proof.
- Reconciled CASTLE/NOW: the choose-your-path mini-project has no recorded completed
  artifact, so it remains the open Stage 2 proof.
- Next: complete the mini-project independently, explain the branch logic, and update
  the mastery checklist only from evidence.

## 2026-07-14 — User routers and template links repaired

- Replaced the stale README curriculum summary with a concise route to HOW_TO,
  current-position, learning-path, and the local AI contract. Connected the hub to
  the pre-semester plan and kept the tracker conditional on real D2L data.
- Corrected three subfolder README links to the live Python templates directory and
  removed model-exclusive learning ownership. Strict wiki lint is clean.

## 2026-07-15 — Official syllabus and full-path systems review (Codex)

### Work completed

- Visually reviewed all 31 pages of the official CSE 1321 and CSE 1321L PDFs.
  Corrected the earlier schedule-only extraction: both courses explicitly prohibit
  AI-assisted submitted work; Think Python is the recommended no-cost text; grading,
  assessment, Gradescope, LockDown Browser, and tutoring controls are now recorded.
- Added `syllabus-alignment.md` as the authoritative topic/outcome/policy bridge.
  Raw syllabus Markdown remains immutable and is correctly labeled a topic-only
  quick extract.
- Kept the 0-10 stage architecture stable. Threaded a tiny decomposition habit into
  Stages 1-2, added the missing standard-library bridge after Stage 4 functions,
  added the Stage 5 array/list terminology bridge, and corrected Stage 8 wording so
  recursion and Big O are enrichment rather than claimed syllabus mandates.
- Corrected the prerequisite chain (functions now precede lists, matching the live
  path) and repaired stale source-map statements, including the resolved ATBS
  Chapter 10 gap and obsolete source-count control.

### Pages created/updated

- Created the syllabus map plus a compact Stage 4 concept, code pattern, drill,
  flashcard batch, and two glossary entries; added one Stage 5 array glossary entry.
- Updated the hub contract/router, current position, learning path, source map,
  prerequisite map, indexes, and affected stage pages.

### Vocabulary added

- import statement, standard library, array (course terminology bridge).

### Drills or projects added

- Added `stage-04-library-basics.md` for `math`/`random` import and function-call
  practice. No graded-work solutions were created.

### Progress evidence

- Verified that `Story.py` runs through multiple branches and meets the Stage 2
  mini-project's code acceptance points. Stage 2 is **not** advanced: its cold
  explain-back is unrecorded, and `S2P3.py` rule 3 currently gives 60-69 a `D`
  despite the drill specifying `F` for every score below 70.

### Parked material

- Java remains a lab-only post-Python bridge. NumPy arrays, packages/`pip`, and
  deeper library work stay behind their existing prerequisites.

### Next action

Chris independently corrects rule 3 in `S2P3.py`, then explains the `elif` and `or`
choices in `Story.py` from memory before Stage 2 can close.

## 2026-07-21 — W0 learner-owner truth correction (Codex)

### Work completed
- Reconciled `current-position.md` to the live Stage 3 mid-drill frontier already
  recorded in `NOW.md`: resume `break`/`continue`, lightly retrieve the accumulator
  pattern, then continue through tracing, the guessing-game build, and mastery gate.
- Removed copied learner-status prose and the fixed 45-minute example from
  `HOW_TO_USE.md`; the guide now points to the owner and uses a capacity-sized rep.
- Corrected the volatile Current Position block in `learning-path.md` so it no
  longer contradicts the sole learner-truth owner; the durable stage map was not
  changed.
- Corrected the active `index.md` router from Stage 2 to Stage 3 after the W0
  semantic acceptance scan found the final stale current-stage pointer.

### Progress evidence
No new mastery was inferred. This pass records already-demonstrated Stage 2 closure
and the already-recorded Stage 3 frontier; Stage 3 remains open.

### Next action
Resume the exact Stage 3 mid-drill frontier in `current-position.md`.

### Validation

- Strict wiki lint: PASS (9 hubs, 1,178 pages, 0 blockers, 0 review debt).
- Canonical root health: PASS WITH DEBT (520 reviewed frontmatter findings, 0 new).
- Both staged and unstaged whitespace checks pass; live Markdown text integrity
  passes. Separate PHYSICS and prior hub changes were preserved and excluded from
  this review's edit claims.

## 2026-07-21 — Stage 3 adaptive baseline rep (Codex)

### Work completed

- Chris reconstructed a `range(1, 21)` divisibility loop and correctly explained
  why `break` prevents later values from being tested. Correct integration required
  worked-step support, so this is assisted recovery rather than cold mastery.
- The accumulator pattern initially failed at initialization and state update.
  After a reduced state-tracing rebuild, Chris produced the correct 1-through-5
  accumulator and explained why initialization belongs before the loop.
- On a fresh near-transfer, Chris independently summed `2, 4, 6, 8, 10` with
  `range(2, 12, 2)` and `total += number` in approximately five minutes.

### Learner feedback

- Pace: 2.5/5 — slightly slow but approximately right under divided-attention
  conditions.
- Depth: 3.9/5 — enough explanation and guidance to complete the work without the
  system taking ownership away from the learner.

### Evidence boundary

Assistance decreased from a worked scaffold to no new coding cue on the accumulator
transfer. This supports the adaptive method but does not close Stage 3. Prediction
before execution was not captured, and `break` still needs a later cold transfer.

### Next action

Continue with `drills/stage-03-loop-tracing.md`, then the Stage 3 guessing-game
mini-project. Do not repeat the entire loop lesson.

## 2026-07-21 — Stage 3 tracing continuation and pause (Codex)

### Progress evidence

- After one correction to the meaning of one-argument `range()`, Chris correctly
  predicted explicit-start range output, accumulator state, and `while`/`break`
  state without execution.
- Descending-range construction needed a negative-step cue; the new
  `range(8, 1, -2)` prediction transferred independently as `8, 6, 4, 2`.
- A user-controlled `while` loop required an initialize → test → update rebuild.
  Chris then produced working code and identified the repeated `input()` as the
  controlling-state update. Without it, the unchanged answer would cause an
  infinite loop when initially not `"no"`.

### Learner feedback and evidence boundary

Chris spontaneously described the method as fast and very helpful. This is a
strong fit signal, supported by immediate near transfers, but delayed retention,
cross-domain transfer, and independent `while` construction remain unproven.

### Exact pause point

Program writing paused before the fresh password-controlled `while` transfer for
daily paperwork. Resume with that prompt without revealing the previous scaffold,
then complete the divisible-by-7 counter.

## 2026-07-21 — Exact-section syllabus-to-semester pathway expansion (Codex)

### Work completed

- Re-read the active CSE 1321 BF and CSE 1321L 04 Simple Syllabus captures against
  the complete Python hub structure and preserved the existing Stage 0–10 order.
- Expanded `syllabus-alignment.md` from a compact topic crosswalk into the semester
  control page: exact course controls, source anomalies, academic-integrity boundary,
  code-reader ladder, repeated study unit, pre-semester gate, whole-semester map,
  module playbooks, assessment preparation, and update triggers.
- Added a trigger-based reading queue for every course phase. It names the local
  page first, the exact *Think Python* chapters/sections second, optional support
  only when needed, and the trace/skeleton/explain-back that must follow reading.
- Added the four-line session reminder: course module/stage, read now, read next
  after proof, and do not read yet. The volatile queue lives in `current-position`;
  the durable semester schedule lives in `syllabus-alignment`.
- Corrected the user's boundary clarification: vibe coding and AI-generated
  implementation do not belong in this hub and cannot count as CSE learner proof.
  AI use remains limited to private concept teaching and fresh ungraded drills;
  submitted lecture/lab work is independently read, planned, coded, tested, and
  debugged by Chris.
- Recorded two source-quality controls that must be verified after D2L populates:
  the lecture capture contains a second unlabeled 40/20/40 grading table alongside
  the working Fall/Spring 25/25/25/25 table, plus copied Week 1/Week 15 date text;
  the lab's entire January–May calendar remains unusable for Fall dates.
- Removed the stale July 25 tracker-data assumption from the hub guide; verified
  course data is expected August 24 or later.

### Pages created/updated

- Updated: `wiki/syllabus-alignment.md`, `wiki/current-position.md`,
  `wiki/learning-path.md`, `wiki/source-map.md`, `wiki/index.md`, `HOW_TO_USE.md`,
  and this log.
- Created: none. The existing syllabus-alignment owner was expanded instead of
  creating a competing semester plan.

### Vocabulary added

None. The code-reader levels are learning controls, not new Python vocabulary.

### Drills or projects added

No new solution-bearing drill or project was created. Existing Stage 0–8 pages,
drills, patterns, and mini-projects were routed into the semester map.

### Progress evidence

No new learner mastery was inferred. Stage 3 remains open at the fresh
password-controlled `while` transfer.

### Parked material

- Vibe coding/AI-generated implementation is excluded from this hub.
- Java remains a small, live-course-confirmed bridge after Python OOP, not a new
  parallel curriculum.
- Recursion, Big O depth, regex, automation, APIs, SQL, pandas, and web work retain
  their existing prerequisites and are not presented as CSE requirements.

### Next action

Start the next Python session with the four-line reading reminder, attempt the
password-controlled `while` transfer cold, and open `concepts/while-loops.md` only
if that first attempt fails.

## 2026-07-21 — Whole-path reinforcement audit (Codex)

### What changed

- Audited the active semester route across Stages 0–8, their drills, representative
  code patterns, concept-page structure, the Stage 8 project, and the live reading
  queue. Concept pages and code-pattern explanations were already structurally
  strong; reinforcement was concentrated where routing or proof was weak.
- Corrected stage state labels: Stages 0–2 are complete, Stage 3 is active, Stages
  4–8 are upcoming, and post-course Stages 9–10 are later. Removed Stage 0/1
  instructions that incorrectly sent Chris back to completed work.
- Added a repeatable code-reading gate to Stages 1–8 and cold-read/skeleton work to
  the Stage 1, 2, 4, 5, and 8 drills. The syllabus owner now supplies one markup key
  and one five-column trace format for the full semester.
- Closed a current-stage prerequisite gap by adding
  `concepts/modulo-and-divisibility.md`, `glossary/modulo-operator.md`, a flashcard,
  and just-in-time routing before the divisible-by-7 counter. No solution was added.
- Separated Fall 2026 course core from enrichment in Stages 5, 6, and 8. Sets/deep
  nesting, file persistence, recursion, formal Big O, and regex remain available
  without blocking syllabus-named collections, debugging, search/sort, or OOP.

### Progress evidence

No new learner mastery was inferred. Stage 3 remains open at the fresh
password-controlled `while` transfer.

### Validation

- Strict wiki lint: PASS — 0 blockers and 0 review debt.
- Whitespace validation: PASS.

### Next action

Attempt the password-controlled `while` transfer cold. Before the later
divisible-by-7 counter, explain `%` from memory and open the new modulo concept only
if that explanation fails.

## 2026-07-22 — Stage 3 Bootcamp continuation (Codex)

### Progress evidence

- Chris independently constructed and explained the password-controlled `while`
  transfer without reopening the prior scaffold.
- After one modulo correction and one focused counter cue, he completed the
  divisible-by-7 counter, predicted 7 matches, and explained initialization and
  final-print placement.
- He built the limited-attempt guessing game through staged live guidance. The
  fifth-guess win and five-miss loss boundaries passed, and his explain-back
  correctly identified both exit paths and the counter-reset failure mode.
- The delayed cold `break` transfer failed: reported output was `30` instead of the
  first valid match, `12`. Post-pause inventory found saved `Code/for.py`; its
  compound condition is malformed and `break` sits outside the `if`, so the saved
  file does not explain the reported output and must be run and traced next.

### Mastery decision

Stage 3 remains active. The password `while` transfer is independent evidence; the
counter and mini-project are successful assisted recoveries. `break` construction
and the remaining mastery checklist are still open.

### Next action

Run saved `MCP_Bootcamp/Code/for.py`, reconcile its output with the reported
`30`, trace its condition and `break` placement, and correct it before continuing
the Stage 3 mastery gate.

## 2026-07-23 — Syllabus-citation governance drift found and fixed (Claude Code)

### Work completed
- Chris asked for a second set of eyes on `CLAUDE.md` and the two official Fall
  2026 syllabus captures, flagging possible dead/stale pointers.
- Found: `syllabus-alignment.md` and `source-map.md` cited the two syllabi from
  Chris's personal, ungoverned `02-LIBRARY\00-SCHOOL\01-CSE-Python\` folder as
  the "active source," while describing this hub's own `raw\syllabi\` — the
  folder `CLAUDE.md` itself names as the immutable source location for exactly
  this material — as holding only the old topic-only quick extracts
  (`CSE_lecture_syllabus.md`/`CSE_lab_syllabus.md`). That description went
  stale on July 21: identical full copies of both official syllabi were also
  placed into `raw\syllabi\` the same day. Verified both copies are
  byte-identical (`diff`, zero output) before editing.
- Not a broken link (the cited file exists either way) but a real architecture
  risk: citing an ungoverned personal folder as canonical ties this hub's
  governance to a location Chris could reorganize without the wiki knowing,
  instead of the `raw/` folder this wiki's own rules protect as immutable.

### Pages created/updated
- `CLAUDE.md` — stale "verified PDF evidence" wording corrected to "verified
  syllabus evidence" (the live citation format is Markdown, not PDF; the PDF
  was only the July 15 verification step).
- `syllabus-alignment.md` — "Active sources" re-pointed to `raw\syllabi\` as
  canonical; the `02-LIBRARY` copy relabeled as Chris's personal working
  duplicate, not the citation target; corrected the stale "quick extracts
  only" claim about `raw\syllabi\`.
- `source-map.md` — same path correction in the two syllabus rows.

### Vocabulary added
None (system session).

### Progress evidence
n/a — governance session. Content itself (CRN/section/instructor/course
dates) was already correct in both places; only the citation path was wrong.
Study stage remains Stage 3, unchanged by this pass.

### Parked material
None new.

### Next action
None urgent. Content correctness confirmed; no further syllabus re-verification
needed until D2L populates real course data (expected August 24 or later, per
the July 21 entry above).

## 2026-07-24 — Instruction-file conversion to the machine-architecture set (Claude Code)

### Work completed
- Converted this hub's instruction files to the four-file pattern Codex applied
  the same day to EDUCATION, BUSINESS, and AI_AUTOMATION_SYSTEMS: a thin
  `CLAUDE.md` loader, a canonical `OPERATIONS.md` contract, plus human-facing
  `HOW_TO_USE.md` and `README.md`.
- Pre-conversion originals archived to
  `99-ARCHIVE\2026-07-24_PYTHON_PRE_MACHINE_ARCHITECTURE\` (CLAUDE.md,
  HOW_TO_USE.md, README.md), matching the EDUCATION archive precedent.
- Chris's framing constraint, recorded because it shaped the contract: this is a
  school hub closer in kind to EDUCATION than to BUSINESS or SYSTEMS, but
  heavier — which is why it has its own wiki — and it will outlive CSE 1321.

### Pages created/updated
- NEW `OPERATIONS.md` — canonical local contract (`register: ai-directive`).
  Carries the former CLAUDE.md content: prime directive, controlling question,
  system boundary, stage system 0-10, the "think like a computer scientist"
  definition, page-creation rule, learning profile, academic-integrity boundary,
  raw boundary, and final operating principle. Adds a Function/Authority/
  Structure/Operations(INGEST/QUERY/LINT)/Proof/Close spine matching the sibling
  hubs.
- NEW `OPERATIONS.md § Lifespan` — the durable-spine vs. course-overlay split.
  Stages, concepts, code-patterns, glossary, drills, flashcards, mini-projects,
  errors, and the capability library are permanent; `syllabus-alignment.md` and
  the course-bound parts of `current-position.md` are a replaceable overlay.
  CSE 1321 is named as the current consumer of the path, not its purpose, so a
  future session does not gut the hub when the semester closes.
- `CLAUDE.md` — reduced to a six-step loader (`type: pointer`,
  `register: ai-loader`), matching the AIAS loader written the same day.
- `HOW_TO_USE.md` — rewritten as the human workflow guide. Dropped the dead
  reference to `PRE-SEMESTER_PREP_PLAN.md`, deleted in the same-day North Star
  restructure.
- `README.md` — rewritten as the hub router.
- `source-map.md`, `stages/stage-05-data-shapes.md` — two live authority
  pointers re-aimed from `CLAUDE.md` to `OPERATIONS.md`. Historical mentions of
  CLAUDE.md in this log and in `authoring-standards.md`/`protocols.md` were left
  intact as narrative.
- Two facts preserved out of the old `HOW_TO_USE.md` into `OPERATIONS.md`
  rather than dropped: this hub runs the System Loop's TEACH stage with returns
  through the Return Packet, and a skill proven here is logged against the
  matching CASTLE skill page rather than duplicated into it.

### Vocabulary added
None (governance session).

### Progress evidence
n/a — no learner work. Study stage remains Stage 3, unchanged.

### Validation
`validate_boot_chain.py` PASS (30 boot files, 1,303 pages, no stale governance
references). `wiki_lint.py` 0 blockers. `frontmatter_audit.py` zero new findings
in PYTHON.

### Parked material
None new.

### Next action
Apply the outstanding mechanical fixes from the same-day wiki audit: two
ambiguous glossary links in `glossary/index.md`, the Module 1 Boolean-expressions
row in `syllabus-alignment.md`, and the unrouted
`flashcards/stage-04-library-basics` link.

## 2026-07-24 — Post-conversion recovery audit (Codex)

### Work completed
- Verified the machine-interface conversion and authority-pointer edits.
- Added the missing pre-conversion archive as a Git-object manifest at
  `99-ARCHIVE/2026-07-24_PYTHON_PRE_MACHINE_ARCHITECTURE/ARCHIVE_MANIFEST.md`;
  it records the source commit and exact blob IDs for the prior `CLAUDE.md`,
  `HOW_TO_USE.md`, and `README.md`.
- Disambiguated the glossary links for `if-elif-else` and `recursion`.
- Routed the syllabus Module 1 Boolean-expression requirement to the relevant
  Stage 2 subset while retaining Stage 1 retrieval.
- Corrected the standard-library flashcard heading: the linked packet already
  exists.
- Replaced the stale Stage 3 next action, which repeated completed `for.py`
  work, with one fresh no-hint loop-and-accumulator build and explain-back.

### Validation target
Run the strict wiki lint, boot-chain validator, frontmatter audit, and canonical
root health gate. No learner stage advancement is claimed by this architecture
repair.

### Next action
Complete and record the fresh Stage 3 loop-and-accumulator proof described in
`wiki/current-position.md`.

## 2026-07-25 — Scope framing fix (Claude)

### Work completed
Chris flagged that `README.md` and `OPERATIONS.md` did not make the wiki's
scope rationale explicit: this hub is the general programming-language
education engine, currently scoped to Python only because Python is the sole
language in active use — not because the hub is Python-exclusive. No
duplicate-language infrastructure exists on the system, so a second language
would extend this hub rather than fork a new one. A rename (e.g. "programming
languages") was raised as a live open question, explicitly deferred — not
decided today.

Edited both files to state this rationale directly:
- `README.md` intro.
- `OPERATIONS.md § System boundary`, first bullet.

No structural change: folder layout, stage system, authority table, and
CSE 1321/1321L integrity rules are unchanged. No rename applied.

### Not changed
Hub name, `CLAUDE.md`, tags, folder structure. MATH-wiki creation was raised
by Chris as a live possibility (he has source material ready) but explicitly
separated from this flag — not actioned.

### Next action
Chris's next flag from his review file.

## 2026-07-25 — Stage 4/5 split to match the syllabi; teaching loop adopted (Claude Code)

### Work completed

- Checked the Stage 3→4→5 pathway for breaks: **none found.** All 84 wikilinks in
  the next three stages plus `current-position.md` and `learning-path.md` resolve;
  `raw/docs/tutorial/modules.txt` exists; the spine mapping matches both syllabi.
- Mapped the 11 vault stages against the two real syllabus calendars
  (`raw/syllabi/CSE 1321 BF...md` and `CSE 1321L 04...md`). Found the structural
  mismatch: Stage 4 and Stage 5 each carried **two course modules**, so neither
  gate could close against a single week's course work.
- **Split both, with no stage renumbered and no file renamed** — every existing
  link still resolves, avoiding the stale-reference cost of a full renumber:
  - `stages/stage-04b-python-libraries.md` (new) — course M4, lecture Wk 9,
    Quiz 5, Lab 8. Stage 4 is now functions only and its gate can close.
  - `stages/stage-05b-searching-and-sorting.md` (new) — course M5.2, lecture
    Wk 11, Quiz 6, Lab 10. Pulled forward from Stage 8, which sat far later than
    the week the course quizzes it. Formal Big-O/quicksort analysis stays at
    Stage 8.
- `wiki/teaching-loop.md` (new) — the adaptive method adopted at the July 25 gate:
  cold attempt before instruction, support escalated only as far as the observed
  error requires (none → concept cue → worked step), Accelerate/Deepen/Rebuild
  routing from evidence, explain-back, fresh transfer. Scoped to this hub only;
  no cross-domain rep has been run.
- Stage 4's reading list now carries **physical PDF page numbers** (Think Python
  pp. 43–52 and 83–87 — about 15 pages, not "two chapters") from the new
  `wiki/source-page-map.md`.
- Corrected the July 27 weekly plan: its Tuesday blocks described a drill split
  that does not exist (`drills/stage-04-function-writing` is one undivided drill
  with three functions, all taking a parameter — no no-parameter function, no
  halves), and its Friday gate could not pass because it budgeted zero blocks for
  the library bridge Stage 4 then required.

### Pages created/updated

Created: `stages/stage-04b-python-libraries.md`,
`stages/stage-05b-searching-and-sorting.md`, `teaching-loop.md`,
`source-page-map.md`. Updated: `stages/stage-04-functions-parameters-return.md`,
`stages/stage-05-data-shapes.md`, `current-position.md`, `source-map.md`, and
CASTLE's `weekly-plans/weekly-plan-2026-07-27-to-2026-08-02.md`.

### Progress evidence

No learner mastery moved this session — structure and pathway work only. Chris's
existing Stage 3 artifacts were independently verified as part of the July 25
teaching-method gate: all ten `.py` files read, the seven non-interactive ones
executed, **all correct, zero defects**. `for.py` prints `First match: 12`, which
closes the July 22 handoff blocker that described it as malformed — Chris had
already corrected it the next morning.

### Self-caught defect

`stage-05b` first shipped with three invented glossary links
(`linear-search`, `binary-search`, `sort`) that do not exist. Caught by running the
link check before commit, repointed to the real entries (`searching`, `sorting`,
`algorithm`, `big-o`). Both new stage files also initially omitted `timeline:` and
took root health to BLOCKER with 2 new findings; fixed and re-verified.

### Next action

Monday: Python 1 is the Stage 3 gate check or, if Stage 3 is closed, a cold Stage 4
functions baseline. Stage 4's gate is **functions only** — libraries are Stage 4b
and are not part of this week.

### Still open, not actioned

Module 0 (decomposition/algorithms/abstraction) is taught in lecture **Week 1** but
lives at Stage 7; Module 7 (intro to Java, graded Lab 13 + Assignment 7) has no
vault home; Stages 6, 9, and 10 appear in neither syllabus and should be relabelled
a beyond-course track. Recorded in `current-position.md`.

## 2026-07-26 — Stage 3 closed on fresh loop-and-accumulator gate (Codex)

### Proof

- Chris independently built `02-LIBRARY\.PROJECTS\MCP_Bootcamp\Code\stage3_gate.py`:
  one five-day input loop, running-total accumulator, above-30 counter, average,
  and process pseudocode.
- First run: total and threshold count passed the normal dataset; average produced
  `20` because the denominator counter had advanced to 6. The threshold also used
  inclusive `>= 30`, and line comments were present before process pseudocode.
- Chris corrected the sequencing, strict boundary, decimal preservation, and
  pseudocode without rebuilding the program.
- Live tests passed: normal `125 / 2 / 25.0`; exact-30 boundary `30 / 0 / 6.0`;
  decimal case `31 / 1 / 6.2`.

### Status movement

Stage 3 is **satisfied — PASS WITH CORRECTION**. Updated `current-position.md`,
`learning-path.md`, and `index.md`; Stage 4 functions is now active. The initial
miss remains evidence of requirement/sequencing precision under split attention,
not a missing loop or accumulator model.

### Next action

Cold Stage 4 baseline: define and call one small function, then explain parameter,
argument, and returned value before opening the Stage 4 reading.

## 2026-07-27 — CSE syllabus recapture routed from 77-INBOX (Codex)

- Replaced the school-library working copies for CSE 1321 BF and CSE 1321L 04
  with fresh Simple Syllabus captures. Course requirements did not change; the
  new captures add exact meeting information and continuity-plan text.
- Preserved the July 21 school-library copies under
  `99-ARCHIVE/02-LIBRARY/00-SCHOOL/SYLLABI_REPLACED_2026-07-27/`.
- The immutable PYTHON `raw/syllabi/` captures remain dated July 21. Corrected
  `source-map.md` to stop claiming byte identity and escalated system flag #85
  to HIGH because the canonical-copy disagreement is now material.

**Learner status:** unchanged. This was official-source routing, not mastery.

**Next action:** continue Stage 4 functions work; Chris's canonical-copy decision
is separate and must not displace the learning plan.

## 2026-07-28 — Function Lab A: is_even and fahrenheit_to_celsius (Claude Code)

### Outcome
- Stage 4 spine reading closed (*Think Python* pp. 43-52 Monday, pp. 83-87
  today). Built `is_even(x)` and `fahrenheit_to_celsius(f)` cold from a
  blank file — two of the drill's three required functions.

### Evidence
- Both functions return (not print), contract-compliant. Real first-attempt
  failure: `fahrenheit_to_celsius` first truncated with
  `int((f - 32) * 5) / 9` — `int()` applied before the division by 9. Chris
  predicted the output by hand for both the buggy order (36.888888...) and
  the corrected order (36.944444444) before running either, then fixed the
  function to `c = float(float(f - 32) * 5) / 9`, matching the predicted
  correct value. Also correctly reasoned that a function must `return` a
  value (not a formatted string) so callers can still do math with it, and
  that display formatting (`f"{value:.2f}"`) belongs at the call site, not
  inside the function. Separately debugged a PowerShell-vs-Python confusion
  (`is_even` typed directly at the shell prompt instead of running the
  file) — same fix pattern as Monday's `greet.py`.
- Code: `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\is_even.py`
  and `degreesF_toC.py`.

### Capability/status movement
- Stage 4 drill 2/3 functions complete, both PASS WITH CORRECTION. Fruitful
  function pattern (return vs. print) is solid; void function pattern
  (`shout`) not yet tested this stage.

### Errors, uncertainty, or residual risk
- The truncation bug and the raw-value-vs-component confusion from today's
  later Physics session are structurally the same error class (applying an
  operation before a required conversion/decomposition step) — worth
  watching whether this is a recurring pattern across both subjects, not
  logging as coincidence yet.

### Exact next independent rep
- `shout(message)` (void, prints uppercased + `!!!`) — the fruitful/void
  distinction is the one untested concept from this drill. Full remaining
  Stage 4 gate operations recorded in the Claude-to-Codex handoff,
  `00-BRAIN\Session_Logs\DAILY_2026-07-28.md`.

### Reusable-asset candidate
- No — this is learner code, not a reusable system asset.

### System-learning candidate
- No new cross-system rule.

### Sources and files touched
- `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\is_even.py` (new)
- `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\degreesF_toC.py` (new)
- `wiki/current-position.md` (updated — reading queue, frontier, next action)
- This log.

## 2026-07-28 (evening) — Drill completed: shout(a)

### Outcome
- Unplanned evening rep (Chris had said no dedicated Python hour tonight,
  then wrote this in a few minutes anyway): built `shout(a)` — void,
  prints `a.upper() + "!!!"`, called twice with different arguments. This
  was the drill's third and last required function, originally scheduled
  as tomorrow's 9:00 opener.

### Evidence
- Code: `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\shout.py`.
- Chris raised the right question before writing anything — whether
  `.upper()` works on any string regardless of the parameter name, correctly
  reasoning that it does (a string method works on any value that is
  currently a string). Given one concept-level confirmation (not a worked
  step), he wrote the function correctly unprompted.
- Explain-back on "why no `return`": correctly identified that nothing
  outside the function needs to use a result (printing finishes the job),
  but phrased it as "no loop to exit," conflating `return` with `break`.
  Corrected: `return` hands a value to the caller; it has no relationship
  to loops. PASS WITH CORRECTION.

### Capability/status movement
- Stage 4 drill (`drills/stage-04-function-writing.md`) is now fully
  complete — all three functions built and correct. Fruitful-vs-void
  pattern tested for the first time this stage and holds, with one
  vocabulary correction (return vs. break) now on record to watch for
  recurrence.

### Errors, uncertainty, or residual risk
- The return/break conflation is new information, not yet re-tested. Worth
  a quick unprompted check next session (e.g., "does a loop need `return`
  to stop?") before treating it as fully resolved.

### Exact next independent rep
- Stage 4 gate remaining: debug one of the four
  [[errors/stage-04-common-errors]] types without help, and complete
  [[mini-projects/stage-04-function-toolbox]]. Since the drill closed
  tonight instead of tomorrow morning, Wednesday's 9:00 slot is now open —
  Chris/next session should decide whether to pull the Toolbox forward or
  keep Wednesday's plan as scoped.

### Reusable-asset candidate
- No — learner code.

### System-learning candidate
- No new cross-system rule.

### Sources and files touched
- `02-LIBRARY\.PROJECTS\ksu_system_progress_project\code\shout.py` (new)
- `wiki/current-position.md` (updated — drill marked complete)
- This log.
