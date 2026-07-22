---
type: drill
stage: 04
status: draft
concepts: ["function", "def", "call", "parameter", "argument", "return-value", "scope"]
difficulty: beginner
solution_included: false
---

# Drill: Write Three Functions from a Spec

## Objective

Practice writing functions with parameters and return values from a plain-English description, without copying an existing pattern.

## Concepts Practiced

- `def` and function calls
- parameters and arguments
- `return` vs. `print()`
- scope (local variables)

## Cold-Read Gate

Trace the snippet without running it. Mark the caller, argument, parameter, local
variable, returned value, and final output. Explain why the caller can use
`converted` but cannot directly use `result`.

```python
def add_tax(price):
    result = price * 1.08
    return result

converted = add_tax(10)
print(converted)
```

Before completing the Starter Prompt, write all three function signatures and a
one-line return/print contract for each. Only then fill in the bodies.

## Starter Prompt

Write three separate functions:

1. `fahrenheit_to_celsius(f)` — takes a Fahrenheit temperature and **returns** the Celsius equivalent (`(f - 32) * 5/9`).
2. `is_even(n)` — takes a number and **returns** `True` if it's even, `False` if it's odd. (No `if`/`else` needed if you're comfortable with a direct Boolean expression — either approach is fine.)
3. `shout(message)` — takes a string and **prints** it in all uppercase, followed by three exclamation marks. (This one is void — no `return` needed.)

Then write a few lines of calling code that uses all three functions and prints their results (for the two fruitful ones).

## Requirements

- Each function must use a parameter — no hardcoded values inside the function bodies.
- `fahrenheit_to_celsius` and `is_even` must use `return`, not `print()`, inside the function.
- `shout` should use `print()`, not `return` — confirm you understand why this one doesn't need to return anything.
- Call each function at least twice with different arguments to confirm it behaves correctly each time.

## Constraints

- No loops, no conditionals required (though `is_even` may optionally use one) — keep focus on functions themselves.
- Don't use any built-in temperature/even-check functions — write the logic yourself.

## Expected Behavior

Running the calling code should print the Celsius conversion for at least two different Fahrenheit values, `True`/`False` for at least two different numbers, and a shouted version of at least one message.

## Self-Check Questions

1. For `fahrenheit_to_celsius`, what would happen if you used `print()` instead of `return` inside it, and then tried `temp = fahrenheit_to_celsius(98.6) + 1`?
2. Why doesn't `shout` need a `return` statement?
3. If you tried to print the parameter variable from inside one function, from outside that function (after it returns), what would happen?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
