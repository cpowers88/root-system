---
type: reference
tags: [reference, programming]
---

# Python Anki Phase 1–2 Decks

These files are tab-separated `.tsv` files for Anki import.

## Import settings

- Note type: Basic
- Separator: Tab
- First row: Field names / header
- Fields:
  - Front
  - Back

## Recommended Anki deck names

- Python::Active::Stages 1-3 — import `Python_Stages_01-03_Active.tsv` first;
  this is the current working deck as of July 14.
- Python::00 Intent to Syntax
- Python::01 Core Terms
- Python::02 Strings
- Python::03 Conditionals
- Python::04 Loops
- Python::05 Functions
- Python::06 CS50P Patterns
- Python::07 Debugging Errors Exceptions
- Python::08 Libraries Modules Imports
- Python::09 Unit Tests Pytest
- Python::10 File IO
- Python::11 Mistake Cards

## Daily drill

10 minutes: review old cards  
10 minutes: add or edit cards from the current problem  
10 minutes: write tiny code reps using the tools from the cards

Do not only memorize. Use the words in small working code.

## Adaptive Rotation — Start July 14, 2026

These TSV files are the source bank; Anki is the active queue. Do not delete a
known card from its TSV source. In Anki, **suspend** it when Chris can define it,
recognize it in code, and use it correctly without prompting. Reintroduce a
suspended card if a real code rep or explain-back exposes a gap.

- **Active deck:** the current study stage's vocabulary. Review it daily.
- **Preview deck:** the next stage's vocabulary. Introduce a few terms before
  that stage begins, so the words are familiar when the code arrives.
- **Advance rule:** when a stage closes, make its preview deck active and import
  the following stage as preview during that same flashcard session. Example:
  when Stage 3 closes, make `Python_04_Loops.tsv` active and import
  `Python_05_Functions.tsv` as preview.
- **Calibration:** record keep/suspend/reintroduce decisions in
  `ADAPTIVE_REVIEW_LOG.md` for the first seven days, then tune weekly.

## Anki Reset — July 14

Do not power through the old mixed Python deck. In Anki, rename it to
`Python::Archive::Pre-2026-07-14` so its history remains recoverable. Then import
`Python_Stages_01-03_Active.tsv` into `Python::Active::Stages 1-3`. This 29-card
deck intentionally excludes `print()` (already locked) and one duplicate
`=`/`==` card. Add Stage 4 Functions as a preview deck tomorrow or at the next
flashcard session; do not add unrelated older stacks to the active rotation.
