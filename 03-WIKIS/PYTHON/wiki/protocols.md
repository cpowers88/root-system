---
type: reference
tags: [reference, programming, governance]
---

# Session & Intake Protocols — Python Wiki
### Moved out of CLAUDE.md July 11, 2026 (slim pass). The always-on OS keeps the session minimums; the expanded protocols live here.
### Load this page when running a SOURCE INTAKE, a SYLLABUS INGEST, or a full teaching session. These expand (and supersede) the AGENT.md § Wiki Shared Layer minimums for this wiki.

---

## Session Start Protocol (expanded)

At the start of every meaningful session, read these files first:

1. `wiki/current-position.md`
2. `wiki/learning-path.md`
3. `wiki/source-map.md`
4. `wiki/glossary/index.md` if present, otherwise `wiki/glossary/README.md`
5. `wiki/parking-lot.md`
6. Last 3 entries in `wiki/log.md`

Then state:

```text
Current stage:
Current concept:
Next reading:
Next drill:
Vocabulary due for review:
Blocked by:
Parked advanced material:
```

Do not start by reading random source pages. Do not jump to advanced topics unless Chris explicitly asks.

---

## Multi-Source Intake Protocol

When Chris provides many books, docs, or syllabi at once, do **not** deep-summarize everything immediately.

Run the intake in this order:

1. Inventory all sources.
2. Create or update `wiki/source-map.md`.
3. For each source, identify:
   - title
   - author/source
   - source type
   - difficulty level
   - best use
   - beginner usefulness
   - school-readiness usefulness
   - computer-science usefulness
   - Python syntax usefulness
   - application/project usefulness
   - advanced material to park
   - recommended role in the pathway
4. Identify overlapping topics across sources.
5. Identify missing prerequisites.
6. Select one primary spine source for the current phase.
7. Select support sources per phase.
8. Build or update `wiki/learning-path.md`.
9. Park advanced material in `wiki/parking-lot.md` and `wiki/parked-advanced/`.
10. Ask Chris for approval before generating large numbers of concept pages.

The correct result of a 10-book intake is **not 10 book summaries**. The correct result is a compiled path.

---

## Source Roles

Every source must be assigned one or more roles:

- `spine` — main teaching path for a stage or phase.
- `support` — clarifies a concept when the spine is weak.
- `practice` — provides exercises, drills, or examples.
- `reference` — lookup material, not primary reading.
- `advanced` — useful later, not for current stage.
- `school-policy` — syllabus/policy/timeline only.
- `capability-map` — expands what code can solve.
- `project-source` — supports mini-projects or capstones.

Only one source can be the active `spine` for a stage unless Chris approves a blended stage.

---

## Learning Path Control (expanded)

`wiki/learning-path.md` is the command center.

It must always answer:

- What stage is Chris currently in?
- What concept comes next?
- What source supports it?
- What page should Chris read next?
- What drill proves the concept?
- What vocabulary must be reviewed first?
- What mini-project is approaching?
- What advanced ideas are parked?
- What must not be touched yet?

Claude must update `learning-path.md` after each meaningful ingest or teaching session.

---

## Syllabus Ingest Rule

When ingesting a syllabus:

1. Extract course policies, AI rules, schedule, topic order, grading categories, required books, due-date patterns, and tools.
2. Do not extract assignment answers.
3. Do not build solutions to labs or projects.
4. Add course topics to `learning-path.md` as alignment constraints.
5. Add policy restrictions to `current-position.md` and `source-map.md`.
6. If AI prohibition exists, mark the course as `ai-restricted`.

---

## End-of-Session Protocol (expanded)

At the end of every meaningful session:

1. Update `wiki/log.md`.
2. Update `wiki/index.md`.
3. Update `wiki/current-position.md` if progress changed.
4. Update `wiki/learning-path.md` if the next step changed.
5. Update glossary and flashcards for new terms.
6. Update `wiki/parking-lot.md` for any advanced or off-scope ideas.
7. State the next action in one sentence.

Append this block to `wiki/log.md`:

```markdown
## YYYY-MM-DD — [session title]

### Work completed

### Pages created/updated

### Vocabulary added

### Drills or projects added

### Progress evidence

### Parked material

### Next action
```
