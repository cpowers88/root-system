---
type: reference
tags: [physics, school]
timeline: reference
---

# Physics Anki Import and Rotation

## Current deck (2026-07-16)

Import **`Physics_All_Stages.apkg`** into Anki: **File → Import**, select the
file. It is a ready-made package, not a TSV — no note-type or separator setup
needed.

This creates one parent deck, `Physics`, with one subdeck per stage:

```
Physics::Stage 01 - Physics and Measurement
Physics::Stage 02 - Motion in One Dimension
Physics::Stage 03 - Vectors
...
Physics::Stage 18 - Special Relativity
```

223 cards total, generated directly from the wiki's own
`03-WIKIS\PHYSICS\wiki\flashcards\stage-N-*.md` source files (the same
Q/A pairs used inside the vault) — not re-authored separately, so the two
stay in sync. Stage 3's two dot/cross-product preview cards (Chapter 7
material previewed early) carry a `preview` tag if you want to filter them out
of the Stage 3 subdeck.

**Study only the subdeck for the stage you're actively working or reviewing.**
The whole point of the per-stage split is so you never have to face all 223
cards at once — open `Physics::Stage 04 - ...` (or whichever stage is active
per `current-position.md`) and leave the rest closed.

**If you re-import after regenerating the package:** Anki matches notes by an
internal ID derived from the deck name + card number, so re-importing updates
existing cards in place rather than duplicating them, as long as the deck
names haven't changed.

## Superseded

- `Physics_Stages_01-03_Active.tsv` (July 14 build) — a hand-picked 35-card
  active/preview subset for Stages 1–3 only. Superseded by the full
  stage-separated package above; left in place as source reference, not
  deleted.
- `00_Physics_Foundations.tsv`, `01_Measurements.tsv`, `02-Kinematics.tsv`,
  `03_Vectors.tsv`, `Equations.tsv`, `05_Mistake_Cards.tsv` — pre-July-14
  mixed decks. Source reference only; do not reimport into the daily rotation.
- If an old mixed Physics deck still exists in Anki from before July 14,
  rename it to `Physics::Archive::Pre-2026-07-14` rather than deleting it.

## Status Rules (still apply per-card)

- **New:** cannot yet give a correct meaning.
- **Learning:** partly correct, needs prompting, or confuses model/units/direction.
- **Locked:** can define it, identify the physical situation, state relevant units,
  and use it in a problem without prompting. Suspend in Anki.
- **Reopen:** a locked term caused a mistake; return it to review.

Track status changes in `ADAPTIVE_REVIEW_LOG.md`; suspend locked cards in
Anki rather than deleting them.
