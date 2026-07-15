---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5E — CASTLE Special Roles

## Outcome

CASTLE's index, append-only log, and live current-position page express their
different roles through metadata v2. The index remains a core reference map, the
log becomes historical rather than a reference/action page, and current-position
remains the live baseline without an unnecessary rewrite.

## Evidence baseline

- Approved Phase 5D checkpoint: `873e15a`.
- Live dry run: 236 safe complete conversions; 620 reviewed findings; 100 missing
  type; 520 timeline; 0 schema; 0 new baseline debt.
- `wiki\index.md` and `wiki\log.md` each have one reviewed `missing_type` finding
  and one legacy `reference` control tag.
- Neither file is a safe mechanical conversion because its missing type requires a
  role decision. `wiki\current-position.md` is already valid v2 metadata.
- Vault-wide wiki convention uses `type: map` for primary indexes and `type: log`
  for append-only logs.

## Frozen role manifest

- `00-BRAIN\CASTLE\wiki\index.md` → `type: map`, `timeline: reference`,
  `reference_priority: core`, `tags: []`.
- `00-BRAIN\CASTLE\wiki\log.md` → `type: log`, `timeline: log`, `tags: []`.
- `00-BRAIN\CASTLE\wiki\current-position.md` → verify and preserve `type: map`,
  `timeline: now`, `status: active`, `tags: [baseline]`; no edit expected.

## Role rules

- The index organizes durable navigation, so it is a core reference map; its
  utility does not make it current work.
- The append-only log is historical evidence, so `timeline: log` is the complete
  control. It receives no `reference_priority` because it is not part of the
  reference navigation layer.
- Current-position represents live state and already uses `timeline: now`; a
  metadata pass may not rewrite correct live truth merely for symmetry.

## Exclusions

- No action-page, roadmap, map-body, index-body, current-position-body, NOW,
  subject-wiki, Library, school, raw, Journal, archive, client, or external edit.
- No baseline refresh and no attempt to migrate the remaining 618 findings.
- The only allowed body change is the required append-only CASTLE log entry for
  this phase.
- Claude's DAILY and two PHYSICS files remain outside the phase boundary.

## Acceptance tests

1. Index, log, and current-position match the frozen role manifest exactly.
2. CASTLE wiki contains zero legacy control tags after migration.
3. Core reference retrieval grows 5 → 6 by adding the index; supporting remains 3;
   current remains 8; historical log retrieval returns the CASTLE log.
4. Index and current-position bodies are byte-preserved; the log body changes only
   through the append-only Phase 5E entry.
5. Reviewed findings fall exactly 620 → 618 by resolving the two named
   `missing_type` identities; missing type falls 100 → 98; timeline remains 520;
   safe conversions remain 236; schema and new findings remain 0.
6. Metadata self-tests, canonical health, both whitespace scopes, live Markdown
   integrity, and Claude's three-file boundary pass.

## Loop contract

- Pass 1 applies the two frozen frontmatter migrations and verifies the already-v2
  current-position page.
- Loop 1 challenges type, timeline, and reference-priority semantics plus all four
  retrieval counts.
- Loop 2 checks body preservation, exact debt identities/delta, health, and the
  concurrent-file boundary.
- Correct correctness failures regardless of percentage; otherwise avoid expanding
  this small closure phase.

## Rollback and review boundary

The diff begins at `873e15a`. Phase 5E remains uncommitted until Chris reviews the
final report. Approval will authorize only the index, log, and this report as a
three-file checkpoint plus design of the next bounded Phase 5 realm.

## Pass record

### Pass 0 — baseline

- Special-role v2 state: index 0/1; log 0/1; current-position already valid.
- CASTLE wiki legacy control tags: 2, both `reference` on index/log.
- Retrieval: core reference 5; supporting reference 3; current 8; historical log 0.
- Findings: 620 total; 100 missing type; 520 timeline; 0 schema; 0 new/resolved.
- Safe complete conversions: 236.
- Working tree: Claude's DAILY and two PHYSICS files, plus this report only.

### Pass 1 — special-role migration

- Migrated index to `type: map`, `timeline: reference`, and
  `reference_priority: core`; removed its legacy `reference` tag.
- Migrated log to `type: log` and `timeline: log`; removed its legacy
  `reference` tag and assigned no misleading reference priority.
- Verified current-position already matches the frozen live-role manifest and left
  it untouched.
- Appended the required Phase 5E result to the CASTLE log; index and
  current-position bodies remain unchanged.

### Loop 1 — role and retrieval challenge

- CASTLE wiki legacy control tags: 2 → 0.
- Retrieval counts match the role model exactly: core reference 6, supporting
  reference 3, current 8, historical log 1.
- The index joins normal durable navigation without entering the action queue; the
  log leaves reference retrieval and appears only as history.
- Current-position remains the eighth current page, proving the special-role pass
  did not alter Phase 5D's action frontier.
- Dry-run result: 618 current findings, 618/618 identities covered, 236 safe
  conversions, 0 target writes.

### Loop 2 — preservation, debt identity, health, and boundary

- Frontmatter audit resolved exactly
  `missing_type|00-BRAIN\CASTLE\wiki\index.md|` and
  `missing_type|00-BRAIN\CASTLE\wiki\log.md|`; new findings remain 0.
- Final debt split: 98 missing type, 520 timeline, 0 schema, 618 total; no baseline
  refresh occurred.
- Index body is unchanged, current-position has no diff, and log body changes only
  by the required append-only Phase 5E entry.
- Metadata self-test passed with deterministic plan hash
  `b3357e2930ef34c534769a79b27de585b8726292b0d26cba9152516751d15593`,
  618/618 identities covered, and zero target writes.
- Canonical health: **PASS WITH DEBT** — 0 blockers, 4 wiki-review items, 618
  reviewed metadata findings, 0 new and 2 resolved; boot/governance, shared skills,
  both whitespace scopes, and live Markdown text integrity pass.
- Claude's DAILY and two PHYSICS files remain unstaged, unedited by Phase 5E, and
  outside its three-file boundary.

### Final correction loop — complete coverage and claim precision

- Full inventory proves all 20 CASTLE wiki pages now have one valid `type` and one
  valid `timeline`; missing type and missing timeline inside CASTLE are both 0.
- Because every CASTLE page uses v2 metadata and the vault-wide schema count is 0,
  no inline or multiline legacy control remains hidden in CASTLE frontmatter.
- Rechecked live retrieval language and counts: core 6, supporting 3, current 8,
  and historical log 1. No active interface retains the former core count.
- Found no role, query, debt-identity, body-preservation, or boundary correction.
  Tightened the final caveat below so metadata-role verification cannot be mistaken
  for a full semantic-freshness certification of current-position content.
- The correction loop adds no target file and preserves the exact three-file
  checkpoint.

## Human checkpoint

Phase 5E is complete and intentionally uncommitted. Approval authorizes exactly
`wiki\index.md`, `wiki\log.md`, and this report, followed by design of the next
bounded Phase 5 realm. This phase verified current-position's metadata role and
preserved its body; it did not certify the semantic freshness of that body. The
health gate also does not evaluate review-cadence completion, source
ownership/duplicate disposition, or ordinary direct-path prose.
