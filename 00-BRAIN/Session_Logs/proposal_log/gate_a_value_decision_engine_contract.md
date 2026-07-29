---
type: contract
timeline: next
status: research-only
tags: [business, technology, value, decision-making]
created: 2026-07-29
---

# Gate A — Value Decision Engine Contract

> **RESEARCH-ONLY · IMPLEMENTATION-LOCKED**
>
> This document authorizes research and specification only. It does not authorize
> project scaffolding, code, fixtures, downloads, API calls from a local program,
> changes to the KSU tracker, or claims of Python mastery. Implementation unlocks
> only when Chris explicitly reopens the build after reviewing Gate A and Gate B.

## 1. Contract Decision

Build, later, a transparent advisory engine that converts permitted structured
operational evidence into traceable findings and proposed next tests. The engine
organizes evidence for human judgment; it does not make consequential decisions or
take action.

The engine exists to strengthen `.ROOT`'s permanent function:

```text
unfamiliar problem
→ find what costs time, money, quality, or opportunity
→ structure and validate the evidence
→ identify the decisive exception or constraint
→ recommend the smallest justified response
→ test it in real use
→ measure the result
→ harvest reusable capability
```

## 2. User and Audience

- **Primary user and decision owner:** Chris Powers.
- **V1 review audience:** Chris and the AI operator assisting with evidence
  preparation.
- **Later audience:** a workflow owner receiving a sanitized decision packet after
  the method has been tested and Chris authorizes that use.
- **Not an audience:** an autonomous agent permitted to implement recommendations.

## 3. Decision the Engine Supports

The engine supports this decision:

> Given a bounded operational dataset and a named decision question, which
> evidence-backed exception or pattern deserves Chris's attention next, what is
> still unknown, and what smallest test could determine whether real value exists?

It must distinguish:

| Term | Meaning |
|---|---|
| Observation | A source-grounded fact about a record or population |
| Finding | A calculated pattern or exception with provenance and limitations |
| Recommendation | A proposed next test or response based on a finding |
| Decision | Chris's disposition of the recommendation |
| Action | Work explicitly authorized after the decision |
| Outcome | What actually happened after authorized use |
| Learning | A rule, threshold, method, or assumption changed by the outcome |

No earlier item may be presented as a later one.

## 4. Evidence-to-Value Theory

Structured information becomes potential value only when it reduces uncertainty
around a real decision. It becomes verified value only when use produces an
observed improvement, better decision, saved time, reduced error/risk, qualified
demand, reuse, or received revenue.

The engine therefore follows this proof ladder:

1. **Calculation proof** — the result is reproducible from the cited records.
2. **Interpretation proof** — Chris agrees the finding means what the engine says.
3. **Use proof** — a permitted real workflow uses the finding.
4. **Outcome proof** — the use improves a decision or measurable condition.
5. **Demand proof** — a qualified person grants access, asks for more, or credibly
   expresses willingness to pay.
6. **Revenue proof** — payment is received.
7. **Repeatability proof** — the method works again with lower effort or stronger
   economics.

Research, a score, a report, public data, or a working program cannot independently
claim stages 3–7.

## 5. V1 Proof Environments and Claim Ceilings

### KSU Academic Tracker

Purpose: deterministic internal validation against an existing SQLite structure.

Permitted claim ceiling:

- the engine can read a database without changing it;
- detect declared data-quality and due-state exceptions;
- trace a finding to its source row;
- produce a reviewable decision packet.

Not permitted:

- calling sample records current academic truth;
- calling the tracker a business workflow;
- claiming market demand or economic value.

### NYC 311

Purpose: transfer test against foreign, official, frequently updated operational
data with identifiable cases, dates, categories, agency ownership, and resolution
information.

Permitted claim ceiling:

- the adapter works on an external operational schema;
- calculations reveal workload, aging, cycle-time, concentration, or data-quality
  patterns inside the selected sample;
- the engine clearly distinguishes evidence from missing context.

Not permitted:

- declaring an agency ineffective from volume alone;
- assuming due dates or resolution codes have meanings not established by metadata;
- converting an operational proxy into dollars;
- claiming a sellable service.

### Future Atlanta or Other Market

Purpose: test geographic relevance and adapter portability.

Entry condition: an official source with enough documentation and equivalent
operational fields to support a bounded decision question. Local relevance does not
lower the evidence standard.

## 6. Human Disposition Contract

The engine may rank attention. Chris assigns the final disposition:

| Disposition | Meaning |
|---|---|
| `test_next` | Evidence supports one bounded next test |
| `implement` | Prior test evidence supports authorized implementation |
| `collect_more_data` | A material missing fact prevents a sound test or action |
| `monitor` | Valid signal, no current action; named trigger/check date required |
| `save_for_later` | Potentially useful but displaced or phase-inappropriate |
| `reject` | Evidence, fit, economics, or risk does not justify continuation |

Every disposition records Chris's rank, reason, review date, and next check when
applicable. The engine never upgrades `test_next` to `implement`.

## 7. Decision Policy

For every finding:

1. Show the source and calculation.
2. Show missing or contradictory evidence.
3. Separate measured consequence, proxy consequence, and unknown consequence.
4. Apply the Recommendation Ladder from eliminate through custom build.
5. Recommend the cheapest rung supported by evidence.
6. State the smallest test, success signal, stop rule, owner, and review trigger.
7. Return the recommendation to Chris.

Unknown consequence remains unknown. It may lower priority or require more data; it
may not be filled with an invented estimate.

## 8. Boundaries

V1 is:

- advisory;
- deterministic for the same input, configuration, and `as_of` date;
- source-traceable;
- read-only toward input data;
- standard-library Python unless Gate B is explicitly revised;
- limited to structured CSV and SQLite inputs;
- designed for a human-reviewed Markdown/JSON/CSV decision packet.

V1 is not:

- a dashboard;
- a generative-AI ranking system;
- an autonomous agent;
- a prediction or machine-learning model;
- an unstructured-document extraction system;
- a client-data repository;
- an outreach, pricing, publishing, or implementation authority;
- a replacement for workflow observation;
- a Python learner-proof project while AI supplies its architecture or code.

## 9. Privacy, Safety, and Academic Boundaries

- No private/client data enters `.ROOT`.
- No credentials or API tokens enter the vault, reports, fixtures, or logs.
- Public sources must name publisher, source URL, retrieval date, scope, and
  limitations.
- The KSU database is opened read-only and is never treated as submitted course
  work.
- CSE restrictions remain absolute.
- External communication, spending, accounts, deployment, and commitments require
  Chris's explicit approval.
- Source datasets remain unchanged; generated outputs live separately.

## 10. Implementation Unlock

Implementation remains locked until all are true:

1. Chris approves this Gate A contract.
2. Chris approves Gate B's interfaces and acceptance tests.
3. The project is assigned a real build block that does not silently displace a
   fixed school commitment.
4. The live Python-learning boundary is stated: project code is not learner proof
   unless independently written under the owning stage's gate.
5. The exact first slice and stop condition are selected.
6. Git/worktree state is checked and unrelated work is preserved.

Unlock authorizes only the first approved slice, not the entire proposal.

## 11. Stop Conditions

Stop and return to research if:

- the decision question is absent;
- source semantics cannot support the intended calculation;
- validation falls below the Gate B threshold;
- economic consequence is necessary but unavailable;
- a simpler non-code method answers the question;
- implementation would require private data or credentials not yet authorized;
- project work displaces protected school work without Chris's explicit choice;
- a generated component is being treated as learner mastery.

## 12. `.ROOT` Return

Every meaningful run returns the canonical five fields:

1. Outcome.
2. Evidence link.
3. Capability/status movement.
4. Reusable-asset candidate.
5. System-learning candidate.

Executable work belongs in the future project boundary. Tested, sanitized,
client-facing method components may later enter
`05-BUSINESS\06-Capability Library`; research remains research until use proves it.

## Gate A Acceptance

Gate A is ready for Chris's review when he can answer:

- What decision does the engine support?
- What can KSU and NYC evidence honestly prove?
- What remains human judgment?
- What turns a finding into verified value?
- What exactly unlocks implementation?

**Current verdict:** RESEARCH-ONLY · IMPLEMENTATION LOCKED.
