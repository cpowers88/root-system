---
type: drill
timeline: next
stage: 04
status: ready
concepts: [module, import-statement, standard-library, function-call]
difficulty: beginner
solution_included: false
---

# Drill: Use Two Standard-Library Modules

## Objective

Practice importing a built-in module, calling one of its functions, and explaining
the `module.function(...)` shape.

## Concepts Practiced

- `import`
- standard-library modules
- dot notation
- arguments and return values

## Starter Prompt

Write two tiny, separate scripts:

1. Import `math`, ask for a non-negative number, and print its square root using
   `math.sqrt()`.
2. Import `random` and print one random whole number from 1 through 10 using
   `random.randint()`.

## Requirements

- Put each `import` near the top of its script.
- Call the function through the module name (`math.sqrt`, `random.randint`).
- Store each function's return value in a clearly named variable before printing.
- Explain which values are arguments and which values are return values.

## Constraints

- Use only the Python standard library; do not install anything.
- Do not use `from ... import *`.
- Keep each script under 10 lines so the focus stays on the import/call pattern.

## Expected Behavior

The math script prints the correct square root for a valid non-negative input. The
random script prints an integer within the inclusive range 1-10 on every run.

## Self-Check Questions

1. What error or failure would you expect if you removed `import math`?
2. Why does the call use `math.sqrt()` instead of only `sqrt()`?
3. Did `import random` install anything? Why not?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate
answer key and confirms this is not graded school work.
