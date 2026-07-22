---
domain: systems
type: case-study
tags: [subject/system-dynamics, subject/maintenance, subject/feedback-loops, subject/implementation]
timeline: now
status: wiki-only
source_role: example
use_cases: [systems-analysis, process-design, client-interview, audit]
---

# The Maintenance Game: From Du Pont's Reactive-Maintenance Trap to a Reusable Implementation Method, Plus Sterman's Twelve Principles

**Summary**: Du Pont discovered it spent 10-30% more on maintenance than industry leaders while getting 10-15% lower plant uptime — paradoxical until a system dynamics model revealed a self-reinforcing "reactive maintenance culture" trap, and an interactive role-play ("the Manufacturing Game") successfully spread that insight to thousands of frontline workers who would never read a model. Closes with Sterman's twelve-point distillation of what made all three of Chapter 2's case studies work — the chapter's most directly reusable consulting-methodology content.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 2 ("System Dynamics in Action"), sections 2.4-2.5 (chapter complete)

**Last updated**: 2026-06-22

---

## The Paradox: Spending More, Getting Less

Du Pont's 1991 benchmarking study found a result that contradicted every manager's mental model — more maintenance employees per dollar of plant value, *more* overtime (not less), excessive spare-parts inventories *and* heavy reliance on costly expedited procurement, and 10-30% higher maintenance spend per dollar of plant value alongside 10-15% *lower* uptime than industry leaders. Many blamed the brutal, cyclical chemicals-industry environment (energy crises, recessions, new low-cost competitors). Winston Ledet's diagnosis: blaming outside forces "while psychologically safe, didn't provide any leverage to improve" — the explanation had to be in **how Du Pont responded** to those pressures, not the pressures themselves (a direct instance of the [[barriers-to-learning-and-virtual-worlds]] fundamental-attribution-error trap, here applied to blaming "the environment" rather than internal system structure).

## The Reframe: From Defect Correction to Defect Prevention

The model's first conceptual shift, before any quantification: stop treating maintenance as **defect correction** (a cost center fixing failures) and start treating it as **defect prevention/elimination** (a physics problem). Equipment fails when **latent defects** — leaky seals, dirty bearings, out-of-true shafts, miscalibrated instruments — accumulate past a threshold; a machine with latent defects can still run, but is failure-bound unless the defects are removed.

**The core stock-and-flow structure**: total latent defects is a single stock, filled by normal wear-and-tear *and* by collateral damage from breakdowns themselves (a seized bearing can bend a shaft, overheat a motor, break couplings — creating new defects), and drained by two balancing loops: reactive maintenance (repair after failure) and planned maintenance (proactive repair before failure).

## The Vicious-Cycle Cascade That Traps a Plant in Reactive Mode

What looks symmetrical (two balancing loops draining the same stock) is destabilized by a cascade of self-reinforcing positive loops triggered by cost pressure (the 1973 oil crisis is the chapter's worked trigger):

- **R1 (collateral damage)**: cost-cutting forces planned-maintenance budgets down first (since "when critical equipment breaks down, it must be fixed" — reactive work is non-discretionary) → defects rise → breakdowns rise → collateral damage from those breakdowns adds still more defects.
- **R2 ("Go to the Outage")**: more breakdowns pull mechanics off planned work *and* mechanics actively prefer reactive work for the overtime pay — quoted directly: "to hell with this vibration monitoring stuff, I'm going to the outage area" — further starving planned maintenance.
- **R3 ("Too Busy for PM")**: falling uptime makes operators *less* willing to release working equipment for planned maintenance ("I can barely meet demand as it is and you want me to take this line down?") — the very symptom of the trap (low uptime) becomes the reason planned maintenance can't happen, deepening the trap.
- **R4-R7 (parts quality, design improvement, training, planning capability)**: rising breakdown-driven costs force cuts to part quality, equipment upgrades, mechanic training, and the planning/scheduling function itself (cut first, since planners "don't actually fix anything") — each cut independently raises defects and breakdowns further.
- **R8-R9 (revenue and reputation erosion)**: low uptime constrains revenue directly *and* damages delivery-reliability reputation, eroding price and volume — both forcing still deeper budget cuts, accelerating every loop above.
- **R10 (reactive culture)**: over years, a workforce that has only ever known frequent breakdowns comes to treat low uptime and reactive firefighting as simply normal — even the *physical plant* embeds the low-reliability assumption (backup pumps installed because primary units are known to fail).

**The diagnostic punchline directly explains the original paradox**: spending *more* while getting *less* isn't a contradiction once you see that nearly all the extra spending was reactive (overtime, expedited parts, collateral-damage repair) rather than the proactive spending that actually prevents defects — the budget total went up while its *composition* shifted entirely away from the activities that would have reduced it.

## The Counterintuitive Policy Result: Why Cost-Minimization Made Things Worse

Simulated policy comparisons (Table 2-1 in the source) produced a result that directly explains why past Du Pont improvement attempts had failed: implementing the *same* proactive-maintenance policy suite under two different mandates produced wildly different outcomes —

- **Optimize-and-downsize** (cut headcount to hold uptime constant at the old 83.5% baseline): 91 → 61 mechanics, **$1.2M/year saved**.
- **Maximize profit, no downsizing** (reinvest the productivity gain into more planned maintenance instead of harvesting it as headcount cuts): uptime rises to 93.3%, **$9 million/year** in added profit — roughly 7.5x the savings-only result, using the *identical* policy suite.

**Why**: cost-minimization immediately harvests every productivity gain as a headcount cut, so planned-maintenance resources stay permanently constrained and the organization never escapes firefighting mode. Reinvesting instead lets falling breakdowns free up mechanics for *more* planned work, which cuts breakdowns further, compounding — **the same R1-R10 loops that ran as vicious cycles downward now run as virtuous cycles upward**, with synergy across policies exceeding the sum of their individual effects.

**The critical adoption trap this also explains**: every one of these policies shows **worse-before-better** behavior — costs rise and uptime *falls* immediately after implementation (taking equipment offline for planned work that hasn't yet paid off, while still bearing the old reactive repair load), and only later does the breakdown rate actually fall. **"If managers do not understand why it occurs or how long it might last, they may interpret the short-run deterioration in performance as evidence that the policies don't work and then abandon them"** — directly explaining why Du Pont's *own* prior improvement attempts, simulated and confirmed to have failed in just this way, had been abandoned before they could pay off.

## The Implementation Problem: A Model Can't Reach Thousands of Mechanics

A white paper and management presentations produced "nothing" — predictable pushback ("we already know planned maintenance is a good idea," "we tried that and it didn't work," "your model doesn't account for x"). Ledet's diagnosis: **the real client group wasn't management, it was the thousands of line managers, operators, and mechanics whose daily behavior actually had to change** — and none of them could plausibly be trained in system dynamics or given access to the simulation model itself.

**The solution**: convert the simulation model into the **Manufacturing/Maintenance Game**, an in-person role-play (three roles — operations manager, maintenance manager, spare-parts manager — using physical chips and markers to represent equipment and latent defects) embedded in a 2-day interactive workshop designed to engage "visual, auditory, and kinesthetic" learning modes, not slide presentations. **The game reliably reproduces real organizational conflict**: the maintenance manager's requests to take equipment down are realistically rebuffed by an operations manager under demand pressure — and teams following cost-minimization policies experience the same slow uptime decline the formal model predicted, while teams committing to planned maintenance experience the same worse-before-better dip before improvement, **compressed from months into a few hours of play**.

## Results and the Two Honest Complications

By 1994, plants using the program showed pump MTBF improving 12%/doubling of cumulative experience (vs. 5% for 23 non-implementing plants) alongside a 20% direct-cost reduction (vs. a 7% *increase* for non-adopters) (Carroll, Sterman, and Marcus 1998). Conservative company-wide estimate: **$350M+/year** in avoided maintenance costs.

**Two complications worth keeping** (the source is explicit these aren't unqualified successes): (1) **success creates its own threat** — corporate cost-cutting mandates, applied indiscriminately, pulled resources away from a program whose early phase *looks* like rising cost; (2) the program's internal champion (Ledet) eventually left Du Pont entirely to commercialize the game independently, since the company itself struggled to reward or retain the team that had created the value.

## The Lima, Ohio Refinery: The Sharpest Single Number in the Chapter

BP's Lima refinery had fallen into the identical reactive-maintenance trap and was already slated for sale or closure when it adopted the maintenance game (1994) — championed not by top management but by a maintenance training supervisor and an engineer (Paul Monus). Maintenance costs rose 30% in the first six months (the predicted worse-before-better dip); management, primed by the model's prior explanation of this pattern, held course. **BP still moved to close the refinery in 1996** after failing to find a buyer — but the employees who stayed kept running the program anyway, "because they had chosen to be there."

**By 1998**: pump MTBF rose from 12 to 58 months; pump failures fell from 640/year to 131/year; safety incidents cut by a factor of 4; **total new value created: $43 million/year against a program cost of $320,000/year — a 143:1 return**. Clark USA bought the refinery for $215 million and kept it operating. Sterman's explicit judgment: "without the dramatic improvements in refinery operations stimulated by the systems thinking intervention it is unlikely Clark, or any buyer, would have offered enough for the facility to keep it running." **One specific sub-result worth keeping verbatim**: eliminating butane flare-off (zero pollution, $1.5M/year savings) took 2 weeks and cost $5,000 — a known fix, with the needed engineering knowledge and most materials already on-site, that had simply never been acted on for 8 years because of the team's mental model that "the problem was imposed by external forces beyond their control." **The barrier was never technical. It was always the mental model.**

## Sterman's Twelve Principles for Successful System Dynamics Practice

Distilled from all three Chapter 2 cases ([[gm-auto-leasing-case-study]], [[ingalls-shipbuilding-project-dynamics-case]], and this case) — the chapter's most directly portable consulting-methodology content:

1. **Develop a model to solve a particular problem, not to model the system.** Exclude everything not relevant to the client's actual problem; scope for feasibility and timeliness.
2. **Modeling should be integrated into a project from the beginning** — starting in the problem-definition phase, not bolted on afterward — and it should shift diagnosis toward system structure rather than blaming individuals.
3. **Be skeptical about the value of modeling; force the "why do we need it" discussion at the start.** System dynamics is not the right tool for every problem. Welcome hard client questions about whether/how it will actually help, early.
4. **System dynamics does not stand alone.** It complements (not replaces) benchmarking, statistical analysis, and market research — modeling rests on a strong base of existing data and domain understanding.
5. **Focus on implementation from day one.** Constantly ask "how will the model help the client make decisions" and "how do we get there from here" — including quantifying costs/benefits the client's existing accounting system doesn't already capture.
6. **Modeling works best as an iterative joint inquiry between client and consultant**, not as a tool for advocacy. Don't build the client's pre-existing opinion into the model — let them test it themselves, in real time, in workshops.
7. **Avoid black-box modeling.** A model built out of the client's sight will never change their mental model or their behavior. Show them the model; let them run and criticize their own tests; resolve their objections to *their* satisfaction, not just yours.
8. **Validation is continuous, not a single after-the-fact test.** Confidence builds gradually by repeatedly confronting the model with data and expert opinion (both modeler's and client's) — not by one historical-fit check.
9. **Get a preliminary model working as soon as possible; add detail only as necessary.** Don't build a comprehensive conceptual model before simulating anything — a conceptual model is only a hypothesis, and simulation is what actually tests and improves it (directly echoing [[barriers-to-learning-and-virtual-worlds]]'s 1.4.3 argument for why simulation, not diagrams alone, is necessary).
10. **A broad model boundary matters more than a lot of internal detail.** Capturing the feedbacks the client's mental model is missing matters more than precisely representing each component — dynamics emerge from interactions, not component complexity (the same point from [[policy-resistance-and-feedback-thinking]]'s feedback-loop section).
11. **Use expert modelers, not novices.** Modeling is not programming — you cannot hand a qualitative diagram to a coder. It requires disciplined methodology and business judgment built through real practice; use any project as a chance to build that capability in others, but don't substitute an untrained team for expert guidance on a real engagement.
12. **Implementation does not end with a single project.** In all three cases, the modeling work's impact continued for years past the original engagement — models got reapplied, modelers built transferable expertise, and clients carried the new way of thinking into new roles and organizations.

## Connects to

- [[barriers-to-learning-and-virtual-worlds]] — the entire maintenance case is an applied demonstration of why simulation/role-play ("virtual worlds") succeeds where a written report failed: it compresses the worse-before-better delay into hours and lets thousands of non-technical participants experience the dynamic directly rather than being told about it.
- [[policy-resistance-and-feedback-thinking]] — the R1-R10 vicious-cycle cascade is the chapter's most fully worked example of multiple interacting positive feedback loops, directly building on the basic loop-type vocabulary from Chapter 1.
- [[ingalls-shipbuilding-project-dynamics-case]] — both cases hinge on a "worse-before-better" transition that gets misread as policy failure if not anticipated; both also show a model converting an unresolvable blame dynamic (chemicals industry conditions / Navy vs. contractor) into structural accounting.
- management-by-abdication and fatal-assumption-and-technician-takeover — Ledet's realization that the *real* client was thousands of mechanics, not the management team, parallels the E-Myth's insistence that systemic change requires reaching the people actually doing the work, not just redesigning policy at the top.

## North Star Connection

- How this applies to the audit business: the reactive-maintenance vicious-cycle cascade (R1-R10) is a directly transferable diagnostic template for *any* client whose "maintenance," "rework," or "firefighting" budget keeps rising while output quality falls — not just literal equipment maintenance. The worse-before-better warning is a critical, reusable client-expectation-setting tool before recommending any genuine process change. The Manufacturing Game itself is a strong candidate model for a low-tech, high-engagement audit deliverable when a client's frontline workforce (not just management) needs to internalize a systemic insight.
- Track relevance: Business / Systems — directly relevant to field-service and construction-equipment maintenance (the entry-hypothesis market), and a strong implementation-methodology reference for every future engagement.
- Possible future Second Brain use: the twelve principles are a strong, near-ready candidate for a standalone "How Chris Runs a Systems-Audit Engagement" methodology checklist; a simplified physical/board-game version of the latent-defect mechanic is a plausible audit-deliverable tool for client workshops.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The vicious-cycle cascade and worse-before-better warning are both core, repeatedly-applicable audit diagnostics; the 12 principles are a ready-made engagement methodology |
| Current usefulness | 5 | Immediately usable diagnostic template and client-expectation-management tool |
| KSU support | 4 | Strong applied case in organizational dynamics and implementation, slightly less formula-heavy than the queueing/Factory Physics material |
| Tech-stack relevance | 1 | Conceptual/case-study content, no direct tool dependency |
| Business audit value | 5 | The Lima 143:1 ROI number and the "barrier was never technical, always the mental model" line are both sharp, quotable, client-ready arguments |
| Data/workflow value | 3 | The latent-defect/MTBF tracking concept is a plausible real data-collection framework for an equipment-heavy client |
| Reading urgency | 4 | Closes out Chapter 2 and delivers the chapter's single most reusable methodology summary (the 12 principles) |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Engagement-methodology reference (the 12 principles) plus a diagnostic template for any client trapped in a "spend more, get less" reactive cycle (maintenance, rework, expediting, firefighting) — and a client-expectation-setting tool for the worse-before-better transition before recommending genuine process change.

**Use when**:
A client describes a costly, recurring firefighting pattern with rising spend and falling output quality, or when a proposed fix needs to survive a likely-to-be-misread early dip in performance before benefits appear.

**Do not use when**:
The client's situation has no plausible vicious-cycle structure — a single, non-recurring quality issue doesn't need the full R1-R10 framing.

**Fast retrieval query**:
`subject/maintenance` + `subject/feedback-loops` — or search "Du Pont reactive maintenance trap" / "Manufacturing Game latent defects" / "Lima refinery 143 to 1" / "worse before better maintenance" / "twelve principles system dynamics"
