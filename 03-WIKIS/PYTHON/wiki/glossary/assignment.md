---
type: glossary-entry
stage: 01
status: draft
aliases: ["assignment statement"]
related_terms: ["variable", "value"]
---

# Assignment

## Plain-English Definition

The action of attaching a name (variable) to a value, using the `=` operator.

## What Problem It Helps Solve

Creates the link between a name and the data it refers to, so the data can be reused later by name.

## When Chris Will See It

Every time a variable is created or updated: `name = value`.

## Code Example

```python
score = 0
score = score + 10   # reassignment
```

## Common Confusion

`=` is assignment ("make this point to that"). `==` is comparison ("are these equal?"). Mixing these up is one of the most common beginner errors.

## Physical-World Anchor

Like writing a new name on a mailbox — the mailbox (value) doesn't change, but who it belongs to (the variable name) does.

## Related Terms

- [[glossary/variable]]
- [[glossary/value]]

## Flashcard Q/A

**Front:** What does `=` do in Python, and how is it different from `==`?

**Back:** `=` assigns a value to a variable name. `==` checks whether two things are equal. They are not interchangeable.
