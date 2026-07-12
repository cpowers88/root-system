---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/audit, subject/system-dynamics, subject/stocks-and-flows, subject/climate-systems, subject/inertia]
---

# Global Warming as a Stock-Flow Problem: Why Temperature Keeps Rising After Emissions Stop

**Summary**: Even before considering any feedback loops, the pure stock-flow structure of the global carbon cycle and heat balance explains a deeply counterintuitive result — global mean temperature continues rising for roughly three decades after greenhouse gas emissions fall to zero, and stabilizing emissions at current levels does not stabilize the climate at all (atmospheric CO2 still more than doubles by 2300). This is Sterman's primary illustration that stock-flow inertia alone, independent of feedback, can produce highly counterintuitive dynamics.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 7 ("Dynamics of Stocks and Flows"), section 7.2

**Last updated**: 2026-06-22

---

## The Basic Physics, Reduced to a Stock-Flow Structure

Earth's surface temperature is set by a balance: incoming solar energy (insolation) vs. outgoing reradiated energy (black-body radiation, which increases with temperature). Greenhouse gases (GHGs) reduce the atmosphere's emissivity, trapping some outgoing radiation — without any GHGs at all, mean global temperature would be about −17°C (a permanently ice-covered planet); with the actual historical GHG concentration, it's about +15°C. **Two coupled stock-flow chains drive the dynamics**: the **global carbon cycle** (atmospheric CO2 as a stock, fed by fossil-fuel burning, drained by ocean/biomass uptake — with the deep ocean modeled as up to 10 distinct layers in Fiddaman's (1997) model, since vertical mixing is slow) and the **global heat balance** (surface/atmosphere temperature as a stock, with heat also slowly exchanging with the deep ocean, governed by the temperature differential between layers).

**A specific, named modeling flaw worth keeping as a methodological caution**: the widely-cited DICE climate-economy model (Nordhaus 1992) was found by Fiddaman to violate basic mass conservation by letting a significant fraction of carbon emissions simply vanish into an unmodeled sink — a direct, real-world instance of [[aggregation-and-challenging-the-clouds]]'s "challenge the clouds" discipline being skipped, with material consequences for the model's resulting projections.

## The Counterintuitive Result: Temperature Keeps Rising After Emissions Hit Zero

**The chapter's central simulated result**: even in a scenario where anthropogenic CO2 emissions fall to exactly zero in the year 2000, **global mean temperature continues rising for roughly three more decades**, only then beginning a very slow decline. This is not a feedback-driven surprise — it follows directly from the stock-flow structure alone, via two separate accumulation-lag mechanisms working together:

1. **The atmospheric CO2 stock declines only slowly even after its inflow stops**, because the *outflows* themselves shrink in response to falling concentration: lower atmospheric CO2 reduces the rate of uptake by biomass and by the ocean's mixed layer, while CO2 continues flowing *into* the atmosphere from ongoing biomass/humus decay (a stock-driven process that doesn't stop just because new emissions have). The compensating shrinkage of the outflows offsets much of the inflow's disappearance — so 50 years after emissions completely stop, modeled atmospheric CO2 has only fallen back to roughly its 1990 level.
2. **The heat-balance stock keeps rising as long as incoming radiation exceeds outgoing plus ocean-transferred heat** — and elevated (even if now slowly falling) atmospheric CO2 keeps suppressing outgoing radiation for years after the emission stoppage, so the surface keeps absorbing net heat and warming, just at a diminishing rate, until roughly 2030 when the balance finally re-equalizes.
3. **A further lag on the cooling side**: during the warmest decades, heat flowed *from* the warmer surface *into* the deep ocean (a one-way consequence of the temperature differential). Once the surface starts to cool, that stored deep-ocean heat begins flowing *back* toward the surface, actively slowing the temperature decline — the system's own thermal "memory" resists cooling even after the original forcing (CO2) has receded.

**This is reason #2 from [[stock-flow-fundamentals-and-notation]] (inertia/memory) and the graphical-integration delay logic from [[graphical-integration-and-differentiation]], both playing out simultaneously at planetary scale** — and it directly explains why the IPCC's own finding ("a discernible human influence on climate") cannot be resolved by simply correlating emissions with temperature in real time: the stock-flow lags are long enough that current temperature reflects decades of *past* emissions, not current ones.

## Why Stabilizing Emissions Doesn't Stabilize the Climate

**The chapter's most policy-relevant single result**: a simulation holding GHG emissions constant at 1995 levels indefinitely still produces **atmospheric CO2 more than doubling by 2300, and roughly 3°C of additional global mean warming.** This directly explains why the 1997 Kyoto Protocol's target (industrialized nations cutting emissions to ~95% of 1990 levels by 2012) was never going to be sufficient even if fully implemented (which it wasn't — the US Senate declared it dead on arrival, and rapidly developing nations' emissions, China's especially, were forecast to nearly double by 2015 on their own). **The mechanism is the same stock-flow logic as above, just run forward instead of toward zero**: as long as the *inflow* to atmospheric CO2 exceeds the *outflow*, the stock keeps growing, regardless of whether the inflow itself has stopped growing — "stabilizing the rate of filling a bathtub above the rate it drains still fills the bathtub, just more slowly."

**The explicit, italicized takeaway**: "stabilizing emissions near current rates will not stabilize the climate... mitigating the risk of climate change... requires a substantial decline in the rate of GHG emissions" — not a plateau, an actual *decrease*, because the relevant target is matching the inflow to the (slow, currently overwhelmed) natural outflow capacity, not just halting the inflow's *growth*.

## Three General Lessons (Stated Directly by the Source)

1. **Global warming cannot be proven or disproven by naively correlating emissions and temperature** — the dynamics involve multi-decade lags on both the carbon-cycle and heat-balance sides, so any simple same-period correlation is methodologically inadequate, directly the same warning as [[causal-loop-diagram-guidelines]]'s correlation-vs-causation discipline, here at planetary scale.
2. **The full impact of past emissions has not yet been observed** — oceans and terrestrial systems have been absorbing carbon at *elevated* rates precisely because the stocks aren't yet saturated; as those absorption-capacity stocks fill, their absorption *rate* (the negative feedback that's currently masking some of the problem) diminishes, meaning **future emissions may have a larger marginal warming impact than equivalent past emissions did** — a counterintuitive, stock-driven nonlinearity easy to miss if you only look at historical correlations.
3. **System inertia means meaningful warming and climate change are already locked in** — "action to halt warming must be taken decades before we can know what the consequences of warming will be," a direct, severe version of the decision-under-uncertainty problem any audit engagement faces on a smaller scale whenever a client's system carries comparable lag.

## Connects to

- [[stock-flow-fundamentals-and-notation]] — this case is the highest-stakes available illustration of "stopping the inflow doesn't fix the stock" (reason #2, inertia/memory) — halting emissions doesn't undo the accumulated atmospheric CO2 or the absorbed ocean heat.
- [[graphical-integration-and-differentiation]] — the three-decades-of-continued-warming result is a direct, real-world instance of the accumulation-creates-delay mechanism demonstrated abstractly in that page's phase-lag example.
- [[aggregation-and-challenging-the-clouds]] — the DICE model's mass-conservation violation is a concrete, consequential failure to "challenge the clouds" (an unmodeled, infinite-capacity sink for vanishing carbon).
- [[traffic-congestion-and-compensating-feedback]] — "stabilizing the rate doesn't stabilize the level" is structurally the same lesson as that case's "more capacity doesn't reduce congestion, it just changes what the capacity gets absorbed by" — both are cases where a plausible-sounding policy target (stabilize X) fails to address the actual stock-level problem.

## North Star Connection

- How this applies to the audit business: the core lesson — **"stopping/stabilizing a flow does not stop or stabilize the stock it feeds, if the stock's outflow capacity is already overwhelmed"** — is a directly transferable diagnostic for any client with a large, slow-draining liability stock (accumulated technical debt, deferred maintenance backlog, environmental liability, accumulated customer dissatisfaction): a policy that merely halts the *growth* of new problems won't reduce the *existing* backlog unless the processing/resolution rate genuinely exceeds the (now-stopped, but still nonzero) new-problem rate.
- Track relevance: Systems — a vivid, well-evidenced illustration of stock-flow inertia at the largest possible scale, useful both as a standalone systems-thinking teaching case and as source material for explaining the same dynamic to a client at a much smaller scale.
- Possible future Second Brain use: a "stabilize vs. reverse" framing question (is the client's proposed fix merely stabilizing an inflow, or actually reducing the existing stock) is a strong candidate addition to an audit-recommendation review checklist, directly modeled on this case's central distinction.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The "stabilizing the flow doesn't stabilize the stock" lesson is broadly transferable to any large-backlog client diagnosis |
| Current usefulness | 3 | Powerful as an illustrative case and teaching tool; the specific climate content itself is not directly actionable for SMB audit clients |
| KSU support | 5 | Rich, well-documented real systems-dynamics case combining stock-flow theory with a major real-world policy debate |
| Tech-stack relevance | 1 | Conceptual case study, no direct tool dependency |
| Business audit value | 4 | The "stabilize vs. reverse" distinction is a sharp, reusable framing for evaluating any client backlog-reduction proposal |
| Data/workflow value | 2 | Illustrative rather than a directly reusable data-collection method |
| Reading urgency | 3 | High illustrative value, lower direct urgency than the chapter's drug-policy case for Chris's specific client base |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Illustrative teaching case and client-communication tool — use the "three decades of continued warming after emissions stop" result as a vivid, memorable analogy when explaining to a client why simply halting a bad practice won't immediately fix an accumulated backlog or liability.

**Use when**:
A client proposes "stabilizing" or "capping" a problematic inflow (new defects, new complaints, new deferred-maintenance items) and assumes this alone will resolve the existing accumulated stock.

**Do not use when**:
The client's situation involves no meaningful accumulated stock or lag — a genuinely simple, fast-clearing backlog doesn't need this level of framing.

**Fast retrieval query**:
`subject/climate-systems` + `subject/inertia` — or search "temperature rises after emissions fall to zero" / "stabilizing emissions does not stabilize climate" / "DICE model mass conservation violation" / "ocean heat stored deep ocean slows cooling"
