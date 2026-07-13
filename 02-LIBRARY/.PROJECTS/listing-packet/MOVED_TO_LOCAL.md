---
type: project
tags: [parked, project]
---

# Project-listing-packet — Moved to Local Disk
### Moved: July 4, 2026

---

The active code for this project (git repo, source, tests, docs, samples,
templates, data, and outputs) has moved to:

```
D:\DEV\active\Project-listing-packet\
```

GitHub remote: `github.com/cpowers88/listing-packet-clean1` (branch
`native-acroform-filler` as of the move).

## Why it moved

The project's `.git` repo and Python virtual environments (`.venv`,
`.venv311`) were living directly in this Drive folder. That violates
`WHERE_IT_GOES.md`'s own rule (`.py`/`.js`/`.sql` — local PC + GitHub
only, never Drive) and put a git working tree and ~thousands of venv
package files on a Drive-streaming mount — slow to sync, and it was not
listed as a current project in `vault_map.md` or `NORTH_STAR.md`.

`.venv` and `.venv311` (plus `__pycache__`, `.pytest_cache`) were deleted
outright rather than moved — they're fully reinstallable from
`requirements.txt` and carried no unique content.

## What's still here

One file Drive would not let move cleanly — a native Google Doc pointer,
not a real local file:

```
outputs/mvp_test_finalcheck/Powers_FinalPaper.gdoc
```

Left in place since `.gdoc` files only resolve through Drive anyway.

## Note on uncommitted changes

At the time of the move, the working tree had 3 uncommitted deletions
(`docs/keyedinformapping.pdf`, `fixtures/markedfields.pdf`,
`templates/ResidentialDataInput_MASTER_ORIGINAL.pdf`). These carried over
to the local copy unchanged — nothing was committed or discarded during
the move.
