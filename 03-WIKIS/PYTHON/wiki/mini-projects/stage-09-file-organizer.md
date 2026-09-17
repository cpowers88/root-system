---
type: mini-project
stage: 09
status: draft
concepts: ["module", "file-path", "automation-script", "decomposition", "incremental-development"]
solution_included: false
timeline: reference
---

# Mini-Project: File Organizer

## User Story

As a learner, I want to build a script that sorts a messy folder's files into subfolders by file type, so that I can prove I understand the `os`/`shutil` modules and have built a genuinely useful automation script — not just a teaching exercise.

## Required Concepts

- [[glossary/module]]
- [[glossary/file-path]]
- [[glossary/automation-script]]
- [[glossary/decomposition]]
- [[glossary/incremental-development]]

## Build Phases

### Phase 0 — Plan First (Stage 7 process applies here too)

Before writing code: decompose the chore into steps (list the folder, identify each file's type, decide the destination, move it) and write down at least one test case using sample files.

### Phase 1 — List and Categorize

Set up a test folder with a mix of file types (`.txt`, `.csv`, `.jpg`, etc. — empty placeholder files are fine for testing). Write a script that lists every file and prints which category it would go into (by extension), without actually moving anything yet.

### Phase 2 — Create Destination Folders

Extend the script to create a subfolder for each category (if it doesn't already exist) using `os.makedirs(path, exist_ok=True)`.

### Phase 3 — Actually Move the Files

Add the `shutil.move()` call to actually relocate each file into its category folder. Test against the throwaway test folder, not anything real, until you're confident it works correctly.

## Acceptance Checklist

- [ ] The plan from Phase 0 was written before any code, per Stage 7's process.
- [ ] The script correctly identifies each file's category by extension.
- [ ] Destination folders are created automatically if they don't exist.
- [ ] Files are moved correctly, and subfolders already present in the source folder are not mistakenly treated as files.
- [ ] The script was tested on throwaway sample files first, not real/important data.
- [ ] Chris can explain, out loud, what would happen if `shutil.move()` were called before confirming the destination folder exists.

## Stretch Goals — Parked

- Extend to also handle Excel files (ATBS Ch.14) or PDFs (ATBS Ch.17) as additional categories — fine to explore, not required for this mini-project.
- Add basic scheduling so it runs automatically on a timer (Windows Task Scheduler or cron) — conceptual only at this stage, per [[glossary/scheduling]].

## Reflection Questions

1. What specifically made this feel like "automating a real chore" rather than just a coding exercise?
2. What was the riskiest part of this script to get wrong, and how did testing on sample files protect against that?
3. If you ran this script twice in a row on the same folder, would anything break the second time? Why or why not?

## Answer Policy

No full solution unless Chris confirms this is not graded school work.
