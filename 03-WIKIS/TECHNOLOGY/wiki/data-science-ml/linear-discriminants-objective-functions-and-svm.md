---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, use-case/audit, subject/data-science, subject/linear-models, subject/support-vector-machines, subject/objective-functions, stack/ai-frameworks-apis]
---

# Parametric Modeling: Why "Best Fit" Is a Choice You Make, Not a Fact You Discover

**Summary**: A second, fundamentally different way to build a predictive model — instead of recursively splitting the data (tree induction), specify the *form* of a mathematical function up front and let the data determine its parameters. The single most important, easy-to-overlook idea in this approach: there is no universal definition of "best fit" — every parametric technique secretly encodes a specific choice of objective function, and support vector machines turn out to be nothing more mysterious than one particular, well-motivated choice of that objective.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 4 ("Fitting a Model to Data")

**Last updated**: 2026-06-22

---

## Parametric Modeling: A Genuinely Different Strategy From Tree Induction

**The core distinction from [[tree-induction-and-decision-boundaries]], worth keeping precise**: tree induction *discovers* both the model's structure and its parameters simultaneously, through recursive splitting. **Parametric modeling inverts this** — the data scientist specifies the *form* of the model in advance (most commonly, a weighted sum of numeric attributes), leaving only the numeric weights unspecified, and the data mining procedure's entire job is to find the weight values that make this pre-chosen form fit the data as well as possible. **A useful terminology note for anyone with a statistics background**: in some statistical/econometric traditions, "the model" technically refers only to the bare structural equation *before* its parameters are fit — this book uses "the structure of the model" for that bare equation, reserving "model" for the fully fit, ready-to-use version.

## Decision Boundaries Don't Have to Be Axis-Perpendicular

**The chapter's key visual motivation for this whole new family of techniques**: a classification tree's decision boundaries are always perpendicular to a single attribute's axis (since each node tests exactly one attribute), producing a "staircase"-shaped partition of the feature space. **Stripping away those axis-parallel lines and looking at the raw data points often reveals that a single straight line — at any angle, not just horizontal or vertical — would separate the classes almost perfectly.** **This single observation is the entire motivation for linear discriminant functions**: a model defined as a weighted sum of the attributes, f(x) = w₀ + w₁x₁ + w₂x₂ + ..., classifies an instance by checking whether f(x) is positive or negative — geometrically, whether the point falls above or below (in two dimensions) the line the weights define. **In three dimensions the boundary is a plane; in higher dimensions, a "hyperplane"** — directly the same geometric vocabulary already introduced for tree decision boundaries, now generalized to *any* orientation rather than only axis-parallel ones.

**The weights themselves carry an intuitive, if loose, interpretation worth keeping as a quick mental shortcut**: a feature's weight magnitude is roughly its importance for the classification — a near-zero weight means that feature can typically be ignored or dropped, a large-magnitude weight (positive or negative) means that feature is pulling the decision strongly in one direction.

## The Central Problem: Infinitely Many Lines Can All Fit Perfectly

**The chapter's sharpest illustration of why fitting a linear model is genuinely harder than it first appears**: given training data that's perfectly linearly separable, there are typically **infinitely many different lines** that separate the two classes with zero training error — each with a different slope and intercept, each representing a meaningfully different model. **This forces the single most important and most-overlooked question in all of parametric modeling, worth keeping as the standing discipline before trusting any "best fit" model**: what exactly do we mean by "best"? **The chapter's explicit, blunt framing**: a fitted model's weights are only "best" relative to whatever objective function was chosen to evaluate them — and that choice is rarely a neutral, objective fact; it's a modeling decision, made (often implicitly) based on convention, convenience, or faith that the objective function is a reasonable proxy for what you actually want. **The practical upshot for evaluating any vendor's or prior analyst's model**: "this model fits the data well" is an incomplete claim until you know *which* objective function "well" was measured against — different reasonable choices of objective function produce genuinely different "best" models from the identical data.

## Support Vector Machines: Just One Particular, Well-Motivated Objective Function

**The chapter's explicit demystification, worth keeping as the single most useful reframe for any non-technical reader who's been intimidated by the term "SVM"**: "support vector machines are linear discriminants... For many business users interacting with data scientists, that will be sufficient" — an SVM is not a different *kind* of model from the linear discriminants already described; it's the *same* linear model form, with one particular, carefully chosen objective function for picking among the infinite candidate lines.

**The first big idea — maximize the margin**: instead of asking "which single line separates the classes," ask "what is the *fattest possible bar* that fits between the two classes, with no points inside it?" — then take the centerline of that widest bar as the actual decision boundary. **Why this is more than just an aesthetic preference, worth keeping as the actual statistical justification**: the training data is only a *sample* from a larger population; future, unseen instances will scatter somewhat differently than the exact training points, and some will likely land closer to the boundary than anything in the training set did. **A margin-maximizing boundary gives the most "leeway" against exactly this kind of future shift** — a new point would have to fall further into the margin than any alternative linear boundary would tolerate before getting misclassified. **A genuinely useful framing for explaining this to a client without the math**: SVM picks the boundary that's "safest" against the inevitable difference between the training sample and whatever comes next, not just the boundary that happens to fit the training sample best.

**The second big idea — what to do when no line separates the data perfectly (the typical real-world case)**: rather than asking "which perfectly-separating line is best" (often there is none), the SVM objective function **penalizes each misclassified point proportionally to how far it lands on the wrong side of the boundary**, then balances the *width* of the margin against the *total* of these penalties. **This specific penalty shape is called hinge loss**: zero penalty for any point correctly on its own side (even right up against the margin boundary), a penalty that grows linearly with distance past the boundary for any misclassified point. **The general vocabulary worth keeping**: a "loss function" is the general data-science term for how much penalty an error of a given size incurs, and different techniques are meaningfully distinguished by which loss function they use — hinge loss (SVM, named for its bent, hinge-like graph shape), zero-one loss (a flat penalty of exactly 1 for any error regardless of size, 0 otherwise), and squared error (penalty proportional to the *square* of the distance, heavily punishing large errors). **A sharp, important caution about squared error specifically, worth keeping for any future modeling decision**: squared error is generally used for numeric (regression) targets, not classification, **because it would also penalize points that are already correctly, confidently classified far on the right side of the boundary** — actively punishing the model for being *too* confidently correct, which is rarely what a classification problem actually wants. **The general, transferable principle behind all of this**: the choice of loss/objective function should be driven by what actually matches the real business goal, not by mathematical convenience alone — a theme the chapter returns to explicitly in the regression material that follows.

## Connects to

- [[tree-induction-and-decision-boundaries]] — this page's linear, any-orientation decision boundaries are the direct counterpoint to that page's axis-perpendicular tree boundaries; both are visualized using the identical instance-space framework.
- [[linear-regression-least-squares-and-logistic-regression]] — the companion page showing how the exact same "choose an objective function, then optimize" framework produces linear regression and logistic regression, just by swapping in a different objective.
- [[tree-vs-linear-models-and-nonlinear-extensions]] — the page comparing tree-structured and linear models head-to-head on a real dataset, and extending the linear-function idea into nonlinear SVMs and neural networks.

## North Star Connection

- How this applies to the audit business: the "best fit is only best relative to a chosen objective function" principle is a sharp, important due-diligence question for evaluating any predictive model a client's vendor or in-house team presents — "what objective function was this optimized against, and does that actually match our business goal" is a question most non-technical stakeholders never think to ask. The SVM margin-maximization logic ("safest against the gap between training data and what comes next") is a clean, jargon-free way to explain why a more conservative, less-perfectly-fit model can actually be the more trustworthy one for a client wary of "the model looked perfect in testing."
- Track relevance: Tech — foundational vocabulary for evaluating and selecting predictive-modeling techniques in any future client engagement.
- Possible future Second Brain use: a "what objective function was this optimized for" due-diligence question is a strong, near-ready candidate addition to a model/vendor-review checklist.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The objective-function due-diligence question is a sharp, broadly applicable model-evaluation tool |
| Current usefulness | 4 | Directly useful for evaluating any existing or proposed predictive model, even without building one from scratch |
| KSU support | 4 | Strong, rigorous quantitative grounding in a widely-used technique family (linear discriminants, SVMs) |
| Tech-stack relevance | 4 | Core vocabulary for the `stack/ai-frameworks-apis` category and any future modeling work |
| Business audit value | 4 | The margin-maximization explanation is a strong, accessible client-communication tool for justifying a more conservative model choice |
| Data/workflow value | 3 | Conceptually important but less directly hands-on than the tree-induction or SQL material |
| Reading urgency | 4 | Builds directly on tree induction and sets up the regression/logistic-regression material that follows |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Model due-diligence and client-communication tool — ask what objective function any presented model was actually optimized against before trusting a "best fit" claim, and use the margin-maximization framing to explain why a more conservative model can be more trustworthy than one that fits training data perfectly.

**Use when**:
Reviewing a vendor's or prior analyst's predictive model, or explaining to a client why an SVM/linear-discriminant-based model chose a particular decision boundary over an alternative that fit the training data just as well.

**Do not use when**:
The audience needs the literal mathematical mechanics rather than the conceptual/business framing — this page intentionally skips most of the underlying optimization math, consistent with the source chapter's own stated approach.

**Fast retrieval query**:
`subject/linear-models` + `subject/support-vector-machines` — or search "infinitely many lines separate classes objective function" / "SVM margin maximization fattest bar" / "hinge loss vs squared error vs zero-one loss" / "support vector machines are linear discriminants"
