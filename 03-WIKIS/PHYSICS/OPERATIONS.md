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
  source: physical situation (named fast, assumed known — see Teaching contract)
  sequence: calculus relationship -> formula derivation -> physical mapping -> problem type -> example -> drill
  gate: independent mastery check, immediate + 48-72h durability

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
| PHYSICS canonical syllabus evidence | `raw/syllabus/` |
| Cross-course source status and noncanonical school references | `02-LIBRARY/00-SCHOOL/SYLLABUS_STATUS.md` |
| Learner truth and mastery evidence | `wiki/current-position.md` |
| Syllabus-controlled execution path and durable stage packets | `wiki/learning-path.md` |
| Semester reading and pacing triggers | `wiki/pacing-trigger-map.md` |
| Source roles and verification | `wiki/source-map.md` |
| Page specifications and expanded protocols | `wiki/authoring-standards.md` |
| Current cross-system sequencing | CASTLE and `NOW.md` |

authority_rules:
  - Official exact-section material overrides every derivative page.
  - Until Chris says otherwise, `raw/syllabus/PHYS 2211 51 (83719) Principles of
    Physics I.md` controls the preparation topic path because it matches the Fall
    term and instructor on Chris's registration paperwork. (Renamed 2026-08-08
    when Chris removed the duplicate "Best copy" capture; schedule verified
    identical.)
  - Its section number, CRN, deadlines, grading, and instructor-specific policy
    remain nonbinding for Section 54.
  - When its topic label and printed chapter number disagree, the topic label
    controls and Serway's table of contents identifies the correct chapter.
  - The textbook supplies explanations, derivations, examples, and practice in
    the syllabus order; textbook order does not independently control sequencing.
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
2. Name the physical situation in one line — assumed known, not built up
   (Chris has prior Physics 1/2; see Teaching contract).
3. State the calculus relationship first, then derive the equation from it.
4. Define every variable and unit; state assumptions, fast.
5. Teach as calculus construction -> worked pattern -> fresh drill -> explain-back.
6. End with one exact independent action.

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

### Calculus construction leads; physics is assumed, not taught (revised 2026-07-30, Chris-directed)

Chris has already completed introductory Physics 1/2 and Calculus 1/2. He
knows the physics — free-body diagrams, energy, momentum, the conceptual
model behind every topic in this course. That is not what's missing, and
this hub does not re-teach it by default. What's missing, and what this
contract now leads with, is **calculus mechanics and formula construction**.

> Go straight to the calculus: identify the relationship, derive the
> formula, connect it to the physics Chris already has, then apply it.
> Do not rebuild the physical concept from zero on the way there.

This replaces the older "explain the physical situation, then arrive at the
calculus eventually" sequencing (previously step 9 of 12 in this file). PHYS
2211 is a calculus-based course; calculus is not a late-arriving support
layer, it is the point, for every topic across the full Stage 1-18 sequence.

**Standard rep, every calculus-bearing topic (most of the semester):**

1. Name the physical system in one line — what's changing or accumulating,
   with respect to what. A fast anchor, not a build-up: do not walk through
   system boundary, objects involved, and a diagram as separate preliminary
   steps. If Chris can't place it in one line, that's the signal to use the
   Fallback below — expect this rarely, not by default.
2. State the calculus relationship explicitly — the derivative, integral, or
   differential equation, named plainly. Never skipped; this is the actual
   content of a calculus-based course, not optional ceremony.
3. Derive the formula symbolically from that relationship, term by term.
4. **Explain the connection** — what each calculus term and operation
   physically means and why, in real depth, every time. This step is not
   fast-tracked like steps 1 and 2: the physics is solid and the calculus
   mechanics are solid, but the *bridge between them* — why this derivative
   is this physical quantity — is the actual identified gap (Chris's own
   words: "connecting to the physics is still hazy, and needs explaining as
   we go"). Give it real explanation every rep; do not assume it's obvious
   just because the two halves it connects are.
5. Work two to three problems applying the derived formula.
6. **Immediate check** — quiz cold, same session, no notes, no worked
   example open. Proves present understanding, not durable recall.
7. **Durability check, 48-72 hours later** — reconstruct the relationship or
   solve a transfer problem cold. This is the check that actually counts for
   advancement; an immediate pass alone does not.

**Escalation, not a separate default track:** if either check misses, go
deeper — a full boundary-condition/assumption walkthrough, an additional
worked example, another durability check after the repair. If both pass,
move on. Depth is earned by a demonstrated miss, not spent by default on
every topic — this keeps 16 weeks of material moving without turning every
formula into a lecture. `wiki/math-readiness-path.md`'s cold-redo nights
(spaced ~2 days after first exposure) are this durability check already
built into the pre-semester schedule.

**Rust, not a gap (clarified 2026-07-30):** the calculus mechanics
themselves (power rule, boundary conditions, and so on) get the same
treatment as the physics — Chris has completed Calc 1/2, so this is recall
of disused material, not new learning. State each rule in one line; do not
derive it from first principles (no proving the power rule from limits)
unless a cold check shows it's genuinely gone, not just rusty. Once stated,
recognition comes back fast — today's live session proved this directly:
one line each on the derivative and integral power rules, and correct
application followed within the same exchange. Pace the whole sequence for
someone reactivating known material, not encountering it for the first
time.

**Three separate things, three separate paces (named explicitly 2026-07-30
so this doesn't get re-blurred later):**

| Piece | State | Pace |
|---|---|---|
| Physics concepts (forces, energy, motion) | Chris already has these | Assumed; fallback only on a demonstrated miss |
| Calculus mechanics (the rules themselves) | Rusty, not missing | Stated in one line; fast recall, not derived from first principles |
| **The connection between them** | **The actual identified gap** | **Real explanation, every rep — never fast-tracked** |

Conflating any two of these rows is what produced today's earlier drafts of
this contract — pace each one correctly, not uniformly.

**Fallback — physics-concept teaching:** use only if a cold check shows the
physical concept itself, not just the calculus, is actually missing. Then
build the physical situation properly (system, diagram, knowns/unknowns,
governing principle) before returning to the calculus-led sequence above.
This is the exception path. Most of this course is physics Chris already
has; the job is building the math on top of it, not teaching it from
underneath again.

The iPad stays the diagram/first-attempt surface
(`wiki/ipad-handwritten-physics-method.md`); Markdown is the shared
derivation and reasoning surface once the sketch exists — Markdown never
replaces the spatial work. Units and dimensional reasoning stay mandatory
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
reorganize, archive, or delete anything under it unless Chris explicitly
authorizes the named exception. PHYSICS syllabus evidence is canonical there;
derived work belongs in `wiki/`.

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
