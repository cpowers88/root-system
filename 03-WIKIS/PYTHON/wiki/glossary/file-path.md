---
type: glossary-entry
stage: 06
status: draft
aliases: ["relative path", "absolute path"]
related_terms: ["open-read-write-close"]
timeline: reference
---

# File Path

## Plain-English Definition

The address of a file on disk. A **relative** path is relative to wherever the program is run from; an **absolute** path is the full address from the drive root.

## What Problem It Helps Solve

Tells Python exactly which file to open, the same way a street address tells a mail carrier where to deliver.

## When Chris Will See It

Inside `open()`: `open("data.txt")` (relative) or `open("C:/Users/Chris/data.txt")` (absolute).

## Code Example

```python
open("notes.txt")                      # relative — depends on current working directory
open("C:/Users/Chris/notes.txt")       # absolute — works from anywhere
```

## Common Confusion

A relative path depends on where the program is *run from* (the current working directory), not where the `.py` file itself is saved — this causes "file not found" errors that seem inconsistent between running from VS Code vs. a terminal.

## Physical-World Anchor

"Next door" (relative — meaningful only from where you're standing) versus a full street address (absolute — works no matter where you start).

## Related Terms

- [[glossary/open-read-write-close]]

## Flashcard Q/A

**Front:** What's the difference between a relative and an absolute file path?

**Back:** A relative path depends on where the program is run from; an absolute path is the full address and works from anywhere.
