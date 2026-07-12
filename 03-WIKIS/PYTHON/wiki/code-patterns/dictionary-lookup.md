---
type: code-pattern
stage: 05
status: draft
concepts: ["dictionary", "dictionary-key-value-pair"]
tags: [stage-05, dictionaries, lookup]
---

# Code Pattern: Dictionary Lookup (Safe and Unsafe)

## Purpose

Retrieve a value from a dictionary by its key, either trusting the key exists or safely handling the case where it might not.

## Use This When

You need to retrieve, check, or update data that's stored under a meaningful label rather than a position.

## Do Not Use This When

The data doesn't have a natural label and is just an ordered group of similar items — use a list and index instead.

## Skeleton

```python
# unsafe — crashes if the key doesn't exist
value = my_dict[key]

# safe — returns a default instead of crashing
value = my_dict.get(key, default_value)
```

## Filled Example

```python
student = {"name": "Chris", "age": 16}

age = student["age"]              # works — "age" exists
grade = student.get("grade", "N/A")  # "grade" doesn't exist — returns "N/A" instead of crashing
```

## Step-by-Step Trace

1. `student["age"]` looks up the key `"age"` directly. Since it exists, it returns `16`.
2. `student.get("grade", "N/A")` looks up `"grade"`. Since it's missing, instead of raising `KeyError`, `.get()` returns the fallback value `"N/A"`.

## Beginner Mistakes

- Using `student[key]` for a key that might not exist, causing an unhandled `KeyError`.
- Forgetting `.get()` needs a default as its second argument if you want a custom fallback — without one, it returns `None`.
- Trying to look up a dictionary by position (`student[0]`) instead of by key.

## Related Terms

- [[glossary/dictionary]]
- [[glossary/dictionary-key-value-pair]]

## Drill Link

- [[drills/stage-05-data-structure-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-05-data-shapes]].
