---
type: drill
stage: 06
status: draft
concepts: ["file-path", "open-read-write-close", "exception", "traceback", "try-except", "syntax-runtime-semantic-error"]
difficulty: beginner
solution_included: false
---

# Drill: Read the Traceback, Fix the Bug

## Objective

Practice reading real tracebacks to locate and fix bugs, and writing `try`/`except` blocks around genuinely risky operations.

## Concepts Practiced

- reading tracebacks bottom-up
- identifying syntax vs. runtime vs. semantic errors
- `try`/`except` with a specific exception type
- file reading/writing with a context manager

## Starter Prompt

**Part A — Diagnose without running (predict first):**

For each snippet, write down: (1) which error type you expect, if any, and (2) the fix — before running it to check.

```python
# Snippet 1
def half(n):
    return n / 2

print(half("10"))

# Snippet 2
scores = [85, 92, 78]
print(scores[3])

# Snippet 3
with open("does_not_exist.txt", "r") as f:
    print(f.read())
```

**Part B — Write it yourself:**

1. Write a small program that asks the user for a number and divides 100 by it, using `try`/`except` to handle both a non-numeric input (`ValueError`) and a division by zero (`ZeroDivisionError`) — with a different message for each.
2. Write a program that writes three lines to a file, then reads them back and prints how many lines there are.

## Requirements

- Part A: write your prediction *before* running each snippet.
- Part B: both programs should run without crashing on any reasonable input, including the failure cases being tested for.

## Constraints

- No advanced exception hierarchies — just catch the specific exception types named above.

## Expected Behavior

Part A predictions should match the actual tracebacks once run. Part B's first program should handle both failure cases gracefully with distinct messages; the second should correctly report the line count.

## Self-Check Questions

1. In Snippet 1, what type of error occurs, and why does dividing a string by 2 fail that way?
2. In Snippet 3, is this a syntax, runtime, or semantic error — and how do you know?
3. For Part B's divide program, why does it need two separate `except` clauses instead of one?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
