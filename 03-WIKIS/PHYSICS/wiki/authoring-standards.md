---
type: reference
timeline: reference
tags: [physics, governance]
---

# Authoring Standards & Protocols — Physics Wiki
### Moved out of CLAUDE.md July 11, 2026 (slim pass). Load when CREATING or RESTRUCTURING pages or running a source intake — not needed for teaching/reading sessions.

---

## Core Wiki Files — what each must do

### `wiki/learning-path.md`
The master staged path. It must tell Chris what to study next.
Each stage/unit must include goal, source alignment, syllabus alignment, prerequisites, vocabulary, equations, variables and units, diagrams, calculus connections, problem types, worked examples, drills, common errors, mastery checklist, do-not-move-on-until criteria, and parked advanced topics.

### `wiki/source-map.md`
Tracks every source and its best use.

### `wiki/concept-map.md`
Maps concepts and dependencies.

### `wiki/equation-map.md`
Maps equations by chapter/unit, variables, units, assumptions, and problem type.

### `wiki/calculus-map.md`
Explains every derivative, integral, vector, slope, area, rate, or limit idea required for physics.

### `wiki/problem-type-map.md`
Classifies physics problems by recognition pattern and solving method.

### `wiki/units-and-dimensions.md`
Tracks SI units, derived units, unit conversions, and dimensional-analysis rules.

### `wiki/parking-lot.md`
Parks material that is valid but not needed yet.

---

## Page Types

Every new page starts with metadata v2 frontmatter containing at least
`type:`, exactly one `timeline:` value, and categorical `tags:` where useful.
Use independent `stage:` and `status:` properties when needed; never encode
those controls as tags.

### Concept Page
Use for physical ideas: displacement, velocity, acceleration, force, energy, momentum, fields, waves, etc.
Must answer what it is, real situation, objects/system, changing quantities, model/equation, variables, units, calculus connection, diagram, problem type, beginner mistake, and practice next.

### Equation Page
Use for formulas. Must answer equation, plain-English meaning, variables, units, when to use, when not to use, assumptions, calculus origin, example problem type, and common mistake.

### Problem-Type Page
Use for recognizers and solving patterns. Must answer how to recognize it, given information, unknown requested, diagram, equations, solving pattern, unit checks, traps, and drills.

### Calculus-Link Page
Use when physics requires calculus. Must answer physics idea, calculus idea, plain-English connection, symbol meaning, small example, course location, and common mistake.

---

## Stage Packet Requirements

Each stage/unit packet must include, as needed: stage overview, concept pages, equation pages, problem-type pages, calculus links, glossary entries, flashcards, worked examples, drills, common errors, and mastery checklist.

Do not overbuild. Generate only what supports the current stage unless Chris asks.

---

## Beginner-Readable Writing Rules

- Use short paragraphs.
- Use direct headings.
- Avoid textbook haze.
- Use one idea per section.
- Define terms before using them heavily.
- Use diagrams or diagram descriptions when helpful.
- Use units every time an equation is introduced.
- Explain why an equation applies, not just how to plug numbers in.
- Distinguish concept understanding from algebra manipulation.
- Include physical-world anchors.

---

## Source Intake Protocol (expanded)

When Chris adds syllabus, textbook, or other material to `raw/`:

1. Do not deep-summarize everything immediately.
2. First update `wiki/source-map.md`.
3. Classify each source by role, difficulty, best use, chapters/sections, syllabus relevance, calculus relevance, problem-solving relevance, and what to park.
4. Build or update `wiki/learning-path.md`.
5. Build or update `concept-map.md`, `equation-map.md`, `calculus-map.md`, `problem-type-map.md`, and `units-and-dimensions.md`.
6. Generate only the current unit/stage packet unless Chris asks for more.

### Required Source Roles

- `spine` — primary textbook or syllabus-driven path
- `support` — clarifies difficult concepts
- `equation-reference` — formulas, variables, units, assumptions
- `problem-practice` — drills and worked examples
- `visual-support` — diagrams, simulations, animations, graphing
- `calculus-support` — math bridge for derivatives, integrals, vectors, rates
- `parked-advanced` — useful later, too advanced now

---

## Session Protocols (expanded)

**Start of session:** read `OPERATIONS.md`, `wiki/index.md`, most recent `wiki/log.md` entries, `wiki/learning-path.md`, `wiki/current-position.md`; state the one-session objective in one sentence; do not duplicate pages already present.

**End of session:** use the local instance of the canonical Return Packet from
`01-NORTH_STAR/System Contracts/ROOT_CAPABILITY_CONTRACT.md`. Update
`wiki/index.md` only when navigation changed, update `wiki/current-position.md`
only when independent learner evidence changed, and append `wiki/log.md`.
Lead with the outcome and evidence; a file inventory is supporting detail, not
the report.

Append to `wiki/log.md` in this format:

```markdown
## YYYY-MM-DD — Session Title

### Outcome
-

### Evidence
-

### Capability/status movement
-

### Errors, uncertainty, or residual risk
-

### Exact next independent rep
-

### Reusable-asset candidate
- Yes/no. If yes, name the proposed owner; do not create it without scope.

### System-learning candidate
- Yes/no. If yes, name the flag or learning nomination.

### Sources and files touched
-
```

For a **learning session**, Evidence must include cold performance, prompting
level, units/model/diagram result, and miss classification. For a **system
session**, Evidence must include files changed and checks run. Write "none" when
a field did not move; never omit the field and leave the reader guessing.
