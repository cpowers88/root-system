---
type: system-update
timeline: now
status: active
tags: [architecture, castle, cleanup, path-integrity]
created: 2026-07-24
---

# `.ROOT` Architecture Update — Unified Findings and Cleanup

**Date:** July 24, 2026  
**Scope:** CASTLE elevation proposal, folder/file synopsis, read-only path audit prototype, and update-artifact cleanup.

## Current conclusion

`.ROOT` is a working unit. The existing logical structure is strong enough to
continue from, but physical CASTLE elevation remains unproved. The next
structural decision must be evidence-gated by a read-only impact audit; no
directory move is currently authorized.

## Evidence consolidated

- The eight-source architecture intake is complete: 3,789/3,789 physical
  pages. It supports logical functional roles without requiring one physical
  topology, separate Watchtower sensing, versioned instruction interfaces,
  stable move identifiers, checkpoints, dependency-aware validation, and
  fresh-session acceptance.
- The skeleton and synopsis now agree: CASTLE elevation is a hypothesis,
  Watchtower stays separately observable and non-acting, and `77-INBOX` is the
  single universal intake door.
- CASTLE does have bounded write authority. It may maintain its own maps,
  decisions, logs, proof status, indexes, `NOW.md`, and approved return
  packets. It may not silently rewrite North Star, governance, owner truth,
  immutable `raw/`, private journal material, or another realm's content.

## Read-only audit test

Prototype: `00-BRAIN\scripts\path_reference_audit.py`  
Schema: `00-BRAIN\scripts\path_reference_audit.schema.json`

The prototype compiled, parsed its report schema, and scanned 1,669 Markdown
files in approximately six seconds. It returned 1,285 findings:

| Finding | Count |
|---|---:|
| Ambiguous wikilink | 254 |
| Unresolved wikilink | 316 |
| Unresolved Markdown link | 623 |
| Broken/unverified anchor | 92 |

The non-zero exit is expected. This is an inventory, not a clean-pass claim.
Templates, legacy references, duplicate basenames, dependency material, and
real defects are not yet separated. The prototype writes nothing to `.ROOT`.

## Cleanup performed

Archived reversibly under `99-ARCHIVE\`:

- `ARCHIVED_2026-07-24_2.md`
- `ARCHIVED_2026-07-24_mybadcodexplan.md`
- `ARCHIVED_2026-07-24_newvaultstructure.md`
- `ARCHIVED_2026-07-24_Untitled.md`
- `ARCHIVED_2026-07-24_update_data_review_wiki_instructions.md`
- `ARCHIVED_2026-07-24_INGEST_PROTOCOL_2026-07-24_VAULT_REDESIGN_SOURCES.md`

Kept live:

- `vault-skeleton-design.md`
- `newvaultstructureclaude.md`
- CASTLE contracts, templates, wiki maps/reports/logs, and the audit
  prototype/schema.
- Corrected CASTLE `OPERATIONS.md` so its intake rule matches the resolved
  single-door `77-INBOX` state.

No raw evidence, private material, live directory, or unrelated worktree
change was modified. The two live design files remain at their current paths
until the impact audit establishes a safe canonical relocation, if one is
needed.

## Next exact action

Classify the 1,285 audit findings into three dispositions:

1. intentional/template or generated reference;
2. historical reference to baseline/archive;
3. live integrity defect requiring correction.

Then create the baseline allowlist and extend the prototype into the four
separate checks: path moves, resolvable references/anchors, canonical-copy
violations, and instruction-register conformance. Only after that should a
CASTLE relocation impact report be produced.

**Check-at:** after finding classification and baseline review, before any
directory move or governance edit.

## Classification update

The first conservative pass classified 221 findings as intentional template,
historical narrative, or intentional external reference and left 1,064
unclassified candidates open. Rules are recorded in
`00-BRAIN\scripts\path_reference_baseline.json`; the detailed report is
`2026-07-24_PATH_REFERENCE_CLASSIFICATION_REPORT.md` in this session-log
folder. The rules are now integrated into the auditor through `--baseline`.
The final post-integration run scanned 1,673 Markdown files, baselined 221
findings, and left 944 unbaselined after hub-scoped resolution. The next step is inspecting the
unbaselined CASTLE/wiki subset.

The subset run corrected a validator false-positive by scoping wikilink
resolution to each owning hub's `wiki/` root. The corrected scan reports 1,165
total findings, 221 baselined, and 944 unbaselined; the live CASTLE/domain-wiki
subset contains 266 unbaselined findings. PHYSICS is the first repair queue
(149), followed by TECHNOLOGY (69), SYSTEMS/PYTHON (42), and six isolated
CASTLE/BUSINESS/REVENUE_LAB findings. No link was changed.

Decision: carry the PHYSICS cluster as deferred structural work. Do not
bulk-repair or baseline it until the later-stage packet/page architecture is
reviewed; the eventual fix may be a new PHYSICS structure rather than link
patches.

## Implementation closeout

The dated implementation packet now contains the reconciled roadmap, runbook,
session index, and isolated validator fixture test. The current audit result is
1,673 Markdown files scanned, 1,165 findings, 221 baselined, and 944
unbaselined. The next action is a separately scoped CASTLE impact report and
Watchtower handoff test; no physical relocation is authorized by this packet.
