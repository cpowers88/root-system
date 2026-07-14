---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/decision-analysis, subject/utility-theory, subject/bayes-theorem, subject/operations-research]
---

# Decision Analysis: Decision Criteria, Bayes' Theorem, Decision Trees, and Utility Theory

**Summary**: A structured framework for choosing among alternatives under uncertainty — three competing decision criteria (maximin, maximum likelihood, Bayes' decision rule), how to formally value whether it's worth paying for more information (EVPI/EVE) before deciding, decision trees as the standard way to solve multi-stage decisions by backward induction, and utility theory for when raw expected-dollar-value doesn't match how a real decision maker actually weighs risk.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 16 ("Decision Analysis"), sections 16.2–16.4 in full (decision criteria, experimentation/Bayes' theorem, decision trees), 16.6 in full (utility theory) — the running Goferbroke Co. example (pp. 682–701 printed / physical ~713–732)

**Last updated**: 2026-07-13

---

## The Decision Analysis Framework

A decision maker picks one **decision alternative** from a known set. The outcome also depends on an uncertain **state of nature** outside the decision maker's control. Every (alternative, state) combination has a known **payoff** (usually money), organized into a **payoff table**. Prior beliefs about which state is more likely are the **prior probabilities** (a **prior distribution**).

This is structurally similar to a two-player zero-sum game (see game theory) with "nature" as the passive second player — but nature isn't malicious, it's random, which is exactly why the game-theory maximin criterion often isn't the right tool here.

## Three Decision Criteria (No Experimentation)

Using the running example (Goferbroke Co.: drill for oil, payoff $700K if oil / −$100K if dry, vs. sell the land for a certain $90K; prior P(oil)=0.25):

- **Maximin payoff criterion**: for each alternative, find its worst-case payoff; pick the alternative whose worst case is best. Extremely conservative — assumes nature is out to get you. For Goferbroke: sell the land (guaranteed $90K beats drilling's worst case of −$100K).
- **Maximum likelihood criterion**: identify the *most probable* state of nature, then pick the best alternative *for that state only*. Ignores everything about less-likely-but-still-possible states — including a big, attractive payoff sitting behind a low-probability state. For Goferbroke: also sell (dry is the more likely state).
- **Bayes' decision rule** (the standard choice): compute the *expected* payoff for each alternative across all states, weighted by prior probability; pick the alternative with the highest expected payoff. For Goferbroke: E[drill] = 0.25(700) + 0.75(−100) = 100 > E[sell] = 90 → **drill**. Only this criterion reverses the other two, because it's the only one that actually weighs the attractive-but-unlikely upside.

**Sensitivity analysis on the prior**: since priors are often the shakiest number in the model, plot expected payoff vs. the prior probability for each alternative — the **crossover point** where the optimal choice flips is the single most useful number to sanity-check against real-world judgment. For Goferbroke, the crossover is at P(oil) = 0.2375 — below it, sell; above it, drill.

## Decision Making With Experimentation: Posterior Probabilities

Before committing, it's often possible to buy more information (a test, a survey, a pilot). This updates priors into **posterior probabilities** via **Bayes' theorem**:

```
P(state | finding) = P(finding | state)·P(state) / Σ_k P(finding | state_k)·P(state_k)
```

A **probability tree diagram** organizes this cleanly: prior probabilities × conditional probabilities (P(finding|state), known from past experience with the test) → joint probabilities → normalize by the finding's total probability → posterior probabilities. Once posteriors are in hand, Bayes' decision rule runs exactly as before, just with posteriors replacing priors (and the experiment's cost subtracted from the payoff).

**Deciding whether the experiment is even worth running** — two complementary bounds, computed *before* running it:

- **Expected Value of Perfect Information (EVPI)** = (expected payoff assuming the experiment removes *all* uncertainty) − (expected payoff without any experimentation). This is an *upper bound* — real experiments are never perfect, so if EVPI itself doesn't beat the experiment's cost, don't bother computing anything more precise; the answer is already no.
- **Expected Value of Experimentation (EVE)** = (expected payoff actually achievable *with* the real, imperfect experiment, weighting each possible finding by its probability) − (expected payoff without experimentation). This is the real, precise answer — but requires doing the full posterior-probability calculation first, which is why EVPI is checked first as a cheap screening bound.

For Goferbroke: EVPI = 142.5 (≫ the $30K survey cost, so worth investigating further); EVE = 53 (still > $30K cost) → the seismic survey should be conducted.

## Decision Trees: Solving Multi-Stage Decisions by Backward Induction

A decision tree visualizes a *sequence* of decisions and random events as a branching structure: **decision nodes** (squares — a choice point) and **event/chance nodes** (circles — a random outcome), each labeled with payoffs (cash flows) and, on event-node branches, probabilities.

**Solving procedure — always right to left (backward induction):**
1. Start at the rightmost column of nodes and move left one column at a time.
2. **At each event node**: compute its expected payoff = Σ (branch payoff × branch probability). Record this value at the node.
3. **At each decision node**: compare the expected payoffs of its branches; keep the best one (mark rejected branches with a double-dash), and record that best value at the node.
4. Repeat leftward until reaching the initial decision node — its recorded value is the overall optimal expected payoff.

The tree is *solved* right-to-left but *read* left-to-right: following only the un-dashed branches from the root gives the actual optimal policy — a full contingency plan ("do the survey; if unfavorable, sell; if favorable, drill"), not just a single action.

## Utility Theory: When Expected Dollars Isn't the Right Measure

Real decision makers routinely reject a higher-expected-value gamble for a lower-but-certain payoff (most people prefer a certain $40K over a 50/50 shot at $100K, even though the gamble's expected value is $50K). This isn't irrational — it means the decision maker's utility for money isn't linear.

- **Risk-averse**: decreasing marginal utility (each additional dollar matters less than the last) — the common case for consequential amounts of money.
- **Risk-seeking**: increasing marginal utility — rare, but real for some individuals/contexts.
- **Risk-neutral**: utility strictly proportional to money — the implicit assumption whenever Bayes' decision rule is applied directly to raw payoffs; usually only realistic for small stakes.

**The fundamental property**: a decision maker is indifferent between two alternatives if and only if they have the same *expected utility* — this is what makes utility-weighted Bayes' decision rule work at all.

**The equivalent lottery method** for actually building a utility function: (1) assign U(worst payoff) = 0 and U(best payoff) = 1 (the scale itself is arbitrary — any positive linear transformation preserves which alternative wins); (2) for any intermediate payoff M, ask the decision maker: *what probability p makes you indifferent between definitely receiving M, versus a lottery paying the best outcome with probability p and the worst outcome with probability (1−p)?* — then U(M) = p. Repeat for enough intermediate values to sketch the curve. Applying utility values (instead of raw dollars) inside Bayes' decision rule can *reverse* the raw-dollar-optimal decision — for Goferbroke, a cash-constrained owner's genuine risk aversion around the possibility of a $130K loss (survey cost + dry hole) can flip the optimal policy relative to the pure expected-monetary-value analysis.

## Key Takeaways

- Bayes' decision rule (maximize expected payoff) is the standard criterion, but maximin and maximum-likelihood exist for good reasons (extreme risk aversion; focusing analysis effort on the dominant scenario) — know when each is actually the right tool, not just default to Bayes reflexively.
- EVPI is a cheap, fast screening bound computed *before* deciding whether a more expensive, precise EVE calculation is even worth doing — never skip straight to running an expensive experiment/survey without this check.
- Decision trees are just Bayes' decision rule (and EVE reasoning) organized visually for multi-stage problems — the backward-induction solving procedure is mechanical once the tree is built correctly.
- Utility theory exists because "maximize expected dollars" silently assumes risk-neutrality — for any decision where the stakes are large relative to the decision maker's resources (exactly the situation most SMB clients are in), that assumption should be checked, not assumed.

## Connects to

- [[linear-programming-formulation-and-graphical-solution]] — decision analysis and LP are sibling deterministic/probabilistic optimization frameworks in the same OR toolkit; sensitivity analysis (crossover points here, allowable ranges there) plays an analogous role in both.
- [[sensitivity-analysis-and-postoptimality]] — the same "how much can my estimate be wrong" discipline applied here to prior probabilities instead of LP parameters.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | Decision trees + EVPI/EVE are directly usable, non-technical-sounding tools for structuring and defending any client "should we invest in X first" or "is it worth paying for more data before deciding" question |
| Current usefulness | 4 | No active engagement needs this yet, but of everything ingested so far this is the most immediately client-conversation-ready |
| KSU support | 5 | Standard, heavily-tested intro-OR chapter |
| Tech-stack relevance | 2 | Straightforward to build as a simple spreadsheet or Python decision-tree calculator; no specialized solver needed |
| Business audit value | 5 | "Is it worth paying for a pilot/survey/data study before committing" is one of the most common real SMB decision-under-uncertainty questions, and EVPI/EVE gives a rigorous, quick answer |
| Data/workflow value | 3 | Requires payoff estimates and prior probabilities from the client — usually elicited through structured conversation, not pulled from existing data |
| Reading urgency | 4 | First of the "chunk 2" probabilistic-OR pages; genuinely novel content, no overlap with anything already in this wiki |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Structuring a client's "should we invest/commit now, or pay for more information first" decision — build the payoff table, compute EVPI as a fast screening check, then a decision tree if the decision has multiple stages.

**Use when**:
A client faces a genuinely uncertain decision with identifiable alternatives and states of nature, especially when there's an option to reduce uncertainty (survey, pilot, test) before committing.

**Do not use when**:
The "states of nature" aren't really random/uncertain but reflect a competing rational actor's strategic choice — that's game theory's territory, not decision analysis's, despite the superficial payoff-table similarity.

**Fast retrieval query**:
`subject/decision-analysis` + `subject/utility-theory` — or search "Bayes decision rule" / "expected value of perfect information" / "decision tree backward induction" / "equivalent lottery method" / "risk averse utility function"

## North Star Connection

- How this applies to the audit business: EVPI/EVE gives a fast, rigorous answer to "should the client pay for a pilot program or more data before committing to a bigger investment" — a genuinely differentiated, quantified deliverable most competitors won't offer. Utility theory is the honest answer to "the math says invest, but the client is nervous" — it's not irrationality, it's risk aversion, and it can be modeled rather than dismissed.
- Track relevance: Systems / KSU / Business — high across all three, and the most directly client-conversational of the OR material ingested so far.
- Possible future Second Brain use: Yes — a simple decision-tree + EVPI/EVE Python or spreadsheet template is a strong, fast-to-build candidate for the capability library.
