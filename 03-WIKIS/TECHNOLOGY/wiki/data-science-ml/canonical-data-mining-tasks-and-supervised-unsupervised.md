---
domain: technology
type: concept
tags: [subject/data-science, subject/classification, subject/clustering, subject/supervised-learning]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow, audit]
stack: [ai-frameworks-apis]
---

# The Nine Canonical Data Mining Tasks, and Why "Supervised vs. Unsupervised" Is the First Question to Ask

**Summary**: Despite the huge number of named data mining algorithms, nearly every one addresses one of just nine fundamental task types — recognizing which type a business problem actually reduces to is the single most leverage-able skill in scoping any analytics project, since it avoids reinventing known solutions and focuses creative effort where it's actually needed. The supervised/unsupervised distinction is the first and most consequential fork in that recognition process — illustrated sharply by why credit card fraud and Medicare fraud, despite both being "fraud detection," require fundamentally different approaches.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 2 ("Business Problems and Data Science Solutions")

**Last updated**: 2026-06-22

---

## Why Task-Type Recognition Is "a Critical Skill," Not Just Taxonomy

**The chapter's explicit framing, worth keeping as the standing justification for learning this vocabulary at all**: "a critical skill in data science is the ability to decompose a data-analytics problem into pieces such that each piece matches a known task for which tools are available. Recognizing familiar problems and their solutions avoids wasting time and resources reinventing the wheel" — and, just as importantly, frees up human creativity for the parts of the problem that genuinely require it, rather than spending it on a problem someone else has already solved. **Every unique business problem (MegaTelCo's specific churn situation) still decomposes into common subtasks** (estimating, from historical data, the probability a given customer leaves shortly after contract expiration) — the idiosyncrasy lives in the business context; the underlying analytical task is usually generic and well-studied.

## The Nine Tasks, With the Distinguishing Question for Each

1. **Classification / class probability estimation** — predicting which of a small set of mutually exclusive classes an individual belongs to ("will this customer respond to this offer?"), or producing a *probability* of membership rather than a hard yes/no (a "scoring" model). **The two are closely related — a model that does one can usually be adapted to do the other.**
2. **Regression ("value estimation")** — predicting a *numerical* value for an individual ("how much will this customer use the service?"). **The clean informal distinction from classification, worth keeping verbatim**: "classification predicts whether something will happen, whereas regression predicts how much something will happen."
3. **Similarity matching** — finding individuals similar to a known reference (IBM finding companies similar to its best customers to focus sales effort; the basis for most product-recommendation systems built on "people similar to you liked X").
4. **Clustering** — grouping individuals by similarity with **no specific predictive purpose attached** ("do our customers naturally fall into groups?") — useful for exploratory domain understanding, which may then *suggest* a follow-on supervised task.
5. **Co-occurrence grouping** (market-basket analysis, association rule discovery) — finding what tends to occur *together* in the same transaction, distinct from clustering's similarity-of-attributes framing (ground meat and hot sauce purchased together more than chance would predict).
6. **Profiling (behavior description)** — characterizing an individual's, group's, or population's *typical* behavior, often used as the baseline for anomaly detection (knowing a credit card's normal purchase pattern is exactly what makes an unusual new charge flaggable).
7. **Link prediction** — predicting whether a connection between two data items should exist, and how strong it should be (social-network "you and Karen share 10 friends" suggestions; recommendation systems framed as predicting missing/weak edges in a customer-product graph).
8. **Data reduction** — replacing a large dataset with a smaller one that preserves most of the important information, **always trading information loss for tractability or clarity** (reducing a massive movie-viewing dataset down to a handful of latent genre-preference dimensions).
9. **Causal modeling** — understanding what actually *causes* what, as distinct from mere correlation/prediction (did the ad cause the purchase, or did the targeting model simply find people who would have purchased anyway?). **The chapter's explicit, important discipline here**: any causal conclusion must be stated alongside the specific assumptions required for it to hold — "there always are such assumptions — always ask" — and even the most carefully randomized experiment can still harbor an overlooked one (the placebo effect's discovery in medicine is the cited cautionary example of exactly this).

**Most of the book's worked examples draw from just four of these (classification, regression, similarity matching, clustering)** — not because the other five matter less, but because those four are the clearest vehicles for the underlying fundamental principles the book is actually trying to teach.

## Supervised vs. Unsupervised: The First, Most Consequential Fork

**The precise distinguishing question, worth keeping as a fast diagnostic for scoping any new analytics request**: has a specific *target* been defined? "Do our customers naturally fall into groups?" (no target — unsupervised) vs. "Can we find groups of customers with a particularly high likelihood of canceling service right after contract expiration?" (a specific target — churn — supervised). **Supervised techniques are generally more useful precisely because they're aimed at a defined purpose** — clustering produces groupings based on similarity, "but there is no guarantee that these similarities are meaningful or will be useful for any particular purpose."

**A second, easy-to-overlook technical requirement for a problem to actually be supervised, not just supervisable in principle**: the target's value must actually **exist in the data**, not merely exist conceptually. Wanting to know if a customer will stay at least six months is useless as a supervised target if historical retention data was only ever recorded for two months — **the target value (the individual's "label") often has to be actively, expensively acquired**, directly echoing [[data-asset-strategy-signet-bank-capital-one-case]]'s point that data is something you sometimes have to deliberately invest in producing, not something that's simply lying around waiting to be mined.

**Classification and regression are the two subtypes of supervised learning, distinguished cleanly by the target's data type**: a numeric target → regression; a categorical (often binary) target → classification, **even when the actual model output is a probability number** (e.g., the probability a customer churns) — this is still classification/"class probability estimation," not regression, because the underlying thing being predicted is categorical, not numeric. **The mapping for the other task types, worth keeping as a quick lookup**: similarity matching, link prediction, and data reduction can go either way; clustering, co-occurrence grouping, and profiling are generally unsupervised.

## Why "Both Are Fraud Detection" Can Be a Misleading Surface Similarity

**The chapter's sharpest illustration of why task-type recognition requires digging past the surface label of a business problem, not just its name**: credit card fraud and Medicare fraud are both "fraud detection," but they require fundamentally different approaches, because of one structural fact about the data each generates. **Credit card fraud has a reliable, naturally-occurring label**: the legitimate cardholder and the fraud perpetrator are different people with opposed interests, so fraud gets caught (by the company or eventually the customer reviewing a statement) and reliably recorded as fraud vs. legitimate — a clean supervised target exists, essentially as a side effect of how the system already works. **Medicare fraud has no such disinterested party**: the people committing fraud (providers submitting false claims, sometimes patients) are themselves legitimate system users, and there's no separate party with an opposing interest who will reliably flag exactly what "correct" billing should have been. **The consequence**: Medicare billing data has no reliable target variable for fraud, so the credit-card supervised approach simply doesn't transfer — Medicare fraud detection instead requires unsupervised methods (profiling, clustering, anomaly detection, co-occurrence grouping) to surface suspicious *patterns* without ever having clean ground-truth labels to learn from. **The general, transferable lesson**: two problems sharing a surface-level business label can require entirely different technical approaches once you actually examine whether — and how — the target data gets generated; the label name is not a safe guide to the right method.

## Connects to

- [[data-driven-decision-making-and-data-science-definition]] — this page's nine-task taxonomy is the concrete vocabulary underlying that page's Type 1 (discovery)/Type 2 (repeated-at-scale) decision framing; most Type 2 decisions are supervised classification/regression problems specifically.
- [[data-asset-strategy-signet-bank-capital-one-case]] — the "the target must exist in the data, not just in principle" requirement is the technical version of that page's "data is an asset you sometimes have to deliberately invest in acquiring" argument.
- [[stock-flow-fundamentals-and-notation]] — profiling-for-anomaly-detection (establishing a behavioral norm, then flagging deviations) is conceptually similar to a goal-seeking negative-feedback structure with an implicit, learned target rather than an explicitly stated one.

## North Star Connection

- How this applies to the audit business: the supervised/unsupervised fork and the nine-task taxonomy together give Chris a fast, structured way to scope any client's "we want to use our data better" request into a concrete, known problem type — rather than starting from scratch on every engagement. The credit-card-vs-Medicare-fraud contrast is a directly reusable diagnostic question for any client request: does the historical data this client has actually contain a reliable target label, or does it only *seem* to (the way Medicare billing data superficially resembles credit-card transaction data but isn't actually labeled the same way)?
- Track relevance: Tech — core scoping vocabulary for any future data/analytics audit work, directly supporting the `use-case/data-workflow` track.
- Possible future Second Brain use: a "does the target actually exist in the data" checklist question (modeled on the credit-card vs. Medicare contrast) is a strong candidate addition to a client data-discovery interview protocol.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The supervised/unsupervised fork and the task taxonomy are foundational, immediately reusable scoping tools for any client analytics request |
| Current usefulness | 5 | Directly applicable to scoping any future data-workflow engagement |
| KSU support | 3 | Conceptual taxonomy, foundational for the technology track but not directly ISYE-quantitative |
| Tech-stack relevance | 5 | Core vocabulary for the entire `stack/ai-frameworks-apis` category |
| Business audit value | 4 | The "does the target actually exist in the data" question is a sharp, generally applicable client-discovery diagnostic |
| Data/workflow value | 5 | Directly informs how to scope and structure any client data-mining request |
| Reading urgency | 5 | Foundational vocabulary needed before any of the book's later, more technical chapters make sense |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Engagement-scoping tool — when a client describes a "we want to use our data" goal, classify it against the nine canonical tasks and check the supervised/unsupervised fork (does a clean target actually exist in their data, or only seem to) before proposing an approach.

**Use when**:
Scoping any new client analytics request, especially one where the client's framing ("we want to detect fraud," "we want to find our best customers") could map onto multiple different underlying task types depending on what data actually exists.

**Do not use when**:
The client's need is purely descriptive reporting (a database query or dashboard) with no pattern-discovery or prediction goal — that's a different layer entirely (see [[related-analytics-techniques-and-business-questions]] for the database-query/OLAP distinction).

**Fast retrieval query**:
`subject/classification` + `subject/supervised-learning` — or search "nine canonical data mining tasks" / "supervised vs unsupervised target exists in data" / "credit card fraud vs Medicare fraud labels" / "classification predicts whether regression predicts how much"
