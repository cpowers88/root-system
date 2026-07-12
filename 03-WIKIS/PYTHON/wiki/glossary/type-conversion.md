---
type: glossary-entry
stage: 01
status: draft
aliases: ["type casting"]
related_terms: ["integer", "float", "string"]
---

# Type Conversion

## Plain-English Definition

Turning a value from one type into another — most commonly text into a number (`int()`, `float()`) or a number into text (`str()`).

## What Problem It Helps Solve

`input()` always returns a string, even if the user typed a number. Type conversion is what makes that text usable in math.

## When Chris Will See It

Right after almost every `input()` call where the answer needs to be used as a number.

## Code Example

```python
age_text = input("Age? ")   # "16" — a string
age = int(age_text)           # 16 — a real integer
```

## Common Confusion

`int("hello")` raises a `ValueError` — not every string can become a number. `int("3.9")` also fails — convert to `float()` first if decimals are possible.

## Physical-World Anchor

Like exchanging currency — `"7"` and `7` look related but you can't use one where the other is expected until you convert it.

## Related Terms

- [[glossary/integer]]
- [[glossary/float]]
- [[glossary/string]]

## Flashcard Q/A

**Front:** Why do you usually need to convert the result of `input()` before doing math with it?

**Back:** Because `input()` always returns a string, even if the user typed a number — you must convert it with `int()` or `float()` first.
