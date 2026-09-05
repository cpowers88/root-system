---
domain: systems
type: concept
tags: [subject/mrp, subject/manufacturing-history, subject/factory-physics]
timeline: next
status: wiki-only
source_role: primary
use_cases: [audit, systems-analysis, ksu-support]
---

# The MRP Crusade: History, the Independent/Dependent Demand Insight, and Push vs. Pull

**Summary**: Material Requirements Planning (MRP) became the dominant production-control paradigm in the US starting in the 1970s by formalizing a single key insight — components have demand that is *derived from*, not independent of, the demand for the finished products they go into — and this insight is also why MRP is classified as a "push" system, in contrast to pull systems like kanban.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), section 3.1 and 3.1.1

**Last updated**: 2026-06-21

---

## From Statistical Reorder Points to MRP

Before MRP, most production control systems used some variant of statistical reorder points (see [[statistical-inventory-models-newsvendor-base-stock]] and [[qr-model-and-lead-time-variability]]): production of any part — finished product or component — was triggered when its inventory fell below a specified level. Joseph Orlicky and others at IBM developed MRP in the early 1960s as digital computers became available for scheduling and inventory control beyond basic accounting. MRP got a major adoption boost in 1972 when the American Production and Inventory Control Society (APICS) launched an actual marketing campaign — the "MRP Crusade" — to promote it. By 1989 MRP software and implementation support exceeded $1 billion in sales; by 2005 the broader software family it anchors (MRP II, ERP, SCM) represented a $24 billion+ industry. **Every later computerized manufacturing-management approach — MRP II, business resource planning, ERP, and supply chain management — has MRP's original logic at its core**, which is why the book argues every manufacturing manager needs real familiarity with how it works (and doesn't).

## The Key Insight: Independent vs. Dependent Demand

Statistical reorder point systems treat demand for every part — finished product or raw component — the same way: as an independently arriving, uncertain quantity. **MRP's foundational insight is that this is wrong for the majority of parts in a typical bill of material.** Demand for a finished product is **independent demand** — it originates outside the production system entirely, from the market, and is genuinely uncertain. But demand for the components that make up that finished product is **dependent demand** — once you know the production schedule for the finished product (and the bill of materials), component demand is *known*, not uncertain, because it's mechanically derived from the parent schedule.

Treating dependent demand as if it were independent — applying a statistical reorder-point trigger to a component whose actual demand could be computed exactly from the parent schedule — ignores real information and produces inefficient scheduling. **MRP's core mechanism is working backward from a production schedule for independent-demand (end) items to mechanically derive schedules for dependent-demand (component) items**, explicitly preserving the link between the two that a reorder-point system discards.

## Push vs. Pull

Because MRP computes what *should* be started into production based on a forecast/schedule of demand, and then pushes those jobs into the system accordingly, it is classified as a **push system**. This stands in direct contrast to **pull systems**, most famously Toyota's **kanban**, which authorize new production only as existing inventory is actually consumed — production is pulled by real consumption rather than pushed by a computed schedule. This push/pull distinction is one of the most consequential framings in the whole book; kanban and pull systems are covered in depth in the book's Chapter 4, with a fuller push-vs-pull comparison in Chapter 10.

## Key Takeaways

- MRP's single most important conceptual contribution is distinguishing independent demand (uncertain, market-driven, applies to end items) from dependent demand (known, mechanically derivable from a parent's schedule and the bill of materials, applies to most components) — and explicitly preserving that linkage in scheduling.
- A statistical reorder-point system applied uniformly across both end items and their components throws away real, knowable information about component demand — this is the specific inefficiency MRP was built to fix.
- MRP is a push system (schedules computed and pushed into production); kanban-style pull systems are the structural alternative, authorizing production only from actual consumption. This single distinction underlies most modern arguments about lean/JIT vs. ERP/MRP-driven scheduling.
- MRP's $24B+ software descendants (ERP, SCM) all still run on this same 1960s core logic — auditing or evaluating any client's ERP system means, underneath the modern interface, evaluating an MRP engine.

## Connects to

- [[statistical-inventory-models-newsvendor-base-stock]] and [[qr-model-and-lead-time-variability]] — the statistical reorder-point methods MRP was explicitly built to improve on for dependent-demand items.
- [[mrp-mechanics-netting-lot-sizing-bom-explosion]] — the concrete algorithm (netting, lot sizing, time phasing, BOM explosion) that implements the independent/dependent demand insight described here.
- [[wagner-whitin-dynamic-lot-sizing]] — the lot-sizing logic inside MRP's "lot sizing" step is the same problem Wagner-Whitin solves exactly.
- [[manufacturing-peak-decline-resurgence]] — MRP/ERP/SCM is named explicitly there as the "integration" trend running alongside lean's "efficiency" trend and Six Sigma's "quality" trend.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Any client using an ERP/MRP system is running this exact logic underneath a modern UI — essential background for evaluating it |
| Current usefulness | 3 | Conceptual grounding more than an immediately deployable tool |
| KSU support | 5 | Canonical production-control-systems history, standard in any OM/ISYE sequence |
| Tech-stack relevance | 3 | Directly relevant to evaluating `stack/industry-platforms` (ERP/MRP software) for any client |
| Business audit value | 4 | The independent/dependent demand distinction is a sharp diagnostic for whether a client's scheduling approach (whatever software they use) actually fits their situation |
| Data/workflow value | 2 | Conceptual, not a data-handling technique itself |
| Reading urgency | 3 | Mid-ingest of Chapter 3, actively in progress |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / ERP evaluation background — understanding what a client's MRP/ERP system is actually computing underneath its interface, and whether push (MRP-style) or pull (kanban-style) scheduling logic actually fits their operation

**Use when**:
A client uses (or is considering) an MRP/ERP/SCM system, or when diagnosing whether a client's actual production-control approach (formal or informal) correctly distinguishes genuinely uncertain end-item demand from mechanically-derivable component demand.

**Do not use when**:
The client has no multi-level bill of materials (i.e., sells single, non-assembled items) — the independent/dependent demand distinction doesn't apply.

**Fast retrieval query**:
`subject/mrp` + `use-case/systems-analysis` — or search "independent demand" / "dependent demand" / "push system" / "MRP Crusade"

## North Star Connection

- How this applies to the audit business: any client running an ERP or MRP-based scheduling system is running a 1960s-era algorithm with a modern interface — understanding the independent/dependent demand distinction lets Chris evaluate whether that system's configuration actually fits the client's bill-of-material structure, rather than treating the software as a black box. The push/pull framing is also a fast lens for diagnosing scheduling problems: is this client's production literally being pushed by a forecast that's wrong, when a pull mechanism would self-correct?
- Track relevance: Business / Systems / KSU — strong across all three, this is foundational production-control history with a direct modern-software-evaluation use.
- Possible future Second Brain use: Not yet — useful background for whenever an ERP/MRP-configuration audit becomes an active engagement.
