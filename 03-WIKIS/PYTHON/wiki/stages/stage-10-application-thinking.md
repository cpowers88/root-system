---
type: stage
timeline: reference
stage_number: 10
status: ready
source_spine: "Automate the Boring Stuff Ch.12-13, 16; Python Crash Course Ch.11 + Part II"
support_sources: ["Invent Your Own Computer Games Ch.17-21", "raw/docs/howto/argparse.txt"]
---

# Stage 10 — Application Thinking

## Purpose

Take the final step from "scripts" to "applications": CLI design, automated testing, a first taste of databases, and an introductory look at APIs/web requests.

## Why This Stage Comes Now

This is the last stage of the original 11-stage path. Everything before this taught a specific tool or skill; this stage is about combining them into something that resembles a real, shareable piece of software — runnable from a command line, tested automatically, and (optionally) backed by a database.

## Prerequisites

Stage 9 — modules/packages, files/folders at scale, CSV/JSON.

## Concepts To Learn

- [[concepts/cli-programs-and-argparse]]
- [[concepts/automated-testing-with-pytest]]
- [[concepts/databases-and-sqlite]]
- [[concepts/apis-and-web-requests]]

## Vocabulary To Add

- [[glossary/cli]]
- [[glossary/argument-parsing]]
- [[glossary/unit-test]]
- [[glossary/database]]
- [[glossary/api]]
- [[glossary/web-request]]

Full flashcard batch: [[flashcards/stage-10-application-thinking]]

## Required Code Patterns

- [[code-patterns/cli-with-argparse]]
- [[code-patterns/pytest-test-function]]

## Drills

- [[drills/stage-10-application-practice]]

## Mini-Project

- [[mini-projects/stage-10-capstone-choice]] — Chris picks one of three tracks: CLI tool, small Pygame game, or a tested module.

## Common Errors Reference

- [[errors/stage-10-common-errors]]

## Read Next

1. Automate the Boring Stuff Ch.12 — "Designing and Deploying Command Line Programs."
2. `raw/docs/howto/argparse.txt` — the official argparse tutorial, as a reference alongside Ch.12.
3. Python Crash Course Ch.11 — "Testing Your Code" (full chapter — installing pytest, testing a function, testing a class).
4. Automate the Boring Stuff Ch.16 — "SQLite Databases." Read for the basic connect/execute/commit/query pattern; deeper SQL (joins, complex schemas) is beyond this stage.
5. Automate the Boring Stuff Ch.13 — "Web Scraping" — skim only for the API/web-request concept; the full scraping implementation (BeautifulSoup, etc.) stays parked.
6. If Track B (Pygame) is chosen: Python Crash Course Ch.12-14, or Invent Your Own Computer Games Ch.17-21, as the project-source for that track specifically.

## Mastery Checklist

- [ ] Define CLI, argument parsing, unit test, database, API, and web request in plain English.
- [ ] Recognize each of these in a short piece of code.
- [ ] Write a CLI script using `argparse` with at least one required and one optional argument, from memory.
- [ ] Write a `pytest` test function with multiple assertions, including at least one edge case.
- [ ] Explain why tightly coupling logic to input/output makes code harder to test, and how to fix it.
- [ ] Debug at least one of the four error types in [[errors/stage-10-common-errors]] without help.
- [ ] Complete [[drills/stage-10-application-practice]].
- [ ] Complete [[mini-projects/stage-10-capstone-choice]] (any track) and explain the solution out loud.

## Stage Mastery Target

Can build and explain a small end-to-end program (input -> processing -> output) with at least one automated test.

## Parked Until Later

- Flask/FastAPI (web app frameworks), SQLAlchemy (database ORMs), Docker, CI/CD, cloud deployment — all explicitly out of scope for this vault's current depth; see `wiki/parking-lot.md`.
- NumPy/pandas — parked until a real data-analysis need arises.
- Full web scraping implementation (BeautifulSoup), OCR, keyboard/mouse automation, text-to-speech — niche/optional, only if Chris asks.
- Business applications (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY` — formerly FORGE) — explicitly a different hub; bridge only if Chris asks directly.
- This is the end of the originally-planned 11-stage path. Future sessions should check with Chris on what comes next: deeper practice within Stages 1-10, a business-applications bridge (`03-WIKIS\BUSINESS` / `03-WIKIS\TECHNOLOGY`), or genuinely new advanced material.
