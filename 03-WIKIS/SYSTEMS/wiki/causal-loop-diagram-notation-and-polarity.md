---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/client-interview, use-case/audit, subject/system-dynamics, subject/causal-loop-diagrams, subject/feedback-loops]
---

# Causal Loop Diagram Notation: Link Polarity, the Stock/Flow Trap, and the s/o Debate

**Summary**: The formal notation for causal loop diagrams (CLDs) — link polarity, loop identifiers — with the single most common error CLDs invite: confusing a link's polarity (a structural, ceteris-paribus statement about direction of influence) with the actual behavior of a stock, which depends on net flow, not on any one link's sign.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 5 ("Causal Loop Diagrams"), section 5.1

**Last updated**: 2026-06-22

---

## The Notation: Links, Polarity, Loop Identifiers

A causal loop diagram is variables connected by arrows (causal links), each link assigned a polarity (+ or -), with important loops marked by a loop identifier circulating in the same direction as the loop (clockwise loop → clockwise identifier) and labeled positive/reinforcing (R) or negative/balancing (B).

**Precise definitions** (Table 5-1 in the source — worth quoting exactly, since informal restatements routinely get this wrong):
- **Positive link** (X → Y, +): if X increases, Y increases *above what it otherwise would have been*; if X decreases, Y decreases below what it otherwise would have been. In accumulation terms: X *adds to* Y.
- **Negative link** (X → Y, -): if X increases, Y decreases below what it otherwise would have been; if X decreases, Y increases above what it otherwise would have been. In accumulation terms: X *subtracts from* Y.

## The Critical Caveat: Polarity Describes Structure, Not Actual Behavior

**This is the chapter's single most important — and most frequently violated — distinction.** Link polarity is a **conditional, ceteris-paribus statement**: it tells you what *would* happen to Y if X changed and nothing else did. **It does not tell you what will actually happen**, for two reasons:

1. **Most variables have multiple inputs.** A birth rate depends on both the fractional birth rate *and* population size — you cannot say whether an increase in the fractional birth rate will actually raise the birth rate without also knowing what population is doing. Assessing one link's polarity always assumes all other variables held constant; assessing actual system behavior requires considering all inputs simultaneously, which is exactly why simulation (not diagram-reading alone) is usually needed to determine which loops actually dominate.

2. **CLDs don't distinguish stocks from flows** (covered fully in Chapter 6). This produces a specific, easy-to-make mistake: population is a *stock*, increased by the birth rate and decreased by the death rate. A positive link from births to population means **births add to population — not that population rises when births rise**. A decrease in the birth rate does **not** decrease the population (births can only increase it, never reduce it) — it just means population is *higher than it otherwise would have been*, even while net population could still be falling if deaths exceed births. **The precise, source-quoted rule**: "It is always true... that if the birth rate rises, population will rise above what it would have been in the absence of the change in births, even if the population continues to fall." Knowing whether a stock is actually rising or falling requires knowing its *net* rate of change (inflow minus outflow), not any single link's polarity in isolation.

**Why this matters for audit work**: a causal diagram showing "more sales calls → more sales" (+) does not mean sales are necessarily growing — if customer churn (a competing outflow) is rising faster, the sales stock can still be shrinking even as that one link's effect is genuinely positive. **Reading a CLD's polarities is not the same as reading its behavior** — a distinction worth stating explicitly to a client team the first time they see a diagram, to prevent the common misreading.

## The s/o Notation Debate (and Why This Book Rejects It)

An alternate convention (popular in the "systems thinking" tradition — Senge, Kim) uses **s** ("X and Y move in the **s**ame direction") and **o** ("X and Y move in **o**pposite directions") instead of +/-. Sterman explicitly rejects this notation, citing Richardson (1997)'s argument: **"X and Y move in the same direction" is not generally a correct statement** — it conflates the *ceteris paribus* structural claim with an actual-behavior claim, exactly the error the polarity caveat above is designed to prevent. The s/o convention also breaks down entirely for stock-flow relationships: "births and population do not move in the same direction" in the relevant sense — a falling birth rate doesn't cause population to fall, since births are a pure inflow. **Sterman's recommendation, and this wiki's adopted convention going forward**: use +/- notation exclusively, while still being able to read s/o notation when encountered in other sources, since "s"/"o" remain common in some systems-thinking literature (Peter Senge's *The Fifth Discipline* tradition).

## Connects to

- [[policy-resistance-and-feedback-thinking]] — this chapter formalizes the loop-type vocabulary (positive/negative, reinforcing/balancing) introduced informally in Chapter 1 into precise, diagrammable notation.
- [[fundamental-modes-growth-goal-seeking-oscillation]] — the loop-polarity rules here are the formal underpinning for that chapter's structure-to-behavior heuristic (you need correct polarity assignment to correctly diagnose which structure is dominant).
- [[causal-loop-diagram-guidelines]] — the companion page covering the chapter's full set of diagramming guidelines (loop-polarity determination methods, naming conventions, layout, aggregation level).

## North Star Connection

- How this applies to the audit business: the polarity-vs-behavior distinction is essential to get right before presenting any causal diagram to a client — a client team will naturally (and incorrectly) read "+" as "this thing is going up," and a single sentence of correction up front ("this shows direction of influence, not what's actually happening") prevents a major misunderstanding mid-presentation.
- Track relevance: Systems — foundational notation for any future causal-diagramming work, whether in client workshops or personal modeling.
- Possible future Second Brain use: a one-page "how to read a causal loop diagram" client handout, built directly from this page's polarity definitions and caveat, is a strong candidate deliverable for any engagement that uses CLDs.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | Essential prerequisite for any future causal-diagramming work with clients |
| Current usefulness | 3 | Useful once CLDs are actually being drawn in an engagement; less immediately actionable than the case-study pages |
| KSU support | 5 | Canonical, precise system dynamics notation |
| Tech-stack relevance | 2 | Could underpin a simple diagramming tool, but primarily conceptual |
| Business audit value | 3 | Important for correct client communication, but a supporting tool rather than a standalone audit insight |
| Data/workflow value | 1 | Notation, not a data method |
| Reading urgency | 3 | Necessary foundation before the chapter's much higher-value case studies |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Reference for correctly drawing and presenting causal loop diagrams — especially the polarity-vs-behavior caveat, which should be stated explicitly the first time a CLD is shown to any client audience.

**Use when**:
Drawing a causal loop diagram for a client or sketching one informally during discovery, especially involving any stock-and-flow relationship (most business variables).

**Do not use when**:
A quick verbal explanation of cause-and-effect suffices and no diagram is actually being drawn — the formal notation isn't necessary for casual discussion.

**Fast retrieval query**:
`subject/causal-loop-diagrams` — or search "link polarity ceteris paribus" / "births do not decrease population" / "s and o notation causal diagrams"
