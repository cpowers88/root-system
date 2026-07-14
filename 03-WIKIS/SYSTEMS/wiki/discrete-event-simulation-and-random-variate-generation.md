---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/simulation, subject/discrete-event-simulation, subject/random-variate-generation, subject/operations-research]
---

# Discrete-Event Simulation and Random Variate Generation

**Summary**: When a stochastic system is too complex for a closed-form model (queueing theory, decision analysis) to handle analytically, simulation imitates the system's behavior directly — repeatedly generating random events according to known probability distributions and tracking what happens. Covers when simulation is (and isn't) the right tool, discrete-event vs. continuous simulation, and the core toolkit for turning uniform random numbers into random observations from any target distribution (inverse transformation, acceptance-rejection).

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 20 ("Simulation"), sections 20.1 and 20.4 in full (core methodology — pp. 892–917 printed / physical ~924–949); sections 20.2, 20.3, 20.5–20.6 (random number generators, output-data analysis, spreadsheet/ASPE mechanics) at conceptual level only — this is a 176-page chapter, and the remainder is largely repeated worked examples applying the same core methodology across different business scenarios, not new technique. Chunked deliberately shallow past the core methodology; flag for a deeper pass only if a specific simulation build is underway.

**Last updated**: 2026-07-13

---

## When Simulation Is (and Isn't) the Right Tool

Simulation is expensive: building the model, validating it, running many long computer replications, and carefully analyzing noisy output all take real time and effort. **The rule**: use simulation only when the stochastic system is too complex for a closed-form mathematical model (queueing theory, decision analysis, etc.) to handle satisfactorily. A closed-form model, when one is available, is almost always superior — it abstracts the problem's structure and directly reveals cause-and-effect relationships, rather than just producing numeric output. Simulation is the fallback for complexity that defeats analytical modeling, not a default first choice.

**Discrete-event vs. continuous simulation**: a **discrete-event simulation** changes the system's state instantaneously at random points in time as specific events occur (e.g., a customer arrival or service completion in a queueing system) — this covers the large majority of practical OR simulation applications, including all of this chapter's coverage. A **continuous simulation** changes state continuously over time (e.g., an aircraft's position during flight), typically requiring differential equations and materially more complex analysis. Continuous systems can often be approximated as discrete-event simulations by treating continuous change as frequent small discrete jumps — a common practical simplification.

## The Core Loop: Generate Random Numbers → Convert to Random Observations

Every simulation reduces to the same two-layer mechanism:

1. **Generate uniform random numbers** — random observations from a continuous uniform distribution on [0,1]. In practice these come from a **pseudo-random number generator** (a deterministic algorithm, e.g. a congruential method, that produces a sequence *statistically indistinguishable* from true randomness) rather than genuine randomness — reproducibility for testing/debugging is actually a feature, not a limitation.
2. **Convert uniform random numbers into random observations from the distribution the model actually needs** (coin flips, dice, exponential service times, normal demand, etc.) — via one of the methods below.

## Converting Uniform Random Numbers to Any Distribution

- **Simple discrete distributions**: allocate ranges of the uniform random number in direct proportion to each outcome's probability (e.g., 0.0–0.4999 = heads, 0.5000–0.9999 = tails for a fair coin; a lookup table for dice-throw probabilities).
- **The inverse transformation method** (the general-purpose technique): given cumulative distribution function F(x), generate a uniform random number r, then solve `F(x) = r` for x — that x is the desired random observation. For discrete distributions, this is implemented as a table lookup (Excel's `VLOOKUP` against a cumulative-probability table is the standard spreadsheet approach). For continuous distributions, it requires solving F(x)=r analytically:
  - **Exponential distribution**: F(x) = 1 − e^(−αx) inverts cleanly to `x = −ln(r)/α` — the standard, simplest way to generate exponential service/interarrival times for a queueing simulation (directly connects to [[queueing-theory-birth-death-process-and-mms-models]]).
  - **Erlang distribution**: sum of k independent exponentials — generated directly from k uniform random numbers via `x = −(1/kα)·ln(r1·r2···rk)`.
  - **Normal distribution**: an approximate method exploits the Central Limit Theorem (summing n uniform random numbers approximates a normal distribution — good even for small n=5–10, and n=12 conveniently eliminates a square-root term); exact, faster methods exist and are what real software actually uses (e.g. Excel's `NORMINV(RAND(), μ, σ)`).
  - **Chi-square distribution**: sum of squares of n standard-normal random observations.
- **The acceptance-rejection method** — for distributions where inverting F(x) isn't computationally feasible: generate a candidate x uniformly over its possible range, then accept it with probability proportional to its actual target density f(x) (generate a second uniform random number and accept iff it's ≤ f(x)/L, where L bounds f(x)'s maximum); reject and retry otherwise. This produces valid draws from f(x) without ever needing to invert it — at the cost of occasionally wasting a draw.

## Key Takeaways

- Simulation is a *fallback* tool for complexity that defeats closed-form models, not a first-choice default — always check whether a queueing/decision-analysis/LP model can handle the problem analytically first.
- The entire simulation machinery reduces to one core primitive (generate a uniform random number) plus a small toolkit for converting that primitive into observations from whatever distribution the real system actually needs.
- The inverse transformation method is the default, general-purpose technique; acceptance-rejection is the fallback when inversion isn't computationally tractable.
- Discrete-event simulation covers the vast majority of practical OR applications — continuous simulation (differential-equation-driven) is a specialized, harder case mostly reserved for physical/engineering systems.

## Connects to

- [[queueing-theory-birth-death-process-and-mms-models]] — simulation is the practical fallback when a queueing system is too complex for the exact M/M/s-style closed-form models (non-exponential distributions, multiple interacting queues, complex routing).
- [[decision-analysis-and-utility-theory]] — simulation can evaluate complex multi-stage decision problems too tangled for a tractable decision tree.
- [[sensitivity-analysis-and-postoptimality]] — the same "how much can this estimate be wrong" discipline applies to simulation output (running multiple replications, checking result stability) as to LP parameters.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Simulation is directly named in this wiki's own charter as part of the ISYE spine, and is genuinely one of the most flexible, broadly-applicable audit tools when a client's process is too tangled for a closed-form model |
| Current usefulness | 3 | No active engagement needs simulation yet, though it's the natural next step whenever a client process is too complex for queueing/LP models directly |
| KSU support | 5 | Standard, heavily-tested intro-OR chapter; explicitly named in this wiki's charter |
| Tech-stack relevance | 4 | The full toolkit (random number generation, inverse transformation, acceptance-rejection) is directly and easily implementable in Python (`numpy.random`, `scipy.stats`) — genuinely fast to build a working audit simulation |
| Business audit value | 4 | Simulation is the tool of last resort but broadest applicability — when a client's real process is too messy for a closed-form model, this is what still works |
| Data/workflow value | 3 | Requires distributional estimates (arrival patterns, service times, demand) for each random component being modeled |
| Reading urgency | 4 | Third of the "chunk 2" probabilistic-OR pages — deliberately shallow given the chapter's 176-page size; the remainder is repeated worked examples, not new methodology |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Modeling a client process too complex for closed-form queueing/decision-analysis/LP models — multiple interacting queues, non-exponential distributions, complex routing/scheduling logic — by directly imitating its random behavior over many simulated runs.

**Use when**:
A closed-form model has been ruled out as insufficient for the complexity involved (check queueing theory, decision analysis, and LP first — simulation is the fallback, not the default).

**Do not use when**:
A closed-form analytical model is available and adequate — it's cheaper to build, faster to run, and directly reveals cause-and-effect structure that raw simulation output doesn't.

**Fast retrieval query**:
`subject/simulation` + `subject/random-variate-generation` — or search "discrete-event simulation" / "inverse transformation method" / "acceptance-rejection method" / "uniform random number"

## North Star Connection

- How this applies to the audit business: simulation is the broadest-applicability tool in the whole OR toolkit — when a client's process is too tangled for a clean queueing or LP model (multiple interacting bottlenecks, irregular arrival patterns, complex routing), a simulation built in Python is still buildable and still gives a defensible, testable answer.
- Track relevance: Systems / KSU — core, testable content, explicitly named in this wiki's own charter.
- Possible future Second Brain use: Yes — a small Python simulation toolkit (random-variate generators for common distributions, a basic discrete-event loop) is a strong, broadly reusable capability-library candidate.
