---
type: os
timeline: reference
tags: [physics, school]
---

# CLAUDE.md — Physics Education Vault Operating System
### Slimmed July 11, 2026 per the Claude-docs review (flag 64). Full prior version: `99-ARCHIVE\ARCHIVED_2026-07-11_PHYSICS_CLAUDE.md`. Page formats, core-file specs, intake and session protocols → [[authoring-standards]].

## Mission

This vault is a sequential physics education engine for Chris.

It converts syllabi, textbook chapters, lecture notes, examples, and approved study resources into a clear learning path for physics class readiness and long-term engineering competence.

This vault is not a pile of chapter summaries.

The correct output is:

```text
source material → mapped concepts/equations/problem types → staged study path → guided practice → mastery checks
```

## Prime Directive

Any AI teaching physics in this hub must teach it as a sequence of:

```text
physical situation → model → quantities → equation → units → calculus connection → problem type → worked example → drill → mastery check
```

Every page must help Chris answer:

1. What physical situation is happening?
2. What objects or system are involved?
3. What quantities are changing?
4. What model or equation applies?
5. Why does that model apply?
6. What do the variables mean?
7. What are the units?
8. What calculus appears, if any?
9. What diagram should be drawn?
10. What problem type is this?
11. What beginner mistake should be avoided?
12. What should Chris practice next?

## Chris Learning Profile

Canonical profile: `00-BRAIN\CHRIS_CORE.md § How Chris Learns Best` and
§ Key Operating Constraints (spatial/numerical strengths, weak vocabulary
recall, explain-back, physical anchors, skeleton-first). Physics-specific
applications:

- Calculus explained only as it appears in the physics.
- Problem types classified by recognition pattern; worked examples before
  independent drills; mastery checks before moving forward.
- Units and dimensional analysis every time an equation appears.
- Dense textbook sections must be broken up — he may try to go too fast;
  the system keeps the path controlled.

Operating principle:

```text
Aggressive goal. Controlled path.
```

## Shared Wiki Rules

The shared layer for all `03-WIKIS` hubs — raw/ immutability, large-source
chunking, session start/close minimums, update-over-create, contradiction
flagging, recency markers, the lint pass, and the academic-integrity boundary —
lives in `00-BRAIN\AGENT.md § Wiki Shared Layer`. One copy, zero drift.
This wiki's expanded protocols live in [[authoring-standards]] and supersede
the shared minimums when running full sessions.

## Folder Structure

- `raw/` — immutable sources: `syllabus/`, `textbook/`, `lecture-notes/`,
  `problem-guides/`, `examples/`
- `templates/` — page skeletons
- `wiki/` — core files: `index.md`, `log.md`, `current-position.md`,
  `learning-path.md` (the master staged path — must always tell Chris what to
  study next), `source-map.md`, `concept-map.md`, `equation-map.md`,
  `calculus-map.md`, `problem-type-map.md`, `units-and-dimensions.md`,
  `parking-lot.md`, plus subfolders: `stages/ concepts/ equations/
  calculus-links/ problem-types/ worked-examples/ drills/ glossary/
  flashcards/ diagrams/ common-errors/ parked-advanced/`

What each core file must contain, the four page types (concept, equation,
problem-type, calculus-link), stage-packet requirements, writing rules, and
source roles: [[authoring-standards]].

## Session Minimums

- **Start:** read `wiki/index.md`, recent `log.md` entries,
  `learning-path.md`, `current-position.md`; state the one-session objective;
  do not duplicate existing pages.
- **Close:** update `index.md` + `log.md` (format in [[authoring-standards]]),
  list files changed, state Chris's next exact action, park what should be
  parked.
- **Intake:** never deep-summarize everything; source-map first, then path,
  then only the current stage packet. Full protocol: [[authoring-standards]].

## Mastery Standard

A stage is complete only when Chris can define the key terms, identify the
physical situation, choose the correct model/equation, list variables and
units, draw or describe the correct diagram, explain the calculus connection
if present, solve representative problems, check units, identify common
traps, and explain the solution out loud.

Reading alone is not mastery.

## Parking Rules

Park advanced material when it is useful later but blocks current learning.

Parked topics must include topic, source, why parked, prerequisite needed,
likely future stage/unit, and unlock condition.

## Final Operating Principle

Do not make physics look bigger than it is.

Break it into:

```text
situation → model → equation → units → math → problem type → practice
```

The purpose of the vault is to make physics visible, ordered, and learnable.
