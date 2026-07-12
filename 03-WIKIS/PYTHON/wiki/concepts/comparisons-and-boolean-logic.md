---
type: concept
stage: 02
status: draft
source_refs: ["Think Python Ch.5 (Boolean Expressions, Logical Operators)", "Automate the Boring Stuff Ch.2", "Python Crash Course Ch.5"]
prerequisites: ["values-and-expressions", "variables-and-assignment"]
tags: [stage-02, comparisons, boolean-logic]
---

# Concept: Comparisons and Boolean Logic

## Plain-English Meaning

A **comparison operator** (`==`, `!=`, `<`, `>`, `<=`, `>=`) asks a yes/no question about two values and produces a **Boolean** — `True` or `False`. **Boolean operators** (`and`, `or`, `not`) combine multiple yes/no questions into one bigger yes/no answer.

## What Problem This Solves

A program can't make a decision without first being able to ask a question and get back a definite `True`/`False` answer. Comparisons and Boolean logic are how a program "asks a question."

## When To Use It

Any time the program needs to test something before deciding what to do: "is the user old enough?", "did they guess the right number?", "is the list empty?"

## When Not To Use It

Don't use `=` (assignment) when you mean `==` (comparison) — this is the single most common Stage 2 mistake. Don't chain comparisons with plain English logic in your head; write out the `and`/`or`/`not` explicitly.

## Code Shape

```python
age == 18        # equality check -> True or False
age != 18        # not-equal check
age >= 18        # greater-than-or-equal
age >= 13 and age < 20   # combining two comparisons
```

## Tiny Working Example

```python
age = 16
is_teenager = age >= 13 and age <= 19
print(is_teenager)   # True
```

## Beginner Mistakes

- Writing `age = 18` (assignment) when checking equality — should be `age == 18`.
- Forgetting that `and` requires **both** sides to be `True`, while `or` only needs **one** side.
- Writing `age >= 13 and <= 19` — Python needs the variable repeated on both sides: `age >= 13 and age <= 19`.

## Physical-World Anchor

A comparison is like a yes/no question on a form ("Are you 18 or older?"). `and`/`or`/`not` are how you combine multiple form questions into one rule ("eligible if 18 or older AND a resident").

## Required Vocabulary

- [[glossary/condition]]
- [[glossary/boolean]]
- [[glossary/comparison-operator]]
- [[glossary/boolean-operators]]

## Related Code Patterns

- [[code-patterns/if-elif-else-decision-chain]]

## Drill

- [[drills/stage-02-decision-rules]]

## Explain-Back Questions

1. What does a comparison operator produce — and what are the only two possible answers?
2. What's the difference between `and` and `or` when combining two conditions?
3. Why does `age = 18` not check anything, even though it looks similar to `age == 18`?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.5, "Boolean Expressions" and "Logical Operators")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.2)
- (source: Python Crash Course, 3rd Ed., Ch.5, "Conditional Tests")
