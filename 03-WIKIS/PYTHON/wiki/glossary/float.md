---
type: glossary-entry
stage: 01
status: draft
aliases: []
related_terms: ["integer", "type-conversion"]
---

# Float

## Plain-English Definition

A number with a decimal point — Python's name for this type is `float` (short for "floating-point number").

## What Problem It Helps Solve

Represents quantities that need fractional precision: prices, measurements, averages.

## When Chris Will See It

Anywhere decimals are involved: `price = 9.99`, `average = total / count`.

## Code Example

```python
price = 9.99
type(price)   # <class 'float'>
```

## Common Confusion

Dividing two integers with `/` in Python always produces a `float`, even if the result is a whole number (`6 / 2` is `3.0`, not `3`).

## Physical-World Anchor

Like a measuring cup that shows fractions of a cup, not just whole cups.

## Related Terms

- [[glossary/integer]]
- [[glossary/type-conversion]]

## Flashcard Q/A

**Front:** What is a float in Python?

**Back:** A number with a decimal point, represented by the `float` type.
