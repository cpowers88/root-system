---
type: drill
stage: 01
status: draft
concepts: ["variable", "input", "type-conversion", "string", "print"]
difficulty: beginner
solution_included: false
---

# Drill: Input and Conversion Practice

## Objective

Practice collecting input, converting it to the right type, and using it in both math and text output — without looking at notes.

## Concepts Practiced

- `input()`
- type conversion (`int()`, `float()`, `str()`)
- variables and assignment
- `print()` and f-strings

## Cold-Read Gate

Before writing your program, annotate this snippet without running it. Label each
input, conversion, assignment, calculation, and output; predict both the value and
type of `future_age` and the final printed line for the inputs `Chris` and `40`.

```python
name = input("Name: ")
age_text = input("Age: ")
age = int(age_text)
future_age = age + 5
print(f"{name}: {future_age}")
```

Then write an input-process-output skeleton for the Starter Prompt before filling
in any expressions.

## Starter Prompt

Write a short program that:

1. Asks the user for their name (text — no conversion needed).
2. Asks the user for their age (convert to `int`).
3. Asks the user for the price of something they want to buy (convert to `float`).
4. Prints a sentence using all three, including a calculation (e.g., "In 5 years, [name] will be [age + 5] years old, and the item will probably cost more than $[price].")

## Requirements

- Use `input()` exactly three times.
- Convert age and price to the correct numeric type before doing any math with them.
- Use an f-string for the final output.
- Do not hardcode the name, age, or price — they must come from the user.

## Constraints

- No loops, no functions, no conditionals — Stage 1 tools only.
- Keep it to one straight-through script (no branching).

## Expected Behavior

Running the program should pause three times for input, then print one sentence combining all three pieces of information with at least one calculated value inside it.

## Self-Check Questions

1. What type is `age` immediately after `input()`, before you convert it? What type is it after?
2. What would happen if you forgot to convert `price` and tried `price + 1.50`?
3. Why doesn't the name need any conversion?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
