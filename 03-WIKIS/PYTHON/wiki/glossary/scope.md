---
type: glossary-entry
stage: 04
status: draft
aliases: ["local variable", "local scope"]
related_terms: ["parameter", "function"]
timeline: reference
---

# Scope

## Plain-English Definition

Where a variable can be seen and used. A variable created inside a function is **local** to it — it exists only while that function is running, and disappears once the function finishes.

## What Problem It Helps Solve

Keeps functions self-contained — a variable inside one function can't accidentally clash with or be overwritten by a variable with the same name somewhere else.

## When Chris Will See It

Any time a variable is created inside a function and then seems to "disappear" outside it.

## Code Example

```python
def add_one(n):
    result = n + 1   # result is local to add_one
    return result

print(add_one(5))   # 6
print(result)         # NameError — result doesn't exist out here
```

## Common Confusion

Changing a parameter's value *inside* a function doesn't change the original variable that was passed in as the argument — the parameter is a separate, local name.

## Physical-World Anchor

What happens in a sealed room stays in that room — once you leave (the function ends), nothing from inside is visible anymore, unless you carried something out with you (`return`).

## Related Terms

- [[glossary/parameter]]
- [[glossary/function]]

## Flashcard Q/A

**Front:** What happens to a variable created inside a function once the function finishes?

**Back:** It disappears — it was local to that function's scope and isn't visible outside it.
