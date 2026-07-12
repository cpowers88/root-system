---
type: glossary-entry
stage: 01
status: draft
aliases: []
related_terms: ["string"]
---

# Concatenation

## Plain-English Definition

Joining two strings together end-to-end, usually with `+`.

## What Problem It Helps Solve

Lets you build a longer piece of text out of smaller pieces — combining a label with a name, for example.

## When Chris Will See It

Whenever text is being assembled from parts: `"Hello, " + name + "!"`. Often replaced by f-strings, which do the same job more readably.

## Code Example

```python
first = "Py"
second = "thon"
print(first + second)   # "Python"
```

## Common Confusion

`+` only concatenates when both sides are strings. `"Age: " + 25` fails because `25` is a number, not text — it must be converted with `str()` first, or an f-string used instead.

## Physical-World Anchor

Like taping two strips of paper end-to-end to make one longer strip.

## Related Terms

- [[glossary/string]]

## Flashcard Q/A

**Front:** What is string concatenation?

**Back:** Joining two strings together, usually with `+`, to form one longer string.
