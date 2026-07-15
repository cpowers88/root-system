---
type: plan
timeline: log
status: approved
tags: [governance, audit, source-routing]
created: 2026-07-15
---

# Phase 6D — Source Routing and Disposition

## Outcome

Every file in the closed legacy source holding area now has a hash-backed
disposition without changing that raw boundary. The Make.com collection is a
deliberately indexed reference corpus instead of an ambiguous half-source lane.
Two redundant value-stream-mapping clippings are preserved in the archive and no
longer sit inside the CSE/Python course lane.

## Evidence

- Approved Phase 6C checkpoint: `08b1354`.
- `02-LIBRARY\.raw ARCHIVE\` contains 12 files: 7 have byte-identical live-home
  copies, 2 have verified knowledge-page evidence homes but no live exact copy,
  and 3 remain unprocessed.
- The Make.com folder began with 44 nonduplicate files: one synthesis and 43
  vendor-documentation captures. It had no human entry point and carried 85
  metadata findings: 42 missing `type` and 43 missing `timeline`.
- The two CSE/Python VSM clippings had no inbound links. Their subject is already
  represented by the SYSTEMS VSM method page and BUSINESS lean-methodology page.

## Owned paths

1. `00-BRAIN\WHERE_IT_GOES.md`.
2. `02-LIBRARY\08-AI-AUTOMATION\make.com_notes\` — frontmatter-only
   normalization of the 44 existing files plus one new `README.md`.
3. `03-WIKIS\BUSINESS\wiki\ai-integration-company\theory-of-constraints.md`.
4. `03-WIKIS\TECHNOLOGY\wiki\ai-and-llm\ai-developer-tools-landscape-2026.md`.
5. The two former CSE/Python VSM paths and their dated physical archive copies.
6. This report.

## Exclusions

- No file inside `.raw ARCHIVE`, any wiki `raw`, or Journal was edited, moved,
  renamed, or deleted.
- The three unprocessed legacy sources were not promoted merely to make the
  inventory look complete; routing still requires a real research question and
  an explicit raw exception.
- Imported Make Help Center `docId:` links were not converted into invented local
  notes. The README identifies them as vendor capture artifacts.
- Claude's PHYSICS current-position and log remain outside this phase.

## Legacy Source Manifest

The `SHA-256` value identifies the retained legacy file. “Live match” means a
byte-identical copy outside raw holding, Journal, and archive.

| Legacy file | SHA-256 | Disposition | Owner / evidence home |
|---|---|---|---|
| `12 Small Business Automation Ideas & Tools for Efficiency.md` | `D4B02393DB4AA92078DDF1D1ED1677377305A1B46DBB6024DC4D228667B16AD7` | Unprocessed; retained | Proposed BUSINESS intake only when a specific SMB-automation research question justifies it |
| `CoIntelligence.pdf` | `C631F638751082FE70F23A8F8EA0BF8EC87DB8B303C9E59CFFBEFDC81B9E6CCA` | Exact duplicate | `02-LIBRARY\08-AI-AUTOMATION\Co-Intelligence.pdf` |
| `Entrepreneurship.pdf` | `B38EB737B886D16E4321A27645F369042F2476B1CD3BC4DC6EB4120F37EEE15D` | Exact duplicate | `03-WIKIS\BUSINESS\raw\Entrepreneurship.pdf` |
| `Foundations of Scalable Systems.pdf` | `5A5459A6797DCAC443CE0E29F6910192213632DAAE368F4391EBA9DDA9BD2F9A` | Exact duplicate | `03-WIKIS\TECHNOLOGY\raw\Foundations of Scalable Systems.pdf` |
| `How This Course Will Work  The Odin Project.md` | `FA38576970C10111DC9CA2516E2C374437EA9D182E0E57BDA58A48A12CABC72D` | Unprocessed; retained | Proposed TECHNOLOGY intake if web-development foundations become active |
| `python-crash-course.pdf` | `A909B38F22B60A860CEB7F80CDBBEE3AF776BA8CCF36864375B0D75534C2A1AE` | Exact duplicate | `03-WIKIS\PYTHON\raw\books\python-crash-course.pdf` |
| `The Goal, GOLDRATT.pdf` | `C235A717BA1F683AF3CF776900F23EDB0C4808FEA4FD07AC233A958BDF968033` | Processed; retained source | `03-WIKIS\BUSINESS\wiki\ai-integration-company\theory-of-constraints.md`; source path corrected in page |
| `theChecklisManifesto.pdf` | `00F5F8BB4C6ED5E63BD66B0F4DD5E3FDDADA9446267C457E8CC6CF7E36C81D7F` | Exact duplicate | `03-WIKIS\BUSINESS\raw\theChecklisManifesto.pdf` |
| `thePhoenixProject.pdf` | `B089A07D496244FEF85E086C14E0637E90DF3A82405F76B028EF715D8CB93D0A` | Exact duplicate | `03-WIKIS\BUSINESS\raw\thePhoenixProject.pdf` |
| `thinkpython.pdf` | `7A8A8A7B0B433F9E85C49ECB524EDD7344FA1822FD85B5B60E77B826D6E28A37` | Exact duplicate | Canonical source: `03-WIKIS\PYTHON\raw\books\thinkpython.pdf`; course copy: `02-LIBRARY\00-SCHOOL\01-CSE-Python\thinkpython.pdf` |
| `Top AI Tools for Developers in 2026 Best GenAI Coding Tools.md` | `B488C1CCC136C41EB3218D3519299A8B25AE73D6E105804472E7807D8D6CD9F6` | Processed; retained source | `03-WIKIS\TECHNOLOGY\wiki\ai-and-llm\ai-developer-tools-landscape-2026.md`; false `raw/` path corrected |
| `Type This Into Claude, It'll Make You Build 10x Faster.md` | `1A04A4D5CD461078472439B2CAE8B2F5A3CDD07663E4B7588EFF2A27C96638C8` | Unprocessed; retained | Proposed AI_AUTOMATION_SYSTEMS intake only after source-quality review and a live question |

## Make.com Corpus Disposition

- Chosen disposition: normalized, deliberately indexed reference corpus in its
  existing stable library home. It is not a new wiki intake lane.
- Added `type: reference`, `timeline: reference`, and `status: source-capture`
  where missing; the synthesis retains `type: landscape-rep` and `status: research`.
- Added one README with a start-here instruction, nine practical lookup categories,
  a volatility warning, and an explicit boundary for imported vendor IDs.
- README coverage: 44 unique wikilink targets, 44 resolved; all 43 captures plus
  the synthesis are reachable. No byte-identical duplicates exist in the corpus.
- Metadata result: 85 prior findings resolved; 0 required-field or dual-encoding
  findings remain in the 45-file folder.

## VSM Disposition

- Removed both clippings from `02-LIBRARY\00-SCHOOL\01-CSE-Python\Notes\`.
- Preserved dated copies in `99-ARCHIVE\`, with plain-text authors, corrected
  subject tags, `timeline: log`, `status: archived`, and notes naming both
  canonical knowledge homes.
- Verified the article bodies are byte-for-byte text-identical from the first
  content heading/paragraph onward. The second file's stray leading colon was
  removed as capture noise.
- Verified 0 inbound links to either former course-note path.

## Loop Record

### Pass 0 — evidence freeze

Frozen all 12 source hashes, exact live-home matches, the 44-file Make inventory,
both VSM targets, the `08b1354` rollback point, and Claude's two-file boundary.
No disposition was inferred from filename similarity alone.

### Pass 1 — smallest coherent repair

Closed the legacy folder to new intake in placement authority; wrote the complete
manifest; normalized and indexed Make.com; corrected two false/missing source
connections; and archived the redundant VSM clippings with content preservation.

### Loop 1 — discoverability and schema clarity

- **Quality dimension:** one-step retrieval without metadata ambiguity.
- **Baseline:** Make.com had 0 entry pages, only 1/44 files had both required
  metadata fields, and the legacy source set had no complete disposition map.
- **Target:** improve retrieval/schema clarity by 3–10% without broad renaming,
  source rewriting, or raw movement.
- **Measured result:** entry-page coverage moved 0/44 -> 44/44; required metadata
  coverage moved 1/44 -> 44/44; source disposition moved 0/12 -> 12/12. The
  completeness jump exceeds the target because partial routing would preserve the
  original failure.
- **Correction found:** the first audit exposed two legacy `reference` tags beside
  `timeline: reference`; both were removed, eliminating dual encoding.

### Loop 2 decision

Loop 1 exposed no second failure class after the two-tag correction. Per protocol,
Loop 2 was not run without a new class or human request.

### Correction loop

Verified required metadata, all README targets, exact source hashes and homes,
VSM archive existence/body preservation, former-path absence, source citations,
complete diff, phase boundary, root health, and both whitespace states.

## Acceptance Tests

1. All 12 legacy files have full hashes, dispositions, and owner/evidence homes.
2. The legacy folder is explicitly closed; raw contents remain unchanged.
3. Make.com has one clear start page; 44/44 targets resolve; 0 local metadata
   findings remain.
4. Both VSM clippings are absent from CSE/Python, present in archive, content
   preserved, and connected to canonical SYSTEMS/BUSINESS homes.
5. Canonical health, boot/governance, wiki navigation, shared skills, Markdown
   integrity, and staged/unstaged whitespace pass with no new metadata debt.
6. Only the Phase 6D owned set enters the checkpoint; PHYSICS remains excluded.

## Final Validation

- Canonical health: **PASS WITH DEBT**.
- Boot/governance: PASS.
- Wiki navigation: PASS — 0 blockers, 0 review debt, 773 expected classifications.
- Metadata remains reviewed baseline debt: 530 findings, 0 new, 90 resolved.
- Shared skill mirrors: PASS.
- Live Markdown integrity: 1,167 files checked, 0 findings.
- Unstaged and staged whitespace: PASS.
- Source-routing scope, which root health explicitly does not evaluate: 12/12
  hashes unchanged; 0 raw-path changes; 44/44 README targets resolve; both VSM
  archive copies exist and both preserved article bodies compare identical.
- Boundary: 51 Phase 6D tracked checkpoint paths; Claude's 2 PHYSICS paths remain
  changed but excluded.

## Rollback Boundary

The Phase 6D tracked diff begins at `08b1354`. Reverting the checkpoint restores
the 50 tracked live-path changes plus this report; the two ignored physical archive
copies must be reviewed separately so preservation is not accidentally reversed.

## Human Approval

Chris approved this exact source-routing checkpoint on July 15, 2026. The approval
does not include Claude's two PHYSICS files or authorize movement inside a raw
boundary. Phase 7 begins only after this isolated checkpoint is committed.
