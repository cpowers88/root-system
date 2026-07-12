---
type: glossary-entry
stage: 01
status: draft
aliases: ["int"]
related_terms: ["float", "type-conversion"]
---

# Integer

## Plain-English Definition

A whole number, with no decimal point — positive, negative, or zero. Python's name for this type is `int`.

## What Problem It Helps Solve

Represents counts, ages, scores, and any quantity that doesn't need fractional precision.

## When Chris Will See It

Anywhere whole numbers are used: `age = 16`, `score = 0`.

## Code Example

```python
age = 16
type(age)   # <class 'int'>
```

## Common Confusion

`int("16")` works (text that looks like a whole number), but `int("16.5")` fails — `int()` can't parse a decimal-looking string directly.

## Physical-World Anchor

Like counting whole objects — you can have 3 apples, but not "3.5 apples" if you're only counting whole ones.

## Related Terms

- [[glossary/float]]
- [[glossary/type-conversion]]

## Flashcard Q/A

**Front:** What is an integer in Python?

**Back:** A whole number (no decimal point), represented by the `int` type.
