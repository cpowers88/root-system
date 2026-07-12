---
type: concept
stage: 01
status: draft
source_refs: ["Think Python Ch.2 (Assignment Statements, Variable Names)", "Python Crash Course Ch.2 (Variables)"]
prerequisites: ["values-and-expressions"]
tags: [stage-01, variables, assignment]
---

# Concept: Variables and Assignment

## Plain-English Meaning

A **variable** is a name that refers to a value. **Assignment** is the act of attaching that name to a value using `=`. The variable is a label pointing at the value — not a box that contains it permanently; the label can be moved to point at a new value at any time.

## What Problem This Solves

Without variables, every value would need to be retyped everywhere it's used, and a program couldn't remember a result to use later (like a user's name, or a running score).

## When To Use It

Whenever you need to store a value to use again later in the program — user input, a calculation result, a name, a score.

## When Not To Use It

If a value is only ever used once and immediately, you don't strictly need a variable — but giving it a name is almost always more readable.

## Code Shape

```python
variable_name = value
```

## Tiny Working Example

```python
age = 16
name = "Chris"
age = age + 1   # reassignment: age now points to a new value, 17
print(name, age)
```

## Beginner Mistakes

- Confusing `=` (assignment) with `==` (comparison). `=` means "make this name point to this value." `==` means "are these two things equal?"
- Using a variable before assigning it a value (`NameError`).
- Forgetting that reassigning a variable doesn't change the old value anywhere else — it just moves the label.

## Physical-World Anchor

A variable is like a name tag on a parking space, not a locked box. The space (`age`) can hold one car (value) at a time, and you can swap which car is parked there, but the name tag itself never changes.

## Required Vocabulary

- [[glossary/variable]]
- [[glossary/assignment]]

## Related Code Patterns

- [[code-patterns/input-and-type-conversion]]

## Drill

- [[drills/stage-01-input-and-conversion]]

## Explain-Back Questions

1. What's the difference between `=` and `==`?
2. If `x = 5` and then `x = x + 1`, what does `x` equal now, and why?
3. Why does using a variable before assigning it cause an error?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.2, "Assignment Statements" and "Variable Names")
- (source: Python Crash Course, 3rd Ed., Ch.2, "Variables")
