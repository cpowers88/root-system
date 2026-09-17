---
type: stage
timeline: now
stage_number: 04
status: ready
course_module: "M3 — Functions (lecture Weeks 7-8, Quiz 4; lab Lab 7 + Assignment 4)"
source_spine: "Think Python Ch.3 + Ch.6"
support_sources: ["Automate the Boring Stuff Ch.4", "Python Crash Course Ch.8", "Python Workout Ch.7"]
---

# Stage 04 — Functions, Parameters, and Return Values

## Purpose

Learn to package reusable logic into functions, pass data in with parameters, and get results back out with return values.

> **Scope narrowed 2026-07-25.** The standard-library bridge that used to close this
> stage now lives in [[stages/stage-04b-python-libraries]], because both syllabi
> assess functions (Module 3) and libraries (Module 4) as separate modules with
> separate quizzes and labs. **This stage's gate is functions only** — it can and
> should close without any library work.

## Why This Stage Comes Now

Stages 1-3 gave Chris the raw tools (values, decisions, loops) but every program so far has been one long, flat script. Functions are the first real organizing tool — packaging logic so it can be named, reused, and combined. Every later stage (data structures, program design, OOP) assumes functions are second nature.

## Prerequisites

Stage 3 — `for`/`while` loops, counters, accumulators.

## Concepts To Learn

- [[concepts/defining-and-calling-functions]]
- [[concepts/parameters-and-arguments]]
- [[concepts/return-values]]

## Vocabulary To Add

- [[glossary/function]]
- [[glossary/def]]
- [[glossary/call]]
- [[glossary/parameter]]
- [[glossary/argument]]
- [[glossary/scope]]
- [[glossary/return-value]]
- [[glossary/fruitful-void-function]]

Full flashcard batch: [[flashcards/stage-04-functions]]

## Code-Reading Gate

Read function signatures and call sites before bodies. Trace `caller -> arguments
-> parameters -> local state -> return value -> caller`, then write signatures and
return placeholders before implementing any body.

## Required Code Patterns

- [[code-patterns/function-with-parameter]]
- [[code-patterns/function-with-return-value]]

## Drills

- [[drills/stage-04-function-writing]] — **three functions, each taking one
  parameter**: `fahrenheit_to_celsius(f)` and `is_even(n)` return, `shout(message)`
  prints. It is one undivided drill; there is no no-parameter function in it and no
  first-half/second-half split.
- Extra practice: Python Workout Ch.7 (Functions), physical p.127 — see
  [[source-page-map]].

## Mini-Project

- [[mini-projects/stage-04-function-toolbox]]

## Common Errors Reference

- [[errors/stage-04-common-errors]]

## Read Next

**Total assigned spine reading is about 15 pages, not two chapters.** Physical PDF
pages below — open them directly; full map in [[source-page-map]].

1. Think Python **Ch.3, physical pp. 43–52** — "Function Calls" (43), "Math
   Functions" (44), "Composition" (45), "Adding New Functions" (45), "Definitions
   and Uses" (47), "Flow of Execution" (47), "Parameters and Arguments" (48),
   "Variables and Parameters Are Local" (49), "Stack Diagrams" (50), "Fruitful
   Functions and Void Functions" (51), "Why Functions?" (52).
2. Think Python **Ch.6, physical pp. 83–87** — "Return Values" (83), "Incremental
   Development" (84–85), "Boolean Functions" (87). **Stop at 87.** "More Recursion"
   (88), "Leap of Faith" (90), and "Checking Types" (91) are Stage 8.
3. Automate the Boring Stuff Ch.4 (Functions) — parallel reinforcement; already a
   per-chapter `.md` file, no page math needed.
4. Python Crash Course **Ch.8, physical p. 211** — extra worked examples;
   **skip** arbitrary arguments and arbitrary keyword arguments.

Library reading moved to [[stages/stage-04b-python-libraries]].

## Mastery Checklist

- [ ] Define function, parameter, argument, scope, return value, and fruitful/void function in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a function with a parameter and a return value from memory, without notes.
- [ ] Explain the difference between a parameter and an argument out loud.
- [ ] Explain why a local variable doesn't exist outside its function.
- [ ] Debug at least one of the four error types in [[errors/stage-04-common-errors]] without help.
- [ ] Complete [[drills/stage-04-function-writing]].
- [ ] Complete [[mini-projects/stage-04-function-toolbox]] and explain the solution out loud.

## Stage Mastery Target

Can write a function with a parameter and a return value from memory, and explain when to use `return` versus `print()` inside a function.

## Parked Until Later

- Default parameter values, keyword arguments, `*args`/`**kwargs` — Stage 8-10, as needed.
- Recursion (a function calling itself) — Stage 8.
- Standard-library import and use — [[stages/stage-04b-python-libraries]], the next
  stage, matching the course's Module 4.
- Splitting Chris's own project across multiple modules/files — Stage 9, once
  there is a real maintenance reason.
- Decorators — well beyond this vault's current scope.

## Teaching Method

Run this stage on the loop in [[teaching-loop]] — cold attempt before instruction,
support escalated only as far as the observed error requires, explain-back, fresh
transfer. Adopted 2026-07-25 on the Stage 3 evidence.
