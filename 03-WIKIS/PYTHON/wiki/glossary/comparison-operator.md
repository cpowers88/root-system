---
type: glossary-entry
stage: 02
status: draft
aliases: []
related_terms: ["boolean", "condition"]
---

# Comparison Operator

## Plain-English Definition

A symbol that compares two values and produces a Boolean: `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`.

## What Problem It Helps Solve

Lets a program ask a precise yes/no question about two values, instead of just storing or printing them.

## When Chris Will See It

Inside almost every `if`/`elif`/`while` condition.

## Code Example

```python
guess == answer
score >= 100
name != "Chris"
```

## Common Confusion

`==` (comparison) vs. `=` (assignment) — the single most common Stage 2 mistake. `=` makes something happen (assigns); `==` asks a question (compares).

## Physical-World Anchor

Like a balance scale: it tells you which side is heavier, or whether they're equal — it doesn't change either side.

## Related Terms

- [[glossary/boolean]]
- [[glossary/condition]]

## Flashcard Q/A

**Front:** What's the difference between `=` and `==`?

**Back:** `=` assigns a value to a variable. `==` compares two values and returns True or False.
