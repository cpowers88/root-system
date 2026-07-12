---
type: tool-capability
status: active
stage: 5
python_tools: [str methods]
prerequisites: [strings, loops, lists]
tags: [reference, programming, capability]
---

# Capability: Clean Messy Text

## Real-World Problem

Names typed three different ways (`" chris "`, `"CHRIS"`, `"Chris "`), phone numbers with random dashes and spaces, copy-pasted data full of extra whitespace and inconsistent capitalization.

## Beginner Version

A script that takes a list of messy strings and normalizes each one: strip whitespace, fix capitalization, remove unwanted characters, and print the cleaned versions.

## Python Tools Involved

- `.strip()`, `.lower()`, `.upper()`, `.title()` — whitespace and case.
- `.replace(old, new)` — remove/swap characters.
- `.split()` and `"x".join(list)` — take apart and reassemble.
- `in` checks and `if` — decide what needs fixing.

## Prerequisites

[[stages/stage-01-python-atoms]] (strings), [[stages/stage-03-loops-and-repetition]] (apply to many items), [[stages/stage-05-data-shapes]] ([[concepts/strings-as-sequences]] is the home concept).

## Tiny Example

```python
raw_names = ["  chris POWERS ", "ROD smith", " ana  Diaz"]
for name in raw_names:
    clean = name.strip().title()
    print(clean)   # Chris Powers / Rod Smith / Ana  Diaz
```

## Mini-Project Idea

A "contact list cleaner": read 10 messy names/emails from a list, normalize them all, print a before/after table.

## School Relevance

Direct — string methods are core CSE 1321 material, and cleaning tasks are the most natural drill for them.

## Future Business Relevance

High — every client export (customer lists, job logs) arrives messy; cleaning is step one of any audit.

## Advanced Version — Parked

Regular expressions (ATBS Ch. 9 — Stage 8), NA-safe cleaning across whole spreadsheet columns with pandas (`.str` accessor — see [[string-manipulation-and-regex-in-pandas]], parked data-analysis strand). See [[parking-lot]].
