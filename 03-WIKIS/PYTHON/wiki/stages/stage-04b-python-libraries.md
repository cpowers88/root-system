---
type: stage
timeline: next
stage_number: 04b
status: ready
course_module: "M4 — Python Libraries (lecture Week 9, Quiz 5; lab Lab 8)"
source_spine: "Official Python documentation — raw/docs/tutorial/modules.txt"
support_sources: ["Python Workout Ch.9 (modules/packages) — reference only"]
---

# Stage 04b — Python Libraries

## Purpose

Import a standard-library module, call a function through it, and explain the
difference between importing something Python already has and installing
something it doesn't.

## Why this is its own stage

Split out of Stage 4 on 2026-07-25. Both syllabi treat functions and libraries as
**separate modules with separate assessments** — lecture gives Module 3 (functions)
Weeks 7–8 with Quiz 4, then Module 4 (Python Libraries) Week 9 with Quiz 5; lab
gives them Lab 7 and Lab 8. Carrying both in one stage meant Stage 4's gate could
not close on a week that only budgeted functions work, which is exactly the
conflict found in the July 27 weekly plan. One stage, one module, one gate.

## Prerequisites

**Stage 4 (functions) must be closed first.** You cannot judge what a module gives
you until calling a function and using its return value is automatic. This is the
only hard ordering in the pair — the course sequences it the same way.

## Concepts To Learn

- [[concepts/standard-library-basics]]

## Vocabulary To Add

- [[glossary/module]]
- [[glossary/import-statement]]
- [[glossary/standard-library]]

Full flashcard batch: [[flashcards/stage-04-library-basics]]

## Code-Reading Gate

Given an unfamiliar `import`, say what the module name is, what the dot in
`module.function()` is doing, and where the returned value goes — before running
anything.

## Required Code Patterns

- [[code-patterns/import-and-call-standard-library]]

## Drills

- [[drills/stage-04-library-basics]]

## Read Next

1. [[concepts/standard-library-basics]] — the local page first.
2. `raw/docs/tutorial/modules.txt` — section 6 opening and the basic
   `import module` example **only**. This is the official documentation, and
   reading a real doc page is itself the skill the course's library module is
   testing.
3. Official documentation for the one function you actually import (`math.sqrt`,
   `random.randint`) — read it for the input/output contract, not for a tour.

**Do not** survey the standard library. Two modules, used properly, closes this
stage. Packages, `pip`, and third-party installation are Stage 9.

## Mastery Checklist

- [ ] Import one standard-library module and call a function through the module name.
- [ ] Explain the difference between importing and installing, in plain English.
- [ ] Read one official documentation entry and state that function's input/output
  contract without running it.
- [ ] Wrap one library call inside a function of your own, so the rest of the
  program calls your name rather than the library's.
- [ ] Complete [[drills/stage-04-library-basics]].

## Stage Mastery Target

Can reach for a standard-library module when a problem calls for one, read its
documentation for the contract, and hide it behind one named function of your own.

## Parked Until Later

- Third-party packages and `pip` — Stage 9, because dependency management is a
  different skill from using what ships with Python.
- Writing your own importable modules — Stage 9.
- `from x import y` and aliasing forms — introduce only if a drill needs them.

## Teaching Method

Run this stage on the loop in [[teaching-loop]] — cold attempt before instruction,
support escalated only as far as the observed error requires, explain-back, fresh
transfer.
