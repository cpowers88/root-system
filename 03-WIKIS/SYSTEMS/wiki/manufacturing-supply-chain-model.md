---
domain: systems
type: framework
tags: [subject/system-dynamics, subject/supply-chains, subject/manufacturing, subject/model-initialization]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, supply-chain, audit]
---

# Building a Manufacturing Supply Chain Model: Order Fulfillment, Production, and Why Amplification and Lag Are Inevitable

**Summary**: A complete, staged manufacturing supply chain model (order fulfillment, production/WIP, production starts, demand forecasting) built directly from the generic stock-management structure — showing that even a smoothly-behaving, non-oscillating firm unavoidably amplifies and lags demand changes, purely as a consequence of its physical production delay. Plus the chapter's reusable discipline for initializing any model in a balanced equilibrium before testing it.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 18 ("The Manufacturing Supply Chain"), section 18.1

**Last updated**: 2026-06-22

---

## The Model, Built in Stages

Following the chapter's own explicit methodology — relax simplifying assumptions one at a time, fully test each version before adding more — the model accumulates structure step by step: **order fulfillment** (how shipments respond to inventory adequacy), **production and WIP** (a third-order manufacturing delay), **production starts** (the generic stock-management decision rule applied to both inventory and WIP), **demand forecasting** (exponential smoothing), then **order backlogs** and **raw materials inventory** as successive refinements. **The explicit reason for this staged approach, worth keeping as a standing modeling discipline**: building everything at once makes it impossible to isolate which structural element is producing which behavior; adding one piece at a time and fully understanding its effect before adding the next is what actually builds usable insight, not just a working simulation.

## Order Fulfillment: Why Shipments Fall Short Even With "Enough" Inventory

The order fulfillment ratio (shipments achieved relative to desired shipments) is a function of the ratio of maximum shipment rate (set by current inventory and minimum order-processing time) to desired shipment rate. **A subtlety with real, practical audit consequences**: for a firm carrying many SKUs, the *aggregate* fulfillment ratio drops below 100% even when the aggregate maximum shipment rate still exceeds aggregate desired demand — because at any given moment, *some* individual items are likely to be out of stock even while the total inventory looks adequate on paper. **The more SKUs aggregated together, or the less predictable individual-item demand, the lower the achievable fulfillment ratio at any given aggregate inventory coverage** — a direct, quantifiable reason why "we have plenty of inventory in total" can coexist with chronic stockouts on specific items, and a sharp caution against trusting aggregate inventory metrics alone when diagnosing a client's fill-rate problem.

## Production Starts: The Generic Stock-Management Rule, Applied Twice

Production starts are driven by **two nested adjustment loops**: an Inventory Control loop (desired production = expected orders + adjustment for the finished-goods inventory gap) and a WIP Control loop (desired production starts = desired production + adjustment for the WIP gap, where desired WIP = manufacturing cycle time × desired production, a direct application of Little's Law). **Desired inventory coverage itself has two components worth keeping separate**: a base coverage (the minimum order-processing time alone) plus a **safety stock coverage** specifically sized to hit a target service level — the higher the safety stock, the higher the achievable fulfillment ratio, a direct, quantifiable tradeoff between inventory carrying cost and service level that the model makes explicit rather than leaving as guesswork.

## A Critical Modeling Discipline: Always Initialize in Balanced Equilibrium

**A general best practice worth keeping for any future modeling work, not just this specific chapter**: a model should always be initialized so that every stock starts exactly at its equilibrium (desired) value, with all flows already equal to their target rates. **Why this matters**: if a model starts *out* of equilibrium, any test you run afterward gets confounded with the model's own transient settling-down behavior — you can no longer cleanly attribute the observed response to the specific shock you introduced, since some of what you're seeing is just the model working off its own initial imbalance. **The practical implementation rule**: specify initial conditions as *algebraic expressions* in terms of other parameters (e.g., Inventory₀ = Desired Inventory), never as bare numerical values — an expression-based initial condition stays correct automatically if you later change a parameter, while a hardcoded number silently throws the model out of equilibrium the moment any upstream parameter changes.

**A genuinely tricky wrinkle worth flagging**: sometimes the "obvious" way to express an initial condition creates a **simultaneous equation** — e.g., setting initial inventory equal to (desired coverage × shipment rate) seems reasonable, but the shipment rate itself depends on inventory through the order-fulfillment function, so inventory ends up depending on itself. **The general fix**: express the initial condition in terms of a variable that *doesn't* participate in the loop creating the circularity (e.g., desired shipment rate instead of actual shipment rate) — the two formulations only differ to the extent the actual rate falls short of the desired rate, which is exactly zero at a true equilibrium anyway. **Not every model has a balanced equilibrium at all** (explicitly noted: most growth/diffusion models from the skipped Chapter 9, and any model with unlimited-market growth assumptions, have no such equilibrium) — in those cases, the right move is to initialize each subsystem in equilibrium relative to its own inputs, or initialize the whole model along its natural growth path if one exists.

## Why Amplification and Phase Lag Are Unavoidable, Even Without Oscillation

**The chapter's central, sharpest result**: simulating the full model's response to a clean 20% step increase in customer orders produces amplification (production starts peak >42% above baseline — an amplification ratio of 2.12) and phase lag (the peak comes roughly half a year after the demand step, far longer than the 8-week production delay alone would suggest) — **but no oscillation at all**. The response is smooth, intendedly rational, and eventually settles cleanly at the new equilibrium. **This is the chapter's key theoretical point, worth keeping as a standing diagnostic distinction**: amplification and phase lag are an **inevitable, structural** consequence of any production delay — there is no way to avoid them, "no matter how smart the managers... may be" — while **oscillation is not inevitable** and specifically requires the additional failure (from [[beer-game-and-origin-of-oscillations]]) of mismanaging the supply line. **The mechanism behind the inevitability**: the *only* way inventory can rise back to a new, higher target is for production to temporarily exceed shipments — so any genuine increase in demand necessarily forces a temporary overshoot in production, and the overshoot in production starts must be larger still, since WIP itself must also be built up to a higher steady-state level to sustain the new throughput.

**Two further refinements quantify how each added piece of realistic structure compounds amplification, additively but predictably**: adding an explicit order backlog (rather than losing unfilled orders) **slightly reduces** amplification (2.12 → 1.97) because the backlog itself buffers the shock, smoothing how fast desired shipments can rise; adding a raw-materials inventory layer **increases** amplification further (to 2.52 for materials orders) because the materials-ordering decision inherits and compounds the inventory and WIP adjustments already happening upstream of it. **The general rule, worth treating as a standing expectation for any multi-stage client supply chain**: every additional stock and adjustment loop added to a supply chain tends to add its own increment of amplification on top of what's already there — a structural reason "more visibility/more buffers" doesn't automatically mean "more stable," and why the chapters that follow (linking multiple firms together) show amplification compounding even further at each additional link.

## Connects to

- [[stock-management-structure-and-amplification]] — this page applies the generic stock-management structure from that page twice over (inventory control, WIP control) inside a single integrated manufacturing model.
- [[beer-game-and-origin-of-oscillations]] — the amplification-without-oscillation result here is the clean baseline case against which the Beer Game's oscillation (caused specifically by ignoring the supply line) should be compared.
- [[littles-law-and-best-case-performance]] — Desired WIP = Manufacturing Cycle Time × Desired Production is a direct, named application of Little's Law inside the production-starts decision rule.
- [[modeling-process-and-client-ethics]] — the balanced-equilibrium initialization discipline is a concrete, technical instance of the "testing should be controlled experimentation" principle from that page's five-step modeling process.

## North Star Connection

- How this applies to the audit business: the SKU-aggregation fulfillment insight ("plenty of total inventory can still mean chronic stockouts on specific items") is a sharp, immediately checkable diagnostic for any client complaining about fill-rate problems despite "enough" inventory on paper. The amplification-is-inevitable-but-oscillation-is-not distinction is a clear, defensible way to set client expectations about how much volatility a supply chain redesign can realistically eliminate (the structural amplification from delays) versus how much is actually fixable (the supply-line-management failure that turns amplification into oscillation).
- Track relevance: Business / Systems — directly applicable supply-chain diagnostic vocabulary and a strong, transferable modeling-discipline practice (balanced-equilibrium initialization) for any future spreadsheet or simulation work.
- Possible future Second Brain use: a "balanced equilibrium initialization checklist" for any spreadsheet model Chris builds, and a "SKU-aggregation fulfillment check" (is the client's "adequate inventory" actually adequate at the individual-item level) are both strong candidate practical tools.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The amplification-vs-oscillation distinction and SKU-aggregation insight are both directly useful audit diagnostics |
| Current usefulness | 4 | Immediately applicable to any client fill-rate or production-planning conversation |
| KSU support | 5 | Rigorous, fully worked manufacturing supply chain model — strong ISYE/operations coursework material |
| Tech-stack relevance | 4 | The balanced-equilibrium initialization discipline is directly applicable to any spreadsheet or simulation model Chris builds |
| Business audit value | 4 | Sets clear, defensible client expectations about what's structurally inevitable vs. actually fixable in a supply chain |
| Data/workflow value | 3 | The SKU-aggregation insight directly informs how to interpret a client's own inventory/fill-rate data |
| Reading urgency | 4 | Foundational for the rest of Part V's supply-chain and labor-market material |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Diagnostic and modeling-discipline tool — use the SKU-aggregation insight when a client's "adequate inventory" coexists with stockout complaints, and use the balanced-equilibrium initialization practice for any spreadsheet/simulation model built for a client.

**Use when**:
A client reports adequate aggregate inventory but chronic specific-item stockouts, or when building any model that needs to cleanly isolate the response to a single test scenario.

**Do not use when**:
The client's system has no meaningful production delay or multi-SKU aggregation issue — a single-product, made-to-stock retail reorder process doesn't need this level of structural analysis.

**Fast retrieval query**:
`subject/manufacturing` + `subject/model-initialization` — or search "order fulfillment ratio aggregate SKU" / "balanced equilibrium initialization" / "amplification inevitable oscillation not" / "simultaneous initial condition equations"
