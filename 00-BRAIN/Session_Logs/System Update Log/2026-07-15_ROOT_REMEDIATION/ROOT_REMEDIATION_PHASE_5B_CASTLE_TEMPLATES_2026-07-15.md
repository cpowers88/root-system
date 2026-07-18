---
type: plan
timeline: now
status: approved
tags: [governance, audit]
created: 2026-07-15
---

# Phase 5B — CASTLE Creation-Template Metadata

## Outcome

Each CASTLE template truthfully identifies the live file as an active reference
template while giving a valid, explicit metadata block for the artifact created
from it. Template placeholders no longer masquerade as the template file's own
status, category, tier, or source role.

## Evidence baseline

- Approved Phase 5A checkpoint: `dcddab9`.
- Live dry run after Phase 5A: 260 safe complete conversions; 620 reviewed
  findings; 0 schema findings; 0 new baseline debt.
- All seven files currently have a generated-artifact `type`, a legacy
  `reference` tag, and no `timeline` property.
- Five files encode multiple allowed `status` values as one pipe-delimited YAML
  scalar; `skill-template` also does this for `category`; `source-summary-template`
  does it for `tier` and `source-role`. The audit accepts those strings, but they
  describe choices for a future copy, not facts about the live template file.

## Owned manifest — exactly seven files

All are under `00-BRAIN\CASTLE\templates`:

- `decision-rule-template.md`
- `evidence-template.md`
- `phase-template.md`
- `project-template.md`
- `service-capability-template.md`
- `skill-template.md`
- `source-summary-template.md`

## Template contract

The live template file uses:

```yaml
type: template
timeline: reference
status: active
template_for: <generated artifact type>
tags: [<topic tags only>]
```

Each body begins with a plain-language use instruction and a fenced YAML block
describing the copied artifact. Fixed values stay fixed; true choices use one
angle-bracket list of allowed values. Base topic tags are immediately valid;
`timeline` is explicit and independent from `status`.

## Exclusions

- No CASTLE wiki action page, log, phase, skill, proof project, or source summary.
- No Session Log other than this Phase 5B report.
- No subject wiki, Library, school, raw, Journal, archive, client content, or
  Claude-owned DAILY/PHYSICS file.
- Existing body prompts remain intact except for the new copy-metadata guidance.
- This phase does not decide the current status/timeline of any existing artifact.

## Acceptance tests

1. Exactly seven template files are owned.
2. Every live file has `type: template`, `timeline: reference`, `status: active`,
   the correct `template_for`, preserved topic tags, and zero legacy controls.
3. Every copy block contains one concrete generated `type`, one `timeline`, topic-
   only tags, and any artifact-specific choice fields formerly in live frontmatter.
4. Copy blocks make timeline/status independence clear for phase, project,
   service-capability, and skill artifacts.
5. Live safe conversions fall exactly 260 → 253; the 620 reviewed finding
   identities and zero schema debt remain unchanged.
6. Canonical root health and both whitespace scopes do not regress; Claude's
   three files remain outside the phase.

## Loop contract

- Pass 1 converts the seven live frontmatters and adds seven copy blocks.
- Loop 1 validates the template itself separately from the generated artifact.
- Loop 2 challenges placeholder clarity, allowed value preservation, deterministic
  migration delta, link/text integrity, and Claude boundaries.
- Correctness failures are fixed regardless of percentage; otherwise document
  why further wording churn would reduce clarity rather than improve it.

## Rollback and review boundary

The diff begins at `dcddab9`. Phase 5B remains uncommitted until Chris reviews
the final report. Approval authorizes only this eight-file checkpoint (seven
templates plus this report) and design of the next bounded Phase 5 chunk.

## Pass record

### Pass 0 — baseline

- Truthful template-file metadata: 0/7.
- Explicit copied-artifact metadata blocks: 0/7.
- Live safe conversions: 260.
- Reviewed findings: 620; schema findings: 0; new findings: 0.
- Working tree outside this report: Claude's DAILY and two PHYSICS files only.

### Pass 1 — separate live-template and copied-artifact metadata

- Converted 7/7 live files to `type: template`, `timeline: reference`,
  `status: active`, the correct `template_for`, and preserved topic-only tags.
- Relocated generated-artifact `type`, timeline/status choices, skill category,
  source tier, and source role into one copy block per template.
- Added `reference_priority` to the source-summary copy block so reference utility
  remains independent from reliability tier and roadmap role.
- Live safe conversions fell exactly 260 → 253.
- Reviewed findings remained 620/620 unchanged: 100 missing type, 520 timeline,
  0 schema, 0 new, 0 resolved.

### Loop 1 — paste and replacement challenge

- Found that the initial copy examples were structurally valid but not fully
  paste-ready: they omitted YAML frontmatter delimiters and did not explicitly
  say to replace the copied file's entire frontmatter.
- Added `---` delimiters to all 7 blocks and made full-frontmatter replacement
  explicit, preventing an AI from appending a second metadata block.
- Clarified that every angle-bracket choice must be resolved and only topic tags
  remain in `tags`.
- Measured result: paste-ready blocks 0/7 → 7/7; explicit replacement rules
  0/7 → 7/7.

### Loop 2 — dual-role and vocabulary challenge

- Validated live-template metadata separately from copied-artifact metadata:
  **PASS (7/7)** for both roles.
- Programmatically resolved every copy block to its first allowed choice and ran
  the metadata-v2 validator: 7/7 resolved copies pass.
- Confirmed exact preservation of the original status lists, eight skill
  categories, four source tiers, and six source roles.
- Metadata and migration self-tests pass. Deterministic plan SHA-256:
  `5e3345c110b4f4bc7378cda653062a81a205741eb7c45f26847b3884943738e7`.
- No further wording or schema change improved clarity without adding choices not
  supported by the original templates.

### Additional usability pass — first-time copy workflow

- Walked all 7 files as a first-time user performing the complete copy workflow,
  not only as a metadata validator.
- Found two consistent friction points: `<topics...>` could be deleted in a way
  that left invalid list punctuation, and the helper never explicitly said to
  rename the copy or remove the helper block afterward.
- Replaced every topic placeholder with an immediately valid base tag list. Users
  may add optional topic tags without first repairing YAML.
- Standardized the workflow in all 7 files: copy and rename file/title → replace
  frontmatter → choose values/add optional topics → delete the instruction and
  example block.
- Added a plain-language five-value timeline legend to all 5 variable-timeline
  templates; evidence and source-summary retain an explained fixed `reference`
  timeline.
- Measured improvement: valid base tags 0/7 → 7/7; rename guidance 0/7 → 7/7;
  cleanup guidance 0/7 → 7/7; timeline legends 0/5 → 5/5.
- Usability + dual-role validation: **PASS (7/7)**. Choice vocabularies, migration
  counts, and deterministic plan hash remain unchanged.

## Acceptance result

| Test | Result | Evidence |
|---|---|---|
| Frozen manifest | PASS | exactly 7 templates |
| Truthful live metadata | PASS | 7/7 template/reference/active/template_for |
| Paste-ready copy metadata | PASS | 7/7 full blocks with valid base tags and cleanup workflow |
| Timeline/status independence | PASS | explicit phase/project/service/skill rules |
| Choice-vocabulary preservation | PASS | all original lists retained exactly |
| Resolved-copy validation | PASS | 7/7 pass metadata v2 |
| Expected dry-run delta | PASS | safe conversions 260 → 253 |
| Baseline identity preservation | PASS | 620 unchanged; 0 new/resolved/schema |
| Canonical health | PASS WITH DEBT | 0 blockers; 4 wiki review; 620 reviewed metadata debt |
| Claude boundary | PASS | 3 concurrent files remain outside Phase 5B |

## Review checkpoint

Chris approved Phase 5B on July 15, 2026. Approval authorizes only an isolated
eight-file checkpoint (seven templates plus this report) and design of the next
bounded Phase 5 chunk.

The canonical health gate does not evaluate semantic freshness, review-cadence
completion, source ownership/duplicate-source disposition, or all ordinary
direct-path prose; those claims remain with their owning reviews.
