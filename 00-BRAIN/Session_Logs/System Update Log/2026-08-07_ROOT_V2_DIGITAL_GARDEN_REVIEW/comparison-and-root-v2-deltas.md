---
type: architecture-decision
timeline: now
status: proposed
tags: [architecture, decision, digital-garden, root-v2, economic-value]
created: 2026-08-07
---

# Digital-Garden Comparison and `.ROOT V2` Architecture Deltas

## Decision

Preserve `.ROOT` as the canonical Markdown knowledge store. Do not create a
second live vault. Design and test a shadow V2 runtime that reads the current
vault, compiles bounded context and dashboards, records append-only events, and
writes no canonical state until it passes explicit gates.

This is a proposed architecture decision, not approval to implement or migrate.

## Why six was enough for this pass

The six cases cover the major independent variables relevant to `.ROOT`:
teaching method, lifecycle breadth, minimal publishing, search-first retrieval,
incremental compilation, and implementation-born knowledge. Additional gardens
are unlikely to change the core decision until Chris defines the product and
measurement requirements. Research should now switch from breadth to challenge
and falsification.

## Evidence comparison

Scores are analyst judgments from 1 (weak) to 5 (strong), based on visible
repository evidence. They compare reusable patterns, not the creators' overall
work.

| Garden | Teaching | Retrieval | Source/view separation | Implementation proof | Economic conversion |
|---|---:|---:|---:|---:|---:|
| David Gasquez handbook | 5 | 3 | 2 | 3 | 2 |
| Lyz Blue Book | 3 | 3 | 2 | 2 | 2 |
| Maxdeviant knowledge | 2 | 2 | 3 | 1 | 1 |
| Karlicoss Exobrain | 3 | 5 | 5 | 2 | 2 |
| Jethro Kuan Braindump | 2 | 3 | 5 | 3 | 1 |
| Simon Willison TIL | 3 | 5 | 5 | 5 | 3 |

No reviewed garden closes the full loop from intent to learning, validated
implementation, measurable SMB outcome, reusable IP, and revenue. That loop is
the distinctive job of `.ROOT V2`.

## Proposed operating loop

`intent -> trusted intake -> understanding -> practice -> implementation ->`
`verification -> measured outcome -> reusable asset -> offer -> feedback`

Each transition must leave a small evidence record. AI may draft, compile, and
recommend; Chris approves consequential action and validates exceptions.

## Seven architecture deltas

### 1. One canonical knowledge store; many disposable views

Markdown and immutable evidence remain canonical. Search databases, dashboards,
AI briefings, navigation, and public/client outputs are generated. No dual live
writes.

### 2. One active-state record

Replace scattered interpretations of “now” with one machine-readable active
state. Daily pages and dashboards become views of it. A generated view may
explain state but cannot silently become a second authority.

### 3. A context compiler

Given an objective, assemble only the controlling rules, active state, relevant
knowledge, evidence, and next action. Include source paths and reasons for every
selection. Rebuild incrementally when dependencies change.

### 4. Knowledge maturity and provenance

Use one lifecycle across domains:

`captured -> understood -> tested -> proven -> packaged`

Also record source authority, confidence, recency, privacy class, and the proof
that advanced the item. “Packaged” means reusable as a checklist, skill,
template, audit method, training unit, or offer component.

### 5. A teaching transaction, not a page

For important concepts, generate a system map, plain explanation, analogy,
worked example, Chris attempt, feedback, proof, and a transfer task. Completion
requires demonstrated use, not reading or note creation.

### 6. An implementation and value ledger

For each workflow improvement, record baseline, intervention, validation,
measured outcome, exceptions, reusable method, and potential offer. Candidate
SMB measures include cycle time, error/rework rate, labor minutes, handoffs,
wait time, throughput, adoption, and dollar impact.

### 7. Generated navigation and bounded interfaces

Folders define ownership; search and compiled views define interaction. Generate
indexes where possible. Keep governance small enough to load by need, not as a
large universal boot payload.

## Candidate success gates

The phrase “100% better” should be operationalized before implementation. A
credible V2 pilot should meet all of these on a bounded workflow:

- reduce median time from intent to correct next action by at least 50%;
- reduce manually maintained active-state surfaces to one canonical record;
- reduce irrelevant boot/context material by at least 50% without missing a
  controlling instruction in tests;
- retrieve the authoritative source and provenance for at least 95% of a fixed
  question set;
- produce one verified implementation artifact from each selected learning
  unit;
- convert at least one repeated workflow improvement into a reusable client
  asset with a measurable outcome hypothesis;
- pass existing governance and health gates with no new blocker.

A true 100% improvement can only be claimed against a named baseline metric—for
example, halving time or doubling verified outputs—not as a general property.

## Rejected patterns

- copying the full vault into a new live folder before the runtime is proven;
- hand-maintaining a giant navigation tree;
- treating number of notes, links, or project ideas as value;
- mixing clips, inferred claims, and verified facts without provenance;
- making a publishing stack the operating core;
- adding cloud dependencies before a local, readable fallback works;
- allowing AI-generated state to become authoritative without validation;
- migrating while existing governance blockers remain unresolved.

## Five interview decisions required before prototyping

1. What are the three recurring activities where `.ROOT` currently costs Chris
   the most time or creates the most uncertainty? **Getting the day started, progressing the education bot, being prepared for the material we review when learning.**
2. What observable behavior proves that Chris has *understood* a concept?  **This is subjective and will need to be evaluated often, what is being used?**
3. Which first SMB workflow should be the end-to-end value-loop pilot?  I almost think we should not focus so much on which workflow just let the research take us there, so I guess WORKFLOW of business in general is a great place to start along with supply chain could be another good place, we need to build the foundation up from the roots and learn what is the most valuable thing for us to learn, then we do that. School semester is going to be our focus, but while we are focused on this we can gather technology and business material we are going to need to make top decisions when they come up.
4. Which outputs may be public, internal, private, or client-confidential?   For now the system is going to be private github repository, and live on my desktop mainly but laptop and IPAD(minimal) access will be needed, we can use google drive for this or set up a home network, I leave this choice up to you.
5. Which one baseline metric should be doubled or halved first?  I am not sure I do know I did not treat the vault correctly to start and the usability from a human perspective has suffered, I tried to fix the machine end previously hoping that would help slightly but I honestly didn't tell yall about the problems clearly I guess

## Next exact action

Run the independent Claude challenge using `claude-challenge-packet.md`. Then
record Claude's disagreements in this packet without changing the decision.
Interview Chris on the five questions. Only then write a V2 prototype ADR and
an approval-gated, read-only pilot plan.
