---
type: concept
stage: 08
status: draft
source_refs: ["Think Python Ch.5 (Recursion, Stack Diagrams for Recursive Functions, Infinite Recursion)", "Grokking Algorithms Ch.3"]
prerequisites: ["defining-and-calling-functions", "if-elif-else"]
tags: [recursion, base-case]
timeline: reference
---

# Concept: Recursion

## Plain-English Meaning

**Recursion** is a function that calls itself to solve a smaller version of the same problem, until it reaches a **base case** — a version simple enough to answer directly, with no further recursive call needed.

## What Problem This Solves

Some problems are naturally defined in terms of smaller versions of themselves ("the factorial of 5 is 5 times the factorial of 4"). Recursion lets the code mirror that definition directly, instead of forcing it into a loop.

## When To Use It

When a problem can be broken into "solve a smaller version of the same problem, then combine the result" — counting down, processing nested structures, certain search/sort algorithms (Stage 8's algorithm topics use recursion under the hood).

## When Not To Use It

If a plain loop solves the problem just as clearly, prefer the loop — it's usually easier to read and doesn't risk hitting Python's recursion depth limit. Recursion shines specifically when the "smaller version of the same problem" framing is natural.

## Code Shape

```python
def recursive_function(n):
    if n == base_case_value:        # the base case — stops the recursion
        return base_case_result
    else:
        return combine(n, recursive_function(smaller_n))
```

## Tiny Working Example

```python
def countdown(n):
    if n <= 0:           # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)   # recursive call, with a smaller n

countdown(3)   # prints 3, 2, 1, Done!
```

## Beginner Mistakes

- Forgetting the base case entirely, or writing one that's never actually reached — causes infinite recursion and a `RecursionError`.
- Not making the problem smaller on each recursive call (e.g., calling `countdown(n)` instead of `countdown(n - 1)`) — same result, infinite recursion.
- Trying to trace a recursive function by reading top-to-bottom once, instead of tracking each call as it "pauses" waiting for the next one to finish (a stack of paused calls).

## Physical-World Anchor

Russian nesting dolls — each doll contains a smaller one, until you reach the smallest doll that doesn't open (the base case). Opening them all is like unwinding a recursive call.

## Required Vocabulary

- [[glossary/recursion]]
- [[glossary/base-case]]

## Related Code Patterns

- [[code-patterns/recursive-function-with-base-case]]

## Drill

- [[drills/stage-08-algorithms-and-classes-practice]]

## Explain-Back Questions

1. What two things must every correctly-written recursive function have?
2. What happens if a recursive function never reaches its base case?
3. Trace `countdown(3)` by hand — what gets printed, and in what order do the calls actually finish?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.5, "Recursion," "Stack Diagrams for Recursive Functions," "Infinite Recursion")
- (source: Grokking Algorithms, 2nd Ed., Ch.3, "Recursion")
