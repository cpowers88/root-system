---
type: concept
stage: 05
status: draft
source_refs: ["Think Python Ch.11 (A Dictionary Is a Mapping, Looping and Dictionaries)", "Python Crash Course Ch.6", "Automate the Boring Stuff Ch.7"]
prerequisites: ["lists", "for-loops"]
tags: [stage-05, dictionaries, key-value]
---

# Concept: Dictionaries

## Plain-English Meaning

A **dictionary** stores data as **key-value pairs** — each value is looked up by a meaningful label (the key) instead of a numeric position. Written in curly braces: `{key: value}`.

## What Problem This Solves

A list works well when position matters or items are interchangeable. But "store a person's age" doesn't naturally have a position — it has a *name*. Dictionaries let you look things up by a label that makes sense.

## When To Use It

Whenever data is naturally labeled rather than ordered: a person's attributes, word counts, settings/configuration, anything you'd describe as "the X of Y."

## When Not To Use It

If the data is just an ordered sequence with no natural label (a list of scores, a queue of tasks), a list is simpler and more appropriate.

## Code Shape

```python
my_dict = {"key1": value1, "key2": value2}
my_dict["key1"]              # look up by key
my_dict["new_key"] = value    # add a new key-value pair
for key in my_dict:
    # loop over keys
for key, value in my_dict.items():
    # loop over key-value pairs together
```

## Tiny Working Example

```python
student = {"name": "Chris", "age": 16, "grade": "A"}
print(student["name"])     # "Chris"
student["age"] = 17         # update an existing value
for key, value in student.items():
    print(f"{key}: {value}")
```

## Beginner Mistakes

- Looking up a key that doesn't exist — `KeyError: 'key_name'`. Use `.get("key_name")` if a missing key should produce `None` instead of crashing.
- Confusing the key with the value when reading dictionary code: `student["name"]` reads "name," but returns the *value* stored under that key.
- Trying to access a dictionary by numeric position like a list (`student[0]`) — dictionaries aren't ordered by position; they're looked up by key.

## Physical-World Anchor

A dictionary (the book kind!) — you look up a word (the key) to find its definition (the value). You don't flip to "page 5" expecting a specific word; you look up the word directly.

## Required Vocabulary

- [[glossary/dictionary]]
- [[glossary/dictionary-key-value-pair]]

## Related Code Patterns

- [[code-patterns/dictionary-lookup]]

## Drill

- [[drills/stage-05-data-structure-practice]]

## Explain-Back Questions

1. What's the key difference between how you look something up in a list versus a dictionary?
2. What error do you get from looking up a missing key, and how can you avoid it?
3. Give an example of data that's a better fit for a dictionary than a list, and explain why.

## Source Notes

- (source: Think Python, 2nd Ed., Ch.11, "A Dictionary Is a Mapping," "Looping and Dictionaries")
- (source: Python Crash Course, 3rd Ed., Ch.6)
- (source: Automate the Boring Stuff, 3rd Ed., Ch.7, "Dictionaries and Structuring Data")
