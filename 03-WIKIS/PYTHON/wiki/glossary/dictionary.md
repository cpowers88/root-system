---
type: glossary-entry
stage: 05
status: draft
aliases: ["dict"]
related_terms: ["dictionary-key-value-pair", "list"]
timeline: reference
---

# Dictionary

## Plain-English Definition

A collection of key-value pairs, written in curly braces: `{key: value, key2: value2}`. Values are looked up by their key, not by position.

## What Problem It Helps Solve

Lets a program store labeled data, where looking something up by a meaningful name makes more sense than by numeric position.

## When Chris Will See It

Anywhere data has a natural label: a person's attributes, settings, counts keyed by name.

## Code Example

```python
student = {"name": "Chris", "age": 16}
student["age"]   # 16
```

## Common Confusion

Dictionaries aren't accessed by numeric position like lists — `student[0]` doesn't mean "the first item," it means "look up the key `0`," which probably doesn't exist and raises `KeyError`.

## Physical-World Anchor

A book dictionary — you look up a word (key) to find its definition (value); you don't flip to "page 5" expecting a specific word.

## Related Terms

- [[glossary/dictionary-key-value-pair]]

## Flashcard Q/A

**Front:** How do you look something up in a dictionary?

**Back:** By its key, not by numeric position.
