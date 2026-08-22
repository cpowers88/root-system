---
domain: systems
type: framework
tags: [subject/factory-physics, subject/littles-law, subject/queuing-theory, subject/throughput-wip-cycle-time]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, data-workflow, process-design, ksu-support]
---

# Little's Law and Best-Case Line Performance

**Summary**: The book's first and most fundamental Factory Physics relationship — WIP = TH × CT (Little's Law) — derived intuitively from a hand-simulation of a zero-variability production line (Penny Fab One) at increasing WIP levels, showing exactly how throughput and cycle time behave below, at, and above the critical WIP level, plus six concrete, practical real-world applications of Little's Law that make it one of the single most broadly useful tools in the entire book.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 7 ("Basic Factory Dynamics"), section 7.3.1

**Last updated**: 2026-06-21

---

## Setting Up the Experiment: Holding WIP Constant to Isolate the Relationship

Real systems make WIP and throughput vary simultaneously and confusingly (e.g., an MRP system that floods the line with work one month and starves it the next — see [[mrp-history-and-push-pull-paradigm]]), which obscures the underlying relationship between them. **To isolate the pure relationship, the book deliberately holds WIP constant**: start a line with a fixed number of jobs, and release a new job every time a finished job exits — a protocol later named **CONWIP** (constant WIP), developed fully in Chapters 10 and 14.

## Best-Case Performance: Hand-Simulating Penny Fab One at Increasing WIP

Penny Fab One (the four-station, 2-hour-per-station balanced line from [[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]], rb = 0.5 penny/hour, T0 = 8 hours, W0 = 4 pennies) is hand-simulated with **deterministic process times** (the "best possible circumstances" — absolutely regular processing, no variability at all) at successively higher WIP levels:

- **WIP = 1**: the single penny spends 2 hours at each of 4 stations in sequence — CT = 8 hours = T0; one penny exits every 8 hours, so TH = 0.125/hour = 25% of rb.
- **WIP = 2**: after an initial transient, the second penny never waits — CT stays at 8 hours, but now two pennies exit every 8 hours, so TH = 0.25/hour = 50% of rb.
- **WIP = 3**: same pattern — CT remains 8 hours, TH rises to 0.375/hour = 75% of rb.
- **WIP = 4 (= W0, the critical WIP)**: all four stations stay busy continuously once steady state is reached — CT is still exactly T0 = 8 hours (its *minimum* possible value), and TH reaches exactly rb = 0.5/hour (its *maximum* possible value) — **this dual optimum (minimum CT and maximum TH simultaneously) is only achieved at precisely the critical WIP level.**
- **WIP = 5**: with only 4 machines, a fifth penny must now queue at station 1 even in steady state — CT rises to 10 hours (8 processing + 2 queueing), but because all stations remain continuously busy, TH stays unchanged at rb = 0.5/hour. **From this point on, every additional unit of WIP purely increases cycle time with zero throughput benefit.**
- **WIP = 10**: a queue of 6 pennies persists at station 1, cycle time rises to 20 hours (12 queueing + 8 processing), TH still pinned at rb = 0.5/hour. **Each additional penny added beyond W0 increases cycle time by exactly 2 hours (one station's process time) with no further throughput gain.**

## The Critical WIP Level Is the Single Sweet Spot — In the Zero-Variability Case

**Below W0**: every additional unit of WIP buys proportionally more throughput at no cost in cycle time (CT stays pinned at T0). **Above W0**: every additional unit of WIP buys nothing but more cycle time (TH stays pinned at rb). **Only exactly at W0 does the line simultaneously achieve maximum throughput (rb) and minimum cycle time (T0)** — any less WIP loses throughput for no cycle-time benefit; any more WIP gains nothing but cycle time. **W0 = rb × T0 holds for any line** (balanced or not) — for a balanced line, W0 equals the number of machines exactly; for an unbalanced line, W0 is strictly less, since some stations are inevitably underutilized even at the ideal WIP level.

**A critical caveat the book states directly**: this clean optimum exists *only* in the zero-variability case. **Once real variability enters the picture (the subject of the rest of Chapter 7 and Chapters 8-9), the very concept of an "optimal WIP level" becomes ill-defined** — increasing WIP under variability generally increases *both* throughput (good) and cycle time (bad) simultaneously, turning WIP-setting into a genuine trade-off rather than a single identifiable sweet spot.

## Little's Law: WIP = TH × CT

**Close examination of the simulated data reveals a relationship that holds at every single WIP level tested**: WIP is always exactly equal to the product of throughput and cycle time. This is **Little's Law** (named for John D.C. Little, who supplied the mathematical proof), and the book's first formal Factory Physics relationship:

**Little's Law: WIP = TH × CT**

**Crucially, Little's Law holds for *all* production lines, not just zero-variability ones** — but as established in [[descriptive-vs-prescriptive-models-and-conjecture-refutation]], **Little's Law is not actually a law at all, but a tautology**: it can be proven mathematically for special cases (e.g., as time approaches infinity), though it doesn't hold *precisely* for any finite (i.e., real, observable) time window except under special circumstances. **The book uses it anyway, deliberately, as a conjecture and a practical approximation** — and in this approximate sense, it is *extremely* broadly applicable: it holds for a single station, an entire line, or an entire plant, as long as all three quantities are measured in mutually consistent units, and it holds over the long term even when it's imprecise moment-to-moment.

## Six Practical Applications of Little's Law

1. **Queue length / utilization calculations.** Because Little's Law applies to individual stations, it directly computes expected queue length and utilization. **Worked example (Penny Fab Two, running at the bottleneck rate of 0.4 job/hour)**: at station 1 (single machine, 2-hour process time), expected WIP = TH × CT = 0.4 × 2 = 0.8 job, implying the single machine is utilized 80% of the time. At station 3 (six machines, 10-hour process time), expected WIP = 0.4 × 10 = 4 jobs, so average utilization is 4/6 ≈ 66.7% — **exactly equal to the ratio of the bottleneck rate to station 3's own rate (0.4/0.6)**, confirming the relationship's internal consistency.
2. **Cycle time reduction.** Rearranging as CT = WIP/TH makes it immediately clear that, holding throughput constant, reducing cycle time *requires* reducing WIP — meaning **large queues are a direct, visible signal of an opportunity to reduce cycle time** (specific reduction measures covered later in Chapter 17).
3. **Indirect measurement of cycle time.** Directly measuring cycle time requires tracking every individual part's entry and exit times — often impractical. **Since WIP and throughput are routinely tracked anyway, the ratio WIP/TH is a perfectly reasonable, far easier-to-compute indirect proxy for cycle time.**
4. **Planned inventory.** When jobs are deliberately scheduled to finish *n* days ahead of their due date (a "safety lead time," common because customers in an inventory-conscious era often refuse early deliveries), Little's Law directly predicts the resulting finished-goods inventory: FGI = n × TH (TH in units/day) — a quantified, predictable consequence of any safety-lead-time policy.
5. **Inventory turns.** Recall from [[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]] that inventory turns = TH/(average inventory). If all inventory is WIP (no FGI — product ships directly off the line), turns = TH/WIP = 1/CT by Little's Law; including FGI, turns = TH/(WIP+FGI), which by Little's Law is the inverse of the total average time a job spends in the line *plus* the finished-goods crib. **Intuitively: inventory turns are simply one divided by the average residence time of inventory in the system** — a clean, general way to think about what "turns" actually measures.
6. **Multiproduct systems.** Little's Law doesn't require measuring everything in physical part-units — if many different part types each have their own WIP/CT/TH, it can be applied separately to each, **or** the whole system can be measured in dollars (TH as cost of goods sold per day, WIP in dollars), letting CT = WIP/TH compute a single *average* cycle time across an entire multiproduct mix without needing to track each product type individually.

## Key Takeaways

- The best-case (zero-variability) simulation shows a sharp, clean structure: below critical WIP (W0), more WIP buys pure throughput gain at zero cycle-time cost; above W0, more WIP buys pure cycle-time cost at zero throughput gain; exactly at W0, both are simultaneously optimized.
- This clean optimum disappears once real variability is introduced — under variability, there is no single "optimal WIP," only a genuine trade-off between more throughput and more cycle time, which the rest of Chapters 7-9 are built to formalize.
- Little's Law (WIP = TH × CT) is a tautology, not an empirical discovery — but it remains one of the most broadly useful relationships in the entire book precisely because it holds (as an approximation) for any consistently-measured system: a single station, a line, an entire plant, or an entire multiproduct dollar-denominated system.
- The six practical applications turn Little's Law into a genuinely versatile data-analysis tool: deriving queue/utilization estimates from throughput and cycle-time data alone, using WIP/TH as a cheap proxy for hard-to-measure cycle time, predicting FGI from a planned safety-lead-time policy, and reframing inventory turns as simply the inverse of average inventory residence time.

## Connects to

- [[material-information-and-pipeline-delays]] — applies Little's Law inside
  conserved delay structures and distinguishes pipeline, first-order, and
  higher-order residence-time assumptions.
- [[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]] — the bottleneck rate, raw process time, and critical WIP (W0) concepts this page's best-case simulation directly builds on and quantitatively confirms.
- [[descriptive-vs-prescriptive-models-and-conjecture-refutation]] — the tautology/conjecture-and-refutation framing this page directly applies to Little's Law, exactly as previewed there.
- [[factory-physics-formal-model-buffers-and-variability]] — the explicit statement that the clean WIP-optimum disappears under real variability is the direct quantitative confirmation of that page's "variability is the root cause of all buffering" thesis.
- [[capacity-planning-and-shop-floor-control]] and [[mrp-history-and-push-pull-paradigm]] — the CONWIP protocol (holding WIP constant by releasing one job per completion) is the formal version of the pull-system logic already introduced in those pages, now given a precise WIP-control mechanism.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Little's Law and its six applications are immediately usable, genuinely versatile audit/data-analysis tools |
| Current usefulness | 5 | The "WIP/TH as an indirect cycle-time proxy" application alone is a practical, buildable analysis for almost any client with throughput and WIP data |
| KSU support | 5 | This is the single most canonical relationship in all of queueing theory and production systems engineering |
| Tech-stack relevance | 3 | Directly implementable as a simple Python/spreadsheet calculation against real client WIP/throughput data |
| Business audit value | 5 | "Large queues signal a cycle-time-reduction opportunity" and the WIP/TH cycle-time proxy are both immediately deployable, concrete audit findings |
| Data/workflow value | 5 | Six concrete, directly computable applications from data most plants already track (WIP, throughput) |
| Reading urgency | 5 | This is the load-bearing relationship for the entire rest of Part II |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit data analysis — using Little's Law (WIP = TH × CT) against a client's existing throughput and WIP data to estimate cycle time, station-level utilization, or expected finished-goods inventory under a stated safety-lead-time policy, without needing to instrument individual job tracking

**Use when**:
A client tracks throughput and WIP but not cycle time directly (very common), or has visibly large queues at a specific station and needs a quantified argument for why that represents a cycle-time-reduction opportunity, or needs to predict the inventory impact of a proposed safety-lead-time change.

**Do not use when**:
The system has very high variability or is far from steady state (e.g., a startup ramp-up, a highly seasonal business) — Little's Law is a long-run average relationship and can be misleading applied to short, highly transient windows.

**Fast retrieval query**:
`subject/littles-law` + `priority/now` — or search "WIP equals throughput times cycle time" / "best case performance critical WIP" / "CONWIP" / "inventory turns residence time"

## North Star Connection

- How this applies to the audit business: Little's Law is probably the single most practically reusable formula in the entire Factory Physics framework for the audit business — it lets Chris estimate cycle time, station utilization, or projected FGI directly from data almost every client already has (WIP counts, throughput rates), without expensive new instrumentation. The "large queues signal a cycle-time-reduction opportunity" framing is an immediately deployable, source-backed audit finding.
- Track relevance: Business / Systems / KSU — extremely strong across all three; this is genuinely foundational, load-bearing material.
- Possible future Second Brain use: Yes — a strong, near-ready candidate for a reusable audit calculation tool/template (Python script or spreadsheet implementing the six applications against real client data).
