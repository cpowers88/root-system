---
type: concept
stage: 06
status: draft
source_refs: ["Think Python Ch.20 (Debugging: Syntax/Runtime/Semantic Errors)", "Invent Your Own Computer Games Ch.6 (Using the Debugger)"]
prerequisites: ["exceptions-and-tracebacks"]
tags: [stage-06, debugging, error-types]
---

# Concept: The Debugging Process

## Plain-English Meaning

Debugging is the systematic process of finding and fixing a program's mistake. Python errors fall into three categories: **syntax errors** (the code isn't valid Python at all — caught before the program even runs), **runtime errors** (the code is valid but crashes while running, like dividing by zero), and **semantic errors** (the code runs fine but produces the wrong result — no error message at all, the hardest kind to catch).

## What Problem This Solves

Every program will have bugs. Debugging isn't a sign of failure — it's a normal, expected, learnable skill. Having a process (rather than guessing randomly) makes bugs much faster to find.

## When To Use It

Any time a program crashes, behaves unexpectedly, or produces wrong output.

## When Not To Use It

N/A — debugging is always the right move when something's wrong. The skill is choosing *which technique* fits the symptom.

## Code Shape

```text
1. Read the error message (if there is one) — bottom line first.
2. Find the exact line it points to.
3. Check: is this a syntax error (won't run at all), a runtime error (crashes partway through), or a semantic error (runs, but wrong output)?
4. Add a print() statement near the suspect line to see what's actually happening.
5. Form a specific guess about the cause — don't just randomly change code.
6. Test the guess. If wrong, narrow down further.
```

## Tiny Working Example

```python
def average(numbers):
    total = 0
    for n in numbers:
        total = n   # BUG: should be total += n
    return total / len(numbers)

print(average([1, 2, 3]))   # prints 1.0 — wrong, but no error message
# Debug by adding: print(total) inside the loop to see it's not accumulating
```

## Beginner Mistakes

- Randomly changing code and re-running, hoping something works, instead of forming a specific hypothesis first.
- Ignoring a traceback's line number because "the code looks fine there" — the *symptom* often appears a few lines away from the actual *cause*.
- Giving up on semantic errors because there's no error message to point at — these require checking intermediate values with `print()`, since Python won't flag them itself.

## Physical-World Anchor

Like a doctor diagnosing symptoms — you don't just guess treatments randomly; you narrow down the cause systematically by checking specific things one at a time.

## Required Vocabulary

- [[glossary/syntax-runtime-semantic-error]]

## Related Code Patterns

- [[code-patterns/try-except-block]]

## Drill

- [[drills/stage-06-debugging-practice]]

## Explain-Back Questions

1. What's the difference between a syntax error, a runtime error, and a semantic error?
2. Why is a semantic error often harder to find than the other two types?
3. What's the first concrete step you should take when a program crashes with a traceback?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.20, "Syntax Errors," "Runtime Errors," "Semantic Errors")
- (source: Invent Your Own Computer Games with Python, 4th Ed., Ch.6, "Using the Debugger")
