---
type: guide
tags: [reference, business, apqc, client]
---

# 06-Capability Library — APQC-Indexed Client Asset System

## Purpose

This folder holds reusable client-facing capability assets: checklists, SOPs, workflow maps, report sections, SQL patterns, API patterns, automation patterns, and lightweight tools that can be reused across audits or client delivery.

This is not a wiki and not a source-note folder. The wikis hold learning and research. This folder holds assets that can become part of paid work.

## The Pipeline

```text
reusable idea -> draft asset -> internal test/proof -> client-ready asset
              -> client instance -> deployment feedback
```

- **Reusable idea:** a repeated method, checklist, script, query, or workflow map noticed in a wiki (`03-WIKIS\BUSINESS`, `03-WIKIS\SYSTEMS`, or any hub), a field note, an audit template, or a live project.
- **Draft asset:** the idea gets packaged here as `APQC_[process-area]_[asset-name].md` via `APQC_ASSET_TEMPLATE.md`, indexed in `CAPABILITY_LIBRARY_INDEX.md` at maturity `draft`, with a named next-action test — see Entry Rule below. Structured and indexed does not mean proven; maturity is stated honestly.
- **Internal test/proof:** the draft gets a named test — a practice audit, a tracker/POL internal run, or real field observation (see `FIRST_RUN_CHECKLIST.md` § Close the Loop) — before it can advance past `draft` to `tested internally`.
- **Client-ready asset:** once proven internally, the asset is clear enough to show or use with a prospect/client (maturity `client-ready`).
- **Client instance:** when an asset gets used with a real prospect or client, the filled/applied copy lives in the matching `05-BUSINESS` subfolder (Audit Templates output, Field Notes, Case Studies, Proposals & SOWs) — never a second copy inside this folder. This folder keeps the reusable master; client work keeps the instance.
- **Deployment feedback:** what the client instance revealed (what worked, what broke, what needed changing) updates the asset's maturity and content here, and — if the gap traces back to the source method — also updates the originating wiki page or `05-BUSINESS\01-Audit Templates\` method file it was built from. The loop closes at the source, not just in the library.

**Inbound sources:** wiki pages (BUSINESS, SYSTEMS, or any hub with a reusable pattern), `05-BUSINESS\01-Audit Templates\`, `05-BUSINESS\02-Field Notes\`, live project builds, and direct field/client observation.

**Test requirement:** every asset needs a named test before it can move past `draft` — a practice audit, a tracker/POL internal run, or real field observation (see `FIRST_RUN_CHECKLIST.md` § Close the Loop). No asset skips straight to `client-ready` without one. The named test is required to advance maturity, not to enter the folder — see Entry Rule below.

**Outbound destinations:** `05-BUSINESS` subfolders for client/practice instances; the originating wiki or method file when deployment feedback corrects the source, not just the packaged copy.

## Entry Rule

An asset belongs here only if all four are true:

1. It can be reused across more than one client or practice audit.
2. It has a business use case a nontechnical owner can understand.
3. It maps to at least one APQC process area or operating workflow.
4. It has a next action toward testing, packaging, or client use.

If it is only a note, put it in the matching wiki or library reference folder. If it is only for one client, put it in that client/project folder when one exists.

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