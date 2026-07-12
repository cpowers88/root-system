---
type: code-pattern
stage: 02
status: draft
concepts: ["condition", "if-elif-else", "branch", "boolean-operators"]
tags: [stage-02, conditionals, decision-chain]
---

# Code Pattern: `if` / `elif` / `else` Decision Chain

## Purpose

Make the program take a different action depending on which of several mutually-exclusive conditions is true.

## Use This When

You have a set of conditions where exactly one outcome should happen — checking a guess against a target, validating a range, classifying a value into one of several categories.

## Do Not Use This When

The conditions aren't mutually exclusive (more than one might need to trigger independently) — use separate `if` statements instead. Also don't reach for this if there's only one condition with no alternative — a plain `if` is enough.

## Skeleton

```python
if condition_1:
    # action for condition_1
elif condition_2:
    # action for condition_2
else:
    # fallback action
```

## Filled Example

```python
guess = int(input("Guess a number 1-10: "))
answer = 7

if guess == answer:
    print("Correct!")
elif guess < answer:
    print("Too low.")
elif guess > answer:
    print("Too high.")
else:
    print("Something went wrong.")
```

## Step-by-Step Trace

1. Python checks `guess == answer` first. If True, that branch runs and the rest are skipped entirely.
2. If False, it checks `guess < answer` next, only if it got this far.
3. If that's also False, it checks `guess > answer`.
4. `else` only runs if none of the above were True (here, effectively impossible given the math, but it's good practice as a safety net).

## Beginner Mistakes

- Using `=` instead of `==` in a condition.
- Forgetting the colon `:` after each `if`/`elif`/`else`.
- Indentation mismatch between the condition line and its body.
- Writing separate `if` statements instead of `elif`, which can let multiple branches run when only one should.

## Related Terms

- [[glossary/condition]]
- [[glossary/if-elif-else]]
- [[glossary/branch]]

## Drill Link

- [[drills/stage-02-decision-rules]]

## Flashcards To Create

- Already covered in [[flashcards/stage-02-decisions]].
