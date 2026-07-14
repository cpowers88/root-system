---
type: reference
tags: [reference, systems]
---

# SYSTEMS Wiki — Index

98 pages (verified count, 2026-07-13). 40 moved intact from `FORGE\wiki\systems\` on July 7, 2026 (FORGE
retirement); 30 more moved the same day from FORGE's `wiki\business\` — Sterman
*Business Dynamics* case studies and Factory Physics/JIT/lean/MRP/ERP history pages
that were filed under FORGE's business/ folder but are subject/factory-physics or
subject/system-dynamics content, confirmed via frontmatter before the move (`domain:`
retagged from `business` to `systems` on arrival; content otherwise unchanged). Every
page keeps its original frontmatter tag tracks (`type`, and the full
priority/status/domain/source-role/use-case/subject tracks) — see `CLAUDE.md` and
`HOW_TO_USE.md` for how the tagging system works. 4 more added July 8, 2026 from new
sources dropped in `raw/` (process mining + VSM cluster) — the first pages ingested
directly into this wiki rather than inherited from FORGE.

## Stocks, Flows & Causal Loop Diagrams

- [[stock-flow-fundamentals-and-notation]] — formal stock/flow definitions, notation, why stocks drive dynamics
- [[identifying-stocks-flows-and-state-determined-systems]] — snapshot test, units discipline, presenting models to clients
- [[graphical-integration-and-differentiation]] — reading stock/flow behavior off a graph, no calculus
- [[global-warming-stock-flow-inertia-case]] — why temperature keeps rising after emissions stop
- [[first-order-systems-growth-decay-and-doubling-time]] — exponential growth, Rule of 70
- [[causal-loop-diagram-notation-and-polarity]] — link polarity, the stock/flow trap
- [[causal-loop-diagram-guidelines]] — eleven rules for readable CLDs

## Feedback, Growth & Oscillation

- [[policy-resistance-and-feedback-thinking]] — why interventions backfire; event vs. feedback worldview
- [[barriers-to-learning-and-virtual-worlds]] — nine reasons experience-based learning fails in complex systems
- [[fundamental-modes-growth-goal-seeking-oscillation]] — the three fundamental modes and their generating structures
- [[s-shaped-growth-overshoot-collapse-and-chaos]] — limits, overshoot/collapse, Easter Island, chaos
- [[multiple-loop-systems-and-loop-dominance]] — why linear models can't produce S-shaped growth
- [[descriptive-vs-prescriptive-models-and-conjecture-refutation]] — modeling philosophy

## Supply Chains, Business Cycles & Markets

- [[stock-management-structure-and-amplification]] — the generic stock management structure, why supply chains amplify
- [[manufacturing-supply-chain-model]] — full staged supply chain model, amplification and lag
- [[labor-supply-chain-and-overtime-stabilization]] — hiring delays cause oscillation; overtime as a fix
- [[business-cycle-origin-and-is-it-dead]] — the business cycle as damped oscillation
- [[commodity-cycles-and-the-generic-market-model]] — why commodity markets don't self-correct

## Factory Physics — Basic Dynamics

- [[littles-law-and-best-case-performance]] — WIP = TH × CT, derived and applied
- [[factory-dynamics-definitions-bottleneck-rate-and-critical-wip]] — precise definitions
- [[worst-case-performance-and-batch-moves]] — worst-case line performance
- [[practical-worst-case-and-bottleneck-investment-tradeoffs]] — PWC performance, investment tradeoffs
- [[internal-benchmarking-and-hal-case-study]] — the HAL PCB case
- [[labor-constrained-systems-and-flexible-labor]] — labor as the binding constraint
- [[factory-physics-formal-model-buffers-and-variability]] — the formal model, three buffers

## Variability & Queuing

- [[variability-randomness-and-classification]] — CV classification, LV/MV/HV
- [[causes-of-variability-breakdowns-setups-rework]] — formulas and worked examples
- [[flow-variability-and-queueing-fundamentals]] — arrival CVs to the M/M/1 queue
- [[vut-equation-and-parallel-machines]] — Kingman's equation, variability pooling
- [[blocking-and-finite-buffer-queues]] — the M/M/1/b model
- [[variability-pooling-and-chapter-8-conclusions]] — pooling across batch/safety-stock/queue contexts

## Factory Physics — Manufacturing History & Methodology

- [[factory-physics-framing-and-scope]] — what Factory Physics claims to be and its scope
- [[factory-physics-four-step-improvement-methodology]] — the book's closing improvement method
- [[american-manufacturing-origins-and-system]] — the American System and the rise of Big Business
- [[scientific-management-and-taylor]] — Taylor's system, its insight, its flaw
- [[modern-manufacturing-organization-and-human-element]] — structure and the human element
- [[manufacturing-peak-decline-resurgence]] — golden era, decline, the professional-manager critique
- [[mrp-history-and-push-pull-paradigm]] — the MRP crusade, independent/dependent demand, push vs. pull
- [[mrp-erp-empirical-failure-and-other-scientific-approaches]] — why MRP/ERP/BPR/VSM/DMAIC all fall short of a real systems paradigm
- [[erp-and-scm-history-and-tradeoffs]] — MRP II to ERP/SCM, the unresolved core problem
- [[jit-origins-goals-and-environment-as-control]] — JIT's origins, the seven zeros
- [[jit-implementation-tactics-and-quality-revolution]] — capacity buffers, setup reduction, cell layout, the quality revolution
- [[goodbye-jit-hello-lean]] — JIT's rebrand to lean, Six Sigma replacing TQM
- [[what-went-wrong-three-trends-critique-and-case-for-science]] — the case for a science of manufacturing
- [[strategic-objectives-hierarchy-and-efficient-frontiers]] — order winners, connecting strategy to operations
- [[cost-accounting-pitfalls-abc-and-production-planning]] — why ABC isn't enough; fully-absorbed costs bankrupting production plans

## Sterman Case Studies — Applied System Dynamics

- [[beer-game-and-origin-of-oscillations]] — why ignoring the supply line causes oscillation
- [[real-estate-boom-bust-case-study]] — professionals making the same mistake as beer-game novices
- [[gm-auto-leasing-case-study]] — how a carmaker's own policy created its competitor
- [[ingalls-shipbuilding-project-dynamics-case]] — quantifying project ripple effects with the rework cycle
- [[dupont-maintenance-game-and-twelve-principles]] — reactive-maintenance trap, Sterman's twelve principles
- [[fge-phantom-orders-and-sequential-debottlenecking]] — a hot product becoming an inventory write-down
- [[cocaine-epidemic-stock-flow-case]] — stock-flow logic vs. government survey data
- [[traffic-congestion-and-compensating-feedback]] — policy resistance and compensating feedback
- [[invisible-hand-and-market-feedback-structure]] — speculative bubbles, the Medigap death spiral
- [[supply-chain-interactions-and-trust]] — instability destroying trust, lead-time gaming
- [[pulp-paper-cycles-and-sensitivity-analysis]] — two cycles, one model, stress-testing before trusting
- [[student-workload-causal-diagram-case-study]] — a full worked causal-diagramming case
- [[aggregation-and-challenging-the-clouds]] — two real stock-flow case studies
- [[modeling-process-and-client-ethics]] — managers as designers, the modeler's ethical line
- [[time-horizon-and-endogenous-explanation]] — scoping a diagnosis correctly, model boundary

## Process Mining & Value Stream Analysis

- [[process-mining-manifesto-principles-and-challenges]] — the founding IEEE manifesto: discovery/conformance/enhancement, event-log maturity ladder, six principles, eleven challenges
- [[xes-standard-for-event-logs]] — the tool-independent event-log interchange standard; the minimum data schema for mining
- [[pm4py-process-mining-in-python]] — the Python library: discovery, alignments, quality metrics on pandas-native data; now incl. the LLM module (four PM-on-LLM paradigms) and the UCM requirements-model extension
- [[value-stream-mapping-method-and-lean-guidelines]] — current/future-state mapping, map anatomy, the seven lean flow guidelines
- [[apqc-process-classification-framework]] — the 13-category process taxonomy: inventory/benchmarking/content layer that precedes mapping and mining; audit completeness check
- [[bpmn-2-0-specification]] — the OMG process-notation standard distilled: three sub-models, the working palette (typed tasks, event matrix, five gateways), token semantics and their traps, compensation model; the 80/20 audit subset named; PCF names → BPMN specifies → VSM measures

## Inventory, MRP & Kanban

- [[eoq-model-and-lot-sizing]] — the Economic Order Quantity model
- [[wagner-whitin-dynamic-lot-sizing]] — optimal lot sizing under varying demand
- [[statistical-inventory-models-newsvendor-base-stock]] — News Vendor and Base Stock models
- [[qr-model-and-lead-time-variability]] — the (Q,r) model, synthesizing lot size and reorder point
- [[mrp-mechanics-netting-lot-sizing-bom-explosion]] — the four-step MRP algorithm
- [[mrp-special-topics-lot-sizing-safety-stock-troubleshooting]] — lot-sizing rules, troubleshooting
- [[mrp-problems-nervousness-and-yield-losses]] — MRP's core problems
- [[capacity-planning-and-shop-floor-control]] — RCCP, CRP, dispatching, I/O control
- [[kanban-mechanics-and-pull-system-variants]] — two-card/one-card kanban, base stock equivalence

## Linear Programming (Deterministic Operations Research)

- [[linear-programming-formulation-and-graphical-solution]] — Wyndor Glass Co., standard form, CPF solutions, the four assumptions
- [[simplex-method-mechanics]] — geometric intuition, tabular form, tie-breaking/degeneracy, the Big M method
- [[duality-theory-and-economic-interpretation]] — the dual problem, shadow prices, complementary slackness
- [[sensitivity-analysis-and-postoptimality]] — allowable ranges, the 100% rule, reading a solver's sensitivity report
- [[transportation-and-assignment-problems]] — special-structure LPs, the transportation simplex method, the assignment problem

## Probabilistic Operations Research

- [[decision-analysis-and-utility-theory]] — decision criteria, Bayes' theorem, EVPI/EVE, decision trees, utility functions
- [[queueing-theory-birth-death-process-and-mms-models]] — the birth-and-death process, balance equations, exact M/M/1 and M/M/s results
- [[discrete-event-simulation-and-random-variate-generation]] — when to simulate, inverse transformation and acceptance-rejection methods
- [[game-theory-two-person-zero-sum-games]] — dominated strategies, minimax/maximin, saddle points, mixed strategies
- [[markov-chains-and-markov-decision-processes]] — the Markovian property, steady-state probabilities, optimal policies via LP

## Combinatorial and Network Optimization

- [[network-optimization-models]] — shortest path, minimum spanning tree, maximum flow, minimum cost flow
- [[integer-programming-and-branch-and-bound]] — binary formulation patterns, the branch-and-bound algorithm
- [[transshipment-problem]] — routing through intermediate transfer points, reformulated as a transportation problem
- [[dynamic-programming-and-the-principle-of-optimality]] — stages, states, backward recursion, the Markovian property
- [[nonlinear-programming-and-kkt-conditions]] — when LP's assumptions break, the Karush-Kuhn-Tucker conditions
- [[metaheuristics-tabu-search-simulated-annealing-genetic-algorithms]] — escaping local optima for problems too large for exact methods

## Inventory, Reliability, and Forecasting

- [[multiechelon-inventory-and-revenue-management]] — supply-chain-wide inventory coordination, dynamic capacity pricing
- [[reliability-theory-series-parallel-and-k-out-of-n-systems]] — series/parallel/k-out-of-n systems, minimal paths and cuts
- [[forecasting-time-series-and-exponential-smoothing]] — constant-level forecasting methods, seasonal adjustment

## Project Management and OR Practice

- [[project-management-with-pert-cpm]] — critical path, slack, uncertain durations, time-cost trade-offs
- [[the-art-of-spreadsheet-modeling]] — Plan-Build-Test-Analyze, changing cells vs. output cells
- [[queueing-system-design-decisions]] — balancing service cost against waiting cost
