---
type: glossary-entry
stage: 01
status: draft
aliases: ["str"]
related_terms: ["concatenation", "type-conversion"]
timeline: reference
---

# String

## Plain-English Definition

Text — any sequence of characters wrapped in matching quotes (single or double).

## What Problem It Helps Solve

Lets a program represent and work with words, names, sentences, and any other text.

## When Chris Will See It

Any time text is involved: names, messages, prompts, file contents.

## Code Example

```python
name = "Chris"
greeting = f"Hello, {name}!"
```

## Common Confusion

A string that *looks* like a number (`"42"`) is still text, not a number, until it's converted with `int()` or `float()`. You can't do math on it directly.

## Physical-World Anchor

Quotation marks are like quotes in a sentence you're reading aloud — "say this exactly," not "look this word up."

## Related Terms

- [[glossary/concatenation]]
- [[glossary/type-conversion]]

## Flashcard Q/A

**Front:** What is a string?

**Back:** Text in Python — any characters wrapped in matching single or double quotes.
