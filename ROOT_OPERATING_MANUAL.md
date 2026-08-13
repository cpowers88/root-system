---
type: guide
timeline: reference
status: live
register: human-context
reference_priority: core
tags: [governance]
created: 2026-07-12
---

# ROOT_OPERATING_MANUAL.md — The Human Operating Manual
### Second stop after `START_HERE.md`. This file explains how Chris operates, proves, closes, and evolves work inside `.ROOT`. It does not repeat the map or copy AI governance — it points to both.

---

## 1. How to Use This Manual

- Read `START_HERE.md` first — that's the map.
- Open this manual when deciding **how to operate**: what loop to run, which realm owns the question, what counts as proof.
- Open the named local guide only when actually working inside a specific realm (CASTLE, a wiki, the Capability Library).
- Use `00-BRAIN\WHERE_IT_GOES.md` for exact file placement and naming — this manual does not duplicate its tables.

---

## 2. The Five-Move Operating Loop

```text
ORIENT -> ROUTE -> WORK -> PROVE/PACKAGE -> CLOSE
```

These five moves are the **task protocol** — how one work session runs inside
the canonical System Loop. How the loop, these moves, the pipeline in §7, and
the cadence all fit one system:
`01-NORTH_STAR\System Contracts\ROOT_INFORMATION_FLOW_CONTRACT.md`.

1. **Orient:** open `NOW.md`; confirm the starting action, fixed commitments, soft time boundary, and whether the work is diverging or converging.
2. **Route:** choose one owner realm.
3. **Work:** open that realm's local guide and canonical current page.
4. **Prove/package:** record learning or use evidence; a Capability Library asset may be packaged at `draft` maturity, but proof is required before it advances past `draft`.
5. **Close:** record movement and the next exact action; update status only when reality changed.

### Shared Skill Quick Reference

Ask naturally or name the skill. Canonical definitions live in
`00-BRAIN\SKILLS\`; `.agents\skills\` and `.claude\skills\` are generated
discovery mirrors and are never edited by hand.

| When you want to... | Shared skill | What it returns |
|---|---|---|
| close, wrap up, switch AI, or leave | `session-close` | DAILY/log updates, cockpit check, handoff decision, and next action |
| check `.ROOT` health or validate a system checkpoint | `root-health` | one honest health result with blockers and reviewed debt separated |
| decide whether to learn, build, buy, test, or pursue an idea | `profit-gate` | PASS, HOLD, or REJECT through CASTLE's live decision rule |
| change an Obsidian graph color or add a color group | `graph-colors` | updated generated graph configuration from `COLOR_MAP.yaml` |

### Safe Diagnostic Commands

Run these from `.ROOT`. They are read-only in the forms shown:

| Check | Command |
|---|---|
| Complete reviewed health gate | `python 00-BRAIN\scripts\root_health.py` |
| Boot and governance paths | `python 00-BRAIN\scripts\validate_boot_chain.py` |
| Wiki blockers and review debt | `python 00-BRAIN\scripts\wiki_lint.py --strict --fail-on-review` |
| Frontmatter against the reviewed baseline | `python 00-BRAIN\scripts\frontmatter_audit.py --baseline 00-BRAIN\scripts\frontmatter_baseline.json` |
| Shared-skill mirror equality | `python 00-BRAIN\scripts\sync_shared_skills.py --check` |
| Metadata-plan determinism and zero target writes | `python 00-BRAIN\scripts\metadata_migration_plan.py --self-test` |

These maintenance forms write generated artifacts:

| Maintenance action | Command | What it writes | Use only when... |
|---|---|---|---|
| rebuild graph colors | `python 00-BRAIN\scripts\build_graph_colors.py` | `.obsidian\graph.json` | `COLOR_MAP.yaml` has an approved edit |
| synchronize shared skills | `python 00-BRAIN\scripts\sync_shared_skills.py --sync` | `.agents\skills\` and `.claude\skills\` mirrors | a canonical skill changed and was validated |
| save a metadata dry-run report | `python 00-BRAIN\scripts\metadata_migration_plan.py --output ...` | one approved report under `00-BRAIN\Session_Logs` | a named review task requires the artifact |

A frontmatter baseline refresh is a separate reviewed decision, not a routine
command.

---

## 3. Question Router

| Question | Owner |
|---|---|
| What matters today? | `.ROOT\NOW.md` |
| What phase or skill comes next? | `00-BRAIN\CASTLE` |
| What controls the mission? | `01-NORTH_STAR` |
| What business vehicle are we testing? | `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` |
| What must happen before and during Fall 2026? | `01-NORTH_STAR\Goals & Milestones\fall_2026_semester.md` plus live PYTHON/PHYSICS/EDUCATION current-position pages |
| What materially changed outside `.ROOT`? | `01-NORTH_STAR\WATCHTOWER.md` and `radar.md` |
| What must the AI OS be capable of? | `01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md` |
| Where does this file go? | `00-BRAIN\WHERE_IT_GOES.md` |
| What should I learn or retrieve? | Matching `03-WIKIS` hub |
| What opportunity deserves testing next? | `00-BRAIN\CASTLE\wiki\opportunity-queue.md` |
| Where are official course files? | `04-SCHOOL` |
| Where does an active build live? | `02-LIBRARY\.PROJECTS` plus local/GitHub code |
| Where does business strategy or a blank master live? | `03-WIKIS\BUSINESS` |
| Where does an active client-specific/private artifact live? | A separate client workspace or repository outside `.ROOT` |
| Where does a reusable or sanitized business artifact live? | `05-BUSINESS` |
| Where does a reusable capability asset live? | `05-BUSINESS\06-Capability Library` |
| Where does a manually dropped unsorted file go? | `77-INBOX` — capture filter and routing steps: `CASTLE\OPERATIONS.md` § Weekly Inbox Routing Checklist |
| Where does an automatic Obsidian web clipping go? | `77-INBOX` — the clipper routes there; use the weekly routing checklist |
| Where does private reflection go? | `88-JOURNAL`; AI never reads it |

---

## 4. How to Operate Each Realm

| Realm | Question Owned | Canonical First File | Standard Work Loop | Proof Standard | Output Destination | Deeper Instruction |
|---|---|---|---|---|---|---|
| `NOW.md` | What matters today? | `.ROOT\NOW.md` | Read the start action, school commitment, technology rep, business/system item, and soft time boundary | Work began from a clear start and status reflects reality | Updates to `NOW.md` itself | Castle owns and refreshes it every session |
| CASTLE | What phase or skill comes next? | `00-BRAIN\CASTLE\wiki\current-position.md` | Orient (index + log + roadmap) → identify the phase/skill gap → point to the realm that does the work → log the sequencing decision | A phase/skill page names exit criteria, and the actual work happened in its home realm, not here | Updated maps, phase/skill pages, `wiki/log.md`, `NOW.md` refresh | `00-BRAIN\CASTLE\HOW_TO_USE.md` |
| `01-NORTH_STAR` | What controls the mission and current strategic vehicle? | `01-NORTH_STAR\NORTH_STAR.md` | Load the star; add `CURRENT_STRATEGY.md`, `fall_2026_semester.md`, or reviews only when their question is active | The fixed direction is preserved and the vehicle changes only through evidence | Reviews and approved star/strategy updates; Chris may authorize a mid-cycle impact-reviewed change | `01-NORTH_STAR\README.md` |
| North Star system contract | What must `.ROOT` be able to do and return? | `01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md` | Load for architecture/evolution audits; apply the named capability, proof, and return contract without copying AGENT governance | A fresh session can find owners, evidence, authority, and next action | Approved system changes return to their owning files/logs | `00-BRAIN\AGENT.md` remains behavioral authority |
| Watchtower (in `01-NORTH_STAR`) | What external change could materially affect us? | `01-NORTH_STAR\WATCHTOWER.md` | Verify in the owning evidence home → add a qualifying radar row → sweep → CASTLE gate/test | A row names evidence, affected assumption/choice, consequence/test, and review trigger; action follows measured proof | Exactly `WATCHTOWER.md` and `radar.md`; decisions return to CASTLE/current strategy | `01-NORTH_STAR\WATCHTOWER.md` |
| `WHERE_IT_GOES.md` | Where does this file go? | `00-BRAIN\WHERE_IT_GOES.md` | Check its Decision Tree before creating any file | The file lands at the named path on the first try | N/A — this file is the placement authority itself | None deeper; this file is the authority |
| Matching `03-WIKIS` hub | What should I learn or retrieve? | that hub's `wiki/current-position.md` (or `index.md` where no staged path exists) | current position → concept/stage → practice/drill → proof, per that hub's own loop | A drill, mini-project, or applied use proves the concept — a generated page alone does not | Study aids stay in-vault; skills proven get logged against the matching CASTLE skill page | that hub's own `HOW_TO_USE.md` |
| `04-SCHOOL` | Where are official course files? | the course's own folder | Pull syllabus/D2L material as-is; AI help stays within that course's stated AI policy | Submitted coursework is Chris's own work | Stays in the course folder | course briefs (EDUCATION wiki links out for study support) |
| `02-LIBRARY\.PROJECTS` | Where does an active build live? | the project's own `Docs\` folder | Build locally/GitHub; only small single-file scripts may live here | The build runs and does what its `Docs\` say | Code stays local + GitHub; status shows in `NOW.md` and CASTLE | the project's own `Docs\` folder |
| `03-WIKIS\BUSINESS` | Where do business methods and research live? | `03-WIKIS\BUSINESS\wiki\index.md` after `CURRENT_STRATEGY.md` when the question concerns the active vehicle | strategy assumption → method/evidence → bounded action → field result | A real conversation, observation, delivery, or use corrects the method; re-reading a plan is not proof | Blank masters live in `05-BUSINESS`; active client-specific copies go to the separate client workspace; sanitized reusable learning may return there | `03-WIKIS\BUSINESS\HOW_TO_USE.md` |
| Separate client workspace/repository | Where does active client-specific/private work live? | the client-authorized workspace outside `.ROOT` | instantiate approved masters → execute the engagement → retain client data only in that boundary | Real engagement evidence exists and client confidentiality is preserved | Remains outside `.ROOT`; only sanitized lessons, reusable methods/assets, approved case studies, and non-sensitive metadata return | client-specific instructions and agreement |
| `05-BUSINESS` | Where does a reusable or sanitized business artifact live? | the matching subfolder (Audit Templates, Field Notes, Case Studies, Pricing Models, Proposals & SOWs) | create reusable masters or sanitize approved field learning before capture | The artifact contains no active client-private content and its maturity/evidence is honest | Stays in its subfolder; generalized results may update the BUSINESS wiki | none deeper — this folder is reusable/sanitized business operations |
| `05-BUSINESS\06-Capability Library` | Where does a reusable capability asset live? | `CAPABILITY_LIBRARY_INDEX.md` | idea → draft asset (`APQC_[process]_[name].md`) → index row → named test → tested internally → client-ready | Maturity is stated honestly: idea / draft / tested internally / client-ready / deployed; proof gates advancement past `draft`, not entry | The index row plus the asset file itself | `README.md` and `FIRST_RUN_CHECKLIST.md` |
| `77-INBOX` | Where does a manually dropped unsorted file go? | the file inside `77-INBOX\` | drop it → weekly sweep routes it via `WHERE_IT_GOES.md`, or flags it ambiguous | Nothing sits past one weekly review | Routes out to its real home | CASTLE's Weekly Inbox Routing Checklist (`OPERATIONS.md`) |
| Automatic Obsidian clipping | Where does a web clipping go? | the clipped file inside `77-INBOX\` | clip it → weekly sweep routes it via `WHERE_IT_GOES.md`, or flags it ambiguous | Nothing sits past one weekly review | Routes out to its real home | CASTLE's Weekly Inbox Routing Checklist (`OPERATIONS.md`) |
| `88-JOURNAL` | Where does private reflection go? | N/A | Chris writes; AI never reads or writes here | N/A | Stays private | none — hard boundary, no exceptions |

---

## 5. Starting Claude Code Safely

Start Claude Code from `C:\Users\chris\.ROOT` for normal `.ROOT` work. This keeps
the project policy, root instructions, status, and file references on one known
base. Starting from a subfolder is no longer required and must not be supported by
copying `.claude\settings*.json` into individual wikis.

The safety layers are intentionally separated:

- `C:\Users\chris\.claude\settings.json` carries the user-level journal/raw and
  destructive-command denies that follow Claude if the launch folder changes.
- `.ROOT\.claude\settings.json` is the tracked, reviewable project policy.
- `.ROOT\.claude\settings.local.json` holds machine-specific allow candidates
  only; it cannot weaken the two safety layers above.

These controls protect **places and consequential actions**, not model roles.
Claude retains the same in-scope task authority as Codex: it may orient and route,
read raw evidence, research, teach, create and edit non-protected files, build and
test scripts or software, operate CASTLE and the wikis, design and synchronize
skills, audit or implement approved governance, use web/MCP tools, and validate or
checkpoint work. The practical boundaries are:

- no AI reads or writes `88-JOURNAL`;
- raw evidence may be read but never modified without an explicit approved
  exception;
- shell deletion, directory removal, `git reset --hard`, and `git clean` are
  blocked because `.ROOT` archives history instead of deleting it;
- edits, shell commands, PowerShell, and MCP calls remain available through human
  permission prompts; an `ask` rule is a gate, not a denial;
- academic, external-action, credential, client/privacy, and governance approval
  stops come from `AGENT.md` and apply equally to every model.

Launch with the ordinary `claude` command. Do not add `--tools`,
`--disallowedTools`, `--setting-sources`, `--safe-mode`, or `--bare` during normal
`.ROOT` work; those are intentional troubleshooting/session overrides and can hide
normal capabilities or configuration sources.

After any settings edit, open a **fresh** Claude session and run `/status`, then
`/permissions`. Confirm both the user and project sources are listed and that
journal/raw/destructive rules appear as denies. Run `claude doctor` if Claude
reports an invalid settings file.

Claude's file-tool deny rules are the enforced Claude-tool boundary on native
Windows. Its operating-system sandbox is available on macOS, Linux, and WSL2—not
native Windows—so the checked-in sandbox block is defense in depth for a supported
environment and must not be described as Windows OS enforcement. Arbitrary Python
or Node subprocesses are not constrained by Claude's file-tool path rules; they
remain approval-gated and governed by the same raw/private prohibition.

References: [Claude Code settings](https://code.claude.com/docs/en/settings),
[permissions](https://code.claude.com/docs/en/permissions), and
[sandboxing](https://code.claude.com/docs/en/sandboxing).

---

## 6. How to Work With AI-Operated Folders

`.ROOT` uses one AI team. Any AI may complete any in-scope task it can safely
access. Claude and Codex profiles describe strengths and tool limits,
not exclusive jobs. A material alternative or conflict is stated once with a
recommendation; unless a true safety/authority boundary applies, AI then follows
Chris's direction.

For consequential work, the system recommends a lead and requires an
independent challenger/validator by default. If a second surface is unavailable,
deterministic checks plus explicit disclosure are the bounded fallback Chris may
accept.

Use **DIVERGE** when gathering evidence or exploring options and **CONVERGE**
when choosing, building, validating, or finishing. The modes control AI intake
and tangent behavior, not Chris's authority to redirect.

Standard request pattern for consequential or multi-file work:

```text
Goal:
Owner realm:
Source/evidence:
Desired output:
Permission level: report only / draft / execute approved changes
Proof or acceptance check:
```

Chris does not need to fill every field in casual use — the pattern exists for consequential or multi-file work, not every question.

### Visual folder identity

Windows Explorer folder skins are generated and repaired through
`00-BRAIN\scripts\folder_icons.ps1`. Major realms use distinct Tabler symbols
and colors; repeated roles such as notes, templates, code, stages, and logs reuse
one identity. The full operating guide, protected-folder exclusions, preview,
backup location, and repair commands are in `00-BRAIN\FOLDER_ICON_SYSTEM.md`.

Do not repair icons manually one folder at a time. Run:

```powershell
pwsh -File 00-BRAIN\scripts\folder_icons.ps1 -Mode Apply -RefreshExplorer
```

For wikis, the AI must:

1. Load the governing OS and local wiki instructions.
2. Read `wiki/index.md` and recent log entries.
3. Read current-position/path files when the hub has an active frontier.
4. Search before creating.
5. Leave raw immutable.
6. Distinguish generated content from learned/applied proof.
7. Update log/index/current position only when required.
8. State the next action.

---

## 7. Knowledge-to-Value Pipeline

This pipeline is the **business application** of the shared information flow
(`ROOT_INFORMATION_FLOW_CONTRACT.md`) — the same eight states applied to
turning knowledge into assets:

```text
raw source -> domain wiki / field evidence -> Watchtower when external + material
           -> CASTLE opportunity decision -> bounded real work
           -> draft capability asset -> internal test/proof -> client-ready asset -> client use
           -> field evidence updates the asset and wiki
```

Rules:

- Source ingestion is not mastery.
- A generated page is not proof.
- CASTLE sequences; it does not absorb or teach.
- Watchtower observes and routes; it never changes strategy or opens work itself.
- A capability asset must be reusable, owner-understandable, APQC-mapped, testable, and indexed; it may be indexed at `draft` maturity, but proof is required before it advances past `draft`.
- Active client-specific/private content stays in its separate client workspace;
  only sanitized lessons, reusable methods/assets, approved case studies, and
  non-sensitive metadata may return to `.ROOT`.

---

## 8. How `.ROOT` Evolves From Evidence and Direction

```text
AI-observed friction -> log -> repeated evidence -> proposal -> approval -> validation
Chris-directed change -> impact review -> approval -> implementation -> validation
External change -> evidence home -> Watchtower -> CASTLE test -> outcome -> Ratchet
```

- One-time AI-observed friction stays in a DAILY or local log.
- Repeated lessons promote at weekly/monthly review.
- HIGH safety or truth conflicts enter `SYSTEM_FLAGS.md` immediately.
- `AI_AUTOMATION_SYSTEMS` researches and proposes system improvements.
- CASTLE/review cadence evaluates timing and impact.
- Chris may directly authorize a change without waiting for repeated evidence;
  the impact review and validation still apply.
- The skeleton stays frozen; improve content and interfaces inside it.

---

## 9. Human Stop Rules

Stop and request a decision or audit when:

- Two files claim ownership of the same truth.
- Current-position conflicts with actual progress.
- A guide's current-state claim is visibly stale.
- Placement cannot be decided in under one minute.
- Work would touch raw or private data, or governance/structure lacks Chris approval.
- Maintenance is displacing School, active Tech proof, or current business execution.

---

## 10. Closing the Loop

The minimum close, every session that changes anything:

- What moved?
- What evidence proves it?
- What file/status changed?
- What is the next exact action?
- Does `NOW.md` actually need refreshing?

After governance, system-script, settings, metadata-policy, or shared-skill work,
run the canonical read-only health gate from `.ROOT`:

```text
python 00-BRAIN\scripts\root_health.py
```

`BLOCKER` stops the checkpoint. `PASS WITH DEBT` means the named checks found no
new blocker while reviewed debt remains; it is not “clean.” `PASS` means only the
listed scopes passed. Use `--strict` for a zero-debt acceptance gate and `--json`
for machine-readable output. The command explicitly lists what it does not
evaluate, including semantic freshness, project truth, review cadence, and source
ownership. Ordinary learning sessions do not need this system-wide check.

---

## 11. Instruction Directory

- `START_HERE.md` — the map.
- `ROOT_OPERATING_MANUAL.md` — this file, the human master manual.
- `00-BRAIN\WHERE_IT_GOES.md` — placement and naming.
- `01-NORTH_STAR\System Contracts\ROOT_INFORMATION_FLOW_CONTRACT.md` — how the four system views translate into one information flow; the seven-line trace.
- `00-BRAIN\AGENT.md` — the AI operating system.
- `00-BRAIN\CLAUDE.md` / `CODEX.md` — AI capability profiles.
- `00-BRAIN\CASTLE\HOW_TO_USE.md` — command-center use.
- `01-NORTH_STAR\WATCHTOWER.md` — material external-signal routing.
- `01-NORTH_STAR\README.md` — star companion loading and review contract.
- `03-WIKIS\SYSTEMS\HOW_TO_USE.md`, `03-WIKIS\PYTHON\HOW_TO_USE.md`, `03-WIKIS\EDUCATION\HOW_TO_USE.md`, `03-WIKIS\PHYSICS\HOW_TO_USE.md`, `03-WIKIS\BUSINESS\HOW_TO_USE.md`, `03-WIKIS\TECHNOLOGY\HOW_TO_USE.md`, `03-WIKIS\AI_AUTOMATION_SYSTEMS\HOW_TO_USE.md`, `03-WIKIS\REVENUE_LAB\HOW_TO_USE.md` — one per hub, same skeleton.
- `05-BUSINESS\06-Capability Library\README.md` and `FIRST_RUN_CHECKLIST.md` — reusable asset operation.

---
*Master human instruction file. Map: `START_HERE.md`. Placement: `WHERE_IT_GOES.md`. AI governance: `AGENT.md` + capability profiles — read separately, never copied here.*
*Created: July 12, 2026.*
