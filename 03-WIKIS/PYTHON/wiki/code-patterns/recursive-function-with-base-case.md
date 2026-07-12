---
type: code-pattern
stage: 08
status: draft
concepts: ["recursion", "base-case"]
tags: [stage-08, recursion]
---

# Code Pattern: Recursive Function With a Base Case

## Purpose

Solve a problem that's naturally defined in terms of a smaller version of itself, by having a function call itself until it reaches a simple, directly-answerable case.

## Use This When

The problem has a clear "smaller version of the same problem" structure: countdown, processing nested data, certain mathematical definitions (factorial, Fibonacci).

## Do Not Use This When

A plain loop expresses the same logic just as clearly — prefer the loop, since it's usually easier to read and avoids Python's recursion depth limit.

## Skeleton

```python
def recursive_function(n):
    if n == base_case_value:       # base case — stops the recursion
        return base_case_result
    else:
        return combine(n, recursive_function(smaller_version_of_n))
```

## Filled Example

```python
def factorial(n):
    if n == 0:                  # base case: 0! is defined as 1
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))   # 4 * 3 * 2 * 1 * 1 = 24
```

## Step-by-Step Trace

1. `factorial(4)` checks the base case (`n == 0`) — false, so it computes `4 * factorial(3)`.
2. `factorial(3)` similarly computes `3 * factorial(2)`, and so on, pausing each call while waiting on the next.
3. `factorial(0)` finally hits the base case and returns `1` directly.
4. The paused calls now resolve in reverse: `1 * 1 = 1`, then `2 * 1 = 2`, then `3 * 2 = 6`, then `4 * 6 = 24`.

## Beginner Mistakes

- Missing the base case, or writing one that's never reached — causes a `RecursionError: maximum recursion depth exceeded`.
- Forgetting to actually shrink the problem on the recursive call (calling `factorial(n)` instead of `factorial(n - 1)`).
- Trying to trace the function by reading top-to-bottom once instead of tracking the stack of paused calls.

## Related Terms

- [[glossary/recursion]]
- [[glossary/base-case]]

## Drill Link

- [[drills/stage-08-algorithms-and-classes-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-08-algorithms-and-classes]].
