---
type: report
tags: [next, governance, instruction-design, execution-brief]
created: 2026-07-12
status: approved-for-execution
---

# .ROOT User Operating Instructions — Execution Brief

## Objective

Build a complete human operating layer for `.ROOT` that lets Chris answer, in under one minute:

1. What should I do now?
2. Which system owns this question or file?
3. How do I work inside that system?
4. How does work become retained knowledge, proof, or client value?
5. How does the system learn from use without drifting or expanding its skeleton?

The instruction design must reduce friction, preserve one source of truth, and keep School -> Tech -> Solo Business in order.

## Approved Architecture

Use a three-level instruction stack. Do not create a new top-level folder or a second master manual.

| Level | File class | Job |
|---|---|---|
| 1 — Master use | `.ROOT\START_HERE.md` | Human control surface: start, route, operate, close, evolve |
| 2 — Placement | `00-BRAIN\WHERE_IT_GOES.md` | Sole authority for file location, naming, tags, and promotion destinations |
| 3 — Local use | Each realm's `HOW_TO_USE.md` / README | Domain-specific start page, work loop, outputs, boundaries, and close |

AI governance remains separate:

- `00-BRAIN\AGENT.md` — universal AI OS.
- Lane files — engine behavior.
- Local `CLAUDE.md` / `CODEX.md` — realm-specific AI rules.

Human instructions describe how Chris uses the system. AI instructions describe what an engine may do. Do not blend them into one large prompt.

## Canonical Human Operating Doctrine

This doctrine should be expressed in `START_HERE.md` in simple language.

### The Five-Move Operating Loop

```text
ORIENT -> ROUTE -> WORK -> PROVE/PACKAGE -> CLOSE
```

1. **Orient:** Open `NOW.md`. Confirm the one priority and active track.
2. **Route:** Classify the work using the routing table below. One owner system.
3. **Work:** Open that realm's `HOW_TO_USE.md`, then its canonical current page.
4. **Prove or package:** Record evidence of learning/use. Promote reusable results only after proof.
5. **Close:** Record what moved and the next exact action; refresh current-position/NOW only when reality changed.

### Question Router

| If Chris is asking... | Owner |
|---|---|
| What matters today? | `.ROOT\NOW.md` |
| Where am I going and what phase/skill comes next? | `00-BRAIN\CASTLE` |
| What controls the mission or target? | `01-NORTH_STAR` |
| Where does this file belong? | `00-BRAIN\WHERE_IT_GOES.md` |
| What should I learn or retrieve in a domain? | Matching `03-WIKIS` hub |
| Where are official course files? | `02-LIBRARY\00-SCHOOL` |
| Where does an active build live? | `02-LIBRARY\.PROJECTS` plus local/GitHub code |
| Where does business strategy or a blank master live? | `03-WIKIS\BUSINESS` |
| Where does a filled client/business artifact live? | `05-BUSINESS` |
| Where does a reusable proven client capability live? | `05-BUSINESS\06-Capability Library` |
| Where does an unsorted capture go? | `77-INBOX` |
| Where does private reflection go? | `88-JOURNAL` — AI never reads |

### The Knowledge-to-Value Pipeline

```text
raw source -> domain wiki -> CASTLE relevance decision -> real work/proof
           -> reusable capability asset -> client use
           -> field evidence updates asset and wiki
```

Rules:

1. A source becomes knowledge only after domain refinement.
2. Knowledge becomes a commitment only when CASTLE says why it matters now.
3. A generated page is not proof; a completed drill, build, observation, or deployment is proof.
4. A method enters the Capability Library only when reusable, APQC-mapped, testable, and tied to an owner-facing use case.
5. Client-specific material never moves back into a wiki or generic asset.
6. Field evidence may correct a wiki claim, business method, or capability maturity.

### Evolution Rules

1. Friction is evidence; log it before inventing structure.
2. One-time friction stays in the DAILY/log. Repeated friction promotes through weekly/monthly review.
3. HIGH safety or truth conflicts go to `SYSTEM_FLAGS.md` immediately.
4. New profit opportunities pass the CASTLE profit-skill gate.
5. Governance and structural changes require Chris approval.
6. The skeleton remains frozen; improve instructions and content inside it.
7. Prefer removing ambiguity or duplication over adding a page.
8. An improvement is complete only when validated against live use.

### Human Stop Rules

Stop and ask the AI to audit when:

- two files claim ownership of the same truth;
- a current-position page conflicts with actual progress;
- a guide says “empty,” “current,” or gives a count that no longer matches reality;
- Chris cannot decide where something belongs in under one minute;
- a task would touch raw, private data, governance, or structure;
- system maintenance displaces School, active Tech proof, or current business execution.

## Required File Edits

### 1. `.ROOT\START_HERE.md`

**Owner:** Claude Code

**Action:** compress and restructure in place. Preserve the useful folder map and color reference, but make the human operating loop the dominant first half.

Required section order:

1. `Your Morning` — keep, tighten.
2. `The Five-Move Operating Loop` — add canonical loop.
3. `Question Router` — add table above.
4. `The System Map` — keep existing folder map, shorten long descriptions.
5. `How Knowledge Becomes Value` — add promotion pipeline.
6. `How .ROOT Evolves Without Drifting` — add evolution rules.
7. `How Any AI Enters` — retain boot-chain summary.
8. `Color and Tag Navigation` — retain, compress if needed; do not duplicate tag authority.
9. `Human Stop Rules` — add concise list.
10. `Close the Loop` — task report, current-position, NOW, weekly review.

Do not copy naming tables or full placement rules from `WHERE_IT_GOES.md`. Point to them.

### 2. `00-BRAIN\WHERE_IT_GOES.md`

**Owner:** Claude Code

**Action:** preserve as sole placement/naming authority. Add only the missing promotion distinctions to the decision tree and Wiki Intake Boundary.

Add explicit routing for:

- source evidence -> matching wiki `raw\` when intentionally ingested;
- refined knowledge -> matching wiki;
- proof/project evidence -> project, course, or field-note home;
- reusable multi-client asset -> Capability Library;
- filled client-specific artifact -> appropriate `05-BUSINESS` folder;
- system friction/proposal -> AI_AUTOMATION_SYSTEMS proposal or SYSTEM_FLAGS depending urgency.

Do not duplicate the master use loop here.

### 3. `00-BRAIN\CASTLE\HOW_TO_USE.md`

**Owner:** Claude Code

**Action:** make CASTLE's human contract explicit:

- Enter to orient and sequence, not to perform domain work.
- Every answer must resolve to `why now`, `proof required`, `realm of work`, and `next action`.
- Add the outbound routing rule: read phase -> work in owner realm -> return proof/status.
- Add the promotion role: CASTLE authorizes timing; it does not certify mastery by page existence.

### 4–10. Seven wiki `HOW_TO_USE.md` files

**Owner:** Claude Code

Use one consistent skeleton while preserving domain-specific rules:

```markdown
# HOW TO USE — [HUB]
## The Question This Hub Owns
## Start Here
## Standard Work Loop
## What Counts as Proof
## Outputs and Where They Go
## Boundaries / What Goes Elsewhere
## How This Hub Learns From Use
## Close the Session
## Current State
```

Shared meanings:

- `Start Here` names no more than three files.
- `Standard Work Loop` is domain-specific.
- `Proof` distinguishes created content from learned/applied evidence.
- `Outputs` states the artifact's next home.
- `Learns From Use` explains how errors, field evidence, or volatile changes update the hub.
- `Current State` uses dated, durable wording and avoids fragile exact counts unless generated automatically.

Hub-specific requirements:

- **SYSTEMS:** concept -> diagnostic question/model -> audit/course application -> evidence. Replace stale 41-page claim with non-fragile wording.
- **PYTHON:** current-position -> stage -> concept -> drill -> mini-project -> proof. Fix `wiki/index.md` title from `Education Wiki Index` to `Python Wiki Index`.
- **EDUCATION:** course brief/current-position -> weekly need -> study support -> evidence. Replace empty-scaffold claim.
- **PHYSICS:** situation -> model -> equation/units -> worked example -> drill -> mastery. Keep Stage 3 truth in domain file.
- **BUSINESS:** current phase -> decision/method -> blank master -> instantiated artifact in `05-BUSINESS` -> field feedback. Name the canonical current-phase entry.
- **TECHNOLOGY:** require a session-mode declaration: `landscape decision` or `applied retrieval`. Name the canonical current frontier and preserve AI-lane closure.
- **AI_AUTOMATION_SYSTEMS:** research -> evidence -> proposal -> review -> promotion. Replace empty-scaffold claim and state that two loops have already completed without using fragile page counts.

### 11. `05-BUSINESS\06-Capability Library\README.md`

**Owner:** Claude Code

Add:

- the full promotion gate;
- clear distinction between `idea`, `proof`, `asset`, and `client instance`;
- inbound sources (wiki, project, field note, audit template);
- outbound destinations (practice test, client artifact, case study, improved asset);
- feedback rule: deployments update maturity and may correct the source wiki/method.

Preserve APQC naming and maturity ladder. Do not call this a wiki.

### 12. Root `AGENTS.md`

**Owner:** Claude Code

Current problem: the pointer names missing `00-BRAIN\AGENTS.md`.

Replace the boot pointer with the live authority chain:

```text
1. 00-BRAIN\AGENT.md
2. Correct lane file: CLAUDE.md / CODEX.md / ATLAS.md
3. CHRIS_CORE.md
4. SYSTEM_FLAGS.md when required
5. Optional HAT and local operating file
```

Preserve the rule that no doctrine belongs in the pointer.

### 13. `00-BRAIN\CASTLE\wiki\README.md`

**Owner:** Claude Code

Replace copied “top .01% output” mission wording with a pointer to canonical `01-NORTH_STAR\NORTH_STAR.md`. Do not paraphrase the target in this file.

### 14. `00-BRAIN\CASTLE\wiki\current-position.md`

**Owner:** Claude Code

Reconcile Physics from stale Stage 1 language to the PHYSICS domain source of truth: active Stage 3, Vectors, with Stage 1–2 mastery confirmation caveat as written in the domain current-position page. Add `source checked: 2026-07-12` or equivalent.

## Preconditions

1. Read every target live in the execution session.
2. Search target folders for equivalents and archives.
3. Confirm parent chains by name to `.ROOT`.
4. Preserve all Markdown links, frontmatter, tags, and encoding.
5. Archive prior versions only if the edit is a substantial rewrite, using `ARCHIVED_2026-07-12_...`.
6. Do not touch `raw\`, `88-JOURNAL`, or unrelated files.

## Validation

Run these checks after editing:

1. `rg -n -i "empty scaffold|41 pages|top \\.01%|00-BRAIN\\\\AGENTS.md|# Education Wiki Index"` across live targets; classify every remaining hit.
2. Confirm PHYSICS and CASTLE both report Stage 3 / Vectors.
3. Confirm each of seven hubs has exactly one live `wiki/index.md`, `wiki/log.md`, and `HOW_TO_USE.md`.
4. Run `00-BRAIN\scripts\validate_boot_chain.py`.
5. Run `00-BRAIN\scripts\wiki_lint.py --strict` or the script's documented strict invocation.
6. Run `00-BRAIN\scripts\frontmatter_audit.py` using its documented arguments.
7. Confirm no files changed under any `raw\` path or outside scope.
8. Confirm `START_HERE.md` points to `WHERE_IT_GOES.md` instead of duplicating naming rules.
9. Confirm every local guide identifies start, work, proof, output destination, boundary, learning feedback, and close.
10. Append relevant wiki/CASTLE logs, today's DAILY block, and refresh NOW only if today's operating picture changed.

## Stop Conditions

Stop and report rather than improvise if:

- a local guide's owner of truth is ambiguous;
- the implementation requires a new folder or new governance file;
- a source-of-truth conflict cannot be resolved from live files;
- validation introduces new blockers or review debt;
- preserving content would push an always-loaded file materially beyond the existing context budget;
- the edit would require touching raw, private, or archived material outside the named archive actions.

## Execution Order

1. Fix root pointer and P1 truth conflicts.
2. Rewrite `START_HERE.md` human control surface.
3. Add promotion distinctions to `WHERE_IT_GOES.md`.
4. Normalize CASTLE and seven wiki human guides.
5. Strengthen Capability Library README.
6. Update indexes/logs only where required.
7. Validate the complete instruction path end to end.

## Report Format

Claude Code returns:

```markdown
## Files Changed
## Instruction Architecture Implemented
## Drift Corrections
## Archives Created
## Validation Results
## Remaining Risks
## Single Next Action
```

## Skill and Tool Candidates

- `execution-owner: Claude Code`
- Candidate: `validate_knowledge_interfaces.py`
- Build only if the same interface drift recurs after this pass. For this execution, deterministic `rg` acceptance checks are enough.

## Expected Outcome

Chris can start at `START_HERE.md`, identify the owner system, operate it correctly, place every resulting artifact, and understand how real-world evidence evolves the system—without reading AI governance or learning a second structure.
