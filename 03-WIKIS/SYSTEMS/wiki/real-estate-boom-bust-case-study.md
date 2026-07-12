---
domain: systems
type: case-study
tags: [priority/now, status/wiki-only, domain/systems, source-role/example, use-case/systems-analysis, use-case/client-interview, use-case/audit, subject/system-dynamics, subject/supply-chains, subject/real-estate-cycles, subject/groupthink]
---

# Real Estate Boom and Bust: Why Sophisticated, Well-Capitalized Professionals Make the Same Mistake as Beer Game Novices

**Summary**: Real, on-the-record interviews with senior real estate developers and advisors reveal that the same supply-line-ignoring mistake that produces oscillation in the Beer Distribution Game — among complete novices, playing with toy money — also drives one of the largest, most consequential asset-market cycles in the real economy. The interviews expose exactly *why* sophisticated professionals with enormous financial stakes still fail: not ignorance of the numbers, but systematically open-loop mental models, sunk-cost ego investment, herd dynamics, and misaligned incentives running all the way through the financing chain. Closes Chapter 17 of Business Dynamics.

**Sources**: BusinessDynamics.pdf (Sterman, *Business Dynamics: Systems Thinking and Modeling for a Complex World*, McGraw-Hill, 2000), Chapter 17 ("Supply Chains and the Origin of Oscillations"), sections 17.4.3 and 17.5 (chapter complete)

**Last updated**: 2026-06-22

---

## The Scale and Persistence of the Cycle

Hoyt's (1933) classic study of Chicago real estate from 1830 to 1932 — the chapter's headline data — shows land valuations swinging roughly ±50% around trend and construction activity ranging from 60% below average (busts) to more than double average (booms), over cycles lasting **10-20 years**, far longer and larger in amplitude than the ordinary 3-5 year business cycle. **The explicit point this rules out**: such a long, large cycle cannot be blamed on ordinary macroeconomic fluctuation — something specific to the real estate market's own structure is generating it. The chapter notes this isn't historical curiosity: North American and European property boomed in the late 1980s and crashed in the early 1990s; Japan's bubble economy of the same era and southeast Asia's late-1990s building boom-and-bust are cited as recent, large-scale recurrences of the identical pattern.

## The Causal Structure: The Same Stock-Management Trap, Dressed as a Real Asset Market

Demand for commercial space tracks regional employment; low vacancy pushes effective rents up; rising rents raise both operating profitability *and* capital gains (market value) for existing buildings — and **high, rising profits attract new developers and abundant financing**, swelling the supply line of buildings under development. **The delay is severe**: 2-5 years between project initiation and a completed building actually reaching the market. **The negative feedback loops that should balance the market** (Demand Response, Supply Response, and Speculation — labeled B1-B3 in the source) only correct things *after* the long construction delay plays out, by which point the market has typically already overbuilt.

**The specific, sharp diagnostic the source draws from the data**: in the Chicago cycle, construction activity peaks **at or after** the peak in prices — meaning by the time builders are breaking the most ground, rents are already starting to soften and vacancy is already starting to rise. **This is the supply line problem from [[beer-game-and-origin-of-oscillations]] playing out at a multi-year, multi-billion-dollar scale**: developers should be tracking the volume of space already under construction industry-wide and tempering new starts well before prices peak — but they routinely don't, and the empirical timing proves it. Anthony Downs's quoted assessment of the late-1980s bust: national office vacancy exceeded 19% for three straight years by 1987 (up from under 5% in 1981) — "overwhelming evidence" — yet **banks accelerated construction lending in 1988-89 anyway**, and long-term investors kept buying at high prices even as effective rents were visibly falling.

## What the Field Interviews Actually Revealed (Hernandez 1990; Thornton 1992)

MIT researchers interviewed senior, bottom-line-accountable executives at leading real estate firms, using a careful methodology designed to avoid leading the witness: open, neutral questions first, asking directly about cycles/delays/the supply line **only if the developer hadn't mentioned them unprompted.** **The finding was almost uniform and striking**: virtually none spontaneously raised cycles, time lags, or the supply line at all. Developers' own accounts focused almost entirely on **detail complexity** — site selection, navigating permitting, financing relationships, architect/contractor networks ("Location is a bigger factor than the macro market... location, location, location") — with essentially no spontaneous attention to **dynamic complexity** (directly the same distinction from [[barriers-to-learning-and-virtual-worlds]]'s 1.3.1).

**When asked directly about cycles, the responses ranged from openly dismissive to actively fatalistic**: "We never looked at cycles. Our analysis figured stable, positive economic growth." "I am lousy when it comes to cycles... There are too many other factors... I think they probably negate them." One advisor's account is the sharpest available illustration of [[barriers-to-learning-and-virtual-worlds]]'s confirmation-bias material: industry forums routinely circulate newspaper clippings from 1929, 1974, and 1981 warning of the exact same pattern — and "even with this supposed evidence of real estate cycles in history, [they] won't change [people's] minds! The pressure of the system is very strong."

**Several distinct, independently-operating failure mechanisms emerged from the interviews, each worth keeping as a separate diagnostic category**:

- **Trend extrapolation instead of structural analysis**: developers explicitly described adjusting projections incrementally off "last year's benchmark" ("most people are bullish, rents are firm, so we will do a little more") rather than modeling the underlying supply-demand feedback at all.
- **No formal tracking of the competitive pipeline**: "Tracking the supply in the pipeline is a real difficult task. Nothing is done formally... a total guess." Even developers who claimed to track supply often failed to close the loop back to price ("we figured it would just affect the amount of time it took to lease up the property" — not that added supply would actually depress rents).
- **Sunk-cost / ego/identity investment**: "I am not about to walk away from this project given the time and money I have already invested in it... It's a big ego thing... like being in a fraternity."
- **Financial models used for persuasion, not inquiry**: discounted-cash-flow spreadsheets were built primarily to secure financing, with inputs ("tweaked") to hit whatever internal rate of return the lender wanted to see — not as genuine forecasting tools subjected to real scrutiny. "That pro forma and a couple of glossy pictures and the bank gives them the loan!"
- **Reliance on speculative reversion (capital gains) to paper over weak fundamentals**: when rental cash flow alone didn't justify a project, developers leaned on an assumed future sale at appreciated value — explicitly described as breaking their own stated risk rule ("we never wanted to get in a position where the residual component was 50% of the valuation... we broke this rule a few times").
- **Misaligned lender incentives and herd dynamics throughout the financing chain**: loan officers compensated on loan *volume* rather than loan *quality* ("he will find a way to make loans"), supposedly-independent appraisers "rubber-stamping" deals to avoid losing future business, and competitive pressure not to be the one firm sitting out a hot market — "one big complicitous circle. No one wanted to say no."
- **Institutional amnesia**: the chapter's closing quote on this point is worth keeping verbatim — "All it takes is just one generation. A generation of bankers and developers to churn through. A generation that hasn't been through the cycles." Knowledge of the pattern doesn't reliably transmit across personnel turnover, so each new generation of decision-makers effectively relearns the lesson the hard way.

## The Controlled Experiment That Confirms the Interviews Weren't Just Talk

Bakken (1993) built a management flight simulator directly on the causal structure above and had **professional developers from one of the largest US real estate firms at the time** play it, alongside MIT MBA students. **The professionals performed no better than the students** — both groups badly underperformed a simple benchmark investment rule that explicitly accounted for the supply line. Learning across repeated plays was slow, and what little learning occurred transferred poorly to changed market conditions. **The single most telling detail**: when professional players went bankrupt in the simulation, they frequently blamed the *model*, insisting real-world prices "could never drop so far or so fast" — and the source notes dryly that a few years later, in reality, most of those same professionals had lost everything. This is the controlled-experiment version of exactly the [[barriers-to-learning-and-virtual-worlds]] finding that misperceptions of feedback are robust to expertise, financial stakes, and market institutions — real money and real careers did not protect against the identical structural failure novices show in the Beer Game.

## 17.5 Chapter Summary

Every supply chain is built from the generic stock-management structure (target stock, acquisition/loss rates, and — whenever there's a real delay — a supply line requiring its own explicit management). **Oscillation specifically requires both a time delay in a negative feedback loop *and* a failure by the decision-maker to account for that delay** — neither condition alone is sufficient. The chapter's closing diagnosis is worth keeping as the master explanation tying every case in this chapter together: the failure to track the supply line isn't fundamentally an information problem (better measurement systems could fix it, if people understood they needed them) or fundamentally an incentive problem (compensation could be redesigned, if investors understood the structural risk) — it traces back to **flawed mental models of dynamically complex systems**, which then shape the very institutions, information systems, and incentive structures that perpetuate the same flawed models. **The closing, slightly grim note**: ignoring time delays reliably produces unpleasant surprises, which reinforces the belief that markets/business are simply "capricious and unpredictable" rather than structurally explicable — strengthening exactly the short-term, reactive mental model that caused the problem in the first place.

## Connects to

- [[beer-game-and-origin-of-oscillations]] — this case is the chapter's proof that the Beer Game's "toy" finding generalizes to real, high-stakes, multi-year asset markets run by sophisticated professionals, not just an artifact of a simplified classroom exercise.
- [[barriers-to-learning-and-virtual-worlds]] — the interview material is a rich, real-world confirmation of nearly every barrier from that chapter: detail-complexity focus over dynamic-complexity awareness (1.3.1), confirmation bias toward "this time is different" (1.3.7), and misperceptions of feedback robust to expertise and stakes (1.3.4).
- understanding-resistance-faces-and-underlying-concerns — the developers' own described ego/identity investment in their projects directly parallels Block's resistance material on why people defend positions even against overwhelming disconfirming evidence.
- management-by-abdication and fatal-assumption-and-technician-takeover — the institutional-amnesia finding (it takes "one generation" to relearn) parallels the E-Myth's warning about knowledge that lives only in people's heads and disappears when they leave.

## North Star Connection

- How this applies to the audit business: this case is an unusually rich, directly quotable source of client-communication material for any engagement touching capital investment, capacity expansion, or competitive-supply tracking — the failure modes documented here (trend extrapolation instead of structural analysis, no formal pipeline tracking, sunk-cost ego investment, models built to persuade rather than to test) are generic enough to show up in a contractor's bidding/capacity decisions, not just commercial real estate. The interview methodology itself (ask neutral questions first, only prompt directly about structural concepts if the subject doesn't raise them unprompted) is a directly reusable discovery technique for assessing whether a client team genuinely understands the dynamic structure of their own market or is operating on pure trend extrapolation.
- Track relevance: Business / Systems — among the richest available sources of real, on-the-record evidence for why sophisticated professionals fail at exactly the diagnostic Chris is positioned to supply; directly supports the audit-discovery methodology track.
- Possible future Second Brain use: the open-ended-then-prompted interview technique (used to distinguish genuine structural understanding from rehearsed answers) is a strong candidate addition to a client-discovery interview protocol; the seven named failure mechanisms are a strong candidate checklist for diagnosing any client's capacity/investment decision-making process.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | An unusually rich source of real, on-the-record professional failure modes directly transferable to any capacity/investment audit |
| Current usefulness | 5 | The seven named failure mechanisms are immediately usable as a client diagnostic checklist |
| KSU support | 5 | A landmark, heavily field-researched case combining interviews, archival data, and a controlled experiment |
| Tech-stack relevance | 1 | Conceptual case study, no direct tool dependency |
| Business audit value | 5 | The interview methodology and the seven failure mechanisms are both directly reusable, high-value audit techniques |
| Data/workflow value | 4 | The neutral-then-prompted interview technique is a concrete, transferable data-collection method |
| Reading urgency | 4 | Closes out Chapter 17 with the richest case-study material in the chapter |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client-discovery interview technique and diagnostic checklist — use the neutral-then-prompted questioning method to assess whether a client team genuinely understands their market's structural dynamics or is operating on pure trend extrapolation, and check for the seven named failure mechanisms (trend extrapolation, no pipeline tracking, sunk-cost ego investment, persuasion-not-inquiry models, speculative reliance, misaligned incentives, institutional amnesia) in any capacity/investment decision review.

**Use when**:
Auditing a client's capital investment, capacity expansion, or competitive-supply-tracking process, especially one involving long lead times between a decision and its market effect.

**Do not use when**:
The client's decisions involve no meaningful lead time or competitive supply dynamic (e.g., a simple, fast-turnaround retail reorder) — the full real-estate-cycle framing would overcomplicate a short-cycle decision.

**Fast retrieval query**:
`subject/real-estate-cycles` + `subject/groupthink` — or search "Chicago real estate cycle Hoyt 1933" / "developers location location location" / "one generation bankers developers churn through" / "Bakken real estate flight simulator professionals bankrupt"
