---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5G — Root Entry Metadata

## Outcome

Every Markdown page at the vault root uses metadata v2, so the live daily cockpit
and the durable human/agent entry surfaces separate cleanly. The first-stop map now
also connects directly to the second-stop operating manual.

## Evidence baseline

- Approved Phase 5F checkpoint: `551b951`.
- The root contains exactly six Markdown pages: `NOW.md` already has
  `timeline: now`; the other five each have one valid type and one unambiguous
  legacy `reference` control tag.
- Live dry run: 225 safe complete conversions; 618 reviewed findings; 98 missing
  type; 520 timeline; 0 schema; 0 new baseline debt; 2 previously resolved.
- No audit finding is owned by this phase. All five migrations are listed by the
  deterministic safe-conversion planner.

## Final role manifest after improvement loops

### Current cockpit — preserve unchanged

- `NOW.md` — `type: dashboard`, `timeline: now`, `status: active`.

### Core human entry — migrate to `timeline: reference`, `reference_priority: core`

- `START_HERE.md` — whole-system map and first human stop.
- `ROOT_OPERATING_MANUAL.md` — human operating guide and second stop.

### Automatic model entry — migrate to `timeline: reference`

- `AGENTS.md` — root Codex auto-load pointer.
- `CODEX.md` — root Codex profile pointer.
- `CLAUDE.md` — root Claude auto-load pointer.

## Role rules

- `now` means an active operating cockpit whose content answers what to do now.
- `reference` means a durable map, guide, or boot pointer used to enter or
  understand the system; importance and auto-loading do not make it an action.
- `type` continues to describe each artifact's form independently from timeline.

## Exclusions

- The only allowed body change is one `START_HERE.md` map row linking the operating
  manual plus its visible revision-date update. No other body text, headings,
  commands, paths, permission rules, types, statuses, or topic tags change.
- No `reference_priority` on the three automatic model pointers: they are boot
  shims, not human reference destinations. No supporting/lookup rank is invented.
- No baseline refresh, manual finding resolution, nested realm, raw, Journal,
  archive, client, or external edit.
- Claude's DAILY and two PHYSICS files remain outside the phase boundary.

## Acceptance tests

1. All 6 root Markdown pages have one valid type and one valid timeline; root
   legacy control tags fall 5 -> 0.
2. Root retrieval is exactly 1 now and 5 reference, with no next/later/parked/log
   classification invented; core-reference retrieval returns exactly the two
   human entry documents.
3. Four owned pointer/manual diffs are frontmatter-only. `START_HERE.md` changes
   only its metadata, revision caption, and one operating-manual map row; all types
   and topic tags are preserved.
4. Safe conversions fall exactly 225 -> 220; reviewed findings remain 618/618
   with 98 missing type, 520 timeline, 0 schema, 0 new, and 2 resolved.
5. `NOW.md` remains byte-unchanged.
6. Metadata self-tests, canonical health, both whitespace scopes, live Markdown
   integrity, and Claude's three-file boundary pass.

## Loop contract

- Pass 1 applies only the five frozen control migrations.
- Loop 1 challenges root completeness and current/reference semantics against the
  complete six-page root inventory.
- Loop 2 checks body/type/topic preservation outside the one frozen navigation
  edit, exact dry-run delta and finding identity stability, health, and the
  concurrent-file boundary.
- Correct correctness failures regardless of percentage; do not turn this
  metadata phase into a rewrite of the root experience.

## Rollback and review boundary

The diff begins at `551b951`. Phase 5G remains uncommitted until Chris reviews the
final report. Approval authorizes five root metadata migrations, the one documented
`START_HERE.md` navigation connection, and this report as an exact six-file
checkpoint, followed by design of the next bounded realm.

## Pass record

### Pass 0 — baseline and frozen scope

- Root pages: 6; v2: 1; legacy controls: 5.
- Frozen retrieval target: 1 now and 5 reference.
- Safe conversions: 225.
- Findings: 618 total; 98 missing type; 520 timeline; 0 schema; 0 new; 2 resolved.
- Working tree: Claude's DAILY and two PHYSICS files, plus this report only.

### Pass 1 — frozen control migration

- Migrated the five root maps/guides/pointers to explicit
  `timeline: reference`, removing only their legacy `reference` tags.
- Preserved every type and topic tag. `NOW.md` was not edited.

### Loop 1 — complete-root semantic and usability challenge

- Enumerated all six root Markdown pages rather than relying on the migration
  manifest. Final retrieval is exactly 1 now and 5 reference, with 0 legacy root
  controls and no invented next/later/parked/log state.
- Confirmed `NOW.md` is the only active cockpit. The system map, operating guide,
  and three model boot pointers are durable entry infrastructure, not tasks.
- Initially challenged whether to add `reference_priority` and deferred it because
  root placement already expressed entry order. The later improvement loop found
  stronger retrieval evidence and corrected this decision for the two human entry
  documents only.

### Loop 2 — preservation, debt identity, health, and boundary

- All 6/6 root pages have one valid type and timeline. Before the additional
  improvement loops, the five owned Git diffs contained frontmatter changes only;
  `NOW.md` had no diff.
- Safe conversions fell exactly 225 -> 220. Reviewed findings remained 618/618:
  98 missing type, 520 timeline, 0 schema, 0 new, and the same 2 resolutions.
- Both metadata self-tests passed. The deterministic plan hash is
  `c56f8f30b4c98442a6e8c5c70b9bc825cd61aab7af71646ed856613e9b70a582`,
  with 618/618 finding identities covered and zero target writes.
- Canonical health is **PASS WITH DEBT**: 0 blockers, 4 wiki-review items, 618
  reviewed metadata findings, 0 new and 2 resolved; boot/governance, shared skill
  mirrors, both whitespace scopes, and live Markdown text integrity pass.
- Claude's DAILY and two PHYSICS files remain unstaged, unedited by Phase 5G, and
  outside the exact six-file phase boundary.

### Initial correction loop — claim precision and entry-order coherence

- Rechecked all six title/type/timeline combinations and the first-stop/second-stop
  language in `START_HERE.md` and `ROOT_OPERATING_MANUAL.md`. The additional loops
  subsequently exposed and corrected the missing return connection and core rank.
- Reworded the acceptance claim from byte identity to unchanged body content. Git
  proved a frontmatter-only semantic diff at that stage; line-ending handling is a
  storage concern and should not be overstated as byte identity.
- At that checkpoint no additional correction was warranted; the user-requested
  improvement loops then supplied new retrieval and navigation evidence.

### Additional improvement loop 1 — core-reference discoverability

- Found a user-facing contradiction: `START_HERE.md` teaches
  `[reference_priority:core]`, but the first-stop map and second-stop manual were
  absent from that result.
- Added `reference_priority: core` to exactly those two human destinations. The
  three auto-loaded model pointers remain unranked so the core human query stays
  useful instead of returning boot shims.
- Improvement: core root retrieval moves from 0 discoverable human entry pages to
  the complete 2-page first-stop/second-stop route, with no body or timeline change.

### Additional improvement loop 2 — reciprocal human navigation

- Found a one-way connection: `ROOT_OPERATING_MANUAL.md` identifies itself as the
  second stop after `START_HERE.md`, but the root map did not list or link the
  manual anywhere.
- Added one plain-language row to the root map: open the manual to use proof loops,
  ownership rules, and the closeout pattern. Updated the visible map revision date
  from July 14 to July 15 so the page does not misstate its freshness.
- Improvement: the first-stop/second-stop route is now both metadata-discoverable
  and directly navigable; no governance, permission, command, or model boot text
  changed.

### Post-improvement correction loop — functional link and scope truth

- Corrected the new manual label from inline code to a real relative Markdown link;
  the map now provides an actionable connection rather than merely naming the file.
- Corrected the rollback and approval language: the phase now contains five metadata
  migrations plus one documented `START_HERE.md` navigation edit, not a
  frontmatter-only five-page change.
- Rechecked all report claims against the final diff. Four page bodies remain
  untouched, `NOW.md` remains unchanged, and the only root body edits are the map's
  visible revision caption and the new manual row.

### Final validation after all loops and corrections

- Complete root retrieval: 6 pages; 1 now; 5 reference; 2 core human references;
  0 legacy root controls. The manual target exists, the map contains exactly one
  clickable relative link to it, and the manual still declares itself second stop.
- Safe conversions remain at the expected 220. Both metadata self-tests pass with
  deterministic hash
  `c56f8f30b4c98442a6e8c5c70b9bc825cd61aab7af71646ed856613e9b70a582`,
  618/618 finding identities covered, and zero target writes.
- Frontmatter remains **BASELINE DEBT**, not clean: 618 findings, 98 missing type,
  520 timeline, 0 schema, 0 new, and the same 2 resolved identities.
- Canonical health remains **PASS WITH DEBT**: 0 blockers; 4 wiki-review items;
  boot/governance, shared skill mirrors, staged and unstaged whitespace, and 1,159
  live Markdown text-integrity checks pass.
- Exact boundary remains five root pages plus this report. Claude's DAILY and two
  PHYSICS files remain unstaged and outside the phase; `NOW.md` remains unchanged.

## Human checkpoint

Phase 5G is complete and intentionally uncommitted. Approval authorizes five root
metadata migrations, the documented `START_HERE.md` revision caption and clickable
manual row, plus this report as an exact six-file checkpoint. It does not authorize
other root instruction changes, Claude's concurrent work, or a reviewed metadata
baseline refresh.

The health gate does not evaluate semantic freshness beyond the complete-root role
challenge performed here, review-cadence completion, source ownership/duplicate
disposition, or ordinary direct-path prose. Approval may be followed only by the
exact six-file commit and design of the next bounded Phase 5 realm.
