---
type: glossary-entry
stage: 02
status: draft
aliases: ["truthiness"]
related_terms: ["boolean", "condition"]
---

# Truthy / Falsy

## Plain-English Definition

Python treats some non-Boolean values as if they were `True` or `False` when used in a condition. Empty things (`""`, `0`, `[]`, `None`) count as **falsy**; almost everything else counts as **truthy**.

## What Problem It Helps Solve

Lets you write `if my_list:` instead of the longer `if len(my_list) > 0:` — shorter, common Python style once you know the rule.

## When Chris Will See It

Occasionally in other people's code, and worth knowing about now even though Stage 2 won't drill it heavily — it becomes more useful once lists/strings are introduced in Stage 5.

## Code Example

```python
name = ""
if name:
    print("Has a name")
else:
    print("No name yet")   # this runs, because "" is falsy
```

## Common Confusion

`0` is falsy but `"0"` (the string) is truthy — a non-empty string is always truthy, even if its *contents* look like a falsy value.

## Physical-World Anchor

An empty box still "exists," but if you ask "is there anything in here?" the honest answer for an empty box is no — that's falsy.

## Related Terms

- [[glossary/boolean]]
- [[glossary/condition]]

## Flashcard Q/A

**Front:** Is `0` truthy or falsy? Is `"0"` (the string) truthy or falsy?

**Back:** `0` is falsy. `"0"` is truthy, because it's a non-empty string.
