---
type: plan
timeline: now
status: approved
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5C — CASTLE Reference and Navigation Layer

## Outcome

CASTLE's eight non-action reference/navigation pages use metadata v2 and expose
their practical retrieval priority without being confused with the live execution
frontier. A user can distinguish the five core routers/maps from three supporting
on-demand references.

## Evidence baseline

- Approved Phase 5B checkpoint: `f7a39ea`.
- Live dry run: 253 safe complete conversions; 620 reviewed findings; 0 schema;
  0 new baseline debt.
- Seventeen CASTLE wiki pages are mechanically convertible. Eight are stable
  routers, maps, rules, or source packs tagged `reference`; nine carry `now` or
  `next` and require separate action-horizon review.
- All eight owned pages have valid `type`, exactly one legacy `reference` control,
  and no current audit finding.

## Owned manifest — exactly eight files

- Core navigation (`reference_priority: core`): `README.md`,
  `north-star-roadmap.md`, `phase-map.md`, `skill-map.md`, `source-map.md`.
- Supporting on-demand reference (`reference_priority: supporting`):
  `decision-rules\adding-a-profit-skill.md`,
  `source-summaries\claude-code-docs-pack-2026-07.md`, and
  `source-summaries\openai-platform-docs-pack-2026-07.md`.

All paths are under `00-BRAIN\CASTLE\wiki`.

## Priority rule

- `core`: a primary CASTLE entry/router or master map that organizes downstream
  pages and is expected during normal navigation.
- `supporting`: a focused rule or evidence pack retrieved for a named decision or
  claim, not part of every normal navigation pass.
- `lookup` remains available but is not assigned in this manifest; none of these
  eight pages is merely a narrow fact lookup.

Priority is retrieval usefulness, not timeline, reliability tier, authority, or
artifact status. Every owned page uses `timeline: reference`.

## Exclusions

- The nine `now`/`next` CASTLE pages: opportunity queue, phases 0–4, KSU proof
  project, field-observation skill, and SQL skill.
- CASTLE log/index/current-position, which have separate historical/live roles.
- All Session Logs except this report; all subject wikis, Library, school, raw,
  Journal, archive, client content, and Claude-owned DAILY/PHYSICS files.
- No body, link, type, tier, source-role, status, or topic wording changes unless a
  loop finds an active instruction that directly conflicts with metadata v2 or
  user navigation.

## Acceptance tests

1. Exactly eight owned files match the frozen manifest.
2. Each has one `timeline: reference`, one allowed `reference_priority`, preserved
   type/status/tier/source-role/topic tags, and zero legacy controls.
3. Core/supporting assignments follow the stated rule and are explained in the
   report; no importance is inferred from filename alone.
4. User-router language does not imply that reference priority is an action queue.
5. Safe conversions fall exactly 253 → 245; all 620 finding identities and zero
   schema debt remain unchanged.
6. Canonical health, both whitespace scopes, text/link integrity, and Claude's
   three-file boundary do not regress.

## Loop contract

- Pass 1 performs the eight metadata conversions and explicit priority assignments.
- Loop 1 challenges every core/supporting decision against page purpose and links.
- Loop 2 tests user retrieval language, property-query compatibility, migration
  delta, health, and boundaries.
- Correctness failures are fixed regardless of percentage; otherwise avoid body
  churn and document why the metadata alone is sufficient.

## Rollback and review boundary

The diff begins at `f7a39ea`. Phase 5C remains uncommitted until Chris reviews the
final report. Approval authorizes only this nine-file checkpoint (eight pages plus
this report) and design of the next bounded Phase 5 chunk.

## Pass record

### Pass 0 — baseline

- Owned v2 pages: 0/8.
- Reference-priority assignments: 0/8.
- Live safe conversions: 253.
- Reviewed findings: 620; schema findings: 0; new findings: 0.
- Working tree outside this report: Claude's DAILY and two PHYSICS files only.

### Pass 1 — reference-layer migration

- Migrated 8/8 pages to `timeline: reference` and removed exactly eight legacy
  `reference` tags while preserving types, status, tier, source role, and topics.
- Assigned `reference_priority: core` to the user router and four master maps;
  assigned `supporting` to the focused decision gate and two official-doc packs.
- Live safe conversions fell exactly 253 → 245.
- Reviewed findings remained 620/620 unchanged: 100 missing type, 520 timeline,
  0 schema, 0 new, 0 resolved.

### Loop 1 — navigation-purpose challenge

- Reviewed page purpose and inbound CASTLE references rather than treating link
  count as the priority rule. Inbound counts ranged from 1 to 7.
- Confirmed the five core pages are the ordinary router/master maps even where a
  focused decision rule has more inbound links. The rule and docs packs remain
  supporting because they are retrieved for named decisions or claims.
- Found one usability gap: the user router did not explain how to retrieve the two
  reference layers or distinguish retrieval priority from the action queue.
- Initially added property searches for core reference, supporting reference, and
  current work. The additional transition check below corrected the current-work
  route because its property query was not yet complete.

### Loop 2 — metadata, body, query, and boundary challenge

- Reference-layer validation: **PASS (8/8; core=5; supporting=3)**.
- Body comparison against `f7a39ea`: seven bodies unchanged; only `README.md`
  contains the documented navigation guidance.
- The router states explicitly that `reference_priority` selects reference layer
  and utility, never “work on this now”; `timeline` controls action horizon.
- Metadata and migration self-tests pass. Deterministic plan SHA-256:
  `4a08c054861ed966ff80872c2c8f7b5075448d49fdbb700eefb6cf22f21426cb`.
- The additional transition check below tested query completeness against the
  nine excluded live-action pages without modifying them.

### Additional transition check — query completeness

- Tested the router's searches against the live mixed metadata state rather than
  validating syntax alone.
- CASTLE has 5 current `now` pages: 1 uses `timeline: now`; 4 still use the legacy
  `now` tag and are intentionally deferred to Phase 5D. The proposed
  `[timeline:now]` search therefore hid 80% of the current CASTLE pages.
- Replaced that incomplete query with the canonical `.ROOT\NOW.md` route and a
  plain transition warning. The property search can be restored only after the
  action-page migration is complete.
- Changed the roadmap description from “current priorities” to “durable pathway
  and sequencing context,” preserving `NOW.md` as current-work authority.
- Reworded `reference_priority` from retrieval frequency to reference layer and
  utility, matching the Metadata Standard.

## Acceptance result

| Test | Result | Evidence |
|---|---|---|
| Frozen manifest | PASS | exactly 8 owned pages |
| Valid reference metadata | PASS | 8/8; zero legacy controls |
| Priority split | PASS | 5 core routers/maps; 3 supporting rule/evidence pages |
| User retrieval guidance | PASS | two complete reference searches + canonical NOW route |
| Retrieval/action distinction | PASS | explicit priority-vs-timeline rule |
| Body control | PASS | 7 unchanged; 1 documented router improvement |
| Expected dry-run delta | PASS | safe conversions 253 → 245 |
| Baseline identity preservation | PASS | 620 unchanged; 0 new/resolved/schema |
| Canonical health | PASS WITH DEBT | 0 blockers; 4 wiki review; 620 reviewed metadata debt |
| Claude boundary | PASS | 3 concurrent files remain outside Phase 5C |

## Review checkpoint

Chris approved Phase 5C on July 15, 2026. Approval authorizes only an isolated
nine-file checkpoint (eight pages plus this report) and design of the next bounded
Phase 5 chunk. The nine CASTLE action pages remain excluded from this checkpoint
and require their own current-truth review.

The canonical health gate does not evaluate semantic freshness, review-cadence
completion, source ownership/duplicate-source disposition, or all ordinary
direct-path prose; those claims remain with their owning reviews.
