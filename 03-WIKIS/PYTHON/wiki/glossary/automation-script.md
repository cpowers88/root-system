---
type: glossary-entry
stage: 09
status: draft
aliases: []
related_terms: ["scheduling"]
timeline: reference
---

# Automation Script

## Plain-English Definition

A program written specifically to replace a repeated manual chore — sorting files, generating a report, renaming a batch of items — with something that runs automatically.

## What Problem It Helps Solve

Repetitive manual chores are slow and error-prone. A script does the same steps reliably, every time, without getting bored or making typos.

## When Chris Will See It

Anywhere Stages 1-8's tools (loops, conditionals, files, functions) are applied to a real, repeated chore rather than a teaching exercise.

## Code Example

```python
import os

# automation script: count text files in a folder, instead of doing it by hand
count = sum(1 for f in os.listdir("notes") if f.endswith(".txt"))
print(f"{count} text files found.")
```

## Common Confusion

Not every program is "an automation script" — the label specifically means it replaces a *repeated* manual task. A one-off calculation isn't really automating anything.

## Physical-World Anchor

A recurring chore chart that actually gets followed every time, versus relying on memory to redo the same steps manually each week.

## Related Terms

- [[glossary/scheduling]]

## Flashcard Q/A

**Front:** What makes a script an "automation script" specifically?

**Back:** It replaces a repeated manual chore, rather than just performing a one-off calculation.
