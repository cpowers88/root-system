---
type: concept
stage: 05
status: draft
source_refs: ["Think Python Ch.8 (A String Is a Sequence, len, String Slices, Strings Are Immutable)", "Automate the Boring Stuff Ch.8"]
prerequisites: ["strings", "for-loops"]
tags: [stage-05, strings, sequences, slicing]
---

# Concept: Strings as Sequences

## Plain-English Meaning

A string isn't just "text" — it's a **sequence** of individual characters, each with a position (**index**) starting at 0. You can pull out single characters or ranges of characters (**slices**), but you can never change a string in place — strings are **immutable**.

## What Problem This Solves

Lets you work with parts of text precisely: the first letter, the last three characters, every other character — instead of treating a string as one indivisible blob.

## When To Use It

Any time you need a specific character or substring: validating the first letter of a name, checking a file extension, building a cipher.

## When Not To Use It

Don't try to assign to a string index (`name[0] = "J"`) — strings can't be modified in place. Build a new string instead.

## Code Shape

```python
text = "Python"
text[0]        # "P" — first character, index 0
text[-1]       # "n" — last character
text[1:4]      # "yth" — a slice from index 1 up to (not including) 4
len(text)      # 6
```

## Tiny Working Example

```python
word = "hello"
print(word[0])      # "h"
print(word[-1])     # "o"
print(word[1:3])    # "el"
print(len(word))    # 5
```

## Beginner Mistakes

- Forgetting indexing starts at 0, not 1 — `word[1]` is the *second* character.
- Trying to modify a string directly: `word[0] = "H"` raises `TypeError: 'str' object does not support item assignment`.
- Off-by-one in slices — `word[1:3]` stops *before* index 3, giving 2 characters, not 3.

## Physical-World Anchor

A string is like a row of numbered mailboxes on a street — you can look into any box by its number, but you can't change which house is at that address; you'd have to build a new street.

## Required Vocabulary

- [[glossary/index]]
- [[glossary/slice]]
- [[glossary/mutable-immutable]]

## Related Code Patterns

- [[code-patterns/list-loop-and-index]]

## Drill

- [[drills/stage-05-data-structure-practice]]

## Explain-Back Questions

1. What index does the first character of a string have?
2. Why does `word[0] = "H"` raise an error?
3. What does `word[1:3]` actually include — and what does it leave out?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.8, "A String Is a Sequence," "len," "String Slices," "Strings Are Immutable")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.8, "Strings and Text Editing")
