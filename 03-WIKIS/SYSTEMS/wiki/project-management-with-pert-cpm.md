---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/project-management, subject/critical-path-method, subject/pert, subject/operations-research]
---

# Project Management with PERT/CPM: Critical Path, Slack, Uncertainty, and Time-Cost Trade-offs

**Summary**: The standard framework for scheduling a project made of interdependent activities — find the critical path (the longest route through the project network, which sets the minimum possible project duration), compute slack for every other activity (how much delay each can absorb without affecting the deadline), extend the model to handle uncertain activity durations (PERT's three-estimate approach), and decide where to spend money "crashing" (accelerating) activities to hit an aggressive deadline.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 22 ("Project Management with PERT/CPM"), sections 22.3–22.4 in full (critical path method, PERT probabilistic durations — pp. 22-5 to 22-19 of the chapter / physical ~1130–1150); section 22.5 (time-cost trade-offs / crashing) at conceptual level with real cost-data example — physical ~1160

**Last updated**: 2026-07-13**

---

## The Project Network and the Critical Path

A project is modeled as a network of activities with **precedence relationships** (which activities must finish before others can start) and estimated durations. A **path** through the network is a sequence of activities from START to FINISH; its length is the sum of its activities' durations.

**The critical path is the *longest* path through the network — and the project's minimum possible duration equals this path's length**, not the sum of all activities' durations (since many activities run in parallel) and not the length of just any path (since a path's activities may have to wait on predecessors *not* on that path). The Reliable Construction Co. example (14 activities, 6 possible paths ranging 31–44 weeks) has an estimated project duration of 44 weeks — set entirely by its one critical path.

## The Forward and Backward Pass: Finding Every Activity's Timing Window

**Forward pass** (compute earliest possible timing, working start-to-finish): `ES = largest EF among all immediate predecessors` (an activity can't start until *every* predecessor is done, not just one); `EF = ES + duration`. Applied all the way to FINISH, this yields the project's earliest completion time (the critical path length).

**Backward pass** (compute latest allowable timing without delaying the project, working finish-to-start): `LF = smallest LS among all immediate successors` (an activity must finish in time for *every* successor's latest start, not just one); `LS = LF − duration`.

**Slack** = `LF − EF` (equivalently `LS − ES`) — how much an activity's start/finish can slip without delaying the whole project. **Every activity with zero slack lies on the critical path** — this is both the formal definition of "critical" and a mechanical way to *find* the critical path for large networks (rather than enumerating every path and comparing lengths, which doesn't scale).

**Practical output**: the earliest-time schedule (ES/EF) is normally used to set the initial plan, since it preserves slack as a buffer against surprises; the latest-time schedule (LS/LF) is the "last chance" fallback showing how much room remains before a delay becomes fatal — and it directly tells the project manager exactly where to focus monitoring attention (the zero-slack critical activities) versus where some schedule slippage is tolerable (positive-slack activities).

## PERT: Handling Uncertain Activity Durations

CPM's forward/backward pass assumes every duration is a known constant. **PERT's three-estimate approach** captures genuine uncertainty per activity: optimistic (o), most likely (m), and pessimistic (p) time estimates, combined (assuming a **beta distribution** shape) into:

```
mean:     μ = (o + 4m + p) / 6
variance: σ² = ((p − o) / 6)²
```

**Three simplifying approximations** turn per-activity uncertainty into a project-level probability distribution, avoiding the need to consider all possible paths under all possible duration combinations:

1. **Assume the "mean critical path"** (the path that's critical when every activity takes its mean duration) **is also the longest path** under real variability — only approximately true, but the true longest path is rarely much longer when it fails.
2. **Assume the critical-path activities' durations are statistically independent**, so their variances simply *add*: `σ²ₚ = Σ (variance of each critical-path activity)`.
3. **Assume the resulting project-duration distribution is approximately normal** (justified by the Central Limit Theorem once the critical path has enough activities, roughly 5+) — with mean `μₚ = Σ(critical-path activity means)` and the summed variance from step 2.

This turns "what's the probability of finishing by the deadline" into a simple normal-distribution calculation once μₚ and σ²ₚ are known — directly answering a project sponsor's most pressing question (Reliable's example: μₚ=44 weeks, σ²ₚ=9, against a 47-week deadline with a $300,000 late penalty).

## Time-Cost Trade-offs: Crashing

Every activity has a **normal time/cost** and a **crash time/cost** (the fastest achievable duration, at higher cost — overtime, extra crews, expedited materials) — the **crash cost per week saved** is the marginal price of accelerating that specific activity. **The key insight for deciding where to spend crashing money**: accelerating a *non-critical* activity (one with slack) does nothing for the project deadline — only crashing activities on the (current) critical path shortens the project, and once enough crashing happens, a *different* path can become the new critical path, requiring a shift in crashing focus. This makes the crashing decision itself an optimization problem (commonly solved via LP or a marginal-cost-based iterative procedure) — spend crash dollars on whichever critical-path activity has the *cheapest* cost-per-week-saved, re-identify the critical path after each acceleration, and repeat.

## Key Takeaways

- The critical path — not total activity-time or any arbitrary path — sets the minimum achievable project duration; everything else in PERT/CPM (slack, PERT's probability calculation, crashing decisions) is built around correctly identifying it.
- Slack = LF − EF is simultaneously the formal definition of the critical path (zero slack) and the practical answer to "where can I afford some schedule risk."
- PERT's three simplifying approximations convert individually-uncertain activity durations into one clean, directly answerable question ("probability of meeting the deadline") — at the cost of some approximation error that's usually small in practice.
- Crashing money is only well-spent on current critical-path activities, and the critical path itself can shift as crashing proceeds — a static "which activities to crash" list isn't enough; the critical path needs re-checking after each acceleration.

## Connects to

- [[network-optimization-models]] — the project network's forward/backward pass is structurally a longest-path calculation (the mirror image of the shortest-path algorithm already covered).
- [[decision-analysis-and-utility-theory]] — the PERT probability-of-meeting-deadline calculation is the same normal-distribution/CLT reasoning used elsewhere in probabilistic OR.
- [[linear-programming-formulation-and-graphical-solution]] — the crashing decision (which activities to accelerate, by how much, at minimum total cost) is directly formulable and solvable as an LP.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Project scheduling is one of the most universally recognizable, immediately applicable OR techniques for any client running multi-step engagements (construction, IT implementation, any complex deliverable) |
| Current usefulness | 4 | Directly usable for managing Chris's own multi-step projects, not just client work |
| KSU support | 5 | Standard, essentially universal intro-OR/ISYE content — one of the most practically ubiquitous techniques in the entire curriculum |
| Tech-stack relevance | 4 | Directly implementable via Python (networkx for the critical path calc) or standard project-management software (MS Project, even a well-built spreadsheet) |
| Business audit value | 5 | "Here's your critical path, here's where you have schedule slack, here's your probability of hitting the deadline, here's where to spend money to accelerate" is an extremely concrete, universally applicable client deliverable |
| Data/workflow value | 4 | Requires activity list, durations (or three-point estimates), and precedence relationships — straightforward to gather from any client running a defined project |
| Reading urgency | 5 | High-value, broadly applicable, closes a real gap — this is arguably the single most universally practical technique in the entire OR ingest |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Building a project schedule for any client (or internal) multi-activity project — identify the critical path, communicate slack to set monitoring priorities, use PERT's three-estimate approach when durations are genuinely uncertain, and use crashing analysis when facing a deadline that requires accelerating specific activities.

**Use when**:
Any project has multiple interdependent activities with meaningful precedence constraints — construction, software rollout, any multi-phase client engagement, or Chris's own multi-step work.

**Do not use when**:
Activities are essentially independent with no meaningful precedence structure (then it's not really a scheduling problem) or the project is simple enough (a handful of sequential steps) that formal network analysis adds more overhead than insight.

**Fast retrieval query**:
`subject/project-management` + `subject/critical-path-method` + `subject/pert` — or search "forward pass backward pass slack" / "critical path longest path" / "PERT three estimate beta distribution" / "crashing time-cost trade-off"

## North Star Connection

- How this applies to the audit business: PERT/CPM is probably the single most universally recognizable and immediately deployable OR technique for any client running a defined project — a critical-path analysis with slack and a deadline-probability estimate is a concrete, easy-to-explain, high-credibility deliverable that doesn't require the client to understand any underlying math.
- Track relevance: Systems / KSU / Business — extremely high across all three; this is core, practical, universally applicable material.
- Possible future Second Brain use: Yes, high priority — a `networkx`-based critical-path/slack calculator (plus PERT probability and basic crashing analysis) is one of the strongest, most broadly reusable capability-library candidates from this entire OR ingest.
