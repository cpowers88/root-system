---
type: map
timeline: reference
tags: [programming]
---

# Prerequisite Map

## Purpose

This page defines what must be understood before moving to a concept.

Claude must check this page before adding advanced material to the active path.

---

## Core Python Dependency Chain

```text
run a file
  → print output
  → values
  → variables
  → expressions
  → strings / numbers
  → input
  → type conversion
  → comparisons
  → Boolean logic
  → if / elif / else
  → loops
  → functions
  → parameters / arguments
  → return values
  → standard-library import/use
  → lists / tuples
  → dictionaries
  → files
  → errors / tracebacks
  → program design
  → small automation
```

---

## Tool-Selection Dependencies

| If Chris needs to... | He must understand... |
|---|---|
| Store one thing | variable |
| Store text | string |
| Store a number | int / float |
| Ask the user something | input + variable |
| Choose between paths | comparison + Boolean + `if` |
| Repeat an action | loop |
| Repeat over known items | `for` loop |
| Repeat until something changes | `while` loop |
| Reuse code | function |
| Send information into a function | parameter / argument |
| Get information back from a function | return value |
| Reuse a capability that ships with Python | standard-library module + `import` |
| Store many ordered things | list |
| Store labeled things | dictionary |
| Save/load outside the program | files |
| Diagnose failure | traceback + debugging process |

---

## Advanced Unlocks

| Topic | Required Before Unlock | Vault Stage |
|---|---|---|
| pandas | lists, dictionaries, files, functions | Stage 10+ optional data-analysis strand |
| NumPy | lists, numbers, loops, functions | Stage 10+ optional data-analysis strand |
| APIs | dictionaries, JSON, functions, errors | Stage 10+ (intro only) |
| Flask/FastAPI | functions, dictionaries, files, HTTP basics | parked beyond Stage 10 |
| SQL / SQLite | data shapes, tables, filtering, joins intro | Stage 10 |
| OOP (classes, objects) | functions, dictionaries, program design | Stage 8 |
| recursion | functions, conditionals | Stage 8 |
| Big O / algorithms (sorting, searching, hash tables) | loops, functions, data shapes | Stage 8 |
| regex | strings, functions | Stage 8 (lighter-weight) |
| testing (`pytest`) | functions, return values, errors | Stage 10 |
| automation workflows (files, CSV/JSON, scheduling) | files, loops, conditionals, functions | Stage 9 |
| CLI design (`argparse`) | functions, automation basics | Stage 10 |
| web scraping | dictionaries, functions, internet basics | Stage 10 |
| Business applications (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE) | automation bridge + data handling | after Stage 9 |

**Finalized 2026-06-24** against the full source roster in `wiki/learning-path.md` and `wiki/source-map.md`.
