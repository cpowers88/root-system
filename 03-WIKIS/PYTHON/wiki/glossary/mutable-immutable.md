---
type: glossary-entry
stage: 05
status: draft
aliases: ["mutability", "immutability"]
related_terms: ["list", "string", "tuple"]
---

# Mutable / Immutable

## Plain-English Definition

**Mutable** means a value can be changed in place after it's created (lists). **Immutable** means it can't — any "change" actually creates a brand new value (strings, tuples, numbers).

## What Problem It Helps Solve

Explains why some operations work on lists but raise errors on strings or tuples, and why copying a mutable value needs extra care (see [[glossary/aliasing]]).

## When Chris Will See It

Any time code tries to modify something in place: `my_list[0] = x` works, `my_string[0] = x` doesn't.

## Code Example

```python
my_list = [1, 2, 3]
my_list[0] = 99        # works — lists are mutable

my_string = "abc"
my_string[0] = "z"      # TypeError — strings are immutable
```

## Common Confusion

"Immutable" doesn't mean you can't get a *new* value derived from the old one (`my_string.upper()` returns a new string) — it just means the original can't be changed in place.

## Physical-World Anchor

A whiteboard (mutable — erase and rewrite) versus a printed page (immutable — to "change" it, you print a new page).

## Related Terms

- [[glossary/list]]
- [[glossary/aliasing]]

## Flashcard Q/A

**Front:** What's the difference between mutable and immutable?

**Back:** Mutable values can be changed in place after creation (lists). Immutable values cannot — any change creates a new value (strings, tuples, numbers).
