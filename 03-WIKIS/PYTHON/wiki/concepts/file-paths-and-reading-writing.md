---
type: concept
stage: 06
status: draft
source_refs: ["Think Python Ch.14 (Persistence, Reading and Writing, Filenames and Paths)", "Automate the Boring Stuff Ch.10", "Python Crash Course Ch.10"]
prerequisites: ["strings-as-sequences", "for-loops"]
tags: [files, paths]
timeline: reference
---

# Concept: File Paths, Reading, and Writing

## Plain-English Meaning

A **file path** is the address of a file on disk — either **relative** (relative to where the program runs from, like `"data.txt"`) or **absolute** (the full address from the drive root, like `"C:/Users/Chris/data.txt"`). Reading opens a file to pull data out; writing opens a file to put data in.

## What Problem This Solves

Variables disappear when a program ends — files are how a program saves data permanently and loads it back later.

## When To Use It

Whenever a program needs to remember something between runs, or process data that lives outside the program itself.

## When Not To Use It

If data only needs to exist while the program runs (no need to persist it), a variable is enough — don't reach for a file unnecessarily.

## Code Shape

```python
with open("filename.txt", "r") as f:   # "r" = read mode
    contents = f.read()

with open("filename.txt", "w") as f:   # "w" = write mode (overwrites!)
    f.write("some text")
```

## Tiny Working Example

```python
with open("notes.txt", "w") as f:
    f.write("Hello, file!")

with open("notes.txt", "r") as f:
    print(f.read())   # "Hello, file!"
```

## Beginner Mistakes

- Using a relative path and not realizing it depends on where the program is *run from*, not where the `.py` file is saved — this causes "file not found" errors that seem to happen randomly.
- Opening a file in `"w"` (write) mode when you meant to read — this erases the file's existing contents.
- Forgetting to close a file — using `with open(...) as f:` (the context manager pattern) handles this automatically; manually calling `.close()` is easy to forget.

## Physical-World Anchor

A file path is like a mailing address — relative paths are like "next door," meaningful only from where you're currently standing; absolute paths are like a full street address that works from anywhere.

## Required Vocabulary

- [[glossary/file-path]]
- [[glossary/open-read-write-close]]

## Related Code Patterns

- [[code-patterns/file-read-with-context-manager]]

## Drill

- [[drills/stage-06-debugging-practice]]

## Explain-Back Questions

1. What's the difference between a relative and an absolute file path?
2. Why does opening a file in `"w"` mode risk losing existing data?
3. What does the `with` keyword do for you automatically when working with files?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.14, "Persistence," "Reading and Writing," "Filenames and Paths")
- (source: Automate the Boring Stuff, 3rd Ed., Ch.10, "Reading and Writing Files")
- (source: Python Crash Course, 3rd Ed., Ch.10, "Reading from a File," "Writing to a File")
