---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/audit, use-case/data-workflow, subject/system-dynamics, subject/stocks-and-flows, subject/calculus-without-math]
---

# Graphical Integration and Differentiation: Calculus Without the Math

**Summary**: How to infer a stock's behavior from a graph of its net flow (graphical integration) and infer a flow's behavior from a graph of the stock (graphical differentiation) — purely visually, with no calculus required. Includes the worked phase-lag example showing accumulation itself creates a precise quarter-cycle delay between a fluctuating inflow and the resulting stock.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 7 ("Dynamics of Stocks and Flows"), section 7.1

**Last updated**: 2026-06-22

---

## Static vs. Dynamic Equilibrium

A stock is in equilibrium when its net rate of change is zero (inflow exactly balances outflow) — but this comes in two distinct flavors worth keeping separate. **Dynamic equilibrium**: flows continue, but they net to zero, so the stock's *content* keeps turning over even though its *level* stays constant (the US Senate has held exactly 100 seats since 1959, even as individual senators continuously come and go). **Static equilibrium**: both flows are literally zero, so not only is the stock's level constant, its actual contents never change at all (the stock of known Bach cantatas — we're not going to lose the known ones, and new discoveries are vanishingly unlikely, and Bach obviously can't write more). **The distinction matters for any audit context**: a client metric that "looks stable" needs the follow-up question of *which* kind of stability it is — a workforce headcount that's constant because turnover exactly offsets hiring is a fundamentally different (and differently risky) situation than a workforce that's constant because literally nobody has left or joined.

## Graphical Integration: The Core Technique

**The central, calculus-free insight**: the amount added to a stock during any interval equals **the area under the net-rate curve** for that interval. This is intuitively just "rate × time" applied to a curve instead of a constant: divide the interval into small enough segments that the rate is roughly constant within each one, multiply each segment's rate by its duration to get a small rectangle of area, and sum the rectangles — exactly the logic underlying numerical simulation itself (Euler integration), just done by eye on a graph rather than by a computer.

**The eight-step procedure** (Table 7-2 in the source), usable on any stock-flow system without writing a single equation:

1. Graph total inflow and total outflow separately.
2. Calculate and graph the *net* rate (inflow − outflow).
3. Set up a separate stock graph beneath the flow graph, with aligned time axes (different units require different scales).
4. Plot the stock's known *initial* value — this can never be inferred from the flow graph alone, it must be given.
5. Break the net-rate curve into segments of similar behavior (constant, linearly rising, etc.) and compute the area (added/subtracted quantity) for each segment in turn, building the stock's value segment by segment.
6. For each segment, determine the *direction and curvature* of the stock's trajectory from the sign and trend of the net rate: positive-and-rising net rate → stock accelerating upward; positive-and-falling → stock still rising but decelerating; negative-and-growing-more-negative → stock falling at an increasing rate; negative-and-shrinking-toward-zero → stock falling at a decreasing rate.
7. Wherever net rate is exactly zero, the stock is momentarily flat — and a sign change in the net rate marks a literal maximum (positive-to-negative) or minimum (negative-to-positive) in the stock's trajectory.
8. Repeat across all segments until the full stock trajectory is sketched.

**The step-pulse worked example makes the core lesson vivid**: an inflow that jumps to 20 units/second for exactly 10 seconds, then drops back to zero, produces a stock that rises by 200 units during the pulse and then **stays at that new, higher level permanently** — it does not return to its starting value just because the rate returned to its starting value. **"Stocks provide a memory of all past events"** is the chapter's explicit statement of this — and it's the same mechanism already encountered as reason #2 in [[stock-flow-fundamentals-and-notation]] (inertia/memory), now demonstrated mechanically rather than just asserted. A further detail worth keeping: **accumulation changes the shape of its input** — a rectangular pulse with two sharp discontinuities produces a smooth, continuous output curve (a ramp up, then flat), because integration is inherently a smoothing operation.

## The Phase-Lag Result: Accumulation Itself Creates a Precise Delay

**The chapter's sharpest, most quotable worked result**: a constant outflow (100 units/month) paired with an inflow that oscillates sinusoidally around the same average (±50 units/month, 12-month period) produces a stock that **also oscillates with the same 12-month period and a fixed amplitude — but lagging the inflow's peak by exactly one-quarter cycle (3 months).** This isn't a coincidence of the specific numbers chosen — it's provable directly from calculus (integrating a cosine produces a sine, and sin(θ) = cos(θ − π/2), a precise quarter-cycle/90° phase lag) and it generalizes: **any pure accumulation process, with no additional dynamics, imposes a quarter-cycle lag between a sinusoidal driving flow and the resulting stock.** The amplitude of the resulting stock fluctuation also has a precise, computable relationship to the input amplitude and period (amplitude scales by period/2π) — meaning a slower-oscillating input produces a *larger* swing in the stock, not just a more delayed one.

**Why this matters beyond the math**: this is a clean, derivable instance of [[fundamental-modes-growth-goal-seeking-oscillation]]'s oscillation mode — but it shows the delay arising from pure accumulation alone, with *no feedback loop at all* in this particular example. **The lesson for diagnosing any client system**: a lag between a driving input and an observed output doesn't automatically mean there's a complicated feedback structure to find — sometimes the lag is simply the unavoidable mathematical signature of accumulation itself, and the right diagnostic question is "how much of this delay is just the stock filling/draining, versus how much is an additional feedback-driven delay layered on top?"

## Graphical Differentiation: Reading the Flow from the Stock's Slope

The inverse operation: given the stock's trajectory, the net rate at any point is simply the **slope of a line tangent to the stock curve at that point.** A stock falling linearly has a constant negative net rate (the slope); a stock rising at a decreasing rate (concave down) has a positive but falling net rate; a sudden kink in the stock's trajectory (an instantaneous change in slope) corresponds to an instantaneous step-change in the net rate.

**An important limitation worth flagging explicitly**: graphical differentiation only ever recovers the *net* rate — if a stock has multiple separate inflows and outflows, you cannot recover their individual values from the stock's trajectory alone. **The chapter's clean illustrating example**: a firm's cash balance staying perfectly flat is consistent with revenues and expenses both being $1 million/year, or both being $1 billion/year — the net behavior is identical, but the underlying gross flows (and the risk/scale they represent) are completely different. **A direct audit caveat**: a stable-looking stock metric can be hiding wildly different — and wildly different-risk — underlying gross flow volumes, and the net-rate view alone can never reveal which is the actual case.

## Connects to

- [[stock-flow-fundamentals-and-notation]] — this page operationalizes that page's "stocks integrate their flows" claim into a concrete, step-by-step visual technique, and the step-pulse example is a direct mechanical demonstration of reason #2 (inertia/memory) from that page.
- [[fundamental-modes-growth-goal-seeking-oscillation]] — the quarter-cycle phase-lag result is a precisely derivable special case of that page's oscillation mode, here shown arising from pure accumulation with zero feedback loops.
- [[barriers-to-learning-and-virtual-worlds]] — the graphical-differentiation limitation (net rate alone can't reveal gross flow magnitudes) is a structural version of that chapter's limited-information barrier, here expressed as an unavoidable mathematical fact rather than a measurement-system flaw.

## North Star Connection

- How this applies to the audit business: graphical integration/differentiation is a fast, low-tech skill directly usable in a client meeting — sketching a rough net-flow curve on a whiteboard and reasoning through the resulting stock shape (or vice versa) requires no software and builds client confidence in a forecast or diagnosis in real time. The "stable net flow can hide wildly different gross flows" caveat is a sharp question to ask before trusting any client metric that looks flat or stable.
- Track relevance: Systems — a core, broadly transferable analytical skill for quick, in-the-room diagnostic sketching during any audit discovery session.
- Possible future Second Brain use: a short "sketch the stock from the flow" practice exercise (Sterman's own recommendation — practice while reading the newspaper) is a good personal-skill-building habit worth tracking, given how directly it supports client-facing work.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | A fast, low-tech, directly client-usable analytical skill for whiteboard-level reasoning |
| Current usefulness | 4 | Immediately practicable without any software, in any client meeting |
| KSU support | 5 | Canonical system dynamics technique, directly useful for any quantitative systems coursework |
| Tech-stack relevance | 2 | Directly underlies how to sanity-check any spreadsheet model's stock-flow behavior by eye |
| Business audit value | 4 | The "stable stock can hide wildly different gross flows" caveat is a sharp, reusable due-diligence question |
| Data/workflow value | 3 | A concrete technique for visually sanity-checking time-series data before formal analysis |
| Reading urgency | 3 | A useful skill-building chapter, somewhat less immediately high-stakes than the chapter's two case studies |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Whiteboard-level diagnostic sketching — use graphical integration to predict a stock's likely trajectory from a described or sketched flow pattern in real time during a client conversation, without needing a computer or formal model.

**Use when**:
Reasoning through a client's described future scenario (a planned change in hiring rate, spending rate, or production rate) and wanting to quickly sketch the resulting stock trajectory for discussion.

**Do not use when**:
The actual flows are too irregular or poorly understood to sketch meaningfully — forcing a clean graphical-integration exercise onto genuinely chaotic or unknown data will produce false confidence.

**Fast retrieval query**:
`subject/calculus-without-math` — or search "graphical integration area under net rate" / "quarter cycle phase lag accumulation" / "stocks provide memory of past events" / "stable cash balance hides gross flows"
