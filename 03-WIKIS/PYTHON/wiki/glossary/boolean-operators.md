---
type: glossary-entry
stage: 02
status: draft
aliases: ["and", "or", "not", "logical operators"]
related_terms: ["boolean", "condition"]
---

# Boolean Operators (`and`, `or`, `not`)

## Plain-English Definition

Words that combine or invert Boolean values: `and` (both must be True), `or` (at least one must be True), `not` (flips True to False and vice versa).

## What Problem It Helps Solve

Lets a program test more than one condition at once, instead of writing deeply nested separate `if` statements for every combination.

## When Chris Will See It

Whenever a decision depends on more than one thing being true: "is the user old enough AND a resident?"

## Code Example

```python
age >= 13 and age <= 19      # both must be True
day == "Saturday" or day == "Sunday"   # either can be True
not is_logged_in              # flips True/False
```

## Common Confusion

`and` requires **both** sides to be `True` — if either side is `False`, the whole thing is `False`. `or` only needs **one** side to be `True`. These get reversed by beginners surprisingly often.

## Physical-World Anchor

`and` is like needing both a ticket *and* an ID to get in. `or` is like accepting either cash *or* card to pay.

## Related Terms

- [[glossary/boolean]]
- [[glossary/condition]]

## Flashcard Q/A

**Front:** What's the difference between `and` and `or`?

**Back:** `and` needs both conditions to be True. `or` only needs one of them to be True.
