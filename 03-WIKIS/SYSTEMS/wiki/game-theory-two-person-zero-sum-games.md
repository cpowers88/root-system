---
domain: systems
type: framework
tags: [priority/now, status/wiki-only, domain/systems, source-role/primary, use-case/systems-analysis, use-case/operations-research, use-case/ksu-support, subject/game-theory, subject/minimax, subject/operations-research]
---

# Game Theory: Two-Person Zero-Sum Games, Dominated Strategies, Saddle Points, and Mixed Strategies

**Summary**: The formal framework for a decision made against a *rational, self-interested* opponent — not the passive, random "nature" of decision analysis. Covers eliminating dominated strategies, the minimax/maximin criterion, why some games have a stable ("saddle point") pure-strategy solution and others require randomized mixed strategies, and the graphical solution procedure for the two-undominated-strategy case.

**Sources**: IntroductiontoOpersationsResearch.pdf (Hillier & Lieberman, *Introduction to Operations Research*), Chapter 15 ("Game Theory"), sections 15.1–15.4 in full (pp. 661–672 printed / physical ~691–702); section 15.5 (LP formulation of general games) at conceptual level

**Last updated**: 2026-07-13**

---

## Game Theory vs. Decision Analysis

Both frameworks use a payoff table and both apply a form of minimax/maximin reasoning — but they differ in one crucial assumption. **Decision analysis** ([[decision-analysis-and-utility-theory]]) treats the "opponent" as nature — passive, random, not out to get you. **Game theory** assumes the opponent is a **rational, self-interested player** actively trying to win, which is why the maximin criterion (overly conservative for decision analysis, where it's just one of three competing criteria) is the *central* tool here — against a truly rational adversary, planning for their worst-case response isn't pessimism, it's realism.

A **two-person, zero-sum game** is defined by: each player's set of **strategies**, and a **payoff table** (given only for player 1, since player 2's payoff is always its negative — one player's gain is exactly the other's loss). Both players know the full payoff table and both players' strategy sets in advance; the actual play is simultaneous, without knowing the opponent's choice.

## Dominated Strategies

**A strategy is dominated if another available strategy is always at least as good, regardless of what the opponent does** — a dominated strategy can be eliminated immediately, no further analysis needed. Eliminating dominated strategies can cascade: removing one player's dominated strategy can reveal a *new* dominated strategy for the *other* player (since a rational opponent knows the first player will never use the eliminated option), and so on. In the simplest cases, successive elimination narrows the game all the way down to a single remaining strategy pair — the entire game is solved without any further machinery.

## The Minimax Criterion and Saddle Points

When dominated-strategy elimination doesn't fully resolve the game, apply the **minimax criterion**: each player selects the strategy that's best *even if announced to the opponent in advance* — player 1 picks the strategy with the largest *minimum* payoff (**maximin**); player 2 picks the strategy with the smallest *maximum* payoff to player 1 (**minimax**). 

**When the maximin value equals the minimax value**, that shared value is called a **saddle point**, and it's a genuinely **stable (equilibrium) solution**: neither player has any incentive to unilaterally switch, because doing so only makes their own position worse — even if the opponent's strategy is fully known in advance. The **value of the game** is this payoff; a game with value 0 is a **fair game**.

**When they differ (no saddle point), pure-strategy play is inherently unstable** — each player, reasoning about the other's rational best response, would keep wanting to switch strategies in an endless cycle (illustrated directly by the coin-flip-style "odds and evens" game: always showing the same number of fingers lets a rational opponent exploit the pattern completely).

## Mixed Strategies: The Answer When There's No Saddle Point

When no saddle point exists, the rational solution is to **randomize** — assign a probability distribution over your own pure strategies (a **mixed strategy**) and use a physical randomization device (a coin flip, etc.) to actually choose at play time, so that *even you* don't know your choice until the moment of play — this is the only way to guarantee the opponent can't exploit predictability, even a partial, statistically-detected pattern.

**Expected payoff** for a pair of mixed strategies (x for player 1, y for player 2): `Σᵢ Σⱼ pᵢⱼ·xᵢ·yⱼ`, where pᵢⱼ is the pure-strategy payoff. The minimax criterion extends directly to mixed strategies: each player picks the mixed strategy maximizing (player 1) or minimizing (player 2) their guaranteed expected payoff.

**The minimax theorem** (the central theoretical result): for *any* two-person zero-sum game, allowing mixed strategies, the optimal mixed-strategy pair always achieves maximin value = minimax value = the value of the game — i.e., **every such game has a stable solution once mixed strategies are allowed**, even when no pure-strategy saddle point exists. This is a strong, general guarantee — no two-person zero-sum game is ever fundamentally unsolvable in this framework.

## The Graphical Solution Procedure (Two Undominated Strategies)

When one player (after eliminating dominated strategies) has only two remaining pure strategies, the game can be solved graphically: plot the opponent's expected-payoff line (as a function of the two-strategy player's mixing probability x1) for each of the opponent's pure strategies. The two-strategy player's optimal x1 is where the **lower envelope of these lines peaks** (the maximin point) — found algebraically by setting the two relevant lines equal and solving. The opponent's optimal mixed strategy is then recovered by requiring their expected-payoff line to be exactly horizontal at the value of the game, using only the pure strategies whose lines pass through the maximin point (any strategy whose line doesn't pass through that point gets probability zero — including it would only pull the expected payoff away from the equilibrium value).

**For larger games** (more than two undominated strategies for both players), the standard approach transforms the game into an equivalent linear program, solvable directly by the simplex method (see [[simplex-method-mechanics]]) — game theory and linear programming are, in this sense, the same underlying mathematics viewed from two different framings.

## Key Takeaways

- Game theory's minimax reasoning is only the *right* default when the counterpart is genuinely rational and adversarial — the same reasoning applied to a random, passive "nature" (decision analysis's domain) is needlessly pessimistic.
- Dominated-strategy elimination is cheap, always worth trying first, and occasionally solves the whole game outright.
- A saddle point (maximin = minimax) means the game has a stable pure-strategy solution; its absence isn't a failure of the theory — it's the correct signal that rational play requires randomization.
- The minimax theorem guarantees every two-person zero-sum game is solvable once mixed strategies are allowed — there's no such thing as a truly unsolvable case in this framework, only cases requiring the mixed-strategy machinery instead of a simple lookup.
- Every game with mixed strategies reduces to an LP — the same simplex machinery from earlier in this ingest applies here too.

## Connects to

- [[decision-analysis-and-utility-theory]] — the sibling probabilistic-OR framework; explicitly contrasted here (rational adversary vs. passive random "nature") despite superficially similar payoff-table structure and minimax-flavored reasoning.
- [[linear-programming-formulation-and-graphical-solution]] and [[simplex-method-mechanics]] — any game with mixed strategies (beyond the two-undominated-strategy graphical case) is solved by transforming it into an equivalent LP.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 3 | Genuinely competitive-strategic client situations (pricing wars, competitive bidding) are less common in SMB operational-waste audits than decision-analysis-under-uncertainty situations, but real when they occur |
| Current usefulness | 2 | No active engagement needs this yet; narrower applicability than decision analysis or LP |
| KSU support | 5 | Standard intro-OR chapter, directly referenced by and complementary to the Decision Analysis chapter already ingested |
| Tech-stack relevance | 2 | Mixed-strategy solving for larger games routes through an LP solver (PuLP/SciPy) already covered by earlier pages; the graphical two-strategy case is simple enough for hand/spreadsheet solving |
| Business audit value | 2 | Most applicable to genuinely competitive-strategic scenarios (bidding against a specific known rival, pricing games) rather than typical internal-operations audit findings |
| Data/workflow value | 2 | Requires a genuine adversarial payoff structure with a known/estimable competitor payoff table — less commonly available than typical audit data |
| Reading urgency | 3 | Third of "chunk 3" — short chapter, complements Decision Analysis directly, but narrower practical applicability than the other OR material ingested |

**Overall priority**: NEXT

## Use / Retrieval Notes

**Best use**:
Analyzing a genuinely competitive-strategic decision against a specific, rational rival (competitive bidding, pricing strategy against a known competitor) where decision analysis's "passive nature" framing doesn't fit.

**Use when**:
The "opponent" is an actual rational, self-interested actor actively trying to win against you — not random uncertainty.

**Do not use when**:
The uncertainty is genuinely random/environmental rather than adversarial — use decision analysis instead (see [[decision-analysis-and-utility-theory]]), which is the correct framework for passive-nature uncertainty and is far more commonly applicable in SMB audit work.

**Fast retrieval query**:
`subject/game-theory` + `subject/minimax` — or search "dominated strategy" / "saddle point" / "mixed strategy minimax theorem" / "graphical solution procedure games"

## North Star Connection

- How this applies to the audit business: narrower applicability than most OR material ingested so far — most useful for the rarer client situation involving genuine competitive strategy (bidding, pricing against a specific rival) rather than typical internal-operations waste-finding.
- Track relevance: KSU — solidly standard intro-OR content; Business relevance is real but narrower than Decision Analysis or LP.
- Possible future Second Brain use: Lower priority than other OR material — a reusable tool here would need a genuinely adversarial-strategy client scenario to justify building.
