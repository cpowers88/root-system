---
type: drill
stage: 09
status: draft
concepts: ["module", "package", "pip", "csv", "json", "automation-script"]
difficulty: beginner
solution_included: false
timeline: reference
---

# Drill: Modules, CSV, and JSON Practice

## Objective

Practice using standard library modules for files/folders, reading and processing a CSV file, and reading/writing JSON.

## Concepts Practiced

- `import` and the standard library
- `os`/`shutil` for working with files and folders
- `csv` module for tabular data
- `json` module for structured data

## Starter Prompt

**Part A — Folder listing:**

Create a small test folder with 4-5 files of mixed extensions (`.txt`, `.csv`, a couple of others). Write a script that lists every file in that folder and prints a count of how many have each extension.

**Part B — CSV processing:**

Create a small CSV file with at least 5 rows of data (e.g., `name,score` — a few students and their test scores). Write a script that reads it and prints the average score.

**Part C — JSON round-trip:**

Write a script that builds a Python dictionary with at least 3 keys (one of which is a list), saves it to a `.json` file, then reads that file back and prints it to confirm it matches what was saved.

## Requirements

- Part A must use `os.listdir()` and check extensions with `.endswith()`.
- Part B must convert the score column to a number before averaging — and skip the header row correctly.
- Part C must use both `json.dump()` and `json.load()`.

## Constraints

- No third-party packages required — this drill only needs the standard library (`os`, `csv`, `json`).
- Test on a throwaway folder/file, not anything important.

## Expected Behavior

Part A should correctly count files by extension. Part B should print a correct average matching what you'd compute by hand. Part C should print back the exact same data that was saved.

## Self-Check Questions

1. In Part A, what would happen if the test folder also contained a subfolder — would your script handle it correctly?
2. In Part B, what error would you get if you forgot to skip the header row, and why?
3. In Part C, what would `print(loaded_data)` show if you forgot to call `json.load()` and just printed the raw file object instead?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
