---
type: concept
stage: 02
status: draft
source_refs: ["Think Python Ch.5 (Conditional Execution, Alternative Execution, Chained/Nested Conditionals)", "Automate the Boring Stuff Ch.2", "Python Crash Course Ch.5"]
prerequisites: ["comparisons-and-boolean-logic"]
tags: [conditionals, branching]
timeline: reference
---

# Concept: `if` / `elif` / `else`

## Plain-English Meaning

`if`/`elif`/`else` is how a program **branches**: it checks a condition, and runs a different block of code depending on whether that condition is `True` or `False`. `elif` ("else if") lets you check additional conditions in order; `else` is the catch-all for "none of the above."

## What Problem This Solves

Without branching, a program runs the exact same steps every single time, regardless of input. Branching lets the program react differently to different situations.

## When To Use It

Whenever the next step in a program depends on a condition: checking a guess, validating input, deciding which message to show.

## When Not To Use It

Don't stack unrelated `if` statements when you mean mutually-exclusive options — use `elif` so only one branch runs. Don't nest `if` inside `if` when a single `elif` chain would be clearer and flatter.

## Code Shape

```python
if condition_1:
    # runs only if condition_1 is True
elif condition_2:
    # runs only if condition_1 was False and condition_2 is True
else:
    # runs only if none of the above were True
```

## Tiny Working Example

```python
guess = 7
answer = 7

if guess == answer:
    print("Correct!")
elif guess < answer:
    print("Too low.")
else:
    print("Too high.")
```

## Beginner Mistakes

- Forgetting the colon `:` at the end of the `if`/`elif`/`else` line.
- Indentation mismatch — Python uses indentation to know what's *inside* the branch.
- Using separate `if` statements instead of `elif` when the conditions are mutually exclusive — this can accidentally run more than one branch.
- Forgetting `else` as a safety net for unexpected input.

## Physical-World Anchor

A flowchart with diamond-shaped decision boxes: each diamond is one `if`/`elif` check, and you follow exactly one path out of it, never more than one.

## Required Vocabulary

- [[glossary/if-elif-else]]
- [[glossary/branch]]
- [[glossary/truthy-falsy]]

## Related Code Patterns

- [[code-patterns/if-elif-else-decision-chain]]

## Drill

- [[drills/stage-02-decision-rules]]

## Explain-Back Questions

1. What's the difference between using three separate `if` statements versus `if`/`elif`/`elif`?
2. When would you reach for `else` instead of writing one more `elif`?
3. What happens if you forget the colon at the end of an `if` line?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.5, "Conditional Execution," "Alternative Execution," "Chained Conditionals," "Nested Conditionals")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.2)
- (source: Python Crash Course, 3rd Ed., Ch.5)
