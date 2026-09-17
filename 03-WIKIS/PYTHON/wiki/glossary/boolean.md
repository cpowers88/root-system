---
type: glossary-entry
stage: 02
status: draft
aliases: ["bool"]
related_terms: ["condition", "truthy-falsy"]
timeline: reference
---

# Boolean

## Plain-English Definition

A value that is either `True` or `False` — Python's `bool` type. Named after George Boole, who formalized this kind of logic.

## What Problem It Helps Solve

Gives a program a definite, two-state answer to a yes/no question, which `if`/`elif`/`while` can act on.

## When Chris Will See It

As the result of any comparison (`age == 18`) or Boolean combination (`a and b`).

## Code Example

```python
is_adult = age >= 18   # is_adult is now True or False
print(type(is_adult))    # <class 'bool'>
```

## Common Confusion

`True` and `False` are capitalized keywords in Python, not strings — `"True"` (with quotes) is just text, not the Boolean value.

## Physical-World Anchor

A light switch: on or off, nothing in between.

## Related Terms

- [[glossary/condition]]
- [[glossary/truthy-falsy]]

## Flashcard Q/A

**Front:** What is a Boolean value?

**Back:** A value that is either True or False — Python's `bool` type.
