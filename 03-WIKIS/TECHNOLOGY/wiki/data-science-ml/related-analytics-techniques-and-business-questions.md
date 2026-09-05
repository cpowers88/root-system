---
domain: technology
type: concept
tags: [subject/data-science, subject/database-querying, subject/statistics]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow, audit, reporting]
stack: [sql-sqlite, data-visualization]
---

# Statistics, Database Queries, OLAP, and Data Mining Are Different Tools — Knowing Which One a Question Actually Needs

**Summary**: Four nearly-identical-sounding business questions ("who are our most profitable customers?" through "will this new customer be profitable?") each require a genuinely different analytics technology — and confusing them wastes time, hires the wrong specialist, or produces an answer that doesn't actually address what was asked. Closes Chapter 2 of Data Science for Business with a clean taxonomy distinguishing data mining from summary statistics, hypothesis testing, database querying, OLAP, data warehousing, regression analysis, and machine learning/KDD.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 2 ("Business Problems and Data Science Solutions")

**Last updated**: 2026-06-22

---

## Summary Statistics: Choose Them With the Distribution in Mind, Not by Default

**Statistics**, in business-analytics usage, means two distinct things worth keeping separate: a catch-all term for computed numeric values of interest (sums, averages, rates — "summary statistics"), and the formal academic field (capitalized "Statistics") that underlies much of data science's theoretical foundation, including hypothesis testing and confidence-interval estimation. **A sharp, real-numbers illustration of why the choice of summary statistic matters, not just its computation**: the 2004 US Census reported a *mean* household income over $60,000, but the *median* was only $44,389 — because income distribution is heavily right-skewed (many people earning relatively little, a smaller number earning enormously more pulls the mean upward). **The general, transferable rule this example supports**: always check whether your chosen summary statistic is actually appropriate for the *shape* of the underlying distribution before using it for any business decision — a skewed distribution routinely makes the mean actively misleading where the median (or another robust statistic) tells the real story.

**Hypothesis testing's role, framed precisely against data mining's role**: hypothesis testing answers "is this observed difference (Northeast churn rate 22.5% vs. national 15%) likely real, or just random sampling variation?" — it's a tool for *confirming* a specific, pre-stated conjecture. **Data mining is explicitly framed as the complementary, prior step: hypothesis *generation*** — finding candidate patterns in data in the first place, which should then be followed by careful testing (ideally on separate data, foreshadowing the book's later treatment of overfitting and holdout validation). **The practical sequencing lesson**: data mining surfaces candidates; statistical hypothesis testing is what should validate them before they're trusted — treating a data-mined pattern as already proven, without the testing step, is a common and avoidable error.

## Database Querying and OLAP: Confirming a Hypothesis vs. Discovering One

**A database query** retrieves a specific subset or computed statistic, in a technical language (SQL or a GUI front-end), and **fundamentally involves no pattern discovery** — it answers a question the analyst already knew how to ask. **The chapter's clean illustrating contrast, worth keeping as the precise distinction**: if an analyst already *suspects* that middle-aged men in the Northeast show unusual churn behavior, a SQL query (`SELECT * FROM CUSTOMERS WHERE AGE > 45 AND SEX='M' AND DOMICILE='NE'`) confirms or explores that specific, pre-formed hypothesis. **Data mining, by contrast, is what could have generated that same query as its *output*** — a data mining procedure examining historical churners and non-churners might *discover* that exactly this segment predicts churn, with the resulting SQL query then used downstream simply to retrieve the matching records. **The general lesson for any client conversation about "we need a report" vs. "we need to find something we don't know to look for"**: a query tool is the right answer when the analyst already knows the relevant pattern or segment; data mining is the right answer when the pattern itself is what's missing.

**OLAP (On-Line Analytical Processing)** sits between these — a GUI for fast, interactive, pre-programmed-dimension exploration ("drill into sales by region and time by clicking and dragging") that, like a query tool, performs **no modeling or automatic pattern-finding** — it just makes manual, visual exploration along *known* dimensions fast and easy. **The dimension-flexibility distinction worth keeping**: OLAP's exploration dimensions must be foreseen and pre-programmed into the system; data mining tools can incorporate new dimensions as part of the exploration itself, on the fly. **OLAP and data mining are explicitly framed as complementary, not competing** — OLAP is a strong tool for the kind of manual exploration that often *precedes* or *follows up on* a data-mined discovery, not a substitute for it.

## Data Warehousing: Infrastructure, Not Analysis Itself

A data warehouse collects and coalesces data across an enterprise's many separate transaction-processing systems into one accessible analytical resource. **It's explicitly framed as a *facilitating* technology for data mining, not a requirement** — most data mining doesn't actually require a full warehouse — **but firms that have invested in one can typically apply data mining more broadly and more deeply**, since integrating, say, sales, billing, and HR records into one accessible structure is what makes a pattern like "characteristics of effective salespeople" (which spans multiple originally-separate systems) discoverable at all.

## Regression Analysis vs. Predictive Modeling: Same Math, Different Goal

**A genuinely important, easy-to-miss distinction for anyone arriving from a traditional statistics/econometrics background**: regression analysis (in its classical statistical sense) and the book's predictive-modeling focus often use the *same underlying mathematical techniques* but pursue **different goals**, and the lessons from one don't all transfer cleanly to the other. **Classical regression analysis is typically aimed at *explaining* a specific, already-observed dataset** — understanding *why* churn happened in this historical data. **Predictive modeling is aimed at *generalizing* to new, not-yet-seen cases** — predicting which customers who haven't yet left are the best ones to target now, to reduce *future* churn. **The chapter's explicit warning, worth keeping for anyone with a stats background reading further into this book**: "the lessons learned from explanatory modeling do not all apply to predictive modeling" — readers may encounter techniques (deliberately reducing model complexity to improve generalization, even at the cost of a worse fit to the historical data) that initially look backwards or even contradictory if approached with a pure explanatory-modeling mindset.

## Machine Learning vs. Data Mining/KDD: Overlapping Fields, Different Centers of Gravity

Both fields grew out of (and remain closely tied to) Machine Learning, Applied Statistics, and Pattern Recognition, sharing techniques and researchers freely. **The chapter's clean way of separating their emphasis, worth keeping for understanding which community's literature/vendors are likely most relevant to a given problem**: Machine Learning (as a subfield of AI) is concerned more broadly with *any* form of performance improvement from experience, including robotics, computer vision, and questions of agency/cognition that have no real business-analytics analogue. **Data Mining/KDD split off specifically to focus on real-world *application* concerns**, and — directly relevant to any business-facing engagement — KDD remains more concerned with the *entire* process (data preparation, evaluation, and so on, i.e., exactly the CRISP-DM cycle from [[crisp-dm-process-and-data-leakage]]) rather than just the modeling-algorithm core. **The practical upshot**: when a business problem is the actual frame (as opposed to a general AI research question), the KDD/data-mining literature and community are generally the more directly relevant ones to draw from.

## Four Nearly-Identical Questions, Four Different Required Technologies

**The chapter's closing taxonomy, worth keeping as a standing diagnostic for matching any client question to the right tool before recommending an approach (or a specialist)**:

1. **"Who are our most profitable customers?"** — if "profitable" can be defined cleanly from existing data, this is a **plain database query**: retrieve and sort customer records.
2. **"Is there really a difference between profitable customers and the average customer?"** — this is a **hypothesis-testing** question, answered with a confidence statement ("the difference is significant, with <5% probability it's due to chance").
3. **"But who really *are* these customers — can I characterize them?"** — basic characteristics come from querying; but determining what genuinely *differentiates* profitable from unprofitable customers (beyond just listing their attributes) is **data mining**.
4. **"Will some particular new customer be profitable, and how much revenue should I expect?"** — this is **predictive modeling**, and it's explicitly **two distinct supervised sub-questions, not one**: a classification question (will they be profitable — yes/no or a probability) and a regression question (how much value will they generate — a number). **The chapter's pointed final note, worth keeping as the closing lesson of this whole taxonomy**: these two phrasings sound almost identical in plain English, but require genuinely different model types — confusing them produces a model built for the wrong question.

## Connects to

- [[canonical-data-mining-tasks-and-supervised-unsupervised]] — the classification-vs-regression distinction in question #4 above is the direct, concrete application of that page's formal classification/regression taxonomy to a single, realistic business question.
- [[crisp-dm-process-and-data-leakage]] — the data-mining-as-hypothesis-generation framing here is the conceptual basis for why Evaluation (a later CRISP-DM stage) exists at all: a data-mined hypothesis still needs the confirmatory testing step before being trusted.
- [[sql-select-where-and-filtering]] and [[sql-grouping-and-aggregate-functions]] — the database-query examples here are the direct conceptual companion to the already-ingested PracticalSQL material; this chapter explains *when* to reach for SQL versus when SQL alone is the wrong tool.
- [[pandas-summary-stats-and-value-counts]] — the mean-vs-median skewed-distribution warning directly extends the already-ingested pandas `describe()`/summary-statistics material with the business-judgment layer of *which* statistic to trust.

## North Star Connection

- How this applies to the audit business: the four-question taxonomy is a directly reusable client-conversation tool — when a client says "we want to understand our customers/jobs/equipment better," walking through which of the four question types they're actually asking immediately clarifies whether the right deliverable is a SQL report, a statistical confidence check, a characterization analysis, or a full predictive model, and prevents both over-delivering (building a model when a query would do) and under-delivering (running a query when the client actually needed a discovered pattern).
- Track relevance: Tech / Business — directly supports scoping conversations across the entire data-workflow track, and clarifies which of Chris's existing SQL/pandas skills already cover a given client request versus when a heavier predictive-modeling investment is actually warranted.
- Possible future Second Brain use: the four-question taxonomy ("who/is there a difference/characterize them/predict a new one") is a strong, near-ready candidate for a standalone client-intake question script.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The four-question taxonomy is a fast, directly reusable tool for scoping any client analytics request to the right technology |
| Current usefulness | 5 | Immediately applicable to distinguishing "this needs a SQL query" from "this needs real data mining" in any client conversation |
| KSU support | 3 | Conceptual taxonomy, less directly ISYE-quantitative than other tracks |
| Tech-stack relevance | 5 | Directly clarifies the relationship between Chris's existing `stack/sql-sqlite` skills and when heavier analytics tooling is actually needed |
| Business audit value | 5 | Prevents both over-scoping (building a model when a query suffices) and under-scoping (running a query when real pattern discovery is needed) |
| Data/workflow value | 4 | Directly informs tool selection for any client data-workflow request |
| Reading urgency | 4 | Closes out the chapter's foundational vocabulary before the book moves into specific predictive-modeling techniques |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Client-intake scoping tool — walk through the four-question taxonomy (who/is-there-a-difference/characterize/predict-a-new-one) whenever a client's request is ambiguous about whether they need a report, a statistical check, a characterization, or a predictive model.

**Use when**:
A client says "we want to understand X better" or "help us use our data," before committing to a specific technical approach or quoting a scope.

**Do not use when**:
The client's request is already unambiguous about which of the four question types it is — the taxonomy is a disambiguation tool, not a mandatory checklist for every engagement.

**Fast retrieval query**:
`subject/database-querying` + `subject/statistics` — or search "mean vs median skewed income distribution" / "data mining as hypothesis generation" / "OLAP vs data mining dimensions" / "who are our most profitable customers four questions" / "explanatory modeling versus predictive modeling"
