---
type: glossary-entry
stage: 04
status: draft
aliases: ["fruitful function", "void function"]
related_terms: ["return-value", "function"]
timeline: reference
---

# Fruitful / Void Function

## Plain-English Definition

A **fruitful** function returns a value with `return`, meant to be used by whatever called it. A **void** function performs an action (like printing) but doesn't hand back a usable value.

## What Problem It Helps Solve

Gives a clear way to decide, before writing a function, what kind of job it's actually doing — producing a result, or performing an action.

## When Chris Will See It

Every function falls into one category or the other, even without the label being said out loud.

## Code Example

```python
def square(n):       # fruitful — returns a value
    return n * n

def greet(name):      # void — just performs an action
    print(f"Hello, {name}!")
```

## Common Confusion

Calling a void function and trying to use "what it returns" in a calculation — it returns `None`, which usually causes a `TypeError` if you try to do math with it.

## Physical-World Anchor

A vending machine (fruitful — hands you something) versus a doorbell (void — does something, but hands you nothing back).

## Related Terms

- [[glossary/return-value]]

## Flashcard Q/A

**Front:** What's the difference between a fruitful function and a void function?

**Back:** A fruitful function returns a usable value. A void function performs an action but doesn't hand anything back.
