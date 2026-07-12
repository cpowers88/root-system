---
type: code-pattern
stage: 01
status: draft
concepts: ["variable", "input", "type-conversion"]
tags: [stage-01, input, conversion]
---

# Code Pattern: Get Input and Convert Type

## Purpose

Collect a value from the user with `input()` and convert it into the type you actually need (`int` or `float`) so it can be used in math.

## Use This When

The program needs a number from the user — an age, a quantity, a price — and will do arithmetic with it.

## Do Not Use This When

The input is meant to stay as text (a name, a yes/no answer) — skip the conversion step.

## Skeleton

```python
raw_text = input("Prompt: ")
value = int(raw_text)     # or float(raw_text) if decimals are possible
```

## Filled Example

```python
age_text = input("How old are you? ")
age = int(age_text)
print(f"Next year you'll be {age + 1}.")
```

## Step-by-Step Trace

1. `input("How old are you? ")` shows the prompt and waits.
2. Whatever the user types is returned as a **string**, stored in `age_text`.
3. `int(age_text)` converts that string into a real integer, stored in `age`.
4. `age + 1` now works because `age` is a number, not text.

## Beginner Mistakes

- Skipping the conversion and trying `age + 1` directly on the string result of `input()` — raises `TypeError`.
- Using `int()` on a value that might contain a decimal (`int("3.9")` raises `ValueError`) — use `float()` instead.
- Converting a name or other non-numeric input with `int()` — raises `ValueError`.

## Related Terms

- [[glossary/input]]
- [[glossary/type-conversion]]
- [[glossary/integer]]
- [[glossary/float]]

## Drill Link

- [[drills/stage-01-input-and-conversion]]

## Flashcards To Create

- Already covered in [[flashcards/stage-01-python-atoms]] — "Why convert input?" and "int() vs float() decision rule" cards.
