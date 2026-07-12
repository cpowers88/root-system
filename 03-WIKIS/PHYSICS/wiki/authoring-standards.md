---
type: reference
tags: [reference, physics, governance]
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

**Start of session:** read `CLAUDE.md`, `wiki/index.md`, most recent `wiki/log.md` entries, `wiki/learning-path.md`, `wiki/current-position.md`; state the one-session objective in one sentence; do not duplicate pages already present.

**End of session:** update `wiki/index.md` and `wiki/log.md`; confirm what changed; list files created/updated; state the next exact action for Chris; identify blocked items; identify what should be parked.

Append to `wiki/log.md` in this format:

```markdown
## YYYY-MM-DD — Session Title

### Objective
-

### Sources touched
-

### Files created/updated
-

### Concepts/equations/problem types added
-

### Parked material
-

### Next action for Chris
-
```
