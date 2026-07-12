---
type: glossary-entry
stage: 08
status: draft
aliases: []
related_terms: ["recursion"]
---

# Base Case

## Plain-English Definition

The simplest version of a recursive problem, answered directly without any further recursive call — this is what stops the recursion.

## What Problem It Helps Solve

Without a base case (or with one that's never actually reached), a recursive function calls itself forever, eventually crashing with a `RecursionError`.

## When Chris Will See It

The first `if` check inside any recursive function.

## Code Example

```python
def countdown(n):
    if n <= 0:        # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
```

## Common Confusion

Having a base case isn't enough — each recursive call must actually move *toward* it (here, `n - 1` shrinks toward `n <= 0`). A recursive call that doesn't shrink the problem will never reach the base case.

## Physical-World Anchor

The smallest Russian nesting doll — the one that doesn't open, where opening dolls stops.

## Related Terms

- [[glossary/recursion]]

## Flashcard Q/A

**Front:** What happens if a recursive function's base case is never actually reached?

**Back:** Infinite recursion — the function keeps calling itself until Python raises a RecursionError.
