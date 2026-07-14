---
type: tracker
tags: [now, programming, flashcards]
---

# Python Flashcard Calibration — July 14–20, 2026

## Purpose

Keep only terms that still need recall in Anki's active rotation. The TSV files
remain the complete source bank; a known term is **suspended in Anki**, never
deleted, so it can return if real code exposes a gap.

## Card Status Rules

| Status | Meaning | Anki action |
|---|---|---|
| New | Not yet explained or used correctly | Add / keep active |
| Learning | Can partly explain it but needs prompting | Keep active |
| Locked | Can define it, recognize it in code, and use it correctly without prompting | Suspend |
| Reopen | A supposedly locked term caused an error or weak explain-back | Unsuspend / return to active |

## Current Rotation

| Role | Deck | Terms | Review use |
|---|---|---|---|
| Active | `Python_Stages_01-03_Active.tsv` | Selected Stage 1–3 vocabulary: 29 cards, no known `print()` card or duplicate `=`/`==` card | Learn and review now |
| Preview | `Python_05_Functions.tsv` | Stage 4 functions vocabulary | Add tomorrow or at the next flashcard session; do not start Stage 4 code yet |
| Locked baseline | `print()` | User can accurately explain that it displays what is inside its parentheses to the user | Suspend in Anki; keep in the source TSV |

**Anki reset:** rename the old mixed deck to `Python::Archive::Pre-2026-07-14`.
Import the active 29-card deck as `Python::Active::Stages 1-3`; the source TSV
files remain the reference bank.

## Seven-Day Calibration Log

At flashcard time, Chris gives each card or term a quick status: **new**,
**learning**, **locked**, or **reopen**. Evidence must be an explanation, a
correct code use, or an error that revealed the gap.

| Date | Kept active / added | Suspended as locked | Reopened | Evidence / confusion noticed | Next preview terms |
|---|---|---|---|---|---|
| Jul 14 | 29-card Stage 1–3 active deck | `print()` | — | User accurately explained `print()`; Stage 2 story used branching and `or` | Stage 4: function, parameter |
| Jul 15 | | | | | |
| Jul 16 | | | | | |
| Jul 17 | | | | | |
| Jul 18 | | | | | |
| Jul 19 | | | | | |
| Jul 20 | | | | | |

## Advance Procedure

At the next flashcard session, add Stage 4 Functions as preview. Thereafter,
before the final flashcard review of a completed stage, import the following
stage's deck as preview. Do not add code drills from the preview stage until its
prerequisites are complete.
