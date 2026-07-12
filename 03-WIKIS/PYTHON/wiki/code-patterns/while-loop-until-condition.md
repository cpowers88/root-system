---
type: code-pattern
stage: 03
status: draft
concepts: ["while-loop", "infinite-loop", "break-continue"]
tags: [stage-03, while-loop]
---

# Code Pattern: `while` Loop Until a Condition Changes

## Purpose

Repeat an action until something becomes true (or false) — most commonly, validating input or repeating until success.

## Use This When

You don't know in advance how many repetitions are needed: "keep asking until valid," "keep guessing until correct."

## Do Not Use This When

You already know the number of repetitions or have a known sequence to step through — use [[code-patterns/for-loop-over-range]] instead, since it's harder to accidentally make infinite.

## Skeleton

```python
# set up whatever the condition depends on, before the loop
while condition:
    # do something
    # update whatever the condition depends on, so it can eventually become False
```

## Filled Example

```python
guess = -1
target = 7
while guess != target:
    guess = int(input("Guess the number: "))
print("Correct!")
```

## Step-by-Step Trace

1. `guess` starts at `-1`, which is not equal to `target` (7), so the condition `guess != target` is `True` and the loop body runs.
2. Each pass asks for a new guess and updates `guess`.
3. Once `guess` equals `target`, the condition becomes `False`, and the loop stops — control moves to the line after the loop.

## Beginner Mistakes

- Forgetting to update the variable the condition checks — guaranteed infinite loop.
- Setting the initial value (`guess = -1`) to something that could accidentally already satisfy the condition, ending the loop before it should start.
- Using `while True:` without a `break` somewhere that's actually reachable.

## Related Terms

- [[glossary/while-loop]]
- [[glossary/infinite-loop]]
- [[glossary/break-continue]]

## Drill Link

- [[drills/stage-03-loop-tracing]]

## Flashcards To Create

- Already covered in [[flashcards/stage-03-repetition]].
