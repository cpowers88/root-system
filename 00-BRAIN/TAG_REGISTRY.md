---
type: reference
timeline: reference
tags: [governance]
created: 2026-07-21
---

# TAG_REGISTRY.md — Canonical Topic Tags

One machine-checkable list of approved cross-cutting topic tags for `.ROOT`.
`WHERE_IT_GOES.md § Metadata Standard` defines the rule (tags are the
categorical axis, 0-3 normal, 5 max, 3+ files or it's noise); this file is
the actual registry that rule points to, so the list lives in one place.

## Approved Tags

governance, north-star, watchtower, school, business, programming,
ai-automation, technology, systems, physics, math, audit, client, pricing,
strategy, research, security, workflow, meta-learning, economics,
technical-writing, open-textbook, dataset, provisional, castle,
system-evolution, learning

This list is a starting point, not a ceiling — derived from tags already
grouping 3+ live files as of the 2026-07-21 audit. Add a tag here only when
it clears that bar (or has a clearly scheduled third use); remove one that
drops below it after the 30-day singleton review.

## Deprecated / Converted Families (2026-07-21)

These legacy tag families are retired from `tags:` — the information now
lives in a real frontmatter property. Do not reintroduce them in new or
edited frontmatter.

| Legacy tag pattern | Replaced by | Status |
|---|---|---|
| `priority/now`, `priority/next`, `priority/later` | `timeline: now` / `next` / `later` | Converted, 201 instances |
| `status/wiki-only` | `status: wiki-only` | Converted, 201 instances |
| `stage-NN` (PYTHON/PHYSICS numbered stage) | `stage: NN` property (kept where already present; tag dropped as duplicate) | Converted, 65 instances |
| `phase-N`, `phase-all` (BUSINESS roadmap phase) | `stage: phase-N` (per `03-WIKIS\BUSINESS\CLAUDE.md`'s own documented convention — **not** a new `phase:` property; `stage` and `phase` are different concepts that happen to share a legacy tag shape, and BUSINESS's own doc already resolves this by keeping one property, `stage`, with a `phase-N` string value) | Converted, 54 instances |

Converting `stage-NN`/`phase-N` tags exposed that a number of PYTHON,
PHYSICS-adjacent, and BUSINESS files never actually had a real `timeline:`
property — they were only passing metadata validation because those legacy
tags were accepted as temporary timeline stand-ins. Where the file was
clearly durable library/reference content (code patterns, concepts,
glossary, drills, errors, mini-projects, tool-capability pages, BUSINESS
pathway/template pages), `timeline: reference` was assigned as the honest,
consistent value. This was a real gap the audit had been masking, not new
debt introduced by the conversion.

## Governance Question — Resolved 2026-07-21 (later same night)

Chris decided: convert to properties, for long-run consistency with the
rest of this migration and with how properties scale (queryable directly,
don't inflate the tag vocabulary as new values are added). Executed via
`convert_domain_stack_tags.py` (archived 2026-08-16 to
`99-ARCHIVE\ARCHIVED_2026-08-16_completed-tag-migrations\`) — 174 files across
TECHNOLOGY and SYSTEMS: `domain/*` dropped (174 instances — inferable from
the `03-WIKIS/<hub>` path; a few files separately keep a legitimate
top-level `domain:` scalar property where one already existed, untouched),
`source-role/*` → `source_role:` property (173 instances; one file
genuinely carried two values, e.g. `primary` and `example` — represented
as a list rather than picked arbitrarily), `use-case/*` → `use_cases:` list
property (381 instances across files, many multi-valued), `stack/*` →
`stack:` list property (47 instances). `TECHNOLOGY\CLAUDE.md` and
`SYSTEMS\CLAUDE.md` both updated in the same pass so neither hub's own doc
still endorses the retired tag families. `root_health.py` confirmed 0 new
debt from this conversion (identical 413 total / 5 new / 212 resolved
before and after — the 5 new are the pre-existing, unrelated PHYSICS
findings noted above).

Note: TECHNOLOGY/SYSTEMS's new `source_role:` property is a controlled
enum (`primary`/`example`/`reference`/`support`), while PYTHON's
pre-existing `source_role:` property (on `source-summaries/` pages) is a
free-text curriculum-spine descriptor — same property name, different
per-hub vocabulary, which `WHERE_IT_GOES.md`'s Metadata Standard already
permits (same pattern as `stage`/`status` having realm-specific
vocabularies). Not a collision; just don't expect one shared enum across
both usages.

## Fixed This Pass, Unrelated to Tags

- `00-BRAIN\scripts\build_graph_colors.py` had no real `--check` flag (an
  invocation with `--check` silently ignored the flag and wrote anyway) —
  added a genuine read-only check mode.
- `00-BRAIN\scripts\metadata_migration_plan.py`'s `--output` flag has never
  worked (`REPORT_DIR` was referenced but never defined) — fixed.
- `00-BRAIN\scripts\frontmatter_audit.py`'s `EXCLUDED` set didn't cover
  `02-LIBRARY\.raw ARCHIVE\` (a documented immutable folder per
  `WHERE_IT_GOES.md`) — four files there were briefly eligible for the
  mechanical timeline conversion before this was caught and fixed; nothing
  in that folder was actually touched.
- `.obsidian\graph.json`'s search-exclusion filter had drifted to empty
  (contradicting `COLOR_MAP.yaml` and `START_HERE.md`) — restored, and two
  new infrastructure folders (`.folder-icons`, `tmp`) added to
  `excluded_from_graph`. `outputs\` was left flagged, not excluded — it
  holds real generated content and deserves its own color group, a call for
  Chris, not a silent exclusion.

## Tooling

- `00-BRAIN\scripts\metadata_migration_plan.py` — read-only planner for the
  single-plain-timeline-tag conversion (deterministic, self-testing).
- `00-BRAIN\scripts\apply_safe_metadata_conversions.py` — applies exactly
  that planner's `safe_complete_conversions`, refusing to run if the live
  tree no longer matches the plan's hash.
- `convert_legacy_tag_families.py` — the four-family conversion above
  (`--check` / `--apply`), skips anything ambiguous rather than guessing.
  **Archived 2026-08-16** — see below.
- `convert_domain_stack_tags.py` — the TECHNOLOGY/SYSTEMS
  `domain/source-role/use-case/stack` conversion (`--check` / `--apply`).
  **Archived 2026-08-16** — see below.

> **Both converters were retired on 2026-08-16 to
> `99-ARCHIVE\ARCHIVED_2026-08-16_completed-tag-migrations\`.** Each was run one
> last time first and reported **0 files would be changed**, so no live file still
> carries the shapes they convert. They are kept as the record of how the
> migration was performed and **will not run from the archive** — both import
> `frontmatter_audit` from their old sibling directory. If a legacy family ever
> reappears, write a fresh converter rather than resurrecting these.

## Not Done Tonight

- `subject/*` singleton review/promotion/link-replacement (255 distinct
  values, 176 used on only one file — needs per-tag judgment: promote a
  genuinely recurring theme, replace a one-note label with a wikilink/index
  entry, or remove it; not a mechanical pass).
- Extending `frontmatter_audit.py` to flag unregistered tags, aliases, and
  the `<3-file`/`>5-tags-per-note` thresholds against this registry.
