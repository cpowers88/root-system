---
type: error-log
stage: 01
status: draft
tags: [stage-01, errors, debugging-preview]
---

# Stage 1 Common Errors

A light preview of error-reading — full debugging is Stage 6. The goal here is just to recognize these four shapes when they appear.

## 1. `TypeError` from mixing string and number

```python
age = input("Age? ")     # age is a string, even if you type "16"
print("Next year: " + age + 1)
```

```text
TypeError: can only concatenate str (not "int") to str
```

**Why it happens:** `input()` always returns a string. You can't `+` a string and a number directly.

**Fix:** convert with `int()`/`float()`, or use an f-string instead of `+`.

## 2. `NameError` from a missing or misspelled variable

```python
print(naem)
```

```text
NameError: name 'naem' is not defined
```

**Why it happens:** Python doesn't know any variable by that name — usually a typo, or using a variable before assigning it.

**Fix:** check spelling and confirm the variable was assigned earlier in the code.

## 3. `SyntaxError` from missing quotes or parentheses

```python
print(Chris)
```

```text
NameError: name 'Chris' is not defined
```

(Note: this specific example actually raises `NameError`, not `SyntaxError`, because `Chris` looks like a valid variable name to Python. The fix is the same lesson either way: text needs quotes.)

```python
print "Hello"
```

```text
SyntaxError: Missing parentheses in call to 'print'
```

**Why it happens:** forgetting quotes around text, or forgetting `print()`'s parentheses (a leftover habit from Python 2).

**Fix:** wrap text in quotes; always call `print()` with parentheses in Python 3.

## 4. `ValueError` from converting non-numeric text

```python
age = int("sixteen")
```

```text
ValueError: invalid literal for int() with base 10: 'sixteen'
```

**Why it happens:** `int()` can only convert text that's actually a whole number written as digits.

**Fix:** make sure the input is a valid number before converting, or catch the error (full handling is Stage 6 — for now, just recognize this shape).

## How to Read Any of These

1. Read the **last line first** — it names the error type and the specific problem.
2. Read the line number Python points to — that's where it noticed the problem (not always where the *real* mistake is).
3. Ask: "What type did I expect this value to be, and what type did it actually turn out to be?"

## Related

- [[concepts/numbers-and-type-conversion]]
- [[concepts/print-and-input]]
- [[concepts/variables-and-assignment]]
