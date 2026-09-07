---
type: code-pattern
stage: 06
status: draft
concepts: ["exception", "try-except"]
tags: [exceptions, try-except]
timeline: reference
---

# Code Pattern: `try` / `except` Block

## Purpose

Attempt an operation that might fail in a known, specific way, and provide a graceful fallback instead of letting the program crash.

## Use This When

You can name the *specific* exception you expect (e.g., `ValueError` from a bad conversion, `FileNotFoundError` from a missing file) and you have a sensible response ready.

## Do Not Use This When

You're not sure what could go wrong, or you'd just be hiding a bug rather than handling an expected, recoverable case. Fix the underlying issue instead of wrapping it in a vague `try`/`except`.

## Skeleton

```python
try:
    risky_code()
except SpecificErrorType:
    fallback_code()
```

## Filled Example

```python
try:
    age = int(input("Age? "))
except ValueError:
    print("That wasn't a valid number — using 0 instead.")
    age = 0

print(f"Age recorded: {age}")
```

## Step-by-Step Trace

1. Python runs everything inside `try:` normally.
2. If `int(input(...))` raises a `ValueError` (because the input wasn't a valid number), Python immediately jumps to the matching `except ValueError:` block.
3. If no exception occurs, the `except` block is skipped entirely, and execution continues after the whole `try`/`except`.

## Beginner Mistakes

- Catching the wrong exception type (or a bare `except:`), which can mask bugs that have nothing to do with the case you meant to handle.
- Putting too much code inside `try:` — if anything in that block could fail for many different reasons, it gets hard to know which one actually triggered the `except`.
- Forgetting that code after the `except` block still runs normally — `except` doesn't end the program, it just handles that one failure and moves on.

## Related Terms

- [[glossary/exception]]
- [[glossary/try-except]]

## Drill Link

- [[drills/stage-06-debugging-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-06-files-errors-debugging]].
