---
type: specification
timeline: next
status: research-only
tags: [business, technology, value, decision-making]
created: 2026-07-29
---

# Gate B — Value Decision Engine Interface and Test Specification

> **RESEARCH-ONLY · IMPLEMENTATION-LOCKED**
>
> This document specifies future behavior. It authorizes no files, code,
> fixtures, downloads, API execution, database changes, or package installation.
> Gate B becomes build authority only after Chris explicitly approves it and
> reopens a named implementation slice.

## 1. V1 System Boundary

```text
source manifest
      +
read-only CSV or SQLite input
      ↓
source adapter
      ↓
normalized operational records
      ↓
data-quality gate
      ↓ PASS / PASS_WITH_WARNINGS
transparent exception rules
      ↓
scored findings + proposed smallest tests
      ↓
decision packet
      ↓
Chris disposition
      ↓
later measured-outcome comparison
```

Core analysis must not know whether a record came from KSU, NYC, Atlanta, or
another compatible source. Source-specific interpretation belongs in the manifest
and adapter.

## 2. Planned Command Interface

These commands describe the future public interface:

```text
value_engine validate --manifest <path>
value_engine run --manifest <path>
value_engine review --run <run_id> --finding <id> --disposition <value>
                    --rank <integer> --reason <text>
value_engine compare --baseline <run_id> --candidate <run_id>
```

Behavior:

- `validate` reads and reports; it creates no recommendation.
- `run` proceeds only after a passing validation gate.
- `review` changes only the human-review artifact, never generated findings.
- `compare` explains changed findings, rules, thresholds, scores, and
  dispositions.
- Every command returns a nonzero exit status on a contract failure.
- Error messages name the failing boundary and corrective action.

No `implement`, `send`, `publish`, `update-source`, or automated-action command is
part of V1.

## 3. Dataset Manifest Contract

Required conceptual fields:

| Field | Type | Rule |
|---|---|---|
| `dataset_id` | string | Stable across snapshots of the same logical source |
| `title` | string | Human-readable |
| `publisher` | string | Source authority |
| `source_url` | URL | Official provenance page or endpoint |
| `source_type` | enum | `csv` or `sqlite` |
| `source_path` | path | Existing local input |
| `adapter` | string | Registered adapter identifier |
| `snapshot_date` | date | Retrieval or database snapshot date |
| `as_of_date` | date | Fixed analytical clock |
| `decision_question` | string | One decision, not a topic |
| `scope` | string | Included period/population |
| `exclusions` | list[string] | Known omissions |
| `field_map` | object | Source field to normalized-field mapping |
| `valid_states` | list[string] | Source-defined accepted states |
| `thresholds` | object | Named, sourced analytical thresholds |
| `consequence_basis` | enum | `measured`, `proxy`, or `unknown` |

Manifest failures:

- missing required field;
- unsupported source type;
- nonexistent path;
- duplicate mapping;
- invalid date;
- `as_of_date` preceding the scoped period;
- missing official provenance for a public source;
- measured consequence without a named input and calculation;
- threshold without definition or source.

The manifest snapshot and input SHA-256 checksum identify the run.

## 4. Normalized Record Contract

| Field | Type | Required | Meaning |
|---|---|---:|---|
| `record_id` | string | yes | Stable source or derived identifier |
| `dataset_id` | string | yes | Manifest source identifier |
| `category` | string | yes | First-level work/problem type |
| `subcategory` | string/null | no | More specific type |
| `owner` | string/null | no | Accountable course, agency, or workflow owner |
| `location_group` | string/null | no | Non-private geography/group |
| `channel` | string/null | no | Intake or operating channel |
| `opened_at` | datetime/null | no | Case/work creation |
| `due_at` | datetime/null | no | Source-defined deadline |
| `closed_at` | datetime/null | no | Source-defined closure |
| `state` | string/null | no | Original operational status |
| `value_amount` | decimal/null | no | Only when source-grounded |
| `value_unit` | string/null | no | Dollars, hours, count, etc. |
| `source_row_number` | integer/string | yes | Trace back to input |
| `source_fields` | object | yes | Original selected fields |
| `validation_flags` | list[string] | yes | Empty when valid |

Normalization rules:

- preserve original values before normalization;
- parse dates into one documented ISO-8601 representation;
- never silently repair malformed states or dates;
- maintain stable IDs across identical inputs;
- reject duplicate normalized IDs;
- omit unnecessary address-level or sensitive location fields;
- do not create financial values from operational proxies.

## 5. Adapter Contract

An adapter must:

1. Declare its supported source type and semantic assumptions.
2. Verify required source fields before reading records.
3. Map one source record to one normalized record unless aggregation is explicitly
   declared.
4. Preserve source traceability.
5. Report rejected records and reasons.
6. Avoid source writes.
7. Expose adapter version in every run.

V1 planned adapters:

- `ksu_tracker_v1` — SQLite-specific.
- `service_request_311_v1` — manifest-driven CSV adapter.

A new conventional 311 dataset passes portability when it needs a new manifest and
field mapping only. New code is justified when its lifecycle/state semantics cannot
be represented by the existing adapter.

## 6. KSU Adapter Research Baseline

Live schema inspected July 29, 2026:

- `courses(course_id, code, name, professor, credit_hours)`
- `assignments(assignment_id, course_id, name, due_date, status, grade, notes_file)`
- `tests(test_id, course_id, name, test_date, chapters_covered, study_status, notes_file)`
- `readings(reading_id, course_id, chapter, pages, due_date, completed, notes_file)`

Current fixture state:

- 5 courses;
- 1 assignment;
- 1 test;
- 0 readings;
- assignment state `pending\` is malformed relative to the brief's declared states;
- sample paths and records are not verified Fall operational truth.

The future adapter must open SQLite using a read-only URI and demonstrate unchanged
input checksum before and after the run.

## 7. NYC 311 Adapter Research Baseline

Official dataset identifier: `erm2-nwe9`.

Official interface research confirms:

- dataset updates daily and field values may change;
- `unique_key` identifies the service request;
- `created_date` and `closed_date` describe lifecycle dates;
- `agency`/`agency_name` identify the responding owner;
- `complaint_type` and `descriptor` provide hierarchy;
- `resolution_description` and `resolution_action_updated_date` provide last-action
  context;
- geography and intake-channel fields are available;
- the dataset excludes requester personally identifying information.

Planned minimum field selection:

```text
unique_key
created_date
closed_date
agency
agency_name
complaint_type
descriptor
location_type
incident_zip
status
due_date
resolution_description
resolution_action_updated_date
borough
open_data_channel_type
```

Research sources:

- https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9
- https://catalog.data.gov/dataset/311-service-requests-from-2010-to-present
- https://dev.socrata.com/docs/queries/index.html

Snapshot rules:

- fixed 90-day completed period, not a moving "last 90 days";
- Department of Buildings records if schema/sample coverage is adequate;
- no more than 5,000 records for V1;
- explicit field selection;
- explicit stable ordering by `unique_key` after the date filter;
- query text, retrieval date, response count, and source metadata saved with the
  future snapshot;
- no app token for the first bounded proof; throttling or reliability failure
  returns to the gate rather than creating an account silently.

Socrata documentation requires explicit ordering for stable paging. The V1 query
must use bounded filtering rather than bulk export or deep paging.

## 8. Data-Quality Gate

Required metrics:

- input rows;
- accepted/rejected rows;
- duplicate IDs;
- missing required fields;
- invalid states;
- invalid/reversed dates;
- missing category/owner;
- source checksum;
- usable-record percentage;
- limitations.

Statuses:

| Status | Rule |
|---|---|
| `PASS` | No critical defect and at least 95% usable |
| `PASS_WITH_WARNINGS` | At least 80% usable with limitations disclosed |
| `FAIL` | Below 80%, duplicate IDs, unreadable source, or broken mapping |

`FAIL` produces a validation artifact only. It suppresses findings and
recommendations.

These percentages are V1 operational defaults, not universal truths. The first
tuning cycle must test whether they hide a decision-relevant defect.

## 9. Finding Contract

Every finding includes:

```text
finding_id
rule_id and version
decision_question
population definition
numerator / denominator
calculation
threshold and source
representative record IDs
severity
frequency
consequence
confidence
actionability
total priority score
measured/proxy/unknown consequence label
limitations and disconfirming evidence
Recommendation Ladder rung
proposed smallest test
success signal
stop rule
owner
review trigger
```

Planned rule families:

- invalid record;
- overdue open;
- closed late;
- aged open;
- high cycle time;
- category concentration;
- owner concentration;
- missing decision data;
- repeated pattern.

Volume alone is not an exception. A source-defined deadline, comparative baseline,
documented threshold, or explicit decision need must support the interpretation.

## 10. Transparent Score Contract

Five 1–5 components:

- severity;
- frequency;
- consequence;
- confidence;
- actionability.

Planned V1 weighting:

```text
severity      25%
frequency     20%
consequence   25%
confidence    20%
actionability 10%
```

Display on a 0–100 scale with every component and explanation visible.

Controls:

- unknown consequence scores 1;
- proxy consequence cannot exceed 3;
- confidence below 3 defaults to `collect_more_data`;
- no reachable owner prevents default `test_next`;
- deterministic ties resolve by confidence then finding ID;
- the score orders review but never authorizes action.

The weights are a hypothesis. They become retained V1 defaults only after Chris
hand-calculates sample scores, reviews their ordering, and records the first tuning
result.

## 11. Decision Packet Contract

One future run folder contains:

```text
manifest_snapshot.json
run_metadata.json
validation_report.json
normalized_records.csv
findings.json
findings.csv
decision_packet.md
human_review.json
```

The packet must show:

1. Decision question.
2. Publisher, source, retrieval date, scope, and checksum.
3. Validation verdict.
4. Limitations and claim ceiling.
5. Ranked findings with calculations.
6. Decision anatomy: input, uncertainty, judgment, proposed action, expected
   outcome, feedback.
7. Recommendation Ladder reasoning.
8. Smallest test and stop rule.
9. Chris review table.
10. Canonical Return Packet.

Generated analysis and human review remain separate. Reruns may not overwrite
Chris's decisions.

## 12. Test Specification

### Contract tests

- Reject incomplete or contradictory manifests.
- Reject duplicate field mappings and IDs.
- Reject measured-value claims lacking calculations.
- Prove source files are unchanged.

### Normalization tests

- Valid dates normalize consistently.
- Invalid dates remain visible and flagged.
- Original malformed states remain traceable.
- Null optional fields do not crash analysis.
- Identical inputs yield identical record IDs and ordering.

### Rule tests

For each rule:

- one normal case;
- one threshold boundary;
- one definite exception;
- one missing-data case;
- one disconfirming/false-positive case.

### Scoring tests

- Hand-calculated normal case matches.
- Unknown and proxy consequence caps hold.
- Confidence and owner controls change the proposed disposition.
- Ties resolve deterministically.
- Score changes identify the contributing component.

### Human-review tests

- Every approved disposition is accepted.
- Invalid dispositions are rejected.
- Rank and reason are required.
- Applicable review/check date is required.
- Rerun preserves review for unchanged stable finding IDs.
- Changed findings require re-review.

### End-to-end KSU acceptance

- SQLite opens read-only.
- Malformed `pending\` is flagged, not corrected.
- Due-state logic is traceable.
- Source checksum is unchanged.
- Packet labels the data as sample/fixture evidence.
- No learner-mastery or market-value claim appears.

### End-to-end NYC acceptance

- Saved bounded snapshot runs offline.
- Row count and query provenance reconcile.
- Core engine contains no NYC-specific field names.
- At least one calculation is traceable to source cases.
- Volume is not mislabeled as failure.
- Unknown economic consequence remains explicit.
- A second compatible 311 fixture loads through manifest mapping only.

### Determinism test

Same input checksum + manifest + adapter/rule versions + `as_of_date` must produce
analytically equivalent validation and findings. Run timestamps may differ; the
substantive output may not.

### Failure/recovery test

Corrupt one copied fixture field or mapping, prove a clear failure at the correct
boundary, restore the copy, and prove a passing rerun. Never corrupt the live
source.

## 13. Deferred Interfaces

Explicitly outside V1:

- AI-generated ranking;
- unstructured document extraction;
- dashboards;
- scheduling;
- notifications;
- write-back to source systems;
- client authentication/permissions;
- deployment;
- automatic implementation.

A future AI scorer must operate as an optional challenger beside the deterministic
baseline. It requires a fixed evaluation set, disagreement review, cost/privacy
record, and rollback to deterministic-only mode.

## 14. First Future Implementation Slice

When Chris unlocks implementation, the smallest permitted slice is:

1. Manifest contract.
2. Normalized record contract.
3. Tiny synthetic in-memory fixture.
4. Validation gate.
5. Deterministic tests for those contracts.

It excludes KSU, NYC, scoring, reporting, and API work until the interface slice
passes. The first stop/review occurs before any real-source adapter is written.

## Gate B Acceptance

Gate B is ready for Chris's review when:

- every input/output boundary is named;
- KSU and NYC claim ceilings are preserved;
- tests can disprove the important claims;
- portability does not require premature framework building;
- no code is needed to understand the future behavior;
- the first implementation slice is independently stoppable.

**Current verdict:** RESEARCH-ONLY · IMPLEMENTATION LOCKED.
