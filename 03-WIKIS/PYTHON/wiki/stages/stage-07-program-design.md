---
type: stage
stage_number: 07
status: ready
priority: upcoming
source_spine: "Think Python Ch.4, Ch.9, Ch.13 (Case Studies)"
support_sources: ["Invent Your Own Computer Games Ch.7", "Think Like a Programmer Ch.1 (strategy/discussion only)"]
---

# Stage 07 — Program Design

## Purpose

Learn to plan before coding: decomposition, pseudocode, flowcharts, incremental development, and testing.

## Why This Stage Comes Now

Stages 1-6 gave Chris every syntax tool he needs for genuinely useful programs — but every mini-project so far has been small enough to hold in his head at once. Real problems (and the mini-projects from here on) are bigger than that. This stage is the one explicitly about *not* writing code as the first step.

The official lecture introduces decomposition, algorithms, and abstraction in its
first week. The path therefore uses a tiny plan-before-code habit in earlier
stages; Stage 7 is where that habit becomes a full, independently tested skill.

## Prerequisites

Stage 6 — files, exceptions, debugging process.

## Concepts To Learn

- [[concepts/decomposition-and-pseudocode]]
- [[concepts/flowcharts]]
- [[concepts/incremental-development-and-testing]]

## Vocabulary To Add

- [[glossary/decomposition]]
- [[glossary/pseudocode]]
- [[glossary/flowchart]]
- [[glossary/algorithm]]
- [[glossary/test-case]]
- [[glossary/incremental-development]]

Full flashcard batch: [[flashcards/stage-07-program-design]]

## Code-Reading Gate

Extract the program's inputs, outputs, assumptions, major steps, and tests before
reading implementation detail. Explain the control and data flow in plain English,
then produce pseudocode and function signatures before writing bodies.

## Required Code Patterns

None new this stage — Stage 7 is a process skill applied across every pattern already learned in Stages 1-6.

## Drills

- [[drills/stage-07-decompose-a-problem]]

## Mini-Project

- [[mini-projects/stage-07-plan-and-build]] — note this one is intentionally open-ended; Chris picks the problem.

## Common Errors Reference

- [[errors/stage-07-common-errors]] (process mistakes, not Python tracebacks, this time)

## Read Next

1. Think Python Ch.4 — "A Development Plan" specifically (the rest of Ch.4 is the turtle-graphics case study itself; read it as a worked example of decomposition in action, not for the turtle syntax).
2. Think Python Ch.9 and Ch.13 — read as worked examples of incremental development and case studies, not for deep technical content (word play and data structure selection details are Stage 8 territory).
3. Invent Your Own Computer Games Ch.7 — "Designing Hangman with Flowcharts," the direct model for this stage's flowchart concept.
4. Think Like a Programmer, Ch.1 ("Strategies for Problem Solving") — read for the problem-solving narrative only. **Do not read or use the C++ code examples** — translate the reasoning into your own Python-shaped pseudocode instead. See `wiki/parking-lot.md` for why.

## Mastery Checklist

- [ ] Define decomposition, pseudocode, flowchart, algorithm, test case, and incremental development in plain English.
- [ ] Recognize each of these when looking at a planning document or worked example.
- [ ] Take a brand-new plain-English problem and decompose it into concrete steps on paper, without help.
- [ ] Draw a simple flowchart for a problem with 2-3 decision points.
- [ ] Build a program incrementally, confirming each added piece before moving to the next.
- [ ] Write test cases *before* coding, and check the finished program against them.
- [ ] State the program's inputs, expected outputs, assumptions, and one failure
  mode before coding; explain how correctness prevents unsafe or misleading output.
- [ ] Complete [[drills/stage-07-decompose-a-problem]].
- [ ] Complete [[mini-projects/stage-07-plan-and-build]] and explain the solution out loud, including one place where the plan was tested by reality.

## Stage Mastery Target

Can take a new plain-English problem, decompose it into steps on paper first, and build it incrementally — without skipping straight to code.

## Parked Until Later

- Formal software engineering methodology (Agile, Scrum, etc.) — not relevant at this scale.
- Design patterns (reusable software architecture templates) — well beyond this vault's current scope.
- Unit testing frameworks (`pytest`) as a formal practice — Stage 10 (Python Crash Course Ch.11 covers this directly); Stage 7's "test case" is the informal, by-hand version of the same idea.
