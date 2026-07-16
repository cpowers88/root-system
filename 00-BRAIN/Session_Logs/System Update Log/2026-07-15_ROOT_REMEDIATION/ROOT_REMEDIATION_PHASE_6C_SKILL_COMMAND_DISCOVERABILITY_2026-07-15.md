---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit, skills, commands]
created: 2026-07-15
---

# Phase 6C — Skill and Command Discoverability

## Outcome

Chris has one early, plain-language quick reference for all shared `.ROOT` skills and
safe diagnostic commands, while write-capable maintenance commands are visibly
separated. The placement authority accurately inventories every live system script.

## Evidence

- Approved Phase 6B checkpoint: `e5dcaf8`.
- Five canonical skills exist (`atlas-brief`, `graph-colors`, `profit-gate`,
  `root-health`, `session-close`) and both discovery mirrors match exactly.
- Each skill has concise trigger-focused frontmatter and a bounded procedure; no
  skill-content defect was found.
- `ROOT_OPERATING_MANUAL.md` documents only the root-health command and has no human
  list of the five skills.
- `00-BRAIN\WHERE_IT_GOES.md` inventories 5 of 7 live scripts, omitting
  `root_health.py` and `metadata_migration_plan.py`.
- Some maintenance commands write generated files or mirrors. A flat command list
  would create an ease-of-use false pass unless read-only checks and write-capable
  maintenance are distinguished.

## Owned paths

1. `ROOT_OPERATING_MANUAL.md`
2. `00-BRAIN\WHERE_IT_GOES.md`
3. This report.

## Exclusions

- No canonical skill, generated skill mirror, script, profile, boot file, graph
  configuration, metadata baseline, migration output, or command behavior changes.
- Do not execute graph generation, skill synchronization in write mode, metadata
  report writing, or baseline refresh.
- No PHYSICS, raw, Journal, archive, source-routing, or concurrent-file edit.
- Do not create a skill README or duplicate the procedural bodies of skills inside
  the human manual.

## Acceptance tests

1. The manual lists all 5 shared skills exactly once with a natural-language trigger
   and concise outcome; it points to the canonical skill home and generated mirrors.
2. The manual separates read-only diagnostic commands from commands that write
   generated artifacts or mirrors and names the approval/precondition for each.
3. The placement authority lists all 7 live scripts exactly once in its script
   inventory.
4. Every listed skill/script path exists. Canonical skill validation and mirror
   synchronization pass; no skill or mirror diff exists.
5. Canonical health, boot/governance, wiki navigation, live Markdown integrity, and
   both staged/unstaged whitespace checks pass with no new metadata debt.
6. Only the two named live documents plus this report enter the checkpoint; Claude's
   two PHYSICS files remain outside.

## Rollback boundary

The Phase 6C diff begins at `e5dcaf8`. Its exact three-file checkpoint can be
reverted without disturbing Phase 6A/6B or Claude's unstaged PHYSICS work.

## Human decision

At the checkpoint Chris may approve, request one bounded revision, hold, or reject.
No Phase 6C commit and no Phase 6D source-routing work begins before that decision.

## Loop plan

- Pass 0 freezes skill/script inventory, mirror hashes, live command references, and
  the concurrent-file boundary.
- Pass 1 adds one human quick reference and corrects the authoritative script list.
- Loop 1 targets command-safety clarity: verify every command's real side effects and
  keep read-only checks visibly separate from write-capable maintenance.
- Loop 2 runs only if Loop 1 exposes another failure class or Chris requests it.
- The correction loop checks counts, exact path existence, skill mirrors, complete
  diff, health, whitespace, and the exact three-file boundary.

## Pass record

### Pass 0 — baseline and frozen boundary

- Starting checkpoint: `e5dcaf8`; concurrent files: PHYSICS current-position and
  log only, both excluded.
- Canonical skills: 5; discovery mirrors: 2; mirror validation PASS with matching
  hashes for every skill.
- Each skill contains exactly one matching `name`, one trigger-focused
  `description`, no extra frontmatter field, and 12–26 total lines. No skill body or
  trigger change was justified.
- Human quick-reference coverage: 0/5 skills. Focused safe-command coverage: one
  documented root-health command. Write-capable maintenance forms were not grouped
  or side-effect classified.
- Placement-authority script inventory: 5/7; `root_health.py` and
  `metadata_migration_plan.py` were absent from the list despite existing on disk.

### Pass 1 — smallest coherent repair

- Added one early manual section mapping natural requests to all five shared skills
  without copying their procedural bodies.
- Added six read-only diagnostic forms covering health, boot, wiki review, metadata
  baseline comparison, skill-mirror equality, and metadata-plan self-test.
- Added three write-capable maintenance forms and named exactly what each writes and
  the condition for using it.
- Updated the placement authority's script inventory to all seven live scripts in a
  stable alphabetical list.
- No skill, mirror, script, generated artifact, or baseline changed.

### Loop 1 — command-safety clarity

- **Quality dimension:** command clarity and false-safe prevention.
- **Baseline:** 1/9 useful command forms had an explicit safe/read-only context in
  the human manual; three write-capable forms were not visibly separated.
- **Target:** improve safety clarity by 3–10% without adding a new command layer or
  copying skill procedures.
- **Bounded change:** replaced the write-capable prose with a scan-friendly table
  naming action, exact command, written artifact, and use condition.
- **Measured result:** side-effect-classified command coverage moved 1/9 -> 9/9;
  all six read-only and all three write-capable forms are separated. This exceeds
  the target because incomplete classification would knowingly leave a command with
  ambiguous side effects.
- **Stop decision:** keep. Every command path exists, all read-only forms ran without
  writes, and no write-capable form was executed.

### Loop 2 decision

Loop 1 exposed no new failure class. Per the run protocol, Loop 2 is not run without
a new class or a human request.

### Correction loop

- Verified quick-reference skill coverage 5/5, read-only command coverage 6/6,
  write-capable coverage 3/3, and placement script inventory 7/7 with one occurrence
  of each filename inside the inventory.
- Confirmed all 12 canonical skill/script paths exist. Shared-skill mirror validation
  passes: 5 canonical skills and 2 mirrors.
- The skill-creator package's optional `quick_validate.py` helper could not start in
  either available Python runtime because its `yaml` dependency is absent. No claim
  relies on that helper: an equivalent read-only structural check confirmed matching
  folder/name fields, one description, no extra frontmatter fields, and sub-500-line
  bodies for all five unchanged skills.
- All six documented read-only commands pass. Metadata-plan self-test covers 615/615
  findings with zero target writes; the frontmatter baseline reports 615 unchanged,
  0 new, and 5 resolved.
- Complete diff review shows only the manual quick reference, authoritative script
  inventory, and this report. Claude's PHYSICS files remain excluded and unstaged.

## Final validation

- Boot/governance: PASS (30 boot files, 1,090 live pages).
- Wiki navigation: PASS (0 blockers, 0 review debt, 773 expected classifications).
- Shared skills: PASS (5 canonical, 2 mirrors, matching hashes).
- Metadata remains reviewed baseline debt: 615 findings, 0 new, 5 resolved.
- Canonical health: **PASS WITH DEBT**; boot/governance, wiki navigation, shared
  skills, staged whitespace, and unstaged whitespace pass.
- Live Markdown integrity: 1,167 files checked, 0 findings.

## Human checkpoint

Phase 6C is complete and intentionally uncommitted. Approval authorizes only the
manual quick reference, the placement authority's complete script inventory, and
this report as an exact three-file checkpoint. It does not authorize a skill,
mirror, script, graph, migration, baseline, PHYSICS, or Phase 6D source-routing edit.
