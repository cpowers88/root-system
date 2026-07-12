---
domain: systems
type: method
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/audit, use-case/process-design, use-case/systems-analysis, use-case/client-interview, subject/value-stream-mapping, subject/lean-manufacturing, subject/pull-systems]
---

# Value Stream Mapping: Method, Map Anatomy, and the Seven Lean Guidelines

**Summary**: Value-stream mapping (VSM) — Toyota's "material and information flow diagram" — diagrams every step in the material *and* information flows needed to bring a product from order to delivery. The method: draw the **current state map** of what actually happens, then a **future state map** of how flow should work, and use the gap as the implementation blueprint. Its unique claim among mapping tools: it is the only one that shows the linkage between material flow and information flow on one page.

**Sources**: "Value Stream Mapping Overview" web clipping (lean.org lexicon, Lean Enterprise Institute, pub. 2020), captured 2026-07-08 — in `raw/`. Canonical treatment: Rother & Shook, *Learning to See* (Shingo Prize, 1999).

**Last updated**: 2026-07-08

---

## The Method

A **value stream** is all the actions — value-creating and not — required to bring a product from raw material to the customer. Mapping it:

1. **Select a product family** — one flow, not the whole plant.
2. **One person leads the mapping personally** — walking the flow, not delegating to a workshop.
3. **Map "door-to-door"** — the current state map captures the actual condition of material and information flow. The point is not a perfect drawing: "the main intention of current state mapping is going through the process of trying to understand the dock-to-dock flow."
4. **Draw the future state map** — the target flow — and treat the difference as the implementation plan.

Repeating current-state → future-state cycles is presented as the simplest way to teach yourself and others to *see* value and waste.

## Map Anatomy

Three zones: **information flow** (what tells each process what to make and when), **process boxes** (one box per area of *connected* material flow — the box ends wherever flow disconnects and material stops), and **process data boxes** underneath, carrying the standard metrics:

- **C/T** cycle time — operator's time through all work elements before repeating
- **L/T** lead time — one piece's time through the process or stream end to end
- **Uptime** — % of time the machine is available
- **C/O** changeover time — setup time to switch products
- **%C/A** — % complete and accurate (perfect quality) out of the step
- **Availability** — operating time per shift

Note the C/T-vs-L/T distinction is Little's Law territory: the gap between the sum of cycle times and the actual lead time is WIP waiting, per [[littles-law-and-best-case-performance]].

## The Seven Guidelines for a Lean Value Stream (future-state design rules)

1. **Produce to takt time** — takt = available time / demand rate; the pace proxy for customer demand.
2. **Develop continuous flow wherever possible** — one-piece flow, immediate handoff, no stagnation.
3. **Use supermarket pull where continuous flow can't extend upstream** — where batching is unavoidable, don't schedule those processes independently; link them to downstream customers via supermarket pull ([[kanban-mechanics-and-pull-system-variants]] is the mechanism).
4. **Schedule only one point** — the **pacemaker process**; everything upstream is paced by pull from it.
5. **Level the production mix at the pacemaker (heijunka)** — long single-product runs feel efficient locally but swell inventories and stretch order-to-delivery lead time for the whole stream.
6. **Level the volume: paced withdrawal at a pitch** — release and withdraw small consistent work increments (typically 5–60 minutes' worth). **Pitch = takt × pack-out quantity** (e.g. 30 s takt × 20-piece pack = 10 min pitch). This creates a predictable heartbeat, so problems surface within one pitch, not one shift.
7. **(Where flow, pull, and leveling are set)** improve the remaining process capabilities — the map shows which C/O, uptime, or %C/A number is the binding constraint.

## VSM vs. Process Mapping

A process map optimizes individual steps; a value-stream map works on the whole — "improving the whole, not just optimizing the parts." VSM's listed strengths: it visualizes flow beyond single processes, shows *sources* of waste rather than just waste, provides a common language, forces flow decisions into the open instead of letting them happen by default, forms the implementation blueprint, and uniquely links material flow to information flow.

## Standing Critique (from elsewhere in this wiki)

Factory Physics files VSM among the practitioner methods without a scientific base ([[mrp-erp-empirical-failure-and-other-scientific-approaches]]) — a mapping convention, not a theory that predicts behavior. The synthesis position: use VSM as the *communication and data-collection instrument* (its data boxes collect exactly the CT, availability, and variability inputs the VUT equation and Little's Law consume), and use factory-physics laws to *analyze* what the map records. [[fge-phantom-orders-and-sequential-debottlenecking]] shows what happens when improvement proceeds without either.

## Key Takeaways

- VSM = current state → future state → gap as implementation plan; the mapping walk itself is half the value.
- The map's one irreplaceable feature: material flow and information flow on the same page — most operational dysfunction lives in the information flow.
- Future-state design compresses to: takt, flow where you can, pull where you can't, schedule one pacemaker, level mix and volume at a pitch.
- The data boxes are a ready-made audit data-collection template; C/T vs. L/T gaps quantify waiting via Little's Law.
- Treat VSM as instrument, not theory — pair the map with factory-physics analysis of what it shows.

## Connects to

- [[kanban-mechanics-and-pull-system-variants]] — the supermarket-pull mechanism guidelines 3–4 depend on, and how to size it.
- [[jit-implementation-tactics-and-quality-revolution]] — setup reduction and cell layout are what make guideline 2's continuous flow and guideline 5's mix leveling feasible.
- [[littles-law-and-best-case-performance]] — converts a map's C/T vs. L/T gap into a WIP diagnosis.
- [[mrp-erp-empirical-failure-and-other-scientific-approaches]] — the critique that VSM lacks a scientific base; this page's method should be read with that caveat attached.
- [[factory-physics-four-step-improvement-methodology]] — the improvement method VSM's map feeds; already tagged subject/value-stream-mapping.
- [[goodbye-jit-hello-lean]] — the lean movement context VSM arrived with (*Learning to See*, 1999).
- [[process-mining-manifesto-principles-and-challenges]] — the data-driven sibling: VSM draws the flow from walking it; process mining discovers it from event logs. On a client with system data, do both and compare.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | VSM is the most client-legible artifact an operations audit can produce — one page a client can point at |
| Current usefulness | 5 | Usable on the very first client walkthrough with paper and a stopwatch; no tooling required |
| KSU support | 3 | Standard lean/IE curriculum content, but introductory-level |
| Tech-stack relevance | 3 | Map data boxes define the fields a lightweight data-collection tool would capture |
| Business audit value | 5 | Current-vs-future-state framing is a natural proposal structure: diagnosis, target, gap = engagement scope |
| Data/workflow value | 4 | The data-box metric set (C/T, L/T, C/O, uptime, %C/A) is a reusable data-request template |
| Reading urgency | 4 | Short, immediately applicable, and the critique pages that balance it are already read |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client-facing method — structuring a first operational walkthrough (current state), presenting findings (the map), and framing the engagement (future state + gap). The seven guidelines are the future-state design checklist.

**Use when**:
A client has a definable product/service family flowing through multiple steps and the presenting complaint is lead time, WIP, or "nobody can see the whole process."

**Do not use when**:
Flow is genuinely non-repetitive (true job shop, one-off projects) — the takt/pacemaker logic assumes a reasonably stable family; and never present the map as the analysis itself — pair it with Little's Law / VUT reasoning or the recommendation has no predictive basis.

**Fast retrieval query**:
`subject/value-stream-mapping` + `use-case/audit` — or search "current state map" / "pacemaker" / "takt" / "pitch" / "heijunka" / "%C/A"

## North Star Connection

- How this applies to the audit business: VSM is the audit's front door — cheap to produce, immediately understood by a non-technical owner, and structurally identical to a proposal (current state = diagnosis, future state = promise, gap = scope). Its data boxes quietly collect exactly the quantitative inputs the wiki's factory-physics pages need for the rigorous half of the engagement, and on clients with system data, a process-mining discovery of the same flow gives an evidence-based cross-check of the walked map.
- Track relevance: Business / Systems — strong; the single most directly billable method in this wiki.
- Possible future Second Brain use: Yes — a one-page VSM data-collection sheet (data-box fields per process step) is a near-term audit template candidate.
