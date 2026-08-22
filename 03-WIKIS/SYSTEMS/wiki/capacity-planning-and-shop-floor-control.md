---
domain: systems
type: framework
tags: [subject/mrp, subject/capacity-planning, subject/factory-physics]
timeline: next
status: wiki-only
source_role: primary
use_cases: [systems-analysis, process-design, ksu-support]
---

# Capacity Planning and Shop Floor Control: RCCP, CRP, Dispatching, and I/O Control

**Summary**: How MRP II patched MRP's infinite-capacity blind spot — a quick rough-cut capacity check on the master schedule (RCCP), a more detailed but still infinite-capacity check on the resulting plan (CRP), and the short-term shop-floor control functions (job release, dispatching rules, input/output control) that govern what actually happens once a job hits the floor — including a frank accounting of why each of these tools is more limited than it sounds.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 3 ("The MRP Crusade"), sections 3.2.1-3.2.4

**Last updated**: 2026-06-21

---

## Rough-Cut Capacity Planning (RCCP)

RCCP is a fast feasibility check on the master production schedule, applied *before* full MRP processing. It uses a **bill of resources** for each end item — the hours required at each critical resource (process center) to build one unit, aggregated across the item itself and everything its bill of materials explodes into. Multiplying each period's MPS quantity by the bill of resources and summing across all items gives a predicted **load** at each resource in each period, compared against available capacity.

**Two structural biases pull RCCP in opposite directions, and the book is explicit that this makes its overall behavior hard to predict**: RCCP performs no time-offsetting (it assumes everything for a period can be completed within that period, regardless of how the work is actually sequenced or how routings stagger across time) — this makes RCCP *optimistic*. But RCCP also performs no netting against on-hand inventory/WIP, which is conservative for any item with significant existing stock or shared components — this makes RCCP *conservative*. In practice, the optimism effect usually dominates, so **RCCP tends to be an optimistic estimate, but not reliably so.**

**Worked example caution**: summing capacity requirements across an entire planning horizon can mask real period-by-period infeasibility — the book's own example shows 510 hours required against 520 hours available in aggregate (apparently fine), while the period-by-period breakdown reveals several individual weeks badly overloaded and others with slack. **Aggregate capacity sufficiency says nothing about period-by-period feasibility** — a critical distinction for any capacity check.

## Capacity Requirements Planning (CRP)

CRP runs *after* MRP and checks the resulting planned order releases (plus existing WIP) against process-center capacity, using actual routing data and lead times. Despite the name, **CRP does not perform finite capacity analysis — it performs "infinite forward loading"**: it predicts completion times for each process center using fixed lead times (regardless of how loaded that center actually is), then simply compares the resulting load profile against available capacity, with **no correction applied when the load exceeds capacity.**

**This produces a genuine internal contradiction the book highlights directly**: once a process center is shown as overloaded, every downstream prediction past that point is necessarily wrong, because real congestion *would* slow throughput — but CRP's fixed-lead-time assumption can't represent that. A worked comparison makes this vivid: CRP shows a load profile with isolated overload spikes on specific days, while a true finite-capacity model (one that actually accounts for queueing — covered in the book's Chapter 7) shows a completely different picture: two full days of *zero* output while the backlog works through the system, followed by steady output at the resource's true capacity. **CRP's reported "overload days" and a finite model's actual congestion pattern can look nothing alike.**

CRP also has three practical limitations beyond its theoretical inaccuracy: enormous data requirements, voluminous/tedious output, and — critically — **CRP only flags that a problem exists, not what caused it or what to do about it**; diagnosing the root cause requires disaggregating the load and using pegging to trace back to the originating MPS demand. Combined with the rise of true finite-capacity scheduling tools, the book notes CRP has fallen out of serious use in many organizations.

## Short-Term Control: Job Release, Dispatching, and I/O Control

Once MRP/MRP II planning generates a **job pool** of planned order releases, three short-term control functions govern execution:

- **Job release** converts planned order releases into actual scheduled receipts, and performs **allocation** — resolving conflicts when multiple planned orders compete for the same scarce component. The function allocates available stock to whichever order can actually be completed (i.e., has sufficient stock of *all* its required components), generating a shortage notice for the order(s) left without enough material rather than starting a job that will stall partway through.
- **Job dispatching** decides which job in a process center's queue runs next. No dispatching rule is universally best because, by nature, **dispatching rules are myopic** (they only see the local queue, not the shop as a whole), and true shop-wide optimal scheduling is both computationally enormous and often counterintuitive. Common rules, each with a real tradeoff:
  - **Shortest process time (SPT)** — run the shortest job next; minimizes average flow time and tends to keep average due-date performance good, but can let a single long job wait indefinitely (high variance in lateness). **SPT(x)** fixes this by forcing any job that's waited x time units to jump the queue regardless of its length.
  - **Earliest due date (EDD)** — run the job closest to its due date; works well when jobs are similar in size and routing, otherwise rarely outperforms SPT.
  - **Least slack** / **least slack per remaining operation** — prioritize by (due date − remaining process time − now), optionally normalized by operations remaining.
  - **Critical ratio** — prioritize by (time remaining)/(work remaining); a ratio below 1 means the job is already going to be late, above 1 means it has slack.
- **Input/output (I/O) control** (Wight 1970) monitors each process center's WIP level directly: if WIP rises above a target band, reduce the release rate (via the MPS); if it falls below, increase it. **The book's pointed critique**: by only reacting once WIP has *already* become excessive, I/O control is structurally reactive rather than preventive — "too little, too late" — which is one reason pull systems like kanban (which control WIP *directly* and measure output daily, rather than waiting for an after-the-fact signal) can outperform push systems like MRP/ERP in practice.

## Key Takeaways

- RCCP and CRP both inherit MRP's core infinite-capacity assumption — they check feasibility against fixed lead times rather than modeling real congestion, which makes both tools unreliable predictors once a resource is genuinely overloaded.
- Aggregate (whole-horizon) capacity sufficiency is not the same as period-by-period feasibility — RCCP's own worked example shows this directly.
- CRP only signals *that* a problem exists; finding *why* requires manual disaggregation and pegging — a real operational cost the tool doesn't advertise.
- No job-dispatching rule is universally best, because all of them are myopic by construction (local queue only, not shop-wide); SPT, EDD, least slack, and critical ratio each trade off differently between flow time, due-date variance, and computational simplicity.
- I/O control reacts to excess WIP only after it has already accumulated — a structural disadvantage relative to pull systems that control WIP directly and continuously.

## Connects to

- [[mrp-problems-nervousness-and-yield-losses]] — capacity infeasibility there is the conceptual problem; RCCP/CRP here are the (imperfect) tools built to catch it.
- [[mrp-history-and-push-pull-paradigm]] — the I/O-control-vs-kanban comparison here is a direct, concrete instance of the push-vs-pull framing established there.
- [[mrp-mechanics-netting-lot-sizing-bom-explosion]] — the job pool / planned order releases that job release and dispatching act on are the literal output of that four-step algorithm.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Useful for evaluating a client's ERP capacity-planning modules and explaining shop-floor scheduling behavior |
| Current usefulness | 2 | Mostly relevant once a client's production scheduling/capacity planning is under active diagnosis |
| KSU support | 5 | Canonical production-control-systems and scheduling-theory content |
| Tech-stack relevance | 2 | Conceptual, though dispatching rules are simple enough to prototype |
| Business audit value | 3 | The I/O-control-vs-kanban critique is a useful lens for diagnosing why a client's WIP keeps spiraling out of control before anyone notices |
| Data/workflow value | 2 | Mostly conceptual |
| Reading urgency | 3 | Completes Chapter 3's technical content |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
KSU support / ERP capacity-module evaluation — understanding what RCCP/CRP modules in a client's ERP system actually check (and don't check), and why WIP-monitoring-based controls (I/O control) tend to react too late

**Use when**:
A client's ERP system reports capacity feasibility but production keeps falling behind anyway, or a client's WIP levels seem to spiral before anyone notices a problem.

**Do not use when**:
The client has no formal capacity-planning module or production scheduling system to evaluate.

**Fast retrieval query**:
`subject/capacity-planning` + `use-case/process-design` — or search "rough-cut capacity planning" / "infinite forward loading" / "dispatching rules" / "input output control"

## North Star Connection

- How this applies to the audit business: the I/O-control-vs-kanban critique ("too little, too late") is a sharp, reusable framing for any client whose only WIP-control mechanism is reactive — useful for recommending a shift toward direct WIP limits (kanban-style) rather than after-the-fact capacity reports.
- Track relevance: Systems / KSU — solid, detailed production-control content, completes the MRP/MRP II picture begun in earlier Chapter 3 pages.
- Possible future Second Brain use: Not yet.
