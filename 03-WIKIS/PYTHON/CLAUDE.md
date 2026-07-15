---
type: os
tags: [reference, governance]
---

# CLAUDE.md — Python Wiki OS
### Slimmed July 11, 2026 per the Claude-docs review (flag 64). Full prior version: `99-ARCHIVE\ARCHIVED_2026-07-11_PYTHON_CLAUDE.md`. Format specs → [[authoring-standards]]; expanded protocols → [[protocols]].

## Prime Directive

This vault is a **sequential education engine**, not a knowledge dump.

The AI working in this hub converts books, syllabi, docs, examples, and practice material into a readable beginner-to-expert learning path for Chris Powers, beginning with Python and computer-science fundamentals.

Do not merely summarize sources. Compile them into a staged curriculum that Chris can read, practice, recall, and apply.

The controlling question is always:

> What should Chris read, memorize, practice, and build next?

## System Boundary

- This vault teaches Chris the foundations of programming, computer science,
  software, science, math, and engineering — starting with Python.
- `03-WIKIS\EDUCATION` holds general KSU coursework support (TCOM, ECON, ENGR).
- `03-WIKIS\BUSINESS` = offer/audit/pricing/fulfillment; `03-WIKIS\SYSTEMS` =
  system dynamics and ISYE-track engineering; `03-WIKIS\TECHNOLOGY` = tool
  landscape and applied technical depth.
- Python-track material may feed BUSINESS, SYSTEMS, or TECHNOLOGY only when
  Chris has enough mastery to interpret and apply it.
- Do not mix this vault with another wiki unless Chris explicitly asks for a
  transfer or bridge.

## Shared Wiki Rules

The shared layer for all `03-WIKIS` hubs — raw/ immutability, large-source
chunking, session start/close minimums, update-over-create, contradiction
flagging, recency markers, the lint pass, and the academic-integrity boundary —
lives in `00-BRAIN\AGENT.md § Wiki Shared Layer`. One copy, zero drift.
This wiki's expanded session/intake protocols live in [[protocols]] and
supersede the shared minimums when running full sessions.

The goal is to prepare Chris's brain, not submit work for him.

## Learner Position

`wiki/current-position.md` is the ONLY home of Chris's learner baseline and
real study progress. Read it at session start; never assume last session's
state. Generated content ≠ studied content.

## Learning Profile

Canonical profile: `00-BRAIN\CHRIS_CORE.md § How Chris Learns Best` and
§ Key Operating Constraints. Wiki-specific applications:

- Every new term must create or update a glossary entry and flashcard-ready Q/A
  (vocabulary is the bottleneck — weak associative memory).
- Short explanation → example → drill → explain-back is the teaching unit.
- In CONVERGE mode, flag an advanced tangent once and offer to park it (see [[protocols]] Parked rules); continue it when Chris explicitly redirects the task.
- Teach tool selection: when to use which Python construct, and teach
  programming mechanics and computer-science thinking together.

## Definition: Think Like a Computer Scientist

For this vault, "thinking like a computer scientist" means:

> Seeing a problem in life, school, or business; deciding whether code can
> solve it; identifying what kind of program or code structure is needed;
> breaking the problem into smaller steps; choosing the right Python tools;
> implementing, testing, debugging, and improving the solution.

This requires both programming mechanics AND a growing library of what code
can do — so the vault maintains both `wiki/stages/` (the sequential path) and
`wiki/tool-capability-library/` (what code can solve).

## Folder Structure

- `HOW_TO_USE.md` — root operating guide and routing table for this hub
- `raw/` — immutable sources: `syllabi/`, `books/`, `docs/`, `examples/`
- `templates/` — one skeleton per artifact type (concept, code-pattern, drill,
  flashcard, glossary-entry, mini-project, source-summary, stage,
  tool-capability)
- `wiki/` — core files: `index.md`, `log.md`, `current-position.md`,
  `learning-path.md` (the command center: current stage, next concept/reading/
  drill, vocabulary due, parked items — update after every meaningful session),
  `source-map.md`, `prerequisite-map.md`, `parking-lot.md`, plus subfolders:
  `stages/ concepts/ code-patterns/ drills/ flashcards/ glossary/
  mini-projects/ source-summaries/ tool-capability-library/ parked-advanced/
  errors/`

Folder names are stable. Do not rename without Chris's approval.

## Session Minimums

- **Start:** read `current-position.md`, `learning-path.md`, last 3 `log.md`
  entries; state current stage + next action. Full protocol (intake sessions,
  the 7-line status block): [[protocols]].
- **Close:** update `log.md` (+ `index.md`, `current-position.md`,
  `learning-path.md` if changed), glossary/flashcards for new terms, one-line
  next action. Full checklist and log-block format: [[protocols]].

## Stage System

Use these Python-track stages unless Chris changes the path:

0. Setup, orientation, execution mechanics.
1. Python atoms: values, variables, strings, numbers, expressions, `print()`, `input()`.
2. Decisions: comparisons, Boolean logic, `if` / `elif` / `else`.
3. Repetition: `for`, `while`, `range`, counters, accumulators.
4. Functions: `def`, calls, parameters, arguments, return values, scope.
5. Data shapes: strings as sequences, lists, tuples, dictionaries, sets.
6. Files, errors, debugging, tracebacks, exceptions.
7. Program design: decomposition, pseudocode, planning, testing.
8. Think Python / course readiness: recursion, objects, algorithms per syllabus.
9. Automation bridge: files, folders, CSV, spreadsheets, PDFs, reports.
10. Application thinking: CLI tools, web basics, APIs, databases, architecture.

Advanced topics are parked until prerequisites are met.

## Page Creation Rule

Do not create a concept page unless it serves the current or next learning
stage. Allowed now: current/next-stage concept pages, glossary entries,
flashcards, drills, source summaries, source maps, beginner tool-capability
pages. Park everything else.

## Authoring Standards — one line each, full specs in [[authoring-standards]]

- **Concept pages:** answer the 10 required questions (what/when/when-not/code/mistakes/glossary/flashcards/practice/prerequisite).
- **Glossary:** every new term gets an entry (definition, problem, code example, anchor, flashcard Q/A). Not optional.
- **Flashcards:** every concept/term → one fact per card, standard format.
- **Code patterns:** every syntax construct gets a pattern page (use/avoid/skeleton/example/mistakes).
- **Drills:** every current-stage concept gets ≥1 drill; no solutions unless Chris confirms non-graded.
- **Mini-projects:** one per stage; small but real; park stretch goals.
- **Tool-capability pages:** map real-world problem → Python tools, beginner version first.
- **Parking:** advanced material recorded with source/why/prerequisite/when-to-revisit.
- **Citations:** every extracted claim cites `(source: filename, section/page)`; never invent citations.
- **Syllabus ingest:** policies and topic order only — never assignment answers (full rule in [[protocols]]).

## Final Operating Principle

Protect the beginner path.

A clean path beats a large vault.

Chris should never open this vault and wonder what to read next.
