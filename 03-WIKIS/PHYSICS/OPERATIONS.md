---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [physics, school, governance]
created: 2026-07-24
---

# PHYSICS_WIKI — OPERATIONS

## Function

Convert verified syllabi, textbook material, lecture notes, examples, and
approved resources into a sequential calculus-based physics learning engine.

control_question: What physical situation is present, what model applies, and what should Chris independently practice next?

pipeline:
  source: physical situation
  sequence: model -> quantities -> diagram -> equation -> units -> calculus connection -> problem type -> example -> drill
  gate: independent mastery check

This hub is not a chapter-summary collection. Packet generation never advances
the learner frontier.

## Lifespan

| Layer | Contents | Lifespan |
|---|---|---|
| durable_spine | stages, concepts, equations, calculus links, problem types, examples, drills, glossary, flashcards, errors, math support | Permanent physics and engineering capability |
| course_overlay | syllabus coverage, pacing triggers, exact-section facts, course-bound current-position entries, `raw/syllabus/` | Replaced and archived when the course changes |

PHYS 2211 is the current consumer of the durable spine, not the reason the hub
exists.

## Authority

| Owns | Authority |
|---|---|
| Permanent direction and AI limits | `01-NORTH_STAR/NORTH_STAR.md` |
| Fall 2026 readiness and outcomes | `01-NORTH_STAR/Goals & Milestones/fall_2026_semester.md` |
| Official syllabi, assignments, notes, and records | `02-LIBRARY/00-SCHOOL/` |
| Cross-course source status | `02-LIBRARY/00-SCHOOL/SYLLABUS_STATUS.md` |
| Learner truth and mastery evidence | `wiki/current-position.md` |
| Durable 18-stage sequence | `wiki/learning-path.md` |
| Semester reading and pacing triggers | `wiki/pacing-trigger-map.md` |
| Source roles and verification | `wiki/source-map.md` |
| Page specifications and expanded protocols | `wiki/authoring-standards.md` |
| Current cross-system sequencing | CASTLE and `NOW.md` |

authority_rules:
  - Official exact-section material overrides every derivative page.
  - Neighbor-section evidence is provisional and cannot control deadlines, grading, instructor policy, or AI use.
  - No page may claim mastery Chris did not demonstrate independently.
  - Do not duplicate learner truth outside `wiki/current-position.md`.

## Boundary

owns:
  - sequential physics learning
  - equations with assumptions, variables, and units
  - calculus in physical context
  - problem recognition and solving patterns
  - independent drills and mastery evidence

routes_out:
  general_course_support: `03-WIKIS/EDUCATION/`
  programming: `03-WIKIS/PYTHON/`
  systems_and_isye: `03-WIKIS/SYSTEMS/`
  business_translation: CASTLE then `03-WIKIS/BUSINESS/`

This hub runs the TEACH stage of the System Loop and its bounded
`raw -> wiki` STRUCTURE intake. Proof returns through the canonical Return
Packet. Do not define a competing loop.

## Structure

```text
raw/                         immutable evidence
templates/                   artifact skeletons
wiki/
  index.md                   navigation map
  log.md                     append-only operational record
  current-position.md        sole learner-truth authority
  learning-path.md           durable Stage 1-18 sequence
  pacing-trigger-map.md      course-overlay timing
  source-map.md              source inventory and roles
  syllabus-coverage-ledger.md
  concept-map.md equation-map.md calculus-map.md problem-type-map.md
  math-readiness-path.md units-and-dimensions.md parking-lot.md
  authoring-standards.md      page formats and expanded protocols
  stages/ concepts/ equations/ calculus-links/ problem-types/
  worked-examples/ drills/ glossary/ flashcards/ diagrams/
  common-errors/ parked-advanced/ appendix/
```

Folder names are stable. Do not rename or restructure without Chris's explicit
approval. Do not prebuild empty structure.

## Operations

### INGEST

1. State the exact learning or verification gap.
2. Identify the authoritative source, section, date, and role.
3. Check exact-section status and academic-integrity constraints.
4. Process large sources in bounded chunks; record coverage.
5. Update `source-map.md` before deep extraction.
6. Update existing pages before creating new pages.
7. Separate verified fact, provisional mapping, inference, and unknown.
8. Cite extracted claims with source and page/section.
9. Generate only the current-stage packet unless Chris authorizes broader work.
10. Update required maps/indexes and append `wiki/log.md`.

### QUERY

1. Read `wiki/current-position.md` and the active stage.
2. Identify situation, system boundary, knowns, unknowns, and diagram.
3. Select the governing physical principle before selecting an equation.
4. Define every variable and unit; state assumptions.
5. Explain calculus only where it represents physical change or accumulation.
6. Teach as explanation -> worked pattern -> fresh drill -> explain-back.
7. End with one exact independent action.

### LINT

Check:
  - official-source precedence and stale course facts
  - neighbor-section claims presented as exact-section truth
  - unresolved links, planned-page classification, and index drift
  - equations missing variables, units, assumptions, or use conditions
  - concepts without problem recognition or practice
  - generated content presented as learner progress
  - current-position contradictions
  - material that outran prerequisites
  - raw-boundary violations

## Teaching contract

For every active topic, answer:

1. What physical situation is happening?
2. What system and objects are involved?
3. What quantities change?
4. What governing model applies, and why?
5. What diagram represents it?
6. What equation follows from the model?
7. What do the variables and units mean?
8. What assumptions limit the equation?
9. What calculus meaning appears?
10. What problem type is this?
11. What beginner error is likely?
12. What independent practice comes next?

Use physical anchors, short explanations, visible sequence, and
beginner-readable vocabulary. Units and dimensional reasoning are mandatory
whenever an equation appears.

## Mastery

proof:
  - correct cold classification of the physical situation
  - independently drawn or described diagram
  - justified model and equation choice
  - correct variables, units, assumptions, and reasonableness check
  - representative problem solved independently
  - correct explain-back without notes

nonproof:
  - page creation
  - reading or recognition alone
  - generated packets
  - copied examples
  - AI-assisted execution

Advance a stage only when its checklist is independently satisfied and recorded
in `wiki/current-position.md`.

## Academic integrity

AI MAY explain concepts, generate fresh private practice, and review Chris's
reasoning where course policy permits.

AI MUST NOT draft, solve, rewrite, or debug prohibited submitted coursework.
Do not transform a live assignment or graded problem into nominal "practice."
When graded status, source ownership, or policy is unclear, stop and ask Chris.

Until the exact PHYS 2211 Section 54 policy is verified, treat neighbor-section
policy as provisional and use the more restrictive safe boundary.

## Raw boundary

`raw/` is immutable evidence. AI MUST NOT create, edit, move, rename,
reorganize, archive, or delete anything under it. Only Chris places files
there. Derived work belongs in `wiki/`.

## Close

1. Append `wiki/log.md`.
2. Update `wiki/current-position.md` only if independent evidence changed.
3. Update index/maps/path only if their owned state changed.
4. Return the local instance of the canonical five-field Return Packet:
   outcome; evidence link; capability/status movement; reusable-asset
   candidate; system-learning candidate.
5. For a learning session, also record the cold performance evidence, error
   class, frontier verdict, and one exact next rep. For a system session,
   record files changed, checks run, and residual risk.
6. Separate **verified**, **inferred**, and **still unknown** claims. Never use
   file creation, packet readiness, or AI-assisted work as learner evidence.
7. Run wiki lint and the canonical root-health gate after governance or
   metadata changes.

### Report quality gate

A session report is not complete unless a fresh reader can answer:

1. What actually changed or was demonstrated?
2. What exact evidence supports that claim?
3. Did learner status move, or explicitly not move?
4. What error or uncertainty remains?
5. What is the one next independent action?

Use exact wiki links or `.ROOT`-relative file paths. Do not report planned work
as completed work, and do not bury the next action under a file inventory.

completion_condition: A fresh session can recover authority, active stage, evidence, and next action without oral history.

## Final principle

Aggressive goal. Controlled path.

`situation -> model -> diagram -> equation -> units -> math -> problem type -> independent practice`
