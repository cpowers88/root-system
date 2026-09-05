---
type: glossary-entry
stage: 04
status: draft
aliases: ["return"]
related_terms: ["fruitful-void-function", "function"]
timeline: reference
---

# Return Value

## Plain-English Definition

The value a function hands back to whatever called it, using the `return` keyword.

## What Problem It Helps Solve

Lets the result of a function be stored, used in further calculations, or passed into another function — not just displayed.

## When Chris Will See It

Any function whose result is meant to be used afterward, not just shown on screen.

## Code Example

```python
def square(n):
    return n * n

answer = square(5)
print(answer + 1)   # 26
```

## Common Confusion

`print()` displays a value but doesn't hand anything back to the caller. `return` does. A function with no `return` statement returns `None` by default.

## Physical-World Anchor

A vending machine handing you a snack (the return value) — not just showing it behind glass.

## Related Terms

- [[glossary/fruitful-void-function]]

## Flashcard Q/A

**Front:** What does a function return if it has no `return` statement?

**Back:** `None` — Python's way of saying "nothing."
