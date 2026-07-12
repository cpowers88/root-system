---
domain: systems
type: framework
tags: [priority/next, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/queuing-theory, use-case/audit, subject/factory-physics, subject/queuing-theory, subject/blocking, subject/kanban]
---

# Blocking and Finite-Buffer Queues: the M/M/1/b Model

**Summary**: Extends queueing theory to systems with finite buffer space — the M/M/1/b queue, where the arrival process stops (the upstream machine is "blocked") whenever the system is full. Fully worked through a two-machine-in-series example showing buffered vs. unbuffered tradeoffs (an 83% WIP reduction at the cost of only 18% throughput), demonstrates that finite buffers force stability regardless of arrival/service rates, and gives the full general (nonexponential) blocking approximation for all three utilization cases (u<1, u>1, u=1), with a worked example showing how reducing process variability lets a small buffer keep almost all of an unbuffered line's throughput.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 8 ("Variability Basics"), sections 8.7-8.7.2 (complete)

**Last updated**: 2026-06-21

---

## Why Blocking Matters: Real Queues Are Never Infinite

Every queueing model considered so far (M/M/1, M/M/m, G/G/1, G/G/m) allows the queue to grow without bound as utilization approaches 1. In the real world, queues are always bounded — by physical space, time, or operating policy. **An important Factory Physics topic is therefore the behavior of systems with finite queueing space.**

**The M/M/1/b queue**: exponential interarrival and process times (as in M/M/1), but only enough space for b units total (in queue plus in process). Once the system is full, the arrival process is *stopped* — the feeding machine is said to be **blocked**. This is an extremely common real manufacturing pattern: a two-station manufacturing cell with a finite buffer between stations, where the upstream machine processes (assumed) ample raw material and feeds the buffer of the downstream machine. **By their very nature, all kanban systems exhibit blocking behavior** — kanban acts exactly like a finite buffer that caps WIP.

**A subtlety in interpreting ra and u under blocking**: ra now represents the rate of *potential* arrivals (assuming the system isn't full) rather than an unconditional arrival rate, and u = ra/re represents what utilization *would be* if no arrivals were ever turned away — consequently, **u can equal or exceed 1** in a blocked system without causing instability, since blocking itself prevents the queue from ever actually growing unbounded.

## The M/M/1/b Steady-State Solution

Following the same birth-death-Markov-chain logic as M/M/1, but now over a *finite* state space n=0,1,...,b:

**pn = uⁿ(1−u) / (1−u^(b+1))**, for n=0,...,b (8.30-8.31)

— reducing to the ordinary M/M/1 result as b→∞. **For the special case u=1**, all states become equally likely: pn = 1/(b+1) for all n (8.32).

**Resulting performance measures** (derived by direct summation, paralleling the M/M/1 derivation):

- **WIP(M/M/1/b)** = u/(1−u) − (b+1)u^(b+1)/(1−u^(b+1)) for u≠1, or **= b/2** for u=1 (8.33, 8.35, 8.37)
- **TH(M/M/1/b) = (1−pb)·ra**, i.e., the *effective* arrival rate after accounting for blocked (turned-away) arrivals — TH = (1−u^b)/(1−u^(b+1)) × ra for u≠1, or = b/(b+1) × ra for u=1 (8.34, 8.36, 8.38)
- CT, CTq, WIPq follow by applying Little's Law as usual (8.39-8.41)

**A formal proof that blocking always reduces throughput relative to no blocking**: TH(M/M/1/b) < re for u=1 (specifically TH = b/(b+1) × re), and the smaller the buffer b, the greater the throughput reduction. **Blocking is therefore never "free"** — there is always a real throughput cost to capping WIP via a finite buffer.

## Worked Example: Buffered vs. Unbuffered Two-Machine Line

**Setup**: two machines in series, te(1)=21 minutes, te(2)=20 minutes, both exponential (ce=1), with room for exactly 2 jobs in the buffer between them (so b=4: two in the buffer, two "in" the machines themselves).

**Unbuffered (infinite-buffer) case**: utilization of the second machine, u = ra/re = (1/21)/(1/20) = 0.9524. Using plain M/M/1 formulas: WIP=20 jobs, TH=0.0476 job/minute, **CT=420.18 minutes**.

**Buffered (b=4) case**: TH(M/M/1/b) = 0.039 job/minute, partial WIP at the second machine (WIPP, i.e., excluding WIP being actively processed at the first machine) = 1.894 jobs, **CT = WIPP + te(1) = 1.894 + 21 = 69.57 minutes**, and total system WIP = TH × CT = 2.71 jobs.

**The tradeoff, quantified**: limiting the buffer reduces WIP and CT by **more than 83%** — but also reduces throughput by **18%**. **The explicit warning this generates**: an 18% throughput loss could easily outweigh the inventory savings, which is exactly why **kanban cannot be implemented simply by shrinking buffer sizes** — that approach typically sacrifices too much throughput. **The only way to reduce WIP and CT without giving up substantial throughput is to also reduce variability** ("remove the rocks, not just lower the water," echoing the classic lean metaphor) — but the M/M/1/b model itself can't be used to study variability reduction, since it assumes exponential process times throughout; that requires the general blocking approximation, covered next.

## Finite Buffers Force Stability — and the Reversibility Result

**A second key observation from M/M/1/b**: a finite buffer forces system stability *regardless of the relative arrival and service rates*, because WIP and CT literally cannot "blow up" — they're capped by the buffer size. **Demonstrated by reversing the example's machine order** (faster machine second, u=21/20=1.05 — formally "unstable" under an infinite-buffer assumption, where WIP/CT would grow to infinity): with the b=4 finite buffer instead, TH=0.0390 job/minute, WIP=2.097 jobs, CT=73.78 minutes, total line WIP=2.88 jobs — all finite and well-defined, despite u>1.

**The reversibility result**: throughput is *unaffected* by which machine is positioned first vs. second in the line (0.0390 job/minute either way) — though WIP and CT differ slightly between orderings, since the arrival rate to the *system* differs (greater when the faster machine feeds the line, since more material enters per unit time). This **reversibility property holds generally**, for lines with more than two machines and general process-time distributions (Muth 1979) — a theoretically elegant result, though one with limited practical bite since firms rarely have the option to literally reverse a production line's machine order.

## General Blocking Models: Beyond Exponential (Partial)

To study variability reduction under blocking, the M/M/1/b model must be extended to general (nonexponential) distributions — an exact treatment is very difficult (see Buzacott and Shanthikumar 1993, Ch. 4 for the full development), but a useful **approximation** follows the same modification pattern used to build G/G/1 from M/M/1.

**Case 1, arrival rate less than production rate (u<1)** (the only case captured so far in this ingest): compute the unblocked expected WIP via Kingman's equation plus Little's Law:

**WIPnb ≈ ra·te + [(c²a+c²e)/2] × [u²/(1−u)]** (8.42)

then back out a **"corrected" utilization** ρ = WIPnb/(WIPnb+u) (8.43), and substitute ρ for (almost all of) the u terms in the M/M/1/b throughput expression:

**TH ≈ [(1−uρ^(b−1))/(1−u²ρ^(b−1))] × ra** (8.44)

This combines Kingman's variability-aware queue-time estimate with the M/M/1/b blocking structure — substantially more complex than the pure M/M/1/b case, but the source notes it remains **straightforward to evaluate in a spreadsheet**. Because ρ=u exactly when ca=ce=1, this approximation also correctly reduces to the pure M/M/1/b result in the all-exponential special case.

Because the WIP and CT expressions for this general case become messy, the source instead gives **bounds**: WIP < min{WIPnb, b} (8.45), and from Little's Law, CT > min{WIPnb, b}/TH (8.46) — only an approximate bound, since TH itself is an approximation.

**Case 2, arrival rate greater than production rate (u>1)**: approximated by reversing the line — when the machines are swapped, the production process becomes the arrival process and vice versa, so the reversed line's utilization is 1/u (<1, since u>1). Compute WIPnb for the reversed line the same way:

**WIPnb ≈ [(c²a+c²e)/2] × [(1/u)²/(1−1/u)] + 1/u** (8.47)

then a corrected utilization ρR = WIPnb/(WIPnb+1/u), set ρ = 1/ρR, and compute TH exactly as in Case 1, again using (8.45)-(8.46) for the WIP/CT bounds.

**Case 3, arrival rate equal to production rate (u=1)**: a direct approximation (Buzacott and Shanthikumar 1993), with no reversal trick needed:

**TH ≈ [(c²a+c²e+2(b−1)) / (2(c²a+c²e+b−1))] × re** (8.48)

— again paired with bounds (8.45)-(8.46) for WIP and CT.

**Worked example — variability reduction lets a small buffer keep almost all the throughput**: revisiting the 8.7.1 example (te(1)=21 min, te(2)=20 min, b=4, u=0.9524), but now with both machines' effective CVs reduced to 0.25 (from 1.0/exponential). WIPnb = [(0.25²+0.25²)/2]×[0.9524²/(1−0.9524)] + 0.9524 = **2.143**. Corrected utilization ρ = (2.143−0.9524)/2.143 = **0.556**. Throughput TH = [(1−0.9524×0.5563¹)/(1−0.9524²×0.5563¹)] × (1/21) = **0.0473 job/min** — only a **<1% reduction** from the unbuffered rate of 1/21 = 0.0476, compared to the 18% reduction seen earlier at ce=ca=1. **The lesson made concrete**: cutting process variability (not just buffer size) is what lets a kanban-style WIP cap keep throughput nearly intact — directly substantiating the "remove the rocks, not just lower the water" warning with numbers, and explaining why variability reduction is treated as essential JIT-implementation groundwork rather than optional polish.

## Key Takeaways

- Finite buffers (the M/M/1/b model) cap WIP/CT growth but always cost some throughput relative to an unbounded queue — there is no free lunch in shrinking buffer sizes.
- The two-machine worked example (83% WIP/CT reduction for an 18% throughput cost) is a directly reusable template for evaluating any kanban/buffer-sizing decision quantitatively, rather than by intuition alone.
- Reducing buffer size alone (without reducing variability) is the wrong lever for getting both low WIP *and* high throughput simultaneously — kanban-style buffer reduction needs to be paired with genuine variability reduction.
- Finite buffers force system stability regardless of arrival/service rates (u can exceed 1 and the system still has finite, well-defined WIP/CT) — a structurally different stability guarantee than the unbuffered queueing models.
- The reversibility result (throughput is unaffected by machine ordering in a line) is theoretically elegant but rarely practically actionable, since reversing machine order is seldom a real option.
- The general blocking model (all three u cases) lets the buffered-vs-unbuffered tradeoff be evaluated with realistic, nonexponential process variability, not just the all-exponential M/M/1/b special case.
- The variability-reduction worked example is the single sharpest, most quotable number in this page: cutting process CV from 1.0 to 0.25 turns an 18% throughput loss into a <1% throughput loss for the *same* buffer size — variability reduction, not buffer-size tinkering, is the actual lever.

## Connects to

- [[vut-equation-and-parallel-machines]] — the general blocking approximation here directly reuses Kingman's equation as its starting point.
- [[kanban-mechanics-and-pull-system-variants]] — this page's "kanban is exactly a finite buffer" framing and its explicit warning against buffer-shrinking-without-variability-reduction directly extend that earlier kanban-mechanics page with formal queueing backing.
- [[flow-variability-and-queueing-fundamentals]] — the M/M/1/b derivation follows the identical birth-death Markov chain method used for the unbounded M/M/1 queue on that page, just over a finite state space.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Directly informs kanban/buffer-sizing decisions, a common SMB/contractor operational question |
| Current usefulness | 4 | The buffered-vs-unbuffered worked example is a directly reusable audit illustration template |
| KSU support | 5 | Standard finite-buffer queueing theory content for any production-systems or operations-research course |
| Tech-stack relevance | 3 | Source explicitly notes spreadsheet-implementability for both M/M/1/b and the general blocking approximation |
| Business audit value | 5 | "Don't shrink your buffer without also reducing variability" is a sharp, quotable, immediately actionable warning against naive kanban/lean buffer-cutting |
| Data/workflow value | 4 | Requires buffer size, arrival/process rates — generally available data for a real client production line |
| Reading urgency | 3 | Important but slightly less universally applicable than the VUT equation or variability-pooling material already ingested |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit warning and calculation tool — when a client is considering kanban implementation or buffer-size reduction, using the M/M/1/b worked example and the "remove the rocks, not just lower the water" framing to push back against naive buffer-shrinking that ignores the throughput cost, and recommending variability reduction as the only way to get both benefits simultaneously.

**Use when**:
A client wants to reduce WIP/inventory via smaller buffers or kanban card counts, especially if framed as a "free" or low-cost inventory-reduction tactic.

**Do not use when**:
The client's system already has very low process-time and arrival variability (ce, ca both near 0) — in that case buffer reduction costs little throughput and the warning is less load-bearing.

**Fast retrieval query**:
`subject/blocking` + `subject/kanban` — or search "M/M/1/b queue" / "blocked machine finite buffer" / "kanban remove the rocks not lower the water" / "reversibility queueing"

## North Star Connection

- How this applies to the audit business: gives Chris a quantified, source-backed counter-argument whenever a client (or a lean/kanban consultant) proposes shrinking buffers or WIP caps without addressing the underlying variability — directly prevents an "I cut inventory and lost too much throughput" failure mode.
- Track relevance: Business / Systems — directly relevant to any kanban or WIP-cap implementation engagement.
- Possible future Second Brain use: a "Buffer-Sizing Calculator" (general blocking model across all three u cases) is now a complete, ready-to-build spreadsheet/Python tool candidate — see [[variability-pooling-and-chapter-8-conclusions]] for the companion pooling toolkit.
