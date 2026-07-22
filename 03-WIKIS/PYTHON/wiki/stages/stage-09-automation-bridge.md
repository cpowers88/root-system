---
type: stage
stage_number: 09
status: ready
priority: later
source_spine: "Automate the Boring Stuff Ch.11, 14-15, 17-20, Appendix A"
support_sources: ["Python Workout Ch.9", "raw/docs/library/csv.txt and datetime.txt"]
---

# Stage 09 — Automation Bridge

## Purpose

Turn Python into a tool that does real chores: organizing files and folders, reading/writing CSV and JSON, and recognizing what's worth automating.

## Why This Stage Comes Now

Stages 1-8 built every fundamental skill in isolated teaching exercises. Stage 9 is where Chris starts applying them to genuinely useful, repeated tasks — the first stage where "is this code actually doing something I care about?" becomes the test, not just "does it demonstrate the concept?"

## Prerequisites

Stage 8 (or Stage 6 minimum for the file-handling parts, if Chris wants to preview automation early).

## Concepts To Learn

- [[concepts/modules-and-packages]]
- [[concepts/organizing-files-at-scale]]
- [[concepts/csv-and-json]]
- [[concepts/automation-script-design]]

## Vocabulary To Add

- [[glossary/module]]
- [[glossary/package]]
- [[glossary/pip]]
- [[glossary/csv]]
- [[glossary/json]]
- [[glossary/automation-script]]
- [[glossary/scheduling]]

Full flashcard batch: [[flashcards/stage-09-automation-bridge]]

## Required Code Patterns

- [[code-patterns/organize-files-by-extension]]
- [[code-patterns/read-csv-and-process]]

## Drills

- [[drills/stage-09-automation-practice]]

## Mini-Project

- [[mini-projects/stage-09-file-organizer]]
- Alternative/extra: a CSV report generator (read a CSV of sample data, compute summary stats, write a results file) if Chris wants more reps with structured data instead of files/folders.

## Common Errors Reference

- [[errors/stage-09-common-errors]]

## Read Next

1. Automate the Boring Stuff Appendix A — "Installing Third-Party Packages" (short, do this first since later chapters assume it).
2. Automate the Boring Stuff Ch.11 — "Organizing Files."
3. Automate the Boring Stuff Ch.18 — "CSV, JSON, and XML Files." Read the XML section only lightly; CSV and JSON are the priority.
4. Automate the Boring Stuff Ch.19 — "Keeping Time, Scheduling Tasks, and Launching Programs" — read for the scheduling *concept* only; skip deep implementation of `sched`/Task Scheduler/cron for now.
5. Automate the Boring Stuff Ch.14 (Excel) and Ch.17 (PDF/Word) — optional extra reading if Chris wants to extend the mini-project's stretch goals; not required for core mastery.
6. Python Workout Ch.9 — "Modules and Packages," plus the CSV/JSON exercises in Ch.6 for extra drill material.

## Mastery Checklist

- [ ] Define module, package, pip, CSV, JSON, automation script, and scheduling in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a script that lists/organizes files in a folder by extension, from memory.
- [ ] Write a script that reads a CSV file, processes its rows, and computes a result.
- [ ] Write a script that saves and reloads data as JSON.
- [ ] Explain what makes a chore a good candidate for automation versus not worth it.
- [ ] Debug at least one of the four error types in [[errors/stage-09-common-errors]] without help.
- [ ] Complete [[drills/stage-09-automation-practice]].
- [ ] Complete [[mini-projects/stage-09-file-organizer]] and explain the solution out loud.

## Stage Mastery Target

Can write a script that reads structured data from a file, processes it, and writes a result, without copying a recipe verbatim.

## Parked Until Later

- Excel and Google Sheets automation (ATBS Ch.14-15) — available as stretch material, full depth held for whenever Chris has a real spreadsheet task.
- PDF/Word document automation (ATBS Ch.17) — same, available but not core to this stage.
- Email/text/push-notification sending (ATBS Ch.20) — requires external account setup; parked per `wiki/parking-lot.md`.
- Real scheduling implementation (cron, Windows Task Scheduler) — conceptual mention only this stage.
- Business tooling (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE) — explicitly out of scope for this Python hub; revisit only when Chris explicitly asks to bridge.
