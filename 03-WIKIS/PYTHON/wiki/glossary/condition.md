---
type: glossary-entry
stage: 02
status: draft
aliases: []
related_terms: ["boolean", "comparison-operator", "if-elif-else"]
---

# Condition

## Plain-English Definition

An expression that evaluates to `True` or `False`, used to decide whether a branch of code should run.

## What Problem It Helps Solve

Lets a program test something ("is the guess correct?") before deciding what to do next.

## When Chris Will See It

Right after every `if`, `elif`, and `while` keyword.

## Code Example

```python
if age >= 18:
    print("Adult")
```

## Common Confusion

A condition isn't a statement by itself — it's the question that an `if` (or `while`) acts on. Forgetting the colon after a condition is a very common error.

## Physical-World Anchor

Like the yes/no question on a checklist that decides which box you check next.

## Related Terms

- [[glossary/boolean]]
- [[glossary/if-elif-else]]

## Flashcard Q/A

**Front:** What is a condition in Python?

**Back:** An expression that evaluates to True or False, used to decide whether a branch of code runs.
