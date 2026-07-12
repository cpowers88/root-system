---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/data-workflow, use-case/ksu-support, subject/mrp, subject/inventory-control, subject/factory-physics]
---

# MRP Mechanics: Netting, Lot Sizing, Time Phasing, and BOM Explosion

**Summary**: The actual four-step algorithm every MRP system runs — netting demand against on-hand inventory and scheduled receipts, sizing the resulting net requirements into production lots, offsetting due dates by lead time to get start times, and exploding the bill of materials to push requirements down to the next level — worked through a multi-level example by hand.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), sections 3.1.2-3.1.4

**Last updated**: 2026-06-21

---

## Inputs: What MRP Needs to Run

MRP draws from three data sources for each part: the **master production schedule (MPS)** — quantities and due dates for all independent-demand items (end items plus any components with their own external demand, such as spares); the **item master file** — bill-of-material data, the lot-sizing rule, and the planning lead time for every part; and the **inventory status file** — current **on-hand inventory** and **scheduled receipts** (purchase orders or manufacturing jobs already released but not yet completed).

Every part is tagged with a **low-level code (LLC)**: the lowest level at which that part is ever used in any bill of material. End items have LLC 0; a part used only by an LLC-1 subassembly gets LLC 1, and so on. **Processing parts strictly in LLC order (lowest first) guarantees all demand for a part has accumulated before that part is processed** — otherwise a part could be scheduled in several small, badly-timed lots instead of one efficient batch, losing the setup-cost economies of scale that lot sizing exists to capture.

## The Four Steps

For each part, defined per period t: D_t (gross requirements), S_t (scheduled receipt quantity), I_t (projected on-hand inventory), N_t (net requirements):

**1. Netting (coverage analysis)** — compute projected on-hand inventory period by period: I_t = I_(t-1) − D_t + S_t, starting from current on-hand. Net requirement N_t is whatever demand isn't covered: N_t = min{max(−I_t, 0), D_t}. More sophisticated systems first try to *expedite* (move earlier) or *defer* (move later) existing scheduled receipts to cover demand before generating any new requirement at all — coverage comes first from on-hand stock, second from existing scheduled receipts (regardless of their current due date), and only last from a brand-new planned order. Adjusting an SR's due date this way is exactly what triggers a **change notice**.

**2. Lot sizing** — net requirements must be grouped into production lot sizes. Because MRP assumes demand is deterministic but varying period to period, this is *exactly* the [[wagner-whitin-dynamic-lot-sizing]] problem from Chapter 2, and Wagner-Whitin is one legitimate lot-sizing rule MRP systems can use. Two much simpler rules are common in practice: **lot-for-lot** (produce exactly the net requirement each period — no batching at all, consistent with JIT's make-only-what's-needed philosophy) and **fixed order period (FOP)**, a.k.a. period order quantity (combine P periods' worth of net requirements into one lot; FOP with P=1 reduces to lot-for-lot).

**3. Time phasing** — subtract the **planning lead time (PLT)** from each lot's due date to get its **planned order release** date. MRP treats lead time as a fixed *attribute of the part* (sometimes of the job size, rarely of actual shop floor conditions) — this is a known simplification that causes real problems when actual cycle times deviate from the assumed PLT, discussed further in the book's Chapter 5 critique.

**4. BOM explosion** — once a part's planned order releases are set, multiply each release quantity by the bill-of-material requirement (e.g., 2 units of part 100 per unit of part A) to generate **gross requirements** for every component at the next level down. These gross requirements are added to whatever gross requirements that component has already accumulated from other parents, before that component is itself processed (which is exactly why strict LLC ordering matters).

**Iterate** these four steps level by level until every part in every bill of material has been processed. The system's outputs are **planned order releases** (the actual new jobs/purchase orders to start), **change notices** (expedite/defer instructions for existing orders), and **exception reports** (flagging discrepancies between the database and reality).

## Worked Multi-Level Example

A simplified bill of materials: part A (end item) requires 2 units of part 100 and 1 unit of part 200; part B (end item) requires units of part 300 and part 500 (LLC 1, since part 500 is only used inside B, and is itself a component of part 300... — the precise LLC chain in the source example assigns part 500 an LLC of 1, fed only by part B).

**Part A, lot-for-lot, lead time 1 week**, MPS gross requirements (weeks 1-8): 15, 20, 50, 10, 30, 30, 30, 30. With 30 on-hand and scheduled receipts of 10 (wk 1), 10 (wk 4), 100 (wk 4): netting first consumes the 30 on-hand against week 1's demand (5 left over), defers the week-1 SR of 10 into week 2 (still short, so the week-2 SR is also used), then must expedite the 100-unit week-4 SR back to week 3 to cover the week-3 demand spike of 50 — producing change notices for both adjustments. The first genuinely uncovered demand lands in week 6 (net requirement 15), with net requirements of 30 in weeks 7 and 8.

**Lot sizing** with FOP (P=2) for part A combines weeks 6-7's net demand into a 45-unit lot and leaves week 8's 30 units as its own lot (can't combine past the planning horizon). **Time phasing** (1-week lead time) sets planned order releases at week 5 (for the 45-unit lot) and week 7 (for the 30-unit lot). **BOM explosion**: each unit of A needs 2 of part 100 and 1 of part 200, so the planned releases generate gross requirements of 90 units of part 100 and 45 units of part 200 in week 5, and 60 units of part 100 and 30 units of part 200 in week 7 — which then get added to whatever gross requirements those parts already accumulated from other parents (e.g., part 100 is also required by part 500, two levels down).

**Part B (lot-for-lot, lead time 2 weeks)** is processed next since it shares part A's LLC of 0. Its planned order releases become gross requirements for part 300 in turn; part 300's releases become gross requirements for part 500 (LLC 1); and so on down the chain — each level's MRP run feeding the next level's gross requirements, in strict LLC order, until the entire bill of materials has been processed.

## Key Takeaways

- The four-step cycle (netting → lot sizing → time phasing → BOM explosion), repeated level by level in strict low-level-code order, is the entire MRP algorithm — everything else in a commercial MRP/ERP system is data management and reporting around this core loop.
- Lot sizing inside MRP is the *same* problem as [[wagner-whitin-dynamic-lot-sizing]] and [[eoq-model-and-lot-sizing]] — many real systems substitute the much simpler lot-for-lot or fixed-order-period rules instead of running full Wagner-Whitin, trading optimality for implementation simplicity.
- MRP treats lead time as a fixed property of a part, not a reflection of actual shop-floor congestion — this hard-coded assumption is a known weak point the book revisits critically in Chapter 5.
- Processing strictly in low-level-code order is not optional bookkeeping — it's what guarantees every part's full gross demand has accumulated (from all its parents) before that part's own lot-sizing and scheduling runs.
- Change notices (expedite/defer) and exception reports exist because real demand changes and real jobs run late — MRP's database is only as accurate as how diligently those changes are entered, which is a recurring real-world failure point (the database stops reflecting the actual shop floor).

## Connects to

- [[mrp-history-and-push-pull-paradigm]] — the conceptual independent/dependent-demand insight this algorithm mechanically implements.
- [[wagner-whitin-dynamic-lot-sizing]] — the lot-sizing step's underlying optimization problem; lot-for-lot and FOP are simpler heuristics for the same problem.
- [[eoq-model-and-lot-sizing]] — EOQ is also a legitimate (if cruder, constant-demand) MRP lot-sizing rule.
- [[qr-model-and-lead-time-variability]] — both this page and the (Q,r) model wrestle with lead-time uncertainty, but MRP's fixed-PLT assumption is a deliberate simplification this page flags as a known weak point.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Understanding the literal algorithm behind any client's ERP/MRP scheduling output is directly useful for diagnosing scheduling problems |
| Current usefulness | 3 | Mostly relevant once a client's MRP/ERP configuration becomes an audit subject |
| KSU support | 5 | Canonical production-control-systems algorithm, standard OM/ISYE content |
| Tech-stack relevance | 3 | The four-step logic is simple enough to prototype in Python/spreadsheet for explaining or auditing a client's MRP output |
| Business audit value | 4 | Directly explains *why* a client's MRP-generated schedule looks the way it does — useful for diagnosing scheduling complaints |
| Data/workflow value | 4 | A clean, bounded data-processing procedure — good model for building a small MRP-explainer or simulator tool |
| Reading urgency | 3 | Mid-ingest of Chapter 3, actively in progress |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / KSU support — explaining or reconstructing why a client's MRP/ERP-generated production schedule looks the way it does

**Use when**:
A client complains their MRP/ERP scheduling output doesn't make sense, or you need to verify whether their lot-sizing rule, lead-time assumptions, or low-level-code processing order are configured sensibly.

**Do not use when**:
The client has no multi-level bill of materials or doesn't use any form of computerized production scheduling — there's nothing here to audit.

**Fast retrieval query**:
`subject/mrp` + `use-case/data-workflow` — or search "netting" / "lot-for-lot" / "fixed order period" / "BOM explosion" / "low-level code"

## North Star Connection

- How this applies to the audit business: this is the literal mechanics underneath any client's ERP scheduling module — if a client's production schedule looks wrong or erratic, this page is the diagnostic checklist (wrong lot-sizing rule? stale on-hand/SR data causing bad netting? lead times that don't match real shop-floor conditions? low-level-code processing errors?) for figuring out why, rather than treating the software as an unauditable black box.
- Track relevance: Systems / KSU — strong, directly testable procedural content with a clear modern-software-audit application.
- Possible future Second Brain use: Yes — a simple Python MRP simulator (the four-step loop applied to a small bill of materials) would be a strong demonstration tool for explaining ERP scheduling logic to a client.
