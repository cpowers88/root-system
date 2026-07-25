---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [programming, school, governance]
created: 2026-07-24
---

# PYTHON_WIKI — OPERATIONS

## Function

Convert books, syllabi, documentation, and practice material into a sequential
beginner-to-expert learning path in Python and computer-science fundamentals,
and hold the durable record of what Chris can actually do.

This is a **learning engine**, not a knowledge dump. Do not merely summarize a
source; compile it into a staged curriculum Chris can read, practice, recall,
and apply.

The controlling question is always:

> What should Chris read, memorize, practice, and build next?

## Lifespan

This wiki outlives any single course. Two layers, different lifespans:

| Layer | Contents | Lifespan |
|---|---|---|
| **Durable spine** | `wiki\stages\` 0–10, `concepts\`, `code-patterns\`, `glossary\`, `drills\`, `flashcards\`, `mini-projects\`, `errors\`, `tool-capability-library\` | Permanent programming capability. Continues after any course ends. |
| **Course overlay** | `wiki\syllabus-alignment.md`, course-bound entries in `current-position.md`, `raw\syllabi\` | Bound to one course. Superseded and archived when that course closes. |

CSE 1321/1321L is the **current consumer** of the staged path, not its reason
for existing. When the course ends, supersede the overlay and continue the
spine — do not shrink, retire, or gut the hub because a semester finished.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR\NORTH_STAR.md` |
| Semester outcomes and readiness gates | `01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md` |
| Official syllabi, assignments, notes, records | `02-LIBRARY\00-SCHOOL\` |
| Cross-course syllabus status | `02-LIBRARY\00-SCHOOL\SYLLABUS_STATUS.md` |
| Chris's learner truth and mastery evidence | `wiki\current-position.md` — sole owner |
| Durable curriculum sequence | `wiki\learning-path.md` |
| Course alignment and reading triggers | `wiki\syllabus-alignment.md` |
| Source classification and roles | `wiki\source-map.md` |
| Page format specifications | `wiki\authoring-standards.md` |
| Expanded session/intake protocols | `wiki\protocols.md` |
| Sequencing and next actions | CASTLE and `NOW.md` |
| General non-Python course support | `03-WIKIS\EDUCATION\` |
| Physics learning system | `03-WIKIS\PHYSICS\` |

An official course source overrides every derivative page here. No file in this
wiki MAY redefine the North Star, claim mastery Chris did not demonstrate, or
advance the learner frontier from generated content.

This hub runs the TEACH stage of the System Loop, plus its own `raw\`→`wiki\`
STRUCTURE intake. Proof returns through the Return Packet. Both are canonical in
`01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md`; do not define a
competing loop or packet here. A skill proven in this hub is logged against the
matching CASTLE skill page, not duplicated into it.

## System boundary

- This wiki is the general programming-language education hub — starting
  with Python because it is the only language currently in active use, not
  because the hub is Python-exclusive. No duplicate-language infrastructure
  exists on the system; when a second language enters scope, extend this hub
  first rather than fork a new one. A rename (e.g. "programming languages")
  is an open question for that point, not a decision made now.
- `03-WIKIS\EDUCATION` holds general KSU course support. PYTHON is the case
  EDUCATION describes as graduating to its own wiki: enough durable staged
  material to need its own engine.
- `03-WIKIS\BUSINESS` owns offer/audit/pricing/fulfillment.
  `03-WIKIS\SYSTEMS` owns system dynamics and the ISYE track.
  `03-WIKIS\TECHNOLOGY` owns tool landscape and applied technical depth.
- Python material feeds those hubs only once Chris has enough mastery to
  interpret and apply it.
- Do not mix this wiki with another unless Chris explicitly asks for a transfer
  or bridge.

## Structure

```text
raw/                      immutable sources: syllabi/ books/ docs/ examples/
templates/                one skeleton per artifact type
wiki/
  index.md                canonical catalog
  log.md                  append-only session history
  current-position.md     learner truth — sole owner of mastery
  learning-path.md        durable Stage 0-10 sequence
  source-map.md           source inventory, roles, and classification
  syllabus-alignment.md   course overlay: pathway, triggers, playbooks
  prerequisite-map.md     concept dependency chain
  parking-lot.md          advanced material held with unlock conditions
  authoring-standards.md  full page/glossary/flashcard/drill format specs
  protocols.md            expanded session, intake, and close protocols
  stages/                 the sequential path, 0-10
  concepts/ code-patterns/ drills/ flashcards/ glossary/
  mini-projects/ source-summaries/ tool-capability-library/
  parked-advanced/ errors/
```

Folder names are stable. Do not rename without Chris's approval. Do not
pre-build empty structure.

## Stage system

Use these stages unless Chris changes the path:

0. Setup, orientation, execution mechanics.
1. Python atoms: values, variables, strings, numbers, expressions, `print()`, `input()`.
2. Decisions: comparisons, Boolean logic, `if` / `elif` / `else`.
3. Repetition: `for`, `while`, `range`, counters, accumulators.
4. Functions: `def`, calls, parameters, arguments, return values, scope.
5. Data shapes: strings as sequences, lists, tuples, dictionaries, sets.
6. Files, errors, debugging, tracebacks, exceptions.
7. Program design: decomposition, pseudocode, planning, testing.
8. Think Python / course readiness: recursion, objects, algorithms.
9. Automation bridge: files, folders, CSV, spreadsheets, PDFs, reports.
10. Application thinking: CLI tools, web basics, APIs, databases, architecture.

Advanced topics stay parked until their prerequisite is met. The dependency
chain is `wiki\prerequisite-map.md`; unlock conditions are `wiki\parking-lot.md`.

## Definition — think like a computer scientist

> Seeing a problem in life, school, or business; deciding whether code can
> solve it; identifying what kind of program or code structure is needed;
> breaking the problem into smaller steps; choosing the right Python tools;
> implementing, testing, debugging, and improving the solution.

This requires programming mechanics **and** a growing library of what code can
do. That is why the hub maintains both `wiki\stages\` (the sequential path) and
`wiki\tool-capability-library\` (what code can solve). Both pillars are
required; neither substitutes for the other.

## Operations

### INGEST

1. State the exact learning gap the source would close.
2. Verify the source's role and difficulty against `wiki\source-map.md`.
3. Read large sources in bounded chunks; record the range covered.
4. Update an existing page before creating a new one.
5. Cite every extracted claim as `(source: filename, section/page)`. Never
   invent a citation.
6. Create a glossary entry and flashcard-ready Q/A for every new term.
   Vocabulary is the bottleneck; this is not optional.
7. Separate verified claim, source claim, inference, and unknown.
8. Update `wiki\index.md` and append `wiki\log.md`.

Syllabus ingest takes policies, outcomes, and topic order only — never
assignment answers.

### QUERY

1. Read `wiki\current-position.md` and `wiki\learning-path.md`.
2. State the four reading lines before teaching: course module / vault stage,
   read now, read next after this proof, do not read yet.
3. Load only the stage and concept pages the active question needs.
4. Teach in the unit: short explanation → example → drill → explain-back.
5. End with a concrete next action — trace, skeleton, drill, or build. Not more
   reading.

### LINT

Check unresolved links and orphan pages, index-versus-tree drift, pages
unreachable from the staged path, concepts taught without a glossary entry or
flashcard, stages without a drill or mini-project, stale course facts, claims
without citations, generated content mistaken for studied content, and material
that outran its prerequisite.

## Page creation rule

Do not create a concept page unless it serves the current or next learning
stage. Permitted now: current/next-stage concept pages, glossary entries,
flashcards, drills, source summaries, source maps, beginner tool-capability
pages. Park everything else with source, reason, prerequisite, and revisit
condition.

Format specifications for every artifact type live in
`wiki\authoring-standards.md`. Load it when creating pages; do not restate it
here.

## Learning profile

Canonical profile: `00-BRAIN\CHRIS_CORE.md § How Chris Learns Best`. Local
applications:

- Every new term creates or updates a glossary entry plus flashcard Q/A.
- Visual structure and physical-world anchors help; use them.
- Teach tool selection — when to use which construct — alongside mechanics.
- In CONVERGE mode, flag an advanced tangent once and offer to park it; follow
  it only when Chris explicitly redirects.

Primary bottlenecks, and the reason the drill/glossary apparatus exists:
vocabulary retention, knowing when to use each construct, loop construction,
parameters and return values, and reading tracebacks.

## Academic integrity

CSE 1321 and CSE 1321L are `ai-restricted`. Both official Fall 2026 syllabi
explicitly prohibit submitted work created or assisted by generative AI.

AI MAY teach concepts, build fresh ungraded practice, and review Chris's
reasoning. AI MUST NOT draft, solve, rewrite, or debug submitted coursework,
and MUST NOT transform a live assignment prompt into "practice." When graded
status is unclear, stop and ask. Never paste a live course prompt or course
code into AI for debugging.

Vibe coding and AI-generated implementation are out of scope for this hub and
can never count as learner proof. The goal is to prepare Chris's brain, not to
submit work for him.

Evidence and course controls: `wiki\syllabus-alignment.md`.

## Raw boundary

`raw\` is immutable. AI MUST NOT create, edit, move, rename, reorganize,
archive, or delete anything under it without Chris explicitly authorizing a
named exception. Extracted material goes to `wiki\`.

## Shared wiki rules

Raw immutability, large-source chunking, session start/close minimums,
update-over-create, contradiction flagging, recency markers, and the lint pass
are defined once in `00-BRAIN\AGENT.md § Wiki Shared Layer`. This wiki's
expanded protocols live in `wiki\protocols.md` and supersede the shared
minimums when running full sessions.

## Proof

Proof is a completed drill, a working mini-project, a correct cold explain-back,
or real use — demonstrated independently by Chris.

Generated content is not studied content. A built packet is content readiness,
not learner progress. Exposure is not mastery. `wiki\current-position.md` moves
only from independent performance.

## Close

Update `wiki\log.md`. Update `wiki\index.md`, `wiki\current-position.md`, and
`wiki\learning-path.md` only where their state actually changed. Add glossary
and flashcard entries for new terms. State the exact next action in one line.

A change is complete when navigation resolves, the log records the operation,
learner truth is not duplicated outside `current-position.md`, and a fresh
session can retrieve the frontier without oral history.

## Final operating principle

Protect the beginner path. A clean path beats a large vault.

Chris should never open this wiki and wonder what to read next.
