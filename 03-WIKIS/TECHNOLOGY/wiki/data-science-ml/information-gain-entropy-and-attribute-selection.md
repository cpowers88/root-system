---
domain: technology
type: concept
tags: [subject/data-science, subject/information-gain, subject/entropy, subject/attribute-selection]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow, audit]
stack: [ai-frameworks-apis]
---

# Information Gain and Entropy: How to Mathematically Ask "Which Variable Actually Tells Me Something?"

**Summary**: The formal vocabulary for predictive modeling (instance, feature, target, induction, training data) and the chapter's first concrete data mining technique — entropy as a precise measure of how "mixed up" a group is with respect to what you're trying to predict, and information gain as the resulting score for how much a candidate attribute actually reduces that mixed-upness. Worked through a real mushroom-edibility dataset where one single attribute (odor) turns out to carry almost all the predictive signal.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 3 ("Introduction to Predictive Modeling: From Correlation to Supervised Segmentation")

**Last updated**: 2026-06-22

---

## The Core Vocabulary, Precisely

**A model is a simplified representation of reality created to serve a purpose** — the same map/blueprint analogy used throughout data science, deliberately abstracting away whatever's irrelevant to the specific decision at hand. **A predictive model specifically is a formula (mathematical, logical/rule-based, or a hybrid) for estimating an unknown value — the target.** **A genuinely useful terminology correction worth keeping**: "prediction" in data science doesn't require the unknown value to be in the *future* — it just has to be currently unknown to the model at decision time, even if it already happened (a fraud-detection model "predicts" whether a *past* transaction was fraudulent, using data available right now). **Descriptive modeling is the named alternative purpose**: not estimating a value, but gaining insight into the underlying *process* — a descriptive churn model tells you what churners typically look like, valued partly for intelligibility even at some cost to raw accuracy, where a purely predictive model can in principle be judged on accuracy alone (though the book flags that intelligibility still matters for predictive models too, for reasons developed later).

**The instance/feature/target/induction vocabulary, worth keeping precise since the same concepts go by different names across statistics, ML, and operations research**: an **instance** (row, example, case) is described by **attributes/features** (columns, variables, predictors, independent variables); the **target variable** (label, dependent variable) is the thing being predicted, and — a subtlety worth flagging explicitly — **the target is never used to predict itself, but its *past* values can absolutely be used as a feature to predict its *future* values.** **Induction** is the philosophical term (generalizing from specific cases to general rules) applied to the process of building a model from data; the **induction algorithm/learner** is what does the inducing; **training data** is the input to that process, and it's called **labeled data** specifically because the target's value is known for every training instance.

## Supervised Segmentation: The Plain-Language Goal Behind the Math

**The intuitive framing worth keeping as the conceptual anchor for everything else in this page**: a predictive model is, at root, an attempt to segment a population into subgroups that have *different* target values on average — and ideally, that segmentation comes with a human-readable description ("middle-aged professionals who reside in New York City have a 5% churn rate"). **The fundamental question this whole chapter exists to answer**: given many candidate attributes and no prior idea which ones matter, how do you *automatically* find — and even rank — the attributes that actually carry useful information about the target, rather than relying on an analyst's guesswork?

## Entropy: A Precise Number for "How Mixed Up Is This Group?"

**Entropy** measures the disorder of a set with respect to some property of interest — in supervised learning, that property is the target variable's value. entropy = −p₁log(p₁) − p₂log(p₂) − ... where each pᵢ is the proportion of the set belonging to class i. **The two boundary cases worth keeping as intuition anchors**: entropy = 0 when a set is perfectly pure (every member shares the same target value — zero disorder); entropy is maximized (=1, for a two-class problem with log base 2) when the classes are perfectly balanced (50/50 — maximum disorder, since you genuinely have no information advantage either way). **A worked, concrete number for calibration**: a set of 10 people, 7 non-write-offs and 3 write-offs, has entropy(S) = −(0.7×log₂0.7) − (0.3×log₂0.3) ≈ 0.88 — fairly disordered, but not maximally so, since the split is moderately (not perfectly) unbalanced.

## Information Gain: How Much Does *This Specific Attribute* Actually Help?

Entropy alone only describes one set's disorder; **information gain (IG)** is the score for how much a *candidate split* on a given attribute reduces entropy, comparing a parent set's entropy to the **weighted average** of its resulting children's entropies: IG(parent, children) = entropy(parent) − [p(c₁)×entropy(c₁) + p(c₂)×entropy(c₂) + ...]. **The weighting-by-proportion step is the precise fix for an otherwise tempting but wrong intuition**: splitting off one single pure instance "looks" like a great result locally, but contributes almost nothing to information gain once it's properly weighted by how small a fraction of the population it actually represents — **a large, reasonably pure split is generally worth more than a tiny, perfectly pure one**, and the weighting in the formula enforces that automatically rather than requiring a separate ad hoc rule.

**The chapter's worked illustration, worth keeping as a template for reasoning through any future split-quality comparison by hand**: splitting a credit-write-off dataset (entropy ≈ 0.99, nearly maximally disordered) on Balance < 50K vs. ≥ 50K produces an information gain of ≈ 0.37 — a substantial reduction. **Splitting the identical parent set on a three-valued Residence attribute (OWN/RENT/OTHER) instead produces only IG ≈ 0.13** — lower, because even though the OWN branch is genuinely much purer than the parent, the RENT and OTHER branches come out essentially **no purer than the original, undivided population**, dragging the weighted average back down. **The general, reusable lesson**: a split can have one excellent child and still score poorly overall if its other children add no real purity gain — information gain correctly penalizes this, where eyeballing just the "best-looking" branch of a candidate split would mislead.

**Information gain handles every one of the chapter's stated complications cleanly, by construction, without special-casing**: it doesn't require any branch to be perfectly pure; it works for splits with any number of resulting branches (not just binary); and the weighting automatically favors splits that produce larger, meaningfully purer groups over ones that merely carve off a tiny, accidentally-pure sliver. **Numeric attributes require one extra step**: they must first be "discretized" — choosing one or more threshold split points and treating the result as a categorical split — and the chapter's stated approach is conceptually brute-force but effective: **try all reasonable candidate split points and keep whichever produces the highest information gain.** **For regression problems (a numeric target), entropy/information gain don't directly apply** — the natural analogous purity measure is **variance**: a pure set (identical target values) has zero variance; the equivalent of information gain becomes the weighted-average *reduction* in variance from parent to children, the identical conceptual move, just swapping the underlying purity metric.

## The Mushroom Dataset: A Case Where One Attribute Does Almost All the Work

The chapter's worked example (5,644 real mushroom samples, 2,156 poisonous / 3,488 edible, from the UCI ML repository / Audubon Field Guide) computes information gain across roughly twenty candidate attributes for predicting edibility. **The parent dataset's overall entropy is 0.96** (close to maximally disordered, since the classes are only mildly imbalanced). GILL-COLOR and SPORE-PRINT-COLOR both reduce entropy *somewhat*, but **ODOR dominates every other attribute by a wide margin** — many individual odor values (almond, creosote, musty, and others) produce **zero-entropy** partitions on their own (an odor value that's *completely* characteristic of either edible or poisonous), and only the "no odor" value retains meaningful uncertainty (≈20% of the population). **The result**: ODOR alone reduces the dataset's total entropy from 0.96 down to about 0.1 — an information gain of roughly 0.86, dramatically higher than any competing attribute. **The chapter's own dry, important caveat, worth keeping verbatim as a standing reminder that a high information-gain number is not by itself a guarantee of real-world reliability**: this assumes "odor can be measured accurately... if your sense of smell is poor you may not want to bet your life on it" — and, more broadly, "you probably wouldn't want to bet your life on the results of mining data from a field guide" at all. **The general, transferable lesson behind the joke**: a strong information-gain score tells you an attribute is statistically informative *within the dataset you measured it on* — it says nothing about whether that attribute can actually be measured reliably, or whether the dataset itself is a trustworthy enough proxy for the real-world decision you actually care about.

## Connects to

- [[canonical-data-mining-tasks-and-supervised-unsupervised]] — this page's entropy/information-gain math is the concrete technical mechanism behind that page's supervised-task framing (finding informative variables once a target is defined).
- [[tree-induction-and-decision-boundaries]] — the companion page showing how repeated, recursive application of information-gain-based attribute selection produces a full classification tree, not just a single best split.
- [[sql-grouping-and-aggregate-functions]] — entropy and information gain are a more formal, predictive-purpose-built cousin of the basic data-quality `GROUP BY`/`COUNT` checks already covered in the SQL material; both ask "how is this population actually distributed," just for different ends.

## North Star Connection

- How this applies to the audit business: information gain is a directly implementable, low-overhead first analytical step for any client engagement with a defined outcome of interest (which customers/jobs/equipment have problem X) and a pile of candidate explanatory variables — running attribute-by-attribute information gain rankings (even by hand, conceptually, before reaching for full modeling software) quickly surfaces which variables actually deserve further attention, exactly as it did for the churn and mushroom examples. The "don't bet your life on field-guide data" caveat is a good, memorable client-facing caution against over-trusting a high information-gain score computed on a small or unreliable dataset.
- Track relevance: Tech — foundational quantitative technique for the data-workflow track, directly extending the already-ingested pandas/SQL skills into actual predictive-variable selection.
- Possible future Second Brain use: a simple "information gain attribute ranker" (a reusable pandas/Python snippet computing entropy and information gain for a given target and candidate attributes) is a strong, near-ready candidate tool for the technology track.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | A directly implementable, low-overhead first analytical step for any client dataset with a defined target |
| Current usefulness | 4 | Immediately applicable once a client dataset and target variable exist; requires that prerequisite |
| KSU support | 4 | Strong, rigorous quantitative content with real information-theoretic grounding (Shannon) |
| Tech-stack relevance | 5 | Directly extends existing `stack/python` and `stack/sql-sqlite` skills into predictive attribute selection |
| Business audit value | 4 | A fast, transparent way to show a client which of their variables actually matter, before committing to a full model build |
| Data/workflow value | 5 | A concrete, reusable data-analysis technique directly applicable to any labeled client dataset |
| Reading urgency | 5 | Foundational technique underlying the rest of the book's predictive-modeling chapters |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Fast attribute-ranking technique — given any client dataset with a defined target variable, compute entropy and information gain across candidate predictors as a quick, transparent first pass before committing to a full model build.

**Use when**:
A client has a labeled historical dataset (a defined outcome of interest, like churn/default/equipment failure) and wants to know which of many candidate variables actually matter.

**Do not use when**:
No target variable is defined yet (this is purely a supervised technique), or the dataset is too small/unreliable to trust a high information-gain score (per the mushroom-dataset caveat).

**Fast retrieval query**:
`subject/information-gain` + `subject/entropy` — or search "entropy formula purity measure" / "information gain weighted children" / "mushroom dataset ODOR highest information gain" / "discretizing numeric attributes split point"
