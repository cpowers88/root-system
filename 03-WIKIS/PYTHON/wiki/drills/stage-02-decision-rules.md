---
type: drill
stage: 02
status: draft
concepts: ["condition", "if-elif-else", "boolean-operators", "comparison-operator"]
difficulty: beginner
solution_included: false
---

# Drill: Plain-English Rules to `if` Chains

## Objective

Practice translating a plain-English decision rule directly into an `if`/`elif`/`else` chain, without looking at notes.

## Concepts Practiced

- comparison operators
- `and` / `or` / `not`
- `if` / `elif` / `else`
- choosing `elif` vs. separate `if` statements

## Cold-Read Gate

Before writing, trace this code for scores `95`, `84`, and `62`. For each input,
record each condition reached, its Boolean result, the branch selected, and the
output. Explain why later branches are skipped after a match.

```python
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
else:
    result = "below B"
print(result)
```

For every Starter Prompt rule, write only the ordered conditions and empty branch
skeleton first. Add the branch actions after the order is correct.

## Starter Prompt

For each rule below, write a short Python snippet (using `input()` where a value is needed) that implements it exactly:

1. "If it's raining and I don't have an umbrella, stay inside. If it's raining and I do have an umbrella, go out with the umbrella. Otherwise, just go out."
2. "A movie ticket costs $12. If you're under 13 or over 65, it costs $8 instead."
3. "Grade the score: 90 or above is an A, 80-89 is a B, 70-79 is a C, anything below 70 is an F."

## Requirements

- Use comparison operators and `and`/`or` where the rule calls for combining conditions.
- Use `elif` (not separate `if` statements) wherever the outcomes are mutually exclusive.
- Include an `else` wherever the rule has a clear "otherwise" case.

## Constraints

- No loops, no functions — Stage 1-2 tools only.
- Each snippet should be a single straight-through script using `input()` for any values it needs.

## Expected Behavior

Each snippet should print exactly one outcome per run, matching the plain-English rule precisely — test each one with at least two different inputs to confirm different branches trigger correctly.

## Self-Check Questions

1. For rule 1, what would happen if you used three separate `if` statements instead of `if`/`elif`/`else`? Try it and see.
2. For rule 2, why does the condition need `or` instead of `and`?
3. For rule 3, what's the correct order to check the grade boundaries in, and why does order matter here?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
