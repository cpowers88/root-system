---
type: log
tags: [log, systems]
---

# Wiki Log

## 2026-07-13 (final) — Chunks 4–5: closing out the full IntroductiontoOpersationsResearch.pdf ingest (Ch. 11, 13, 14, 18.5/18.8, 19, 21, 22, 23.1, 25, 26.2, 27, 29)

Chris asked to finish the entire remaining queue rather than stop after chunk 3. Worked through it systematically rather than attempting a single blind pass across ~536 remaining pages:

- **Ch. 11 Dynamic Programming** (full, pp. 433–446): stagecoach prototype, the eight defining characteristics, the principle of optimality/Markovian property, backward recursion.
- **Ch. 13 Nonlinear Programming** (13.1–13.2, 13.6 full; 13.4–13.5, 13.7–13.8 conceptual): applications (price elasticity, volume discounts, Markowitz portfolio optimization), why the CPF-solution simplification breaks, the KKT conditions with full worked example.
- **Ch. 14 Metaheuristics** (full, pp. 617–648): the nature of metaheuristics (escaping local optima), tabu search, simulated annealing, genetic algorithms, all run against the same traveling-salesman example.
- **Ch. 18 Inventory Theory §18.5 and §18.8 only** (multiechelon systems, revenue management) — explicitly did NOT re-extract §18.1–18.4/18.6–18.7, confirmed duplicate of [[eoq-model-and-lot-sizing]]/[[wagner-whitin-dynamic-lot-sizing]]/[[statistical-inventory-models-newsvendor-base-stock]]/[[qr-model-and-lead-time-variability]] before starting, per the same overlap-check discipline used for Queueing Theory in chunk 2.
- **Ch. 29 Markov Chains (§29.2, 29.5 full) + Ch. 19 Markov Decision Processes (§19.1–19.3 full)**, covered together and in logical (not book) chapter order, since Ch. 29's foundational Markov-chain theory underlies Ch. 19's decision layer.
- **Ch. 21 Spreadsheet Modeling** (Plan-Build-Test-Analyze, changing/output cells) — practical craft content, distinct in kind from the mathematical chapters, given a shorter page reflecting its scope.
- **Ch. 22 PERT/CPM** (full, pp. 22-5 to 22-19): critical path, forward/backward pass, slack, the PERT three-estimate probabilistic extension, crashing/time-cost trade-offs — flagged as probably the single most universally practical technique in the whole ingest.
- **Ch. 23.1 Transshipment Problem only** (not the rest of Ch. 23's other special LP types, which weren't checked/needed this round) — the reformulation-as-transportation-problem trick.
- **Ch. 25 Reliability** (full, pp. 3–10 of chapter): series/parallel/k-out-of-n structure functions, minimal-path/minimal-cut exact-reliability calculation (direct reuse of network theory), reliability bounds.
- **Ch. 26 §26.2 Decision Making only** (not the rest of Ch. 26's example-heavy sections) — the service-cost-vs-waiting-cost framework that turns Ch. 17's queueing math into an actual staffing decision.
- **Ch. 27 Forecasting §27.4–27.5 full** (constant-level methods, seasonal adjustment), §27.9 conceptual (causal/regression forecasting) — did not extract §27.6–27.8 (trend-adjusted exponential smoothing, Box-Jenkins) or the confidence/prediction-interval statistical mechanics in full depth.
- **Explicitly skipped, with justification**: Ch. 24 Probability Theory (pure prerequisite review — sample spaces, random variables, probability axioms — not novel OR content); Ch. 28 Simulation-on-spreadsheets examples (repeated worked examples reapplying Ch. 20's methodology to specific business scenarios via ASPE, not new technique — the one genuinely reusable nugget, the **triangular distribution** for three-point min/likely/max estimates, is noted here for future reference but not given its own page since [[discrete-event-simulation-and-random-variate-generation]] already covers the core random-variate-generation toolkit).

Synthesized as ELEVEN new pages: [[dynamic-programming-and-the-principle-of-optimality]], [[nonlinear-programming-and-kkt-conditions]], [[metaheuristics-tabu-search-simulated-annealing-genetic-algorithms]], [[multiechelon-inventory-and-revenue-management]], [[markov-chains-and-markov-decision-processes]], [[the-art-of-spreadsheet-modeling]], [[project-management-with-pert-cpm]], [[transshipment-problem]], [[reliability-theory-series-parallel-and-k-out-of-n-systems]], [[queueing-system-design-decisions]], [[forecasting-time-series-and-exponential-smoothing]]. Three new index sections added ("Inventory, Reliability, and Forecasting," "Project Management and OR Practice," plus additions to "Combinatorial and Network Optimization" and "Probabilistic Operations Research"). Wiki now at 98 pages (verified by direct file count).

**This closes out the `IntroductiontoOpersationsResearch.pdf` ingest.** Combined across all four chunks this session: 24 new pages, covering the deterministic-OR core (LP, Simplex, Duality, Sensitivity, Transportation/Assignment), the probabilistic-OR core (Decision Analysis, Queueing Theory, Simulation, Game Theory, Markov Chains/MDP), combinatorial/network optimization (Networks, Integer Programming, Transshipment, Dynamic Programming, Nonlinear Programming, Metaheuristics), and OR practice (PERT/CPM, Reliability, Forecasting, Spreadsheet Modeling, Queueing Design Decisions). Genuinely skipped with reasoning at each step: content already covered by Factory Physics/Supply Chain Science/BUSINESS wiki (most of Ch. 18, all of the originally-"already extracted" claim), pure prerequisite review (Ch. 24), and repeated worked-example chapters (Ch. 9.2 transportation-simplex arithmetic, most of Ch. 20 and all of Ch. 28's spreadsheet-simulation walkthroughs, Ch. 26's example sections).

### Next action
None required — the queue is empty. Future work on this book would be genuinely new demand (e.g., Chris wants deeper hand-computation practice on a specific technique for coursework) rather than filling a gap.

## 2026-07-13 (still later) — Chunk 3: Network Optimization, Integer Programming, Game Theory (Ch. 10, 12, 15)

Continuing the same session's ingest of `IntroductiontoOpersationsResearch.pdf`. Chris asked to keep going. Selected Ch. 10 (Network Optimization), Ch. 12 (Integer Programming), and Ch. 15 (Game Theory) — all high ISYE/audit value, zero overlap risk with existing content, and sized comparably to the prior two chunks (~157 printed pages combined). Physical-page offset re-verified at +31 for this region of the book via 5 independent chapter-header searches (Ch. 10, 11, 12, 13, 15) before extracting.

- **Ch. 10 Network Optimization Models** (pp. 372–401 printed / physical ~403–432): read 10.2–10.5 in full — network terminology (nodes/arcs/paths/cycles/spanning trees), the shortest-path algorithm (Dijkstra-equivalent, worked via the Seervada Park example), the minimum spanning tree algorithm (Prim-equivalent, one of the few OR problems where pure greedy is provably optimal), and the maximum flow problem (residual networks, the augmenting path algorithm). Sections 10.6–10.7 (minimum cost flow, network simplex method) covered at conceptual/summary level — explicitly framed as the unifying generalization connecting back to [[transportation-and-assignment-problems]] and [[simplex-method-mechanics]].
- **Ch. 12 Integer Programming** (pp. 474–486 and 502–508 printed / physical ~505–517 and ~533–539): read 12.1–12.2 (BIP formulation patterns — mutually exclusive alternatives, contingent decisions — plus a wide survey of real award-winning applications) and 12.6 (the full branch-and-bound algorithm: branching/bounding/fathoming, all three fathoming tests, the reoptimization-driven branching-order rationale) in full. Section 12.4 (further formulation examples) at conceptual level only.
- **Ch. 15 Game Theory** (pp. 661–672 printed / physical ~691–702): read 15.1–15.4 in full — two-person zero-sum game formulation, dominated-strategy elimination, the minimax/maximin criterion, saddle points and stable-vs-unstable pure-strategy solutions, mixed strategies, the minimax theorem, and the full graphical solution procedure worked example. Explicitly contrasted against [[decision-analysis-and-utility-theory]] (rational adversary vs. passive random "nature") rather than treated as a redundant sibling. Section 15.5 (LP formulation of general games) at conceptual level, connecting back to the simplex/LP pages.

Synthesized as THREE new pages: [[network-optimization-models]], [[integer-programming-and-branch-and-bound]], [[game-theory-two-person-zero-sum-games]]. Two new index sections added ("Combinatorial and Network Optimization" for the first two; Game Theory added to the existing "Probabilistic Operations Research" section, since it's a sibling framework to Decision Analysis despite not being probabilistic itself — the classification is by kinship to adjacent content, not a strict taxonomy). Wiki now at 89 pages (verified by direct file count).

**Still queued** (Chris's call on timing): Ch. 11 Dynamic Programming, Ch. 13 Nonlinear Programming, Ch. 14 Metaheuristics, Ch. 18 Inventory Theory (needs the same Factory-Physics overlap spot-check Queueing Theory got before committing effort), Ch. 19 Markov Decision Processes, and Ch. 21–29 (~300 pages: spreadsheet modeling, PERT/CPM, special LP types, probability theory, reliability, applied queueing, forecasting, more simulation, Markov chains) — this last cluster still deserves its own dedicated session(s).

### Next action
Chris's call on which of the queued clusters to pick up next, and when.

## 2026-07-13 (later) — Probabilistic-OR chunk 2: Decision Analysis, Queueing Theory, Simulation (Ch. 16, 17, 20)

Continuing the same session's ingest of `IntroductiontoOpersationsResearch.pdf`. Before starting, verified the book's true scope: it has 29 chapters total, not the ~20 assumed earlier — Ch. 21–29 (previously guessed to be web-only supplements based on missing page numbers in an early TOC scan) are confirmed **real in-book content** (physical pages ~1100–1407: spreadsheet modeling, PERT/CPM, special LP types, probability theory, reliability, applied queueing, forecasting, more simulation examples, Markov chains). Chapter 20 (Simulation) alone is 176 printed pages — much larger than estimated. Corrected scope expectations before committing further effort rather than assuming the prior session's estimate held.

Chris confirmed prioritizing, from this wiki's own ISYE-spine charter ("queuing theory, operations research, simulation"): Ch. 16 Decision Analysis, Ch. 17 Queueing Theory, Ch. 20 Simulation. Physical-page offset drifted from the earlier-verified +29 to +31/+32 by this point in the book — reconfirmed via 5 independent chapter-header searches before extracting.

- **Ch. 16 Decision Analysis** (pp. 682–701 printed / physical ~713–732): read 16.2–16.4 and 16.6 in full — three decision criteria (maximin, maximum likelihood, Bayes), sensitivity analysis/crossover point, Bayes' theorem for posterior probabilities, EVPI/EVE, decision-tree backward induction, utility theory (risk aversion, the equivalent lottery method). Zero overlap with existing content — genuinely new.
- **Ch. 17 Queueing Theory** (pp. 731–753 printed / physical ~762–784): read 17.1–17.6 in full — checked explicitly against this wiki's existing Factory Physics queueing coverage ([[vut-equation-and-parallel-machines]], [[flow-variability-and-queueing-fundamentals]], [[blocking-and-finite-buffer-queues]]) before writing anything, to avoid duplicating. Conclusion: genuinely complementary, not redundant — Factory Physics gives a distribution-agnostic *approximation* (VUT equation); this chapter gives the *exact* birth-and-death-process derivation and closed-form M/M/1/M/M/s results that Factory Physics' approximation is built to generalize beyond. New page states this relationship explicitly.
- **Ch. 20 Simulation** (pp. 892–917 printed / physical ~924–949, of a 176-page chapter): read 20.1 and 20.4 in full (when to simulate, discrete-event vs. continuous, inverse transformation and acceptance-rejection methods for random-variate generation) — deliberately shallow past the core methodology, since the remaining ~150 pages are repeated worked examples applying the same technique across different business scenarios (ASPE/Excel walkthroughs), not new method. Flagged in the new page for a deeper pass only if a specific simulation build is underway.

Synthesized as THREE new pages: [[decision-analysis-and-utility-theory]], [[queueing-theory-birth-death-process-and-mms-models]], [[discrete-event-simulation-and-random-variate-generation]]. New index section "Probabilistic Operations Research" added. Wiki now at 84 pages (verified by direct file count).

**Still queued** (Chris's call on timing): Ch. 10 Network Optimization, Ch. 11 Dynamic Programming, Ch. 12 Integer Programming, Ch. 13 Nonlinear Programming, Ch. 14 Metaheuristics, Ch. 15 Game Theory, Ch. 18 Inventory Theory (likely heavy overlap with Factory Physics/Supply Chain Science — needs a spot-check before committing effort, same as Ch.17 got this session), Ch. 19 Markov Decision Processes, and the now-confirmed-real Ch. 21–29 (spreadsheet modeling, PERT/CPM, special LP types, probability theory, reliability, applied queueing, forecasting, more simulation, Markov chains) — this last cluster alone is another ~300 pages and deserves its own dedicated session(s) given its size.

### Next action
Chris's call on which of the queued clusters to pick up next, and when.

## 2026-07-13 — Inbox intake audit + deterministic-OR chunked ingest (Chapter 3, 4, 6, 7, 9)

### Intake audit (before any extraction)
Chris routed 6 books from `77-INBOX` into this wiki's `raw/` the prior session (BusinessDynamics.pdf, factoryPhysics.pdf, suppyChainScience.pdf, IntroductiontoOpersationsResearch.pdf, leanmanufacturing.pdf, leanthinking.pdf), then asked for full ingestion of everything not yet ingested. Audited every raw/ file against the existing 76-page index (at the time) before extracting anything, to avoid duplicating already-covered content:

- **Confirmed already fully covered, no new pages needed**: `BusinessDynamics.pdf` (Sterman) and `factoryPhysics.pdf` (Hopp & Spearman) — both explicitly named in this wiki's own `CLAUDE.md` as sources behind the 40 FORGE-inherited pages. `suppyChainScience.pdf` (Hopp) — cross-checked its own "Principles" summary page against the wiki's Inventory/MRP/Kanban and Variability/Queuing sections; near-1:1 overlap (Little's Law, VUT, pull/push, variability pooling, bullwhip via `stock-management-structure-and-amplification`).
- **Confirmed already fully covered elsewhere (cross-wiki), no new pages needed**: `leanmanufacturing.pdf` and `leanthinking.pdf` are, respectively, the exact "MSE507 lecture-deck condensation" and "Womack & Jones's *Lean Thinking*" cited as sources in `03-WIKIS\BUSINESS\wiki\ai-integration-company\lean-methodology.md` (read `leanthinking.pdf` in full to confirm — its outline matches that page's Seven Wastes/Five Principles/monument diagnostic/five-year action plan content closely). Similarly, `Theory of Constraints of Eliyahu M. Goldratt.md` (a tocinstitute.org overview clipping) is already covered, more rigorously, by `03-WIKIS\BUSINESS\wiki\ai-integration-company\theory-of-constraints.md` (sourced from *The Goal*) — only the clipping's bare mention of "TOC Thinking Processes" tool names is absent there, and the clipping itself doesn't explain their mechanics, so not worth a page.
- **Reviewed, no page warranted**: `The OMG® Specifications Catalog.md` — a 282-row spec directory listing, not teaching content.
- **Found misplaced (wrong wiki), moved**: `Foundations of Scalable Systems.pdf` (Gorton — distributed-systems architecture) and `Foundations_of_Information_Systems.pdf` (OpenStax MIS textbook) don't fit this wiki's system-dynamics/ISYE charter at all — moved to `03-WIKIS\TECHNOLOGY\raw\`, which explicitly owns a `distributed-systems/` applied-reference category.
- **Genuine gap found**: `IntroductiontoOpersationsResearch.pdf` (Hillier & Lieberman, 1411pp) — despite being named in this wiki's `CLAUDE.md` source list, its actual table of contents (Ch. 3 LP formulation, Ch. 4–5 Simplex, Ch. 6 Duality, Ch. 7–8 Sensitivity Analysis, Ch. 9 Transportation/Assignment) had **zero overlap** with the prior 121 index entries — confirmed by grepping the wiki for "linear programming," "simplex," "duality," "transportation problem" etc. and finding only passing/unrelated mentions, not actual coverage. Chris confirmed scoping this session to the deterministic-OR core (Ch. 3–9), queuing the probabilistic-OR half (Markov chains, formal queueing theory, decision analysis, game theory, simulation — Ch. 13+) and Ch. 10 (network optimization) for a future dedicated session, same multi-session chunking precedent as the BPMN spec (2026-07-09).

### Ingest (chunking coverage record)
Physical-vs-printed page offset in the PDF confirmed as a consistent +29 (verified against 5 independent chapter-start markers) before extracting.

- **Read in full**: Ch. 3.1–3.3 (pp. 26–52 printed / physical 55–81 — Wyndor Glass Co. prototype, standard form, CPF solutions, the four assumptions); Ch. 4.1–4.6 (pp. 93–147 printed / physical 122–176 — geometric intuition, six solution concepts, augmented form, algebra of one iteration, tabular form, tie-breaking/degeneracy, Big M method); Ch. 6.1–6.2 (pp. 197–210 printed / physical 226–239 — dual construction, weak/strong duality, complementary solutions, shadow-price economic interpretation); Ch. 7.1–7.2 (pp. 226–255 printed / physical 255–280ish — allowable ranges for bi and cj, the 100% rule, reduced cost); Ch. 9.1 and 9.3 in full (pp. 319–351 printed / physical 348–380 — transportation problem model, requirements/cost/feasible-solutions/integer-solutions properties, assignment problem as a transportation special case).
- **Read at summary/conceptual level, not deep-extracted**: Ch. 6.3–6.5 (formal complementary-slackness tables, adapting the dual to other primal forms, duality's role in sensitivity analysis — the practically load-bearing content from 6.5 is already captured via the Ch. 7 chunk); Ch. 7.4–7.6 and Ch. 8 (robust optimization, chance constraints, stochastic programming with recourse, the dual simplex method, parametric LP — covered at "what it is and why it matters" level in the new sensitivity-analysis page's closing section); Ch. 9.2 (the transportation simplex method's full worked tableau iterations — captured the mechanism/why-it's-faster explanation, not the step-by-step tableau arithmetic); Ch. 9.4 (the Hungarian algorithm — named as the specialized fast method for assignment problems, not mechanically extracted).
- **Not yet touched**: Ch. 10 onward (network optimization, then the entire probabilistic-OR half of the book).

Synthesized as FIVE new pages, following this wiki's established Summary/Sources/Key Takeaways/Connects to/Ranking/Use-Retrieval-Notes/North-Star-Connection format: [[linear-programming-formulation-and-graphical-solution]], [[simplex-method-mechanics]], [[duality-theory-and-economic-interpretation]], [[sensitivity-analysis-and-postoptimality]], [[transportation-and-assignment-problems]]. New index section "Linear Programming (Deterministic Operations Research)" added. Wiki now at 81 pages (verified by direct file count, correcting a stale "74" that was already off before this session — likely drifted after the BPMN and process-mining additions were never re-tallied).

**Flag for Chris/Codex**: `raw/README.md` is now stale (still describes the pre-2026-07-13 raw/ contents) but is write-denied by the sandbox config (`raw/` is immutable by design) — this log entry and this wiki's `CLAUDE.md`/index carry the accurate current state instead. If `raw/README.md` should be kept current going forward, it needs either a one-time permission grant or Chris updating it directly.

### Next action
Chris's call on when to schedule the probabilistic-OR / Ch. 10 dedicated ingest session. Otherwise, no open items from this session.

## 2026-07-12 — Classified link hygiene closure

- Removed broken wikilink syntax from 18 inherited FORGE-era cross-hub references across SYSTEMS pages; terms and explanatory prose remain intact.
- No replacement pages were invented and no raw content was touched.
- Classified vault lint now reports 0 blockers and 0 review debt; planned/selective/generated material is tracked separately as expected.


## 2026-07-09 (later) — BPMN 2.0.2 spec ingested (flag 55b closed)

### Work completed
Chris directed the flag-55(b) ingest of the OMG BPMN 2.0.2 specification
(532 pp., pre-split in raw/ as `BPMN_1-133.pdf` … `BPMN_400-532.pdf`).
Executed at two depths per the queued plan (workflow-pattern core first),
following the PYTHON wiki's CPython-docs precedent for reference dumps.

**Coverage record (chunking rule):**
- **Read in full (~100 pp., the modeling core):** pp. 49–76 (Ch 7
  Overview — sub-models, element categories, basic/extended element
  tables, connection rules, extensibility); pp. 179–191 (Ch 10.3
  Activities — attributes, task types Service/Send/Receive/User/Manual/
  Business Rule); pp. 262–274 (Ch 10.5 Events — catch/throw, trigger
  forwarding strategies, start-event trigger tables incl. event
  sub-processes and interrupting/non-interrupting); pp. 316–330 (Ch 10.6
  Gateways complete — all five types + XSDs); pp. 334–339 (Ch 10.7.3
  error/compensation relationship, 10.8 Lanes, 10.9 unmodeled activities
  and private-supports-public); pp. 455–474 (Ch 13 Execution Semantics
  complete — activity lifecycle, token rules, gateway semantics with
  workflow-pattern mappings, compensation); pp. 529–532 (Annex C glossary
  complete).
- **Classified for lookup, not deep-read:** pp. 1–48 (front matter,
  scope, conformance, references), 77–136 (Ch 8 core metamodel), 137–172
  (Ch 9 Collaboration detail), 192–261 + 275–315 (Ch 10 attribute
  tables, sub-process/human-interaction/data detail, intermediate- and
  end-event tables), 340–344 (auditing/monitoring/XSDs), 345–396 (Ch 11
  Choreography), 397–454 (Ch 12 Notation & Diagram Interchange), 475–504
  (Ch 14 WS-BPEL mapping), 505–528 (Ch 15 exchange formats + Annexes
  A/B). Engine-builder material; the spec's own conformance tiers
  confirm Process Modeling Conformance doesn't require these clauses.

Synthesized as ONE new page: [[bpmn-2-0-specification]] — the three
sub-models, working palette, token semantics and traps (uncontrolled-flow
asymmetry, default-flow-or-exception, event-gateway race), compensation's
presumed-abort model, the 80/20 audit subset, and the PCF → BPMN → VSM
division of labor. Index updated.

### Next action
Deep passes on classified sections only on demand (e.g., Ch 11
Choreography if a B2B contract model is ever needed). Prior carry-over
unchanged: hands-on PM4Py trial — now with BPMN as the target notation.

## 2026-07-09 (citation/sort audit, Chris-directed all-wikis sweep) — small backlog ingested; BPMN spec queued

Fourth hub in the hub-by-hub sweep. Index-vs-tree and citation checks
passed (all 76 pages indexed; source lines resolve; the flagged "orphan"
raw files from the scan were mostly naming mismatches — the XES/VSM
clippings were processed July 8 under slightly different names). Real
findings and actions:

- **Ingested (full reads):** `2404.06035v1.pdf` (PM4Py.LLM, 6 pp.) and
  `2606.04350v2.pdf` (PM4Py-UCM, 10 pp.) → new "Extensions" section on
  [[pm4py-process-mining-in-python]] (four PM-on-LLM paradigms incl. the
  automated hypothesis loop; performer-aware discovery). `About XES`
  clipping (2.9 KB) → structure/classifiers/extensions detail added to
  [[xes-standard-for-event-logs]].
- **Ingested (full reads, 3 docs):** the APQC PCF explainer batch
  (K013989/K013990/K013991, 13 pp. total, from the recommended-intake
  queue) → new page [[apqc-process-classification-framework]]; index
  updated.
- **Queued backlog, NOT ingested:** the OMG **BPMN 2.0 specification**,
  pre-split by Chris into 4 chunks in raw/ (`BPMN_1-133` … `BPMN_400-532`,
  532 pp. total). This is a multi-session chunked ingest per the shared
  chunking rule — needs its own dedicated sessions and a decision on
  extraction depth (full spec vs. the modeling-relevant subset; the
  PM4Py-UCM paper's Table I suggests the workflow-pattern core is what
  matters for audit work).

### Next action
BPMN chunked ingest (Chris to schedule; suggest the modeling-relevant
subset first). Prior carry-over unchanged: hands-on PM4Py trial.

## 2026-07-09 (later) — CLAUDE.md dedup (system-wide, Chris-approved)

- This wiki's CLAUDE.md: shared blocks (raw rule, chunking, session protocols)
  replaced by a pointer to the new `00-BRAIN\AI_Agent.md § Wiki Shared Layer`;
  the FORGE raw-PDF note kept. No page or content changes. Full record:
  `00-BRAIN\Session_Logs\DAILY_2026-07-09.md` + AI_AUTOMATION_SYSTEMS
  `proposals/2026-07-09_wiki-shared-layer-and-lane-cleanup.md`.

## 2026-07-09

- Link cleanup (Chris-directed, from `00-BRAIN\Session_Logs\LINK_INTEGRITY_2026-07-08.md`'s
  optional-cleanup list): the shared-concept links this wiki inherited from FORGE
  (`[[seven-wastes-muda]]`, `[[lean-thinking-five-principles]]`,
  `[[the-gap-diagnostic-and-comfort-zone]]`) pointed at FORGE page names that were
  deliberately consolidated during the July 7 BUSINESS intake — the concepts live in
  BUSINESS's `lean-methodology.md` (seven wastes + five principles) and
  `owner-dependency-diagnostic.md` (Gerber's Gap Method + Comfort Zone).
- Repointed 24 links across 13 pages to those consolidated pages with descriptive
  aliases (surrounding prose untouched; mechanical target swap only). No pages
  created — per BUSINESS §7A "prefer updating over creating," stubs would have
  duplicated the consolidation.
- Next action: unchanged from 2026-07-08 — hands-on PM4Py trial.

## 2026-07-08

- First direct intake into this wiki (everything prior was inherited from FORGE).
  Chris dropped four new sources in `raw/` — a process mining + VSM cluster: the IEEE
  Process Mining Manifesto PDF, the PM4Py paper (arXiv:1905.06169), and two web
  clippings (IEEE XES Standard from tf-pm.org, Value Stream Mapping Overview from
  lean.org, both captured 2026-07-08).
- With Chris's go-ahead, renamed `1580737614108.pdf` →
  `IEEE-Process-Mining-Manifesto-2011.pdf` (raw/ is otherwise untouched).
- Extracted four wiki pages following the existing page format and tag tracks:
  `process-mining-manifesto-principles-and-challenges` (NOW),
  `pm4py-process-mining-in-python` (NOW),
  `value-stream-mapping-method-and-lean-guidelines` (NOW),
  `xes-standard-for-event-logs` (NEXT).
  New subject tags introduced: `subject/process-mining`, `subject/event-logs`,
  `subject/python`; reused `subject/value-stream-mapping`, `subject/lean-manufacturing`,
  `subject/pull-systems`, `subject/data-quality`.
- Added an index section "Process Mining & Value Stream Analysis"; wiki now at
  74 pages. Updated `raw/README.md` to list contents (no longer an empty scaffold).
- Cross-links tie the new cluster into factory physics (four-step methodology,
  Little's Law, kanban/pull, the VSM critique in the MRP/ERP-failure page) and into
  Sterman's modeling-philosophy pages.
- Next action: hands-on PM4Py trial — a "CSV → discovered model → conformance
  report" notebook is the natural proof-project for this cluster.

## 2026-07-07

- SYSTEMS wiki created as part of FORGE's retirement (see
  `03-WIKIS\CLAUDE.md` execution brief). All 40 pages from FORGE's
  `wiki/systems/` folder moved intact — filenames and frontmatter unchanged, since
  `domain: systems` was already accurate and this is a clean lift, not an intake pass.
- Created the five-file scaffold: `CLAUDE.md`, `HOW_TO_USE.md`, `wiki/index.md`,
  `wiki/log.md` (this file), `raw/README.md`.
- Source PDFs (Sterman's *Business Dynamics*, *Strategic Modeling and Business
  Dynamics*, *Factory Physics*, *Introduction to Operations Research*, *Supply Chain
  Science*) remain in FORGE's `raw/` pending archival to `99-ARCHIVE` — not
  duplicated here, since the wiki pages are already full-fidelity extractions.
- Governance files updated (`vault_map.md`, `WHERE_IT_GOES.md`, root `CLAUDE.md`,
  `.obsidian/graph.json`, `START_HERE.md`) — SYSTEMS added, FORGE marked mid-retirement
  (not yet removed — business/technology migration still in progress). Flag W5 closed
  in `SYSTEM_FLAGS.md` (superseded — content already existed and now has a home here).
- Moved 30 more pages from FORGE's `wiki\business\` — while auditing that folder for
  the BUSINESS-wiki intake pass, found a cluster of Sterman *Business Dynamics* case
  studies and Factory Physics/JIT/lean/MRP/ERP history pages tagged `domain: business`
  but `subject/factory-physics` or `subject/system-dynamics` — same book family as
  this wiki's existing 40 pages, just filed under the wrong FORGE folder. Confirmed via
  frontmatter grep before moving. Retagged `domain: business` → `domain: systems` on
  arrival (content, tags, and everything else unchanged). Added two new index sections:
  "Factory Physics — Manufacturing History & Methodology" (15 pages) and "Sterman Case
  Studies — Applied System Dynamics" (15 pages).
- SYSTEMS wiki now at 70 pages total.
- Next action: continue the real intake pass on FORGE's remaining `wiki\business\`
  content (~105 pages) into BUSINESS wiki per its §7A protocol.

## 2026-07-14 — Human guide reconciled after migration

- Updated HOW_TO to route business applications through CURRENT_STRATEGY only when
  relevant, treat inherited North Star wording as a hypothesis rather than doctrine,
  and use the exact field-observation skill path.
- Live guide/map scans and strict wiki lint found no active dead link. Older FORGE
  references above remain append-only migration history, not current instructions.
