# .ROOT Vault Skeleton — Functional Roles, Classification Rule, and Move-Integrity Design

*A design spec, not an execution plan. No folder is renamed or moved by this document — it defines the roles, the rule, and the mechanism the skeleton falls out of, and marks the remaining forks as open questions for a later execution pass.*

---

## 1. Purpose

This is not a folder-naming exercise. Four proposals this session (Chris's own sketch, a Claude Chat revision, ATLAS's notes, Codex's notes) all debated folder names and numbers for elevating CASTLE out of `00-BRAIN\CASTLE\`. Evaluating them surfaced a sharper, recurring failure underneath the naming debate: this session hit the same failure mode three independent times — a file moved, was archived, or was cited from the wrong copy, and nothing in the vault caught the stale reference:

1. Python wiki's `syllabus-alignment.md`/`source-map.md` cited a syllabus from an ungoverned personal-folder duplicate instead of the wiki's own immutable `raw/` copy.
2. Physics wiki's `source-map.md`, `syllabus-coverage-ledger.md`, `current-position.md`, and `learning-path.md` all cited `raw/syllabus/syllabus.pdf` as a live file — it had been archived days earlier and no longer existed there.
3. My own first draft of a Business-wiki source-classification page got several rows wrong by not cross-checking existing intake history first.

Renaming folders again would not fix that. What actually needs designing is: (a) a small, stable set of functional roles every file in `.ROOT` maps to regardless of what its folder is called this month, (b) a short decision procedure that routes any new file to its role without ad hoc judgment each time, and (c) a mechanism that catches a stale reference the moment something moves. The folder tree in Section 5 is the *output* of applying (a) and (b) — it reuses every current folder name/role that already works and invents structure only where a genuine gap was confirmed.

---

## 2. The Functional Roles

Pressure-tested at ten. Nine map cleanly to one existing top-level folder each; the tenth (Intake) is currently split across *two* folders serving the same role — that's evidence for the open consolidation question in Section 5, not a flaw in the taxonomy.

| # | Role | Definition | Folder serving it today |
|---|------|------------|--------------------------|
| 1 | **AI Governance & Coordination** | AI operating instructions, capability profiles, system self-knowledge, cross-cutting governance maps. | `00-BRAIN\` |
| 2 | **Durable Direction** | Strategy/priority that outlives any single project or session. | `01-NORTH_STAR\` |
| 3 | **Decision & Sequencing Cockpit** | What's the next highest-value action, who owns it, what proves it, where does it return — points at owner truth, never copies it. | `00-BRAIN\CASTLE\` (relocating) |
| 4 | **External Signal Steering** | A verified external change with material consequence, routed after its evidence already lives in the owning wiki. | `...projectSuccess\` (Watchtower files) |
| 5 | **Staged Research & Learning** | Multi-session research or coursework toward mastery or a decision, in one bounded subject domain. | `03-WIKIS\` |
| 6 | **Reusable Reference & Project Deliverables** | Stable reference material, course files, in-progress build artifacts. | `02-LIBRARY\` |
| 7 | **Sanitized Business Asset System** | Reusable, client-facing assets, sanitized of anything client-specific. | `05-BUSINESS\` |
| 8 | **Universal Intake Door** | Anything new from outside `.ROOT`, not yet triaged. | `77-INBOX\` — resolved 2026-07-24: sole intake door, `Clippings\` retired, Obsidian's web-clipper setting now points here directly |
| 9 | **Private Reflection** | Personal processing no AI ever reads. | `88-JOURNAL\` |
| 10 | **Historical Safety Net** | Superseded/inactive material, preserved rather than deleted. | `99-ARCHIVE\` |

**Not a role, by design:** root-level loose files (`NOW.md`, `START_HERE.md`, `MORNING_BRIEF.md`, `ROOT_OPERATING_MANUAL.md`, `AGENTS.md`/`CLAUDE.md`/`CODEX.md`) are entry surfaces, not content realms — every session touches them regardless of which role its actual work belongs to. They don't get a folder or a role number, and this design doesn't touch them.

---

## 3. The Classification Rule

Text to insert into `00-BRAIN\WHERE_IT_GOES.md`, as a new section titled `## Functional Role Rule — Ask This Before the Decision Tree`, directly above the existing `## Decision Tree — Where Does This File Go?` heading (currently line 41). The existing flat table is not replaced — it becomes the answer key for *today's* folder names; this rule is what makes that answer key derivable instead of memorized, and it survives any future rename.

> ## Functional Role Rule — Ask This Before the Decision Tree
>
> Every file in `.ROOT` serves exactly one of ten permanent functional roles. Ask these questions in order and stop at the first "yes" — the role it lands on is that file's one home, regardless of what its folder happens to be named this month:
>
> 1. **Is this an AI operating instruction, capability profile, session log, system flag, or coordination map?** → *AI Governance & Coordination.*
> 2. **Is this durable direction or priority that holds regardless of any single project — strategy, skill-gap analysis, a standing goal?** → *Durable Direction.*
> 3. **Is this deciding what happens next on something that already has an owner elsewhere — sequencing, proof status, a gate decision — without being the evidence itself?** → *Decision & Sequencing Cockpit.* (If you're about to copy the evidence rather than point to it, stop — it belongs in the owning role instead.)
> 4. **Is this a verified external signal or event with a material consequence, whose evidence already lives in its owning wiki?** → *External Signal Steering.*
> 5. **Is this staged, multi-session research or coursework building toward mastery or a decision in one bounded subject domain?** → *Staged Research & Learning.*
> 6. **Is this stable reusable reference material, a course file, or a build artifact with a concrete deliverable?** → *Reusable Reference & Project Deliverables.*
> 7. **Is this a sanitized, reusable, client-facing business asset — never active client-specific work, which never enters `.ROOT` at all?** → *Sanitized Business Asset System.*
> 8. **Did this file just arrive from outside `.ROOT` and has it not yet been triaged?** → *Universal Intake Door.* (Temporary by definition — nothing lives here past its weekly review.)
> 9. **Is this personal processing no AI should ever read?** → *Private Reflection.*
> 10. **Is this superseded, inactive, or no longer current, but worth keeping as history?** → *Historical Safety Net.*
>
> If none of the above fit and the file is a cross-session entry surface every kind of work touches (a dashboard, an orientation map, an AI pointer) — it stays a loose file at `.ROOT` root; it is not a content realm and does not get a folder.
>
> **The table below is not the rule — it is where each role currently resolves, keyed to today's folder names.** When a folder is renamed, only the table changes; the rule above does not.

---

## 4. The Move-Integrity Mechanism — `path_reference_audit.py`

**Confirmed gap:** no existing script does a general, vault-wide check for stale path-string references after a move or archive. `validate_boot_chain.py` only checks a fixed, hardcoded list of already-known-dead strings. `wiki_lint.py` only checks `[[wikilink]]` resolution inside the 8 wiki hubs' own index/link pages — not plain path strings, not vault-wide. `frontmatter_audit.py` is the right *convention family* to copy (baseline file, `--strict`, `--json`) but audits metadata schema, not path references.

### Spec

- **Inputs:**
  - `--old <path>` (repeatable, or a file listing several) — the path string(s) being retired.
  - `--new <path>` — the replacement location, or the literal value `ARCHIVED` when there is no live replacement.
  - `--since <git-ref>` (optional) — auto-derive the old/new pair list from the file renames/deletions in the given commit range, instead of a manual pair.
  - `--baseline path_reference_baseline.json` — an allowlist of accepted historical mentions (e.g., a session log's own narrative describing what *used to be* true), following the same baseline pattern as `frontmatter_audit.py`.
  - `--strict` — fail (non-zero exit) on any unbaselined hit; without it, the script reports but does not fail the run.
  - `--json` — machine-readable output.
- **Scope:** every tracked `.md`, `.py`, `.ps1`, `.yaml`, `.json` file in `.ROOT`, excluding `99-ARCHIVE\` narrative content by default (history is expected to describe old paths) unless `--strict --include-archive` is passed.
- **What it checks:** greps for the literal old-path string in all its normalized forms — backslash and forward-slash variants, with and without the `.ROOT` prefix, and the bare filename inside a `[[wikilink]]` — and reports every file/line where the *old* string still appears without a corresponding update to the *new* one.
- **Output:** console summary (count of hits, count baselined, count requiring fix) plus, with `--json`, a list of `{file, line, matched_string, old_path, new_path}` objects — one row per required fix, directly usable as a checklist.
- **How it plugs in:**
  - **`AGENT.md` File Safety rule #3** ("Archive approved replacements to `99-ARCHIVE`... do not delete system history") gets one added clause: running `path_reference_audit.py --old <path> --new <path>` with zero unresolved hits is part of what makes an archive/move "approved" and complete — not a separate optional step.
  - **CASTLE's Session Close checklist** (`OPERATIONS.md` § Session Close) gets one added line: if a move or archive happened this session, run `path_reference_audit.py` and clear all hits before the session is considered closed.
- **How it would have caught each of the 3 real incidents this session:**
  1. **Python wiki citations** — running the audit in canonical-path-verify mode (given the syllabus's designated canonical home, flag any *other* full path in the vault referencing the same filename) would have flagged the personal-folder duplicate as a second, non-canonical location the moment either reference was written — instead of it sitting silently until this session's review.
  2. **Physics wiki citations** — this is the exact case the tool is built for: `raw/syllabus/syllabus.pdf` was archived days earlier and four files still cited it as live. Running `path_reference_audit.py --old raw/syllabus/syllabus.pdf --new <archived path>` at the moment of archiving would have listed all four files as required fixes before the archive was considered done.
  3. **My own Business-wiki draft** — running the audit against the draft's own cited paths before publishing would have flagged citations that didn't resolve to any real file at that location, forcing the cross-check that was skipped.

---

## 5. The Full Top-Level Skeleton Tree

```
.ROOT/
├── AGENTS.md / CLAUDE.md / CODEX.md    — AI entry pointers (unchanged)
├── START_HERE.md                        — master orientation map (unchanged)
├── NOW.md                               — daily dashboard (unchanged)
├── MORNING_BRIEF.md                     — 3-line generated daily brief (unchanged)
├── ROOT_OPERATING_MANUAL.md             — human operating manual, Five-Move Loop (unchanged)
│
├── 00-BRAIN/                            — Role 1: AI Governance & Coordination
├── 01-NORTH_STAR/                       — Role 2: Durable Direction
├── CASTLE/                              — Role 3: Decision & Sequencing Cockpit  [RELOCATED — see below]
├── Watchtower/  (...projectSuccess today) — Role 4: External Signal Steering     [OPEN QUESTION — see below]
├── 02-LIBRARY/                          — Role 6: Reusable Reference & Project Deliverables
├── 03-WIKIS/                            — Role 5: Staged Research & Learning
├── 05-BUSINESS/                         — Role 7: Sanitized Business Asset System
├── 77-INBOX/                            — Role 8: Universal Intake Door         [RESOLVED — see below]
├── 88-JOURNAL/                          — Role 9: Private Reflection
└── 99-ARCHIVE/                          — Role 10: Historical Safety Net
```

### Entry Surfaces (root-level loose files) — unchanged

Stay exactly where they are. Entry surfaces, not content realms — nothing about this design touches them.

### `00-BRAIN\` — Role 1: AI Governance & Coordination
**For:** AI operating instructions, capability profiles, coordination maps, the Metadata Standard, the canonical scripts inventory. **Good looks like:** every AI-facing rule has exactly one home (`AGENT.md`, `WHERE_IT_GOES.md`, `SYSTEM_FLAGS.md`), nothing duplicated into another file, `scripts\` holds only vault-maintenance tooling, never project code.

### `01-NORTH_STAR\` — Role 2: Durable Direction
**For:** `NORTH_STAR.md`, System Contracts, skill-gap analysis, weekly/goal artifacts that hold regardless of any one project. **Good looks like:** direction changes rarely, only with explicit approval; nothing here is session-log or task-tracking detail.

### `CASTLE\` — Role 3: Decision & Sequencing Cockpit [RELOCATED]
Currently nested at `00-BRAIN\CASTLE\`, inside a folder whose role (governance/coordination) it doesn't actually share — CASTLE decides sequencing across *all* realms, not just BRAIN's own. This design elevates it to a top-level folder (exact name/number is a later execution decision, out of scope here — `CASTLE/` is a neutral placeholder). **For:** `OPERATIONS.md`'s existing authority chain and 8 standing rules, unchanged. **Good looks like:** every material decision names Why-now/Owner/Next-action/Proof/Return, and `wiki\log.md` is current with the last session's outcome.

### `Watchtower\` — Role 4: External Signal Steering [OPEN QUESTION]
Currently a stray, oddly-named `...projectSuccess\` folder holding only `WATCHTOWER.md` and `radar.md`, disconnected from CASTLE despite doing the same steering function on a different input (external signals vs. internal sequencing).

> **OPEN QUESTION — Chris's call:**
> - **Option A — merge into CASTLE.** Fold `WATCHTOWER.md`/`radar.md` into CASTLE's own `wiki\`. Collapses to 9 roles.
> - **Option B — keep it a separate, clearly-named top-level folder.** Codex's "eyes, not hands" argument: watching external signals is a distinct concern from deciding internal sequencing. Also zero renames — it already exists, it just needs a saner name than `...projectSuccess`.
> - **Recommendation:** Option B — sound on its own merits, and matches the preference to save existing folders rather than merge them away. Not decided here.

### `02-LIBRARY\` — Role 6: Reusable Reference & Project Deliverables
**For:** `00-SCHOOL\` (course files), `.PROJECTS\` (builds with a deliverable), domain reference piles. **Good looks like:** a course or project has exactly one folder, reference material is `.pdf`/`.md` only, nothing here is a live wiki-in-progress.

### `03-WIKIS\` — Role 5: Staged Research & Learning
**For:** the 8 wiki hubs, each with `CLAUDE.md`, `HOW_TO_USE.md`, `wiki\index.md`, `wiki\log.md`, and — for learning-engine hubs — `wiki\current-position.md`. **Good looks like:** every hub's `raw\` is immutable and every citation to it resolves to a file that still exists there (exactly what `path_reference_audit.py` guards).

### `05-BUSINESS\` — Role 7: Sanitized Business Asset System
**For:** audit templates, field notes, case studies, pricing models, proposal/SOW patterns, the capability library — all sanitized, none client-specific. **Good looks like:** every asset is reusable across clients; anything client-specific lives outside `.ROOT` entirely.

### `77-INBOX\` — Role 8: Universal Intake Door [RESOLVED 2026-07-24]
Previously split across `77-INBOX\` (manual drops) and `Clippings\` (automatic Obsidian web-clipping) — two folders serving the identical role, which was itself the evidence one door was redundant. Resolved: `Clippings\` is retired, the Obsidian web-clipper setting now points directly at `77-INBOX\`, and no path anywhere else in the vault needed to change since `77-INBOX\` was already the more heavily-referenced of the two. CASTLE's own `raw\` intake remains a separate triage-only staging point per `WHERE_IT_GOES.md`'s Raw-Intake rule, not a competing front door.

### `88-JOURNAL\` — Role 9: Private Reflection
**For:** personal reflection and private processing. **Good looks like:** no AI reads this folder, ever — that boundary is absolute in `AGENT.md`.

### `99-ARCHIVE\` — Role 10: Historical Safety Net
**For:** anything superseded, inactive, or deprecated but worth keeping, named `ARCHIVED_YYYY-MM-DD_filename.md`. **Good looks like:** nothing is ever deleted, and every archived item was verified by `path_reference_audit.py` to have zero live stale references pointing at its old location before the archive was closed.

### Not part of the canonical skeleton — transient
`2.md`, `Untitled.md`, `newvaultstructure.md`, `newvaultstructureclaude.md` are scratch files from this design effort itself, loose at vault root. No new structure is designed for them — they get archived once this design work concludes, same as any other superseded draft.

---

## 6. What This Explicitly Does Not Include

- **ATLAS's "CASTLE state machine" labels** (e.g., tagging CASTLE as being "in" a named state between sessions) — ceremony without function: no persistent process runs between sessions for CASTLE to be "in a state" of, so a state label would describe nothing real and would itself become another stale-reference risk.
- **ATLAS's machine-readable `NORTH_STAR` spec format** (`RULE_01: X=Y` key-value rules alongside the prose `NORTH_STAR.md`) — creates a second, duplicate source of truth for facts the vault already states once; the vault already carries scar tissue on this exact mistake, tracked as `flag-38: pointers, not copies`. This design does not reintroduce it.
- **ATLAS's `BRAIN` Identity/Behavior subfolder split** — would move roughly 13 of the most-referenced files in the vault to express a distinction (what the AI *is* vs. how it *behaves*) that costs nothing to state in a sentence of prose instead, and moving 13 heavily-referenced files is exactly the kind of change that creates a fresh batch of stale references on day one.

---

## 7. AI-Instruction vs. Human-Instruction Register — A Design Principle, Sharpened by Today's New Sources

*Added 2026-07-24, same session as Section 1-6, at Chris's direction: "we need to start splitting human and AI instruction files and how we write them... y'all [AI] are absolute and don't need all the extra words and I need the extra wording but in specific chunks." Grounded in a targeted read of four newly-arrived books (`AI_engineering.pdf`, `AI_builders_handbook.pdf`, `Prompt_engineering_LLMs.pdf`, `promp_engineering_generative_AI_guide.pdf`, all now in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\`) rather than intuition — and by a live incident found in the same session (see 7.4).*

### 7.1 The vault already has this split — it needs a name and a checklist, not a new folder tree

`CHRIS_CORE.md` (who Chris is, why it matters, chunked into eight numbered contract points with prose explanation) and `AGENT.md` (the OS — rules, tables, a boot sequence) are already two different registers living in two different files. That's the pattern to formalize, not replace. Building a parallel `AI-only/` vs `Human-only/` directory tree would be new structure for something the vault already does correctly at the file level — the actual gap is that no file states which register it's in, or checks itself against one when edited.

**Proposed rule for `WHERE_IT_GOES.md`'s Metadata Standard or a new short section:** every governance/instruction file declares its register in one line at the top — `register: ai-directive` (terse, absolute, scannable, written for a model to execute) or `register: human-context` (chunked, explanatory, written for Chris to read and steer by). A file that must serve both splits into a terse AI half plus a companion human-scoping doc, not one file trying to be both.

### 7.2 What an AI-directive file should contain, in fixed order — *AI Builder's Handbook* §5.1

The book's "Six Parts of a Working Prompt" — Role, Context, Task, Constraints, Examples, Output Format, in that order — is a ready-made checklist for AI-facing files: *"Order matters. Models weight the earliest and latest sections of a prompt most heavily."* `AGENT.md` already does most of this implicitly (mission → priority → work modes → file safety → final rule); it has never been checked against the six parts explicitly. That check is the concrete, low-cost next step — not a rewrite.

### 7.3 "Terse and absolute" is not one fixed register — it depends what's reading it (§5.2)

This is a genuine correction to take back to Chris, not just confirmation: the same source draws a sharper line by *model class*, not human-vs-AI. Standard models want tight, scripted, step-by-step structure. Reasoning models — explicitly naming Claude's extended thinking and Codex-class models, i.e., exactly what runs `.ROOT` — want the opposite: goal and constraints stated plainly, minimal step-by-step, because over-specifying steps for a model built to reason from a goal actively gets in its way. The book's own framing: *"you are briefing a capable specialist,"* not scripting a task. So "AI doesn't need the extra words" is right about padding, throat-clearing, and restated context — but wrong if it means spelling out steps a reasoning model should be deriving itself. `AGENT.md`'s existing style (state the rule and the reason, trust the model to apply judgment — e.g., the whole "Task Completion and Constructive Challenge" section) already matches the reasoning-model register. That's evidence to keep, not change.

### 7.4 Worked cautionary example, same session: flag #83

The `AGENT.md § Wiki Shared Layer` regression (found and fixed this session, logged as flag #83 in the July Closed Flags ledger) is this exact failure in miniature: nine cleanly numbered, checklist-style rules — a textbook AI-directive register — got silently rewritten into one run-on prose paragraph during a file split, which both broke the register (checklist → paragraph, worse for a model to parse) and orphaned the section heading 21 files still point to by name. Nobody caught it because no check exists for register or anchor integrity, only for file paths (Section 4's `path_reference_audit.py` spec). **Extension to that spec, for later implementation:** the same tool, or a lightweight sibling check, should also flag when a numbered/checklist block in a declared `register: ai-directive` file gets collapsed into unstructured prose — a register regression, not just a broken link.

### 7.5 Why long AI-directive files degrade in the middle, and the fix already exists — *Prompt Engineering for LLMs* Ch. 6

Named mechanism: the **"Valley of Meh"** — content in the middle of a long document gets systematically under-weighted (primacy/recency bias), and the standard countermeasure is the **sandwich technique** — state the single most important instruction at both the start and the end of a long document, not only once in the middle. `AGENT.md` already does this by accident: mission/priority load early, and the closing `## Final Rule` section restates the one line that matters most ("Safety boundaries can stop work; model labels and scope commentary cannot. Chris decides."). That's a validated pattern worth keeping deliberately, and worth checking on any AI-directive file long enough to have a genuine middle (roughly 100+ lines) — including, on review, whether wiki `CLAUDE.md` files need their own closing one-liner.

### 7.6 Static vs. dynamic content — already followed, worth naming

The same book's Ch. 5 distinguishes static content (boilerplate/rules, identical every time — `AGENT.md`, wiki `CLAUDE.md`s) from dynamic content (changes per session — `NOW.md`, `DAILY_*.md`, session-specific context). The vault already separates these into different files; this just gives the existing split a name so a future edit doesn't blur them back together (e.g., don't let session-specific detail creep into `AGENT.md`, the mistake the "Session-specific guidance" habit in some AI configs tends toward).

### 7.7 What this section does NOT resolve

- It does not touch `NORTH_STAR.md`. Chris raised revising it "if/as needed" for clarity — that's a separate, higher-stakes edit requiring its own review, not a byproduct of the instruction-register question.
- It does not propose new folders. Section 5's skeleton tree is unchanged by this addition.
- `AI_engineering.pdf` and `promp_engineering_generative_AI_guide.pdf` were sampled (TOC + preface) but not deep-read this session — lowest yield of the four on this specific question; a full chunked ingest of all five new AI books into `AI_AUTOMATION_SYSTEMS\wiki\` remains queued separately (see wiki `log.md`, 2026-07-24 entry), independent of whether Chris acts on 7.1-7.6.

---

## Critical Files for Implementation (later, separately approved)

- `C:\Users\chris\.ROOT\00-BRAIN\WHERE_IT_GOES.md` — where Section 3's rule gets inserted above the existing Decision Tree (line 41).
- `C:\Users\chris\.ROOT\00-BRAIN\AGENT.md` — where File Safety rule #3 gets the `path_reference_audit.py` completion clause added.
- `C:\Users\chris\.ROOT\00-BRAIN\CASTLE\OPERATIONS.md` — where the Session Close checklist gets the move/archive audit step added; its existing authority chain and standing rules are otherwise reused as-is.
- `C:\Users\chris\.ROOT\00-BRAIN\scripts\frontmatter_audit.py` — the convention template (baseline file, `--strict`, `--json`) `path_reference_audit.py` should follow exactly.
- `C:\Users\chris\.ROOT\00-BRAIN\scripts\validate_boot_chain.py` and `wiki_lint.py` — the two existing near-miss scripts whose narrower scope defines exactly what the new script must cover that they don't.
- `C:\Users\chris\.ROOT\00-BRAIN\WHERE_IT_GOES.md` Metadata Standard — where Section 7.1's `register: ai-directive` / `register: human-context` property would be added, if Chris approves it.
- `path_reference_audit.py`'s spec (Section 4) — where Section 7.4's anchor/register-regression check would extend the tool's scope, if approved.

**None of the above are edited by this document.** This is the design spec only — implementation is a separate, later approval.
