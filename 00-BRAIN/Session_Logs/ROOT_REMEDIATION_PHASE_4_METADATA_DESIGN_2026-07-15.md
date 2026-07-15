---
type: plan
timeline: now
tags: [governance, audit]
status: approved
created: 2026-07-15
---

# Phase 4 — Design and Pilot the Metadata Model

## Outcome

`.ROOT` has one approved two-axis metadata contract, a transition-safe audit, and a
small non-school pilot proving that current action, static stage, artifact status,
and reference priority can be queried without treating them as the same timeline.
A deterministic dry run maps existing debt before Phase 5 performs any realm-wide
migration.

## Evidence

- Checkpoint baseline: `64b2c52` (`Phase 3: reconcile live semantic interfaces`).
- `WHERE_IT_GOES.md` treats `now/next/later`, `priority/now`, `stage-NN`, and
  `phase-N` as native equivalents on one sequential axis, although they mean
  current action, reference usefulness, curriculum position, and roadmap position.
- `START_HERE.md` says `tag:#now` represents `priority/now`, current stages, and
  `phase-1`, but one Obsidian tag query cannot truthfully combine those meanings.
- The July 15 integrity audit found at least 110 inherited knowledge pages tagged
  `priority/now`, swamping an actionable “what matters now” view.
- Current audit baseline: 1,136 live files; 0 missing frontmatter, 100 missing
  `type`, 520 timeline findings, 620 total; 0 new / 0 resolved against the reviewed
  Phase 2 baseline.
- The current audit recognizes timeline-like tags but ignores explicit `timeline:`,
  `stage:`, `status:`, and `reference_priority:` properties.
- Broad discovery finds 115 files mentioning `priority/now`, 190 mentioning a
  numbered stage tag, and 165 matching a `now` tag pattern; prose/log references
  make those discovery counts directional rather than migration totals.

## Owned paths

- `00-BRAIN\WHERE_IT_GOES.md`
- `START_HERE.md`
- active instruction surfaces found by loop review: `00-BRAIN\vault_map.md`,
  `00-BRAIN\CASTLE\HOW_TO_USE.md`, and
  `00-BRAIN\HATS\HAT_EDUCATOR_PLAYBOOKS.md`
- `00-BRAIN\scripts\frontmatter_audit.py`
- one read-only metadata dry-run script and its Phase 4 report under
  `00-BRAIN\scripts\` / `00-BRAIN\Session_Logs\`
- frontmatter only in this non-school pilot set:
  - `NOW.md`
  - `00-BRAIN\SYSTEM_FLAGS.md`
  - `00-BRAIN\CASTLE\wiki\current-position.md`
  - `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md`
  - `02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\KSU_Academic_Tracker_Brief.md`
  - `02-LIBRARY\.PROJECTS\listing-packet\MOVED_TO_LOCAL.md`
- template frontmatter examples only when they currently teach file creation
- this phase brief

## Exclusions

- Phase 5 owns bulk metadata migration. Phase 4 may not rewrite a whole wiki,
  library corpus, Make.com corpus, or all 620 baseline findings.
- Claude's unstaged DAILY and PHYSICS files remain preserved and excluded. No
  EDUCATION, PHYSICS, PYTHON, raw, Journal, archive, or external-client content is
  read or modified for the pilot.
- Tags remain categorical topics. This phase does not redesign graph colors,
  folders, ownership, or semantic content.
- The dry run may propose `manual_review`; it must not guess missing types, status,
  stage, or reference priority from filenames alone.

## Acceptance tests

1. The canonical contract defines separate `timeline`, optional `stage`, optional
   `status`, optional `reference_priority`, and topic-only `tags`, with clear allowed
   values and examples.
2. `timeline` answers current action only; stage/phase position, artifact condition,
   and reference usefulness cannot satisfy it by substitution.
3. The audit accepts legacy metadata during the transition, validates pilot v2
   properties, rejects dual/invalid control fields, and preserves baseline-mode,
   zero-debt strict, JSON, and equal-count identity behavior.
4. The dry run is read-only, deterministic, covers every current finding identity,
   separates safe transformations from manual decisions, and writes no target file.
5. The six-file pilot removes legacy control tags only from frontmatter, retains
   topic tags, and yields a small actionable `timeline: now` set without altering
   file meaning.
6. `START_HERE.md` gives verified Obsidian property/tag query guidance and does not
   claim `tag:#now` finds a property or static stage.
7. Root health reports no new metadata debt; boot, wiki, text-integrity, staged and
   unstaged whitespace, and Claude-owned-file boundaries do not regress.

## Rollback boundary

The Phase 4 diff begins at `64b2c52`. It contains schema/audit/dry-run design and
six frontmatter-only pilot edits. Phase 5 cannot begin before the isolated Phase 4
checkpoint and human review.

## Human decision

After Pass 1 and two measured refinement loops, Chris chooses **approve**,
**revise once more**, **hold**, or **reject**. Approval authorizes Phase 5's
realm-by-realm migration, not an all-at-once rewrite.

## Pass record

### Pass 0 — baseline

- Metadata contract: one conflated tag axis.
- Reviewed debt: 620 findings (100 type; 520 timeline); 0 new baseline debt.
- Explicit v2 property support: absent.
- Deterministic migration dry run: absent.
- Pilot set: 6 files; metadata-only changes not started.
- Working tree outside this brief: Claude's DAILY and two PHYSICS files only.

### Pass 1 — implementation

- Replaced the conflated tag axis with required `timeline`, optional `stage`,
  optional `status`, optional `reference_priority`, and topic-only `tags`.
- Verified the documented Obsidian forms `[property:value]`, `path:` plus a
  property term, and `tag:#topic` against the official Search and Properties
  documentation.
- Updated all 6 pilot files and 6 creation templates without changing body
  meaning. The pilot contains 5 `timeline: now` files and 1 `timeline: parked`
  file; legacy control tags remaining in the pilot: 0.
- Extended the audit without refreshing its baseline: 1,137 files checked;
  100 missing type, 520 timeline, 0 schema, 620 total; 0 new and 0 resolved.
- Added a deterministic dry-run plan covering 620/620 finding identities.

### Loop 1 — instruction and classification challenge

- False-pass search found 3 active instruction surfaces still teaching the old
  tag query (`vault_map`, CASTLE `HOW_TO_USE`, Educator playbook); corrected all
  3. Historical logs/reports remain historical evidence and were not rewritten.
- Tightened “safe” classification so a file with any current audit finding
  cannot be called a safe complete conversion.
- Rejected non-scalar `stage`/`status` values and expanded legacy control-tag
  recognition to hyphenated values.
- Measured result: active stale instructions 3 → 0; audit regressions remain 0.

### Loop 2 — ambiguity and write-boundary challenge

- Added duplicate-property rejection for all v2 control fields, preventing YAML
  ambiguity from passing on the first value found.
- Locked `--output` to `ROOT_METADATA_MIGRATION_DRY_RUN_*.json` directly under
  `00-BRAIN\Session_Logs`; an attempted `--output NOW.md` is rejected.
- Hashed the 6 pilot targets before and after final report generation: 0 changed.
- Final deterministic plan SHA-256:
  `bef949594f17f4a3e325646b0940aee97605f669a11dd8c3cebf93a8347b3433`.
- Final dry-run split: 284 safe complete legacy conversions; 620 explicit manual
  finding decisions; 620/620 finding identities covered; 0 target writes.

## Acceptance result

| Test | Result | Evidence |
|---|---|---|
| Separate action/stage/status/reference axes | PASS | Metadata Standard + 6-file pilot |
| Transition-safe audit | PASS | self-test; 620 baseline identities; 0 new schema debt |
| Deterministic, read-only dry run | PASS | repeat hash; 620/620 coverage; output guard; target hash check |
| Verified human query guidance | PASS | `START_HERE.md` property/path/tag examples |
| Creation templates teach v2 | PASS | 6 templates updated with copy rules |
| Active instruction surfaces agree | PASS | 3 stale surfaces found and corrected; focused search 0 remaining |
| Canonical root health | PASS WITH DEBT | 0 blockers; 4 wiki review; 620 reviewed metadata debt |
| Claude boundary | PASS | DAILY + 2 PHYSICS files remain unstaged and outside this phase |

## Review checkpoint

Chris approved Phase 4 on July 15, 2026. Approval authorizes an isolated Phase 4
commit and planning for Phase 5's realm-by-realm migration. It does not authorize
an all-at-once rewrite.

Canonical health gate: **PASS WITH DEBT**, not clean. Named debt is 4 wiki review
items and 620 reviewed metadata findings (100 missing type; 520 timeline; 0 schema;
0 new). The gate does not evaluate semantic freshness, review-cadence completion,
source ownership/duplicate-source disposition, or all ordinary direct-path prose.
