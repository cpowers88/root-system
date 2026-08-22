---
domain: systems
type: framework
tags: [subject/factory-physics, subject/variability, subject/machine-breakdowns, subject/setup-reduction]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, audit, data-workflow]
---

# Causes of Variability: Breakdowns, Setups, and Rework — Formulas and Worked Examples

**Summary**: Quantifies the five named sources of effective process-time variability — natural variability, preemptive outages (breakdowns), nonpreemptive outages (setups), operator availability, and rework — with the explicit CV-inflation formulas for breakdowns and setups, fully worked through the Briar Patch Hare X19/Tortoise 2000 case (CV=2.5 vs. CV=1.0 from identical 75% availability) and a flexible-vs-fast-machine setup comparison, plus the chapter's summary table for sequentially combining multiple outage types.

**Sources**: factoryPhysics.pdf (Hopp & Spearman, 3rd ed., Waveland Press), Chapter 8 ("Variability Basics"), section 8.4

**Last updated**: 2026-06-21

---

## Natural Variability: The Catch-All Baseline

**Natural process time** is the variability inherent in a process excluding random downtimes, setups, or other external influences — minor fluctuations from differences in operators, machines, and material (e.g., dust in an operator's eye). It is a genuine catch-all category since it absorbs unidentified variability sources. Manual processes tend to have more natural variability than automated ones, but **even fully automated machining has some natural variability** (e.g., slight material-composition differences affecting processing speed). In most systems, natural process times are themselves LV (c0 < 0.75) — natural variability alone is rarely the dominant driver; the **detractors** layered on top (downtime, setups, operator unavailability) are what typically push effective process time into MV or HV territory.

## Preemptive Outages (Breakdowns): The Formula and the Hare/Tortoise Case

**Preemptive outages** occur whether wanted or not, including right in the middle of a job (true breakdowns, power outages, emergency operator call-aways, running out of consumables) — distinct from nonpreemptive outages (setups), covered separately below.

**The standard capacity-only treatment**: availability A = mf/(mf+mr), where mf = mean time to failure (MTTF) and mr = mean time to repair (MTTR). Effective mean process time te = t0/A. This is what most industrial capacity-planning tools compute — and it's where they stop.

**The full variability-aware treatment** additionally requires cr = σr/mr (the CV of repair times) and yields the effective SCV:

**c²e = c²0 + (1 + c²r) · A(1−A) · (mr/t0)**

The first term is the natural (unaccounted-for) variability. The second term exists **purely because outages are random** — it would be present even if repair times themselves were perfectly constant (cr = 0; e.g., a fixed-duration periodic adjustment), since the *timing* of the outage is still random. The third term vanishes only if repair-time variability itself (cr) is eliminated. **Both of the latter two terms increase with mr for fixed availability** — so, all else equal, *long* repair times inflate variability more than *short* ones, even at identical availability.

**The Briar Patch Hare X19 / Tortoise 2000 worked numbers**: both machines have t0 = 15 minutes, σ0 = 3.35 minutes (c0 = 0.223, c²0 = 0.05), and 75% availability. The Hare X19 has MTTF = 744 minutes, MTTR = 248 minutes (long, infrequent); the Tortoise 2000 has MTTF = 114.0 minutes, MTTR = 38.0 minutes (short, frequent — exactly 1/3 the times of the Hare X19). Both have repair-time CV = 1.0 (moderate variability). Plugging into the formula for both:

- **Hare X19**: c²e = 0.05 + (1+1)(0.75)(0.25)(248/15) = **6.25**, so ce = **2.5** — well into HV.
- **Tortoise 2000**: c²e = 0.05 + (1+1)(0.75)(0.25)(38/15) = **1.0**, so ce = **1.0** — only MV.

Same availability (75%), same effective mean process time (20 minutes for both, te = t0/A) — but the Hare X19's line will need an outage's worth of WIP (4.13 hours) in a downstream buffer to avoid starving the next station, versus less than one-sixth that for the Tortoise 2000, to achieve equivalent protection against throughput loss.

**The counterintuitive conclusion**: at equal availability, **a machine with frequent-but-short outages is preferable to one with infrequent-but-long outages** — somewhat contrary to intuition (which might favor "one big headache per month" over "a minor throb every day"), but the daily throb is logistically easier to manage and produces less variability and less required buffer WIP. **Caution against complacency**: this doesn't mean short-frequent failures are *good* — no failures at all beats either option; this insight is about converting unavoidable failures to a more manageable pattern (e.g., via preventive maintenance), not deflecting effort from reliability improvement.

## Nonpreemptive Outages (Setups): Formulas and the Flexible-vs-Fast-Machine Case

**Nonpreemptive outages** will inevitably occur but allow some control over *exactly when* (waiting until the current job/piece finishes before stopping) — contrasted with preemptive outages, which force a stoppage regardless of job state. Setups due to process changes (e.g., changing a mask) are nonpreemptive; setups due to product changes are more under direct managerial control (how many units to make before changing over) and are the subject of separate chapters (9, 15) on lot-sizing.

**Why average-capacity-only analysis is insufficient here too**: it can show "short setups beat long setups," but cannot meaningfully compare a slow machine with short/no setups against a fast machine with periodic long setups when their *effective* capacities are equal.

**Formulas** (assuming an average of Ns parts/jobs between setups, mean setup duration ts, CV of setup duration cs, and the probability of needing a setup after any given part being constant — i.e., 1/Ns):

- te = t0 + ts/Ns
- σ²e = σ²0 + [ts·(c²s) + (Ns−1)·t²s] / Ns² (variance contribution)
- c²e = σ²e / t²e

**The worked comparison**: Machine 1 (fast, t0 = 1 hour, c0 = 0.5, 2-hour setup every 4 parts on average) vs. Machine 2 (flexible, no setups, t0 = 1.2 hours, c0 = 0.25, Ns = 10, ts = 2 hours, cs = 0.25). **Effective capacity is identical for both (re = 0.833 parts/hour)** — so the only question that matters is which machine has *less* variability. Computing: Machine 1's c²e = 0.25, while Machine 2's c²e = 0.31 — **Machine 1, the faster machine with periodic long setups, is actually less variable than the slower flexible machine**, despite Machine 1 having setups and Machine 2 not.

**Why this matters**: the conclusion is a function of the specific numbers, not a universal rule — flexible (no-setup) machines do not automatically have less variability. **A modification**: if Machine 2's setup were shortened to ts = 1 hour after an average of Ns = 5 parts (same effective capacity, shorter/more-frequent setups instead of longer/less-frequent), Machine 2's c²e drops to 0.16, making it the better choice. **This variability-reduction effect is a concrete, quantified motivation for two practices already covered elsewhere in the wiki**: JIT's preference for short setups (see [[jit-origins-goals-and-environment-as-control]], [[jit-implementation-tactics-and-quality-revolution]]) and the broader case for flexible manufacturing technology — but the Machine 1/2 numbers are a sharp reminder that "fewer/shorter setups" only helps if it actually reduces the *effective* process-time CV relative to the alternative, which requires running the comparison, not assuming it.

## Rework: The Same Mechanics as Nonpreemptive Outages

**Rework** (a workstation performs a task, checks it, and repeats the task if it failed) is mathematically equivalent to the nonpreemptive-outage/setup case if the rework time is treated as an "outage." It robs capacity (the traditional concern) **and** contributes substantially to effective-process-time variability (an analysis identical in structure to the setup case above shows c²e increases as the rework fraction increases) — so two machines with identical effective capacity but different rework fractions are *not* equivalent, exactly as in the setup case. This quality/operations interface is developed further elsewhere in the book (Chapter 12).

## Summary of Variability Formulas: Sequential Application

When a process is subject to *both* preemptive outages (breakdowns) and nonpreemptive outages (setups, rework) simultaneously, the formulas above are applied **sequentially, not simultaneously**: start from natural process-time parameters (t0, c²0); apply the preemptive-outage (breakdown) formulas to get an intermediate (te, σe, c²e); then apply the nonpreemptive-outage (setup/rework) formulas *using those intermediate values in place of t0 and c²0* to get the final, fully "inflated" effective process-time parameters. Table 8.2 in the source organizes this explicitly by situation (natural / preemptive / nonpreemptive), parameters needed, and worked formula.

## Key Takeaways

- Average-capacity-only analysis treats any two machines/processes with the same effective rate as equivalent — Factory Physics' variability-aware analysis shows this is frequently wrong, with real WIP/buffer/throughput consequences.
- The breakdown-CV formula (c²e = c0² + (1+cr²)A(1−A)(mr/t0)) makes explicit that, at equal availability, *frequent short outages beat infrequent long outages* — the Hare X19 (ce=2.5, HV) vs. Tortoise 2000 (ce=1.0, MV) case is the canonical worked illustration, directly reusable as a client comparison template.
- The setup-CV formula shows flexible (no-setup) machines do *not* automatically have less effective variability than machines with periodic setups — the comparison has to be run with real numbers, not assumed.
- Rework is mathematically identical to a nonpreemptive outage — quality problems are a genuine variability source, not just a capacity-loss issue.
- Combined outage types (breakdowns AND setups on the same process) require applying the formulas sequentially, feeding the breakdown-adjusted (te, c²e) into the setup formula as the new baseline.

## Connects to

- [[variability-randomness-and-classification]] — this page fully quantifies the Hare X19/Tortoise 2000 case introduced there and the CV/SCV vocabulary established there.
- [[jit-implementation-tactics-and-quality-revolution]] — the setup-time variability formula provides the explicit quantitative backing for that page's setup-reduction material (internal/external setup classification).
- [[mrp-problems-nervousness-and-yield-losses]] — yield-loss/rework as a variability source there connects directly to this page's rework-as-nonpreemptive-outage treatment.
- [[littles-law-and-best-case-performance]] — the "WIP needed to absorb an average outage" framing (Hare X19 needing 4.13 hours of downstream buffer WIP vs. Tortoise 2000's <1/6 of that) is a direct application of Little's Law-style buffer reasoning.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | A client's choice between two pieces of equipment with "the same average output" is exactly the comparison this page's formulas resolve rigorously |
| Current usefulness | 5 | Both formulas (breakdown CV, setup CV) are directly computable from data most clients can supply (MTTF/MTTR or setup frequency/duration) |
| KSU support | 5 | Canonical variability-quantification formulas for any production-systems or quality-engineering course |
| Tech-stack relevance | 3 | Strong candidate for a small Python/spreadsheet calculator: input MTTF/MTTR/setup data, output effective CV and recommended buffer sizing |
| Business audit value | 5 | The Hare X19/Tortoise 2000 worked example and the Machine 1/2 setup comparison are both ready-made, numbers-backed client deliverables for equipment-selection or maintenance-strategy decisions |
| Data/workflow value | 5 | MTTF/MTTR and setup frequency/duration data are commonly already tracked (or trackable) by clients, making this formula set highly deployable |
| Reading urgency | 4 | The single most quantitatively "audit-ready" page in the variability material so far |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Audit calculation tool — given two pieces of equipment, two maintenance strategies, or two setup-reduction options with equal average capacity, computing and comparing their effective CVs to determine which actually performs better in terms of WIP/cycle time, not just average throughput.

**Use when**:
A client is choosing between equipment options with similar average capacity but different failure/repair or setup patterns, or is evaluating whether a setup-reduction or preventive-maintenance investment is worth it.

**Do not use when**:
MTTF/MTTR or setup-frequency/duration data isn't available or trustworthy — the formulas are only as good as the underlying failure/setup data; garbage in, garbage out.

**Fast retrieval query**:
`subject/machine-breakdowns` + `subject/setup-reduction` — or search "Hare X19 Tortoise 2000 CV" / "effective process time SCV formula" / "Machine 1 Machine 2 setup comparison" / "frequent short outages preferable"

## North Star Connection

- How this applies to the audit business: this page's two formulas (breakdown-CV, setup-CV) are directly client-deployable calculation tools — Chris can collect a client's MTTF/MTTR or setup-frequency/duration data and produce a rigorous, numbers-backed recommendation on equipment choice, maintenance strategy, or setup-reduction investment, going well beyond what a standard average-capacity analysis would show.
- Track relevance: Business / Systems — among the most directly client-deployable quantitative tools in the entire book so far.
- Possible future Second Brain use: Yes — strong candidate for a reusable "Effective Process-Time Variability Calculator" (Python script or spreadsheet implementing both the breakdown and setup formulas) once a client engagement with trackable equipment-failure or setup data exists.
