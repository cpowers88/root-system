---
type: stage
timeline: later
stage_number: 05b
status: ready
priority: upcoming
course_module: "M5.2 — Dictionaries, searching & sorting algorithms (lecture Week 11, Quiz 6; lab Lab 10)"
source_spine: "Think Python Ch.21 (Analysis of Algorithms) — selective"
support_sources: ["Grokking Algorithms Ch.1-5", "Common-Sense DS&A"]
---

# Stage 05b — Searching and Sorting

## Purpose

Search a collection for a value, sort one into order, and say why one approach is
slower than another — at the level the course actually tests, not at algorithms-
course depth.

## Why this is its own stage

Created 2026-07-25. Searching and sorting were parked at Stage 8 ("Think Python
readiness"), but **both syllabi teach and assess them in Module 5.2** — lecture
Week 11 with Quiz 6, lab Lab 10 — immediately after dictionaries and *before* OOP.
Stage 8 sits far later in the vault order. Leaving them there would have put a
quizzed topic behind two stages Chris hasn't reached.

Pulled forward and scoped down. The deep algorithm-analysis material stays at
Stage 8 for anyone who wants it; this stage covers what Module 5.2 requires.

## Prerequisites

Stage 5 — lists, dictionaries, tuples, and choosing between them. You cannot
search or sort a structure you can't yet read.

## Concepts To Learn

- [[concepts/sorting-and-searching]]
- [[concepts/big-o-and-algorithm-efficiency]] — **plain-language only** at this
  stage: "this one checks every item, that one halves the list each time." Formal
  complexity proofs stay in Stage 8.

## Vocabulary To Add

- [[glossary/searching]]
- [[glossary/sorting]]
- [[glossary/algorithm]]
- [[glossary/big-o]] — plain-language reading only at this stage

Full flashcard batch: [[flashcards/stage-08-algorithms-and-classes]] — use the
searching/sorting cards only; skip the classes cards until Stage 9/OOP.

## Course Core vs. Full Stage

**Course core:** linear search, binary search and why it needs sorted input,
at least one sort you can trace by hand, Python's built-in `sorted()`/`.sort()`,
and a plain-English efficiency comparison.

**Not course core:** formal Big-O notation and proofs, quicksort/mergesort
implementation, recursion-based algorithms, hash-table internals. All Stage 8.

## Code-Reading Gate

Given an unfamiliar search or sort, say what it compares, what it swaps or
returns, how many passes it makes over the data, and what happens when the target
isn't there — before running it.

## Drills

- [[drills/stage-08-algorithms-and-classes-practice]] — searching/sorting portions
  only.

## Read Next

1. [[concepts/sorting-and-searching]] — local page first.
2. Grokking Algorithms Ch.1 (binary search) and Ch.2 (selection sort) — the visual
   treatment fits how Chris reads structure. **Not yet page-mapped**; see
   [[source-page-map]], mapping is open work.
3. Think Python **Ch.21, physical p. 267** — read only enough to connect "checks
   every item" vs. "halves the list." Skip the formal analysis.

## Mastery Checklist

- [ ] Explain linear vs. binary search in plain English, and state why binary
  search requires sorted input.
- [ ] Trace one sort by hand on a five-element list and predict the order after
  each pass.
- [ ] Write a linear search over a list from memory, returning the index or a
  not-found result.
- [ ] Use `sorted()` and `.sort()` and explain the difference (one returns a new
  list, one mutates in place — this is the Stage 5 aliasing lesson again).
- [ ] Say which of two approaches does more work on a long list, and why, without
  using Big-O notation.

## Stage Mastery Target

Can search and sort a real list, choose between the built-in and a hand-written
approach, and explain the cost difference in plain language.

## Parked Until Later

- Formal Big-O notation, quicksort, mergesort, recursion-based algorithms,
  hash-table internals — Stage 8.
- Sorting dictionaries by value and `key=` functions — introduce only if a drill
  needs it.

## Teaching Method

Run this stage on the loop in [[teaching-loop]]. Searching and sorting reward the
cold-attempt-first rule especially well: predicting a sort's state after each pass
*before* running it is the whole skill.
