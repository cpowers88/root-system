---
type: stage
stage_number: 05
status: ready
priority: current
source_spine: "Think Python Ch.8, 10, 11, 12"
support_sources: ["Automate the Boring Stuff Ch.6-8", "Python Crash Course Ch.3-4 & 6", "Python Workout Ch.4-5", "Invent Your Own Computer Games Ch.8-14"]
---

# Stage 05 — Data Shapes

## Purpose

Learn to group and label data: strings as sequences, lists, dictionaries, tuples, sets — and most importantly, when to reach for each one.

## Why This Stage Comes Now

Stages 1-4 worked with one value at a time. Real problems almost always involve *groups* of related data — a roster of names, a set of scores, a record with multiple fields. This stage is also the vault's biggest direct test of "tool selection," the skill CLAUDE.md identifies as Chris's main bottleneck.

## Prerequisites

Stage 4 — functions, parameters, return values, scope.

## Concepts To Learn

- [[concepts/strings-as-sequences]]
- [[concepts/lists]]
- [[concepts/dictionaries]]
- [[concepts/tuples-and-sets]]
- [[concepts/choosing-a-data-structure]]

## Vocabulary To Add

- [[glossary/index]]
- [[glossary/slice]]
- [[glossary/mutable-immutable]]
- [[glossary/list]]
- [[glossary/aliasing]]
- [[glossary/dictionary]]
- [[glossary/dictionary-key-value-pair]]
- [[glossary/tuple]]
- [[glossary/set]]
- [[glossary/nested-structure]]

Full flashcard batch: [[flashcards/stage-05-data-shapes]]

## Required Code Patterns

- [[code-patterns/list-loop-and-index]]
- [[code-patterns/dictionary-lookup]]

## Drills

- [[drills/stage-05-data-structure-practice]]
- Extra practice: Python Workout Ch.4 (Lists and Tuples) and Ch.5 (Dictionaries and Sets) exercises.

## Mini-Project

- [[mini-projects/stage-05-caesar-cipher]]
- Alternative/extra: Invent Your Own Computer Games Ch.8-9 (Hangman — strings/lists) or Ch.10 (Tic-Tac-Toe — lists/2D thinking), if Chris wants more reps before moving on.

## Common Errors Reference

- [[errors/stage-05-common-errors]]

## Read Next

1. Think Python Ch.8 — only "A String Is a Sequence," "String Slices," "Strings Are Immutable" remain unread from this chapter (the rest was covered in Stage 3). Add "Searching," "Looping and Counting," "String Methods," "The in Operator," "String Comparison."
2. Think Python Ch.10 (Lists) — full chapter, especially "Lists Are Mutable," "List Methods," "Aliasing," "List Arguments."
3. Think Python Ch.11 (Dictionaries) — "A Dictionary Is a Mapping," "Looping and Dictionaries," "Dictionaries and Lists" (light preview of nesting). **Skip** "Memos" and "Global Variables" — those lean into recursion/optimization territory for Stage 8.
4. Think Python Ch.12 (Tuples) — "Tuples Are Immutable," "Tuple Assignment" only. Skip "Tuples as Return Values," "Variable-Length Argument Tuples," "Sequences of Sequences" for now.
5. Automate the Boring Stuff Ch.6 (Lists), Ch.7 (Dictionaries), Ch.8 (Strings) — parallel reinforcement.
6. Python Crash Course Ch.3-4 (Lists) and Ch.6 (Dictionaries) — extra worked examples and exercises.

## Mastery Checklist

- [ ] Define index, slice, mutable/immutable, list, aliasing, dictionary, key/value, tuple, set, and nested structure in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Given a new plain-English data scenario, correctly choose list vs. dictionary vs. tuple, and explain why.
- [ ] Write a list-indexing/slicing example and a dictionary-lookup example from memory, without notes.
- [ ] Explain aliasing and why `list_b = list_a` doesn't copy a list.
- [ ] Debug at least one of the four error types in [[errors/stage-05-common-errors]] without help.
- [ ] Complete [[drills/stage-05-data-structure-practice]].
- [ ] Complete [[mini-projects/stage-05-caesar-cipher]] and explain the solution out loud.

## Stage Mastery Target

Can choose the correct data structure (list, dictionary, or tuple) for a new problem and justify the choice, plus read/write/index into each one confidently.

## Parked Until Later

- Sets beyond the light intro given here (full Ch.19 "Goodies" treatment) — Stage 10.
- Nested structures deeper than one level (lists of dictionaries with lists inside) — introduced lightly here, drilled further in Stage 7-8 case studies.
- List comprehensions — Stage 10.
- `Counter`, `defaultdict`, and other specialized collection types — Stage 10, parked per `wiki/parking-lot.md`.
- Searching/sorting algorithms on these structures — Stage 8.
