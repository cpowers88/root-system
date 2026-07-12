---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/systems-analysis, use-case/data-workflow, subject/process-mining, subject/event-logs, subject/data-quality]
---

# Process Mining Manifesto: Discovery, Conformance, Enhancement — Principles and Challenges

**Summary**: The founding document of process mining as a discipline (IEEE Task Force on Process Mining, 2011) — what process mining is (extracting knowledge about *real* processes, not assumed ones, from event logs), its three basic types (discovery, conformance checking, enhancement), the event-log maturity ladder, six guiding principles for doing it right, and eleven open challenges. The single most audit-relevant idea: a process model discovered from a client's actual system data is evidence, where an interview-drawn process map is testimony.

**Sources**: IEEE-Process-Mining-Manifesto-2011.pdf (IEEE Task Force on Process Mining; originally published in *Business Process Management Workshops 2011*, LNBIP Vol. 99, Springer). Van der Aalst et al.

**Last updated**: 2026-07-08

---

## What Process Mining Is

Process mining sits between data mining/computational intelligence on one side and process modeling/analysis (BPM) on the other. The starting point is always an **event log**: a collection of recorded events where each event refers to an **activity** (a well-defined process step) and a **case** (a process instance — a customer order, an insurance claim, a job traveling through a shop). Events may carry extra attributes — timestamp, resource (who or what did it), and data elements (order size, product type).

The point is to discover, monitor, and improve **real** processes — not assumed processes. This is the discipline's core polemic: most organizations' process documentation describes what managers believe happens; the event log records what actually happened.

Two drivers made the field possible: (1) ever more events are recorded automatically by information systems (ERP tables, transaction logs, machine logs — events don't need a dedicated log file), and (2) competitive pressure to actually improve processes rather than re-document them. The manifesto positions process mining as the enabling technology under Six Sigma, TQM, CPI, and compliance regimes (SOX) — the thing that puts the process "under a microscope" with data instead of workshops.

## The Three Basic Types

| Type | Input | Output |
|---|---|---|
| **Discovery** | event log | a process model (Petri net, BPMN, etc.), learned with no a-priori model |
| **Conformance checking** | event log + model | diagnostics: where reality and the model diverge, and how badly |
| **Enhancement** | event log + model | an improved/extended model — e.g. timestamps replayed on the model reveal bottlenecks, waiting times, service levels |

Three misconceptions the manifesto explicitly kills: process mining is **not** limited to control-flow discovery (organizational, case, and time perspectives matter too — who does what, social networks, bottlenecks); it is **not** just a data mining subtype (concurrent process models are structurally unlike decision trees or association rules); and it is **not** offline-only (models learned from history can predict and recommend for *running* cases — detect, predict, recommend as operational support).

## Perspectives

- **Control-flow**: ordering of activities — the backbone.
- **Organizational**: which actors/roles/departments are involved and how they relate (role discovery, social network mining).
- **Case**: properties of instances themselves (which supplier, what order size).
- **Time**: timing and frequency — bottlenecks, service levels, resource utilization, remaining-time prediction.

## Event Log Maturity Levels (Table 1)

Five levels, from ★ to ★★★★★:

- **★★★★★** — excellent quality: automatic, systematic, reliable, safe recording; events and attributes have clear (ontology-backed) semantics. Example: semantically annotated logs of BPM systems.
- **★★★★** — automatic, systematic, reliable; case and activity are explicit notions. Example: workflow/BPM system logs.
- **★★★** — automatic but not systematic; trustworthy though possibly incomplete. Example: **ERP tables**, CRM logs, messaging transaction logs. (This is where most real clients live.)
- **★★** — automatic by-product, coverage varies, system can be bypassed — events may be missing. Example: document management systems, service engineers' worksheets.
- **★** — recorded by hand; events may not match reality. Example: paper trails, paper medical records.

Process mining works on ★★★ and up; ★★ is problematic; ★ is pointless. **Diagnostic implication**: assessing which level a client's data sits at is itself a fast, high-value audit finding.

## The Six Guiding Principles

1. **GP1 — Event data should be treated as first-class citizens.** Logs are usually a debugging by-product ("print statements"); quality of mining output is capped by quality of the log. Trustworthy, complete, well-defined semantics, safe (privacy addressed).
2. **GP2 — Log extraction should be driven by questions.** Without concrete questions you cannot even pick the relevant tables out of an ERP's thousands. Choosing the *case notion* is non-trivial: orders vs. order lines vs. deliveries are different processes from the same database (many-to-many relationships between them).
3. **GP3 — Concurrency, choice, and other basic control-flow constructs must be supported.** A miner that can't express AND-splits produces models that are either wildly underfitting or combinatorially unreadable (10 concurrent activities = 3,628,800 orderings).
4. **GP4 — Events should be related to model elements.** Conformance and enhancement both depend on being able to *replay* the log on the model; event-to-activity ambiguity and event correlation (which events belong to the same case) must be resolved.
5. **GP5 — Models are purposeful abstractions of reality.** There is no "the map" — road maps vs. hiking maps; a manager wants a coarse cost view, an analyst wants a detailed deviation view. Borrow from cartography: size = significance, color = bottleneck, aggregate the insignificant. Directly parallels Sterman's "all models are wrong" discipline in [[descriptive-vs-prescriptive-models-and-conjecture-refutation]].
6. **GP6 — Process mining should be continuous, not one-shot.** Living models with current data projected onto them — "traffic jams" in business processes, navigation-style prediction ("arrival time" of a delayed case) — not a report that goes in a drawer.

## The Eleven Challenges (condensed)

- **C1** Finding/merging/cleaning event data — distributed sources, object-centric vs. process-centric data, missing case IDs, noise, mixed granularity, context merging.
- **C2** Complex logs with diverse characteristics — petabyte-scale (ASML wafer scanners) vs. logs too small to conclude anything; open-world assumption (absence in the log ≠ impossibility).
- **C3** Representative benchmarks — no consensus quality criteria across dozens of discovery techniques.
- **C4** **Concept drift** — the process changes *while being analyzed* (seasonal, competitive); few processes are in steady state. Detecting it requires splitting the log and comparing footprints.
- **C5** Representational bias — the target language silently limits what can be discovered; must be a conscious choice.
- **C6** Balancing **fitness, simplicity, precision, generalization** — the four competing quality dimensions. The "flower model" replays everything (perfect fitness, zero precision); an overfitted model explains only this sample. Same overfitting/underfitting logic as statistical modeling, applied to process structure.
- **C7** Cross-organizational mining — jigsaw (partners in one process) and variant (same process, many organizations, e.g. Salesforce tenants, municipalities) settings; privacy-preserving techniques needed.
- **C8** Operational support — online detect/predict/recommend.
- **C9** Combining with other analysis — notably **operations research and simulation**: mine a simulation model from history, start simulation from the *current state* — a "fast-forward button" on live data. Also visual analytics.
- **C10/C11** Usability and understandability for non-experts — tools always show *a* model, even when the data can't justify any conclusion; trustworthiness should be shown, not hidden.

## Key Takeaways

- Process mining = discovery + conformance + enhancement over event logs; discovery is only one third of it.
- An event log needs case ID + activity + ordering as the minimum; timestamp and resource unlock the time and organizational perspectives.
- The event-log maturity ladder (★–★★★★★) is a ready-made instrument for scoring a client's data before promising anything.
- Question-driven extraction (GP2) and the case-notion choice are where projects actually succeed or die — not in the mining algorithm.
- The four quality dimensions (fitness/simplicity/precision/generalization) are overfitting/underfitting logic for process models.
- Mining + simulation (C9) is the bridge back to this wiki's system-dynamics core: discovered models seeded with current state give a data-grounded "fast forward."

## Connects to

- [[xes-standard-for-event-logs]] — the interchange standard (also from the Task Force, 2010) that makes logs portable across tools; XES replaced MXML.
- [[pm4py-process-mining-in-python]] — the Python library implementing discovery/conformance/enhancement; the practical toolchain for everything this page describes.
- [[mrp-erp-empirical-failure-and-other-scientific-approaches]] — Factory Physics's critique that BPR/VSM/Six Sigma lack a scientific base; process mining is a partial answer (evidence-based process description) and a partial confirmation (a tool, not a theory of manufacturing behavior).
- [[factory-physics-four-step-improvement-methodology]] — process mining slots into the diagnosis step as the data-driven counterpart to walking the flow.
- [[descriptive-vs-prescriptive-models-and-conjecture-refutation]] — GP5's "maps, not the map" is the same modeling philosophy Sterman argues; both traditions insist models are purposeful abstractions.
- [[barriers-to-learning-and-virtual-worlds]] — C9's mined simulation models are a route to Sterman's "virtual worlds" grounded in the organization's own event data.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Process mining is the most direct data-driven version of the audit offer: discover how a client's operation actually runs from their own system data |
| Current usefulness | 4 | The maturity ladder and the three-types framing are usable in a client conversation today, before any tooling |
| KSU support | 3 | Adjacent to ISYE simulation/OR content (C9), not core curriculum |
| Tech-stack relevance | 5 | Defines exactly what the Python/pandas toolchain (PM4Py) implements |
| Business audit value | 5 | "Your documented process vs. your logged process" (conformance checking) is a compelling, defensible audit deliverable |
| Data/workflow value | 5 | Event-log requirements (case, activity, timestamp, resource) tell you precisely what to ask a client's systems for |
| Reading urgency | 4 | Short, foundational, everything else in this cluster hangs off it |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit framing and scoping — deciding whether a client's data can support process mining (maturity ladder), choosing the case notion and questions before extraction (GP2), and setting expectations about what a discovered model is and isn't (GP5, C6).

**Use when**:
A client has an ERP/CRM/ticketing/job-tracking system that records transactions, and the question is "where does work actually get stuck, and does the real flow match the documented one?"

**Do not use when**:
The client's records are ★ or ★★ (hand-kept, bypassable, incomplete) — score the log honestly first; mining a bad log produces confident-looking nonsense (C10/C11 warn that tools always render *a* model).

**Fast retrieval query**:
`subject/process-mining` + `use-case/audit` — or search "event log maturity" / "discovery conformance enhancement" / "fitness precision generalization" / "concept drift"

## North Star Connection

- How this applies to the audit business: this is arguably the most commercially direct page in the wiki — conformance checking *is* an audit, performed on system data instead of interviews. The maturity ladder gives a no-tooling-needed first deliverable ("your event data scores ★★★; here's what that limits and how to fix logging"), and the three-types framing structures a paid engagement: discover the real flow, check it against the believed flow, enhance with bottleneck timing.
- Track relevance: Systems / Business — strong on both; Python track — strong via PM4Py.
- Possible future Second Brain use: Yes — the maturity ladder and the minimum event-log schema (case, activity, timestamp, resource) belong in a client data-intake checklist.
