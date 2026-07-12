---
type: drill
stage: 08
status: draft
concepts: ["recursion", "base-case", "class", "object-instance", "attribute", "method", "big-o", "sorting", "searching"]
difficulty: beginner
solution_included: false
---

# Drill: Recursion, Classes, and Algorithm Reasoning

## Objective

Practice tracing recursive functions by hand, writing a simple class, and reasoning about Big O — three separate skills, each drilled briefly.

## Concepts Practiced

- recursion and base cases
- classes, `__init__`, attributes, methods
- Big O intuition

## Starter Prompt

**Part A — Trace recursion by hand:**

```python
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)
```

Trace `sum_to(4)` by hand: write out each call and what it's waiting on, before running the code to check.

**Part B — Write a class:**

Write a `Book` class with `__init__(self, title, pages)` and a method `summary(self)` that returns a string like `"'Title' has 200 pages."`. Create two different `Book` instances and call `summary()` on each.

**Part C — Big O reasoning (no code, just answer in writing):**

For each snippet, say whether it's closer to O(1), O(n), or O(n²), and explain why in one sentence:

```python
# Snippet 1
x = my_list[5]

# Snippet 2
for item in my_list:
    print(item)

# Snippet 3
for a in my_list:
    for b in my_list:
        if a == b:
            print("match")
```

## Requirements

- Part A: write the full trace before running, then compare.
- Part B: both `Book` instances must show different, correct data when `summary()` is called.
- Part C: answers must include a one-sentence reason, not just the label.

## Constraints

- No sorting/searching algorithm implementation required for this drill — that's covered in the mini-project instead.

## Expected Behavior

Part A's trace should match the actual recursive evaluation. Part B should print two distinct, correct summaries. Part C should correctly label all three snippets.

## Self-Check Questions

1. In Part A, how many "paused" calls exist at the deepest point of the recursion, right before `sum_to(0)` returns?
2. In Part B, what would happen if `summary()` forgot `self` as a parameter?
3. In Part C, what specifically about Snippet 3's structure makes it O(n²) instead of O(n)?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
