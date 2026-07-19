---
type: plan
timeline: next
status: draft
tags: [governance, ai-automation, technology, business, audit]
---

# .ROOT Unified Information-System Implementation Procedure

## Purpose and Authority

This procedure translates
[[ROOT_UNIFIED_INFORMATION_SYSTEM_REDESIGN_REVIEW_2026-07-19]] into bounded,
reviewable implementation gates. The architecture report answers what and why;
this file answers how, in what order, with which tests, and where to stop.

Status is draft. Filing this procedure does not authorize Gate 1 or any later
gate. Chris approves, modifies, or rejects each structural/governance gate.

## Non-Negotiable Boundaries

- Never read or write 88-JOURNAL.
- Never modify or add content under any raw folder.
- Never delete; archive only after verifying the exact target and receiving any
  required approval.
- Do not touch unrelated user work.
- Do not push, send, publish, spend, use credentials, or create external
  repositories without explicit approval.
- C:\Users\chris\.ROOT is canonical.
- Search before creating; one concept receives one canonical home.
- Preserve a before-state and a tested rollback point before every migration
  slice.
- No gate closes because documents were generated. Chris's navigation,
  explain-back, and acceptance are required.

## Gate Discipline

Every gate follows the same procedure:

1. Confirm its input and authority.
2. Capture the before-state.
3. Perform only the bounded change.
4. Inspect the target files and Git diff.
5. Run the named deterministic checks.
6. Run the human acceptance test.
7. Record Outcome, Evidence link, Capability/status movement, Reusable-asset
   candidate, and System-learning candidate.
8. Mark keep, modify, or revert.
9. Name the next exact action.

If a required test fails, stop that gate. Do not hide the failure by refreshing
a baseline or expanding scope.

## Gate 0 — Review and Approval

### Inputs

- The two laptop conversational reports
- The architecture review
- Live .ROOT governance, interfaces, and current-state records
- Chris's corrections and desired operating experience

### Procedure

- Compare every major laptop recommendation with the live capability that
  already exists.
- Classify each recommendation as adopt, adapt, defer, or reject.
- Challenge the eight-stage flow, six logical planes, topology choice, metadata
  extension, and AI context model under all four requested hats.
- Confirm that the design makes the relationships among business, technology,
  research, learning, delivery, and system evolution clearer.
- Record any changes in the architecture report before approving Gate 1.

### Acceptance

Chris can state:

- the problem the redesign solves;
- why the design is not merely another map;
- what remains physically unchanged;
- what evidence could later justify a repository split;
- which part is ready to test first.

### Stop conditions

- A fifth competing loop is being created.
- Plane, realm, flow stage, and proof state cannot be distinguished.
- The design depends on a new paid platform or unavailable integration.
- Important laptop-report claims remain unverified or are being treated as
  governance.

### Gate result

Chris records approve, modify, or reject. Only approve opens Gate 1.

## Gate 1 — Preserve and Baseline

### Inputs

- Approved Gate 0 design
- Current root-health output
- Current Git status, branch, remote, and ignore boundaries
- Current front-door and contract files

### Procedure

- Chris creates the full D-drive pre-redesign snapshot if he wants private
  journal content included. AI does not perform or inspect that copy.
- Verify the snapshot path and date without opening prohibited content.
- Capture a local Git checkpoint for tracked safe content after reviewing the
  exact diff. Any push remains a separate approval.
- Run root health and retain its honest PASS WITH DEBT details.
- Record semantic before-state:
  - inconsistent generated or copied counts;
  - due check_at entries with blank outcomes;
  - duplicate/competing loop language;
  - broken or unclear front-door routes;
  - existing metadata debt and explicit not-evaluated scopes.
- Inventory the current cockpit, contracts, maps, Bases, Canvas files, scripts,
  and owner interfaces.

### Required artifacts

- Baseline report with date, commit, health output, semantic debt, and rollback
  pointers
- Approved exact implementation slice for Gate 2

### Validation

- python 00-BRAIN\scripts\root_health.py
- git status --short
- git diff --check
- git diff --cached --check
- Manual verification of the D-snapshot existence by Chris

### Acceptance

The old system can be restored, the protected boundaries are explicit, and no
unrelated work is included.

### Rollback

No tracked architecture content changes in this gate beyond the approved
baseline record. Revert that record by archive/replacement procedure if needed;
do not use destructive Git reset.

## Gate 2 — Information Flow Contract Prototype

### Inputs

- Approved architecture report
- Existing ROOT_CAPABILITY_CONTRACT
- Existing task protocol, knowledge-to-value pipeline, cadence, and Return Packet
- Contractor workflow artifacts from MCP_Bootcamp

### Procedure

- Draft ROOT_INFORMATION_FLOW_CONTRACT.md beside the capability contract.
- Define Intent, Capture, Trust, Structure, Understand, Decide, Act, and Learn.
- Define the six planes and distinguish them from physical realms.
- Add the translation table for:
  - every System Loop stage;
  - every task-protocol move;
  - cadence/review events;
  - every Return Packet field.
- Define the module contract and conditional metadata.
- Walk the contractor workflow through every stage.
- Record where the proposed model fails, duplicates another concept, or lacks an
  owner/return path.

### Required artifacts

- Draft Information Flow Contract
- Contractor-case trace
- Review findings and revised contract

### Deterministic validation

- Required frontmatter exists.
- All canonical links resolve.
- No competing metadata definition is introduced outside WHERE_IT_GOES.md.
- No raw or journal content is copied into the trace.

### Human acceptance

Chris explains the contractor trace without notes and distinguishes:

- realm from plane;
- System Loop stage from information state;
- task protocol from operating cadence;
- generated artifact from measured proof.

### Stop conditions

- A stage cannot be explained in general business language.
- A technical meaning cannot be assigned beneath a human stage.
- The trace requires oral history to identify state, owner, or next handoff.
- The contract requires physical movement before it can be tested.

### Rollback

Keep the prior contracts authoritative; archive the rejected draft with the
review verdict if the prototype fails.

## Gate 3 — Obsidian System-Shell Prototype

### Inputs

- Accepted Information Flow Contract
- Current START_HERE.md and ROOT_OPERATING_MANUAL.md
- Enabled core Obsidian plugins

### Procedure

- Build one native Canvas showing realms, planes, Information Flow, feedback,
  controls, and return paths.
- Build one native Base showing current work, pending review, evidence/proof
  state, and stale or overdue items from existing metadata.
- Prototype the revised START_HERE cockpit without yet rewriting every owner
  interface.
- Test five representative flows:
  1. contractor workflow;
  2. research intake;
  3. learning/proof task;
  4. system change;
  5. ordinary daily operation.

### Required artifacts

- System-map Canvas
- Control Base
- Candidate START_HERE interface
- Five test traces

### Validation

- Core plugins only; no community dependency.
- Links and embedded views resolve.
- Views do not expose ignored/private content.
- Existing canonical owners remain clear.
- Obsidian loads and navigates the interface without material delay.

### Human acceptance

For each test, Chris identifies the current state, owner, plane, next evidence,
technology job, approval boundary, and return path.

### Stop conditions

- The interface becomes a larger inventory rather than a moving system view.
- Dynamic views require mass metadata migration before they are useful.
- The cockpit duplicates canonical truth rather than pointing to it.

### Rollback

Remove the prototype from the live front-door link and retain it as an archived
design artifact. Restore the prior START_HERE from the Gate 1 checkpoint.

## Gate 4 — Install the Shared Shell

### Inputs

- Accepted Gate 3 prototype
- Approved file-impact list

### Procedure

- Promote the candidate cockpit into START_HERE.md.
- Update ROOT_OPERATING_MANUAL terminology:
  - System Loop remains the lifecycle;
  - five moves become task protocol;
  - knowledge-to-value becomes an applied pipeline;
  - daily-to-quarterly sequence becomes operating cadence.
- Cross-link ROOT_CAPABILITY_CONTRACT and ROOT_INFORMATION_FLOW_CONTRACT.
- Extend WHERE_IT_GOES.md with the three conditional flow fields and their
  exact applicability.
- Install the Canvas, Base, and module-contract template.
- Update only directly affected pointers and owner interfaces.

### Validation

- Canonical root-health gate
- Boot-chain validation
- Strict wiki-link/navigation check
- Frontmatter comparison against the reviewed baseline
- Staged and unstaged whitespace checks
- Direct inspection of every changed governance/interface file

### Human acceptance

A cold start from START_HERE answers the existing six capability-contract
questions plus the information-movement questions without a second briefing.

### Stop conditions

- Two files claim authority over the same term.
- A pointer contains copied strategy or status truth.
- Interface changes require unrelated domain-content migration.
- The health gate reports a blocker or new metadata regression.

### Rollback

Archive the failed shell with its verdict and restore the Gate 1 versions
through a reviewed patch. Re-run all validation.

## Gate 5 — Module Audit by Plane

### Inputs

- Stable shared shell
- Module-contract template
- Current realm interfaces and current-state pages

### Order

1. Direction and Control
2. Evidence and Research
3. Knowledge and Capability
4. Work and Delivery
5. Integration and Automation
6. Audit and Evolution

Within each plane, prioritize business, technology, AI Automation Systems,
CASTLE, and active project interfaces.

### Procedure per module

- Name canonical truths and accepted inputs.
- Trace output and Return Packet destination.
- Identify duplicate ownership, stale claims, missing promotion rules, and
  unclear approval boundaries.
- Add conditional flow metadata only to active flow-bearing artifacts.
- Repair generated/countable facts through generation or deterministic
  validation where practical.
- Archive superseded interfaces only after confirming all inbound links and
  installing a pointer when required.

### Acceptance

The module contract matches observed operation, and a sample input can complete
its route without oral history.

### Stop conditions

- Mass backfill becomes necessary.
- A change reaches raw, journal, client-private, or unrelated academic content.
- Plane cleanup displaces a higher fixed commitment without Chris's decision.

### Rollback

Each module is an independent slice with its own before-state and acceptance
record. Revert only that slice through reviewed patches.

## Gate 6 — AI Context Packs and Laptop Git

### Inputs

- Stable canonical shell and module contracts
- One approved ChatGPT task and one approved Claude task
- Reviewed Git ignore/privacy boundary

### Manual pilot

- Build equivalent bounded packs for ChatGPT and Claude.
- Each pack declares:
  - task and desired decision;
  - authority and approval boundary;
  - canonical source list;
  - generated-at time and freshness;
  - exclusions;
  - requested output;
  - Return Packet instructions.
- Compare the two outputs for fidelity, unsupported claims, stale-copy risk,
  disclosure safety, and correct return routing.

### Automation after the pilot

- Implement a deterministic pack generator.
- Use explicit allowlists; never recursively sweep the vault.
- Refuse journal, raw, secrets, client-private, inbox, and archive paths by
  default.
- Include source paths and freshness metadata in rendered output.
- Write rendered packs to an ephemeral/non-canonical output location.
- Promote a shared context-pack skill only after repeated manual success and a
  separate skill-governance review.

### Laptop proof

- Pull the safe repository.
- Create a named branch.
- Make one harmless tracked Markdown change.
- Commit and return the branch.
- Review diff and merge on the main PC.
- Verify ignored/private paths never appear.

### Acceptance

Both AI surfaces identify the same canonical truths and boundaries, and the
laptop round trip creates no divergent main history.

### Stop conditions

- A pack requires broad vault upload.
- A returned report becomes canonical without verification.
- Git exposes ignored/private content or creates a conflict that cannot be
  explained and recovered.

### Rollback

Discard rendered packs, archive the failed pilot record, and keep manual
main-PC operation canonical. Do not delete or force-reset branches.

## Gate 7 — Semantic Health Extension

### Inputs

- Repeated semantic failures documented in earlier gates
- Existing root_health.py orchestration

### Procedure

- Add a read-only semantic-closure check for due check_at records with blank
  outcomes/verdicts.
- Generate or validate hub counts and other machine-checkable interface facts.
- Validate flow metadata values and owner-realm identifiers where present.
- Validate context-pack manifests without reading excluded content.
- Add front-door link and interface smoke checks.
- Preserve judgment-heavy freshness and architectural coherence as named human
  review scopes.

### Validation

- New fixtures include pass, overdue-blank, invalid enum, missing owner, and
  excluded-path cases.
- Existing health tests continue to pass.
- Root health reports semantic scope separately from inherited frontmatter debt.
- No baseline refresh hides new findings.

### Acceptance

The two known semantic failure classes are detected deterministically, while
the report still names what is not evaluated.

### Rollback

Remove the new check from orchestration through a reviewed patch and retain the
failed test evidence. Do not alter the established baseline as rollback.

## Gate 8 — Stabilization and Topology Verdict

### Inputs

- Operational shell and completed acceptance tests
- Bounded observation period with real use
- Logged navigation, routing, retrieval, and context failures

### Procedure

- Run cold human and fresh-AI navigation tests.
- Review routing ambiguity, stale interface events, pack size/fidelity, Git
  friction, Obsidian performance, and module ownership.
- Classify every issue as content, interface, contract, or physical-structure
  failure.
- Attempt bounded interface repair before proposing extraction.
- Record keep, modify, or extract for each module.

### Extraction threshold

Keep the modular vault unless:

- a hard privacy/client/legal/access boundary requires separation; or
- the same structure-caused failure persists through two reviews after
  interface repair.

An extraction proposal requires Chris's explicit approval plus registry,
context/return contract, backup, migration, validation, and rollback design.

### Final acceptance

- Cold orientation succeeds.
- Contractor explain-back succeeds.
- Representative routing succeeds or visibly flags ambiguity.
- ChatGPT/Claude pack parity succeeds.
- Obsidian cockpit and native views succeed.
- Semantic checks catch known debt.
- Laptop branch round trip succeeds.
- Root health and both whitespace checks pass.
- Rollback evidence remains available.

Only then may the redesign be called operational.

## Immediate Next Action

Review the architecture report and this procedure together against both laptop
conversations. Record Gate 0 as approve, modify, or reject before performing
the preservation-and-baseline gate.
