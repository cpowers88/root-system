---
type: contract
timeline: reference
tags: [north-star, governance, ai-os]
status: live
created: 2026-07-19
---

# `.ROOT` Information Flow Contract
### How information moves through the one system — the translation layer
### Installed July 19, 2026 by Chris's Gate 0 decision (interface remodel, no physical change)

## Authority and Loading Rule

`ROOT_CAPABILITY_CONTRACT.md` owns the canonical System Loop and Return Packet;
`AGENT.md` owns AI behavior; `WHERE_IT_GOES.md` owns placement and metadata.
This contract owns exactly one thing: **the single picture of how information
enters `.ROOT`, becomes trustworthy, moves, produces action, and returns
evidence — and how every existing view of the system translates into that
picture.**

This is an information-state view, not a lifecycle. It defines no new loop, no
new owner, no new folder, and no metadata fields. If any statement here appears
to compete with the System Loop, the System Loop wins and the conflict is a
HIGH flag.

Load this file when: orienting a fresh session to how the system fits together,
tracing where any single item stands, designing or auditing an interface, or
briefing an external AI surface.

## The Problem This File Ends

Before July 19, 2026, `.ROOT` exposed four correct but untranslated views:
the twelve-stage System Loop, the five-move task protocol, the
knowledge-to-value pipeline, and the daily-to-quarterly cadence. Each was
right; nothing said they were the same system. This file is the cover sheet:
one flow, with every existing view mapped onto it.

**The four views, named once:**

```text
System Loop   = the canonical lifecycle (what the whole system does)
Five moves    = the task protocol (how one work session runs)
K-to-V pipeline = the business application (how knowledge becomes assets)
Cadence       = the review rhythm (when the system looks at itself)
Flow (this)   = the information state (where one item is, what changes next)
```

## The Eight Information States

Every meaningful item in `.ROOT` — a source, a signal, a course concept, a
business observation, a build, a system change — is always in exactly one of
these states:

| # | Human state | Technical meaning |
|---|---|---|
| 1 | **Intent** | The question, desired outcome, owner, constraints, and authority are defined |
| 2 | **Capture** | The source, event, request, or observation is ingested to its owning home |
| 3 | **Trust** | Provenance, quality, freshness, and uncertainty are validated and visible |
| 4 | **Structure** | The item is modeled, classified, connected, and stored as canonical state |
| 5 | **Understand** | It is transformed, compared, analyzed; findings and capability form |
| 6 | **Decide** | It is routed, gated, recommended, approved, or rejected by its owner |
| 7 | **Act** | Something real is eliminated, built, configured, deployed, taught, or used |
| 8 | **Learn** | The measured outcome returns as evidence and the system improves |

Construction anchor: material delivery (Capture) → inspection (Trust) →
staging and layout (Structure) → shop drawings (Understand) → the go/no-go
meeting (Decide) → the build (Act) → the punch list and as-builts (Learn) —
all under one permit set (Intent).

## The One-System Translation Table

This table is the core of the contract. Every row translates one information
state into every existing view. No view may be extended without updating this
table in the same change.

| State | System Loop stage(s) | Task-protocol move | K-to-V pipeline step | Cadence event | Return Packet field it feeds |
|---|---|---|---|---|---|
| Intent | human governance entering the loop; CASTLE sets the question | ORIENT | (precedes the pipeline) | morning `NOW.md` | frames the eventual **Outcome** |
| Capture | SENSE | ORIENT → ROUTE | raw source → evidence home | sources feed hubs (daily) | — |
| Trust | RESEARCH (source tiers, verification) | ROUTE | relevance filter | weekly inbox/clippings sweep | **Evidence link** integrity |
| Structure | STRUCTURE | WORK | domain wiki update; index/log | monthly property review | **Capability/status movement** |
| Understand | RESEARCH → TEACH | WORK | wiki refinement → learner proof | daily rep | **Capability/status movement** |
| Decide | DECIDE (CASTLE, profit gate, opportunity queue) | ROUTE (owner and gate) | CASTLE opportunity decision | Sunday weekly + Engine Question | **Reusable-asset candidate** (go/no-go) |
| Act | BUILD → PROVE → DEPLOY/USE | WORK → PROVE/PACKAGE | bounded real work → draft asset → client use | daily rep; sprint sessions | **Evidence link**; **Reusable-asset candidate** |
| Learn | MEASURED OUTCOME → LEARN → REVIEW → EVOLVE | PROVE/PACKAGE → CLOSE | field evidence updates asset and wiki | night close → weekly → monthly → quarterly Ratchet | **Outcome**; **System-learning candidate** |

Reading the table down a column re-derives each existing view; reading it
across a row locates one item. That is the whole trick: four views, one
system.

## The Seven-Line Trace

To locate any single item — in a session, a handoff, a review, or an external
AI brief — answer seven lines using only existing vocabulary:

```text
1. Intent        — question/outcome, owner, authority boundary
2. Source/Trust  — where it came from; why it is trustworthy
3. State         — the file where canonical truth lives right now
4. Loop stage    — its current System Loop stage (table above)
5. Next action   — the one next transformation and its approval boundary
6. Proof         — the evidence that will count, and who accepts it
7. Return        — the exact file/owner the outcome evidence returns to
```

If any line cannot be answered from live files, that is the drift to repair —
the trace is a diagnostic, not paperwork. Use it when an item is stuck,
contested, or being handed to another surface; do not trace routine reps.

## Non-Competition Rules

1. This file defines no lifecycle. The System Loop remains the only one.
2. This file assigns no ownership. Stage owners live in the Capability
   Contract; placement lives in `WHERE_IT_GOES.md`.
3. This file adds no metadata. The proposed `flow_stage` / `system_plane` /
   `owner_realm` fields remain **deferred** and may be proposed only when a
   real, wanted query provably fails against existing metadata — the proposal
   goes through `WHERE_IT_GOES.md` and Chris's approval.
4. Plane language (Direction/Control, Evidence/Research, Knowledge/Capability,
   Work/Delivery, Integration/Automation, Audit/Evolution) is **descriptive
   vocabulary only** for audits and conversation; planes are not folders,
   owners, or required classifications.
5. Interfaces (`START_HERE.md`, Canvas, any future Base) may display this
   flow; they point to owners and never copy truth.

## Acceptance Standard

This contract is doing its job when:

- a fresh human or AI session can state, for any active item, its state, owner,
  next action, proof, and return path from live files alone;
- no session needs more than this file plus the Capability Contract to explain
  how the four views fit together;
- no new cycle, vocabulary, or metadata has appeared outside the translation
  table.

Review trigger: first weekly review after August 24, 2026, then quarterly with
the Ratchet, or immediately if any file defines a competing flow.

---
*Companion: `ROOT_CAPABILITY_CONTRACT.md` (lifecycle + Return Packet — canonical).
Behavior: `00-BRAIN\AGENT.md`. Placement/metadata: `00-BRAIN\WHERE_IT_GOES.md`.*
*Installed July 19, 2026 — Chris's Gate 0 decision: interface remodel, physical
structure unchanged, D-drive snapshot preserved by Chris before installation.*
