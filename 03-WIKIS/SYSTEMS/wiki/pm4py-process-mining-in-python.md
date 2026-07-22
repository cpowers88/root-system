---
domain: systems
type: reference
tags: [subject/process-mining, subject/event-logs, subject/python]
timeline: now
status: wiki-only
source_role: primary
use_cases: [data-workflow, audit, systems-analysis]
---

# PM4Py: Process Mining in Python

**Summary**: PM4Py (Berti, van Zelst, van der Aalst — RWTH Aachen / Fraunhofer FIT, 2019) is the open-source Python process mining library, built to close the gap the GUI tools leave: commercial tools (Disco, Celonis) allow little algorithmic customization, and GUI-bound academic tools (ProM, Apromore) can't run large-scale scripted experiments. PM4Py integrates directly with pandas/numpy/scipy/scikit-learn — which makes process mining a Python-native workflow rather than a separate application, and puts the whole discipline inside the existing Python learning track.

**Sources**: 1905.06169v1.pdf (Berti, van Zelst, van der Aalst, "Process Mining for Python (PM4Py): Bridging the Gap Between Process- and Data Science," arXiv:1905.06169, May 2019) · 2404.06035v1.pdf (Berti, "PM4Py.LLM: a Comprehensive Module for Implementing PM on LLMs," arXiv:2404.06035, Apr 2024, 6 pp.) · 2606.04350v2.pdf (Amyot, "Towards Process Mining Use Case Map Models with PM4Py-UCM," arXiv:2606.04350, Jun 2026, 10 pp.) — all in `raw/`.

**Last updated**: 2026-07-09

---

## Why the Library Exists

The tool landscape circa 2019: commercial process mining tools support discovery well but barely allow custom algorithms; ProM and Apromore are open-source and richer (conformance, enhancement) but GUI-driven, which blocks large-scale scripted experimentation; RapidProM scripts experiments but doesn't allow easy algorithmic customization. PM4Py's answer is a plain Python library — `pip install pm4py` — chosen specifically because the data science ecosystem (pandas, numpy, scipy, scikit-learn, tensorflow/keras) already lives in Python. Design goals: easy extension, algorithmic customization, large-scale experiments, shared ecosystem, rich documentation, rigorous testing.

## Architecture

Three strictly separated package families:

- **`pm4py.objects`** — data structures plus import/export and conversion utilities: **event logs** (list of traces; each trace a list of key-value events), **event streams** (flat list of events not yet grouped into cases), **pandas DataFrames** (recommended for large data), plus Petri nets, DFGs, heuristic nets, process trees, transition systems.
- **`pm4py.algo`** — the algorithms: discovery, conformance, enhancement, evaluation.
- **`pm4py.visualization`** — all rendering, kept out of the algorithm code.

Access is through **factory methods**: one entry point per algorithm taking standardized inputs (log + parameters) and a `variant` name (e.g. Alpha Miner `classic` vs. `plus`) — new variants extend an algorithm without breaking callers.

## What It Covers (as of the paper, v1.1)

- **Discovery**: Alpha(+) Miner, Inductive Miner (IMDF).
- **Conformance**: token-based replay and **alignments** (trace-by-trace mapping of log moves vs. model moves; `>>` marks a move present on one side only).
- **Evaluation**: fitness, precision, generalization, simplicity — the manifesto's four quality dimensions ([[process-mining-manifesto-principles-and-challenges]], C6), directly computable.
- **Filtering**: by time-frame, case performance, trace endpoints, variants, attributes, paths.
- **Case management & graphs**: variant/case statistics, case-duration and events-over-time plots.
- **Social network analysis**: handover-of-work, working-together, subcontracting networks.
- **Visualization** via GraphViz (nets, DFGs, trees), NetworkX, Pyvis (interactive social networks).

The canonical five-liner: import an XES log, `alpha_miner.apply(log)` to get a Petri net with initial/final markings, then a GraphViz factory to view it. Conformance is symmetric: `alignments.apply(log, net, im, fm)` returns per-trace alignments.

## Maturity Signals

Released 1.0 in Dec 2018; used by 200 students at RWTH Aachen; XES-certified with maximum score ([[xes-standard-for-event-logs]]); bupaR (the R process mining library) delegates alignments and Inductive Miner to PM4Py; issues on GitHub, docs on the project site. (Note: the paper describes 2019 — the library has grown substantially since; treat the feature list as a floor, and check current docs before relying on API details like the factory-method idiom, which later versions simplified.)

## Extensions: LLMs and Requirements Models (added 2026-07-09)

**PM4Py.LLM (Berti, 2024).** The library ships an `pm4py.llm` module
implementing four paradigms for process mining with LLMs — directly relevant
to how an AI-integration audit would industrialize this pipeline:

1. **Direct provision of insights** — 13 textual abstraction methods
   (`abstract_dfg`, `abstract_variants`, `abstract_case`, Petri nets, DECLARE,
   log skeletons, object-centric logs…) plus visual abstractions of 21
   visualization types for vision models. Limits named in the paper: context
   window, privacy (event data goes to the LLM), hallucination.
2. **Natural language → SQL** — the LLM writes DuckDB queries against the
   pandas event-log dataframe; mitigates privacy/hallucination but only
   answers quantitative questions.
3. **Code generation** — LLM writes pm4py Python against the documented API
   (a security surface the paper flags: generated code is executed).
4. **Automatic hypothesis formulation** — LLM proposes hypotheses over the
   log plus a SQL statement to verify each; refine on failure. This is the
   audit loop (observe → hypothesize → verify) automated.

**PM4Py-UCM (Amyot, 2026).** Open-source extension making Use Case Maps
(ITU-T URN standard) a first-class discovery output: event log → inductive
miner → process tree → hierarchical UCM with performer bindings (roles or
individuals from the log mapped onto activities), round-tripping to jUCMNav.
Two audit-relevant ideas even if UCM is never used: (a) **performer-aware
views answer "who does what, and when"** — the paper's example distinguishes
two same-role employees who specialize in different activities; (b)
**decomposition tuned for understandability** (max elements per map) rather
than fitness — the mined 88-node claims-process model was unreadable until
split into 7 nested maps. Notably, the tool was built with Claude Code
(Opus 4.7) per the acknowledgments.

## Key Takeaways

- Process mining is available as an ordinary Python dependency, interoperable with pandas — no new application to learn, no vendor license.
- The objects/algorithms/visualizations separation and factory-method pattern are themselves a decent case study in library architecture for the Python track.
- Discovery → conformance → evaluation in a few lines each: import log, mine model, align, score fitness/precision/generalization/simplicity.
- A client's CSV export → pandas DataFrame → PM4Py is the entire pipeline from raw system data to a discovered process map.

## Connects to

- [[process-mining-manifesto-principles-and-challenges]] — PM4Py is the practical implementation of the manifesto's three types and four quality dimensions; van der Aalst is an author of both.
- [[xes-standard-for-event-logs]] — PM4Py's native log format and its certification benchmark.
- [[factory-physics-four-step-improvement-methodology]] — a mined model with timing enhancement is the data-driven input to the diagnose step.
- [[internal-benchmarking-and-hal-case-study]] — Factory Physics benchmarks a line against its own best-case laws; a discovered model with timestamps supplies the actual CTs and flows those benchmarks need.

## Ranking

| Category | Score | Reason |
|---|---:|---|
| North Star relevance | 5 | The concrete tool that turns the process mining audit offer from concept into a deliverable |
| Current usefulness | 4 | `pip install pm4py` + any client CSV with case/activity/timestamp = a discovered process map this week |
| KSU support | 3 | Reinforces Python skills; adjacent to ISYE simulation content, not required by it |
| Tech-stack relevance | 5 | Pure Python, pandas-native — sits exactly on the existing learning track |
| Business audit value | 5 | Alignments give a per-case, showable record of where reality deviates from the intended process |
| Data/workflow value | 5 | Defines the working pipeline: system export → DataFrame → model → conformance → visuals |
| Reading urgency | 3 | Read alongside the manifesto; hands-on trial matters more than re-reading the paper |

**Overall priority**: NOW

## Use / Retrieval Notes

**Best use**:
Tooling reference — standing up a process-discovery or conformance analysis on real event data in Python; also an architecture example (factories, object/algo/viz separation) for the Python track.

**Use when**:
An event log (or anything convertible to case/activity/timestamp rows in pandas) exists and the question is "what does this process actually look like, and where does it deviate or stall?"

**Do not use when**:
The data can't support mining yet (score it against the manifesto's maturity ladder first), or the paper's 2019 API details matter — check current PM4Py docs; the library has evolved past the factory-method idiom described here.

**Fast retrieval query**:
`subject/process-mining` + `subject/python` — or search "PM4Py" / "alpha miner" / "inductive miner" / "alignments" / "token replay"

## North Star Connection

- How this applies to the audit business: this is the audit tool with near-zero marginal cost — a client's ticketing or ERP export becomes a discovered process map, a bottleneck-annotated model, and a conformance report using only Python skills already being built. It converts the Python learning track and the audit offer into the same activity.
- Track relevance: Python — strong (real library, real data); Systems — strong (operationalizes the whole process-mining cluster).
- Possible future Second Brain use: Yes — a worked "CSV → discovered model → conformance report" notebook template is an obvious proof-project candidate.
