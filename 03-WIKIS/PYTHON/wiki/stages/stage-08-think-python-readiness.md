---
type: stage
stage_number: 08
status: ready
priority: upcoming
source_spine: "Think Python Ch.5 (recursion), Ch.15-18 (Classes/Objects), Ch.21 (Algorithms)"
support_sources: ["Python Crash Course Ch.9", "Grokking Algorithms Ch.1-5", "Data Structures & Algorithms Ch.1-9", "Python Workout Ch.10", "Invent Your Own Computer Games Ch.15-16", "Automate the Boring Stuff Ch.9"]
---

# Stage 08 — Algorithms and Data Structures (Beginner Depth)

## Purpose

Learn basic OOP and searching/sorting at the depth both syllabi require, supported
by Big O intuition. Recursion remains useful Think Python/CS enrichment, but it is
not explicitly named in the official Fall 2026 syllabi.

## Why This Stage Comes Now

Stages 1-7 gave Chris every mechanical and design tool needed to write real
programs. Stage 8 is the bridge into deeper computer-science thinking. The course
syllabi directly name OOP and searching/sorting; recursion and formal growth-rate
language are support material selected from the spine and algorithm books.

## Prerequisites

Stage 7 — decomposition, incremental development, testing.

## Concepts To Learn

- [[concepts/recursion]]
- [[concepts/classes-and-objects]]
- [[concepts/big-o-and-algorithm-efficiency]]
- [[concepts/sorting-and-searching]]

## Vocabulary To Add

- [[glossary/recursion]]
- [[glossary/base-case]]
- [[glossary/class]]
- [[glossary/object-instance]]
- [[glossary/attribute]]
- [[glossary/method]]
- [[glossary/big-o]]
- [[glossary/sorting]]
- [[glossary/searching]]
- [[glossary/hash-table]]

Full flashcard batch: [[flashcards/stage-08-algorithms-and-classes]]

## Course Core vs. Full Stage

Course core is classes/objects plus linear search, simple sorting, and dictionary
or hash lookup intuition. Recursion, formal Big O analysis, and regex are useful
enrichment; none should block readiness for the syllabus-named material.

## Code-Reading Gate

For classes, trace `class -> instance -> attributes -> method call -> state/output`.
For algorithms, record the target, current position, comparison, and data change
on each step. Predict linear-search and selection-sort behavior before running.

## Required Code Patterns

- [[code-patterns/recursive-function-with-base-case]]
- [[code-patterns/class-with-init-and-method]]

## Drills

- [[drills/stage-08-algorithms-and-classes-practice]]

## Mini-Project

- [[mini-projects/stage-08-card-collection]]
- Alternative/extra: Invent Your Own Computer Games Ch.15-16 (Reversegam + a basic AI opponent) for more OOP-and-game-logic practice once the core mini-project is done.

## Common Errors Reference

- [[errors/stage-08-common-errors]]

## Read Next

1. Think Python Ch.5 — "Recursion," "Stack Diagrams for Recursive Functions," "Infinite Recursion" (the sections held back from Stage 2).
2. Think Python Ch.15 ("Programmer-Defined Types," "Attributes"), Ch.17 ("The init Method," "Printing Objects" — light read only). **Skip** Ch.16 (Classes and Functions — pure functions, modifiers) and Ch.18 (Inheritance, class diagrams) for now; those are deeper OOP than this stage needs.
3. Think Python Ch.21 — "Order of Growth," "Analysis of Basic Python Operations," "Analysis of Search Algorithms," "Hashtables." Skip the "Glossary" math-notation depth if it feels like too much — the intuition matters more than the formal definitions at this stage.
4. Grokking Algorithms Ch.1 (Introduction), Ch.2 (Selection Sort), Ch.3 (Recursion), Ch.4 (Quicksort — read for intuition, the implementation can be skimmed), Ch.5 (Hash Tables).
5. A Common-Sense Guide to Data Structures and Algorithms Ch.1-3 (Big O) as a second explanation if Grokking Algorithms' framing doesn't click — same caveat as before, code language unconfirmed, read for concept only.
6. Python Crash Course Ch.9 (Classes) — extra worked examples; **skip** "Inheritance" and beyond for now.
7. Automate the Boring Stuff Ch.9 (Regular Expressions) — light intro only; this is the lightest-weight addition this stage, not a deep dive.

## Mastery Checklist

### Course-Core Gate

- [ ] Define class, object/instance, attribute, method, sorting, searching, and hash table in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a simple class with `__init__` and one method from memory, without notes.
- [ ] Trace linear search and one pass of a simple sorting algorithm by hand.
- [ ] Debug at least one of the four error types in [[errors/stage-08-common-errors]] without help.
- [ ] Complete the course-core gate in [[drills/stage-08-algorithms-and-classes-practice]].
- [ ] Complete [[mini-projects/stage-08-card-collection]] and explain the solution out loud.

### Full-Stage Enrichment Gate

- [ ] Define recursion, base case, and Big O in plain English.
- [ ] Trace a recursive function by hand and correctly identify its base case.
- [ ] Estimate whether a short snippet is O(1), O(n), or O(n²), with a one-sentence reason.
- [ ] Complete the optional enrichment parts of [[drills/stage-08-algorithms-and-classes-practice]].

## Stage Mastery Target

Course core: can read and write a simple class, trace linear search and simple
sorting, and explain dictionary/hash lookup intuition. Full-stage enrichment adds
recursion tracing and Big O reasoning.

## Parked Until Later

- Trees, balanced trees, Dijkstra's algorithm, greedy algorithms, dynamic programming, k-nearest neighbors (Grokking Algorithms Ch.6-13, Data Structures & Algorithms Ch.10+) — beyond syllabus scope, optional enrichment only.
- Inheritance and polymorphism in depth (Think Python Ch.18) — held until basic classes are second nature.
- Regex beyond the lightest intro — Automate the Boring Stuff Ch.9 gets only a light pass this stage.
- Think Like a Programmer's later chapters (beyond the Ch.1 strategy discussion already used in Stage 7) — still C++ code, still not a direct source for Chris.
