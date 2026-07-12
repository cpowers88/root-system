---
type: concept
stage: 01
status: draft
source_refs: ["Think Python Ch.1 (Values and Types)", "Python Crash Course Ch.2 (Numbers)", "Think Python Ch.5 (Keyboard Input, pulled forward)"]
prerequisites: ["values-and-expressions", "strings"]
tags: [stage-01, numbers, type-conversion]
---

# Concept: Numbers and Type Conversion

## Plain-English Meaning

Python has two main number types: **integers** (`int`, whole numbers like `7` or `-3`) and **floats** (`float`, decimal numbers like `3.14`). **Type conversion** means turning a value from one type into another — most often turning text into a number with `int()` or `float()`, or turning a number into text with `str()`.

## What Problem This Solves

`input()` always hands back a string, even if the user typed a number. Without converting it, you can't do math on it — you can only glue it to other text.

## When To Use It

Convert with `int()` or `float()` whenever you need to do arithmetic on something that arrived as text (almost always: user input). Convert with `str()` when you need to glue a number into a string with `+` instead of an f-string.

## When Not To Use It

Don't convert a string to `int()` if it might contain non-numeric text (like a name) — that raises a `ValueError`. Don't convert when an f-string would let you skip the conversion entirely.

## Code Shape

```python
int("7")        # 7 (as a number, not text)
float("3.14")   # 3.14
str(7)          # "7" (as text)
type(value)     # tells you what type something currently is
```

## Tiny Working Example

```python
age_text = input("How old are you? ")   # always a string, e.g. "16"
age = int(age_text)                       # now it's a real number
print(f"Next year you'll be {age + 1}.")
```

## Beginner Mistakes

- Forgetting to convert `input()` before doing math: `age + 1` crashes with a `TypeError` if `age` is still the string `"16"`.
- Trying `int("hello")` — raises `ValueError` because the text isn't a valid number.
- Forgetting that `int("3.9")` fails — `int()` can't directly parse a decimal-looking string; convert to `float()` first if decimals are possible.

## Physical-World Anchor

Converting types is like exchanging currency — `"7"` (text) and `7` (number) look similar but you can't spend one as if it were the other until you convert it.

## Required Vocabulary

- [[glossary/integer]]
- [[glossary/float]]
- [[glossary/type-conversion]]

## Related Code Patterns

- [[code-patterns/input-and-type-conversion]]

## Drill

- [[drills/stage-01-input-and-conversion]]

## Explain-Back Questions

1. Why does `input()` always return a string, even if the user types `42`?
2. What error do you get from `int("hello")`, and why?
3. When would you use `str()` instead of an f-string?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.1, "Values and Types")
- (source: Python Crash Course, 3rd Ed., Ch.2, "Numbers")
- (source: Think Python, 2nd Ed., Ch.5, "Keyboard Input" — pulled forward into Stage 1 per `wiki/source-map.md`)
