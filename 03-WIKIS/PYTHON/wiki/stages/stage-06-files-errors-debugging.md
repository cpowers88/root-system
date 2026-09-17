---
type: stage
timeline: reference
stage_number: 06
status: ready
source_spine: "Think Python Ch.14, Ch.20"
support_sources: ["Automate the Boring Stuff Ch.5 & 10", "Python Crash Course Ch.10", "Python Workout Ch.6", "Invent Your Own Computer Games Ch.6"]
---

# Stage 06 — Files, Errors, and Debugging

## Purpose

Learn to read and write files, understand exceptions and tracebacks, and debug systematically using the three error categories (syntax, runtime, semantic).

## Why This Stage Comes Now

Every program so far has lived and died within a single run — nothing persists, and every bug so far has been small enough to spot by eye. Real programs save data to files and inevitably break in ways that aren't obvious. This stage gives Chris his first systematic process for both.

## Prerequisites

Stage 5 — lists, dictionaries, tuples, sets.

## Concepts To Learn

- [[concepts/file-paths-and-reading-writing]]
- [[concepts/exceptions-and-tracebacks]]
- [[concepts/debugging-process]]

## Vocabulary To Add

- [[glossary/file-path]]
- [[glossary/open-read-write-close]]
- [[glossary/exception]]
- [[glossary/traceback]]
- [[glossary/try-except]]
- [[glossary/syntax-runtime-semantic-error]]

Full flashcard batch: [[flashcards/stage-06-files-errors-debugging]]

## Course Core vs. Full Stage

Course core is reading tracebacks, distinguishing syntax/runtime/semantic errors,
exception handling, and systematic debugging. File persistence is part of the
full vault stage, but it should not delay the next official course topic when
semester capacity is tight.

## Code-Reading Gate

Read a traceback from the bottom up: exception type and message, failing line,
then the call path. State the last known-good step, the failure boundary, and one
repair hypothesis before editing code.

## Required Code Patterns

- [[code-patterns/file-read-with-context-manager]]
- [[code-patterns/try-except-block]]

## Drills

- [[drills/stage-06-debugging-practice]]
- Extra practice: Python Workout Ch.6 (Files) exercises.

## Mini-Project

- [[mini-projects/stage-06-note-saver]]
- Alternative/extra: Invent Your Own Computer Games Ch.6 (Using the Debugger) for hands-on debugger practice in VS Code, separate from the note-saver project.

## Common Errors Reference

- [[errors/stage-06-common-errors]]

## Read Next

1. Think Python Ch.14 — "Persistence," "Reading and Writing," "Filenames and Paths," "Catching Exceptions." **Skip** "Format Operator," "Databases," "Pickling," "Pipes," "Writing Modules" — those are Stage 9-10 material.
2. Think Python Ch.20 — "Syntax Errors," "Runtime Errors," "Semantic Errors" (the full chapter; it's short and entirely relevant).
3. Automate the Boring Stuff Ch.5 (Debugging) and Ch.10 (Reading and Writing Files) — parallel reinforcement.
4. Python Crash Course Ch.10 (Files and Exceptions) — extra worked examples; **skip** "Storing Data" (JSON) for now — held for Stage 9.
5. Invent Your Own Computer Games Ch.6 — hands-on VS Code debugger walkthrough (breakpoints, stepping through code), a different angle on debugging than reading tracebacks.

## Mastery Checklist

- [ ] Define file path, open/read/write/close, exception, traceback, try/except, and the three error types in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Read a real traceback and correctly identify the failing line and error type without help.
- [ ] Write a `try`/`except` block for a genuinely risky operation, naming a specific exception type (not a bare `except:`).
- [ ] Write a file read/write program using a context manager, from memory.
- [ ] Distinguish a syntax error from a runtime error from a semantic error when shown an example of each.
- [ ] Complete [[drills/stage-06-debugging-practice]].

Full-stage enrichment: complete [[mini-projects/stage-06-note-saver]] and explain
the solution out loud. File persistence does not block the next official course
topic.

## Stage Mastery Target

Can read a traceback, locate the failing line and error type, and either fix the bug or wrap the risky operation in an appropriately specific `try`/`except`.

## Parked Until Later

- JSON/pickling and other serialization formats — Stage 9 (Automation Bridge).
- Databases — Stage 10.
- Custom exception classes, exception chaining, `finally` blocks — beyond this stage's depth, revisit only if a real need comes up.
- Logging (the `logging` module, as opposed to `print()`-based debugging) — Stage 9-10.
