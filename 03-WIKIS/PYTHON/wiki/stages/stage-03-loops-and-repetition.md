---
type: stage
timeline: reference
stage_number: 03
status: active
source_spine: "Think Python Ch.7 (+ for-loop section pulled forward from Ch.8)"
support_sources: ["Automate the Boring Stuff Ch.3", "Python Crash Course Ch.4 & 7", "Invent Your Own Computer Games Ch.3"]
---

# Stage 03 — Loops and Repetition

## Purpose

Learn how a program repeats work: `for` loops, `while` loops, `range()`, counters, accumulators, `break`, `continue`, and loop tracing.

## Why This Stage Comes Now

Stage 2 gave Chris branching, but every program so far still runs each line exactly once. Loops are what let a program do real repetitive work — and they're the foundation every later stage (functions that loop internally, processing lists, automation scripts) depends on.

## Prerequisites

Stage 2 — comparisons, Boolean logic, `if`/`elif`/`else`.

## Concepts To Learn

- [[concepts/for-loops]]
- [[concepts/while-loops]]
- [[concepts/counters-and-accumulators]]
- [[concepts/modulo-and-divisibility]]

## Vocabulary To Add

- [[glossary/loop]]
- [[glossary/iteration]]
- [[glossary/for-loop]]
- [[glossary/range]]
- [[glossary/while-loop]]
- [[glossary/counter]]
- [[glossary/accumulator]]
- [[glossary/break-continue]]
- [[glossary/infinite-loop]]
- [[glossary/modulo-operator]]

Full flashcard batch: [[flashcards/stage-03-repetition]]

## Code-Reading Gate

Trace `initial state -> condition or next item -> body -> update -> exit`. Use a
table with one row per iteration, predict the final values and output before
running, then reduce the solution to a loop skeleton before implementing it.

## Required Code Patterns

- [[code-patterns/for-loop-over-range]]
- [[code-patterns/while-loop-until-condition]]

## Drills

- [[drills/stage-03-loop-tracing]]
- Extra practice: Python Crash Course Ch.4 exercises (4-1 through 4-15) and Ch.7 exercises (7-1 through 7-10).

## Mini-Project

- [[mini-projects/stage-03-guessing-game-with-attempts]]
- Alternative/extra: revisit Invent Your Own Computer Games Ch.3 (Guess the Number) now with its full looping version — this was capped at one guess in Stage 2; now it can use a real `while` loop.

## Common Errors Reference

- [[errors/stage-03-common-errors]]

## Read Next

1. Think Python Ch.7 — "Reassignment," "Updating Variables," "The while Statement," "break," "Square Roots" (optional), "Algorithms." **Skip** nothing else in this chapter — it's all Stage 3 material.
2. Think Python Ch.8 — read only "A String Is a Sequence," "len," and "Traversal with a for Loop." Skip the rest of Ch.8 (slicing, immutability, searching) — that's Stage 5.
3. Automate the Boring Stuff Ch.3 (Loops) — parallel reinforcement.
4. Python Crash Course Ch.4 (Working with Lists — read only the looping sections, skip list-specific content) and Ch.7 (User Input and while Loops).

## Mastery Checklist

- [ ] Define loop, iteration, for loop, while loop, range, counter, accumulator, break, continue, and infinite loop in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Trace a loop's output by hand correctly before running it.
- [ ] Write a counter loop and an accumulator loop from memory, without notes.
- [ ] Explain when to choose `for` vs. `while`.
- [ ] Debug at least one of the four error types in [[errors/stage-03-common-errors]] without help.
- [ ] Complete [[drills/stage-03-loop-tracing]].
- [ ] Complete [[mini-projects/stage-03-guessing-game-with-attempts]] and explain the solution out loud.

## Stage Mastery Target

Can write and correctly trace simple `for` and `while` loops — including counters and accumulators — from memory, without copying a pattern from notes.

## Parked Until Later

- Looping over lists and dictionaries directly (beyond strings/`range()`) — Stage 5, once those data shapes exist.
- Nested loops over complex/multi-dimensional data — Stage 5+.
- Recursion as an alternative to looping — Stage 8.
- List comprehensions (a compact loop-like syntax) — Stage 10 (Python Workout Ch.8 / Think Python's "Goodies" chapter).
