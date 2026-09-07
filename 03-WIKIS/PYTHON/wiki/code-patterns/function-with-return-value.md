---
type: code-pattern
stage: 04
status: draft
concepts: ["function", "return-value", "fruitful-void-function"]
tags: [functions, return-values]
timeline: reference
---

# Code Pattern: Function With a Return Value

## Purpose

Write a function that computes a result and hands it back, so the calling code can use that result (store it, calculate with it, pass it along).

## Use This When

The function's whole point is to produce a value the rest of the program needs — a calculation, a transformation, a yes/no answer.

## Do Not Use This When

The function's job is purely an action with nothing meaningful to hand back (printing a message, for example) — that's a void function, and `return` isn't needed.

## Skeleton

```python
def function_name(parameter):
    result = parameter  # some calculation here
    return result

answer = function_name(some_value)
```

## Filled Example

```python
def square(n):
    return n * n

answer = square(4)
print(answer)          # 16
print(square(4) + 1)    # 17 — used directly inside another expression
```

## Step-by-Step Trace

1. `square(4)` is called; `n` is set to `4` inside the function.
2. `return n * n` computes `16` and immediately exits the function, handing `16` back to the call site.
3. `answer = square(4)` stores that returned value in `answer`.
4. `square(4) + 1` works because the function call itself evaluates to `16` first, then `+ 1` is applied.

## Beginner Mistakes

- Using `print()` inside the function instead of `return`, then trying to use the function's "result" afterward — it'll be `None`.
- Writing code after a `return` line in the same branch, expecting it to still execute — it won't; `return` exits immediately.
- Forgetting to capture the returned value (`square(4)` alone, with no `answer = `, just discards the result).

## Related Terms

- [[glossary/return-value]]
- [[glossary/fruitful-void-function]]

## Drill Link

- [[drills/stage-04-function-writing]]

## Flashcards To Create

- Already covered in [[flashcards/stage-04-functions]].
