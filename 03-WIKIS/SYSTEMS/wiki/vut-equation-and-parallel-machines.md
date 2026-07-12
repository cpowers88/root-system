---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/queuing-theory, use-case/audit, subject/factory-physics, subject/queuing-theory, subject/vut-equation, subject/variability-pooling]
---

# The VUT (Kingman's) Equation, Parallel Machines, and Variability Pooling

**Summary**: Generalizes the M/M/1 queue to realistic (nonexponential) systems via the VUT/Kingman approximation — CTq = V·U·T, a clean decomposition into a variability term, a utilization term, and a time term — fully worked through the Hare X19/Tortoise 2000 case (recovering the chapter's opening numbers and demonstrating how variability propagates downstream from Hare to Tortoise), then extends to parallel-machine stations (M/M/m, G/G/m) and demonstrates the variability-pooling principle: a single combined queue with parallel servers always outperforms separate dedicated queues at identical utilization and variability.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 8 ("Variability Basics"), sections 8.6.5-8.6.7

**Last updated**: 2026-06-21

---

## Why M/M/1 Isn't Enough, and the VUT/Kingman Approximation

Most real manufacturing systems don't satisfy M/M/1's exponential-everything assumptions — process times are seldom exponential, and since departures from non-exponential upstream stations become non-exponential arrivals downstream, interarrival times usually aren't exponential either. The **G/G/1 queue** (general interarrival and process-time distributions) is needed — but without the memoryless property, *exact* G/G/1 performance measures can't be computed.

**The two-moment approximation** (using only mean and CV/standard deviation of the interarrival and process-time distributions) is reasonably accurate for typical manufacturing systems — it degrades only when ce and ca are much greater than one, or when u exceeds 0.95 or falls below 0.1. Because it works well, it's the basis of several commercial manufacturing-queueing-analysis packages.

**Kingman's equation (the VUT equation, 8.25-8.26)**, first investigated by Kingman (1961):

**CTq(G/G/1) = [(c²a + c²e)/2] × [u/(1−u)] × te = V · U · T**

where **V** (the variability term, dimensionless) = (c²a+c²e)/2, **U** (the utilization term) = u/(1−u), and **T** (the time term) = te. This decomposition is exact for M/M/1 (and, less obviously, exact for M/G/1 as well) — when ca = ce = 1, V collapses to 1 and the remaining UT term is exactly the M/M/1 queue time. **The interpretive power of V**: if V < 1, the G/G/1 queue's congestion will be *better* than M/M/1's at the same utilization; if V > 1, it will be *worse*. **This makes M/M/1 the intermediate reference case for single stations, directly analogous to the role the practical worst case played for whole lines** (see [[practical-worst-case-and-bottleneck-investment-tradeoffs]]).

## Worked Example: The Hare X19 and the Variability It Propagates Downstream

**The Hare X19** (from [[variability-randomness-and-classification]] and [[causes-of-variability-breakdowns-setups-rework]]): c²e = 6.25 (HV), feeding from sources making interarrivals roughly exponential (ca²=1), at utilization u = 0.9583. Plugging into the VUT equation:

CTq = [(1+6.25)/2] × [0.9583/(1−0.9583)] × 20 minutes = **1,667.5 minutes = 27.79 hours**

— exactly the number reported at the start of the chapter, now derived from first principles.

**The Tortoise 2000 fed directly by the same demand** (ce²=1, ca²=1): CTq = [(1+1)/2] × [0.9583/(1−0.9583)] × 20 minutes = **1,568.97 minutes = 26.15 hours**.

**The striking finding when the Hare X19 feeds the Tortoise 2000 in series** (same total demand, no yield loss): the Tortoise 2000's *arrivals* are no longer ca²=1, because they're the Hare X19's *departures*. Using the propagation formula (c²d = c²eu² + c²a(1−u²)) from [[flow-variability-and-queueing-fundamentals]]: c²a(Tortoise) = c²d(Hare) = 6.25(0.9583²) + 1.0(1−0.9583²) = **5.82**. Plugging this into the VUT equation for the Tortoise 2000: CTq = [(5.82+1.0)/2] × [0.9583/(1−0.9583)] × 20 minutes ≈ 1,568.97 → wait — actual computed value: **CTq ≈ 26.15 hours** — **almost as large as the queue time at the Hare X19 itself, even though the Hare X19's own process variability is far higher than the Tortoise 2000's.** The reason: the high variability of arrivals *to* the Tortoise 2000 (ca=2.41, inherited entirely from the upstream Hare X19) drives its congestion just as much as its own (much lower) process variability would on its own. **If the Tortoise 2000 instead received only moderately variable arrivals (ca=1.0), its queue time would drop to 7.67 hours (the plain M/M/1 prediction)** — the excess congestion at the Tortoise 2000 is a direct, quantified consequence of variability propagating downstream from the Hare X19. **This is the single clearest illustration in the chapter of why a non-bottleneck station's own low variability does not protect it from a highly variable upstream feeder.**

## Parallel Machines: M/M/m and the Sakasegawa Approximation

Real workstations often consist of multiple machines in parallel, sharing a single combined queue (like a bank, not separate grocery-store checkout lines). The **M/M/m queue** has exact but messy steady-state probabilities that offer little intuition; the **Sakasegawa (1977) closed-form approximation** is far more useful and reasonably accurate:

**CTq(M/M/m) = [u^(√(2(m+1))−1) / (m(1−u))] × te** (8.27)

This reduces exactly to the M/M/1 formula when m=1.

**Worked example (Briar Patch Manufacturing, three Tortoise 2000s)**: demand of 207 jobs/day arrives, served by three parallel machines.

- **Dedicated case** (each machine gets its own 1/3 of demand, separate queues): each machine sees u=0.958, exactly the single-machine case already computed — CTq = 7.67 hours.
- **Combined case** (all three machines share one queue for the full demand): u is unchanged at 0.958 (same total rate divided by same total capacity), but CTq = [0.958^(√8−1) / (3×(1−0.958))] × 1 hour = **2.467 hours** — *dramatically lower* than the dedicated case.

**The reason, and the principle it demonstrates — variability pooling**: a long process time at a dedicated machine delays only the jobs waiting at that one machine (like getting stuck behind a slow shopper at one grocery checkout line); when machines share a combined queue, the next job simply gets routed to a different, available machine instead of waiting (like a single bank queue serving multiple tellers) — the machine experiencing a long process time gets effectively "bypassed" and doesn't disproportionately damage average queue time. **This is a specific instance of the more general variability-pooling property developed further in section 8.8.**

## G/G/m: The Parallel-Machine VUT Equation

For nonexponential process and interarrival times with m parallel machines, the same substitution trick used to build the single-machine G/G/1 approximation from M/M/1 is applied to M/M/m:

**CTq(G/G/m) = [(c²a+c²e)/2] × [u^(√(2(m+1))−1) / (m(1−u))] × te** (8.29)

The V and T terms are identical to the single-machine VUT equation; only the U term changes to incorporate m. **Despite its complicated appearance, it requires no iterative solving and is directly spreadsheet-implementable** — and when paired with the multimachine linking equation (8.11) from [[flow-variability-and-queueing-fundamentals]], it forms the basis of a complete line-performance spreadsheet tool (single-station approximation chained station-to-station via the linking equation).

## Key Takeaways

- The VUT equation (CTq = V·U·T) generalizes M/M/1 to realistic, nonexponential systems using only means and CVs — exact for M/M/1 and M/G/1, a good approximation elsewhere except at extreme variability or utilization (u>0.95 or u<0.1).
- The V term (variability) makes M/M/1 the natural single-station reference point: V<1 means better-than-M/M/1 congestion, V>1 means worse.
- The Hare-feeds-Tortoise worked example is the chapter's sharpest illustration that a downstream station's own low process variability does not protect it from a highly variable upstream feeder — propagated arrival variability can dominate a station's congestion just as much as its own process variability.
- Variability pooling (combining separate queues into one shared queue across parallel machines) dramatically reduces congestion at identical total capacity and utilization — directly analogous to choosing a single bank queue over separate grocery-checkout lines.
- The G/G/m VUT equation, paired with the multimachine linking equation, is directly spreadsheet-implementable as a full line-performance estimation tool — no specialized software required.

## Connects to

- [[flow-variability-and-queueing-fundamentals]] — this page's worked Hare-feeds-Tortoise example directly applies that page's propagation-of-variability formula (8.10) and the four fundamental relations.
- [[variability-randomness-and-classification]] and [[causes-of-variability-breakdowns-setups-rework]] — the Hare X19/Tortoise 2000 case fully resolved here was introduced and quantified (CV values) on those two pages respectively.
- [[practical-worst-case-and-bottleneck-investment-tradeoffs]] — M/M/1 plays the same "intermediate reference case" role for single stations that the PWC plays for whole lines; both establish a "good vs. bad" dividing line using the same exponential/memoryless machinery.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The VUT equation is the single most generally applicable queueing formula in the book — directly usable for almost any real client workstation |
| Current usefulness | 5 | Spreadsheet-implementable today; the variability-pooling result is an immediately deployable recommendation (combine queues, don't dedicate machines) |
| KSU support | 5 | Kingman's equation is the canonical approximation taught in any queueing-theory or production-systems course |
| Tech-stack relevance | 4 | Explicitly noted by the source as spreadsheet-implementable without iterative solving — a strong, near-trivial Python/Excel tool candidate |
| Business audit value | 5 | "Combine your separate queues into one shared queue" (variability pooling) is a concrete, often-free operational recommendation; the Hare-feeds-Tortoise case is a powerful illustration for explaining why a "good" downstream station still suffers from a "bad" upstream one |
| Data/workflow value | 5 | Requires only means and CVs of arrival/process times — data most clients can supply or estimate |
| Reading urgency | 4 | The VUT equation is the practical workhorse formula of the entire variability chapter |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit calculation tool and client recommendation — using the VUT equation to estimate queue time/WIP at any client workstation from basic CV/utilization data, and recommending queue-pooling (combining separate machine queues into one shared queue) wherever multiple parallel machines currently run dedicated queues.

**Use when**:
A client has multiple machines doing the same job with separate queues/assignments (e.g., dedicated operators per machine, or separate order streams per machine), or wants to estimate expected wait times at a workstation without expensive simulation software.

**Do not use when**:
ca or ce is far above 1 (extreme variability) or u is above 0.95 or below 0.1 — the two-moment approximation degrades in these regions and a more careful (or simulation-based) analysis is warranted.

**Fast retrieval query**:
`subject/vut-equation` + `subject/variability-pooling` — or search "Kingman's equation" / "VUT equation factory physics" / "Hare X19 feeds Tortoise 2000" / "variability pooling parallel machines"

## North Star Connection

- How this applies to the audit business: the VUT equation is the single most generalizable, spreadsheet-ready queueing tool in the book — Chris can estimate expected wait times at almost any client workstation from basic data, and the variability-pooling result (combine queues) is a frequently free, immediately actionable recommendation that doesn't require capital investment.
- Track relevance: Business / Systems / KSU — core formula, likely the most-used single equation from this entire chapter in real engagements.
- Possible future Second Brain use: Yes — a spreadsheet/Python tool implementing the VUT equation plus the multimachine linking equation, chained across a multi-station line, is a strong, near-ready candidate for a reusable audit deliverable.
