---
type: guide
timeline: reference
tags: [library]
created: 2026-07-15
---

# 02-LIBRARY — Reference, Projects, and School Files

This is the **input and storage layer**: raw reference material, official course
files, and active build docs. Nothing here is refined knowledge — refinement
happens in `03-WIKIS`; money-system assets live in root `05-BUSINESS`. If a file
teaches, sells, or decides, it doesn't belong here.

## The Three Look-Alikes, Disambiguated

- **`02-LIBRARY\REF-BUSINESS`** — raw business *reference* (clippings, PDFs).
- **`03-WIKIS\BUSINESS`** — refined business *knowledge* (offers, methods, research).
- **Root `05-BUSINESS`** — reusable business *assets* (templates, capability library).

Same triangle for every domain: LIBRARY holds sources, the wiki refines them,
the output realm packages them.

## What Lives Where

| Folder | Holds |
|---|---|
| `04-SCHOOL\` | Official course files per course (syllabi, notes, OneNote, D2L pulls) — the only LIBRARY folder with its own placement rules in `WHERE_IT_GOES.md` |
| `.PROJECTS\` | Active build docs and small scripts; real code lives on GitHub/local repos |
| `.raw ARCHIVE\` | Closed legacy source holding; no new intake and no content changes without Chris's explicit raw exception |
| `ref-math\` | Math textbooks (Strang, OpenStax calculus/precalc/stats) |
| `ref-programming\` | Programming reference not owned by the PYTHON wiki (syntax notes, Automate the Boring Stuff) |
| `ref-business\` | Raw business reference clippings |
| `ref-field-operations\` | Construction/field artifacts (pro-forma workbook) |
| `ref-AI-automation\` | The TECHNOLOGY wiki's spine (`TECHNOLOGY_LIBRARY_STRATEGY.md` — load-bearing, do not move), prompt libraries, make.com notes. Artifact home, **not** an intake lane — new AI research routes to `03-WIKIS\AI_AUTOMATION_SYSTEMS` |
| `ref-meta-how-to-work\` | Three YouScience source reports about Chris; the AI-ready profile lives in `00-BRAIN\CHRIS_CORE.md` + `CHRIS.md`, so PDFs are provenance rather than routine load targets |
| `ref-health\` | Health/fitness reference |
| `ref-misc\` | Everything else (stock-market books — parked, outside the North Star) |
| `coding_toolkit\` | Undocumented as of 2026-07-29 — currently just an empty `python_code\` subfolder; confirm purpose or archive it at the next weekly review |

## Rules of This Realm

1. `ref-` domains are **reference piles by design** — no index/log ceremony is
   owed here; that discipline belongs to the wikis.
2. A source a wiki starts refining moves (or is pointer-copied) into that wiki's
   `raw\` per `WHERE_IT_GOES.md`'s raw-intake rule.
3. New domain folders are created only when real material exists to fill them —
   never speculatively. (The empty 2025-era scaffolds were archived July 15,
   2026: `99-ARCHIVE\ARCHIVED_2026-07-15_EMPTY_LIBRARY_SCAFFOLDS\`.)
4. Naming history: the numbered domains (`01-PHYSICS` … `99-MISC`) became
   `REF-<NAME>` on July 15, 2026, then lowercase `ref-<name>` between July 13-27
   under the later lowercase-everything-else naming rule, so no LIBRARY folder
   shadows a wiki hub or the root money system. Historical logs keep the old
   paths. `ref-AI-automation` keeps mixed-case `AI`; align it to `ref-ai-automation`
   only when the folder is next touched for another reason (cheap-rename rule).
5. `.raw ARCHIVE\` is retained only for legacy source provenance. New source
   intake routes to the owning wiki's immutable `raw\` folder.
