---
type: mini-project
stage: 06
status: draft
concepts: ["file-path", "open-read-write-close", "exception", "try-except", "function"]
solution_included: false
timeline: reference
---

# Mini-Project: Simple Note-Saver

## User Story

As a learner, I want to build a small program that lets me save a note to a file and read past notes back, handling the case where the notes file doesn't exist yet, so that I can prove I understand file reading/writing and exception handling together.

## Required Concepts

- [[glossary/file-path]]
- [[glossary/open-read-write-close]]
- [[glossary/exception]]
- [[glossary/try-except]]
- [[glossary/function]]

## Build Phases

### Phase 1 — Save a Note

Write a function `save_note(text)` that appends `text` (plus a newline) to a file called `notes.txt`, using `"a"` (append) mode so it doesn't erase previous notes.

### Phase 2 — Read Notes Safely

Write a function `read_notes()` that opens `notes.txt` in read mode and prints its full contents — but uses `try`/`except` to catch `FileNotFoundError` and print a friendly "No notes yet!" message instead of crashing if the file doesn't exist.

### Phase 3 — Tie It Together

Write a small driver loop (you can use a plain sequence of calls, or — if comfortable from Stage 3 — a `while` loop with a menu) that lets the user choose to save a new note or view all notes.

## Acceptance Checklist

- [ ] `save_note()` uses append mode, so calling it multiple times adds notes rather than erasing previous ones.
- [ ] `read_notes()` correctly handles the case where `notes.txt` doesn't exist yet, without crashing.
- [ ] Running the program twice in a row (closing and reopening it) shows that notes persist between runs.
- [ ] Uses a context manager (`with open(...) as f:`) for every file operation.
- [ ] Chris can explain, out loud, what would happen if `save_note()` used `"w"` mode instead of `"a"`.

## Stretch Goals — Parked

- Timestamp each note (needs the `datetime` module — fine to mention, not required at Stage 6).
- Let the user delete a specific note (needs more string/list processing of the file's lines — doable now, but optional).

## Reflection Questions

1. Why does `read_notes()` need a `try`/`except` instead of just checking if the file exists some other way? (Either approach is valid — which did you pick, and why?)
2. What's the difference in behavior between opening `notes.txt` in `"w"` vs `"a"` mode across multiple runs of your program?
3. If `save_note()` crashed partway through writing, would the file definitely be closed properly? Why does using `with` matter here?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
