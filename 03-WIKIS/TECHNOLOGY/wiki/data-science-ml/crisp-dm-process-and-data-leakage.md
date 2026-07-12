---
domain: technology
type: method
tags: [priority/now, status/wiki-only, domain/technology, source-role/primary, use-case/data-workflow, use-case/audit, use-case/reporting, subject/data-science, subject/crisp-dm, subject/data-leakage, stack/ai-frameworks-apis]
---

# The CRISP-DM Process: Why Data Mining Is R&D, Not Software Engineering — and the Leakage Trap That Silently Wrecks Models

**Summary**: A six-stage, iteration-by-default process (CRISP-DM) for structuring any data mining project, including the specific warning that managing it like a software development cycle is a recognizable, common, and costly mistake. Plus "leakage" — the single, deceptively easy-to-make data preparation error where a variable available in historical data wasn't actually available at decision time — and why deployment is often more organizationally fraught than technically hard.

**Sources**: DataScienceforBusiness.pdf (Provost & Fawcett, *Data Science for Business*, O'Reilly, 2013), Chapter 2 ("Business Problems and Data Science Solutions")

**Last updated**: 2026-06-22

---

## The Six CRISP-DM Stages, and the One Thing That Matters Most About the Diagram

Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment. **The single most important feature of the actual CRISP-DM diagram, easy to miss if you only read the stage names**: it's drawn as **cycles within a cycle**, not a straight line — "iteration is the rule rather than the exception," and going through the full process once without solving the problem is not a failure, it's the normal, expected first pass. **The chapter's own characterization of why**: the entire first iteration is frequently best understood as exploration — the team genuinely knows much more after going through it once, and the second iteration is correspondingly better-informed. **A second structural detail worth keeping**: shortcuts exist directly from later stages back to Business Understanding (not just sequentially backward one step at a time) — because Evaluation can reveal the results simply aren't good enough to deploy, requiring the team to revisit the *problem definition itself*, not just rerun the model with different parameters.

## Business Understanding: Where Creativity, Not Automation, Does the Heavy Lifting

**The chapter's explicit point about where the "art" in this craft actually lives**: business problems essentially never arrive pre-packaged as clean data mining problems — the creative act of *reformulating* a messy business problem as one or more of the nine canonical tasks from [[canonical-data-mining-tasks-and-supervised-unsupervised]] is where a skilled analyst's judgment matters most, and "high-level knowledge of the fundamentals helps creative business analysts see novel formulations" that a purely technical specialist might miss. **The specific question to front-load here, flagged as one of the book's most important recurring concepts (developed across two later chapters)**: what exactly is the **use scenario** — what will actually be done with the result, and how? Getting this wrong at the start means the eventual model, however technically sound, may simply not answer the question the business actually needed answered.

## Data Understanding: Costs, Reliability, and the Fraud-Detection Contrast Restated as a Process Lesson

**Historical data was virtually never collected with your current problem in mind** — a customer database, a transaction database, and a marketing-response database may cover overlapping but distinct populations with varying reliability, and matching/deduplicating customer records across them is itself a nontrivial analytics problem in its own right (entity resolution). **A genuinely practical, often-skipped discipline worth keeping**: estimate the cost and benefit of *each* data source explicitly during this stage, and decide deliberately whether further data investment is actually merited — some data is free, some must be purchased, and some simply doesn't exist yet and requires its own ancillary collection project (directly the Signet Bank principle from [[data-asset-strategy-signet-bank-capital-one-case]], now placed at its specific point in the process). **The credit-card-vs-Medicare-fraud contrast from [[canonical-data-mining-tasks-and-supervised-unsupervised]] is explicitly framed here as the kind of discovery Data Understanding exists to surface**: a surface-level business-problem label ("fraud detection") can mask a fundamentally different underlying data structure, and catching that mismatch early (rather than after a supervised model fails for lack of a real target) is the actual point of this stage.

## Data Preparation and the Leakage Trap

Typical mechanical work here — converting to tabular format, handling missing values, normalizing numeric ranges — is explicitly **not the book's focus** (it's treated as its own specialized subfield). **What the book does insist on flagging, because it's genuinely easy to miss and genuinely damaging**: **leakage** — a variable present in the historical data that gives information about the target, but that **was not actually available at the moment the real decision would have to be made.** Two concrete, instructive examples worth keeping verbatim: predicting whether a website visitor is about to end her session using "total pages visited in the session" as a predictor — this is highly predictive, but it can't actually be known until *after* the session ends, at which point you already know the answer to the very thing you're trying to predict; predicting whether a customer will be a "big spender" using the categories of items they purchased (or worse, the tax they paid) — both are extremely predictive and both are only known *after* the spending has already happened.

**Why leakage is structurally easy to introduce, not just a careless mistake**: data preparation is "typically performed after the fact — from historical data," meaning the dataset naturally contains the full, completed record of everything that happened, including things that only became knowable *after* the outcome you're trying to predict. **The practical discipline this demands**: for every candidate predictor variable, explicitly ask "would I actually have known this value at the moment I needed to make the prediction, or only afterward?" — a question that has to be asked variable-by-variable, since leakage is rarely obvious from a variable's name alone (the book notes a more detailed, harder-to-spot real leak example is worked through later in the book, in the out-of-scope Chapter 14).

## Modeling and Evaluation: Why "Looks Accurate in the Lab" Isn't the Same as "Worth Deploying"

Modeling itself (the subject of most of the book's later, technical chapters) is "the part of the craft where the most science and technology can be brought to bear" — but **Evaluation exists specifically because "if we look hard enough at any dataset we will find patterns... but they may not survive careful scrutiny."** The goal is confidence that what was found is a genuine regularity, not a sample-specific idiosyncrasy (directly previewing the overfitting material the book develops at length later).

**A sharp, concrete illustration of why laboratory accuracy alone is insufficient**: a detection model (fraud, spam, intrusion) might be **>99% accurate** by ordinary lab standards and still be economically useless in production, because even a small false-positive *rate* applied against an enormous *volume* of legitimate cases generates an unmanageable number of false alarms — the real cost driver is the staffing required to handle every false alarm, plus the customer-relationship cost of wrongly flagging legitimate activity, neither of which shows up in a simple accuracy number. **A second, genuinely important practical point**: model evaluation increasingly has to extend beyond a static lab test into the live deployment environment itself, via carefully designed randomized controlled trials ("in vivo" testing, applying the model to some customers while holding others as a control group) — directly the causal-modeling task type from [[canonical-data-mining-tasks-and-supervised-unsupervised]], now applied specifically to validating whether the model itself actually improves outcomes once deployed, not just whether it predicts well in a static historical test set. **A subtler, easy-to-overlook deployment risk worth flagging**: behavior can change *in direct response to* a deployed model (fraudsters adapt once they sense detection has tightened; the input data's own format or substance can drift without ever notifying the data science team) — meaning evaluation is not a one-time gate passed before deployment, it's an ongoing instrumentation requirement for the life of the deployed system.

## Deployment: Often More Organizational Than Technical

**Deployment can be almost comically low-tech and still highly effective**: the book's own cited example — a set of diagnostic rules discovered through data mining for fixing a common industrial printing error, successfully deployed simply by **taping a printed sheet of the rules to the side of the printer.** Deployment can equally be a quiet change to a data-collection procedure, a strategic pivot, or a fully automated production system that rebuilds and retests its own models continuously (the book's example: automated ad-targeting systems that build new models in production as new campaigns launch) — the latter is necessary specifically when the world changes faster than a human team can manually re-curate models (fraud, intrusion detection) or when there are simply too many individual modeling tasks for manual curation to scale.

**The single sharpest organizational warning in the whole chapter, worth keeping as a standing maxim for any technical handoff**: "Your model is not what the data scientists design, it's what the engineers build." **Production re-coding for speed or system compatibility is real, substantial work, not a formality** — and the chapter's explicit recommended fix for the resulting "over the wall" risk is to involve development-team members (ideally hybrid "data science engineers," fluent in both the production systems and the analytics) **early**, as advisors from the start, gradually transferring ownership as the project matures, rather than handing off a finished prototype cold at the very end.

## Managing the Data Science Team: Why Treating This Like Software Engineering Is a Specific, Named Mistake

**The chapter's explicit, repeated warning, worth keeping as a standing caution for Chris's own client conversations whenever a project sponsor is a software/IT manager**: data mining looks superficially like a software development cycle (it involves code, milestones, deliverables) and managers comfortable running software projects naturally default to managing it the same way — **but this is "usually a mistake."** Data mining is "an exploratory undertaking closer to research and development than it is to engineering" — outcomes are genuinely uncertain in advance, and a given step's results can change the team's *fundamental understanding* of the problem itself, not just adjust a parameter. **Committing to a full production-grade engineering build before that uncertainty has been substantially reduced is "an expensive premature commitment."** **The recommended alternative, worth treating as a standard staged-investment discipline**: invest in cheap, fast information-reducing steps first — pilot studies, throwaway prototypes, a literature review of what's already been tried, and (at larger scale) a genuine experimental testbed supporting agile, repeated experimentation — before committing real engineering resources.

**A sharp, specific staffing/evaluation distinction worth keeping for any audit engagement Chris staffs or subcontracts**: software engineering evaluates people on code quality and throughput (lines written, tickets closed); **analytics work should instead evaluate people on their ability to formulate problems well, prototype quickly, make reasonable assumptions under ill-structured uncertainty, design experiments that represent genuinely good investments, and analyze results carefully** — these are different skills from traditional software engineering, and hiring or managing analytics talent using software-engineering metrics is a structural mismatch.

## Connects to

- [[canonical-data-mining-tasks-and-supervised-unsupervised]] — the credit-card-vs-Medicare-fraud contrast from that page is explicitly the kind of discovery the Data Understanding stage exists to surface before committing further resources.
- [[data-asset-strategy-signet-bank-capital-one-case]] — the explicit cost/benefit estimation discipline for each data source during Data Understanding is the process-level placement of that page's broader "data as a deliberate investment" principle.
- [[modeling-process-and-client-ethics]] — the iterative, cycles-within-a-cycle structure of CRISP-DM directly parallels that page's five-step system dynamics modeling process, both explicitly rejecting a linear, one-pass workflow in favor of repeated, insight-driven iteration.
- verify (skill) — the "in vivo" randomized evaluation discipline and the "looks accurate in the lab, fails in production" warning are the data-science-specific version of the general principle behind verifying a change actually works in the real system, not just in a controlled test.

## North Star Connection

- How this applies to the audit business: the CRISP-DM cycle is a directly reusable structuring framework for narrating any data/analytics-focused audit engagement to a client — explicit stages with explicit iteration make the process legible and build client trust the same way Block's contracting and phase structure does for general consulting engagements. The "data mining is R&D, not engineering" warning is a sharp, important expectation-setting tool for any client (especially one with a software/IT-manager sponsor) who wants firm milestones and guaranteed timelines on what is, honestly, an exploratory process. The leakage trap is a concrete, checkable due-diligence question for reviewing any analytics work a client's existing team or vendor has already produced.
- Track relevance: Tech / Business — directly supports the data-workflow and reporting use-cases, and gives Chris language for setting realistic client expectations on any analytics engagement.
- Possible future Second Brain use: a "could we have actually known this at decision time" leakage-check question, and an "R&D not engineering" client-expectation-setting script (modeled directly on this chapter's software-manager warning) are both strong candidate audit-toolkit artifacts.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The CRISP-DM cycle and the R&D-not-engineering warning are both directly reusable for structuring and selling any analytics engagement |
| Current usefulness | 5 | The leakage-check question is immediately applicable to reviewing any existing or proposed client model |
| KSU support | 3 | Process/methodology content, foundational for the technology track but not directly ISYE-quantitative |
| Tech-stack relevance | 4 | Core process vocabulary for any future `stack/ai-frameworks-apis` engagement |
| Business audit value | 5 | The "your model is what the engineers build" maxim and the R&D-not-engineering expectation-setting are both sharp, immediately usable client-management tools |
| Data/workflow value | 5 | The leakage-check discipline is a concrete, high-value due-diligence technique for any data-workflow audit |
| Reading urgency | 5 | Foundational process framework needed before any of the book's later technical chapters can be properly scoped or sold to a client |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Engagement-structuring and due-diligence tool — use the CRISP-DM cycle to narrate and structure any client-facing analytics engagement, set R&D-not-engineering expectations with software/IT-manager sponsors upfront, and apply the leakage check ("could this have actually been known at decision time?") to any existing model being reviewed.

**Use when**:
Scoping a new analytics engagement's timeline and deliverables with a client, or auditing an existing predictive model (built in-house or by a prior vendor) for hidden leakage before trusting its reported accuracy.

**Do not use when**:
The engagement is purely a one-off database query or reporting task with no pattern-discovery or predictive-modeling component — CRISP-DM's iterative-exploration framing doesn't apply to a simple, well-defined query.

**Fast retrieval query**:
`subject/crisp-dm` + `subject/data-leakage` — or search "CRISP-DM cycles within a cycle" / "data leakage total pages visited" / "your model is what the engineers build" / "data mining is R&D not engineering" / "printer rules taped to the side"
