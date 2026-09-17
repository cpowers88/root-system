---
type: tool-capability
status: active
stage: 9
python_tools: [os, pathlib, shutil]
prerequisites: [loops, strings, file-paths]
tags: [programming, capability]
timeline: reference
---

# Capability: Organize Files and Folders

## Real-World Problem

A Downloads folder with 400 unsorted files. Photos from three phones in one giant dump. Class notes scattered across the desktop. Any "I need to sort/rename/move a pile of files" chore.

## Beginner Version

A script that loops over every file in one folder and moves each file into a subfolder based on its extension (`.pdf` → `PDFs/`, `.jpg` → `Images/`).

## Python Tools Involved

- `os.listdir()` / `pathlib.Path.iterdir()` — list what's in a folder.
- `shutil.move()` — move a file.
- `os.makedirs(..., exist_ok=True)` — create destination folders.
- String methods (`.endswith()`, `.lower()`) or `Path.suffix` — read the extension.

## Prerequisites

[[stages/stage-03-loops-and-repetition]] (loop over files), [[stages/stage-05-data-shapes]] (strings), [[stages/stage-06-files-errors-debugging]] (paths). Taught properly in [[stages/stage-09-automation-bridge]] via [[concepts/organizing-files-at-scale]].

## Tiny Example

```python
import os, shutil

for name in os.listdir("test_folder"):
    if name.lower().endswith(".pdf"):
        os.makedirs("test_folder/PDFs", exist_ok=True)
        shutil.move(f"test_folder/{name}", f"test_folder/PDFs/{name}")
```

## Mini-Project Idea

Already in the vault: [[mini-projects/stage-09-file-organizer]] — sort a throwaway test folder by extension. Pattern reference: [[code-patterns/organize-files-by-extension]].

## School Relevance

Low direct (not a CSE topic) — but it exercises loops, strings, and conditionals on real data, which is exactly the fluency the course needs.

## Future Business Relevance

High — client document dumps (invoices, job photos, contracts) almost always need sorting before any audit work can start.

## Advanced Version — Parked

Watching a folder continuously (`watchdog`), scheduled runs (Task Scheduler/cron — ATBS Ch. 19), renaming by file *content* (needs PDF/Word reading, ATBS Ch. 17). See [[parking-lot]].
