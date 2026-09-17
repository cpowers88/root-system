---
type: tool-capability
status: active
stage: 2
python_tools: [if/elif/else, functions, dictionaries]
prerequisites: [conditionals, comparisons]
tags: [programming, capability]
timeline: reference
---

# Capability: Automate Repetitive Decisions

## Real-World Problem

Any judgment made the same way over and over: "Is this grade an A, B, or C?", "Does this order get free shipping?", "Which folder does this file belong in?", "Is this expense normal or flagged?" Humans get bored and inconsistent; a rule written once runs the same way forever.

## Beginner Version

A function that takes one input and returns one decision, using an `if`/`elif`/`else` chain that mirrors the plain-English rule. Then a loop applies it to a whole list.

## Python Tools Involved

- `if` / `elif` / `else` — the rule itself.
- Comparison + Boolean operators (`and`, `or`, `not`) — compound conditions.
- Functions — name the rule, reuse it everywhere.
- A `for` loop — apply the rule to many items at once.

## Prerequisites

[[stages/stage-02-decisions-and-boolean-logic]] — this is *the* Stage 2 capability. Scale-up needs [[stages/stage-03-loops-and-repetition]] and [[stages/stage-04-functions-parameters-return]]. Pattern: [[code-patterns/if-elif-else-decision-chain]].

## Tiny Example

```python
def shipping(order_total):
    if order_total >= 50:
        return "free"
    elif order_total >= 25:
        return "discounted"
    else:
        return "standard"

for total in [12.50, 30, 75]:
    print(total, "->", shipping(total))
```

## Mini-Project Idea

A triage script: loop over a list of expenses and label each `ok`, `review`, or `flagged` based on 2-3 rules Chris writes in plain English first, then translates to code (Stage 7 practice built in).

## School Relevance

Very high — selection is two full weeks of the CSE lecture schedule; this is its real-world shape.

## Future Business Relevance

Very high — audit rules ("flag any job where materials exceed 40% of invoice") are exactly this pattern, applied to client data rows.

## Advanced Version — Parked

Rules tables driven by dictionaries/config files, `match` statements, decision engines, and anything machine-learning-shaped (far beyond this vault's scope). See [[parking-lot]].
