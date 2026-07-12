---
type: code-pattern
stage: 09
status: draft
concepts: ["module", "file-path"]
tags: [stage-09, files, automation, os-module]
---

# Code Pattern: Organize Files by Extension

## Purpose

Sort a folder's files into subfolders based on their file extension (or any other rule derived from the filename).

## Use This When

You have a messy folder (downloads, exports) and want to group files automatically instead of dragging them by hand.

## Do Not Use This When

The folder only ever has one or two files, or the organization scheme changes too often to encode as a simple rule — manual organization may be simpler.

## Skeleton

```python
import os
import shutil

for filename in os.listdir(source_folder):
    full_path = os.path.join(source_folder, filename)
    if os.path.isfile(full_path) and filename.endswith(extension):
        shutil.move(full_path, destination_folder)
```

## Filled Example

```python
import os
import shutil

source = "downloads"
for filename in os.listdir(source):
    full_path = os.path.join(source, filename)
    if os.path.isfile(full_path) and filename.endswith(".txt"):
        shutil.move(full_path, "downloads/text_files")
```

## Step-by-Step Trace

1. `os.listdir(source)` returns every filename and folder name directly inside `source`.
2. `os.path.join(source, filename)` builds a correct full path for each item.
3. `os.path.isfile(full_path)` confirms it's an actual file, not a subfolder.
4. `filename.endswith(".txt")` checks the extension matches the rule.
5. `shutil.move(...)` physically relocates matching files to the destination folder.

## Beginner Mistakes

- Forgetting the destination folder must already exist (`shutil.move` won't create it) — use `os.makedirs(destination, exist_ok=True)` first if it might not exist.
- Not checking `os.path.isfile()`, so the script tries (and fails) to move subfolders as if they were files.
- Running the real version against real data before testing on a throwaway copy.

## Related Terms

- [[glossary/module]]
- [[glossary/file-path]]

## Drill Link

- [[drills/stage-09-automation-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-09-automation-bridge]].
