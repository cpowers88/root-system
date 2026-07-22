---
type: concept
stage: 03
status: draft
source_refs: ["Think Python Ch.5 (Floor Division and Modulus)"]
prerequisites: ["values-and-expressions", "for-loops"]
tags: [modulo, divisibility]
timeline: reference
---

# Concept: Modulo and Divisibility

## Plain-English Meaning

The modulo operator `%` gives the remainder left after division. A remainder of
zero means the first number divides evenly by the second.

## What Problem This Solves

Modulo lets code recognize repeating number patterns: even or odd numbers,
multiples of a number, clock cycles, and positions that wrap back to the start.

## When To Use It

Use `%` when the question is about a remainder or whether one number is divisible
by another. For example, `number % 7 == 0` asks, “Does seven fit into this number
with nothing left over?”

## When Not To Use It

Do not use `%` when you need the division result itself; use `/` for ordinary
division. In Python, `%` is not a percentage symbol.

## Code Shape

```python
remainder = number % divisor
is_divisible = number % divisor == 0
```

## Tiny Working Example

```python
print(17 % 5)       # 2 items left over
print(21 % 7 == 0)  # True: 21 is divisible by 7
print(9 % 2 == 0)   # False: 9 is odd
```

## Beginner Mistakes

- Reading `%` as “percent” instead of “remainder.”
- Checking `number % divisor == 1` when the goal is divisibility; evenly divisible
  means the remainder is `0`.
- Swapping the operands: `7 % number` asks a different question from `number % 7`.
- Dividing by zero. `% 0`, like `/ 0`, raises an error.

## Physical-World Anchor

Pack 17 objects into boxes that hold 5 each. Three boxes fill completely and 2
objects remain. That leftover count is `17 % 5`.

## Required Vocabulary

- [[glossary/modulo-operator]]

## Related Code Patterns

- [[code-patterns/for-loop-over-range]]

## Drill

- [[drills/stage-03-loop-tracing]]

## Explain-Back Questions

1. In plain English, what does `23 % 5` return?
2. Why does `number % 7 == 0` test divisibility by 7?
3. How would modulo distinguish an even number from an odd number?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.5, “Floor Division and Modulus”)
- Used directly by the Stage 3 divisible-by-7 counter drill and later by the
  Stage 5 Caesar Cipher.
