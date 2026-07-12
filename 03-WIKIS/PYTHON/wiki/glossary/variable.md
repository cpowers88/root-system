---
type: glossary-entry
stage: 01
status: draft
aliases: []
related_terms: ["assignment", "value"]
---

# Variable

## Plain-English Definition

A name that points to a value, created with `=`. The name can be made to point at a different value later (reassignment).

## What Problem It Helps Solve

Lets a program remember and reuse a value — user input, a calculation result, a running total — instead of retyping it everywhere.

## When Chris Will See It

In nearly every program, from the first line on.

## Code Example

```python
age = 16
age = age + 1   # age now points to 17
```

## Common Confusion

A variable is a label, not a box. Reassigning it doesn't change the old value somewhere else — it just points the name at something new. Also commonly confused with `==` (comparison) — `=` is assignment.

## Physical-World Anchor

A name tag on a parking space: the space can hold different cars (values) over time, but the name tag itself doesn't change.

## Related Terms

- [[glossary/assignment]]
- [[glossary/value]]

## Flashcard Q/A

**Front:** What is a variable?

**Back:** A name that points to a value, and can be reassigned to point at a different value later.
