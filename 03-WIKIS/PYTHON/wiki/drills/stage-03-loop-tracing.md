---
type: drill
stage: 03
status: draft
concepts: ["for-loop", "while-loop", "range", "counter", "accumulator", "break-continue", "modulo-and-divisibility"]
difficulty: beginner
solution_included: false
timeline: reference
---

# Drill: Loop Tracing and Loop Writing

## Objective

Practice both directions: predicting what a loop will print by tracing it by hand, and writing a loop from scratch to match a plain-English goal.

## Concepts Practiced

- `for` loops and `range()`
- `while` loops
- counters and accumulators
- `break` / `continue`
- modulo (`%`) and divisibility

## Starter Prompt

**Part A — Trace by hand (no running the code first):**

For each snippet below, write down exactly what it will print, before running it to check.

```python
# Snippet 1
for i in range(3):
    print(i * 2)

# Snippet 2
total = 0
for n in range(1, 5):
    total += n
print(total)

# Snippet 3
count = 0
while count < 10:
    count += 2
    if count == 6:
        break
print(count)
```

**Part B — Write from scratch:**

1. Write a `for` loop that prints every number from 10 down to 1 (use `range()`'s step argument).
2. Write a `while` loop that keeps asking the user "Continue? (yes/no)" until they type "no".
3. Write a loop (your choice of `for` or `while`) that counts how many numbers from 1 to 50 are divisible by 7, using a counter.

Before Part B.3, read [[concepts/modulo-and-divisibility]] only if you cannot
explain why `number % 7 == 0` means “divisible by 7.” Trace the remainders for
`6`, `7`, and `8` before building the loop; this is a concept check, not a solution.

## Requirements

- Part A: write your predicted output *before* running each snippet, then compare.
- Part B: each program should run standalone and produce visible output confirming it worked.

## Constraints

- No functions, no lists/dictionaries yet — Stage 1-3 tools only.

## Expected Behavior

Part A predictions should match actual output once run. Part B programs should each demonstrate the loop type and pattern requested without errors.

## Self-Check Questions

1. In Snippet 3, why does the loop stop at `count == 6` instead of continuing to 10?
2. For Part B's divisible-by-7 counter, why does the counter need to start at 0 before the loop?
3. Which of the Part B problems would have been awkward or impossible with a `for` loop instead of `while` (or vice versa)?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
