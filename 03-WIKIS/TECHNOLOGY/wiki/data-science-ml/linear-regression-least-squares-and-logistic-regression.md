---
domain: technology
type: concept
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, use-case/audit, subject/data-science, subject/linear-regression, subject/logistic-regression, subject/objective-functions, stack/ai-frameworks-apis]
---

# Why "Least Squares" Is a Convenience, Not a Law of Nature — and How Logistic Regression Sneaks a Probability Out of a Straight Line

**Summary**: Least-squares linear regression is the default everyone learns first, but the chapter is explicit that squared error is a *convenient* choice of objective function, not the uniquely correct one — and it has a specific, real weakness (outlier sensitivity) worth knowing before trusting it blindly. Logistic regression solves a different, subtler problem: how do you get a linear function (which ranges from −∞ to ∞) to output something that behaves like a genuine probability (which must stay between 0 and 1) — the answer runs through odds and log-odds, and the result is one of the most widely used techniques in all of data science, hiding behind a name that doesn't actually describe what it does.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 4 ("Fitting a Model to Data")

**Last updated**: 2026-06-22

---

## Linear Regression: Same Model Form, a Different Objective

**The chapter's key unifying point, worth keeping as the throughline for this entire chapter**: linear regression uses the *exact same* model structure as the linear discriminant from [[linear-discriminants-objective-functions-and-svm]] — f(x) = w₀ + w₁x₁ + w₂x₂ + ... — the only thing that changes is the objective function used to fit the weights, since the target here is numeric rather than categorical. **The intuitive objective is straightforward**: minimize the total error between the model's estimated values and the actual training-data values. **But "error" itself isn't a single, self-evident quantity** — the most intuitively natural choice (subtract predicted from actual, take the absolute value — "absolute error") is explicitly **not** what standard linear regression procedures use.

**Standard ("least squares") linear regression instead minimizes the *sum of squared* errors.** **The chapter's candid explanation of why this specific, less-intuitive choice became the overwhelming default, worth keeping as a sharp piece of intellectual honesty about a technique most people never question**: largely **convenience** — it's the technique taught first in basic statistics courses, it's built into virtually every software package, it has a long historical pedigree (introduced by Gauss in the 18th century, with theoretical ties to the normal/Gaussian distribution), and — most decisively, especially in the pre-computer era — squared error is **mathematically far more convenient to work with** than absolute error, including supporting a clean decomposition of model error into distinct sources. **A pointed rhetorical question worth keeping as a standing reminder that even Gauss's own choice was somewhat arbitrary**: "analysts often claim to prefer squared error because it strongly penalizes very large errors. Whether the quadratic penalty is actually appropriate is specific to each application. (Why not take the fourth power of the errors, and penalize large errors even more strongly?)" — even the seemingly principled justification for squaring doesn't uniquely select squaring over any other increasing penalty function; it's a convention that happened to also be mathematically tractable.

**The real, practical cost of this convenience, worth keeping as a standing caution before trusting any least-squares model on messy data**: least-squares regression is **very sensitive to outliers** — a small number of erroneous or genuinely unusual data points can disproportionately skew the entire fitted line, precisely because squaring amplifies the influence of large individual errors. **The chapter's explicit, practical recommendation**: for any **fully automated** system (one that builds and applies models without a human manually inspecting and cleaning the data each time), the modeling needs to be inherently more robust than a model an analyst gets to massage by hand — which may mean deliberately choosing a more outlier-resistant objective function (such as absolute error) over the mathematically convenient default. **The general, transferable principle, worth keeping verbatim**: "once we see linear regression simply as an instance of fitting a (linear) model to data, we see that we have to choose the objective function to optimize — and we should do so with the ultimate business application in mind" — least squares is the default, not the correct answer, and the right answer depends on how the model will actually be used and how reliable the data feeding it really is.

## Logistic Regression: Solving the Wrong-Range Problem via Odds and Log-Odds

**The motivating problem, stated precisely**: we'd like to estimate a genuine *probability* of class membership using a linear function — but f(x) itself ranges from −∞ to ∞, while a valid probability must stay strictly between 0 and 1. Simply treating f(x) as a probability directly would be mathematically incoherent. **The chapter's elegant resolution, worth keeping as a genuinely satisfying piece of applied math reasoning rather than an arbitrary trick**: instead of modeling the probability directly, model something *else* that naturally ranges over the same domain f(x) already covers. **The intermediate stepping stone is odds** — the ratio of the probability of an event happening to the probability of it not happening (an 80% probability corresponds to 4:1 odds) — which ranges from 0 to ∞, closer to but not quite matching f(x)'s full −∞-to-∞ range. **The final step is the log of the odds ("log-odds")**, which *does* range over the full −∞ to ∞ — exactly matching what a linear function can naturally produce. **The payoff**: f(x) can be interpreted directly as the model's estimate of the log-odds that x belongs to the positive class, and a small amount of algebra (Equation 4-4, the "logistic function," 1/(1+e^−f(x))) translates that log-odds estimate back into an actual probability between 0 and 1.

**The resulting "sigmoid" (S-shaped) curve matches the chapter's earlier intuition exactly, worth keeping as the clean geometric/probabilistic unification of the whole chapter's framework**: at the decision boundary itself (f(x)=0), the estimated probability is exactly 0.5 — a coin toss, as it should be. Moving away from the boundary, probability rises (or falls) approximately linearly at first, then flattens out and approaches certainty (0 or 1) the farther out you go — meaning the same f(x) that earlier served purely as a ranking signal for "how far from the boundary" can be smoothly converted into a calibrated probability estimate, simply by passing it through this one fixed transformation.

**The objective function used to actually fit a logistic regression, worth keeping as the conceptual core even without the full math**: maximum likelihood — find the set of weights that, when used to generate probability estimates for every training example, gives the **highest possible "probability of having seen exactly this data"** — i.e., the weights that make actual positive examples get high estimated probabilities and actual negative examples get low estimated probabilities, summed/multiplied across the whole training set. **A genuinely important, easy-to-misunderstand clarification, worth keeping verbatim for anyone tempted to think a logistic regression model's predictions are simply "wrong" whenever an unlikely outcome happens**: a customer estimated at p=0.02 probability of responding who then *does* respond does not mean the model erred — the training data are best understood as a set of statistical "draws" from the true underlying probability distribution, not a literal record of what each individual's "true" probability was. **A 2% probability event happening once is not evidence the model is broken; over many such customers, roughly 2% genuinely should respond, and which specific individuals do is inherently random.**

## Why "Logistic Regression" Is a Misnomer, and Why That's Fine

**A precise terminology clarification worth keeping for any conversation with someone schooled in formal statistics**: by this book's own classification/regression distinction, logistic regression is technically **classification (or, more precisely, class probability estimation), not regression** — even though it numerically estimates a continuous quantity (the log-odds), its *target* variable in the training data is categorical, and that's what determines the task type, not what kind of number the model internally produces. **The chapter's own pragmatic conclusion, worth adopting as the sensible resolution to what could otherwise become an unproductive semantic argument**: "debating this point is rather academic... what is important is to understand what logistic regression is doing" — a class-probability-estimation model built on a linear log-odds function, regardless of what its historically-inherited name suggests.

**Why this technique is so widely deployed, worth keeping as context for why it's worth knowing even briefly**: logistic regression underlies an enormous share of real-world probability-of-X models in active production use — probability of credit default, probability of responding to a marketing offer, probability of fraud on an account, probability that a document is relevant to a search query — precisely because it's the most common, well-understood way to get a calibrated, well-behaved probability estimate out of a linear combination of features.

## Connects to

- [[linear-discriminants-objective-functions-and-svm]] — both linear regression and logistic regression reuse the identical f(x) linear-model structure introduced there; only the objective function changes across all three techniques.
- [[probability-estimation-trees-laplace-correction-and-churn-case]] — logistic regression and probability-estimation trees are two structurally very different routes to the identical goal (a calibrated class-membership probability), worth comparing directly when choosing a technique for any future client deliverable.
- [[information-gain-entropy-and-attribute-selection]] — the squared-error-vs-absolute-error tradeoff (mathematical convenience vs. outlier robustness) is conceptually the same kind of "pick the metric the business goal actually needs" discipline already established for entropy vs. variance as purity measures.

## North Star Connection

- How this applies to the audit business: the explicit "least squares is convenient, not correct" critique is a sharp due-diligence tool for any client-facing regression analysis — asking whether the data is clean enough, or the application automated enough, to warrant a more outlier-robust objective function than the software's default. The "draws from a distribution, not literal individual truths" framing for probability estimates is a valuable, calming explanation to give a client confused or alarmed by a single unlikely outcome (a low-probability customer who did churn, a low-risk loan that did default) — it reframes an apparently "wrong" prediction as expected statistical noise rather than a model failure.
- Track relevance: Tech — foundational, broadly applicable technique vocabulary for the data-workflow track, directly relevant to any future client-facing predictive or risk-scoring work.
- Possible future Second Brain use: a "probability estimates are draws, not individual truths" client-communication script (for explaining away an apparently "wrong" low-probability outcome) is a strong, near-ready candidate for the audit-toolkit.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 4 | The "least squares is a convenience" critique and the "draws not truths" framing are both sharp, transferable client-communication and due-diligence tools |
| Current usefulness | 4 | Directly applicable to evaluating or building any regression or probability-estimation model for a client |
| KSU support | 5 | Strong, rigorous quantitative grounding (odds, log-odds, maximum likelihood) with real statistical depth |
| Tech-stack relevance | 5 | Logistic regression is one of the most widely deployed real-world techniques across the entire `stack/ai-frameworks-apis` category |
| Business audit value | 4 | The "draws not truths" explanation is a genuinely valuable, calming client-communication tool for an apparently anomalous prediction |
| Data/workflow value | 4 | Directly applicable quantitative technique for any client risk-scoring or probability-estimation need |
| Reading urgency | 4 | Builds directly on the linear-discriminant material and is foundational for understanding probability-based business decisions throughout the rest of the book |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Technique-selection and client-communication tool — question whether least-squares is actually the right objective function for a given dataset's outlier risk and automation level, and use the "draws not truths" framing to explain an apparently anomalous low-probability outcome to a worried client.

**Use when**:
Choosing or reviewing a regression technique for messy or automated client data, or explaining why a model's probability estimate wasn't "wrong" just because a low-probability event happened once.

**Do not use when**:
The audience needs the full mathematical derivation of maximum likelihood estimation — this page intentionally keeps the math conceptual, consistent with the source chapter's stated approach for the non-mathematical reader.

**Fast retrieval query**:
`subject/linear-regression` + `subject/logistic-regression` — or search "least squares convenience not correctness Gauss" / "odds log-odds sigmoid probability" / "logistic regression misnomer classification" / "training data draws from distribution not truths"
