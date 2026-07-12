---
type: glossary-entry
stage: 04
status: draft
aliases: []
related_terms: ["argument", "function", "scope"]
---

# Parameter

## Plain-English Definition

A name listed in a function's definition that acts as a placeholder for a value the function will receive when called.

## What Problem It Helps Solve

Lets a function be generic — written once, but able to act on different data depending on what's passed in at each call.

## When Chris Will See It

Inside the parentheses of a `def` line.

## Code Example

```python
def greet(name):   # "name" is the parameter
    print(f"Hello, {name}!")
```

## Common Confusion

A parameter is the name in the *definition*; the argument is the actual *value* supplied at the call. They're easy to mix up because they refer to "the same slot" from two different angles.

## Physical-World Anchor

A blank line on a form: "Name: ____" — the blank itself is the parameter; reusable for anyone filling it in.

## Related Terms

- [[glossary/argument]]
- [[glossary/scope]]

## Flashcard Q/A

**Front:** What is a parameter?

**Back:** A name in a function's definition that acts as a placeholder for a value it will receive when called.
