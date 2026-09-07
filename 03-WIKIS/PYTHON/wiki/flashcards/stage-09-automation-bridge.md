---
type: flashcards
tags: [programming]
timeline: later
---

# Flashcard Batch: Stage 9 — Automation Bridge

## Card: Module

**Front:** What is a module?

**Back:** A single .py file of reusable code that can be brought into another program with import.

**Tags:** python, stage-09, modules

---

## Card: Standard library vs third-party

**Front:** Do standard library modules like `os` or `csv` need to be installed with pip?

**Back:** No — they come built into Python already. Only third-party packages need pip install.

**Tags:** python, stage-09, decision-rule

---

## Card: Where pip runs

**Front:** Where do you run `pip install`?

**Back:** In a terminal, not inside your Python script — it's a one-time setup step.

**Tags:** python, stage-09, pip

---

## Card: CSV values are strings

**Front:** What type are values read from a CSV file, before any conversion?

**Back:** Strings — even values that look like numbers.

**Tags:** python, stage-09, csv

---

## Card: json.load vs json.loads

**Front:** What's the difference between `json.load()` and `json.loads()`?

**Back:** `json.load()` reads from an open file. `json.loads()` parses a JSON string already in memory.

**Tags:** python, stage-09, json

---

## Card: CSV vs JSON decision rule

**Front:** When should you use CSV instead of JSON?

**Back:** When the data is simple, flat, table-shaped (rows and columns). Use JSON when data has nesting or varying structure.

**Tags:** python, stage-09, decision-rule

---

## Card: What makes something an automation script

**Front:** What makes a script an "automation script" specifically?

**Back:** It replaces a repeated manual chore, rather than just performing a one-off calculation.

**Tags:** python, stage-09, automation

---

## Card: Where scheduling lives

**Front:** Is scheduling usually handled inside the Python script itself, or by the operating system?

**Back:** Usually by the operating system (cron, Task Scheduler) — the script itself just needs to work correctly when triggered.

**Tags:** python, stage-09, scheduling

---

## Card: os.path.join decision rule

**Front:** Why use `os.path.join()` instead of building a file path with string concatenation?

**Back:** It automatically uses the correct path separator for the operating system, avoiding bugs that only show up on a different machine.

**Tags:** python, stage-09, decision-rule
