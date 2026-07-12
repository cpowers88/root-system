---
type: tool-capability
status: active
stage: 6
python_tools: [if/elif/else, try/except]
prerequisites: [conditionals, functions, exceptions]
tags: [reference, programming, capability]
---

# Capability: Validate Input and Data

## Real-World Problem

A form where someone typed `"twelve"` in the age box. An empty required field. A price of `-50`. Any place where bad input must be caught *before* it breaks something or pollutes a dataset.

## Beginner Version

A script that asks for input, checks it against rules (right type? in range? not empty?), and either accepts it or re-asks with a clear message.

## Python Tools Involved

- `if` / `elif` / `else` — the rules.
- `try`/`except ValueError` — catch failed conversions like `int("twelve")`.
- `while` — keep asking until valid.
- Functions — package each rule as a reusable check.

## Prerequisites

[[stages/stage-02-decisions-and-boolean-logic]] (rules), [[stages/stage-03-loops-and-repetition]] (re-ask loop), [[stages/stage-04-functions-parameters-return]] (reusable checks), [[stages/stage-06-files-errors-debugging]] ([[code-patterns/try-except-block]]).

## Tiny Example

```python
while True:
    text = input("Age: ")
    try:
        age = int(text)
    except ValueError:
        print("Numbers only, please.")
        continue
    if 0 < age < 120:
        break
    print("That age doesn't look right.")
print(f"Saved age: {age}")
```

## Mini-Project Idea

A sign-up validator: collect name, age, and email; reject empty names, non-numeric or out-of-range ages, and emails without `@`; print the clean record at the end.

## School Relevance

High — selection, loops, and exceptions are all syllabus topics, and validation is their most natural combined exercise.

## Future Business Relevance

High — data-quality checks ("how many rows fail this rule?") are the first step of any audit deliverable.

## Advanced Version — Parked

Validating whole files/columns at once (pandas missing-data tools — [[pandas-missing-data-and-duplicates]], parked strand), schema validators, and SQL constraints ([[sql-table-design-constraints-and-indexes]], parked strand). See [[parking-lot]].
