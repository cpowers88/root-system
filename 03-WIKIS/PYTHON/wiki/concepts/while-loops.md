---
type: concept
stage: 03
status: draft
source_refs: ["Think Python Ch.7 (Reassignment, Updating Variables, The while Statement, break, Algorithms)", "Automate the Boring Stuff Ch.3", "Python Crash Course Ch.7"]
prerequisites: ["if-elif-else", "comparisons-and-boolean-logic"]
tags: [while-loop, break, continue]
timeline: reference
---

# Concept: `while` Loops, `break`, and `continue`

## Plain-English Meaning

A **`while` loop** repeats a block of code for as long as a condition stays `True`. **`break`** immediately exits the loop early. **`continue`** skips the rest of the current pass and jumps to the next check of the condition.

## What Problem This Solves

Some repetition isn't a fixed number of times — it depends on something happening: "keep asking until the user enters a valid number," "keep guessing until correct." A `for` loop can't express "until," but a `while` loop can.

## When To Use It

When you don't know in advance how many repetitions are needed — the loop should keep going until some condition changes.

## When Not To Use It

If you know exactly how many times to repeat, or you're iterating over a known sequence, use a `for` loop instead — it's harder to accidentally write an infinite loop with `for`.

## Code Shape

```python
while condition:
    # repeats as long as condition is True
    # something inside this loop must eventually make condition False
```

## Tiny Working Example

```python
guess = -1
while guess != 7:
    guess = int(input("Guess the number: "))
    if guess != 7:
        print("Try again.")
print("Correct!")
```

## Beginner Mistakes

- Forgetting to update whatever the condition depends on inside the loop — this causes an **infinite loop** that never ends.
- Confusing `break` (exit the loop entirely) with `continue` (skip to the next pass, but keep looping).
- Writing `while True:` without a `break` somewhere inside — this only works if there's a clear exit condition.

## Physical-World Anchor

Like stirring a pot "until it thickens" — you don't know exactly how many stirs that'll take, you just keep checking and stirring until the condition (thickness) changes.

## Required Vocabulary

- [[glossary/while-loop]]
- [[glossary/break-continue]]
- [[glossary/infinite-loop]]

## Related Code Patterns

- [[code-patterns/while-loop-until-condition]]

## Drill

- [[drills/stage-03-loop-tracing]]

## Explain-Back Questions

1. What's the key difference in when you'd choose `while` over `for`?
2. What is an infinite loop, and what's the most common way beginners accidentally write one?
3. What's the difference between `break` and `continue`?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.7, "Reassignment," "Updating Variables," "The while Statement," "break," "Algorithms")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.3)
- (source: Python Crash Course, 3rd Ed., Ch.7, "Introducing while Loops")
