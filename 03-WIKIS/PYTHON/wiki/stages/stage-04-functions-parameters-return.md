---
type: stage
stage_number: 04
status: ready
priority: upcoming
source_spine: "Think Python Ch.3 + Ch.6"
support_sources: ["Automate the Boring Stuff Ch.4", "Python Crash Course Ch.8", "Python Workout Ch.7"]
---

# Stage 04 — Functions, Parameters, and Return Values

## Purpose

Learn to package reusable logic into functions, pass data in with parameters, and get results back out with return values.

## Why This Stage Comes Now

Stages 1-3 gave Chris the raw tools (values, decisions, loops) but every program so far has been one long, flat script. Functions are the first real organizing tool — packaging logic so it can be named, reused, and combined. Every later stage (data structures, program design, OOP) assumes functions are second nature.

## Prerequisites

Stage 3 — `for`/`while` loops, counters, accumulators.

## Concepts To Learn

- [[concepts/defining-and-calling-functions]]
- [[concepts/parameters-and-arguments]]
- [[concepts/return-values]]
- [[concepts/standard-library-basics]] — short syllabus bridge after functions

## Vocabulary To Add

- [[glossary/function]]
- [[glossary/def]]
- [[glossary/call]]
- [[glossary/parameter]]
- [[glossary/argument]]
- [[glossary/scope]]
- [[glossary/return-value]]
- [[glossary/fruitful-void-function]]
- [[glossary/module]]
- [[glossary/import-statement]]
- [[glossary/standard-library]]

Full flashcard batch: [[flashcards/stage-04-functions]]

## Code-Reading Gate

Read function signatures and call sites before bodies. Trace `caller -> arguments
-> parameters -> local state -> return value -> caller`, then write signatures and
return placeholders before implementing any body.

## Required Code Patterns

- [[code-patterns/function-with-parameter]]
- [[code-patterns/function-with-return-value]]
- [[code-patterns/import-and-call-standard-library]]

## Drills

- [[drills/stage-04-function-writing]]
- [[drills/stage-04-library-basics]] — complete after the function drill
- Extra practice: Python Workout Ch.7 (Functions) exercises.

## Mini-Project

- [[mini-projects/stage-04-function-toolbox]]

## Common Errors Reference

- [[errors/stage-04-common-errors]]

## Read Next

1. Think Python Ch.3 — "Function Calls," "Math Functions," "Composition," "Adding New Functions," "Definitions and Uses," "Flow of Execution," "Parameters and Arguments," "Variables and Parameters Are Local," "Stack Diagrams," "Fruitful Functions and Void Functions," "Why Functions?"
2. Think Python Ch.6 — "Return Values," "Incremental Development," "Composition," "Boolean Functions." **Skip** "More Recursion," "Leap of Faith," "One More Example," "Checking Types" — those lean into recursion (Stage 8) and type-checking depth not needed yet.
3. Automate the Boring Stuff Ch.4 (Functions) — parallel reinforcement.
4. Python Crash Course Ch.8 (Functions) — extra worked examples and exercises; **skip** arbitrary arguments and arbitrary keyword arguments.
5. [[concepts/standard-library-basics]] plus `raw/DOCS/tutorial/modules.txt`, section 6 opening and the basic `import module` example only. This is the syllabus's Python Libraries bridge; packages and `pip` stay in Stage 9.

## Mastery Checklist

- [ ] Define function, parameter, argument, scope, return value, and fruitful/void function in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a function with a parameter and a return value from memory, without notes.
- [ ] Explain the difference between a parameter and an argument out loud.
- [ ] Explain why a local variable doesn't exist outside its function.
- [ ] Debug at least one of the four error types in [[errors/stage-04-common-errors]] without help.
- [ ] Complete [[drills/stage-04-function-writing]].
- [ ] Import one standard-library module, call a function through the module name,
  and explain import vs. installation.
- [ ] Complete [[drills/stage-04-library-basics]].
- [ ] Complete [[mini-projects/stage-04-function-toolbox]] and explain the solution out loud.

## Stage Mastery Target

Can write a function with a parameter and a return value from memory, and explain when to use `return` versus `print()` inside a function.

## Parked Until Later

- Default parameter values, keyword arguments, `*args`/`**kwargs` — Stage 8-10, as needed.
- Recursion (a function calling itself) — Stage 8.
- Splitting Chris's own project across multiple modules/files — Stage 9, once
  there is a real maintenance reason. Basic standard-library import/use is part of
  this stage because both course calendars place Python Libraries after functions.
- Decorators — well beyond this vault's current scope.
