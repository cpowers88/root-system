---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5J — Project Document Metadata

## Outcome

The complete six-page `.PROJECTS` document layer separates two current projects,
two on-deck internal actions, and two paused projects through metadata v2. The YT
scanner's internal routes are clickable and its pending human decisions are explicit,
without changing code, evidence, outputs, secrets, external repositories, or public
authorization.

## Evidence baseline

- Approved Phase 5I checkpoint: `22e531c`.
- `02-LIBRARY\.PROJECTS` contains exactly 6 Markdown pages: 2 valid v2 pages,
  3 safe legacy conversions, and 1 reviewed timeline finding.
- Live dry run: 208 safe conversions; 618 findings; 98 missing type; 520 timeline;
  0 schema; 0 new baseline debt; 2 previously resolved.
- Current truth: KSU Tracker awaits real D2L/syllabus use; Lane A's scanner remains
  active but its immediate internal step is human classification. No more scanner
  build is needed today. TCG POS and Listing Packet are explicitly paused.

## Frozen role manifest

- Preserve `KSU_Academic_Tracker_Brief.md` unchanged: `timeline: now`,
  `status: ready`.
- `YT_Outlier_Scanner\README.md`: `timeline: now`, `status: active`; preserve topic
  tags. The validated scanner remains in a one-month internal evidence loop.
- `YT_Outlier_Scanner\channels_seed.md`: `timeline: next`,
  `status: awaiting-review`; preserve topic tags. Confirm/drop unapproved niches
  before a later harvest, after the current top-100 classification step.
- `YT_Outlier_Scanner\PRIVATE_PROOF_OUTLINE.md`: resolve the missing timeline as
  `next`; preserve `status: internal-only` and topic tags. The private proof is
  approved internal work, not a public-content authorization or today's first step.
- `TCG_POS\TCG_POS_SCOPING.md`: `timeline: parked`, `status: paused`; preserve the
  `project` topic tag.
- Preserve `listing-packet\MOVED_TO_LOCAL.md` unchanged: `timeline: parked`,
  `status: paused`.

## Frozen body corrections

- Remove TCG POS's redundant `#TCG #projects` body-tag line.
- Change both stale “before first harvest” instructions—the seed-list title and
  README setup sentence—to “before the next harvest,” because the first scans are
  complete.
- Convert exactly five named YT connections to relative Markdown links: two seed
  references, private proof outline, Lane A charter, and first-findings review.

## Exclusions

- No other body text, project requirement, code, command, data, database, output,
  evidence, channel choice, title, timer, privacy rule, secret, path, status claim,
  external repository, public action, or authorization change.
- No raw, Journal, wiki-body, archive, client, account, publishing, monetization,
  outreach, or baseline edit.
- All concurrent work remains outside the phase boundary. Because that set changed
  during validation, ownership is enforced by an exact five-file Phase 5J allowlist,
  not by assuming a static list of unrelated modified files.

## Acceptance tests

1. All 6 pages have one valid type/timeline/status. Retrieval is exactly 2 now,
   2 next, and 2 parked; legacy controls fall 3 -> 0.
2. The private-proof timeline finding resolves with no new finding: total debt
   falls 618 -> 617; timeline 520 -> 519; resolved identities 2 -> 3.
3. Safe conversions fall exactly 208 -> 205; both existing-v2 pages remain
   unchanged.
4. Exactly one body-tag line and two stale-harvest phrases are corrected; the five
   converted link occurrences (two seed links plus three other routes) resolve to
   existing targets.
5. No project code/output/secret or external repository is read or written by the
   phase; only four project Markdown pages and this external report change.
6. Metadata self-tests, canonical health, both whitespace scopes, live Markdown
   integrity, and the concurrent-file boundary pass.

## Loop contract

- Pass 1 applies only the frozen metadata and body/link corrections.
- Loop 1 challenges project timelines/statuses against `NOW.md`, Revenue Lab,
  CASTLE, dates, approvals, and explicit project conditions.
- Loop 2 checks complete-realm retrieval, link functionality, exact debt resolution,
  existing-v2 preservation, health, and the concurrent-file boundary.
- A correction loop fixes claim or function defects without reopening any project
  or authorizing external work.

## Rollback and review boundary

The diff begins at `22e531c`. Phase 5J remains uncommitted until Chris reviews the
final report. Approval authorizes four bounded project-page edits plus this report
as an exact five-file checkpoint and design of the next bounded realm.

## Pass record

### Pass 0 — baseline and frozen scope

- Realm pages: 6; v2: 2; legacy controls: 3; reviewed findings: 1 timeline.
- Frozen retrieval target: 2 now / 2 next / 2 parked.
- Safe conversions: 208. Findings: 618 total; 98 missing type; 520 timeline;
  0 schema; 0 new; 2 resolved.
- Working tree: four concurrent Claude files plus this report only.

### Pass 1 — frozen metadata and connection corrections

- Applied three legacy migrations, one manual timeline decision, three explicit
  status additions, one tag-line removal, one title correction, and five link
  conversions.
- Preserved all types, all frontmatter topic tags, and both existing-v2 pages.

### Loop 1 — live project horizon and authorization challenge

- Preserved KSU Tracker as now/ready: V1 is shipped but the around-July-25 real-data
  use remains active. Preserved Listing Packet as parked/paused.
- Kept the YT scanner README now/active because the one-month evidence loop and
  human top-100 classification remain current. Moved channel seeds to
  next/awaiting-review because confirmation is required only before the next
  harvest, after today's classification step.
- Resolved the private proof outline as next/internal-only: the proof is approved
  bounded internal work, but not the immediate next action and never public
  authorization.
- TCG POS is parked/paused because its June 23 qualifying-commitment gate closed
  without evidence. Metadata does not reopen it.

### Loop 2 — complete retrieval, debt resolution, links, and preservation

- Complete six-page result: 2 now, 2 next, 2 parked; 6/6 explicit statuses;
  0 legacy controls and 0 project-layer audit findings.
- The private-proof finding resolves without replacement. Reviewed debt falls
  618 -> 617; timeline findings 520 -> 519; resolved identities rise 2 -> 3;
  new findings remain 0.
- Safe conversions fall 208 -> 205. Both existing-v2 pages—KSU Tracker and Listing
  Packet—remain unchanged.
- Five converted link occurrences resolve: two channel-seed routes plus the private
  outline, Lane A charter, and first-findings review. All targets exist.

### Correction loop — stale wording, readability, and scope truth

- Found a second stale “before first harvest” sentence in the README after fixing
  the seed-list title. Corrected both to “next harvest”; final counts are 0 old and
  2 corrected phrases.
- Wrapped long link sentences without changing meaning. Removed only TCG's redundant
  tag-only line; no other project body content was deleted.
- Rechecked authorization language: private proof stays internal-only; no channel,
  account, publishing, monetization, affiliate, outreach, or project reactivation is
  authorized.
- Concurrent work changed repeatedly during the phase. Final boundary evidence uses
  the exact Phase 5J allowlist rather than incorrectly treating the unrelated set as
  static.

### Final validation

- Both metadata self-tests pass with deterministic plan hash
  `6618b9a945da27a91f433acd3ccbd1ab92767dae3f4d6a6313a1e43ca4b3c051`,
  617/617 finding identities covered, and zero target writes.
- Frontmatter remains **BASELINE DEBT**, not clean: 617 findings, 98 missing type,
  519 timeline, 0 schema, 0 new, and 3 resolved identities.
- Canonical health is **PASS WITH DEBT**: 0 blockers, 4 wiki-review items; boot and
  governance, shared skill mirrors, both whitespace scopes, and 1,163 live Markdown
  text-integrity checks pass.
- Exact Phase 5J boundary is four project pages plus this report. Every other
  working-tree change remains unstaged and outside it, including governance,
  CASTLE, contract, and PHYSICS work that appeared during validation.

## Human checkpoint

Phase 5J is complete and intentionally uncommitted. Approval authorizes exactly four
bounded project-page edits plus this report as a five-file checkpoint. It does not
approve any public action, project reopening, code/output/secret change, account,
publishing, monetization, outreach, concurrent file, or baseline refresh.

The health gate does not evaluate semantic freshness beyond the project-state and
authorization challenge performed here, whether the human classification or
one-month evidence cadence was completed, external repository truth, or all ordinary
direct-path prose. Those remain with their owning reviews.
