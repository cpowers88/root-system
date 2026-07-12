---
type: glossary-entry
stage: 07
status: draft
aliases: []
related_terms: ["pseudocode", "decomposition"]
---

# Algorithm

## Plain-English Definition

A precise, step-by-step procedure for solving a problem or completing a task — the actual logic, once it's settled (as opposed to pseudocode, which is the rough plan on the way there).

## What Problem It Helps Solve

Gives a name to "the actual sequence of steps that solves this," separate from the specific code that implements it in any one language.

## When Chris Will See It

Anywhere a procedure is described abstractly — "the algorithm for finding the largest number in a list is: start with the first number, compare it to each other number, keep the bigger one each time."

## Code Example

```text
Algorithm: find the largest number in a list
1. Assume the first number is the largest so far.
2. For each remaining number, if it's bigger than the current largest, update the largest.
3. After checking all numbers, the largest so far is the answer.
```

## Common Confusion

An algorithm isn't tied to Python specifically — the same algorithm could be implemented in any programming language. Stage 7 uses the word loosely (any clear step-by-step procedure); Stage 8 introduces formally analyzed algorithms (sorting, searching) with efficiency considerations.

## Physical-World Anchor

A recipe is an algorithm for making food — precise steps that, followed in order, reliably produce the result, regardless of which kitchen you're in.

## Related Terms

- [[glossary/pseudocode]]
- [[glossary/decomposition]]

## Flashcard Q/A

**Front:** What is an algorithm?

**Back:** A precise, step-by-step procedure for solving a problem, independent of which programming language implements it.
