---
type: glossary-entry
stage: 02
status: draft
aliases: ["branching"]
related_terms: ["if-elif-else", "condition"]
---

# Branch

## Plain-English Definition

One possible path of code that runs depending on a condition — the body of an `if`, `elif`, or `else`.

## What Problem It Helps Solve

Describes the general idea that a program's path can fork, rather than always being a single straight line of instructions.

## When Chris Will See It

Any time `if`/`elif`/`else` is discussed conceptually — each block is "a branch."

## Code Example

```python
if temperature > 90:
    print("It's hot.")   # this block is one branch
else:
    print("It's mild.")  # this block is another branch
```

## Common Confusion

A branch is the *block of code*, not the condition that selects it — the condition decides *which* branch runs.

## Physical-World Anchor

A fork in a hiking trail — you take exactly one path, even though more than one was available.

## Related Terms

- [[glossary/if-elif-else]]

## Flashcard Q/A

**Front:** What is a "branch" in the context of `if`/`elif`/`else`?

**Back:** One possible block of code that runs depending on whether its condition is True.
