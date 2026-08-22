---
type: glossary-entry
stage: 03
status: draft
timeline: reference
aliases: ["modulus operator", "remainder operator", "%"]
related_terms: ["divisibility", "expression", "comparison-operator"]
---

# Modulo Operator

## Plain-English Definition

The Python operator `%`, which returns the remainder after one number is divided
by another.

## What Problem It Helps Solve

It tests divisibility and identifies repeating patterns such as even/odd values or
positions that wrap around a fixed cycle.

## When Chris Will See It

In the Stage 3 divisible-by-7 counter, even/odd checks, and later in the Caesar
Cipher mini-project.

## Code Example

```python
17 % 5            # 2
number % 7 == 0   # True when number is divisible by 7
```

## Common Confusion

`%` means remainder in Python, not percentage. A remainder of `0` means the
division came out evenly.

## Physical-World Anchor

After filling equal-size boxes, modulo is the number of items left unpacked.

## Related Terms

- [[concepts/modulo-and-divisibility]]
- [[glossary/comparison-operator]]

## Flashcard Q/A

**Front:** What does `number % 7 == 0` ask?

**Back:** Whether `number` is divisible by 7 with no remainder.
