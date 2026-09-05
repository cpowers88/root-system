---
type: report
timeline: log
tags: [governance, castle]
created: 2026-07-21
status: complete
---

# Tag Taxonomy Migration — Report for Morning Review
### Session: Claude Code, night of 2026-07-21. For Chris's review before the day's sessions start.

## One-Line Summary

Codex audited the vault's tag taxonomy, I reviewed it as independent challenger and executed it after you approved, caught and fixed one real mistake of my own along the way, and closed every part of the plan that had a clear evidence-backed answer — with zero new metadata debt introduced. One piece (`subject/*` review) is deliberately left open for a dedicated session.

## Why This Happened

Codex ran a full vault-wide audit: 798 unique tags across 805 tagged files, 76.7% of tags below a 3-file grouping threshold, SYSTEMS + TECHNOLOGY carrying 55% of all tag assignments from inherited FORGE-era structured tag families (`priority/*`, `status/*`, `domain/*`, `source-role/*`, `use-case/*`, `stack/*`). Diagnosis: the vault had two incompatible tag systems coexisting, and tags were functioning as a per-note index rather than a navigation layer.

I reviewed the audit as the independent second AI (per `AGENT.md`'s "One AI Team" model), agreed with the diagnosis and the four-layer target architecture (folder/path = where, `timeline:` = when, structured properties = what kind/condition, tags = genuine cross-cutting topics only, links/search = granular concepts). My one pushback was timing — I recommended deferring execution past the July 25/26 Bootcamp evidence gate, since nothing was broken, just messy. You heard that and explicitly chose to execute now, citing available session budget. Proceeded on that basis.

## What Changed

**Four legacy tag families converted to real frontmatter properties** (mechanical, using a planner script that refuses to guess on anything ambiguous):

| Legacy tag | Replaced by | Files |
|---|---|---|
| `priority/now`, `priority/next`, `priority/later` | `timeline: now`/`next`/`later` | 201 |
| `status/wiki-only` | `status: wiki-only` | 201 |
| `stage-NN` (PYTHON/PHYSICS) | dropped as duplicate where `stage:` already agreed | 65 |
| `phase-N`, `phase-all` (BUSINESS) | `stage: phase-N` (BUSINESS's own documented convention) | 54 |

**Second wave, after you resolved the one open governance question** (keep `domain/*`/`source-role/*`/`use-case/*`/`stack/*` as tags, per TECHNOLOGY's old doc, or convert to properties, per the broader audit — you chose properties for long-run system consistency):

| Legacy tag | Replaced by | Files/instances |
|---|---|---|
| `domain/*` | dropped entirely (inferable from `03-WIKIS/<hub>` path) | 174 files |
| `source-role/*` | `source_role:` property | 173 instances |
| `use-case/*` | `use_cases:` list property | 381 instances |
| `stack/*` | `stack:` list property | 47 instances |

**Also fixed:** one `Python`/`python` tag case collision; 19 standalone body-tag lines stripped (tags belong only in frontmatter — none carried information not already in each file's real tags).

**New canonical file:** `00-BRAIN\TAG_REGISTRY.md` — the one list of approved topic tags, the conversion history, and what's still open. `WHERE_IT_GOES.md` now points to it instead of duplicating the list.

**Doc updates:** `03-WIKIS\TECHNOLOGY\CLAUDE.md` and `03-WIKIS\SYSTEMS\CLAUDE.md` both previously endorsed the now-retired tag families in their own text — both corrected so neither contradicts the live state anymore.

## One Real Mistake, Caught Before It Stuck

My first pass at `phase-N` invented a new `phase:` property. Wrong — `03-WIKIS\BUSINESS\CLAUDE.md` already documents the correct target as `stage: phase-N` (one property, shared with PYTHON/PHYSICS's stage concept only in name, not merged in meaning). Caught by actually reading that hub's own doc before declaring the family "done," and corrected across all 54 affected files before moving on.

## Three Real Script Bugs Found and Fixed (Not Tag-Related)

1. `build_graph_colors.py` had **no actual `--check` flag** — invoking it with `--check` silently ignored the argument and wrote anyway. Added a genuine read-only mode.
2. `metadata_migration_plan.py`'s `--output` flag **has never worked** — `REPORT_DIR` was referenced but never defined anywhere in the script. Fixed.
3. `frontmatter_audit.py`'s exclusion list didn't know about `02-LIBRARY\.raw ARCHIVE\`, a folder `WHERE_IT_GOES.md` explicitly marks immutable. Caught before any file there was touched (would have been a real raw-boundary violation); fixed the exclusion list instead.

Also restored `.obsidian\graph.json`'s drifted-empty search-exclusion filter to match `COLOR_MAP.yaml`, and added two missing infrastructure folders (`.folder-icons`, `tmp`) to the exclusion list. `outputs\` was deliberately left un-excluded and flagged instead — it holds real generated content and deserves its own graph color, not silent hiding.

## Validation

- `root_health.py`: total findings 520 → 413 (212 resolved). Only 5 "new" findings the entire night, and those are confirmed **pre-existing PHYSICS pages from Codex's own earlier session**, unrelated to any of this work, left untouched.
- `wiki_lint.py --strict`: PASS, 0 blockers, 0 review debt.
- `validate_boot_chain.py`: PASS, 31 boot files, 1248+ pages.
- Whitespace and Markdown text integrity: PASS throughout.

## Explicitly Left Open (Not a Silent Decision)

- **`subject/*` tag review** — 255 distinct values, 176 used on only one file. This needs per-tag human judgment (promote a genuinely recurring theme to a real tag, replace a one-note label with a wikilink/index entry, or just remove it) — not something a script should guess at. Recommend its own session, not squeezed into system-maintenance time.
- **Extending `frontmatter_audit.py`** to check live tags against `TAG_REGISTRY.md` directly (flag unregistered tags, aliases, `>5-tags-per-note`, case collisions automatically) — infrastructure work, not urgent, would make future drift self-catching.

## Bottom Line for This Morning

The vault's metadata is materially cleaner than it was last night, with real evidence trails (not just claims) at every step, and nothing new is broken. The one thing worth deciding today, if anything: whether `subject/*` review happens this week or waits — it's not blocking anything.
