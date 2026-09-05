---
domain: systems
type: framework
tags: [subject/system-dynamics, subject/stocks-and-flows]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, audit, data-workflow]
---

# Stock and Flow Fundamentals: Notation, Math, and Why Stocks Drive Dynamics

**Summary**: The formal definition of stocks (accumulations) and flows (rates of change), the standard diagramming notation (rectangles/pipes/valves/clouds) and its exact mathematical equivalence to integral/differential equations, and the four distinct reasons stocks — not just feedback loops — are essential to generating a system's dynamics.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 6 ("Stocks and Flows"), section 6.1

**Last updated**: 2026-06-22

---

## Why Causal Loop Diagrams Aren't Enough

Causal loop diagrams (see [[causal-loop-diagram-notation-and-polarity]]) capture feedback structure but cannot represent the stock-and-flow distinction — and this is treated as one of CLDs' most important limitations, not a minor gap. **Stocks and flows, alongside feedback, are the two foundational concepts of dynamic systems theory.** A concrete illustration of the real-world cost of confusing them: many people, "including politicians responsible for fiscal policy," are unclear on whether the federal deficit is a stock or a flow (it's a flow — the annual gap between spending and revenue — while the accumulated national *debt* is the stock) — and this confusion routinely produces underestimated time delays, short-term thinking, and policy resistance in actual fiscal debate.

## Notation: Rectangles, Pipes, Valves, Clouds

- **Stocks** = rectangles (a container holding the stock's contents).
- **Inflows/outflows** = pipes (arrows) with **valves** controlling the rate of flow.
- **Clouds** = sources and sinks — stocks *outside* the model boundary, assumed to have **infinite capacity** and therefore never able to constrain the flows they support. Drawing a cloud is an explicit boundary decision, covered fully in [[aggregation-and-challenging-the-clouds]].

## Mathematical Equivalence: Four Identical Representations

The bathtub metaphor, the stock-flow diagram, the integral equation, and the differential equation are **four exactly equivalent representations containing precisely the same information** — none is more or less rigorous than the others, just more or less convenient for a given audience:

- **Integral form**: Stock(t) = ∫[Inflow(s) − Outflow(s)]ds from t₀ to t, plus Stock(t₀)
- **Differential form**: d(Stock)/dt = Inflow(t) − Outflow(t)
- **INTEGRAL() function notation** (the book's preferred shorthand): Stock = INTEGRAL(Inflow − Outflow, Stock_t₀)

You can mechanically generate any one of these four from any other — there is no information loss or gain in choosing one representation over another, only a difference in what's easiest for a given audience to read (covered fully in [[identifying-stocks-flows-and-state-determined-systems]]'s discussion of presentation choices).

## Four Distinct Reasons Stocks Generate Dynamics (Mass 1980)

This is the chapter's core theoretical claim — stocks are not just bookkeeping, they are a primary *cause* of dynamic behavior, for four separable reasons:

1. **Stocks characterize system state and provide the basis for decisions.** A pilot needs altitude, fuel, heading; a firm needs backlog, inventory, labor stock — without these states, decision-makers are "flying blind." A balance sheet is precisely a snapshot of a firm's financial stocks.

2. **Stocks provide inertia and memory.** A stock's content persists until an inflow or outflow explicitly changes it — meaning past events leave a durable trace that doesn't fade just because circumstances have changed. **The lead-paint example makes this concrete and consequential**: lead paint was banned in 1978, but the *stock* of lead already in inner-city housing remains today, and the only ways to reduce it are expensive deleading or eventual demolition — banning the *inflow* (production) does nothing to the existing *stock*. The same structural point applies to atmospheric CFC-derived chlorine (will persist for decades after production stops, since the stratospheric scrubbing rate is slow) and to **intangible stocks**: beliefs and memories persist with their own inertia — a single bad experience with an airline can leave a belief about their quality that outlasts genuine service improvements by years.

3. **Stocks are the source of all delays.** Every delay, without exception, involves a stock accumulating the gap between an input and a lagging output — a letter "in transit" is a stock; a building under construction is a stock; even the manager's belief about a current shipment rate is a (mental) stock, since measuring any *rate* itself requires accumulating events over some interval and is therefore inherently delayed (instantaneous flow values are never directly observable — see [[identifying-stocks-flows-and-state-determined-systems]]). **The mailed-wedding-invitations example crystallizes the mechanism**: mailing 1,000 invitations at once doesn't change the delivery rate immediately — the stock of "letters in transit" jumps by 1,000 and only gradually drains as deliveries exceed the (separately determined) ongoing mailing rate, with the stock returning to its prior baseline only once the entire batch has cleared.

4. **Stocks decouple flow rates and create disequilibrium.** Because inflows and outflows to a stock are usually governed by *different* decision processes (production planning vs. consumer demand; hiring vs. quitting), they will generally differ — and the stock is exactly what absorbs that difference, permitting disequilibrium to exist at all. **Joseph's advice to Pharaoh** (stockpile grain during the seven good years to survive the seven lean years) is the chapter's biblical-vintage illustration: without a buffering stock, consumption would have to equal production at every instant, and people would starve between harvests. **The general lesson for any client-system diagnosis**: whenever two coupled activities are run by different decision-makers with different information and different shocks, *some* stock must exist between them to absorb the gap — and whether that stock's level stabilizes is never something you can simply assume; it's an emergent property of however the surrounding feedback loops happen to interact, which is frequently the actual question a model exists to answer.

## Connects to

- [[causal-loop-diagram-notation-and-polarity]] — this chapter's stock/flow notation directly resolves the specific limitation flagged there (CLDs can't distinguish "X adds to Y" from "X and Y move together").
- [[identifying-stocks-flows-and-state-determined-systems]] — the companion page covering how to actually identify stocks vs. flows in a real system, units-of-measure discipline, and the "stocks change only through rates" diagramming rule.
- [[barriers-to-learning-and-virtual-worlds]] — the "instantaneous flow values are never observable" point (developed fully in the companion page) is a direct, formal extension of that chapter's limited-information barrier (1.3.2).
- [[fundamental-modes-growth-goal-seeking-oscillation]] — stocks decoupling flow rates (#4 above) is the structural mechanism underlying every oscillation example in that chapter; the delay-creating property (#3) is the literal mechanism behind the oscillation mode itself.

## North Star Connection

- How this applies to the audit business: reason #2 (stocks as inertia) is a sharp, generally applicable audit insight — a client who stops a bad practice ("we banned X going forward") has only changed an *inflow*; the *stock* of accumulated consequence (debt, deferred maintenance, damaged reputation, outdated skills in the workforce) persists and requires separate, deliberate action to actually reduce. Reason #4 (stocks as disequilibrium buffers) directly explains why any client with two departments running on different decision cycles (sales forecasting vs. production scheduling) will always carry some buffer stock, and why that buffer's stability is never something to assume.
- Track relevance: Systems / Business — foundational for every future stock-flow mapping exercise, and a directly client-usable distinction (stopping a bad inflow ≠ fixing the accumulated stock).
- Possible future Second Brain use: a "stock vs. flow audit" checklist (for every client metric discussed, is this a stock or a flow, and does the client's proposed fix target the right one) is a strong candidate discovery-phase tool.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | "Stopping the inflow doesn't fix the stock" is a directly client-usable, broadly applicable diagnostic distinction |
| Current usefulness | 5 | Immediately applicable to nearly any client conversation involving inventory, backlog, debt, reputation, or skill levels |
| KSU support | 5 | Canonical, foundational system dynamics content |
| Tech-stack relevance | 2 | Directly underlies spreadsheet/simulation modeling of any accumulation process |
| Business audit value | 5 | The lead-paint/CFC framing (stopping production ≠ eliminating the accumulated harm) is a sharp, transferable client argument |
| Data/workflow value | 4 | Directly informs how to structure any client data model involving accumulations |
| Reading urgency | 5 | Foundational prerequisite for all subsequent stock-flow modeling work in the book |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Discovery-phase clarifying question — for any client metric under discussion, explicitly ask whether it's a stock or a flow, and if a proposed fix targets only the inflow, ask whether the existing stock (debt, backlog, deferred maintenance, damaged reputation) also needs separate, deliberate action.

**Use when**:
A client describes having "already fixed" a problem by stopping a bad practice, but the consequence (cost, reputation damage, accumulated risk) appears to be persisting.

**Do not use when**:
The system genuinely has no meaningful accumulation — a true one-time, non-recurring event has no stock to analyze.

**Fast retrieval query**:
`subject/stocks-and-flows` — or search "lead paint stock inertia" / "Joseph Pharaoh seven lean years" / "wedding invitations letters in transit" / "INTEGRAL function stock"
