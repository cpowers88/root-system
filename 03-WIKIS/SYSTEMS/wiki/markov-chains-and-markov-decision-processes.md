---
domain: systems
type: framework
tags: [subject/markov-chains, subject/markov-decision-processes, subject/steady-state-probabilities, subject/operations-research]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, operations-research, ksu-support]
---

# Markov Chains and Markov Decision Processes

**Summary**: Markov chains formalize the "memoryless" state-transition process already used informally in queueing theory's birth-and-death process ([[queueing-theory-birth-death-process-and-mms-models]]) — a system that moves between states with fixed transition probabilities depending only on its current state. Steady-state probabilities describe its long-run behavior. Markov decision processes (MDP) then layer *decisions* on top: at each state, choose an action that determines both an immediate cost and the transition probabilities to the next state, and find the policy minimizing long-run average cost — directly solvable via linear programming.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 29 ("Markov Chains"), sections 29.2 and 29.5 in full (Markovian property, transition matrices, steady-state probabilities — pp. 3–19 of the chapter / physical ~1373–1392); Chapter 19 ("Markov Decision Processes"), sections 19.1–19.3 in full (the machine-maintenance prototype, the MDP model, LP formulation — physical ~908–923). Note: covered here in logical order (foundational Markov chain theory before the decision-layer extension), even though Ch. 19 precedes Ch. 29 in the book's chapter numbering.

**Last updated**: 2026-07-13**

---

## Markov Chains: The Formal Memoryless Property

A stochastic process {Xₜ} has the **Markovian property** if the conditional probability of the next state, given the entire history up to now, depends *only* on the current state — not on how the system arrived there: `P{Xₜ₊₁ = j | X₀=k₀,...,Xₜ=i} = P{Xₜ₊₁ = j | Xₜ = i}`. A process with this property is a **Markov chain**. This is the same "lack-of-memory" property already used informally in the exponential-distribution-based birth-and-death process underlying queueing theory (see [[queueing-theory-birth-death-process-and-mms-models]]) — Markov chains are the general formal theory that result.

**Transition probabilities**: `pᵢⱼ = P{Xₜ₊₁ = j | Xₜ = i}` (one-step), collected into a **transition matrix** P (row = current state, column = next state, rows sum to 1). If these probabilities don't change over time, they're **stationary**. The **n-step transition probability** `p⁽ⁿ⁾ᵢⱼ` (probability of being in state j exactly n steps after starting in state i) is obtained by repeated matrix multiplication (`P⁽ⁿ⁾ = Pⁿ`).

## Steady-State Probabilities: Long-Run Behavior

For any **irreducible ergodic** Markov chain (every state reachable from every other; no periodic cycling trap), `lim(n→∞) p⁽ⁿ⁾ᵢⱼ` exists and — critically — is **independent of the starting state i**. This limiting probability πⱼ is the **steady-state probability** of state j, found by solving the **steady-state equations**:

```
πⱼ = Σᵢ πᵢ·pᵢⱼ   for every state j     (equivalently, in matrix form: π = πP)
Σⱼ πⱼ = 1
```

**Interpretation**: πⱼ is the long-run fraction of time the system spends in state j — *not* that the system eventually "settles" into one state (it keeps transitioning forever); rather, the *probability distribution* over states converges and stays fixed. This is exactly analogous to the birth-and-death process's steady-state Pₙ probabilities (see [[queueing-theory-birth-death-process-and-mms-models]]), just for a general discrete-state Markov chain rather than the specific birth/death structure.

**Expected average cost per unit time**: if a cost C(Xₜ) is incurred whenever the system is in state Xₜ, the long-run expected average cost per period is simply `Σⱼ πⱼ·C(j)` — steady-state probabilities convert a state-dependent cost structure directly into a single long-run performance number, which is exactly the building block Markov decision processes need.

## Markov Decision Processes: Adding Decisions

An MDP layers a **decision** on top of each state observation: at every state i, choose an action k from a set of possible decisions; that choice determines (1) an immediate expected cost Cᵢₖ, and (2) the transition probabilities pᵢⱼ(k) to the next state — the decision itself reshapes the underlying Markov chain. The goal: find the **policy** (a rule specifying which decision to make in each state) that minimizes the long-run expected average cost per unit time.

**Worked example — machine maintenance**: a machine's condition is inspected weekly and classified into states (good-as-new, minor deterioration, major deterioration, inoperable — an **absorbing state** once reached, since an inoperable machine can't self-repair). Available decisions: do nothing, overhaul (available only in the major-deterioration state, resets to minor deterioration, costs $2,000 + $2,000 lost production), or replace (resets to good-as-new, costs $4,000 + $2,000 lost production). Each decision determines that state's row in the transition matrix and its immediate cost.

**Evaluating a policy**: fix a specific policy (a decision assigned to every state), solve the resulting Markov chain's steady-state equations for that policy's π values, then compute expected average cost = `Σᵢ Cᵢ,ₖ=dᵢ(R)·πᵢ`. For the machine example, comparing four candidate policies by exhaustive enumeration found the optimal one (replace only when inoperable, overhaul when majorly deteriorated) at $1,667/week — cheaper than the naive "only replace, never overhaul" policy's $1,923/week.

**Scaling beyond exhaustive enumeration — the LP formulation**: exhaustive comparison of every policy works for tiny problems but becomes infeasible once the state/decision space grows. The fix: reframe policy selection as choosing `Dᵢₖ = P{decision=k | state=i}` — a probability distribution over decisions in each state (a **randomized policy**) rather than a fixed 0/1 assignment — which makes the problem's variables continuous and lets the optimal policy be found directly via linear programming (see [[linear-programming-formulation-and-graphical-solution]] and [[simplex-method-mechanics]]), rather than by comparing every possible policy one at a time.

## Key Takeaways

- Markov chains are the general formal theory behind the memoryless assumption already used informally in queueing theory's birth-and-death process — same core property, more general application (any discrete-state system, not just queue lengths).
- Steady-state probabilities are the single most useful practical output of Markov chain analysis — they convert a state-dependent cost or performance structure directly into one long-run average number.
- MDPs are the natural extension once a decision-maker can *influence* the transition probabilities — evaluating one fixed policy is just ordinary Markov-chain steady-state analysis; finding the *best* policy is where the real problem lies.
- The randomized-policy reframing (probabilities over decisions instead of a fixed assignment) is the key trick that converts MDP policy optimization into a solvable linear program — the same pattern of relaxing a discrete structure into a continuous one seen in the assignment problem's LP relaxation (see [[transportation-and-assignment-problems]]).

## Connects to

- [[queueing-theory-birth-death-process-and-mms-models]] — the birth-and-death process is a continuous-time Markov chain; this page's discrete-time steady-state theory is the general formal foundation that specific model already relied on informally.
- [[littles-law-and-best-case-performance]] — steady-state analysis generally is the same conceptual move (converting a dynamic process into one long-run average number) used throughout this wiki's queueing and factory-physics content.
- [[linear-programming-formulation-and-graphical-solution]] — the randomized-policy LP formulation for optimal MDP policies is a direct, practical application of everything in the deterministic-OR core already ingested.
- [[decision-analysis-and-utility-theory]] — MDPs are structurally a multi-period, repeated-decision generalization of the single-shot decision problems decision analysis handles.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Repeated operational decisions with state-dependent costs (maintenance policy, inventory reorder policy, staffing policy) are a real and recognizable audit-relevant pattern |
| Current usefulness | 2 | No active engagement needs this yet |
| KSU support | 4 | Standard, real content; Markov chains specifically are foundational and referenced throughout the queueing theory material already ingested |
| Tech-stack relevance | 3 | Steady-state probabilities are a simple linear-algebra solve (Python/numpy); MDP policy optimization routes through the same LP solvers already covered |
| Business audit value | 3 | "What's your optimal maintenance/replacement policy given these state-transition probabilities and costs" is a concrete, well-defined audit deliverable for equipment-heavy clients |
| Data/workflow value | 3 | Requires transition-probability estimates (from historical state-change data) and cost-per-state-per-decision data — realistic to gather for equipment/inventory-heavy clients |
| Reading urgency | 3 | Fills a real conceptual gap (formalizes the memoryless property used informally elsewhere) and closes out the probabilistic-OR portion of this ingest |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Formalizing a repeated maintenance, replacement, or inventory-reorder decision as a Markov decision process — find the cost-minimizing policy given transition probabilities and state-dependent costs, especially once the problem is too large for manual policy-by-policy comparison (use the LP formulation).

**Use when**:
A client faces a genuinely repeated decision where the current state (equipment condition, inventory level) evolves probabilistically and the decision itself affects that evolution (maintenance choices, reorder choices).

**Do not use when**:
The decision is one-shot rather than repeated (use decision analysis instead — see [[decision-analysis-and-utility-theory]]), or the system's future genuinely depends on more than just its current state (the Markovian property doesn't hold, and the state definition needs to be expanded or a different technique used).

**Fast retrieval query**:
`subject/markov-chains` + `subject/markov-decision-processes` — or search "steady-state equations transition matrix" / "Markovian property lack of memory" / "randomized policy linear programming" / "expected average cost per unit time"

## North Star Connection

- How this applies to the audit business: equipment maintenance/replacement policy and inventory reorder policy are both natural MDP-shaped questions for equipment- or inventory-heavy SMB clients — "here's your cost-minimizing policy, backed by your own historical transition data" is a concrete, quantified deliverable.
- Track relevance: Systems / KSU — genuinely foundational (the formal basis for the memoryless assumption used throughout the queueing material) and real audit application via the maintenance-policy pattern.
- Possible future Second Brain use: Yes — a steady-state-probability calculator plus a simple MDP-policy-comparison template (Python) is a reasonably fast capability-library candidate for equipment-heavy client engagements.
