---
type: concept
stage: 01
status: draft
source_refs: ["Think Python Ch.2 (String Operations)", "Python Crash Course Ch.2 (Strings)", "Automate the Boring Stuff Ch.1"]
prerequisites: ["values-and-expressions"]
tags: [stage-01, strings]
---

# Concept: Strings

## Plain-English Meaning

A **string** is text — any sequence of characters wrapped in quotes. Python doesn't care if you use single (`'...'`) or double (`"..."`) quotes, as long as the opening and closing quote match.

## What Problem This Solves

Programs need to work with words and sentences, not just numbers: names, messages, file contents, user input.

## When To Use It

Any time you're representing text: a name, a message to print, a label, a sentence built from pieces of data.

## When Not To Use It

Don't use a string to represent something you'll do math with (like an age or a price) — that needs a number (see [[concepts/numbers-and-type-conversion]]).

## Code Shape

```python
"some text"
'some text'
f"some text with a {variable} inside it"
```

## Tiny Working Example

```python
first_name = "Chris"
greeting = f"Hello, {first_name}!"
print(greeting)   # Hello, Chris!
```

## Beginner Mistakes

- Forgetting the quotes entirely — Python will think `Chris` is a variable name, not text, and raise a `NameError`.
- Mismatching quote types (starting with `'` and ending with `"`).
- Trying to glue a string and a number together with `+` instead of converting the number first, or using an f-string.

## Physical-World Anchor

Quotes are like quotation marks in a sentence you're reading aloud — they tell you "say this exactly as written," rather than "look up what this word means."

## Required Vocabulary

- [[glossary/string]]
- [[glossary/concatenation]]

## Related Code Patterns

- [[code-patterns/input-and-type-conversion]]

## Drill

- [[drills/stage-01-input-and-conversion]]

## Explain-Back Questions

1. Why does `print(Chris)` (no quotes) cause an error, but `print("Chris")` works?
2. What does an f-string let you do that a plain string can't?
3. What happens if you try `"Age: " + 25` instead of `f"Age: {25}"`?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.2, "String Operations")
- (source: Python Crash Course, 3rd Ed., Ch.2, "Strings" — including f-string usage under "Using Variables in Strings")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.1)
