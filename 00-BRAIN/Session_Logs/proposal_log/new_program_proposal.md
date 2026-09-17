---
type: proposal
timeline: next
status: research-only
tags: [business, technology, value, decision-making]
created: 2026-07-29
---

  # Value Decision Engine V1 — Build and Proof Plan

  ## Summary

  Build a small, transparent, advisory Python engine that converts structured operational data into:

  validated records
  → exceptions and patterns
  → quantified findings
  → transparent priority scores
  → recommended next tests
  → Chris’s disposition
  → measured results
  → improved decision rules

  V1 will be a separate .ROOT project and will not modify the KSU Academic Tracker. It will use:

  1. The tracker database as the deterministic internal validation case.
  2. A bounded sample of the official NYC 311 dataset (https://catalog.data.gov/dataset/311-service-requests-from-2010-to-present) as
     the foreign public-data transfer test.

  3. A configurable 311 adapter contract so Atlanta or another city can be added later.
  4. Standard-library Python only: sqlite3, csv, json, urllib, hashlib, datetime, dataclasses, argparse, and unittest.
  5. Human approval for every disposition. V1 will never act on a recommendation.

  The project will live at:

  02-LIBRARY\.PROJECTS\value_decision_engine\

  The reusable, client-facing method will be harvested separately into the existing Capability Library after testing.

  ## Step-by-Step Implementation

  ### 1. Establish the project contract

  Create a concise project brief defining:

  - Purpose: turn structured operational records into traceable, reviewable decision candidates.
  - Audience: Chris first; later, an owner or workflow operator using a sanitized decision packet.
  - V1 boundary: CSV and SQLite inputs only.
  - Explicit exclusions:
      - no dashboards;
      - no automated actions;
      - no private/client data;
      - no language-model ranking;
      - no unstructured-document extraction;
      - no prediction or machine learning;
      - no modification of source databases;
      - no claim of revenue or economic value without real evidence.

  - Acceptance gates:
      - deterministic output;
      - visible calculations;
      - source provenance;
      - human disposition;
      - reproducible KSU and NYC runs;
      - one measured tuning cycle.

  Record the governing .ROOT methods as pointers, not copied doctrine:

  - System Loop and Return Packet;
  - workflow observation;
  - AI decision anatomy;
  - strategic diagnosis;
  - audit waste math;
  - Recommendation Ladder;
  - Capability Library maturity rules.

  ### 2. Create the minimum project structure

  Use a small, learnable layout:

  value_decision_engine/
  ├── README.md
  ├── value_engine.py
  ├── engine/
  │   ├── models.py
  │   ├── adapters.py
  │   ├── validation.py
  │   ├── analysis.py
  │   ├── scoring.py
  │   └── reporting.py
  ├── configs/
  │   ├── ksu_tracker.json
  │   └── nyc_311.json
  ├── data/
  │   ├── fixtures/
  │   └── snapshots/
  ├── runs/
  └── tests/
      ├── test_validation.py
      ├── test_adapters.py
      ├── test_scoring.py
      ├── test_review.py
      └── test_end_to_end.py

  Do not create a separate repository, virtual environment, dashboard, or dependency file for V1. Reconsider the project boundary only
  if it grows beyond this lightweight standard-library implementation.

  ### 3. Define the dataset manifest interface

  Every run must begin with a JSON manifest containing:

  {
    "dataset_id": "stable_identifier",
    "title": "Human-readable title",
    "publisher": "Source owner",
    "source_url": "Official provenance URL",
    "source_type": "sqlite_or_csv",
    "source_path": "Local snapshot or database",
    "adapter": "adapter_name",
    "snapshot_date": "YYYY-MM-DD",
    "as_of_date": "YYYY-MM-DD",
    "decision_question": "The decision this run supports",
    "scope": "Included records and time period",
    "exclusions": ["Known exclusions"],
    "field_map": {},
    "valid_states": [],
    "thresholds": {},
    "consequence_basis": "measured, proxy, or unknown"
  }

  Validation must reject:

  - missing required manifest fields;
  - unsupported source types;
  - nonexistent local sources;
  - duplicate field mappings;
  - invalid dates;
  - an as_of_date earlier than the source period;
  - remote sources without an official provenance URL;
  - claims of measured consequence without a named calculation field or formula.

  Each run records the manifest and SHA-256 checksum of its input. Source files are read-only from the engine’s perspective.

  ### 4. Define the normalized record contract

  Both adapters must produce the same internal record shape:

  record_id
  dataset_id
  category
  subcategory
  owner
  location_group
  channel
  opened_at
  due_at
  closed_at
  state
  value_amount
  value_unit
  source_row_number
  source_fields
  validation_flags

  Fields may be null when the source does not provide them, but absence must remain visible.

  Normalization rules:

  - preserve the original source row in source_fields;
  - convert dates to ISO-8601;
  - trim ordinary surrounding whitespace;
  - never silently correct malformed values;
  - retain the original malformed value and add a validation flag;
  - derive no financial value unless the manifest supplies a defensible basis;
  - maintain stable record IDs across repeated runs.

  ### 5. Implement source adapters

  #### KSU SQLite adapter

  Read the existing tracker database in SQLite read-only URI mode.

  Map:

  - assignments, tests, and readings into normalized records;
  - course code to owner;
  - item type to category;
  - name, chapter, or test name to subcategory;
  - due/test date to due_at;
  - status, study status, or completion flag to state.

  The adapter must detect:

  - malformed states such as the existing pending\ value;
  - overdue unresolved items;
  - missing note paths;
  - missing or incomplete course metadata;
  - duplicate logical items;
  - impossible or invalid dates.

  Label the current tracker records as sample/fixture evidence. They prove engine behavior, not current academic risk or real-world
  market value.

  #### Configurable 311 adapter

  Implement a generic 311_service_request_v1 adapter driven by field_map. NYC’s manifest will map its column names to the normalized
  contract.

  A later city can plug in through a new manifest when it provides equivalent concepts. New adapter code is required only if the source
  has materially different semantics.

  ### 6. Build the data-quality gate

  No analysis may run until validation produces a gate result.

  Validation output must include:

  - total rows received;
  - accepted rows;
  - rejected rows;
  - duplicate IDs;
  - missing required fields;
  - invalid states;
  - invalid dates;
  - reversed date sequences;
  - missing owner/category fields;
  - source checksum;
  - coverage percentage;
  - limitations.

  Gate statuses:

  - PASS: no critical defects and at least 95% usable records.
  - PASS_WITH_WARNINGS: usable records at least 80%, with limitations disclosed.
  - FAIL: below 80% usable, duplicate record IDs, unreadable source, or broken required mappings.

  A failed gate produces a validation report but no ranked recommendations.

  ### 7. Implement transparent exception rules

  V1 will support these rule families:

  1. invalid_record — required values are malformed or contradictory.
  2. overdue_open — unresolved and past a supplied due date.
  3. closed_late — resolved after its due date.
  4. aged_open — unresolved longer than the manifest’s transparent age threshold.
  5. high_cycle_time — resolution duration exceeds a documented threshold.
  6. category_concentration — one category accounts for an unusually large share of volume or backlog.
  7. owner_concentration — backlog or delay is concentrated under one owner.
  8. missing_decision_data — a decision cannot be supported because a necessary field is absent.
  9. repeated_pattern — the same exception occurs frequently enough to justify a bounded test.

  Each finding must include:

  - stable finding ID;
  - rule that produced it;
  - affected population;
  - numerator and denominator;
  - exact calculation;
  - threshold and source;
  - representative record IDs;
  - operational consequence;
  - consequence evidence status;
  - disconfirming evidence;
  - uncertainty;
  - proposed smallest test.

  ### 8. Implement transparent scoring

  Score every valid finding from 1–5 on:

  - Severity: how far the result exceeds the threshold.
  - Frequency: how much of the relevant population is affected.
  - Consequence: measured effect, defensible proxy, or unknown.
  - Confidence: completeness, sample size, consistency, and directness.
  - Actionability: whether a reachable owner and controllable response exist.

  Priority score:

  severity × 0.25
  + frequency × 0.20
  + consequence × 0.25
  + confidence × 0.20
  + actionability × 0.10

  Convert the weighted 1–5 result to a displayed 0–100 score.

  Rules:

  - Every component must show its value and explanation.
  - Unknown consequence scores 1, never an invented midpoint.
  - Proxy consequence cannot score above 3.
  - A finding with confidence below 3 defaults to collect_more_data.
  - A finding with no reachable owner cannot default to immediate testing.
  - Score breaks are resolved deterministically by confidence, then finding ID.
  - The score orders attention; it does not authorize action.

  ### 9. Apply the Recommendation Ladder

  For each finding, propose the cheapest defensible response:

  1. eliminate;
  2. simplify;
  3. use an existing tool;
  4. configure an existing/off-the-shelf tool;
  5. integrate systems;
  6. build a lightweight response;
  7. build custom software.

  The engine must explain:

  - which rung it recommends;
  - why lower rungs were rejected;
  - what evidence would justify moving lower on the ladder;
  - the smallest test;
  - the stop condition;
  - what outcome should be measured.

  If the available data cannot justify a response rung, recommend collect_more_data.

  ### 10. Produce the decision packet

  Each run creates an immutable run folder containing:

  manifest_snapshot.json
  run_metadata.json
  validation_report.json
  normalized_records.csv
  findings.json
  findings.csv
  decision_packet.md
  human_review.json

  The Markdown decision packet contains:

  1. Decision question.
  2. Source, publisher, freshness, scope, and checksum.
  3. Validation-gate result.
  4. Data limitations.
  5. Executive finding summary.
  6. Ranked findings with full score breakdowns.
  7. Decision anatomy:
      - input;
      - prediction or uncertainty;
      - human judgment;
      - proposed action;
      - expected outcome;
      - feedback measure.

  8. Recommendation Ladder result.
  9. Smallest proposed test and stop rule.
  10. Human review table.
  11. Canonical five-field Return Packet.

  ### 11. Implement Chris’s review interface

  Use these final dispositions:

  - test_next;
  - implement — allowed only when prior test evidence exists;
  - collect_more_data;
  - monitor;
  - save_for_later;
  - reject.

  The CLI review command requires:

  finding ID
  disposition
  Chris rank
  reason
  review date
  next check date when applicable

  Example interface:

  python value_engine.py review `
    --run <run_id> `
    --finding <finding_id> `
    --disposition collect_more_data `
    --rank 1 `
    --reason "Consequence is still only a proxy"

  Human decisions live in human_review.json, separate from generated findings. Re-running analysis must never overwrite them. Stable
  finding IDs allow decisions to carry forward, while changed findings are flagged for fresh review.

  ### 12. Add the tuning comparison

  Implement:

  python value_engine.py compare --baseline <run_id> --candidate <run_id>

  The comparison report must show:

  - findings added, removed, or changed;
  - score changes and their causes;
  - threshold changes;
  - disposition changes;
  - false positives identified by Chris;
  - missed findings added manually;
  - expected versus observed result when a test occurred;
  - recommended rule adjustment.

  A rule changes only after its failure is documented. Preserve prior configurations and results rather than rewriting history.

  ## Paired Build Sequence

  ### Gate A — Contract explain-back

  Before coding, Chris explains:

  - the difference between a finding, recommendation, decision, action, and outcome;
  - why unknown consequence must remain visible;
  - why a score does not authorize implementation.

  ### Gate B — Core model construction

  The agent scaffolds the interfaces and tests. Chris completes or explains selected bounded functions involving:

  - one date-normalization rule;
  - one validation rule;
  - one score calculation.

  This keeps the build connected to the active Python capability path without turning it into prohibited coursework.

  ### Gate C — KSU internal proof

  Run:

  python value_engine.py validate --manifest configs/ksu_tracker.json
  python value_engine.py run --manifest configs/ksu_tracker.json

  Acceptance:

  - database opens read-only;
  - malformed pending\ is detected without correction;
  - the overdue sample item is identified;
  - sample records are labeled non-production evidence;
  - calculations can be traced from report to source row;
  - Chris reviews and disposes every finding;
  - no tracker file or database content changes.

  ### Gate D — First tuning cycle

  Chris marks:

  - false positives;
  - missing findings;
  - unclear score explanations;
  - unhelpful recommendations;
  - any rule he would not trust.

  Update only the failed rules, rerun the same input and as_of_date, and compare results. The second result must be demonstrably clearer
  or more accurate.

  ### Gate E — NYC 311 transfer proof

  Use a fixed, bounded API snapshot rather than the full dataset:

  - official NYC Open Data source;
  - no API credential;
  - Department of Buildings records where available;
  - one fixed 90-day completed period;
  - maximum 5,000 records;
  - stable sort;
  - only fields needed by the normalized contract;
  - snapshot and query recorded in the manifest.

  Run questions:

  - Where are service requests accumulating?
  - Which categories have unusually high unresolved age or cycle time?
  - Which results are data-quality artifacts rather than operational findings?
  - What cannot be valued because economic consequence is absent?
  - What smallest operational test would the evidence justify?

  The engine must not claim NYC operational failure from volume alone. It must distinguish workload, delay, missing data, and actual
  exception evidence.

  ### Gate F — Transfer and market-readiness review

  Pass when:

  - the generic engine operates without KSU-specific logic leaking into the core;
  - the NYC adapter works through field mapping;
  - outputs are deterministic for the saved snapshot;
  - at least one finding is useful enough for Chris to disposition;
  - unknown economic value remains explicit;
  - adding another conventional 311 dataset requires a new manifest, not a core rewrite.

  Atlanta becomes the preferred next-market candidate when a sufficiently complete public dataset is confirmed. Geographic relevance
  does not justify lowering the source or schema standard.

  ## Testing and Acceptance

  ### Automated tests

  Use unittest; add no dependency.

  Cover:

  - manifest validation;
  - SQLite read-only behavior;
  - CSV parsing and field mapping;
  - null and malformed values;
  - duplicate IDs;
  - date normalization and reversed dates;
  - state normalization without silent correction;
  - each exception rule;
  - all score boundaries;
  - unknown/proxy/measured consequence caps;
  - deterministic finding IDs and ordering;
  - failed data gate suppressing recommendations;
  - human-review preservation;
  - comparison output;
  - end-to-end KSU fixture;
  - end-to-end synthetic 311 fixture.

  ### Manual acceptance

  - Trace one KSU finding from database row to final packet.
  - Hand-calculate one score and match the program.
  - Re-run the same snapshot and confirm equivalent analytical output.
  - Confirm source checksums remain unchanged.
  - Disconnect the network and rerun from the saved NYC snapshot.
  - Change one threshold in a copied configuration and confirm the comparison explains the effect.
  - Confirm no recommendation performs an external or local mutation.

  ### Completion criteria

  V1 is complete only when:

  - all automated tests pass;
  - both proof runs complete;
  - Chris can explain the core decision flow;
  - every generated conclusion shows provenance and calculation;
  - one tuning cycle is recorded;
  - the engine remains advisory;
  - no source input is modified;
  - limitations and unrun checks are disclosed.

  ## Capability-Library and .ROOT Return

  After the KSU proof:

  - Create a draft Capability Library asset for the Exception-to-Decision method.
  - Index it with maturity tested internally only after the KSU run passes.
  - Keep executable code in the project folder; the Capability Library holds the reusable owner-facing method, interface, and operating
    checklist.

  After the NYC proof:

  - Update the same asset with sanitized transfer evidence.
  - Do not mark it client-ready; public-data transfer is not client deployment.
  - Append the relevant BUSINESS and TECHNOLOGY wiki logs only where the run genuinely changed maintained knowledge.
      - SQL/data-modeling capability;
      - workflow-diagnosis capability;
      - decision-communication capability;
      - value-production evidence;
      - a current strategy assumption.

  - Do not open an outreach, pricing, product, or client lane without a separate Chris-approved gate.

  ## Assumptions and Defaults

  - The current dirty worktree belongs to Chris and will be preserved.
  - The project remains inside .ROOT because V1 is a small, dependency-free internal proof; growth into a larger application triggers a
    workspace/repository review.

  - Python 3.14 and SQLite are the runtime.
  - No packages are installed for V1.
  - KSU data is a test fixture until verified course data replaces samples.
  - NYC 311 is a transfer dataset, not proof of a sellable service.
  - The engine evaluates structured operational evidence, not arbitrary documents.
  - AI-generated ranking is deferred behind a future scorer plug-in interface and will require its own evaluations, privacy review,
    deterministic baseline comparison, and Chris approval.

  - Human judgment remains authoritative for consequence, disposition, implementation, and strategy.
