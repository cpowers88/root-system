---
domain: systems
type: reference
tags: [subject/process-mining, subject/process-frameworks, subject/bpmn]
timeline: next
status: wiki-only
source_role: primary
use_cases: [audit, systems-analysis]
---

# BPMN 2.0.2 — The Process Modeling Standard (OMG Spec)

**Summary**: BPMN is the ISO/OMG standard notation for drawing business processes — the formal bridge between the flowcharts business people actually understand and the execution languages engines run. Its stated origin problem is the audit problem: analysts model processes as flowcharts, systems execute them as code, and the two drift. One notation with formalized execution semantics closes that gap. For this vault, BPMN matters three ways: it's the output language of process-mining tools ([[pm4py-process-mining-in-python]] discovers BPMN models from event logs), it's the professional-grade upgrade path from ad-hoc boxes-and-arrows in audit deliverables, and its token semantics are a precise vocabulary for describing where a client's process forks, waits, and breaks.

**Sources**: OMG BPMN v2.0.2 specification, 532 pp., in `raw/` as four pre-split chunks (`BPMN_1-133.pdf` … `BPMN_400-532.pdf`). Chunked ingest 2026-07-09 at two depths — modeling core read in full (~100 pp.: Overview, Activities, Events, Gateways, Lanes, all of Execution Semantics, glossary), formal machinery classified for lookup (metamodel, Choreography, BPEL mapping, XSDs, Diagram Interchange). Coverage detail in `wiki/log.md`.

**Last updated**: 2026-07-09

---

## The Three Sub-Models (what kind of diagram am I looking at?)

1. **Process (Orchestration)** — one organization's flow, inside one Pool. Private (internal workflow; executable or documentation-level) or **public** (only the activities that touch the outside world — what BPMN 1.2 called "abstract").
2. **Collaboration** — two or more Pools with Message Flows between them. Pools may be "black boxes" (no internal detail). This is the B2B/customer-interaction view.
3. **Choreography** — the message contract *between* participants with no central controller; activities are message exchanges, not work. (Plus the **Conversation** diagram: a bird's-eye hexagon map of which parties exchange what.)

A private process **supports** its public face: outsiders see only the touchpoints, and instances of the real process must look valid against the public one. That's a precise frame for the audit interview gap between "what the SOP says" and "what actually happens."

## The Working Palette (five element categories)

- **Flow Objects** — the behavior: **Events** (circles), **Activities** (rounded rectangles), **Gateways** (diamonds).
- **Data** — Data Objects / Inputs / Outputs / Stores.
- **Connecting Objects** — **Sequence Flow** (solid arrow; order of work; never crosses a Pool boundary), **Message Flow** (dashed; between Pools only; never within one), Associations, Data Associations.
- **Swimlanes** — **Pool** = participant/organization; **Lane** = sub-partition (role, system, department — meaning is up to the modeler; nestable).
- **Artifacts** — Group, Text Annotation (documentation only; no flow effect).

**Tasks** come in typed flavors, each with a corner marker: Service (gear — automated), Send / Receive (filled/hollow envelope), **User** (human via task list), **Manual** (human, no system at all — the spec itself marks Manual and Abstract tasks *non-operational*: engines can't run them), Business Rule, Script. Markers below the shape: loop, multi-instance (∥ or ≡), compensation (rewind). Sub-Processes collapse behind a [+]; a double border = Transaction.

**Events** are a matrix of *position* (Start / Intermediate / End) × *trigger* (None, Message, Timer, Conditional, Signal, Error, Escalation, Cancel, Compensation, Link, Terminate, Multiple, Parallel Multiple) × *direction* (catch = hollow marker, throw = filled). Two audit-critical variants: **boundary events** (attached to an activity = its exception handling) and **interrupting vs non-interrupting** (solid vs dashed circle — does handling the event kill the work in progress or run alongside it?). Escalation = non-critical, flow continues; Error = critical, flow stops.

**Gateways** (the decision logic — Ch. 10.6 + 13.4, read in full):

| Gateway | Marker | Split behavior | Join behavior | Workflow pattern |
|---|---|---|---|---|
| Exclusive | X (optional) | First true condition wins; **default flow or runtime exception** | Pass-through, no sync | WCP-4/5 |
| Inclusive | O | Every true condition gets a token (1 to all) | Waits for all tokens that can still arrive | WCP-6/7 |
| Parallel | + | All paths, unconditionally | Waits for **all** incoming | WCP-2/3 |
| Complex | ✳ | Condition-driven | `activationCondition`, e.g., "3 of 5" | WCP-9/28/30/31 |
| Event-Based | pentagon in double circle | **The environment decides**: first event to fire wins the race, others withdrawn | — | WCP-16 Deferred Choice |

The Event-Based Gateway is the one non-obvious keeper: "waiting to see whether the customer replies or the 3-day timer expires" is *the* SMB follow-up pattern, and it can't be drawn honestly with an ordinary decision diamond because the *process data* doesn't decide — the outside world does.

## Token Semantics (the part that makes diagrams precise)

A **token** is the theoretical marker that flows from Start Event to End Event; every element is defined by how it consumes/produces tokens. The traps this exposes:

- **Uncontrolled flow is asymmetric**: multiple *incoming* arrows into an activity behave as an exclusive merge (each token fires the activity separately — instances multiply!); multiple *outgoing* arrows behave as a parallel split (every path gets a token). Most accidental process-diagram bugs are exactly this.
- **Exclusive/Inclusive gateways throw a runtime exception if no condition is true and no default is set** — the formal version of "the process has an unhandled case," which is an audit finding when it happens on a whiteboard too.
- Activity lifecycle (Ch. 13): Ready → Active → Completing → Completed, with Failing/Terminating/Withdrawn/Compensating branches. "Withdrawn" exists precisely for event-gateway races.
- **Compensation** runs on a "presumed abort" principle: only *completed* work gets compensated, in reverse order, using a **data snapshot from completion time**. Cancel = terminate the running + compensate the finished. This is rigorous vocabulary for "how do we undo a half-processed order."
- A process instance completes only when no tokens remain and no activity is active; **Terminate** ends everything immediately, handlers included.

## What Was Classified but Not Deep-Read (lookup reference)

Ch. 8 core metamodel (pp. 77–136), Ch. 9 Collaboration detail (137–172; teaching-level content already in Ch. 7), Ch. 10 attribute tables and Items/Data + Human Interactions detail (192–261, 275–315), Ch. 11 Choreography (345–396), Ch. 12 notation/DI summary (397–454), Ch. 14 WS-BPEL mapping (475–504), Ch. 15 XSD/XMI exchange formats (505–528). These are engine-builder and tool-vendor material; pull specific pages if a build ever needs them. The spec's own conformance tiers say the same: **Process Modeling Conformance doesn't require the execution clauses** — a modeler can use the palette honestly without the machinery.

## Key Takeaways

- The 80/20 for audit work: Pools/Lanes + typed Tasks + Start/End/boundary Events + Exclusive/Parallel/Event-Based Gateways + default flows. That subset draws essentially every SMB process truthfully — the same subset PM4Py-UCM's comparison table identifies as the workflow-pattern core shared by every process notation.
- BPMN ≠ VSM ≠ PCF, and the differences are the toolkit: **PCF names what processes exist** (inventory), **VSM measures one value stream's waste** (lean lens: times, inventories, information flow), **BPMN specifies control flow precisely** (decisions, exceptions, parallelism, message contracts). An audit uses them in roughly that order.
- BPMN deliberately excludes org charts, data models, business rules, and strategy — knowing the boundary prevents the one-diagram-for-everything failure mode.
- The interrupting/non-interrupting boundary-event distinction and the Event-Based Gateway are the two pieces of expressive power that plain flowcharts lack and real processes need (deadlines, escalations, wait-for-customer races).

## Connects to

- [[pm4py-process-mining-in-python]] — discovers BPMN models from event logs; the UCM extension's notation comparison names the shared workflow core.
- [[process-mining-manifesto-principles-and-challenges]] — mined models need a target notation; BPMN is the standard one.
- [[apqc-process-classification-framework]] — the inventory layer above; BPMN details the branches the PCF names.
- [[value-stream-mapping-method-and-lean-guidelines]] — the lean lens on the same flow; VSM finds the waste, BPMN specifies the redesign.
- [[xes-standard-for-event-logs]] — same OMG-style pattern of stable IDs + interchange format, for event data instead of models.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The professional notation for the redesign deliverables the audit business sells |
| Current usefulness | 3 | The 80/20 palette is usable in the next practice VSM/process map |
| KSU support | 3 | Adjacent to ISYE process modeling; not current coursework |
| Tech-stack relevance | 4 | PM4Py emits it; every process tool (Camunda, Signavio, Bizagi) speaks it |
| Business audit value | 5 | Precise exception/decision vocabulary + client-portable diagrams |
| Data/workflow value | 4 | Token semantics = the debugging frame for broken workflows |
| Reading urgency | 2 | Core is ingested; remainder is lookup-on-demand |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Notation and semantics reference when drawing a client process map that must be unambiguous — especially decisions, parallel work, deadlines/escalations, and cross-party message exchanges.

**Use when**:
Formalizing a process discovered by interview or mining; specifying a to-be workflow for implementation; naming precisely why a client's process stalls (token stuck at an implicit merge, unhandled default case, race with no event gateway).

**Do not use when**:
The question is waste and cycle time (that's VSM), which processes to examine (that's the PCF), or a quick conversational sketch — BPMN's rigor is overhead until the diagram must be right.

**Fast retrieval query**:
`subject/bpmn` — or search "gateway" / "token" / "boundary event" / "compensation" / "pool lane"

## North Star Connection

- How this applies to the audit business: the redesign the audit sells ("AI does first-pass work, humans handle exceptions") is *literally* a BPMN pattern — Service Tasks feeding a User Task behind an Exclusive Gateway with boundary escalations. Drawing client deliverables in the standard notation makes them portable to any implementation tool and signals professional grade.
- Track relevance: Systems — strong (formal process semantics); Business — strong (deliverable format); Python — supporting (PM4Py emits/consumes it).
- Possible future Second Brain use: Yes — a one-page "BPMN audit palette" cheat sheet (the 80/20 subset with shapes) would be a natural template for `05-BUSINESS` once the first real process map is drawn.
