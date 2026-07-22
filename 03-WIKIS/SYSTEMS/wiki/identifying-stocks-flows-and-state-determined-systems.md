---
domain: systems
type: framework
tags: [subject/system-dynamics, subject/stocks-and-flows]
timeline: now
status: wiki-only
source_role: primary
use_cases: [systems-analysis, client-interview, audit]
---

# Identifying Stocks and Flows: The Snapshot Test, the "Stocks Change Only Through Rates" Rule, and Presenting Models to Clients

**Summary**: The practical toolkit for telling stocks from flows in a real system — the snapshot test, units-of-measure discipline, conservation of material vs. information, why constants and exogenous variables are really just stocks you've chosen not to model, the single most common diagramming error (drawing an information link directly into a stock), and the chapter's explicit guidance on choosing how technical a model presentation should be for a given client.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 6 ("Stocks and Flows"), section 6.2

**Last updated**: 2026-06-22

---

## The Snapshot Test

**The cleanest practical heuristic for telling stocks from flows**: imagine freezing the system with a single photograph. **Anything you could count or measure in that frozen instant is a stock** — inventory level, account balance, water in a reservoir, even a manager's *belief* about the current order rate (a mental stock). **Anything that requires comparing two moments in time is a flow** — you cannot tell from one photograph whether a reservoir's level is rising or falling, or how fast money is being spent from an account, even though the photograph tells you exactly how much is currently in each.

**The test extends cleanly to intangibles**: a posted price is a stock (it stays in effect until someone explicitly changes it, exactly like inventory remains constant until a flow alters it); a trader's verbal bid in a pit is a very short-lived stock, valid until withdrawn or revised. **The expected customer order rate is a genuinely subtle case worth keeping**: the *actual* order rate is a flow, but a manager's *belief* about that rate is a stock — a mental state that persists until new information arrives and the belief is explicitly updated. Critically, **the manager's belief can simply be wrong**, and tracking it as its own stock (separate from the true, unobservable order rate) is exactly what lets a model represent systematic perception bias or lag — directly the same actual-vs-perceived distinction introduced in [[causal-loop-diagram-guidelines]].

## Units of Measure as a Diagnostic Tool

Stocks are measured in plain units (widgets, people, dollars, yen); their associated flows must be measured in **the same unit, per time period** (widgets/week, people/month, $/hour) — and the choice of time period is entirely arbitrary as long as it's used consistently. "Production is running at 1,200 widgets/day" is exactly equivalent to "8,400/week" or "43,800,000/century" — these are all statements about the *instantaneous current rate*, not a claim about how many widgets will actually accumulate over any given interval (which depends on whether the rate stays constant, which it usually won't). **The general rule that catches most stock/flow mislabeling**: if a quantity's units don't naturally include "per time period," it's a stock; if they do, it's a flow.

## Conservation: Material Is Conserved, Information Is Not

A stock-flow network conserves whatever flows through it in the specific sense that an item entering a stock stays there until it explicitly flows out, and when material moves from one stock to another, the first stock's loss exactly equals the second's gain. **The accounts-receivable example sharpens an important subtlety**: the stock of receivables conserves *information about who owes what*, not literal dollars — you can't actually exchange a stock of receivables for cash at face value (a collection agency will only pay a fraction). Yet **the information itself is still conserved**: you can't legally sell the same receivable twice. This distinguishes conserved material/information flows from a separate category entirely: **information *about* a stock's value can be freely shared with anyone in an organization without depleting it** — accessing the receivables balance doesn't use it up, unlike the underlying receivables themselves.

## Constants and Exogenous Variables Are Just Stocks You've Decided Not to Model

A precise, easy-to-forget point: **constants are simply state variables that change too slowly to matter over your chosen time horizon**, not fundamentally different from any other stock. The chapter's video-game-demand example: the population aged 4-20 is a real, slowly-changing stock, but over a multi-year product life cycle it's reasonable to treat it as a fixed constant — *not* because it's fundamentally non-dynamic, but because no significant feedback exists between video-game sales and birth/death/migration rates over that horizon. **Exogenous variables are the same idea at a different time scale**: stocks you've chosen to leave outside the model boundary rather than model explicitly — directly the same boundary-drawing discipline from [[time-horizon-and-endogenous-explanation]], now expressed in stock-and-flow terms specifically.

## Auxiliary Variables: Don't Compress Multiple Ideas Into One Equation

Auxiliaries (intermediate variables that are functions of stocks/constants/exogenous inputs, but are themselves neither stocks nor flows) exist purely for clarity — a model is mathematically identical whether or not you use them, since any auxiliary can always be eliminated by substitution into the rate equation it feeds. **But the chapter is explicit that you should almost never actually do that elimination**: substituting auxiliaries away produces equations that bundle multiple distinct ideas together, are harder for *you* to understand later, harder for *anyone else* to read, and — critically for client-facing work — **harder to revise if a client disagrees with just one piece of the underlying logic**. The population-model example shows the cost concretely: with "Fractional Birth Rate" and "Food per Capita" left explicit as separate auxiliaries, the model clearly shows two distinct loops (a positive growth loop and a negative resource-constraint loop); collapsing them into one "reduced form" equation makes the link between Population and Net Births *literally ambiguous in sign* and erases the ability to see the two loops as separate mechanisms at all. **The general rule: each equation should represent exactly one idea.**

## The Single Most Common Diagramming Error: "Stocks Change Only Through Their Rates"

**No causal link can point directly into a stock.** A stock's value can only change via an explicit inflow or outflow — never by a direct information arrow from some other variable. **The chapter's worked correction, a service-queue model, is the cleanest illustration of why this matters in practice**: people in workshops routinely draw an arrow straight from "Workweek" or "Service Staff" to the stock "Customers Awaiting Service," reasoning (correctly, in plain English) that more staff means a shorter queue — but assigning that link a *negative* polarity directly into the stock is structurally wrong. **The correct diagram** routes Workweek and Staff through the actual outflow (the Customer Departure Rate = Staff × Productivity × Workweek), and *that* rate is what reduces the stock. The end *behavior* is identical either way (more staff → shorter queue) — **but the correct version captures that this happens because the outflow valve opens wider, not because some magical direct link reaches into the bathtub and removes water from it.** Every information link in a properly drawn stock-flow diagram should terminate on a flow's valve, never on a stock's rectangle directly.

## Continuous Time, Instantaneous Flows, and Why You Can Never Actually Measure One

System dynamics represents time as continuous — flows are formally defined as their *instantaneous* value, the literal derivative of the stock at that exact moment. **The chapter makes an important, almost counterintuitive epistemic point: no one can ever actually measure an instantaneous flow value.** GDP is reported as an average rate over a quarter, not an instant; quarterly sales figures are cumulative totals over the quarter, not a snapshot of "sales right now"; even a car's speedometer reports an average velocity over some (very short) prior interval, not literally instantaneous speed — it just happens that the measurement interval is short enough relative to how fast a car's speed actually changes that the distinction rarely matters. **For social and economic systems, the reporting/measurement delay is frequently long relative to how fast the underlying rate is actually changing** — and that gap "dramatically influence[s] the stability of the system," directly connecting to the oscillation-from-delay mechanism in [[fundamental-modes-growth-goal-seeking-oscillation]] and the limited-information barrier in [[barriers-to-learning-and-virtual-worlds]].

## Continuous vs. Quantized Flows — A Purpose-Driven Choice, Not a Fact About Reality

Most real flows are actually **quantized** (discrete whole items — you can't launch half an oil tanker, hire half a person), but the continuous-flow approximation is frequently the right modeling choice anyway, since the error it introduces is usually small relative to ordinary measurement/parameter uncertainty (fractional FTE employees are a perfectly meaningful, useful concept for most workforce models). **The choice is governed entirely by model purpose, not by some deeper truth about the system**: a model of oil-tanker market price cycles can treat tanker ordering/construction/scrappage as continuous; a model meant to optimize port-facility scheduling for individual tanker arrivals must treat ships as discrete entities. **The same logic applies to queueing-theory applications** (see [[flow-variability-and-queueing-fundamentals]] for the discrete-arrival math): even there, the continuous approximation often works well enough that the choice should still be driven by the specific question being asked, not by a default assumption that "people are discrete, so model them discretely."

**A related, frequently-violated modeling discipline worth flagging explicitly**: many queueing-theory applications (and a "great many" textbook theorems) assume the arrival rate to a line is exogenous — but real customers **balk**: a longer line reduces the rate at which new customers choose to join it at all, a genuine negative feedback loop. **Omitting this feedback "in the interests of analytical tractability or programming convenience will often lead to a fatal flaw in your analysis and policy conclusions"** — a direct, sharp warning against borrowing a clean theoretical queueing result without checking whether its exogenous-arrival assumption actually holds for your client's real situation.

## Presenting Stock-Flow Models to Clients: Match the Tool to the Audience

All four representations (bathtub, diagram, integral equation, differential equation) carry identical information, but **choosing the wrong one for a given audience can sink an otherwise excellent modeling project.** Sterman's explicit warning, stated from direct experience: showing differential equations or simulation code to a non-technical client team is "one of the worst things a consultant can do" — it reads as caring more about the elegance of the mathematics than about solving the client's actual problem, and risks humiliating people in the room. **Even technically sophisticated client teams sometimes respond better to concrete physical metaphors than to formal stock-flow notation**: a multinational chemicals firm's engineering team — people with real mathematical training — reported they "never really understood how the business worked" until production, inventory, and even *equipment defects* were drawn as literal tanks, pipes, and valves matching the physical plant equipment they already knew intimately. **An insurance-claims management simulator went further still**, representing claims as letters flowing into an inbox and settlement checks flowing back out, with little human-figure icons for the claims-adjuster workforce — concrete imagery that helped non-technical workshop participants grasp the underlying structure far better than abstract rectangles would have.

**The explicit caution against over-correcting**: don't ever hide the underlying model or equations from a curious client, and recognize that some clients are *offended* by what they perceive as oversimplified cartoon diagrams and prefer the more "professional" formal notation — **there is no universal right answer; you must know your specific client's preferences and technical comfort, established early in the engagement.** And a final discipline aimed at the modeler, not the client: you personally must understand the full mathematical structure underlying any bathtub metaphor you present, even if your client never needs to — "you do need to understand the structure and dynamics of stocks and flows thoroughly and rigorously," regardless of how simply you choose to present it.

## Connects to

- [[stock-flow-fundamentals-and-notation]] — the companion page on stock-flow notation and the four reasons stocks generate dynamics; this page covers the practical identification and diagramming-discipline tools.
- [[causal-loop-diagram-guidelines]] — the actual-vs-perceived-conditions guideline from that page is the general case of this page's "expected order rate is a stock, the true order rate is a flow" example.
- [[barriers-to-learning-and-virtual-worlds]] — "no one can ever measure an instantaneous flow" is a formal, structural restatement of that chapter's limited-information barrier (1.3.2), now grounded in the mathematics of measurement itself rather than just organizational reporting bias.
- [[flow-variability-and-queueing-fundamentals]] — the balking/exogenous-arrival-rate warning directly qualifies how that page's queueing formulas should and shouldn't be applied to a real client line or service system.

## North Star Connection

- How this applies to the audit business: the "stocks change only through rates" diagramming rule is directly useful for catching sloppy reasoning in client discussions ("if we just tell people to come in less, the backlog will shrink" — no, only the *actual processing/departure rate* reduces a backlog, not an exhortation). The balking warning is a sharp, practical check before recommending any queueing-based staffing model to a client whose customers genuinely do walk away from long lines. The presentation-matching guidance (bathtubs vs. equations vs. tanks-and-pipes) is directly applicable to how Chris designs any client-facing report or workshop.
- Track relevance: Business / Systems — the audience-matching guidance is immediately relevant to how Chris presents any future audit deliverable, regardless of the specific analytical content.
- Possible future Second Brain use: a short "how technical should this deliverable be" client-assessment question, paired with the bathtub/tanks-and-pipes/formal-notation spectrum from this page, is a strong candidate addition to an audit report-design checklist.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The snapshot test and the audience-matching presentation guidance are both immediately, broadly applicable to any audit engagement |
| Current usefulness | 5 | The "stocks change only through rates" rule directly catches a common, real client reasoning error |
| KSU support | 5 | Canonical system dynamics methodology, directly useful for ISYE/operations coursework |
| Tech-stack relevance | 3 | The units-of-measure discipline and continuous/quantized choice directly inform any spreadsheet or simulation model build |
| Business audit value | 5 | The presentation-matching guidance is a sharp, directly actionable lesson for designing every future audit deliverable |
| Data/workflow value | 4 | The snapshot test and units discipline are concrete, reusable data-modeling techniques |
| Reading urgency | 4 | High standalone value as both a diagramming-skill reference and a client-communication guide |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Diagramming-error check and client-deliverable design guide — use the snapshot test and "stocks change only through rates" rule when building any client-facing stock-flow model, and use the bathtub/tanks-and-pipes/formal-notation spectrum to choose the right level of technicality for a given client audience.

**Use when**:
Building any model involving an accumulation (backlog, inventory, debt, headcount) for client presentation, or when a client proposes a fix that sounds plausible in plain English but needs checking against the actual stock-flow structure.

**Do not use when**:
The conversation is purely qualitative and no actual diagram or model is being built — the formal apparatus isn't needed for casual discussion.

**Fast retrieval query**:
`subject/stocks-and-flows` — or search "snapshot test stocks flows" / "stocks change only through their rates" / "customer balking exogenous arrival rate" / "tanks and pipes client presentation"
