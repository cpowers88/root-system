---
type: report
tags: [next, governance, instruction-design, execution-brief]
created: 2026-07-12
status: approved-for-execution
supersedes: ROOT_USER_OPERATING_INSTRUCTIONS_EXECUTION_BRIEF_2026-07-12.md
---

# .ROOT User Operating Instructions — Corrected Execution Brief V2

## Decision

`START_HERE.md` is already the correct one-screen human map. It must remain unchanged.

Create a separate master human instruction file at:

```text
G:\My Drive\.ROOT\ROOT_OPERATING_MANUAL.md
```

Chris's human entry sequence becomes:

```text
START_HERE.md -> ROOT_OPERATING_MANUAL.md -> local HOW_TO_USE.md when depth is needed
```

## Instruction Architecture

| Layer | Authority | Job |
|---|---|---|
| Map | `.ROOT\START_HERE.md` | Existing visual orientation and system map; no edits |
| Master human operation | `.ROOT\ROOT_OPERATING_MANUAL.md` | How Chris routes, operates, proves, closes, and evolves work |
| Placement | `00-BRAIN\WHERE_IT_GOES.md` | Sole authority for file location, naming, tags, and destinations |
| Local human operation | Realm `HOW_TO_USE.md` or README | Detailed operating loop for CASTLE, each wiki, and Capability Library |
| AI governance | `AGENT.md`, lane files, local `CLAUDE.md`/`CODEX.md` | What AI reads, owns, may change, must validate, and when it stops |

Human instructions and AI governance remain linked but separate.

## New Master File Specification

### Target

`G:\My Drive\.ROOT\ROOT_OPERATING_MANUAL.md`

### Purpose

Answer these questions without requiring Chris to read AI prompts:

1. What is the correct operating sequence?
2. Which realm owns my question?
3. What file do I open first in that realm?
4. What counts as actual progress or proof?
5. Where does the output go?
6. How does field experience improve `.ROOT`?
7. When should I stop and ask for an audit?

### Required Sections

#### 1. How to Use This Manual

- Read `START_HERE.md` first for the map.
- Open this manual when deciding how to operate.
- Open the named local guide only when working inside a specific realm.
- Use `WHERE_IT_GOES.md` for exact placement and naming.

#### 2. The Five-Move Operating Loop

```text
ORIENT -> ROUTE -> WORK -> PROVE/PACKAGE -> CLOSE
```

1. **Orient:** open `NOW.md`; confirm the one priority and active track.
2. **Route:** choose one owner realm.
3. **Work:** open that realm's local guide and canonical current page.
4. **Prove/package:** record learning or use evidence; package only after proof.
5. **Close:** record movement and the next exact action; update status only when reality changed.

#### 3. Question Router

| Question | Owner |
|---|---|
| What matters today? | `.ROOT\NOW.md` |
| What phase or skill comes next? | `00-BRAIN\CASTLE` |
| What controls the mission? | `01-NORTH_STAR` |
| Where does this file go? | `00-BRAIN\WHERE_IT_GOES.md` |
| What should I learn or retrieve? | Matching `03-WIKIS` hub |
| Where are official course files? | `02-LIBRARY\00-SCHOOL` |
| Where does an active build live? | `02-LIBRARY\.PROJECTS` plus local/GitHub code |
| Where does business strategy or a blank master live? | `03-WIKIS\BUSINESS` |
| Where does a filled business/client artifact live? | `05-BUSINESS` |
| Where does a reusable proven capability live? | `05-BUSINESS\06-Capability Library` |
| Where does an unsorted capture go? | `77-INBOX` |
| Where does private reflection go? | `88-JOURNAL`; AI never reads it |

#### 4. How to Operate Each Realm

For every major realm, provide only:

- question owned;
- canonical first file;
- standard work loop;
- proof standard;
- output destination;
- deeper instruction location.

Do not repeat the visual map from `START_HERE.md`.

#### 5. How to Work With AI-Operated Folders

Teach Chris the standard request pattern:

```text
Goal:
Owner realm:
Source/evidence:
Desired output:
Permission level: report only / draft / execute approved changes
Proof or acceptance check:
```

State that Chris does not need to fill every field in casual use; the pattern exists for consequential or multi-file work.

For wikis, the AI must:

1. load the governing OS and local wiki instructions;
2. read `wiki/index.md` and recent log entries;
3. read current-position/path files when the hub has an active frontier;
4. search before creating;
5. leave raw immutable;
6. distinguish generated content from learned/applied proof;
7. update log/index/current position only when required;
8. state the next action.

#### 6. Knowledge-to-Value Pipeline

```text
raw source -> domain wiki -> CASTLE relevance decision -> real work/proof
           -> reusable capability asset -> client use
           -> field evidence updates the asset and wiki
```

Rules:

- Source ingestion is not mastery.
- A generated page is not proof.
- CASTLE sequences; it does not absorb or teach.
- A capability asset must be reusable, owner-understandable, APQC-mapped, testable, and indexed.
- Client-specific content never moves into a generic wiki or master asset.

#### 7. How `.ROOT` Evolves Without Drifting

```text
friction -> log -> repeated evidence -> review -> approved improvement -> validation
```

- One-time friction stays in a DAILY or local log.
- Repeated lessons promote at weekly/monthly review.
- HIGH safety or truth conflicts enter `SYSTEM_FLAGS.md` immediately.
- AI_AUTOMATION_SYSTEMS researches and proposes system improvements.
- CASTLE/review cadence evaluates timing and impact.
- Chris approves governance and structural changes.
- The skeleton stays frozen; improve content and interfaces inside it.

#### 8. Human Stop Rules

Stop and request an audit when:

- two files claim ownership of the same truth;
- current-position conflicts with actual progress;
- a guide's current-state claim is visibly stale;
- placement cannot be decided in under one minute;
- work would touch raw, private data, governance, or structure;
- maintenance is displacing School, active Tech proof, or current business execution.

#### 9. Closing the Loop

Explain the minimum close:

- What moved?
- What evidence proves it?
- What file/status changed?
- What is the next exact action?
- Does `NOW.md` actually need refreshing?

#### 10. Instruction Directory

List exact pointers, not copied doctrine:

- `START_HERE.md` — map.
- `ROOT_OPERATING_MANUAL.md` — human master manual.
- `WHERE_IT_GOES.md` — placement/naming.
- `AGENT.md` — AI OS.
- lane files — AI roles.
- `CASTLE\HOW_TO_USE.md` — command-center use.
- seven wiki `HOW_TO_USE.md` files — hub operation.
- Capability Library `README.md` and `FIRST_RUN_CHECKLIST.md` — reusable asset operation.

## Deeper Instruction Pass

### CASTLE

Update `00-BRAIN\CASTLE\HOW_TO_USE.md` so every operation identifies:

- why now;
- proof required;
- realm where work occurs;
- next action;
- return path for proof/status.

CASTLE orients and sequences. It does not perform domain work.

### Seven Wikis

Normalize each `HOW_TO_USE.md` around this skeleton:

```text
Question owned
Start here
Standard work loop
What counts as proof
Outputs and where they go
Boundaries
How the hub learns from use
Close
Current state
```

Domain loops:

- **SYSTEMS:** concept -> diagnostic question/model -> course/audit application -> evidence.
- **PYTHON:** current position -> stage -> concept -> drill -> mini-project -> proof.
- **EDUCATION:** course brief/current position -> weekly need -> study support -> evidence.
- **PHYSICS:** situation -> model -> equation/units -> example -> drill -> mastery.
- **BUSINESS:** current phase -> decision/method -> blank master -> instantiated artifact -> field feedback.
- **TECHNOLOGY:** declare `landscape decision` or `applied retrieval` -> answer -> application/decision evidence.
- **AI_AUTOMATION_SYSTEMS:** research -> evidence -> proposal -> review -> promotion.

Also correct the already-audited interface drift:

- SYSTEMS stale 41-page wording.
- EDUCATION stale empty-scaffold wording.
- AI_AUTOMATION_SYSTEMS stale empty-scaffold wording.
- PYTHON index title `Education Wiki Index` -> `Python Wiki Index`.
- BUSINESS and TECHNOLOGY must name one canonical current-frontier entry.

### Capability Library

Update its README to define:

```text
idea -> proof -> reusable asset -> client instance -> deployment feedback
```

Preserve APQC naming and maturity. Clarify inbound sources, test requirements, outbound destinations, and feedback into the originating wiki/method.

## Related Truth Corrections

Execute within the same controlled pass:

1. Root `AGENTS.md`: replace missing `00-BRAIN\AGENTS.md` pointer with the live lane chain.
2. CASTLE README: remove copied “top .01%” wording and point to canonical `NORTH_STAR.md`.
3. CASTLE current position: reconcile Physics to domain Stage 3 / Vectors with the existing Stage 1–2 mastery caveat.

## Explicit Non-Targets

- Do not edit `START_HERE.md`.
- Do not create a new folder.
- Do not merge wikis.
- Do not copy `WHERE_IT_GOES.md` tables into the manual.
- Do not copy AI governance into the human manual.
- Do not touch raw, archives outside approved replacements, or `88-JOURNAL`.
- Do not create the first Capability Library asset in this instruction pass.

## Execution Owner

`Claude Code` — broad instruction-file edits and creation of the approved new master file.

Codex validates after execution.

## Validation

1. Hash `START_HERE.md` before and after; it must be unchanged.
2. Confirm exactly one live `ROOT_OPERATING_MANUAL.md` exists at `.ROOT` root.
3. Confirm the manual points to `START_HERE.md` for the map and `WHERE_IT_GOES.md` for placement.
4. Confirm all seven wiki guides contain owner, start, loop, proof, output, boundary, feedback, close, and current-state guidance.
5. Confirm CASTLE and PHYSICS both report Stage 3 / Vectors.
6. Grep live targets for stale strings: `empty scaffold`, `41 pages`, `top .01%`, `00-BRAIN\AGENTS.md`, and `# Education Wiki Index`.
7. Run boot-chain validation, strict wiki lint, and frontmatter audit using documented invocations.
8. Confirm no scoped-out files changed.
9. Log every changed realm and append the DAILY.
10. Report remaining ambiguity and one next action.

## Stop Conditions

Stop rather than improvise if a new governance rule is required, an owner of truth remains ambiguous, the edit requires a new folder, validation adds blockers/review debt, or raw/private/out-of-scope material would be touched.

## Expected Outcome

Chris reads `START_HERE.md` for orientation, opens `ROOT_OPERATING_MANUAL.md` for the complete human instruction set, and follows a deeper local guide only when operating CASTLE, a wiki, or the Capability Library. The map stays clean; the manual supplies depth; AI governance remains precise and separate.
