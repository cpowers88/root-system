---
type: concept
stage: 01
status: draft
source_refs: ["Think Python Ch.1 (Values and Types, Arithmetic Operators)", "Python Crash Course Ch.2 (Numbers)"]
prerequisites: []
tags: [values, expressions]
timeline: reference
---

# Concept: Values and Expressions

## Plain-English Meaning

A **value** is one single piece of data — a number, a word, a true/false answer. An **expression** is anything Python can boil down to one value: a single value by itself, or values combined with operators like `+`, `-`, `*`, `/`.

## What Problem This Solves

Programs need a way to describe "do this calculation" or "combine these pieces of data" instead of the programmer pre-computing every answer by hand.

## When To Use It

Anywhere you need a result from a calculation or combination of data: math, building a sentence out of pieces of text, comparing two things.

## When Not To Use It

N/A at this level — expressions are the basic building block of every line of code that follows. There's no alternative to "not use" here, only the mistake of writing an expression that mixes incompatible types (see Beginner Mistakes).

## Code Shape

```python
# a value by itself is already an expression
7

# operators combine values into a new value
3 + 4
"a" + "b"
2 ** 3        # exponent
17 % 5        # remainder (modulo)
```

## Tiny Working Example

```python
print(2 + 3 * 4)     # 14 — multiplication happens before addition
print("Py" + "thon")  # "Python"
```

## Beginner Mistakes

- Assuming Python evaluates strictly left-to-right. It follows order of operations (`*` and `/` before `+` and `-`), just like math class.
- Mixing a string and a number directly: `"Age: " + 25` raises a `TypeError`. Numbers must be converted to strings first (see [[concepts/numbers-and-type-conversion]]).

## Physical-World Anchor

Think of a word problem from school: "3 apples plus 4 apples." The phrase itself is the expression; the answer, 7 apples, is the value it evaluates to.

## Required Vocabulary

- [[glossary/value]]
- [[glossary/expression]]

## Related Code Patterns

- (none yet — expressions appear inside every later pattern)

## Drill

- [[drills/stage-01-input-and-conversion]]

## Explain-Back Questions

1. What's the difference between a value and an expression?
2. Why does `2 + 3 * 4` evaluate to 14 and not 20?
3. Why does `"Age: " + 25` cause an error?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.1, "Values and Types" and "Arithmetic Operators")
- (source: Python Crash Course, 3rd Ed., Ch.2, "Numbers")
