---
type: report
timeline: log
status: awaiting-review
tags: [castle, governance, codex, slice-a2]
---

# CASTLE Slice A2 — System Review and Core-Map Proposal

**Date:** July 19, 2026
**Prepared by:** Codex using Operator and Technology Engineer modes
**Decision owner:** Chris
**Implementation status:** Review only; no A2 target changed

## Executive Verdict

**Slice A2 remains the highest-value next system step.** A1 now routes a cold session correctly, but the four core maps it opens still carry copied current state, calendar-shaped instructions, stale capability claims, and one source-registration rule that contradicts `OPERATIONS.md`.

Keep the four-file boundary:

1. `00-BRAIN\CASTLE\wiki\north-star-roadmap.md`
2. `00-BRAIN\CASTLE\wiki\source-map.md`
3. `00-BRAIN\CASTLE\wiki\skill-map.md`
4. `00-BRAIN\CASTLE\wiki\current-position.md`

Modify the earlier A2 plan in one place: `skill-map.md` needs a compact active-capability register, not only removal of two scheduling phrases. `OPERATIONS.md` Rule 4 now requires every active capability to name its owner, enabled outcome, next real rep, proof, and likely value path. The current map does not.

Do not pull Slice B strategy labeling or Slice C `NOW.md` compression into A2.

## CASTLE Decision

- **Why now:** A1 made these maps the trusted next click. Correct entrances pointing into stale maps increase, rather than reduce, drift.
- **Owner:** CASTLE owns sequence and proof status. Domain wikis and projects own detailed truth. Chris approves the structural rewrite and archive batch.
- **Next action:** Claude independently challenges this scope and proposed wording; Codex then prepares the exact four-file replacements for Chris's approval.
- **Proof:** reference maps contain no copied daily state; active capabilities carry the five required fields; shared statuses agree with owner files; roadmap evidence has one registration rule; health gates pass.
- **Return:** after approved implementation, update the CASTLE log and the `.ROOT` row in `NOW.md` only if its live status materially changes.

## Live Findings

| Target | Live evidence | Why it matters | Verdict |
|---|---|---|---|
| `north-star-roadmap.md` | Lines 74–97 copy dated July work, sprint state, daily order, and weekly blocks. `NOW.md` already has newer pause/sequence detail. | A `timeline: reference` roadmap is acting as a second dashboard and has already drifted. | Rewrite the volatile section as standing priorities plus owner pointers. |
| `north-star-roadmap.md` | Line 49 says every ISYE course becomes a sellable service; line 66 fixes Flask/APIs/automation into 2028; lines 101–102 make every page answer a skill-first question. | This narrows transferable learning and hardens a replaceable tool path. | Replace with capability/application/value language and the CASTLE decision question. |
| `source-map.md` | Header says only roadmap-relevant sources register; lines 68–72 require every external source to register before influencing any page. | The file contradicts itself and duplicates domain intake authority. | One roadmap-evidence gate; all other evidence remains with its owner. |
| `source-map.md` | Lines 29–45 copy page counts, learner positions, ingestion counts, and processing status. | Reference evidence map is carrying volatile owner state. | Keep claims and pointers; remove counts and processing/frontier state. |
| `source-map.md` | Line 9 says Tier 1–2 sources determine the roadmap. | Evidence informs confidence; it does not override North Star authority, proof, constraints, or Chris's decision. | Reword the tier rule as an evidence-quality guide. |
| `skill-map.md` | Lines 34–45 require scheduled/calendar blocks; line 116 requires no zero-commit days. | Direct conflict with Chris-owned timing and declared capacity. | Replace with a capacity-sized next-rep output. |
| `skill-map.md` | Data visualization is `not-started` despite the verified July 16 rep. Python still says CS50P PS2. Agentic delivery is `working` because CASTLE exists, without measured delivery proof. | Shared proof state is stale or overstated. | Data visualization → building; Python → Stage 3 building; agentic delivery → building pending measured use and explain-back. |
| `skill-map.md` | Active rows omit owner, next rep, enabled outcome, and likely value path. | The map still fails `OPERATIONS.md` Rule 4 after superficial phrase fixes. | Add one compact active-capability register; keep later capabilities as horizon, not fake active work. |
| `current-position.md` | Lines 24–35 preserve minute-level drill state and reconciliation history; lines 52–64 copy page/topic counts and lane detail. | A monthly baseline becomes stale almost immediately and competes with `NOW.md` and owner files. | Retain monthly proof state and material constraints; point to live owners for detail. |
| `current-position.md` | Lines 88–91 duplicate `SKILL_GAP_ANALYSIS.md`'s monthly question and turn it into daily tracker scheduling. | Duplicate authority can reintroduce the capacity behavior A0/A1 removed. | Point to the owner and record only the July weak-link result and proof frontier. |

## Proposed A2 Target State

### 1. `north-star-roadmap.md` — durable pathway, not current dashboard

Keep:

- October 8, 2031 hard measurement date.
- Degree and $500K–$1M floor.
- Advisor-Builder explicitly labeled as the current vehicle being tested.
- Three coordinated tracks and compounding-asset concept.
- Phase-map and owner links.

Make these exact wording changes:

```markdown
1. **School — the spine.** Complete the KSU BS in Industrial & Systems Engineering. Review each course for transferable capability, real application, and possible economic value; no course is required to become a service.
```

Replace the dated `What Matters RIGHT NOW` section with:

```markdown
## Standing Priority Frame

1. Protect fixed school deadlines and commitments.
2. Build practical workflow, technology, data, automation, AI, integration, security, and operating capability through real use.
3. Prefer work that produces verified capability, useful systems, measurable value, income evidence, or reusable assets.
4. Treat markets, offers, vendors, tools, and revenue models as replaceable strategies.

Current action lives in `.ROOT\NOW.md`. Monthly baseline and proof state live in [[current-position]]. Business milestones and assumptions live in `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md`.
```

Replace the universal skill-first question with:

```markdown
> What is the highest-value next action; who owns it; what proof closes it; and where does the result return?
```

Change the 2028 line from named tools to an outcome category:

```text
2028      Phase 7     Repeatable workflow-system delivery and integration evidence under the strategy then in force
```

Change the evidence guardrail to:

```markdown
- [[source-map]] registers evidence that materially shapes a roadmap choice, strategy assumption, constraint, or gate; domain evidence remains with its owner.
```

### 2. `source-map.md` — roadmap evidence register only

Rebuild it around four short sections:

1. **Purpose:** evidence enters this map only when it materially affects a roadmap choice, strategy assumption, constraint, or gate.
2. **Authority and confidence:** North Star and approved contracts govern; source quality changes confidence, not human authority.
3. **Roadmap-shaping register:** keep stable pointers and the specific claim each supports; remove page counts, file counts, learner positions, ingestion queues, and generic domain-source inventories.
4. **Routing rule:** ordinary research stays in its domain hub; material external change follows evidence owner → Watchtower → CASTLE gate.

Use one registration rule:

```markdown
## Registration Gate

Register evidence here only when it materially changes or supports a roadmap choice, strategy assumption, constraint, or gate. Record the owner, claim affected, confidence/tier when useful, and review trigger. All other sources remain in their domain evidence home and may inform domain work without a CASTLE row.
```

Replace “Tier 1–2 sources determine the roadmap” with:

```markdown
Prefer primary and authoritative evidence for consequential claims. Lower-confidence sources may raise questions or suggest tests; no source silently overrides the North Star, owner truth, measured outcomes, or Chris's decision.
```

### 3. `skill-map.md` — capability horizon plus active proof register

Keep:

- Eight capability categories.
- `not-started → building → working → proven` states.
- The proof ladder separating personal capability from asset maturity.
- Creation-on-activation rule and opportunity gate.

Replace the scheduling block with:

```markdown
## Working Output

When Chris asks what to work on, return the owning system, one capacity-sized next rep, the proof artifact, and the result's return path. Chris chooses timing and work order outside fixed commitments.
```

Add a compact active-capability register with these fields:

| Capability | State | Owner | Next real rep | Proof that moves state | Enabled outcome / likely value path |
|---|---|---|---|---|---|
| Field observation | building | BUSINESS method + `05-BUSINESS\02-Field Notes` | one approved live observation | recognized actual-state record; two tested live sessions for working | workflow diagnosis; academic/operational/commercial |
| Systems/flow thinking | building | SYSTEMS wiki + coursework | apply one flow/constraint model to a real workflow | model improves a decision or finding | engineering, operations, employability |
| Python | building — Stage 3 | PYTHON current-position | close the next owner-defined Stage 3 rep | independent build, explain-back, and debug gate | school, automation, software |
| SQL/SQLite | building — July weak link | tracker + PYTHON/technology owners | use verified real tracker data | correct schema/query result used in the real workflow | school, data systems, employability |
| Git/GitHub discipline | building | active repositories | complete the next approved repository workflow | understandable history and successful recovery/review | reliable delivery and collaboration |
| Data visualization | building — first rep verified | Technology Strategy + live proof vehicle | next justified decision-facing visual | another person can trace the calculation and act | decision support; operational/commercial |
| Agentic delivery | building | approved projects + AI system | complete and measure one real assisted delivery | quality-reviewed output, Chris explain-back, time/quality evidence | delivery leverage and reusable methods |
| Technology landscape | building | Technology Strategy + TECHNOLOGY wiki | one problem-led category/recommendation rep | correct category, ladder rung, constraints, and rejection logic | vendor-neutral integration judgment |
| Recommendation Ladder | building | Technology Strategy | apply it to one observed problem | keep/simplify/buy/integrate/build decision with evidence | cost avoidance and sound architecture |
| Technical writing and communication | building | TCOM/EDUCATION + real artifacts | one audience-specific finding or handoff | reader can decide or operate without hidden context | school, delivery, employability, commercial |

Later capabilities remain in the eight-category horizon but do not receive active next reps until evidence activates them. Remove `no zero-commit days` entirely.

### 4. `current-position.md` — monthly baseline and proof frontier

Keep only information that belongs in a monthly CASTLE baseline:

- fixed destination and material constraints;
- high-level school/capability/business proof state;
- current weak-link result;
- stable advantages and open proof frontiers;
- pointers to live owners and the next monthly review.

Use owner-aware status language:

- Physics Stage 4 is the next active unit; temporary sprint pauses belong in `NOW.md`.
- Python Stage 3 is building; detailed drill position belongs in PYTHON current-position.
- SQL is building; tracker V1 shipped, real-data operating proof remains open.
- Data visualization is building; first rep verified, decision-use proof remains open.
- Field observation is building; desk practice exists, live observation proof remains open.
- Technology landscape is building; category knowledge exists, integration/operation proof remains open.
- Advisor-Builder remains an active hypothesis with zero clients; assumptions and milestones belong to `CURRENT_STRATEGY.md`.
- Financial continuity is a material constraint; live lane evidence and approvals belong to REVENUE_LAB and `NOW.md`.

Remove:

- minute-level Python drill position;
- reconciliation history inside status bullets;
- business-wiki/page counts and scanner-topic counts;
- copied lane mechanics;
- the duplicated monthly weak-link question and daily-practice prescription.

End with:

```markdown
## Owner Pointers

- Current action and temporary pauses: `.ROOT\NOW.md`
- School learner truth: PYTHON and PHYSICS `wiki\current-position.md`
- Monthly weak-link decision: `01-NORTH_STAR\SKILL_GAP_ANALYSIS.md`
- Technology frontier: `02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md`
- Business strategy: `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md`
- Revenue evidence: `03-WIKIS\REVENUE_LAB\wiki\`

Next monthly reconciliation: August 1, 2026.
```

## Explicit Deferrals

- **Slice B:** `phase-map.md`, phases 1–4, strategy-hypothesis labels, price/conversion language, fixed course-to-service mappings, and template value/Return-Packet updates.
- **Slice C — July 26:** compress `NOW.md` after the bootcamp transition; do not restructure it twice during the sprint.
- **August 1 weak-link review:** consider changing `SKILL_GAP_ANALYSIS.md`'s “smallest daily practice” wording to “smallest recurring real rep sized to declared capacity.” Do not silently edit the owner during A2.
- Historical logs and source summaries remain untouched.
- No Phase 5–10 pages, new dashboards, new skill pages, or new tracking layers.

## Acceptance Tests

1. The four A2 predecessors are archived exactly after Chris approves the archive batch.
2. `north-star-roadmap.md` contains no dated current-state section or daily/weekly schedule instruction.
3. No active CASTLE instruction says every course becomes a service, schedules Chris's capacity, or requires zero-commit days.
4. `source-map.md` has exactly one registration rule and it matches `OPERATIONS.md` Rule 3.
5. No copied page/file counts or processing queues remain in the four maps.
6. Every active capability names owner, next rep, proof, enabled outcome, and likely value path.
7. Shared statuses agree with owner truth: Python Stage 3 building; Physics Stage 4 next active unit; data visualization building; SQL building; field observation building.
8. Agentic-delivery status is evidence-calibrated rather than inferred from CASTLE's existence.
9. `current-position.md` remains useful if read any day in the month; temporary detail resolves through owner pointers.
10. Slice B and C content remains untouched.
11. Frontmatter audit reports zero new debt; canonical root health returns PASS WITH DEBT with zero blockers/new debt.
12. July 26 sweep rechecks reference-page drift and the active-capability register; August 1 monthly review updates weak-link truth.

## Questions for Claude's Independent Challenge

1. Is the four-file A2 boundary still the smallest coherent repair after A1?
2. Is the active-capability register required by `OPERATIONS.md` Rule 4, or can the same contract be met more compactly without losing owner/next/proof/value information?
3. Does the roadmap remain concrete enough for Chris while avoiding tool, market, and offer lock-in?
4. Which source-map rows truly shape roadmap decisions, and which should return to domain-only ownership?
5. Does any proposed wording weaken the fixed October 8, 2031 destination, degree commitment, technology/workflow priority, or financial-freedom goal?
6. Should `SKILL_GAP_ANALYSIS.md` join A2, or is the August 1 owner review the safer boundary?
7. Are any controlling core-map conflicts missing that cannot safely wait for Slice B or C?

## Requested Claude Return

Return:

1. Per-file `KEEP`, `MODIFY`, or `REJECT` verdict with live evidence.
2. A verdict on the active-capability register and its minimum useful fields.
3. Exact wording modifications, not broad preferences.
4. Any proposed scope addition paired with why it cannot wait for B, C, or August 1.
5. A final implementation order and deterministic validation commands.

## Return Packet

1. **Current state:** A0 and A1 are committed and the worktree was clean at this review's start. A2 has not been implemented.
2. **Open question:** whether the proposed skill-map register is the minimum coherent contract repair and whether any source rows should remain in CASTLE.
3. **Next exact action:** Claude challenges this report against the live files; Chris reviews the verdict before any A2 archive or edit.
4. **Fragile detail:** do not let strategy-label work, sprint-era `NOW.md` compression, or owner-file scheduling language expand A2 without an explicit reason and approval.

---

*Prepared after a post-A1 CASTLE run. Chris retains final authority over scope, wording, archives, and implementation.*
