---
type: research
timeline: reference
tags: [ai-automation, advisor-builder, ai-adoption, opportunity-scoring, client-frameworks]
source: raw/The Business Case for AI.pdf (Kavita Ganesan, "The Business Case for AI — A Leader's Guide to AI Strategies, Best Practices & Real-World Applications," © 2022, self-published, 294 physical pp. — chunked ingest 2026-07-17; full coverage Introduction + Parts 1–5 + Conclusion (phys pp. 1–~277); About the Author/Connect/Bulk Orders/Acknowledgments/References (to p. 294) classified reference back matter, contents inspected)
---

# The Business Case for AI (Ganesan, 2022) — The Leader's AI-Adoption Playbook

**Kavita Ganesan, PhD** (NLP/search; UIUC/USC), fifteen-year practitioner —
academic research → building AI products → Fortune 500 and SMB/hospital
consulting via her firm Opinosis Analytics. Audience: executives, innovators,
and product managers, explicitly *not* data scientists. The book opens
"**Stop using AI**" — on problems too small for it — and its through-line is
the **disconnect thesis**: the gap between leadership's idea of AI and
implementation reality is the root cause of canceled projects, non-AI work
labeled AI, and initiatives with dismissible benefits. Her consulting always
starts with leadership education before implementation — the same posture as
`.ROOT`'s Advisor-Builder bet.

**Era warning (read first):** © 2022, fully **pre-generative-AI**. "AI" here
means custom ML/DL/NLP/CV pipelines built on your own training data. The
*decision frameworks* below are largely durable; the *feasibility and cost
answers* they produce have shifted hard since — many 2022 "needs a data
scientist + labeled data + months" tasks (sentiment, classification,
extraction, summarization, assistants) are now off-the-shelf LLM calls. Run
every framework with 2026 build/buy/feasibility inputs, not the book's. All
named case-study numbers, salaries, vendor lists, and survey stats are
2019–2021 snapshots — treat as illustrations, never citable current facts.

## Why this book matters to `.ROOT` (the retrieval jobs)

This is the closest thing in the hub to a **client-engagement operating
manual for the Advisor-Builder business**: enter an unfamiliar operation,
find where AI creates measurable value, decide build-vs-buy, implement, and
prove the benefit. It supplies the missing formal layer under BUSINESS's
`smb-ai-audit-method`: opportunity triage, readiness assessment, and
success measurement, each as a repeatable named framework.

## 1. The anti-hype screen: AI vs. "simple software automation"

The book's most-used tool. Most "AI projects" are software-engineering
problems mislabeled (patent-attorney story; oncologist treatment-summary
story). AI-for-AI's-sake has named causes — executive push, **funding
optics** (MMC 2019: ~40% of European "AI startups" used no AI and drew
15–50% more funding), and internal innovation theater. Screening rule:
automation requiring humanlike judgment on case-by-case data = AI candidate;
everything else = better software engineering or a manual process. Her
default sequencing: **start with simple automation or a manual baseline,
replace with AI only on demonstrated benefit** — independently the same
verdict as `.ROOT`'s CASTLE profit-gate discipline (baseline first, evidence
before build).

Five success tips: understand AI → fix foundational gaps first → define
ROI-as-benefits (not immediate financials) → budget sufficiency → long-term
commitment. Five myths countered, including the reusable **deployment-role
triage**: given known error rates, is the model the *sole decision-maker*,
an *assistant*, or a *second opinion*? (Consequence severity decides.)

## 2. IDA: the analytics wedge for client work

**Simple data analytics** (aggregate data as-is) vs. **intelligent data
analytics** (enrich/standardize/summarize messy unstructured data with
ML/NLP *before* analysis; ~80% of enterprise data is unstructured, 60–73%
unused per Forrester). Six IDA plays, all client-shaped: listening at scale
(Ocean Spray → new product lines), consolidating disparate feedback channels
(the fintech Twitter-shaming cautionary tale; her own hospital
patient-experience engagement), open-ended employee-survey standardization,
**search logs as an underused goldmine** (site-search diagnosis, content
strategy), NLP root-cause clustering of incident reports, and BI-tool
augmentation. Staffing rule-of-thumb ladder (done-for-you service /
off-the-shelf / in-house pipelines) — in 2026, LLMs move most of these plays
several rungs down the cost ladder, which *strengthens* the wedge.

## 3. The ML development life cycle (leader's view)

Six phases: problem definition & planning → data acquisition → model
development → **post-development testing** → deployment → monitoring.
Durable lessons: Phase 1 is the most critical and most skipped (decompose
the business problem into subproblems to isolate the actual AI piece);
**plan deployment constraints from day one** (the Rob latency-rework story);
PDT is mandatory (dev performance ≠ production performance; Tay); models
drift (2019 recommender in pandemic 2020) — set-and-forget is the
anti-pattern. Matches this hub's enterprise-roadmap and eval findings.

## 4. B-CIDS readiness + Jumpstart (the client-assessment layer)

Five preparation pillars — **B**udget, **C**ulture, **I**nfrastructure,
**D**ata, **S**kills — assessed by yes/no/some rubric to expose gaps.
Data readiness = four questions: storing? warehousing? **logging?**
(customer interactions, production events, search activity — with legal
check) digitized paper? Cultural readiness = six elements incl. org-wide AI
literacy (defuses fear-driven resistance), cross-functional minimum team
(business stakeholder + AI implementor + engineers; the
data-scientist-can-do-it-all misconception = "chef without kitchen staff"),
and an ethics/accountability committee. The **Jumpstart approach** runs two
tracks in parallel: *disruptive* (pilot 1–2 high-impact initiatives now,
formalize what you learn) and *proactive gap-fill* (close foundational gaps
in planned order). Expectation set: 6 months–2 years to real difference.

## 5. The HI-AI Discovery Framework (the core reusable asset)

Four steps from idea to prioritized portfolio:

1. **Identify PAIs** (potential AI initiatives). Classify the starting
   point — A: manual solution exists; B: software automation exists; C: new
   problem, no solution (highest risk — no fallback, no data exhaust). Then
   gate questions: complex humanlike decision-making? high workload
   (volume × recurrence)? data known and available (maybe allowed)? and for
   B only: accuracy/manageability problems in the incumbent? All yes = PAI.
   Manual processes generate training-data exhaust — a hidden asset;
   pair rules-with-humans to bootstrap data where none exists.
2. **Frame PAIs**: pain point (quantified), project description, potential
   benefits, expected **ROAI** (return on AI investment — improvement over
   an explicit *baseline measurement* per metric, short- vs long-term
   bucketed), data/feasibility notes.
3. **Expert verification**: red flags, reframing, simpler alternatives,
   timeline, and feasibility at three depths (review / +data exploration /
   +prototype — prototype-level for anything complex).
4. **I2R2 scoring**: Implementation-ready? Impact size? ROAI clear? Risk if
   it fails? Each 1/3/5, (weighted) average; **≥4 after verification =
   HI-AI**, pursue; 1–3 = fix the gaps or skip.

The anti-pattern it replaces: bottom-up AI, where hired data scientists
invent projects from available data (the celebrated engineer whose models
never reached production because they solved no business problem).

## 6. Build or buy, and what 2026 changes

Buy (prepackaged; convenient but overgeneralized — test on *your* data
before purchase), internal data-science teams, consultants (three engagement
models: end-to-end / **working prototype** handed to engineering /
technical-advisory coaching), or in-house hires (rule of thumb: 2–3 data
engineers per data scientist; don't hire FTE data scientists without a
project pipeline). Consultant-vetting screen: problem-focused not
techniques-focused, verified past projects (the five-open-source-tools
"data science" vendor story), phased scoping. The 2022 cost table
(~$200/hr consultant vs. ~$150K+ FTE) is stale in numbers but the
*structure* of the comparison survives. **2026 note:** foundation models
collapse much of the build side — the modern first question is "does a
frontier-model API + prompt/context engineering solve this?" before any
custom-ML path; this strengthens buy/assemble and weakens
hire-data-scientists-first even further.

## 7. Measure success: the three-pillar model (the proof layer)

A successful initiative is strong on **all three** pillars:

- **Model success** — DevPerform vs. **ProdPerform** (offline vs. online),
  acceptable thresholds are task-dependent; wide dev→prod gaps mean broken
  assumptions.
- **Business success** — ROAIs tracked against baselines and expected-ROAI
  targets, iteration by iteration; model accuracy has **diminishing
  returns** against ROAI (don't chase 95% when 90% saturates the business
  metric — the Rima story: accuracy fixation with no articulated benefit).
- **User success** — interviews/surveys of the people consuming the AI
  output; surfaces adoption risk and **non-model factors** (UI placement,
  training, latency, wrong metrics) that get wrongly blamed on models.

Decision loop: iterate / deploy-and-iterate / back to drawing board; deploy
when all pillars clear minimum thresholds (optional 1–5 strength scores,
≥3 each). This is the **seventh independent restatement of the
verification-capacity verdict** in this hub — measurement capacity, not
model capability, gates value — and the client-billable version of it:
[[enterprise-ai-adoption-and-production-roadmap]] is Anthropic's 2025 genAI
edition of this same sequence (bounded use case → evals → progressive
rollout → production feedback), converging from the vendor side.

## Cross-links and placement notes

- BUSINESS hub's `smb-ai-audit-method` is the applied home for these
  frameworks in client engagements; this page is the source-depth layer
  (candidate cross-link at BUSINESS's next touch — not edited from here).
- Vetting/tooling depth: [[agent-vetting-worked-examples]],
  [[workflow-automation-tools-landscape]]; governance vocabulary:
  [[nist-ai-rmf]]; bias section (COMPAS, Gender Shades, whitened-résumés
  studies) overlaps and is superseded in depth by
  [[algorithmic-fairness-metrics-ground-truth-and-intervention]] and
  [[training-data-representation-and-feedback-risk]].
- Do not promote: any named case-study metric, cost figure, vendor, or
  survey stat without current verification; the Vodafone video-screening
  example now sits in a legally contested practice class (AI hiring
  regulation post-dates the book).

*Ingested 2026-07-17 in five extraction blocks (phys pp. 1–30, 31–95,
96–165, 166–235, 236–294); chunk provenance in `source:` frontmatter.
References (86 endnotes) inspected as citation back matter.*
