---
type: glossary-entry
stage: 06
status: draft
aliases: ["open()", "context manager"]
related_terms: ["file-path"]
---

# `open()` / Read / Write / Close

## Plain-English Definition

`open()` gets access to a file in a chosen mode (`"r"` read, `"w"` write, `"a"` append). Reading pulls data out; writing puts data in (overwriting by default); closing releases the file. `with open(...) as f:` (a context manager) closes the file automatically.

## What Problem It Helps Solve

Lets a program load saved data back in, or save new data permanently to disk.

## When Chris Will See It

Any time a file needs to be opened, read from, or written to.

## Code Example

```python
with open("notes.txt", "w") as f:
    f.write("Hello, file!")

with open("notes.txt", "r") as f:
    print(f.read())
```

## Common Confusion

Opening a file in `"w"` mode **erases** its existing contents immediately, even before you write anything new — this is a common way to accidentally lose data.

## Physical-World Anchor

Opening a notebook (`open()`), reading a page (read), writing a new page (write — but starting a *new* notebook in `"w"` mode means the old pages are gone), and closing the cover (close).

## Related Terms

- [[glossary/file-path]]

## Flashcard Q/A

**Front:** What happens to a file's existing contents when you open it in `"w"` mode?

**Back:** They're erased immediately, even before you write anything new.
