---
type: concept
stage: 05
status: draft
source_refs: ["Think Python Ch.13 (Data Structures, lighter preview)", "Automate the Boring Stuff Ch.6-7"]
prerequisites: ["lists", "dictionaries", "tuples-and-sets"]
tags: [decision-rule, data-structures]
timeline: reference
---

# Concept: Choosing the Right Data Structure

## Plain-English Meaning

This isn't a new syntax — it's the decision rule for picking *which* data shape fits a given problem: list, dictionary, tuple, or set.

## What Problem This Solves

Stage 5 introduces four different ways to group data. The hardest part isn't learning each one individually — it's recognizing, from a real problem description, which one actually fits. This is exactly the kind of "when do I use this?" instinct the vault is built to train.

## When To Use It

Every time you're about to store more than one related value and aren't sure how — pause and ask the questions below before writing any code.

## When Not To Use It

N/A — this is a decision process, not a code construct to avoid.

## Code Shape

```text
Does each item need a position/order, and might it change (grow/shrink/be edited)?
    -> list

Does each item need a meaningful label instead of a position?
    -> dictionary

Is it a small, fixed group of values that travel together and should never change?
    -> tuple

Do you only care whether something is present, with no duplicates and no order?
    -> set
```

## Tiny Working Example

```python
# A list: order matters, will grow
high_scores = [95, 88, 100]

# A dictionary: labeled data
player = {"name": "Chris", "score": 95}

# A tuple: fixed pair that won't change
screen_size = (1920, 1080)

# A set: just need to know who's already been counted
seen_names = {"Chris", "Alex"}
```

## Beginner Mistakes

- Reaching for a list when the data is actually labeled (using `["Chris", 16, "A"]` instead of `{"name": "Chris", "age": 16, "grade": "A"}` — the list version requires remembering what each position *means*, which doesn't scale).
- Using a dictionary when a simple list would do, just because dictionaries feel more "advanced."
- Not considering a tuple for data that's conceptually a single fixed unit (a coordinate, an RGB color) and using a list instead, accidentally allowing it to be modified.

## Physical-World Anchor

A list is a numbered shelf. A dictionary is a labeled filing cabinet. A tuple is a sealed, labeled box. A set is a guest list where you only care who's on it.

## Required Vocabulary

- (uses vocabulary already introduced: [[glossary/list]], [[glossary/dictionary]], [[glossary/tuple]], [[glossary/set]])

## Related Code Patterns

- [[code-patterns/list-loop-and-index]]
- [[code-patterns/dictionary-lookup]]

## Drill

- [[drills/stage-05-data-structure-practice]]

## Explain-Back Questions

1. Given "store every student's name and their grade," which structure fits, and why?
2. Given "store the top 5 scores of a game, which might change," which structure fits, and why?
3. Given "store a fixed RGB color value," which structure fits, and why?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.13, "Data Structures" — light conceptual preview; full chapter is a Stage 8 case study)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.6-7)
