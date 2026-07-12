---
type: log
tags: [log, systems]
---

# Wiki Log

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
