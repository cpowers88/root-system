---
type: report
tags: [reference, system, launch]
---

# Final .ROOT Launch Optimization Report — July 12, 2026

## Executive Verdict

**GO for normal supervised use. CONDITIONAL GO for autonomous file mutation.**

The architecture is sound: one universal OS, thin engine pointers, lane files, optional hats, local operating files, immutable raw sources, seven specialized wikis, and a CASTLE command center. The boot validator passes (29 boot files; 996 live pages), all 95 OpenAI captures are inventoried, and the existing July 11 cleanup/slim pass removed the major context-loading debt.

The remaining launch risk is not folder architecture. It is **permission enforcement**: `.claude/settings.local.json` is a long historical allowlist containing obsolete paths and broad execution entries, while no deterministic deny rules were found for `88-JOURNAL` or `raw`. Until that is hardened, use human review for consequential writes, moves, external actions, and agent tool calls.

## Evidence Base

- CASTLE/OpenAI corpus: 95 Markdown captures, 1,009,215 bytes, 94 unique plus one byte-identical Agents SDK duplicate.
- Semantic core reviewed: platform/models, Responses/state/streaming/background/compaction, tools/function calling/structured outputs, Agents SDK/orchestration/guardrails/observability, and agent evals.
- Live tree inventory excluding archives/raw/private journal: 1,325+ files across `00-BRAIN`, `01-NORTH_STAR`, `02-LIBRARY`, `03-WIKIS`, and `05-BUSINESS`.
- Validators: boot chain PASS; wiki lint baseline unchanged at 759 findings (198 dead wikilinks, 536 index-drift entries, 25 orphans, 0 missing frontmatter in the lint run).
- Prior reports reconciled: July 11 Codex prelive review, Claude Code launch-readiness review, and slim-pass report.
- Hard boundary honored: `88-JOURNAL` contents were not read.

## OpenAI Engineering Principles Applied

1. **Responses first; add orchestration only when needed.** A workflow should begin with the smallest deterministic flow that works. Multi-agent complexity must be justified by eval evidence.
2. **Schemas at boundaries.** Use strict function schemas and Structured Outputs between model decisions and system actions; free-form text should not flow directly into privileged tools.
3. **Least tool exposure.** Attach only the tools needed for the active task; defer rarely used tools. Tool descriptions, namespaces, and ownership boundaries are part of the control plane.
4. **Human approval at consequential actions.** Destructive, external, financial, private-data, and architecture-changing actions require an explicit approval gate.
5. **Trace before scale.** Capture model calls, tool calls, handoffs, and guardrail events; inspect traces while debugging, then promote stable failures into repeatable datasets and evals.
6. **Treat volatile product facts as volatile.** Model names, prices, limits, SDK syntax, endpoints, and deprecations must be checked live before implementation.

## Findings by Priority

### P0 — Freeze the Skeleton

No new top-level folders, governance layers, agent frameworks, or validators are justified before real usage produces measured friction. The current shape is coherent and already exceeds the minimum needed to launch.

### P1 — CLOSED: Deterministic Permission Hardening

**Original evidence:** `.claude/settings.local.json` was approximately 17 KB and contained many one-session commands and retired locations (`.AI_OS`, old library paths, temporary scratchpads), plus broad rules such as `Bash(python3 *)` and `PowerShell(git *)`. No `deny` block existed.

**Resolved risk:** advisory boundaries are now backed by permission and sandbox controls; the stale allowlist is archived.

**Implemented design:** small categorical allowlist; deterministic read/write denies for `88-JOURNAL`; write denies for every live `raw` root; approval required for consequential commands and external tools; Manual mode with auto/bypass disabled.

**Owner/result:** Chris approved; Codex applied the narrow hardening patch and validator checks.

**Acceptance checks:** JSON parses; required deny rules and all eight sandbox raw paths are present; boot validator passes. No private-content read or destructive raw-write probe was performed.

### P1 — Keep Consequential Tool Calls Human-Gated

Permission hardening now exists. Consequential actions still require human approval under the Agent Evaluation Gate: delete/archive batches, publish, email, spend, change calendars, modify credentials, or alter governance. Function schemas and structured outputs should validate proposed actions before approval.

### P2 — Classify Wiki Lint Instead of Chasing the Number

The 759 lint findings exactly match the July 11 baseline. They are not a new regression and should not block launch. Most dead links are forward-planned PHYSICS pages; most index drift is the PYTHON hub's intentionally selective index colliding with an exhaustive linter; several Python `[[...]]` hits are code-array false positives.

**Optimization:** update the linter to classify `planned`, `code false positive`, `selective-index expected`, and `true defect`. Fix only true defects during the monthly lint. Do not create hundreds of pages merely to make the count zero.

**Acceptance check:** the report prints severity/category totals and exits nonzero only for newly introduced true defects or configured blocker classes.

### P2 — Session-Log Lifecycle

`00-BRAIN/Session_Logs` contains many dated audit and execution reports plus a nested `Report Archive` of old files. This is not a boot-chain problem, but it is retrieval noise.

**Optimization:** weekly review should keep current-week reports live and archive older completed reports under the established `99-ARCHIVE/ARCHIVED_YYYY-MM-DD_...` convention. Preserve dailies/weeklies required by the review chain; do not delete.

### P3 — Cosmetic/Manual Cleanup

- `Clippings` is an empty root folder. Leave it alone unless Chris confirms the capture workflow no longer recreates it.
- The OpenAI raw pack contains one duplicate Agents SDK capture. Raw immutability applies; archive/remove only with explicit approval.
- Ambiguous raw filenames such as `OpenAI API 1.md` and `OpenAI AP15I (1).md` are compensated for by preserved source URLs and the CASTLE chunk page. Do not rename raw.

## Final Architecture Assessment

| Layer | Verdict | Reason |
|---|---|---|
| Root routing | PASS | Thin `CLAUDE.md`/`CODEX.md` pointers; boot chain resolves |
| Governance | PASS | `AGENT.md` controls; lane precedence is explicit |
| Context budget | PASS | July 11 slim pass put always-loaded files under the 200-line target except the deliberately retained North Star |
| Knowledge routing | PASS | CASTLE references specialized wikis rather than absorbing them |
| Source integrity | PASS | Raw remained immutable; large-source chunking is explicit |
| Reporting cadence | PASS WITH DISCIPLINE | DAILY/log chain exists; lifecycle cleanup must occur at reviews |
| Link/index hygiene | PASS | Classified lint: 0 blockers, 0 review debt, 714 expected items; 33 stale FORGE-era links neutralized |
| Deterministic safety | PASS | Manual mode; auto/bypass disabled; tool + sandbox denies protect private/raw boundaries; boot validator enforces drift checks |
| Agent/eval maturity | PASS — SUPERVISED BASELINE | Five-case eval gate and full-action-trace doctrine installed; multi-agent remains eval-justified only |

## Implementation Closure — July 12, 2026

Chris approved all three hardening items. The historical 17,256-byte `.claude` allowlist was archived and replaced atomically with a 1,521-byte least-privilege policy. `88-JOURNAL` now has Read/Edit/Write denies plus sandbox deny-read/write; all eight live raw roots have tool-level glob write denies and explicit sandbox deny-write paths. Manual mode is the default; auto and bypass modes are disabled.

`wiki_lint.py` now separates blockers, review debt, and expected findings. It ignores fenced/inline code examples, recognizes BUSINESS/PYTHON/PHYSICS selective indexes, recognizes planned/inactive PHYSICS material, and supports `--strict`. Final result: **0 blockers, 0 review debt, 714 expected** (135 planned PHYSICS links, 536 selective-index omissions, 25 inactive PHYSICS drafts, 18 code examples). Thirty-three inherited broken wikilinks across SYSTEMS/TECHNOLOGY were converted to accurate plain-text references.

`AGENT.md` now carries a five-rule Agent Evaluation Gate. The supervised baseline passed: normal boot/safety, selective-index edge case, private/injection boundary, raw-write boundary, and strict failure gate. This is a maturity floor, not permission to scale agents without use-case evals.

## Exact Execution Brief

### Objective

Make autonomous operation safe without changing `.ROOT` architecture.

### Scope

`.claude/settings.local.json`, existing boot validator, existing wiki linter, and report lifecycle only. No top-level restructuring, raw edits, journal reads, or doctrine changes.

### Steps

1. Claude Code reads the live settings file and drafts a minimal allow/deny replacement; Chris approves the permission categories.
2. Archive the current settings snapshot before replacement; never create a second live settings file.
3. Implement deny tests for private/raw boundaries and approval gates for consequential actions.
4. Enhance the existing wiki linter with finding classes; do not add another validator.
5. Run boot validation, JSON parsing, boundary-negative tests, and linter regression comparison.
6. Record results in DAILY, SYSTEM_FLAGS, and the next weekly review.

### Stop Conditions

Stop if Claude permission syntax cannot express the required deny semantics, a deny breaks normal read-only wiki work, a proposed edit touches `88-JOURNAL` content, or the implementation requires new governance doctrine.

## Skill and Tool Candidates

- `execution-owner: Claude Code` — permission-boundary test harness for `88-JOURNAL` and `raw`; output: tests/script; destination: `00-BRAIN/scripts/` after approval.
- `execution-owner: Claude Code` — enhance `wiki_lint.py` with planned/false-positive/true-defect classes; output: existing-script enhancement.
- `execution-owner: Claude Code` — source-pack manifest coverage and duplicate-hash validator; output: existing audit-tool enhancement or small script after repeated use proves value.

## Final Launch Rule

Launch the system by using it, not polishing it. School, technical reps, and the active proof project remain ahead of system work. Permission hardening is the only near-term system change that earns priority; everything else waits for the established weekly/monthly cadence or measured friction.
