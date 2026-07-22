---
type: glossary-entry
stage: 04
status: draft
aliases: ["def keyword"]
related_terms: ["function", "call"]
timeline: reference
---

# `def`

## Plain-English Definition

The keyword used to define a function — it tells Python "here's a new function, with this name, and this is what it does."

## What Problem It Helps Solve

Creates the function so it exists and can be called later — it's the "writing the recipe" step.

## When Chris Will See It

At the start of every function definition.

## Code Example

```python
def greet(name):
    print(f"Hello, {name}!")
```

## Common Confusion

`def` only *creates* the function — it doesn't run the body. The body only runs when the function is called.

## Physical-World Anchor

Like the moment you write down a recipe card — the card now exists, but nothing has been cooked yet.

## Related Terms

- [[glossary/function]]
- [[glossary/call]]

## Flashcard Q/A

**Front:** Does writing a `def` block run the function's code?

**Back:** No — `def` only defines the function. The body runs only when the function is called.
