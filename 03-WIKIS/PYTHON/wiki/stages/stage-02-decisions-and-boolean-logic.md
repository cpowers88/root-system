---
type: stage
timeline: reference
stage_number: 02
status: satisfied
source_spine: "Think Python Ch.5 (non-recursive sections)"
support_sources: ["Automate the Boring Stuff Ch.2", "Python Crash Course Ch.5", "Invent Your Own Computer Games Ch.3, 5"]
---

# Stage 02 — Decisions and Boolean Logic

## Purpose

Learn how a program makes a decision: comparisons, Boolean logic, and `if`/`elif`/`else` branching.

## Why This Stage Comes Now

Stage 1 gave Chris values, variables, and I/O — but every program so far runs the exact same steps no matter what. Decisions are what let a program react differently depending on the situation, and every later stage (loops, functions, data structures) assumes Chris can already branch confidently.

## Prerequisites

Stage 1 — values, variables, expressions, strings, numbers, type conversion, `print()`/`input()`.

## Concepts To Learn

- [[concepts/comparisons-and-boolean-logic]]
- [[concepts/if-elif-else]]

## Vocabulary To Add

- [[glossary/condition]]
- [[glossary/boolean]]
- [[glossary/comparison-operator]]
- [[glossary/boolean-operators]]
- [[glossary/if-elif-else]]
- [[glossary/branch]]
- [[glossary/truthy-falsy]]

Full flashcard batch: [[flashcards/stage-02-decisions]]

## Code-Reading Gate

Read conditions in source order. For each test, record `True` or `False`, identify
the one branch that runs, and predict the output for at least two inputs. Write the
condition-and-branch skeleton before filling in branch bodies.

## Required Code Patterns

- [[code-patterns/if-elif-else-decision-chain]]

## Drills

- [[drills/stage-02-decision-rules]]
- Extra practice: Python Crash Course Ch.5 exercises (5-1 through 5-13).

## Mini-Project

- [[mini-projects/stage-02-choose-your-path-adventure]]
- Alternative/extra: Invent Your Own Computer Games Ch.3 (Guess the Number — note: the book's version uses a loop; for Stage 2, cap it at one guess and treat the multi-guess version as a Stage 3 stretch goal) and Ch.5 (Dragon Realm, the direct inspiration for this stage's mini-project).

Before coding, list the possible inputs and the branch/output each input should
produce. This keeps the course's decomposition habit active without pulling the
full Stage 7 design packet forward.

## Common Errors Reference

- [[errors/stage-02-common-errors]]

## Read Next

1. Think Python Ch.5 — "Boolean Expressions," "Logical Operators," "Conditional Execution," "Alternative Execution," "Chained Conditionals," "Nested Conditionals." **Skip** "Floor Division and Modulus," "Recursion," "Stack Diagrams for Recursive Functions," and "Infinite Recursion" — those are Stage 3 and Stage 8 material.
2. Automate the Boring Stuff Ch.2 (if-else and Flow Control) — parallel reinforcement.
3. Python Crash Course Ch.5 (if Statements) — extra worked examples and exercises.

## Mastery Checklist

- [ ] Define condition, Boolean, comparison operator, `and`/`or`/`not`, branch, and truthy/falsy in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write an `if`/`elif`/`else` chain from memory for a new plain-English rule, without notes.
- [ ] Explain why `elif` is sometimes necessary instead of separate `if` statements.
- [ ] Debug at least one of the four error types in [[errors/stage-02-common-errors]] without help.
- [ ] Complete [[drills/stage-02-decision-rules]].
- [ ] Complete [[mini-projects/stage-02-choose-your-path-adventure]] and explain the solution out loud.

## Stage Mastery Target

Can read a plain-English decision rule and translate it directly into a correct `if`/`elif`/`else` chain, including choosing when to combine conditions with `and`/`or`, without referring back to notes.

## Parked Until Later

- Loops (`for`/`while`) — Stage 3.
- Recursion (Think Python Ch.5's recursion sections) — Stage 8.
- Functions with return values — Stage 4.
- The `is`/`is not` identity operators and the walrus operator (`:=`) — not needed yet, may surface incidentally in error messages; don't drill them.
- Match/case structural pattern matching (a newer Python alternative to long `elif` chains) — too advanced for this stage, revisit once `elif` is second nature.
