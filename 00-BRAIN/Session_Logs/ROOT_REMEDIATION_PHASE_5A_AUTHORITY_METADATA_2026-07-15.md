---
type: plan
timeline: now
status: approved
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5A — Authority-Plane Metadata Migration

## Outcome

The live governance and model-instruction plane uses metadata v2 without changing
the meaning, status, routing, or topic classification of any authority file.
This is the first realm migration; it proves the Phase 5 method before templates,
logs, CASTLE action pages, or subject knowledge are considered.

## Evidence baseline

- Approved Phase 4 checkpoint: `7dcc675`.
- Live dry run: 284 safe complete legacy conversions; 620 manual finding
  decisions; 620/620 finding identities covered.
- `00-BRAIN` contains 76 syntactically safe conversions, but that total combines
  authority files, placeholder-bearing templates, historical logs, Claude's live
  DAILY file, and CASTLE action pages. Treating all 76 as one batch would erase
  meaningful review boundaries.
- The unambiguous authority subset is 24 files. Each has exactly one legacy
  `reference` control tag, valid `type`, no audit finding, and no competing control
  tag. The mechanical change is `timeline: reference`, removal of only the
  `reference` tag, and preservation of all topic/status properties.

## Owned manifest — exactly 24 files

- Core: `AGENT.md`, `AI_OS_CORE.md`, `ATLAS.md`, `CHRIS.md`, `CHRIS_CORE.md`,
  `CLAUDE.md`, `CODEX.md`, `LOCAL_MACHINE_MAP.md`, `SYSTEM_LEARNINGS.md`,
  `vault_map.md`, `WHERE_IT_GOES.md`.
- CASTLE operator surfaces: `CASTLE\CLAUDE.md`, `CASTLE\CODEX.md`,
  `CASTLE\HOW_TO_USE.md`, `CASTLE\OPERATIONS.md`.
- Hats: `HAT_ECON.md`, `HAT_EDUCATOR.md`, `HAT_EDUCATOR_PLAYBOOKS.md`,
  `HAT_ENGR1000.md`, `HAT_OPERATOR.md`, `HAT_OPERATOR_PLAYBOOKS.md`,
  `HAT_PHYSICS.md`, `HAT_PYTHON.md`, `HAT_TCOM.md`.

All paths above are under `00-BRAIN`.

## Exclusions

- All `00-BRAIN\Session_Logs`, especially Claude's unstaged
  `DAILY_2026-07-15.md`.
- All `00-BRAIN\CASTLE\templates`; their placeholder `status` values require a
  bespoke creation-template decision, not a mechanical conversion.
- All `00-BRAIN\CASTLE\wiki` action/phase/skill pages; current action meaning must
  be reviewed separately.
- All subject wikis, PHYSICS, EDUCATION, PYTHON, Library, school, raw, Journal,
  archive, client content, and the two Claude-owned PHYSICS files.
- No type, status, stage, reference-priority, or link edits in the owned files.
  Phase 5A changes frontmatter control placement, plus one evidence-backed stale
  control-language correction if a challenge loop proves it necessary.

## Acceptance tests

1. The owned set is exactly 24 files and matches the frozen manifest.
2. Each owned file has `timeline: reference` exactly once and no legacy control
   tag; its prior topic tags, type, and status remain byte-equivalent in meaning.
3. The live dry-run safe count falls by exactly 24 (284 → 260), while all 620
   finding identities remain unchanged and schema debt remains 0.
4. Boot/governance validation, shared skills, text integrity, wiki navigation,
   staged whitespace, and unstaged whitespace do not regress.
5. Claude's DAILY and two PHYSICS edits remain the only pre-existing unstaged
   work and are neither staged nor modified by this phase.

## Loop contract

- Pass 1 performs only the frozen mechanical conversion.
- Loop 1 challenges manifest completeness, exact tag preservation, and any file
  whose semantics are not truly reference-only.
- Loop 2 challenges duplicate controls, live dry-run deltas, boot behavior, and
  the Claude boundary.
- Correctness failures are fixed regardless of percentage. Otherwise each loop
  must document a measured 3–10% improvement or explicitly record that no safe
  wording/design change survives the acceptance tests.

## Rollback and review boundary

The diff begins at `7dcc675`. Phase 5A remains uncommitted until Chris reviews
the final report. Approval authorizes only the isolated Phase 5A commit and the
design of the next bounded realm chunk.

## Pass record

### Pass 0 — baseline

- Owned v2 files: 0/24.
- Owned legacy `reference` controls: 24.
- Live safe conversions: 284.
- Reviewed findings: 620; schema findings: 0; new findings: 0.
- Working tree: Claude's DAILY and two PHYSICS files, plus this phase brief.

### Pass 1 — frozen mechanical migration

- Migrated 24/24 manifest files to `timeline: reference`.
- Removed exactly 24 legacy `reference` tags and retained every non-control topic
  tag, `type`, and pre-existing `status` value.
- Live safe conversions: 284 → 260, the exact expected delta of 24.
- Reviewed findings remained 620/620 unchanged: 100 missing type, 520 timeline,
  0 schema, 0 new, 0 resolved.
- Deterministic plan SHA-256 after the migration:
  `40c319aa8a45ef7ef6f02e0d34293440785d5840b0d1b5eb480837f58a2de4f1`.

### Loop 1 — manifest and semantic challenge

- Inspected every zero-context diff: each owned file contains only one removed
  `tags` line and its v2 `timeline` + preserved topic-tag replacement.
- Confirmed all 24 files are authority/reference surfaces; no action page,
  historical log, creation template, raw input, Journal file, or subject-wiki page
  entered the set.
- Compared each working file body with `7dcc675` after removing frontmatter:
  initial body preservation **PASS (24/24)**.
- The first focused search found only the intentional transition example in
  `WHERE_IT_GOES.md`; the additional human-requested pass below broadened that
  search and found one indirect stale instruction.
- No safe wording or design edit survived the frontmatter-only acceptance test,
  so this loop improved verification depth without increasing scope or diff size.

### Loop 2 — control, baseline, boot, and boundary challenge

- Metadata and migration self-tests pass, including duplicate/non-scalar controls,
  equal-count identity substitution, deterministic coverage, and output guarding.
- Canonical root health: **PASS WITH DEBT**; boot/governance, shared skills,
  unstaged whitespace, staged whitespace, and text integrity pass.
- Wiki navigation: 0 blockers, 4 review items, 773 expected items.
- Metadata: 1,138 files checked; 620 reviewed findings; 0 schema; 0 new.
- Claude's DAILY and two PHYSICS files remain outside the owned manifest and were
  neither modified by this phase nor selected for a checkpoint.
- No additional metadata edit improved correctness after these checks; the frozen
  24-file change is the smallest complete authority-plane migration.

### Additional correction pass — indirect control language

- Broadened the active-instruction search beyond explicit `tag:#now`, “Tag
  Standard,” and “timeline tag” phrases to include indirect “tags move” language.
- Found 1 missed active instruction in `HATS\HAT_PHYSICS.md`: “tags move, colors
  never do.” This contradicted metadata v2 because topic tags do not carry action
  or stage state.
- Corrected it to: update `stage` and `timeline` independently; topic tags and
  graph colors do not move.
- Revised the acceptance claim from 24/24 identical bodies to 23 unchanged bodies
  plus 1 explicit, evidence-backed instruction correction.

## Acceptance result

| Test | Result | Evidence |
|---|---|---|
| Frozen manifest | PASS | exactly 24 owned conversions |
| Correct v2 control | PASS | 24 `timeline: reference`; 0 owned legacy controls |
| Type/status/topic preservation | PASS | zero-context diff review |
| Body control | PASS | 23 unchanged; 1 documented stale-instruction correction |
| Expected dry-run delta | PASS | safe conversions 284 → 260 |
| Baseline identity preservation | PASS | 620 unchanged; 0 new/resolved/schema |
| Canonical health | PASS WITH DEBT | 0 blockers; 4 wiki review; 620 reviewed metadata debt |
| Claude boundary | PASS | 3 concurrent files remain outside Phase 5A |

## Review checkpoint

Chris approved Phase 5A on July 15, 2026. Approval authorizes only an isolated
25-file checkpoint (24 manifest files plus this report) and design of Phase 5B.
It does not authorize the excluded logs, CASTLE action pages, or any subject-realm
migration.

The canonical health gate does not evaluate semantic freshness, review-cadence
completion, source ownership/duplicate-source disposition, or all ordinary
direct-path prose; those claims remain with their owning reviews.
