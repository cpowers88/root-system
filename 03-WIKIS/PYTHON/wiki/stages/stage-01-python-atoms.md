---
type: stage
stage_number: 01
status: ready
priority: current
source_spine: "Think Python Ch.1-2 (+ input() pulled forward from Ch.5)"
support_sources: ["Automate the Boring Stuff Ch.1", "Python Crash Course Ch.2", "Python Workout Ch.2-3", "Invent Your Own Computer Games Ch.1-2, 4"]
---

# Stage 01 — Python Atoms

## At a Glance
- **Core claim:** every later stage (decisions, loops, functions, data structures) is built entirely out of values, variables, strings, numbers, `print()`/`input()`, and type conversion — this is the load-bearing stage.
- **When to use it:** this is Chris's current active study stage (per `wiki/current-position.md`) — open this page to see what to read, practice, and drill next.
- **Decision/action it supports:** whether to move to Stage 2 — gated by the Mastery Checklist below, not by content existing.
- **Key risk:** treating a generated packet as mastery. Stages 2-10 already have full packets built but are NOT yet studied — don't skip ahead because the content exists.

## Purpose

Learn the smallest building blocks of a Python program: values, expressions, variables, assignment, strings, numbers, `print()`, `input()`, and type conversion.

## Why This Stage Comes Now

Every later stage — decisions, loops, functions, data structures — is built entirely out of these atoms. None of that can be taught safely until Chris can write and read these without hesitation.

## Prerequisites

Stage 0 (create/run a `.py` file in VS Code and terminal) — already met.

## Concepts To Learn

- [[concepts/values-and-expressions]]
- [[concepts/variables-and-assignment]]
- [[concepts/strings]]
- [[concepts/numbers-and-type-conversion]]
- [[concepts/print-and-input]]

## Vocabulary To Add

- [[glossary/value]]
- [[glossary/expression]]
- [[glossary/variable]]
- [[glossary/assignment]]
- [[glossary/string]]
- [[glossary/concatenation]]
- [[glossary/integer]]
- [[glossary/float]]
- glossary/type-conversion
- [[glossary/comment]]
-  glossary/print
- [[glossary/input]]

Full flashcard batch: [[flashcards/stage-01-python-atoms]]

## Required Code Patterns

- [[code-patterns/input-and-type-conversion]]

## Drills

- [[drills/stage-01-input-and-conversion]]
- Extra practice: Python Workout Ch.2 (Numeric Types) and Ch.3 (Strings) exercises.

## Mini-Project

- [[mini-projects/stage-01-about-me-program]]
- Alternative/extra: Invent Your Own Computer Games Ch.1-2 (Interactive Shell, Writing Programs) and Ch.4 (A Joke-Telling Program) for more reps at this level.

## Common Errors Reference

- [[errors/stage-01-common-errors]]

## Read Next

1. Think Python Ch.1 — "Values and Types," "Arithmetic Operators."
2. Think Python Ch.2 — "Assignment Statements," "Variable Names," "Expressions and Statements," "Order of Operations," "String Operations," "Comments."
3. Think Python Ch.5 — "Keyboard Input" section only (pulled forward; skip the rest of Ch.5 for now, it's Stage 2/8 material).
4. Python Crash Course Ch.2 (parallel reinforcement, especially the f-string section under "Using Variables in Strings").

## Mastery Checklist

- [ ] Define value, variable, expression, string, integer, float, and type conversion in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a short program from memory that uses `input()`, converts a type, stores it in a variable, and prints formatted output with an f-string.
- [ ] Explain when to use `int()` vs. `float()` vs. leaving a value as a string.
- [ ] Debug at least one of the four error types in [[errors/stage-01-common-errors]] without help.
- [ ] Complete [[drills/stage-01-input-and-conversion]].
- [ ] Complete [[mini-projects/stage-01-about-me-program]] and explain the solution out loud.

## Stage Mastery Target

Can write small scripts using variables, input, type conversion, and output from memory, without referring back to notes.

## Parked Until Later

- Conditionals (`if`/`elif`/`else`) — Stage 2.
- Loops (`for`/`while`) — Stage 3.
- Functions — Stage 4.
- Lists, dictionaries, tuples, sets — Stage 5.
- Anything involving files, errors handling (`try`/`except`), or debugging tools — Stage 6.
- Escape sequences and string formatting beyond basic f-strings — introduced only as needed, not drilled yet.
