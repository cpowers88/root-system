---
type: code-pattern
stage: 06
status: draft
concepts: ["file-path", "open-read-write-close"]
tags: [stage-06, files, context-manager]
---

# Code Pattern: Reading/Writing a File With a Context Manager

## Purpose

Open a file, work with its contents, and have it close automatically — even if something goes wrong partway through.

## Use This When

Any time you need to read from or write to a file.

## Do Not Use This When

There's no real reason to avoid this pattern — it's the recommended default way to work with files in Python. The only thing to choose carefully is the mode (`"r"`, `"w"`, `"a"`).

## Skeleton

```python
with open("filename.txt", "r") as f:
    contents = f.read()
# file is automatically closed here, even if an error happened above
```

## Filled Example

```python
with open("notes.txt", "w") as f:
    f.write("Stage 6 notes\n")
    f.write("Files, errors, debugging\n")

with open("notes.txt", "r") as f:
    print(f.read())
```

## Step-by-Step Trace

1. `open("notes.txt", "w")` creates (or overwrites) the file and opens it for writing.
2. Each `f.write(...)` adds text to the file.
3. Once the `with` block ends, the file is automatically closed — no need to call `.close()` manually.
4. The second `with` block reopens the same file in `"r"` mode and reads its full contents back.

## Beginner Mistakes

- Opening in `"w"` mode when you meant to add to an existing file (use `"a"` for append) — `"w"` always starts fresh, erasing what was there.
- Forgetting that `f.read()` consumes the file's contents — calling it twice in a row without reopening the file returns an empty string the second time.
- Using a relative path that doesn't match where the program is actually run from.

## Related Terms

- [[glossary/file-path]]
- [[glossary/open-read-write-close]]

## Drill Link

- [[drills/stage-06-debugging-practice]]

## Flashcards To Create

- Already covered in [[flashcards/stage-06-files-errors-debugging]].
