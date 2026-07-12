---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/queuing-theory, use-case/audit, subject/factory-physics, subject/queuing-theory, subject/flow-variability, subject/variability]
---

# Flow Variability and Queueing Fundamentals: From Arrival CVs to the M/M/1 Queue

**Summary**: Extends variability analysis from single-station process times to the flow of jobs *between* stations — characterizing arrival/departure CVs, the propagation-of-variability formula linking them through utilization, the demand-to-interarrival-variability link, and the batch-arrival paradox — then introduces queueing theory proper: Kendall's notation, the four fundamental relations linking WIP/CT/throughput at any station, and the complete M/M/1 queue derivation (steady-state probabilities, WIP, CT, queue time, queue WIP).

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 8 ("Variability Basics"), sections 8.5-8.6.4

**Last updated**: 2026-06-21

---

## Characterizing Flow Variability: Arrival Rate, Arrival CV, and the Serial-Line Chain

A workstation's **arrivals** are characterized analogously to process times: the **arrival rate ra** (jobs/unit time, with mean time between arrivals ta = 1/ra) and the **arrival CV ca** (distinct from the process-time CV ce). A low arrival CV indicates regular, evenly spaced arrivals; a high arrival CV indicates uneven, "bursty" arrivals. **Capacity must exceed the arrival rate** (re > ra) for stability — and in virtually all realistic (variable) systems, capacity must be *strictly* greater, not just equal, to avoid an overloaded station.

**Departures** are characterized the same way (departure rate rd = 1/td, departure CV cd). **In a serial production line** (no yield loss or rework), the chain is exact: the departure rate from station i equals the arrival rate to station i+1, and **the departure CV of station i equals the arrival CV of station i+1** — departures from one station literally become arrivals to the next, propagating variability down the line.

## The Propagation-of-Variability Formula: Departure CV as a Utilization-Weighted Blend

The departure variability from a station is jointly caused by arrival variability *and* process-time variability — and **the relative contribution of each depends on the station's utilization u** (fraction of time busy, u = ra/re for a single machine, or ra·te/m for m parallel machines):

- **As u → 1** (station almost always busy): interdeparture times converge to process times, so cd → ce — process-time variability dominates.
- **As u → 0** (station almost always idle): interdeparture times converge to interarrival times, so cd → ca — arrival variability dominates.

**The single-machine interpolation formula (8.10)**: c²d = u²·c²e + (1−u²)·c²a.

**The multi-machine (m > 1) generalization (8.11)**: c²d = 1 + (1−u²)(c²a−1) + [u²/√m]·(c²e−1).

**The practical consequence**: heavily loaded LV stations tend to produce LV departures; heavily loaded HV stations tend to produce HV departures; MV-fed MV stations produce MV departures — and since departures become the next station's arrivals, **all variability classes can and do propagate through a line**, which is exactly why a single highly variable station can degrade the performance of stations far downstream.

**A second source of MV/HV arrivals worth flagging in client audits**: a workstation fed by *many* independent sources (e.g., a heat-treating operation receiving jobs from several different lines) tends to produce arrivals that look memoryless (exponential, ca≈1, MV) even if each individual source's arrivals are regular (LV) — the *superposition* of multiple regular streams looks bursty, because knowing when the last arrival occurred (from any source) gives little information about when the next one (from any source) will occur.

## Linking Demand Variability to Arrival Variability

Often, interarrival-time variability data simply isn't collected — but **demand** variability data usually is (per the demand models introduced in Chapter 2). The link (8.12): if Nt is the number of demand arrivals in period t (mean μn, standard deviation σn), then **c²a ≈ σ²n/μn** — provided the time period is "long enough" (a good rule of thumb: μn ≥ 10). **This works specifically because Nt is a unitless count**, unlike a physical measurement — the formula isn't dimensionally inconsistent as it might first appear. Note carefully: Nt is the *count* of demands in a period, not the total *quantity* demanded (three orders of 10,000 units each gives Nt = 3, not 30,000). The Poisson distribution (mean = variance) is the special case yielding ca = 1 — and Poisson-distributed demand counts correspond exactly to exponentially distributed (memoryless) interarrival times.

## The Batch-Arrival Paradox

**Batch arrivals** (e.g., a forklift delivering 16 jobs once per 8-hour shift) appear to have zero variability from a delivery-schedule perspective (always exactly 16 jobs, always exactly every 8 hours). **But from the perspective of the individual jobs**, the picture is completely different: the first job in the batch has an 8-hour interarrival time; the next 15 jobs each have a *zero* interarrival time. Computing the actual mean and variance of these individual-job interarrival times yields an arrival SCV of **c²a = 15** for a 16-job batch — wildly different from the "zero variability" naive read. **In general, for batch size k, this produces c²a = k − 1.**

**Resolving the apparent contradiction** ("is it c²a = 15 or c²a = 0?"): the truth is "somewhere in between," because batching confounds **two distinct effects**: (1) the batching decision itself — a *controllable variation* issue (a bad-control problem, structurally analogous to the worst case in [[worst-case-performance-and-batch-moves]]), not a randomness issue; and (2) the genuine randomness in the batch arrivals themselves (characterized by the arrival CV *of the batches*, not the individual jobs). This distinction is developed further in Chapter 9's variability-interactions material.

## Queueing Theory: Why It Matters and How Systems Are Classified

Actual process time (including setups, downtime) typically represents only 5-10% of total cycle time in a real plant (documented in published surveys) — **the great majority of cycle time is spent waiting**. The science of waiting is **queueing theory**. A **queueing system** combines an arrival process, a service (production) process, and a queue; queueing disciplines can be FCFS, LCFS, EDD, SPT, or priority-based; queue space can be unlimited or finite.

**Kendall's notation**, A/B/m/b, classifies single-station, single-job-class systems by: A = interarrival-time distribution, B = process-time distribution, m = number of parallel machines, b = maximum jobs allowed in system (omitted, or written as ∞, when unrestricted). Typical distribution codes: **D** (deterministic/constant), **M** (exponential/Markovian), **G** (completely general — e.g., normal, uniform). Example: M/G/3 means exponential interarrivals, generally distributed process times, three parallel machines, infinite buffer.

The book's approach: start with **M/M/1** and **M/M/m** (tractable, intuition-building), then move to the directly manufacturing-relevant **G/G/1** and **G/G/m**, then finite-buffer variants (M/M/1/b, G/G/1/b) — all restricted to a single job class/product for tractability, though the resulting insights carry over to multi-product systems (with full multi-class treatment available in Buzacott and Shanthikumar 1993).

## The Four Fundamental Relations (Hold for Any Single-Station System)

Regardless of distributional assumptions, machine count, or other specifics, four relationships always hold for a single-station queueing system:

1. **Utilization**: u = ra/re = ra·te/m (8.13) — the probability the station is busy.
2. **CT decomposition**: CT = CTq + te (8.14) — total time at station = queue time + process time (means are additive).
3. **Little's Law at the station**: WIP = TH × CT (8.15).
4. **Little's Law at the queue alone**: WIPq = ra × CTq (8.16).

**Practical power of this set**: knowing *any one* of the four performance measures (CT, CTq, WIP, WIPq) lets you compute the other three — a real audit only needs to measure one of these quantities directly.

## The M/M/1 Queue: Full Derivation

The **M/M/1 queue** — exponential interarrivals, single machine with exponential process times, FCFS, unlimited queue space — is the simplest tractable queueing model, not an accurate manufacturing-station representation, but a foundational building block.

**Why it's tractable**: the **memoryless property** of the exponential distribution means the *only* information needed to characterize the system's future evolution is the current number of jobs in the system, n (the elapsed time since the last arrival, or since the current job started processing, is irrelevant — it "forgets" the past). This lets the system be modeled as a simple birth-death Markov chain: state n increases (an arrival) at rate ra, decreases (a departure) at rate re. **Steady-state balance condition**: the rate of moving from n−1 to n must equal the rate of moving from n to n−1 (otherwise probability "drifts"), giving pn = u·pn−1, where u = ra/re is utilization.

**Solving the recursion** (with p0 = 1−u from the requirement that probabilities sum to 1, and the geometric-series identity 1+u+u²+...=1/(1−u)):

**pn = uⁿ(1−u), for n = 0, 1, 2, ...** (8.18-8.19)

**This requires u < 1** (strictly less than 100% utilization) for stability — if u ≥ 1, the implied geometric series is infinite, meaning the queue grows without bound (matches the earlier best-case/worst-case framework's insistence that capacity must exceed demand).

**Performance measures, derived from the pn distribution via standard series-summation techniques**:

- **WIP(M/M/1) = u/(1−u)** (8.21)
- **CT(M/M/1) = WIP/TH = te/(1−u)** (8.22, via Little's Law, since TH = ra = u·re)
- **CTq(M/M/1) = CT − te = u·te/(1−u)** (8.23)
- **WIPq(M/M/1) = ra × CTq = u²/(1−u)** (8.24)

**The key structural insight**: all four measures are **increasing in u** (busier systems mean more congestion — unsurprising) and, for fixed u, CT and CTq are **increasing in te** (slower machines mean more waiting, at any given utilization level). **Critically, all four expressions have (1−u) in the denominator** — meaning **congestion measures explode nonlinearly as utilization approaches 100%**. WIP and cycle time do not increase gently as a line is pushed toward full utilization; they blow up. This nonlinear-blowup behavior, and its practical implications for how close to "100% busy" a real line should ever be run, is developed further in Chapter 9.

## Key Takeaways

- Flow variability propagates through a serial line exactly like a chain — departure CV from one station becomes arrival CV to the next — and the propagation formula (c²d = u²c²e + (1−u²)c²a) shows utilization determines whether process-time or arrival variability dominates a station's output variability.
- A workstation fed by many independent sources tends to look MV/HV (bursty) even if every individual source is regular — a real-world reason MV/HV arrivals show up even without an obviously "broken" upstream process.
- The batch-arrival paradox (c²a = k−1 for batch size k, viewed from the individual-job perspective) shows that "scheduled, predictable" deliveries can still inject substantial flow variability into a line — a genuinely counterintuitive, audit-relevant finding.
- The four fundamental relations (utilization, CT decomposition, and two applications of Little's Law) mean a real audit only needs to measure one performance metric directly to back out the other three.
- The M/M/1 queue's closed-form results (WIP=u/(1−u), CT=te/(1−u)) make explicit and quantitative the chapter's central warning: congestion doesn't scale linearly with utilization — it explodes as u approaches 1, which is the formal underpinning for "don't run your bottleneck at 100% utilization" advice.

## Connects to

- [[variability-randomness-and-classification]] and [[causes-of-variability-breakdowns-setups-rework]] — this page extends the same CV/SCV vocabulary from process times to arrivals/departures, and shares the LV/MV/HV classification scheme.
- [[worst-case-performance-and-batch-moves]] — the batch-arrival paradox here is a direct flow-side counterpart to that page's batch-material-move worst-case finding; both show ordinary scheduling/batching decisions can produce surprisingly bad variability behavior.
- [[practical-worst-case-and-bottleneck-investment-tradeoffs]] — the PWC's exponential/memoryless derivation is the same mathematical machinery used here to make the M/M/1 queue tractable.
- [[littles-law-and-best-case-performance]] — the M/M/1 performance measures are derived by direct application of Little's Law at both the station and the queue level (relations 3 and 4 above).

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The (1−u) denominator insight — congestion explodes near full utilization — is one of the single most important, broadly applicable findings for any operations audit |
| Current usefulness | 5 | The four fundamental relations let an audit measure just one quantity (often the easiest one) and back out the rest |
| KSU support | 5 | This is the literal introduction to queueing theory — M/M/1 derivation, Kendall notation, fundamental relations — core to any production-systems or operations-research curriculum |
| Tech-stack relevance | 3 | M/M/1 formulas are trivial to implement as a Python/spreadsheet utilization-vs-congestion calculator/visualizer |
| Business audit value | 5 | "Don't run near 100% utilization — congestion blows up nonlinearly" is one of the most quotable, defensible, immediately actionable findings to bring to a client |
| Data/workflow value | 4 | Utilization, arrival rate, and process time are all commonly measurable; the formulas convert them directly into WIP/cycle-time predictions |
| Reading urgency | 4 | Sets up the entire queueing-theory toolkit used in the rest of Part II |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client education and capacity-planning sanity check — using the (1−u) denominator result to explain why pushing a line toward 100% utilization causes WIP and cycle time to blow up nonlinearly, and using the four fundamental relations to back out unmeasured performance metrics from whatever data the client actually has.

**Use when**:
A client wants to run equipment or a bottleneck "as close to 100% busy as possible" to maximize ROI on capital equipment, or is making capacity decisions without understanding the WIP/cycle-time cost of high utilization.

**Do not use when**:
The system in question has a hard, deterministic, zero-variability schedule (e.g., a fully paced assembly line with no randomness) — M/M/1-style queueing congestion effects don't apply there in the same way.

**Fast retrieval query**:
`subject/queuing-theory` + `subject/flow-variability` — or search "M/M/1 queue derivation" / "propagation of variability formula" / "batch arrival paradox" / "congestion explodes utilization"

## North Star Connection

- How this applies to the audit business: the M/M/1 congestion-explosion result (WIP and cycle time both have 1/(1−u) in them) is a uniquely powerful, simple-to-explain finding for pushing back on a client's instinct to run equipment "as close to capacity as possible" — directly informs capacity-investment and staffing-level recommendations.
- Track relevance: Business / Systems / KSU — this page is the formal introduction to queueing theory, the mathematical backbone of the rest of Part II.
- Possible future Second Brain use: Yes — a simple M/M/1 (and later G/G/1) utilization-vs-WIP/CT visualizer would make a strong, intuitive client-facing audit tool once a relevant engagement exists.
