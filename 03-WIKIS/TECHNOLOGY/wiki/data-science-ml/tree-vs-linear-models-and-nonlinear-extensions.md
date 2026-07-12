---
domain: technology
type: case-study
tags: [priority/now, status/wiki-only, domain/technology, source-role/example, use-case/data-workflow, use-case/audit, subject/data-science, subject/decision-trees, subject/neural-networks, subject/model-comprehensibility, stack/ai-frameworks-apis]
---

# Trees vs. Linear Models: When 98.9% and 99.1% Accuracy Don't Actually Tell You Which Model Is Better

**Summary**: Classification trees and linear models both carve up the feature space, but in structurally different ways — piecewise, axis-perpendicular segments for trees vs. a single, any-angle dividing surface for linear models — and which is "better" depends as much on who needs to understand the result as on raw accuracy. A real breast-cancer dataset comparison, where logistic regression and a decision tree land within 0.2 percentage points of each other, becomes the chapter's springboard into why a single accuracy number is rarely the full story, and into nonlinear extensions (kernel SVMs, neural networks) that trade interpretability for flexibility — closing Chapter 4 with a direct preview of overfitting.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 4 ("Fitting a Model to Data")

**Last updated**: 2026-06-22

---

## Two Structurally Different Ways to Carve Up the Same Space

**The chapter's precise, two-part comparison between tree-structured and linear models, worth keeping as a clean mental checklist for choosing between them**:

1. **Boundary orientation**: a tree's decision boundaries are always perpendicular to a single attribute's axis, a direct consequence of testing one attribute at a time at each node. **A linear classifier's boundary can run at any angle**, because it's a weighted combination of *all* attributes simultaneously, not a sequence of single-attribute tests.
2. **Boundary shape and count**: a tree is a "piecewise" classifier — it can recursively carve the space into arbitrarily many small regions through repeated divide-and-conquer splitting (though the chapter explicitly flags, foreshadowing the very next topic, that doing so excessively is a bad idea). **A linear classifier instead places exactly one decision surface through the entire space** — enormous freedom in that surface's *orientation*, but strictly limited to a single division into two regions, because there's one equation governing the whole feature space at once.

**The chapter's honest, important admission, worth keeping as a standing caution against false confidence in technique selection**: "it is usually not easy to determine in advance which of these characteristics are a better match to a given dataset" — you typically don't know in advance what the *true* underlying decision boundary actually looks like, so picking a technique based on a theoretical argument about which structural form is "more correct" is usually not a winning strategy.

## Comprehensibility, Not Just Accuracy, Often Decides Which Model Gets Used

**The chapter's sharper, more practically decisive distinction, worth keeping as the real deciding factor in many actual business deployments**: the two model types differ enormously in **comprehensibility to different audiences**. A logistic regression model can be quite transparent to someone with a solid statistics background, and nearly opaque to someone without one; a reasonably-sized decision tree (or its equivalent rule-set form) tends to be the reverse — accessible to a non-technical audience, less natural to someone trained in formal statistics. **Why this matters beyond aesthetics, worth keeping as the actual business stakes**: in most real deployments, the data science team does *not* have final, unilateral authority to put a model into production — a manager (or a whole set of stakeholders across different functions) typically has to "sign off," and they need to be convinced the model will do more good than harm. **The chapter's own example, worth keeping as a concrete illustration of how broad this stakeholder set can be**: deploying a model to dispatch technicians after customer repair calls required buy-in from operations support, customer service, *and* technical development simultaneously — three functionally different audiences, each needing to trust the model on their own terms. **The practical implication**: comprehensibility isn't a "nice to have" layered on top of accuracy — for many real deployments, it's a hard gating requirement, and the more interpretable model can be the *correct* business choice even when it's not the most accurate one.

## The Wisconsin Breast Cancer Case: A 0.2-Point Accuracy Gap That Means Almost Nothing on Its Own

**The setup**: 30 numeric attributes (mean, standard error, and "worst" values of 10 underlying cell-image characteristics — radius, texture, smoothness, concavity, and others) describing 569 cell samples, 357 benign and 212 malignant, with the target a binary benign/malignant diagnosis. **Logistic regression's fitted weights are directly inspectable and rankable**: SMOOTHNESS_worst (weight 22.3) and CONCAVE_mean (19.47) dominate, with several attributes ending up at or near a zero weight — directly usable, exactly as flagged in [[linear-discriminants-objective-functions-and-svm]], as a rough importance ranking. **Logistic regression achieved 98.9% accuracy (six errors out of 569); a comparably-sized decision tree (Weka's J48, 25 nodes/13 leaves) achieved 99.1%** — marginally higher.

**The chapter's own, deliberately unresolved skepticism about this exact comparison, worth keeping as a standing two-part discipline for any reported accuracy figure**: first, **98.9% sounds impressive on its face, but "evaluating classifiers on real-world problems like cancer diagnosis is often difficult and complex"** — a bare accuracy percentage doesn't by itself tell you whether that's actually a good result for this specific problem (a question the book explicitly defers to its later evaluation chapters). **Second, and more pointedly**: the 98.9%-vs-99.1% gap is the result of **exactly one additional misclassified example out of 569** — is that genuinely meaningful evidence the tree is "the better model," or is it well within the kind of variation you'd expect just from chance? **Compounding the problem, both numbers were computed by evaluating each model against the very same data it was trained on** — exactly the methodological gap the book's next chapter (overfitting) and later evaluation chapters exist to address. **The general, transferable lesson, worth keeping as a standing reflex whenever two models' accuracy numbers are close**: a small accuracy difference computed on training data is not, by itself, evidence that one technique is genuinely superior — both the absolute number and the comparison between two close numbers need to survive a more rigorous evaluation methodology before either claim should be trusted.

## Linear Functions Can Fake Nonlinearity, and Nonlinear SVMs/Neural Networks Formalize the Trick

**A genuinely clever and underappreciated point, worth keeping as a standing technique whenever a relationship looks curved rather than straight**: a strictly *linear* function can still represent a *nonlinear* decision boundary in the original feature space, simply by adding new features that are mathematical functions of the originals. The chapter's worked illustration: adding a single new feature, Sepal-width², to the Iris dataset lets an otherwise purely linear model (logistic regression or SVM) produce a curved (parabolic) boundary back in the original two-dimensional space — the model itself never stopped being linear in its *actual* inputs; one of those inputs is simply a squared term.

**Nonlinear support vector machines formalize this exact trick systematically, via a "kernel function"** that maps the original features into some new, higher-dimensional feature space, after which an ordinary *linear* model is fit in that new space — a "polynomial kernel" is conceptually just an automated, systematic way of generating squared terms, products of features, and other higher-order combinations, rather than hand-picking them one at a time the way the Sepal-width² example did manually.

**Neural networks extend the same core fitting-an-objective-function idea in a structurally different direction, worth keeping as a clean, non-mystical mental model**: think of a neural network as a *stack* of simple models (the chapter's own illustration: imagine each layer as a logistic regression) — the first layer learns a set of relatively simple "expert" models directly from the raw features; each subsequent layer learns a further simple model using the *previous* layer's outputs as its inputs. **The genuinely elegant unifying insight, worth keeping as the conceptual payoff of the entire chapter**: the whole multi-layer stack can be represented as one single, very large parameterized numeric function — meaning everything already developed about choosing an objective function and optimizing parameters to fit it applies without modification; **only the lower-layer "expert" models' target labels are never directly provided** (only the final output layer has real training labels) — the optimization process discovers what the lower layers should specialize in entirely as a side effect of optimizing the whole stack's fit to the final target.

## The Chapter's Closing Trade-Off: More Flexibility Always Buys More Risk of Fitting Noise

**The chapter's final, deliberately blunt question and answer, worth keeping verbatim as the bridge into the entire next stage of this ingest**: "given how cool that sounds, why wouldn't we want to do that all the time?" — increasing a model's flexibility to fit the training data increases, in lockstep, **the risk of fitting the training data's noise rather than the real, generalizable pattern underneath it.** **The chapter's explicit framing of why this concern isn't specific to neural networks or any one technique**: it's general to *any* sufficiently flexible parametric model, tree, or combination thereof — "this concern... is one of the most important concepts in data science," dedicated its own full chapter immediately following this one (the out-of-scope-for-this-ingest-so-far Chapter 5, "Overfitting and Its Avoidance," the next planned stop in this DataScienceforBusiness.pdf ingest).

## Connects to

- [[linear-discriminants-objective-functions-and-svm]] and [[linear-regression-least-squares-and-logistic-regression]] — this page's head-to-head comparison and nonlinear extensions build directly on both pages' linear-model foundations.
- [[probability-estimation-trees-laplace-correction-and-churn-case]] — the comprehensibility-vs-accuracy trade-off here directly extends that page's own probability-vs-classification reframing; both pages independently arrive at "what the model is allowed to say" mattering as much as raw predictive accuracy.
- [[crisp-dm-process-and-data-leakage]] — the multi-stakeholder sign-off requirement described here (operations, customer service, technical development) is the concrete, named instance of that page's Evaluation-stage discussion of qualitative, stakeholder-driven model assessment.

## North Star Connection

- How this applies to the audit business: the comprehensibility-vs-accuracy trade-off is directly relevant to choosing which predictive technique to recommend for a given client — a small SMB client's owner-operator decision-maker will need an interpretable tree/rule-set far more than a large client with an in-house statistically literate team would. The "one extra error out of 569, both measured on training data" skepticism check is a sharp, reusable due-diligence question for any vendor or in-house comparison Chris reviews where two models' accuracy numbers are close — close numbers on training data are not by themselves evidence of a real difference.
- Track relevance: Tech — directly informs technique selection and model due-diligence for any future client predictive-analytics engagement.
- Possible future Second Brain use: a "comprehensibility requirement by stakeholder" technique-selection checklist (who needs to sign off, and how technical are they) and the "close accuracy numbers on training data aren't meaningful" skepticism check are both strong, near-ready candidates for the audit-toolkit.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The comprehensibility-vs-accuracy trade-off directly informs technique selection for any future client engagement, especially SMB clients |
| Current usefulness | 4 | Immediately applicable to comparing and selecting between predictive-modeling techniques for a client |
| KSU support | 4 | Strong quantitative grounding (the breast cancer case) with a real, well-documented dataset |
| Tech-stack relevance | 4 | Connects the `stack/ai-frameworks-apis` techniques already covered into a coherent selection framework |
| Business audit value | 5 | The multi-stakeholder sign-off framing and the close-accuracy-numbers skepticism check are both sharp, directly reusable client-engagement tools |
| Data/workflow value | 4 | A concrete technique-comparison case directly applicable to any client model-selection decision |
| Reading urgency | 5 | Closes Chapter 4 and directly sets up the book's next, foundational topic (overfitting) |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Technique-selection and due-diligence tool — weigh comprehensibility needs (who has to sign off, how technical are they) alongside raw accuracy when recommending a predictive technique, and apply the close-accuracy-numbers skepticism check before trusting a small reported difference between two models.

**Use when**:
Recommending a predictive-modeling technique to a client with a specific stakeholder sign-off requirement, or reviewing a vendor/in-house comparison where two models' accuracy figures are close together.

**Do not use when**:
The client has no comprehensibility constraint at all (a fully automated system with no human sign-off step) — in that case accuracy and robustness considerations alone may legitimately dominate the technique choice.

**Fast retrieval query**:
`subject/decision-trees` + `subject/model-comprehensibility` — or search "tree axis perpendicular vs linear any orientation" / "comprehensibility stakeholder sign off model" / "breast cancer 98.9 vs 99.1 percent one extra error" / "neural network stack of logistic regressions" / "more flexibility more risk of fitting noise"
