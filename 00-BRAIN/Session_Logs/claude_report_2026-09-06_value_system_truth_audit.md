---
type: report
timeline: now
status: active
tags: [governance, review, business, revenue, systems, technology, ai-automation, metadata]
created: 2026-09-06
---

# Value-System Truth and Retrieval Audit — what is actually live in the non-school system?

### Scope: `03-WIKIS\BUSINESS` · `SYSTEMS` · `TECHNOLOGY` · `AI_AUTOMATION_SYSTEMS` · `REVENUE_LAB` · `05-BUSINESS`
### Surface: Claude Code (Opus 5) · Hat: Operator · Chris-directed, 2026-09-06
### Mode: **read-only**. Nothing was edited, moved, renamed, archived, or created inside the audited scope. `04-SCHOOL`, every `raw\`, and `88-JOURNAL` were not opened.
### Status: **audit delivered; seven decisions open for Chris. No change implemented.**

---

## 0. Authority and method

Chain loaded: `00-BRAIN\AGENT.md` → `00-BRAIN\CLAUDE.md` → `01-NORTH_STAR\NORTH_STAR.md` →
`Goals & Milestones\CURRENT_STRATEGY.md` → `VALUE.md` → each hub's `OPERATIONS.md` →
`00-BRAIN\WHERE_IT_GOES.md` § Metadata Standard.

Cross-checked against `00-BRAIN\CASTLE\wiki\opportunity-queue.md`, `00-BRAIN\SYSTEM_FLAGS.md`,
`.ROOT\NOW.md`, and a read-only run of `00-BRAIN\scripts\wiki_lint.py`.

471 markdown files read at frontmatter level; 165 carried `timeline: now` or `timeline: next`;
9 more carried a dated action that has passed. Every page in those sets was classified.

**Standing constraint honored throughout:** this is a truth-and-retrieval audit. No business
strategy is changed here, and **no research is called invalid merely because it is not currently
active.** Where a page is proposed for `reference`, its content is untouched and its value
unchallenged.

---

## 1. Verdict

**The knowledge is sound. The *when-to-act* layer is not.**

`.ROOT`'s research corpus is honest, sourced, and well-dispositioned. But the property that tells
a session what to touch — `timeline:` — has been overwritten across two hubs by an inherited
*reading-priority* scale, and one hub (REVENUE_LAB) is asserting a live status that CASTLE
parked six weeks ago against a driver Chris overturned three weeks ago.

**Exactly one page in the entire non-school value system is genuinely `now`:**
`03-WIKIS\BUSINESS\wiki\evidence\opportunity-landscape-run-1-sector-screen.md` (review 2026-09-13).

The other 127 `now` pages are mismarked. That is the finding.

| Layer | Score | Basis |
|---|:--:|---|
| Research quality and sourcing | 9/10 | Primary federal data with as-of dates; volatile claims labeled and given re-pull instructions |
| Raw-source disposition discipline | 9.5/10 | Every substantive raw file carries a truthful disposition, including honest "do not use as operational evidence" rows |
| Ownership boundaries as written | 9/10 | Hub contracts name their authority and their tie-breaks precisely |
| BUSINESS hub current-truth | 9/10 | Cleanest hub in scope; Run 2 can start today |
| **`timeline:` as an action axis** | **2/10** | Finding 1 — 145 files |
| **REVENUE_LAB vs. CASTLE reconciliation** | **3/10** | Findings 2 and 3 |
| **Dated-action follow-through** | **4/10** | Six triggers fired and went unrecorded |
| `05-BUSINESS` integrity coverage | 3/10 | Outside the lint boundary; two defects survived because of it |

Scores are judgment, not measurement.

---

## 2. Counts by hub and classification

| Hub | Files | Active now | Next | Reference (misfiled) | Parked | Archive cand. | Needs Chris | No change |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BUSINESS | 55 | 1 | 0 | 0 | 0 | 0 | 0 | 55 |
| SYSTEMS | 137 | 0 | 0 | **97** | 0 | 0 | 0 | 40 |
| TECHNOLOGY | 143 | 0 | 0 | **48** | 0 | 1 | 1 | 94 |
| AI_AUTOMATION_SYSTEMS | 89 | 0 | 1 | 1 | 0 | 0 | 4 | 84 |
| REVENUE_LAB | 15 | 0 | 0 | 5 | 5 | 0 | 1 | 5 |
| 05-BUSINESS | 34 | 0 | 0 | 6 | 0 | 0 | 3 | 25 |
| **Total** | **473** | **1** | **1** | **157** | **5** | **1** | **9** | **303** |

Raw timeline distribution across the scope: `reference` 237 · `now` 128 · `later` 57 · `next` 37 ·
`log` 10 · `historical` 1 · `parked` 1.

---

## 3. Finding 1 — `timeline:` was overwritten by FORGE reading-priority (145 files)

`WHERE_IT_GOES.md` § Metadata Standard defines `timeline` as the **action** axis:

> `now` means touch it now; `next` means on deck; `later` means intentionally deferred…
> Timeline answers only **when to act**.

The FORGE corpus inherited a different axis. Every inherited page ends with a `## Ranking` table
containing a **Reading urgency** row and an `**Overall priority**: NOW / NEXT / LATER` line. The
2026-07-21 `TAG_REGISTRY` conversion (`priority/*` → `timeline:`) copied that value straight
across, silently changing what the property means.

Cross-tabulation, SYSTEMS + TECHNOLOGY:

| `timeline:` | body says `Overall priority: NOW` | `NEXT` | `LATER` | no ranking line |
|---|---:|---:|---:|---:|
| `now` | **82** | 14 | 1 | 14 |
| `next` | 5 | 22 | 1 | 7 |
| `later` | 0 | 1 | 8 | 47 |

82 of 111 `now` pages literally say "Overall priority: NOW" in a *reading-urgency* table. The 14
`now / NEXT` and 1 `now / LATER` rows are self-contradictory even under the legacy reading.

**Worked example** — `SYSTEMS\wiki\wagner-whitin-dynamic-lot-sizing.md`: `timeline: later`;
body ranking "Reading urgency 3 — Mid-ingest of Chapter 2, actively in progress";
`**Overall priority**: LATER`. The frontmatter is a copy of a June reading judgment, not a
statement about when Chris should act.

**TECHNOLOGY is breaking its own written rule.** `TECHNOLOGY\OPERATIONS.md` § Metadata:

> Applied reference normally carries `timeline: reference` and `status: wiki-only`.

All 48 TECHNOLOGY files in this batch are applied reference in subfolders, carrying
`status: wiki-only` with `timeline: now`/`next`.

**SYSTEMS confirms the same intent.** Its `OPERATIONS.md` calls the hub "a **research-retrieval
engine** — a reference corpus with index and tag retrieval… It becomes a staged learning engine
only when ISYE 2600 activates," and "This hub tracks corpus state, not learner state."

### Consequence, concretely

`WHERE_IT_GOES.md` § Graph view defines the sequential "what's next" view as a search on
`[timeline:now]` → `[timeline:next]` → … Today that query returns 165 pages across the value
system, 164 of which are not actionable. **The retrieval mechanism the metadata standard was
built to serve currently cannot function.**

### What this finding is *not*

It is a frontmatter defect on one line per file. It says nothing about the quality, currency, or
future value of any page's content. No page is proposed for archive, demotion, or removal on the
strength of this finding.

---

## 4. Finding 2 — REVENUE_LAB's machine contract still asserts an overturned premise

`REVENUE_LAB\OPERATIONS.md` § *Why this hub exists* (`register: ai-directive`, `status: live`):

> Recorded 2026-07-14: a major cut in school funding means Chris needs additional income to
> continue past Fall 2026.

Chris ruled on 2026-08-11 — *"income is not as important as getting the system optimized to best
lead us to our 2031 goal"* — and reaffirmed it 2026-08-13. Income is a **target, not a survival
gate**.

`README.md` and `HOW_TO_USE.md` both carry explicit correction blocks recording that ruling.
`OPERATIONS.md` does not.

**The two human-facing files were corrected and the AI-directive file was left standing.** That
is the inversion that matters: `OPERATIONS.md` is the file a session loads and executes;
`README.md` is the file a human skims. The correction landed everywhere except where it binds.

The 2026-08-11 council named this exact failure mode in advance, quoted in `README.md`:

> *"an unreconciled survival claim sitting in a hub"* — the mechanism by which a future session
> re-raises a settled question.

It is still sitting there, 24 days later, in the one file that will be read.

`revenue-lane-scorecard.md` carries the same stale premise inside its CASTLE gate table —
"Phase | PASS | **The funding constraint makes a bounded survival test current-phase**" — with no
correction block at all, and `revenue-lane-scan-brief.md` still reads "Driver: school-funding cut"
in its header above its correction.

---

## 5. Finding 3 — REVENUE_LAB contradicts CASTLE, against its own tie-break rule

`REVENUE_LAB\OPERATIONS.md`:

> CASTLE's opportunity queue owns each opportunity's live status. When this wiki and the queue
> disagree, **the queue is current and this hub is behind — reconcile rather than assert.**

| Claim in REVENUE_LAB | CASTLE `opportunity-queue.md` |
|---|---|
| `revenue-lane-scorecard.md`: "**Survival track — B2 first test now.**" | OPP-20260714-01 — **`parked` since 2026-07-27**, contractor ~1,000 miles away, test cannot run as written |
| `wiki\index.md`: "B2 and Lane A research conditionally pass… **START HERE**" | OPP-20260714-02 (Lane A) — **`parked`**, project folder is literally `YT_Outlier_Scanner(Pause, chris)` |

Ten pages marked `timeline: now` are activating two parked opportunities. The hub is asserting,
not reconciling.

### The Aug 14 prediction check was never recorded

`revenue-lane-scorecard.md` § Honest Failure Conditions:

> Predictions to check ~August 14: B2 first paid engagement within 3 weeks of the conversation
> (yes/no); data-scan niche shortlist produced within 2 weeks of API-key approval (yes/no).

23 days past. Neither answer recorded. This is not bookkeeping — the hub's charter makes it
load-bearing:

> **Wrong predictions are kept and marked, never overwritten.** The rubric improves from its own
> misses, which requires the misses to remain visible.

Both predictions resolved "no," for the same reason, and that reason is the most valuable thing
the queue currently holds (§7).

---

## 6. Conflicts with live strategy, CASTLE, or another owner

**C-1 — `REVENUE_LAB\OPERATIONS.md` asserts a premise Chris overturned.** See §4. *Governance
file; requires explicit approval.*

**C-2 — REVENUE_LAB vs. CASTLE live status.** See §5.

**C-3 — TECHNOLOGY's spine reconciliation is 36 days overdue.**
`TECHNOLOGY\technology_boot_one_review.md` § Exact next action names:

> At the August 1 Technology review, read the live PYTHON current-position… update only the stale
> Current State and capability-trace rows in `TECHNOLOGY_LIBRARY_STRATEGY.md`, and name one
> bounded SQL proof with acceptance evidence.

`02-LIBRARY\ref-AI-automation\TECHNOLOGY_LIBRARY_STRATEGY.md` still reads
`## Current State — July 21, 2026` and still says the full reconciliation *"is scheduled for the
**August 1 monthly review**."* It never happened. The 2026-07-26 stale-claim patch is holding
(Stage 3 closed / Stage 4 active is stated correctly); the reconciliation it explicitly deferred
is open. *Target file is in `02-LIBRARY`, outside this audit's change scope — reported, not
manifested.*

**C-4 — Four AIAS proposals have a fired trigger and a placeholder outcome.**
`check_at: 2026-08-24`, `Outcome: (blank until the check date — record what actually happened,
with an evidence link)` — verbatim placeholder, 13 days past:

- `wiki\system-evolution\proposals\2026-07-08_agentic-tool-vetting-checklist.md`
- `wiki\system-evolution\proposals\2026-07-12_eval-gate-complexity-scaling.md`
- `wiki\system-evolution\proposals\2026-07-12_extension-trigger-table.md`
- `wiki\system-evolution\proposals\2026-07-13_belief-proposal-split-for-system-flags.md`

This violates the hub's own Proposal contract item 8 ("after application, outcome plus
keep/modify/revert verdict") and its LINT check for *"proposals without outcome, evidence,
verdict, or review trigger."* The 2026-08-02 Sunday sweep cleared the July batch cleanly; the
August 24 batch landed on the semester start and was never swept.
`2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md` (`check_at: 2026-11-30`) is correctly future
— no change.

**C-5 — `05-BUSINESS` has no automated integrity coverage.** `wiki_lint.py` reports 0 blockers
and 0 dead links across 1,623 pages, but its `HUBS` constant is the eight `03-WIKIS` hubs plus
CASTLE. `05-BUSINESS` is outside the scan. That is why the dead link and index drift below
survived. **The green lint result is true and narrower than it reads.**

**C-6 — A method page was deleted rather than archived.**
`05-BUSINESS\01-Audit Templates\workflow-observation-question-sequence.md:18` reads
`Method: [[../first-workflow-observation-field-plan|First Workflow Observation Field Plan]]`.
That file **does not exist anywhere in `.ROOT`, including `99-ARCHIVE`.**
`BUSINESS\wiki\log.md:618` records its creation; the 2026-07-24 architecture snapshot
(`System Update Log\2026-07-24_ROOT_ARCHITECTURE_UPDATE\tree.text:6978`) shows it present. It is
also cited by `BUSINESS\wiki\evidence\raw-source-map.md:90` as the retrieval target for *The Mom
Test*. Against `AGENT.md` § File Safety 3 and `WHERE_IT_GOES.md` ("nothing gets deleted, it gets
archived"). Git recovery should be attempted before the link is rewritten.

**C-7 — Stale `CLAUDE.md` hub-loader references in live pages.** The per-hub `CLAUDE.md` /
`AGENTS.md` loaders were removed 2026-08-10 and `WHERE_IT_GOES.md` says they "must not return."
Live pages still point at them:

- `REVENUE_LAB\wiki\index.md:13` — lists `CLAUDE.md` as an existing hub file
- `REVENUE_LAB\wiki\revenue-lane-scan-brief.md:70, :92` — sources the scoring rubric and the
  consequential-action rules from `CLAUDE.md`; both now live in `OPERATIONS.md`
- `TECHNOLOGY\technology_boot_one_review.md` — 6 occurrences (see §8)

`log.md` mentions are historical record and correctly frozen. **No change to any log.**

**C-8 — `05-BUSINESS\02-Field Notes\Symptom .md`** carries a trailing space in its basename.
Portability and retrieval defect. A rename, therefore Chris's call.

**C-9 — Cross-hub bare wikilink.** `BUSINESS\wiki\index.md:26` links
`[[apqc-process-classification-framework|APQC Process Classification Framework]]` with no path;
the page lives in SYSTEMS. It resolves by vault-wide name match (which is why lint passes), but
SYSTEMS' own LINT names "cross-hub link ambiguity" as a defect. See §7 — this is a Run 2 path.

---

## 7. What would obstruct Strategic Landscape Run 2

Run 2 is due **2026-09-20**: 15–20 opportunity cells across procurement/inventory,
capacity/scheduling, field operations, revenue/billing, claims/compliance, data/document flow,
asset reliability, and forecasting.

**O-1 — The SYSTEMS corpus is Run 2's functional substrate and its retrieval axis is noise.**
`market-map.md` § Level 2 directs Run 2 to pull "flow, variability, inventory, scheduling,
queuing, process-mining, forecasting, and decision patterns from the SYSTEMS wiki." A researcher
filtering that hub by `timeline` gets 97 of 133 pages back. Retrieval is currently possible only
through `index.md` and topic tags. **This is the single largest Run 2 friction, and Batch A
removes it.**

**O-2 — APQC is Run 2's Level-2 taxonomy and is reachable only by an ambiguous bare link.**
`market-map.md` § Level 2: "Use the APQC process families as the functional map."
`SYSTEMS\wiki\apqc-process-classification-framework.md` is marked `timeline: next` and is linked
from BUSINESS without a path (C-9). A read-only research worker told to use the APQC families may
not find it. Make the link explicit before Run 2 dispatches.

**O-3 — Run 1's `status: review` is load-bearing and Run 4 must honor it.** The screen records
its own limitation:

> An independent challenger was not available in this session, so the rankings remain
> `status: review`; **Run 4 must include an adversarial pass** before a strategic recommendation
> is eligible.

`AGENT.md` and `00-BRAIN\CLAUDE.md` both require an independent challenger for consequential work
by default. If Runs 2–3 proceed unchallenged, Run 4 inherits four unchallenged runs, and the
pilot's own stop condition — *"if two consecutive runs return source accumulation without a
decision-relevant change, pause the pilot and repair the questions"* — cannot be evaluated fairly.

**O-4 — The access constraint is the most important Run 2 input and is not in Run 2's inputs.**
CASTLE records it once, deliberately, in OPP-20260716-02's Result cell:

> ⚠ **Pattern, recorded once rather than as three separate misses:** this is the *third*
> construction/real-estate-adjacent test blocked on access simultaneously… All three designed a
> sound smallest test and all three failed at the same gate: **Chris has no warm-network access
> to the vertical the method needs.** That is one finding about the access constraint, not three
> about the ideas. It is the real input to any future Advisor-Builder lane choice.

Run 1's probability-adjusted ranking puts **construction #1 and real estate #2** — the two
verticals where three tests just died at the access gate. Run 2 must weight entry friction with
that evidence in hand, or it will re-rank toward the same wall.

This is a strategy *input*, not a strategy change. `CURRENT_STRATEGY.md` §7 already lists "access
wedges fail despite competent, completed outreach/tests" as vehicle-weakening evidence — and
these tests were never completed, because they were never runnable. That distinction should be
stated explicitly in Run 2 so the wedges are neither wrongly exonerated nor wrongly convicted.

**Not an obstruction.** BUSINESS is the cleanest hub in scope. `market-map.md` and the Run 1
screen are correctly marked, sourced to primary federal data with as-of dates, and carry explicit
disconfirmation conditions. **Run 2 can start.**

---

## 8. Proposed change manifest — exact, file by file

Nothing below has been executed.

### Batch A — 145 files · one mechanical operation · `now`/`next` → `reference`

**Selector (machine-checkable):** every `.md` under `03-WIKIS\SYSTEMS` or `03-WIKIS\TECHNOLOGY`
where `timeline ∈ {now, next}` **and** `status: wiki-only`.
**Edit:** the frontmatter `timeline:` line only. No body text, no `## Ranking` table, no content.

#### SYSTEMS — `wiki\`, `now` → `reference` (73)

`aggregation-and-challenging-the-clouds` · `barriers-to-learning-and-virtual-worlds` ·
`beer-game-and-origin-of-oscillations` · `business-cycle-origin-and-is-it-dead` ·
`causal-loop-diagram-guidelines` · `causal-loop-diagram-notation-and-polarity` ·
`causes-of-variability-breakdowns-setups-rework` · `cocaine-epidemic-stock-flow-case` ·
`commodity-cycles-and-the-generic-market-model` · `decision-analysis-and-utility-theory` ·
`discrete-event-simulation-and-random-variate-generation` ·
`duality-theory-and-economic-interpretation` · `dupont-maintenance-game-and-twelve-principles` ·
`dynamic-programming-and-the-principle-of-optimality` ·
`factory-dynamics-definitions-bottleneck-rate-and-critical-wip` ·
`factory-physics-formal-model-buffers-and-variability` ·
`factory-physics-four-step-improvement-methodology` · `factory-physics-framing-and-scope` ·
`fge-phantom-orders-and-sequential-debottlenecking` ·
`first-order-systems-growth-decay-and-doubling-time` ·
`flow-variability-and-queueing-fundamentals` ·
`forecasting-time-series-and-exponential-smoothing` ·
`fundamental-modes-growth-goal-seeking-oscillation` ·
`game-theory-two-person-zero-sum-games` · `global-warming-stock-flow-inertia-case` ·
`gm-auto-leasing-case-study` · `graphical-integration-and-differentiation` ·
`identifying-stocks-flows-and-state-determined-systems` ·
`ingalls-shipbuilding-project-dynamics-case` · `integer-programming-and-branch-and-bound` ·
`internal-benchmarking-and-hal-case-study` · `invisible-hand-and-market-feedback-structure` ·
`labor-supply-chain-and-overtime-stabilization` ·
`linear-programming-formulation-and-graphical-solution` ·
`littles-law-and-best-case-performance` · `manufacturing-peak-decline-resurgence` ·
`manufacturing-supply-chain-model` · `markov-chains-and-markov-decision-processes` ·
`metaheuristics-tabu-search-simulated-annealing-genetic-algorithms` ·
`modeling-process-and-client-ethics` · `multiechelon-inventory-and-revenue-management` ·
`multiple-loop-systems-and-loop-dominance` · `network-optimization-models` ·
`nonlinear-programming-and-kkt-conditions` · `pm4py-process-mining-in-python` ·
`policy-resistance-and-feedback-thinking` ·
`practical-worst-case-and-bottleneck-investment-tradeoffs` ·
`process-mining-manifesto-principles-and-challenges` · `project-management-with-pert-cpm` ·
`pulp-paper-cycles-and-sensitivity-analysis` · `qr-model-and-lead-time-variability` ·
`queueing-system-design-decisions` · `queueing-theory-birth-death-process-and-mms-models` ·
`real-estate-boom-bust-case-study` ·
`reliability-theory-series-parallel-and-k-out-of-n-systems` ·
`s-shaped-growth-overshoot-collapse-and-chaos` · `sensitivity-analysis-and-postoptimality` ·
`simplex-method-mechanics` · `statistical-inventory-models-newsvendor-base-stock` ·
`stock-flow-fundamentals-and-notation` · `stock-management-structure-and-amplification` ·
`strategic-objectives-hierarchy-and-efficient-frontiers` ·
`student-workload-causal-diagram-case-study` · `supply-chain-interactions-and-trust` ·
`time-horizon-and-endogenous-explanation` · `traffic-congestion-and-compensating-feedback` ·
`transportation-and-assignment-problems` · `value-stream-mapping-method-and-lean-guidelines` ·
`variability-pooling-and-chapter-8-conclusions` · `variability-randomness-and-classification` ·
`vut-equation-and-parallel-machines` ·
`what-went-wrong-three-trends-critique-and-case-for-science` ·
`worst-case-performance-and-batch-moves`

#### SYSTEMS — `wiki\`, `next` → `reference` (24)

`american-manufacturing-origins-and-system` · **`apqc-process-classification-framework`** ·
`blocking-and-finite-buffer-queues` · `bpmn-2-0-specification` ·
`capacity-planning-and-shop-floor-control` ·
`cost-accounting-pitfalls-abc-and-production-planning` ·
`descriptive-vs-prescriptive-models-and-conjecture-refutation` · `eoq-model-and-lot-sizing` ·
`erp-and-scm-history-and-tradeoffs` · `goodbye-jit-hello-lean` ·
`jit-implementation-tactics-and-quality-revolution` ·
`jit-origins-goals-and-environment-as-control` · `kanban-mechanics-and-pull-system-variants` ·
`labor-constrained-systems-and-flexible-labor` ·
`modern-manufacturing-organization-and-human-element` ·
`mrp-erp-empirical-failure-and-other-scientific-approaches` ·
`mrp-history-and-push-pull-paradigm` · `mrp-mechanics-netting-lot-sizing-bom-explosion` ·
`mrp-problems-nervousness-and-yield-losses` ·
`mrp-special-topics-lot-sizing-safety-stock-troubleshooting` · `scientific-management-and-taylor` ·
`the-art-of-spreadsheet-modeling` · `transshipment-problem` · `xes-standard-for-event-logs`

> **`apqc-process-classification-framework` is Run 2's Level-2 taxonomy (O-2).** It is `reference`
> because it is retrieval material, not a task — but its cross-hub link from BUSINESS should be
> made path-explicit in the same pass.

#### TECHNOLOGY — `wiki\`, `now` → `reference` (37)

`ai-and-llm\` — `co-intelligence-mollick` · `four-rules-for-co-intelligence` · `llm-fundamentals`

`data-science-ml\` — `ab-testing-hypothesis-tests-and-p-values` ·
`canonical-data-mining-tasks-and-supervised-unsupervised` · `crisp-dm-process-and-data-leakage` ·
`data-asset-strategy-signet-bank-capital-one-case` ·
`data-driven-decision-making-and-data-science-definition` ·
`generalization-overfitting-and-fitting-graphs` · `holdout-cross-validation-and-learning-curves` ·
`information-gain-entropy-and-attribute-selection` ·
`linear-discriminants-objective-functions-and-svm` ·
`linear-regression-least-squares-and-logistic-regression` ·
`probability-estimation-trees-laplace-correction-and-churn-case` ·
`related-analytics-techniques-and-business-questions` · `tree-induction-and-decision-boundaries` ·
`tree-vs-linear-models-and-nonlinear-extensions`

`database-sql\` — `practical-sql` · `sql-advanced-query-techniques` · `sql-data-types` ·
`sql-grouping-and-aggregate-functions` · `sql-importing-and-basic-math` ·
`sql-inspecting-and-modifying-data` · `sql-joining-tables-and-relationships` ·
`sql-select-where-and-filtering` · `sql-table-design-constraints-and-indexes` ·
`sql-views-functions-and-triggers` · `sql-window-functions-and-ranking`

`web-frameworks\` — `flask-basic-application-structure` · `flask-databases-with-sqlalchemy` ·
`flask-email-with-flask-mail` · `flask-large-application-structure` · `flask-rest-apis` ·
`flask-templates-and-jinja2` · `flask-user-authentication` · `flask-web-development` ·
`flask-web-forms`

#### TECHNOLOGY — `wiki\`, `next` → `reference` (11)

`ai-and-llm\` — `ai-alignment-and-ethics` · `ai-as-a-coworker` · `ai-as-a-person` ·
`ai-as-tutor-and-coach` · `ai-creativity-and-hallucination` · `ai-developer-tools-landscape-2026`

`devops\web-application-security-basics` · `web-frameworks\task-queues-for-background-jobs`

`security\` — `api-security-testing-engagement-scoping-and-checklist` ·
`api-vulnerability-classes-owasp-top-10` · `hacking-apis-source-summary`

> **Same class, not manifested:** a further **56** pages carry `timeline: later` +
> `status: wiki-only`. They fall outside the stated audit trigger, so I did not list them — but
> `later` ("intentionally deferred") is equally wrong for a retrieval corpus. Fixing 145 and
> leaving 56 leaves the axis half-converted. **Recommendation: one 201-file pass.**

### Batch B — REVENUE_LAB (10 files)

| File | Current | Proposed | Reason |
|---|---|---|---|
| `wiki\revenue-lane-scorecard.md` | `now` | `parked` + correction block | Both gated lanes parked in CASTLE; gate table still cites the funding constraint (§4); Aug 14 prediction unrecorded (§5) |
| `wiki\index.md` | `now` | `parked` | Calls scorecard "START HERE"; lists nonexistent `CLAUDE.md`; "Prediction check ~Aug 14" passed |
| `wiki\revenue-lane-scan-brief.md` | `now` | `parked` | Lines 70 and 92 source the rubric and action rules from the removed `CLAUDE.md` |
| `wiki\yt-outlier-scanner-first-findings-2026-07-14.md` | `now` | `parked` | OPP-20260714-02 parked; project folder named `(Pause, chris)` |
| `wiki\proof-led-content-strategy-decision-2026-07-16.md` | `now` | `parked` | Conditional GO on a parked lane |
| `wiki\lane-a-content-channel.md` | `now` | `reference` | Durable scored evidence; live status is CASTLE's |
| `wiki\lane-b-freelance-estimating.md` | `now` | `reference` | " |
| `wiki\lane-c-tutoring.md` | `now` | `reference` | " |
| `wiki\lane-d-digital-products.md` | `now` | `reference` | " |
| `wiki\lane-e-ai-assisted-content.md` | `now` | `reference` | " |

### Batch C — 05-BUSINESS (6 files + 2 repairs)

| File | Current | Proposed |
|---|---|---|
| `01-Audit Templates\OBSERVATION_METHODOLOGY.md` | `now` | `reference` |
| `01-Audit Templates\ONE_PAGE_FINDINGS_FORMAT.md` | `now` | `reference` |
| `01-Audit Templates\workflow-observation-question-sequence.md` | `now` | `reference` + link repair (C-6) |
| `01-Audit Templates\TECHNOLOGY_AUDIT_REPORT_TEMPLATE.md` | `next` | `reference` |
| `06-Capability Library\APQC_13_1_WORKFLOW_OBSERVATION_MAP.md` | `now` | `reference` |
| `06-Capability Library\APQC_13_1_WORKFLOW_TECHNOLOGY_STACK_EVIDENCE_TEMPLATE.md` | `next` | `reference` |

Blank reusable masters are `reference` by definition ("use when needed"); every other template in
`01-Audit Templates` already is. None can be exercised — all three field-access opportunities are
parked.

Repairs:
- `TEMPLATE_INDEX.md` — add the 3 missing `01-Audit Templates` rows (lists 5 of 8:
  `OBSERVATION_METHODOLOGY`, `ONE_PAGE_FINDINGS_FORMAT`, `TECHNOLOGY_AUDIT_REPORT_TEMPLATE` absent).
- `01-Audit Templates\workflow-observation-question-sequence.md:18` — dead method link (C-6).

### Batch D — AI_AUTOMATION_SYSTEMS (2 files)

| File | Current | Proposed | Reason |
|---|---|---|---|
| `wiki\agents\agent-vetting-worked-examples.md` | `now` | `reference` | Research page, no action; sole outlier among 86 `reference` siblings |
| `wiki\system-evolution\proposals\2026-07-12_session-close-high-flag-hook.md` | `now` | `next` (low) | Traces to a genuinely open flag (#93), but #93 is **MEDIUM** = "address at the next relevant review," not now |

### Batch E — TECHNOLOGY (1 archive candidate)

`03-WIKIS\TECHNOLOGY\technology_boot_one_review.md` — `timeline: now`, `status: complete`, dated
2026-07-26. Three defects:

1. **Self-contradictory** — `now` + `complete`.
2. **Certifies a dead architecture.** Its PASS validates the boot chain
   `TECHNOLOGY\AGENTS.md → TECHNOLOGY\CLAUDE.md → OPERATIONS.md`. Those loaders were removed
   2026-08-10; `WHERE_IT_GOES.md` says they "must not return." The hub now holds only
   `HOW_TO_USE.md`, `OPERATIONS.md`, `README.md`, and this report.
3. **Wrong home.** A completed standalone report at a hub root; the hub archetype standard admits
   `OPERATIONS` / `README` / `HOW_TO_USE` / `wiki\index` / `wiki\log` and states "No other file is
   universal."

**Proposed:** `99-ARCHIVE\ARCHIVED_2026-09-06_technology_boot_one_review.md`.
**Precondition:** extract its live overdue next action first (C-3), or archiving a stale report
silently retires an open commitment.

---

## 9. The ten highest-value corrections

1. **Correct `REVENUE_LAB\OPERATIONS.md` § Why this hub exists** to the 2026-08-13 ruling,
   preserving the superseded text visibly as `README.md` and `HOW_TO_USE.md` already do. Highest
   value because it is the only defect that can actively cause a future session to act on an
   overturned premise. *Requires Chris's approval — governance file.*
2. **Reconcile the 10 REVENUE_LAB `now` pages against CASTLE** (Batch B). Removes the hub's
   assertion that two parked lanes are live.
3. **Run Batch A plus the 56 `later` siblings as one 201-file metadata pass.** This is what makes
   `[timeline:now]` retrieval and the Obsidian sequential graph mean anything again.
4. **Record the four overdue AIAS proposal outcomes** with keep/modify/revert verdicts, or re-date
   them with a stated reason. A placeholder that has outlived its trigger is how a proposal ledger
   starts lying.
5. **Extract the TECHNOLOGY spine reconciliation before archiving the boot review** (C-3 / Batch E).
6. **Record the Aug 14 REVENUE_LAB prediction check** — predicted vs. actual, both "no," both for
   the access reason. The rubric cannot improve from a miss that was never scored.
7. **Recover `first-workflow-observation-field-plan.md` from git history**, or record its loss
   honestly (C-6).
8. **Extend `wiki_lint.py` to cover `05-BUSINESS`**, or state in `WHERE_IT_GOES.md` that the asset
   system is deliberately unlinted (C-5).
9. **Dispose of the `CAPABILITY_LIBRARY_INDEX` "run first live validation rep before Aug 24" row**
   — 13 days passed and currently unrunnable, since all three field-access opportunities are
   parked. Same pattern the queue already flagged on OPP-20260727-01: *"An indefinitely re-dated
   row is how a queue starts lying."*
10. **Batch C — six blank masters to `reference`.** Small, but it is the difference between "six
    audit assets awaiting action" and the truth: six templates waiting for access that does not
    exist.

---

## 10. No-change conclusions

**303 files are correctly classified today.** The substantive ones:

- **All 55 BUSINESS files.** The one `now` page is genuinely now (review 2026-09-13, future). The
  53 `reference` pages — methods, offers, operating models, pathways, scenarios — are correctly
  `reference`. **None is proposed for archive, and none is invalid for being inactive.**
- **`market-map.md` stays `timeline: reference`, `status: maintained`.** It is the standing method
  and evidence map Run 2 *retrieves*, not a task. `CURRENT_STRATEGY.md` and CASTLE own activation.
  Correct as filed.
- **`market-map.md`'s 12-week-stale BTOS snapshot needs no change.** It carries an as-of date, a
  source, a volatility label, and "re-pull before use" — fully compliant with the BUSINESS
  evidence standard. This is volatile-claim discipline done correctly and worth preserving as the
  pattern other pages copy.
- **All 86 AIAS `reference` research pages**, including the seven proposals whose `check_at` fired
  and whose outcomes were properly recorded on 2026-08-02, and
  `2026-07-12_mcp-vetting-screen-secure-tunnel-gap.md` whose `check_at: 2026-11-30` is correctly
  future.
- **The SYSTEMS and TECHNOLOGY raw-source coverage ledgers.** Every substantive raw file carries a
  truthful disposition, including honest "parked, quality-limited — do not use as operational
  evidence" rows. This is the strongest single practice in the audited scope.
- **All `log.md` files and `REVENUE_LAB\99-ARCHIVE\…\ARCHIVE_MANIFEST.md`.** Their `CLAUDE.md`
  references are historical record; freezing them is correct.
- **All 15 ALL-CAPS content filenames in `05-BUSINESS`.** Grandfathered by `WHERE_IT_GOES.md`
  § Case convention — "No unilateral renames." Not a defect; no rename proposed.
- **`05-BUSINESS\02-Field Notes\Full_AI_Assit_for_processmap1.md`** — `timeline: parked` is
  correct and is the only correctly-parked page in the audited scope.
- **The content of all 145 Batch A pages.** Their research is not stale, not superseded, and not
  invalid. One frontmatter line per file is wrong; nothing else is.

---

## 11. Open decisions — Chris's, not mine

| # | Decision | Why it is yours |
|---|---|---|
| 1 | Correct `REVENUE_LAB\OPERATIONS.md` (§4) | Governance file, `register: ai-directive` — `AGENT.md` requires explicit approval |
| 2 | Does REVENUE_LAB go formally dormant? | Both lanes parked; driver downgraded. A charter-level call |
| 3 | Keep / modify / revert on the four overdue AIAS proposals | Proposal contract item 8 reserves the verdict to Chris or the owning review mechanism |
| 4 | `CAPABILITY_LIBRARY_INDEX` Aug 24 row — re-date or park | Third re-date risk; the queue's own rule says park instead |
| 5 | Attempt git recovery of `first-workflow-observation-field-plan.md`? | Touches history; may need a commit range you remember |
| 6 | Rename `05-BUSINESS\02-Field Notes\Symptom .md` | A rename — `WHERE_IT_GOES.md` forbids unilateral renames |
| 7 | Batch A at 145 files, or 201 including the `later` siblings? | Scope call |

---

## 12. Method limitations — stated, not hidden

- **No independent challenger.** Per `00-BRAIN\CLAUDE.md`, consequential work uses an independent
  validator by default; none was available this session. Deterministic checks were used instead —
  frontmatter extraction across 471 files, a body-vs-frontmatter cross-tabulation on the
  `Overall priority` line, a dated-action regex sweep, a filesystem existence check on every
  claimed hub file, and a read-only `wiki_lint.py` run. **Chris decides whether that bounded
  fallback is sufficient before any batch executes.**
- **Frontmatter-level read for the 145-file batch.** Bodies were sampled, not read in full. The
  classification rests on the frontmatter contract plus each hub's own written rule, which is the
  correct authority for a `timeline:` judgment — but it is not a content review, and no content
  claim is made about those pages.
- **`02-LIBRARY` and `00-BRAIN\CASTLE` were read for authority only.** C-3's target file lives in
  `02-LIBRARY` and is reported, not manifested.
- **Bulk-edit discipline applies to anything approved here.** `AGENT.md` § File Safety 8 requires
  proving the operation on a disposable copy and using `safe_shell.sh` after its self-test before
  a bulk edit runs. Batch A is a bulk edit.
- **A `root_health.py` PASS would cover named technical checks only** — not the semantic truth
  this report is about.

---

## 13. Close

- **Outcome:** value-system truth audit delivered. 473 files classified; 1 genuinely active page
  found; 165 mismarked; 9 conflicts and 4 Run 2 obstructions named.
- **Evidence:** this report; `wiki_lint.py` read-only run (0 blockers, 0 dead links — scope
  limitation recorded at C-5); cross-tabulation in §3.
- **Owner/status movement:** **none.** No file in the audited scope was changed. `SYSTEM_FLAGS.md`
  not written. CASTLE not written. No wiki log appended, because no wiki operation occurred.
- **Next exact action:** Chris rules on the seven decisions in §11, starting with #1. Nothing in
  §8 executes before that.
- **Approval/blocker:** Batch A is a bulk edit and decision #1 is a governance edit. Both are
  blocked on explicit approval.

*Report location: `00-BRAIN\Session_Logs\` — stays at root while its decisions are active, then
moves to `Report Archive\` per `Session_Logs\README.md`.*
