---
type: glossary-entry
stage: 04
status: draft
aliases: []
related_terms: ["parameter", "call"]
timeline: reference
---

# Argument

## Plain-English Definition

The actual value you pass in when calling a function — it gets assigned to the matching parameter name.

## What Problem It Helps Solve

Lets you supply real, specific data to a generic, reusable function each time you call it.

## When Chris Will See It

Inside the parentheses at a function call site.

## Code Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chris")   # "Chris" is the argument
```

## Common Confusion

If you call a function with too few or too many arguments compared to what it expects, Python raises a `TypeError` naming the mismatch.

## Physical-World Anchor

What you actually write in the "Name: ____" blank on a form — the specific value, not the blank itself.

## Related Terms

- [[glossary/parameter]]
- [[glossary/call]]

## Flashcard Q/A

**Front:** What is an argument?

**Back:** The actual value passed into a function call, which gets assigned to the matching parameter.
