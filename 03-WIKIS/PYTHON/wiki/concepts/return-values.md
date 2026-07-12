---
type: concept
stage: 04
status: draft
source_refs: ["Think Python Ch.3 (Fruitful Functions and Void Functions)", "Think Python Ch.6 (Return Values, Boolean Functions)", "Python Crash Course Ch.8 (Return Values)"]
prerequisites: ["defining-and-calling-functions", "parameters-and-arguments"]
tags: [stage-04, return-values, fruitful-void]
---

# Concept: Return Values

## Plain-English Meaning

`return` is how a function hands a value back to whatever called it. A function with a `return` that produces a value is called **fruitful**; a function that just does something (like printing) without handing back a value is called **void**.

## What Problem This Solves

`print()` only displays a value — it doesn't give the program anything to use afterward. `return` is what lets a function's result be stored in a variable, used in a calculation, or passed into another function.

## When To Use It

Whenever the function computes something the rest of the program needs to use — not just display.

## When Not To Use It

If a function's whole job is to perform an action (print something, save a file) and there's nothing meaningful to hand back, it doesn't need a `return` — that's a void function, and that's fine.

## Code Shape

```python
def function_name(parameter):
    result = parameter * 2
    return result

answer = function_name(5)   # answer now holds the returned value, 10
```

## Tiny Working Example

```python
def square(n):
    return n * n

result = square(4)
print(result)        # 16
print(square(4) + 1)  # 17 — the returned value can be used directly in an expression
```

## Beginner Mistakes

- Calling `print()` inside a function and assuming that's the same as `return` — it's not. `print()` only displays; `return` actually hands the value back to be used.
- Forgetting `return` entirely, then trying to use the function's "result" — without `return`, a function gives back `None` by default.
- Writing code *after* a `return` statement inside the same branch, expecting it to still run — `return` immediately exits the function.

## Physical-World Anchor

A vending machine: you put in money (argument), and it **returns** a snack (return value) — it doesn't just display the snack behind glass, it hands it to you to actually use.

## Required Vocabulary

- [[glossary/return-value]]
- [[glossary/fruitful-void-function]]

## Related Code Patterns

- [[code-patterns/function-with-return-value]]

## Drill

- [[drills/stage-04-function-writing]]

## Explain-Back Questions

1. What's the difference between a function that `print()`s a result and one that `return`s it?
2. What does a function return if it has no `return` statement at all?
3. What happens to any code written after a `return` statement, within the same function call?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.3, "Fruitful Functions and Void Functions")
- (source: Think Python, 2nd Ed., Ch.6, "Return Values," "Boolean Functions")
- (source: Python Crash Course, 3rd Ed., Ch.8, "Return Values")
