---
type: guide
tags: [reference, business, apqc, client]
---

# 06-Capability Library — APQC-Indexed Client Asset System

## Purpose

This folder holds reusable client-facing capability assets: checklists, SOPs, workflow maps, report sections, SQL patterns, API patterns, automation patterns, and lightweight tools that can be reused across audits or client delivery.

This is not a wiki and not a source-note folder. The wikis hold learning and research. This folder holds assets that can become part of paid work.

Active client-specific/private work stays in a separate client workspace or
repository outside `.ROOT`; this library holds only reusable masters and
sanitized, non-sensitive learning.

## The Pipeline

```text
reusable idea -> draft asset -> internal test/proof -> client-ready asset
              -> external client instance -> sanitized deployment feedback
```

- **Reusable idea:** a repeated method, checklist, script, query, or workflow map noticed in a wiki (`03-WIKIS\BUSINESS`, `03-WIKIS\SYSTEMS`, or any hub), a field note, an audit template, or a live project.
- **Draft asset:** the idea gets packaged here as `APQC_[process-area]_[asset-name].md` via `APQC_ASSET_TEMPLATE.md`, indexed in `CAPABILITY_LIBRARY_INDEX.md` at maturity `draft`, with a named next-action test — see Entry Rule below. Structured and indexed does not mean proven; maturity is stated honestly.
- **Internal test/proof:** the draft gets a named test — a practice audit, a tracker/POL internal run, or real field observation (see `FIRST_RUN_CHECKLIST.md` § Close the Loop) — before it can advance past `draft` to `tested internally`.
- **Client-ready asset:** once proven internally, the asset is clear enough to show or use with a prospect/client (maturity `client-ready`).
- **Client instance:** when an asset gets used with a real prospect or client, the filled/applied copy lives in the authorized client workspace or repository outside `.ROOT` — never inside this folder or another `.ROOT` subfolder. This folder keeps the reusable master; the external client boundary keeps the instance.
- **Deployment feedback:** sanitized, non-sensitive learning from the client instance (what worked, what broke, what needed changing) may update the asset's maturity and content here and, when relevant, the originating wiki or `05-BUSINESS\01-Audit Templates\` method. The loop closes at the reusable source without importing client-private data.

**Inbound sources:** wiki pages (BUSINESS, SYSTEMS, or any hub with a reusable pattern), `05-BUSINESS\01-Audit Templates\`, sanitized `05-BUSINESS\02-Field Notes\`, live project builds, and approved sanitized field/client observations.

**Test requirement:** every asset needs a named test before it can move past `draft` — a practice audit, a tracker/POL internal run, or real field observation (see `FIRST_RUN_CHECKLIST.md` § Close the Loop). No asset skips straight to `client-ready` without one. The named test is required to advance maturity, not to enter the folder — see Entry Rule below.

**Outbound destinations:** separate authorized client workspaces for active client instances; `05-BUSINESS` subfolders for practice/sanitized artifacts; the originating wiki or method file when sanitized deployment feedback corrects the source.

## Entry Rule

An asset belongs here only if all four are true:

1. It can be reused across more than one client or practice audit.
2. It has a business use case a nontechnical owner can understand.
3. It maps to at least one APQC process area or operating workflow.
4. It has a next action toward testing, packaging, or client use.

If it is only a note, put it in the matching wiki or library reference folder.
If it is only for one client, put it in that client's authorized workspace or
repository outside `.ROOT`.

An asset meeting all four may enter at `idea` or `draft` maturity — proof is not a precondition of entry. It must state its maturity honestly and name its next test (see `FIRST_RUN_CHECKLIST.md`). Proof is required to advance past `draft` into `tested internally` or `client-ready`, not to be indexed here.

## Current Files

- `APQC_ASSET_TEMPLATE.md` — copy this for every new asset.
- `CAPABILITY_LIBRARY_INDEX.md` — one-line inventory of all reusable assets.
- `FIRST_RUN_CHECKLIST.md` — how to run the first asset capture without overbuilding.

## Naming

Use clear owner-facing names:

```text
APQC_[process-area]_[asset-name].md
```

Examples:

```text
APQC_4_2_WORKFLOW_OBSERVATION_MAP.md
APQC_8_6_DATA_CLEANUP_SQL_PATTERN.md
APQC_12_2_VENDOR_TOOL_DECISION_CHECKLIST.md
```

## First-Run Standard

A first-run asset does not need to be perfect. It needs to be specific, APQC-indexed, testable, and tied to the North Star service path.
