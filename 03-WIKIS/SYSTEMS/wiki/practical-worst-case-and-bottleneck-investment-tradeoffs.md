---
domain: systems
type: framework
tags: [subject/factory-physics, subject/queuing-theory, subject/throughput-wip-cycle-time, subject/variability]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, process-design, data-workflow, ksu-support]
---

# Practical Worst-Case Performance, and Bottleneck vs. Nonbottleneck Investment Trade-offs

**Summary**: The Practical Worst Case (PWC) — the book's "maximum randomness" benchmark, derived from a balanced single-machine line with exponentially distributed (memoryless) processing times — gives the chapter's actual real-world comparison standard for internal benchmarking: CTpwc = T0 + (w−1)/rb. Three concrete, named levers for improving a line that performs worse than the PWC (unbalancing the line, using parallel machines, reducing variability below the exponential), followed by a sharp, counterintuitive result about when investing in the bottleneck beats investing in nonbottleneck capacity — and when it doesn't.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 7 ("Basic Factory Dynamics"), sections 7.3.3-7.3.4

**Last updated**: 2026-06-21

---

## The Memoryless Property: Why the Exponential Distribution Defines "Maximum Randomness"

The practical worst case requires processing times to follow a specific continuous probability distribution — the **exponential distribution** — because of a special property called the **memoryless property** (detailed in Appendix 2A): if a machine's processing time is exponentially distributed, knowing *how long* a job has already been in process gives **zero information** about how much longer it will take. Whether a job has been in process for 5 seconds, 1 hour, or 942 hours, the *expected remaining* processing time is identical (e.g., always 1 hour, for a mean-1-hour exponential). **It's as if the machine forgets everything about its past work the moment it tries to predict the future** — hence "memoryless." (The book notes real-world analogs: delayed-flight departure times, train arrivals on certain railways, contractor job-completion times can all behave this way.) **A direct practical consequence**: because the system state needs no information about how long a job has already been processing, the state can be fully captured just by counting jobs at each station — exactly the simplified state-vector representation set up earlier in the chapter.

## Deriving Practical Worst-Case Cycle Time

**Setup**: N single-machine stations, each with average processing time t (so T0 = Nt and rb = 1/t — a balanced line), holding WIP constant at w via the pallet/CONWIP protocol from [[littles-law-and-best-case-performance]]. **Because the three PWC conditions (balanced line, single-machine stations, exponential processing times) guarantee all system states are equally likely** — the genuine "maximum randomness" case — riding along on a pallet, you'd expect to see, on average, the other w−1 jobs in the system spread evenly across the N stations: (w−1)/N jobs ahead of you at any station you arrive at.

**Average time at a station = (your own processing time) + (time for the jobs ahead of you to clear)** = t + [(w−1)/N] × t = t[1 + (w−1)/N]. **The memoryless property is exactly what allows this calculation to ignore how far along the job currently in process already is** — without memorylessness, you'd need to know each ahead-job's elapsed processing time to estimate the remaining wait, which the exponential distribution conveniently makes irrelevant. **Multiplying by N stations** (all assumed identical): CT = Nt[1 + (w−1)/N] = Nt + (w−1)t = T0 + (w−1)/rb (substituting t = 1/rb).

## The Formal Practical Worst-Case Law

**Practical Worst-Case (PWC) Performance**: for WIP level w, **CTpwc = T0 + (w−1)/rb**, and by Little's Law, **THpwc = w/[W0 + w − 1] × rb** (derived by substituting CTpwc and applying TH = WIP/CT, using W0 = rb×T0).

**Sanity checks at the extremes confirm the formula behaves sensibly**: at w=1 (a single job in the system), CTpwc reduces exactly to T0 — as expected, with no other jobs to wait behind. As w→∞, throughput approaches capacity rb while cycle time grows without bound — **the intuition**: achieving throughput close to capacity under high variability requires high WIP, specifically to ensure the bottleneck never starves for lack of work; but high WIP also guarantees a great deal of waiting, hence high cycle times. **The PWC's throughput and cycle time always fall between the best case and the worst case for any given WIP level** — making it a genuinely useful *midpoint* approximating the behavior of many real production systems.

## Internal Benchmarking: The PWC as the Dividing Line Between "Lean" and "Fat"

**By collecting just two of the three quantities (WIP, throughput, cycle time) for a real line — Little's Law supplies the third — a line's actual performance can be classified relative to the three theoretical benchmarks**: systems performing *better* than the PWC (higher throughput, lower cycle time at a given WIP level) are called **"good" (lean)**; systems performing *worse* are called **"bad" (fat)**. **This three-case framework constitutes a genuine internal benchmarking methodology** — distinct from external benchmarking (comparing against other companies' systems) — because it compares a line's actual performance against its own theoretically achievable best, worst, and "maximum randomness" cases, given only its own rb and T0. Section 7.3.5 develops the explicit internal-benchmarking procedure with a real case.

## Three Concrete Levers for Improving a "Bad" Line

If internal benchmarking shows a line performing worse than the PWC, the three assumptions the PWC was *derived* under directly suggest three improvement levers (improving any of them reduces randomness, which improves performance):

1. **Unbalance the line by adding capacity at a station.** This can mean new equipment, reduced downtime (worker breaks, equipment failures), or more efficient work methods. **Adding capacity everywhere obviously increases throughput — but even adding capacity at only some stations (so rb itself doesn't change) still reduces randomness**, because the once-equally-likely states in the system-state table are no longer equally likely, which makes the throughput-versus-WIP curve rise more steeply (less WIP needed for the same throughput). **This directly contradicts the traditional industrial-engineering emphasis on line balancing** — the book notes explicitly that line balancing is primarily relevant to *paced* assembly lines (covered later in Chapter 18), not to a line of independent workstations like those considered here.
2. **Use parallel machines instead of single machines, even with no change in total capacity.** **Worked illustration**: in Penny Fab One with exponential (not deterministic) processing times, collapsing stations 3 and 4 (rimming/deburring, each averaging 2 hours) into one combined station with two parallel machines, each averaging 4 hours per penny, keeps the station's overall capacity unchanged (1 penny/hour either way) and leaves rb and T0 both unchanged. **But in the original separate-station arrangement, two pennies arriving close together could both end up needing the same single rimming or deburring machine, forcing one to wait; in the combined parallel arrangement, any two pennies needing this combined station can both be worked on simultaneously.** The result: less waiting and shorter cycle times at any given WIP level, purely from the parallel-machine arrangement, with zero added capacity.
3. **Reduce variability below what the exponential distribution implies.** Reducing the likelihood of jobs "clumping up" behind a station reduces waiting and directly improves both throughput and cycle time at any given WIP level. **What exactly "variability reduction relative to the exponential" means quantitatively is the explicit subject of Chapter 8**, with practical achievement methods covered later in Part III.

**Confirmed numerically**: plotting Penny Fab Two's actual cycle-time and throughput curves (with exponential processing times at all stations) against the best/worst/PWC benchmarks for the same rb=0.4 and T0=20 shows **Penny Fab Two genuinely outperforms the PWC**, purely because it's unbalanced and uses parallel-machine stations — exactly the first two improvement levers already operating "for free" in its structure, even before any variability reduction is applied.

## Bottleneck Rate vs. Cycle Time: When Speeding Up the Bottleneck Helps Less Than Expected

For a "good" line at typical WIP levels (roughly 5-10× W0), cycle time is approximately w/rb — so **increasing the bottleneck rate rb mechanically reduces cycle time for any given WIP level.** But the bottleneck isn't always the cheapest or most practical thing to speed up — the book's example: a copper plater that's the bottleneck in a PCB plant, already running maximum hours with no staffing/maintenance inefficiency to recover, where the rate is fundamentally governed by process chemistry. **The only way to add capacity here is a second plater — an extremely expensive option that would represent a 100% capacity increase, likely overkill.** In situations like this, **it may make more economic sense to invest in nonbottleneck capacity instead.**

**Worked comparison**: a four-single-machine-station line, three stations at 10 minutes/job and the bottleneck at 15 minutes/job (rb = 4 jobs/hour). **Option A — speed up the bottleneck to 10 minutes (balancing the line, new rb = 6/hour)**: throughput increases for any WIP level, but **a balanced line tends to starve its bottleneck more frequently than an unbalanced line, requiring more WIP for throughput to approach the new (higher) capacity** — so the throughput curve, while reaching a higher ceiling, sits further below that ceiling than the original system did relative to its own (lower) ceiling. **Option B — instead speed up all three nonbottleneck stations to 5 minutes each, leaving the bottleneck at 15 minutes (rb unchanged at 4/hour)**: throughput still increases for any WIP level — **and for small WIP levels, this nonbottleneck-focused improvement actually beats the bottleneck-speedup option**, even though rb itself never changed.

**The crucial caveat that makes this comparison fair (and the result real, not an artifact)**: the nonbottleneck change was actually a *bigger* intervention (cutting process time in half across three machines) than the bottleneck change (cutting it by only 33% at one machine) — **if you have equal freedom to reduce any process time by a fixed amount (say, 5 minutes), the best place to do it is always the bottleneck.** But real-world economics rarely offer equal-cost options across stations — and when bottleneck capacity is genuinely expensive or infeasible to add (as with the copper plater), this analysis shows that **meaningful performance gains remain available by improving nonbottleneck resources instead**, particularly at lower WIP levels where the nonbottleneck-focused gain can actually exceed what the (more expensive) bottleneck-focused option would deliver.

## Key Takeaways

- The Practical Worst Case is the chapter's actual real-world benchmark — CTpwc = T0 + (w−1)/rb, derived from a balanced, single-machine, exponentially-distributed (maximum randomness) line — and gives the dividing line between "good" (lean) and "bad" (fat) line performance for internal benchmarking.
- The exponential distribution's memoryless property (no information from elapsed processing time) is precisely what makes the PWC mathematically tractable and is the formal definition of "maximum randomness" used throughout the chapter.
- Three concrete levers improve a line performing worse than the PWC: unbalance the line (add capacity, even just at some stations — directly contradicting traditional line-balancing wisdom for non-paced lines), use parallel machines instead of single machines (even with zero added capacity), or reduce variability below the exponential (the explicit subject of Chapter 8).
- Speeding up the bottleneck always wins *if the cost of improvement is held equal across options* — but when bottleneck capacity is genuinely expensive or technically constrained (e.g., a chemistry-governed process), nonbottleneck investment can deliver real, sometimes even larger, throughput gains, especially at lower WIP levels.
- "Unbalancing" a line and "using parallel machines" are both genuinely counterintuitive levers relative to traditional industrial-engineering line-balancing doctrine — both work specifically because they reduce randomness in a line of independent workstations, a fundamentally different setting from the paced assembly lines line-balancing was originally designed for.

## Connects to

- [[littles-law-and-best-case-performance]] and [[worst-case-performance-and-batch-moves]] — the PWC is the third and most practically important of the three bounding cases established across these pages, all built on the same pallet/CONWIP thought experiment.
- [[factory-physics-formal-model-buffers-and-variability]] — the PWC's three derivation conditions (balance, single-machine stations, exponential variability) directly map onto that page's "variability is the root cause of all buffering" thesis, now made fully quantitative.
- [[capacity-planning-and-shop-floor-control]] — the bottleneck-vs-nonbottleneck investment trade-off directly extends the bottleneck-identification material already covered there.
- [[goodbye-jit-hello-lean]] — "unbalancing the line" as an improvement lever is a sharp, source-backed counterpoint to traditional lean/line-balancing intuition, worth cross-referencing.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Internal benchmarking against the PWC is a directly deployable, theoretically rigorous audit methodology; the bottleneck-investment trade-off is a sharp client-advisory tool |
| Current usefulness | 5 | The PWC formula is directly computable from any client's rb and T0, giving an immediate "good vs. bad line" diagnostic |
| KSU support | 5 | Canonical queueing-theory result (exponential/memoryless processing, maximum-randomness benchmarking), core to any production-systems course |
| Tech-stack relevance | 3 | Directly implementable as a Python/spreadsheet calculation for any client with known rb and T0 |
| Business audit value | 5 | "Is this line better or worse than its own theoretical maximum-randomness benchmark?" is an extremely strong, quantitatively rigorous audit framing; the bottleneck-vs-nonbottleneck investment analysis is directly client-advisory |
| Data/workflow value | 4 | The PWC formula and the internal-benchmarking comparison are both directly computable from data most plants already have |
| Reading urgency | 5 | This is the chapter's actual real-world comparison standard — essential before the explicit internal-benchmarking case study (7.3.5) that follows |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit diagnostic / internal benchmarking — computing a client's actual WIP, throughput, and cycle time, then comparing against their own theoretical best-case, worst-case, and PWC curves (computed from their measured rb and T0) to classify their line as "good" or "bad," and recommending one of the three named improvement levers if "bad"

**Use when**:
A client wants to know whether their production line's WIP/cycle-time/throughput performance is "good" or "bad" in any objective sense, or is considering a capacity investment and needs help deciding whether to target the bottleneck or nonbottleneck resources.

**Do not use when**:
The client's process doesn't resemble a flow line of distinguishable stations (e.g., a single highly variable custom job shop with no repeatable routing) — the PWC's derivation assumptions (balanced, single-machine, identifiable bottleneck) may not transfer cleanly.

**Fast retrieval query**:
`subject/throughput-wip-cycle-time` + `priority/now` — or search "practical worst case" / "memoryless exponential distribution" / "internal benchmarking lean fat" / "bottleneck vs nonbottleneck investment"

## North Star Connection

- How this applies to the audit business: the PWC formula (CTpwc = T0 + (w−1)/rb) gives Chris a rigorous, computable "good vs. bad" benchmark for any client's production line, using only data the client likely already has (process times, WIP counts). The bottleneck-vs-nonbottleneck investment analysis is directly usable client-advisory content — a concrete, theoretically grounded answer to "should we invest in speeding up our bottleneck, or is there a cheaper way to get similar gains?"
- Track relevance: Systems / KSU — extremely strong; this is the chapter's central practical payload and arguably the most "audit-ready" quantitative tool in the book so far.
- Possible future Second Brain use: Yes — the PWC calculation and the internal-benchmarking comparison are strong, near-ready candidates for a reusable audit calculation tool/template (Python script or spreadsheet).
