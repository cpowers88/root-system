---
type: glossary-entry
stage: 05
status: draft
aliases: []
related_terms: ["list", "mutable-immutable"]
timeline: reference
---

# Aliasing

## Plain-English Definition

When two different variable names point to the *same* mutable object (usually a list), so changing it through one name also changes what the other name sees.

## What Problem It Helps Solve

It doesn't solve a problem — it's a behavior to be aware of, so you don't get surprised when a list "changes on its own" through what looks like an unrelated variable.

## When Chris Will See It

Any time a list is assigned to a new variable with `=`, expecting a separate copy.

## Code Example

```python
list_a = [1, 2, 3]
list_b = list_a       # NOT a copy — list_b is just another name for the same list
list_b.append(4)
print(list_a)            # [1, 2, 3, 4] — list_a changed too!
```

## Common Confusion

To actually make a copy, use `list_b = list_a.copy()` or `list_b = list_a[:]` — plain `=` never copies a list, it only creates a second name for the same one.

## Physical-World Anchor

Two nicknames for the same person — calling either nickname still reaches the same person, and anything that happens to them happens regardless of which name you used.

## Related Terms

- [[glossary/list]]
- [[glossary/mutable-immutable]]

## Flashcard Q/A

**Front:** Does `list_b = list_a` create a copy of the list?

**Back:** No — it makes `list_b` another name pointing to the exact same list. Changing one changes both.
