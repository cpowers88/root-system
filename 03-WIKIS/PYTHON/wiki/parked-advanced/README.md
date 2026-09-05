---
type: guide
timeline: reference
tags: [programming]
---

# parked-advanced

Holding area for advanced material **pages** whose prerequisites aren't met yet.

## How parking actually works in this vault

- **[[parking-lot]] is the tracker.** Every parked topic is a row there (source, why parked, prerequisite needed, when to revisit). Park a *topic* by adding a row — no page needed.
- **This folder holds actual pages** only when parked content is already written out as a page that would pollute the active folders (concepts/, code-patterns/, drills/) — e.g., a future advanced concept page drafted ahead of its stage.
- **It is currently empty by design.** Nothing has been drafted ahead of the path. The FORGE-inherited pandas/NumPy/SQL material is *source inventory*, not drafted curriculum, so it lives in `wiki/source-summaries/` with `status: parked` — not here.

## When a page lands here it must record

- source,
- topic,
- why parked,
- prerequisite needed,
- when to revisit.

(Same fields as a [[parking-lot]] row — the page and the row should point at each other.)
