---
type: specification
timeline: reference
status: active
tags: [governance, system-evolution]
created: 2026-07-24
---

# .ROOT Vault Skeleton — Functional Roles, Classification Rule, and Move-Integrity Design

*A design spec and governing target for the 2026-07-24 meta-layer implementation. The current physical tree remains unchanged; this document defines the logical roles, routing rule, evidence-gated mechanism, and migration conditions.*

---

## 1. Purpose

This is not a folder-naming exercise. Four proposals this session (Chris's own sketch, a Claude Chat revision, ATLAS's notes, Codex's notes) all debated folder names and numbers for elevating CASTLE out of `00-BRAIN\CASTLE\`. Evaluating them surfaced a sharper, recurring failure underneath the naming debate: this session hit the same failure mode three independent times — a file moved, was archived, or was cited from the wrong copy, and nothing in the vault caught the stale reference:

1. Python wiki's `syllabus-alignment.md`/`source-map.md` cited a syllabus from an ungoverned personal-folder duplicate instead of the wiki's own immutable `raw/` copy.
2. Physics wiki's `source-map.md`, `syllabus-coverage-ledger.md`, `current-position.md`, and `learning-path.md` all cited `raw/syllabus/syllabus.pdf` as a live file — it had been archived days earlier and no longer existed there.
3. My own first draft of a Business-wiki source-classification page got several rows wrong by not cross-checking existing intake history first.

Renaming folders again would not fix that. What actually needs designing is: (a) a small, stable set of functional roles every file in `.ROOT` maps to regardless of what its folder is called this month, (b) a short decision procedure that routes any new file to its role without ad hoc judgment each time, and (c) a mechanism that catches a stale reference the moment something moves. The folder tree in Section 5 is the *output* of applying (a) and (b) — it reuses every current folder name/role that already works and invents structure only where a genuine gap was confirmed.

---

## 2. The Functional Roles

Pressure-tested at ten. The roles map to the current vault, with Intake now resolved to one front door (`77-INBOX`). CASTLE elevation and Watchtower naming remain proposed placement questions, not proof that the taxonomy needs more roles.

| # | Role | Definition | Folder serving it today |
|---|------|------------|--------------------------|
| 1 | **AI Governance & Coordination** | AI operating instructions, capability profiles, system self-knowledge, cross-cutting governance maps. | `00-BRAIN\` |
| 2 | **Durable Direction** | Strategy/priority that outlives any single project or session. | `01-NORTH_STAR\` |
| 3 | **Decision & Sequencing Cockpit** | What's the next highest-value action, who owns it, what proves it, where does it return — points at owner truth, never copies it. | `00-BRAIN\CASTLE\` — **settled 2026-07-25; elevation declined, not deferred** |
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

## 4. The Move-Integrity Mechanism — shared scanner with explicit checks

**Confirmed gap:** no existing script does a general, vault-wide check for stale path-string references after a move or archive. `validate_boot_chain.py` only checks a fixed, hardcoded list of already-known-dead strings. `wiki_lint.py` only checks `[[wikilink]]` resolution inside the 8 wiki hubs' own index/link pages — not plain path strings, not vault-wide. `frontmatter_audit.py` is the right *convention family* to copy (baseline file, `--strict`, `--json`) but audits metadata schema, not path references.

### Spec

- **Shared substrate:** one scanner/parser, following the existing baseline/`--strict`/`--json` convention.
- **Separate checks and reports:** (1) explicit old→new path moves and archive references; (2) resolvable file references and anchors; (3) canonical-copy violations; and (4) declared instruction-register conformance. A shared executable is acceptable; one undifferentiated failure metric is not.
- **Inputs:** explicit old/new pairs or a `--since <git-ref>` rename inventory, a baseline for accepted historical mentions, `--strict`, `--json`, and an optional archive-inclusion switch.
- **Scope:** tracked Markdown and implementation/config files across `.ROOT`, with archive narrative excluded by default because it is expected to describe old paths.
- **Acceptance:** report boot-chain, navigation, generated-output, and runtime-consumer references—not only source-file text. A move is not complete until its impact report is clear, or every remaining historical hit is baselined.
- **Session integration:** the read-only prototype now exists at `00-BRAIN\scripts\path_reference_audit.py`; CASTLE Session Close integration remains gated on fixture tests, acceptance evidence, and explicit governance review. The validator remains read-only against live vault content.
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
├── 00-BRAIN/CASTLE/                     — Role 3: Decision & Sequencing Cockpit  [SETTLED 2026-07-25 — STAYS NESTED]
├── Watchtower/  (...projectSuccess today) — Role 4: External Signal Steering     [KEEP SEPARATE — PLACEMENT/NAME TO BE TESTED]
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

### `00-BRAIN\CASTLE\` — Role 3: Decision & Sequencing Cockpit [SETTLED — STAYS]
**Resolved 2026-07-25: CASTLE stays at `00-BRAIN\CASTLE\`.** The role is
cross-realm, so elevation was a plausible usability improvement — but the gate
required evidence that the current nesting causes enough navigation, loading,
ownership, or maintenance failure to justify moving a high-reference directory,
and across the full eight-source intake, two independent mid-update passes, and
both July monthly reviews, that evidence never appeared. A gate that produces
no supporting evidence is answered, not left open. Reopening requires a
documented live failure caused by the nesting, not a fresh proposal.
`OPERATIONS.md`'s authority chain and standing rules remain the baseline.
**Good looks like:** every material decision names
Why-now/Owner/Next-action/Proof/Return, and `wiki\log.md` is current with the
last session's outcome.

### `Watchtower\` — Role 4: External Signal Steering [KEEP SEPARATE]
The source batch supports a separate, read-only sensing boundary: Watchtower observes and records a narrow typed handoff; CASTLE prioritizes, gates, and tracks proof; the owning wiki retains evidence; Chris approves consequential change. The current `...projectSuccess\` name and any relocation remain implementation questions. Test the handoff and interface cost; do not merge the roles by default.

### `02-LIBRARY\` — Role 6: Reusable Reference & Project Deliverables
**For:** `00-SCHOOL\` (course files), `.PROJECTS\` (builds with a deliverable), domain reference piles. **Good looks like:** a course or project has exactly one folder, reference material is `.pdf`/`.md` only, nothing here is a live wiki-in-progress.

### `03-WIKIS\` — Role 5: Staged Research & Learning
**For:** the 8 wiki hubs, each with `CLAUDE.md`, `HOW_TO_USE.md`, `wiki\index.md`, `wiki\log.md`, and — for learning-engine hubs — `wiki\current-position.md`. **Good looks like:** every hub's `raw\` is immutable and every citation to it resolves to a file that still exists there (exactly what `path_reference_audit.py` guards).

### `05-BUSINESS\` — Role 7: Sanitized Business Asset System
**For:** audit templates, field notes, case studies, pricing models, proposal/SOW patterns, the capability library — all sanitized, none client-specific. **Good looks like:** every asset is reusable across clients; anything client-specific lives outside `.ROOT` entirely.

### `77-INBOX\` — Role 8: Universal Intake Door [RESOLVED 2026-07-24]
`77-INBOX\` is the single universal front door. `Clippings\` is retired and the Obsidian web-clipper points here. CASTLE's `raw\` remains a separate triage-only staging point under the existing Raw-Intake rule, not a competing universal door.

### `88-JOURNAL\` — Role 9: Private Reflection
**For:** personal reflection and private processing. **Good looks like:** no AI reads this folder, ever — that boundary is absolute in `AGENT.md`.

### `99-ARCHIVE\` — Role 10: Historical Safety Net
**For:** anything superseded, inactive, or deprecated but worth keeping, named `ARCHIVED_YYYY-MM-DD_filename.md`. **Good looks like:** nothing is ever deleted, and every archived item was verified by `path_reference_audit.py` to have zero live stale references pointing at its old location before the archive was closed.

### Not part of the canonical skeleton — transient
`2.md`, `Untitled.md`, and `newvaultstructure.md` were scratch files from this
design effort and are now preserved in `99-ARCHIVE\` with dated names.
`newvaultstructureclaude.md` remains the live folder/file synopsis. No new
structure is designed for the archived drafts.

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

> **Resolved 2026-07-25 (flag #84 closed).** This proposal was adopted, scoped,
> and written into `WHERE_IT_GOES.md § Metadata Standard` with **five** approved
> values (`ai-directive`, `ai-loader`, `ai-profile`, `human-context`,
> `compatibility-pointer`) restricted to **instruction-interface files only**.
> The property is not a genre label — content, reports, plans, and evidence are
> described by `type:` and carry no register. Note the process failure worth
> keeping: between §8.5's "add it only after validation rules are defined" and
> the actual decision, the property propagated by sibling precedent to 61 files
> and 8 values — two values minted by this update's own output. The audit found
> the core five applied correctly; five leaks onto non-instruction files were
> stripped in the same pass. Live state: 56 files, 5 values, zero outliers.

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
- The initial Section 7 pass sampled `AI_engineering.pdf` and
  `promp_engineering_generative_AI_guide.pdf`. That limitation is now closed:
  all eight July 24 sources were subsequently read in complete physical-page
  chunks. Section 8 records the whole-batch architecture synthesis; generic
  domain compilation remains a separate owner-return decision.

---

## 8. Redesign-Relevant Findings from the 2026-07-24 Book Batch

*Evidence-only synthesis after complete chunk intake of all eight PDFs
(3,789/3,789 physical pages). Full coverage, limitations, and chapter-level
findings live in
`00-BRAIN\CASTLE\wiki\source-summaries\architecture-update-2026-07-24\`.
This section records what the sources say about implementing this design. It
does not approve a move, validator, metadata change, or Watchtower decision.*

### 8.1 Functional-role validation

- **Logical responsibility is not physical topology.** *Agentic AI for
  Engineers* Ch. 5 and 12 distinguishes reusable patterns from centralized,
  hierarchical, sequential, debate, and decentralized topologies. *AI
  Engineering* Ch. 10 likewise treats component placement as fluid. This
  supports keeping the ten roles as logical responsibilities without requiring
  ten agents, ten processes, or one exact folder per responsibility.
- **Start with the smallest topology that passes.** *AI Builder's Handbook*
  Ch. 7–9, *Prompt Engineering for LLMs* Ch. 10, and *Agentic AI for Engineers*
  Ch. 5 independently require escalation from deterministic/single-agent work
  only after a demonstrated limitation. The taxonomy should classify work; it
  should not manufacture orchestration.
- **One fact, one owner; other views are derived.** *R for Data Science* Ch. 9
  formalizes this through tidy data, while Ch. 10 adds key/cardinality
  discipline. This supports domain-wiki ownership and CASTLE pointers rather
  than copied research or proof.
- **An explicit unknown state is necessary.** *Machine Learning Design
  Patterns* Ch. 3's Neutral Class shows why a classifier must be allowed to
  abstain. The Section 3 decision tree needs an unresolved/escalate outcome for
  genuinely ambiguous files rather than forcing a false home.
- **Value remains an outcome layer, not a role.** McKinsey's *Economic
  Potential of Generative AI* separates technical feasibility, solution
  development, adoption, capacity redeployment, and realized value. This
  supports keeping value proof in the Return Packet and owning business system
  instead of adding a generic "value" folder.
- **No source falsified the ten responsibilities.** The books add interfaces,
  lifecycle checks, and failure states, not an eleventh durable content role.
  Collective exhaustiveness still needs real routing fixtures before
  implementation.

### 8.2 Move-integrity tooling

- **Stable identifiers must survive reordered work.** *Machine Learning Design
  Patterns* Ch. 5 (Keyed Predictions) requires keys through asynchronous
  processing. A move audit should report a stable reference/action ID, old
  target, new target, referring file, and status—not only a hit count.
- **Migration needs schema bridges and checkpoints.** The same book's Ch. 4
  (Checkpoints) and Ch. 6 (Bridged Schema) support a compatibility interval,
  restorable checkpoints, and rollback rather than a flag-day move.
- **Reference integrity is relational, not substring-only.** *R for Data
  Science* Ch. 10–11 shows duplicate-key, unmatched-key, and anchor-boundary
  failure. The tool should parse Markdown targets/headings and distinguish
  unresolved, duplicate, and changed-anchor cases in addition to literal path
  strings.
- **Derived outputs need dependency-aware invalidation.** *R for Data Science*
  Ch. 21 and *AI Engineering* Ch. 9 show that caches go stale when only the
  immediate source is tracked. Generated maps, graph configuration, mirrors,
  and rendered interfaces need declared dependencies or regeneration checks
  after a move.
- **Authoring and consumption must use the same transformation.** *Machine
  Learning Design Patterns* Ch. 6 (Transform/Workflow Pipeline and Feature
  Store) provides the direct analogue: a canonical file can be correct while a
  consumer sees a stale transformation. The validator must check boot,
  navigation, generated, and runtime consumption paths, not only source files.
- **Fresh-session reproducibility is an acceptance test.** *R for Data Science*
  Ch. 6 and 24 requires a cold restart/full render from durable source.
  Migration close should include a fresh boot-chain/navigation run rather than
  relying on the session that performed the move.
- **Smallest coherent implementation:** one shared scanner/parser with
  separately reportable checks for path moves, unresolved/duplicate
  references, heading anchors, canonical-copy violations, generated dependency
  drift, and instruction-register regressions. One executable does not mean one
  undifferentiated pass/fail metric.

### 8.3 AI/human instruction register

- **The register proposal is independently corroborated.** *AI Engineering*
  Ch. 5, *AI Builder's Handbook* Ch. 5, *Prompt Engineering for LLMs* Ch. 5–6,
  and *Agentic AI for Engineers* Ch. 6 all treat prompts as versioned interfaces
  with owner, model, schema/format, tests, review, and rollback.
- **Separate instruction, evidence, and runtime state.** *Prompt Engineering
  for Generative AI* Ch. 4–6 and *AI Engineering* Ch. 6 distinguish static
  instruction, retrieved context, memory, and tool output. Retrieved text may
  be stale or adversarial and must never silently inherit instruction
  authority.
- **Add target and acceptance metadata, not a second truth.** The smallest
  useful record is the proposed `register:` property plus target
  model/audience, owner, version/check date, required output contract, and named
  validation. The human-readable body remains the canonical instruction.
- **Validate syntax and semantics separately.** *AI Engineering* Ch. 2 and 5
  and *AI Builder's Handbook* Ch. 5 show that valid Markdown/YAML/JSON does not
  prove the required content or safe behavior. A register validator needs
  structural checks plus behavioral fixtures.
- **Examples and evaluations are versioned dependencies.** *Prompt Engineering
  for LLMs* and *Prompt Engineering for Generative AI* Ch. 1 and 3 show that
  examples change behavior and consume context. They belong with the
  instruction's test record, not as untracked prose.
- **R Markdown supplies a non-AI precedent.** *R for Data Science* Ch. 21–24
  uses a human-readable source plus YAML control metadata and derived outputs.
  This supports metadata over a duplicate machine-only instruction file.
- **Flag #83 becomes the minimum regression fixture.** A validator must catch
  both the missing `§ Wiki Shared Layer` heading and the numbered-list-to-prose
  register collapse while leaving the instruction's substantive meaning for a
  separate behavioral test.

### 8.4 Watchtower-vs-CASTLE architecture evidence

- **Sensing, monitoring, deciding, and acting have different contracts.** *AI
  Engineering* Ch. 6 and 10 separates retrieval/monitoring from planning,
  orchestration, and action. Each has different metrics and failure modes.
- **Independent monitors reduce correlated failure.** *Agentic AI for
  Engineers* Ch. 8 recommends different models, prompts, or isolated context
  for oversight and makes monitoring responsible for drift/anomaly detection,
  not primary action.
- **Feedback does not authorize change.** *Agentic AI for Engineers* Ch. 11 and
  *AI Engineering* Ch. 10 require feedback provenance, diversity, latency,
  evaluation, and a reviewed path to modification. This matches Watchtower
  signal → CASTLE gate → bounded owner test → measured result.
- **Safety should match stakes.** *Agentic AI for Engineers* Ch. 8 and 13
  distinguishes synchronous approval, human-on-the-loop supervision, sampled
  review, and retrospective audit. Watchtower can remain read-only while CASTLE
  applies the consequence/approval gate.
- **Separation has a real cost.** Monitoring adds latency, storage, compute,
  dashboards, and operational overhead. The boundary is justified only if it
  stays small: evidence pointer, affected assumption, consequence/test, review
  trigger—no copied research or parallel project management.
- **No activated source argues that sensing must own sequencing.** The strongest
  contrary pressure is interface overhead, not a need to merge authority.

**Evidence-only close on Watchtower vs. CASTLE:** the batch supports keeping
Watchtower separately observable and non-acting, with a narrow typed handoff
into CASTLE. CASTLE owns prioritization, gating, and proof status; the owning
wiki retains evidence; Chris owns the decision. This corroborates Section 5's
Option B and the archived `Untitled.md` independent lock, but it is not the approval
verdict.

### 8.5 Implementation consequences before any move

1. Test the ten-role classifier on real ambiguous fixtures and require an
   explicit abstain/escalate result.
2. Build the scanner against the three July 24 failure fixtures: dead Physics
   path, noncanonical Python syllabus copy, and missing/restored Wiki Shared
   Layer anchor/register.
3. Require pre-move impact inventory, checkpoint, compatibility map, rollback,
   and fresh-session acceptance.
4. Add `register:` only after structural and behavioral validation rules are
   defined; do not create parallel machine-only instruction copies.
5. Keep Watchtower separate during the migration trial. Test its handoff
   contract; reconsider placement only if measured interface overhead exceeds
   the independence benefit.

---

## 9. Migration, Validation, Value, and Reversal Gate

The meta-layer is implemented before any physical relocation. Every structural
change must pass the same sequence:

1. **Inventory:** produce a deterministic read-only impact report for paths,
   anchors, boot references, navigation, and runtime consumers.
2. **Checkpoint:** preserve the pre-change state and record the exact proposed
   old-to-new mapping.
3. **Human approval:** Chris approves the target, scope, and rollback trigger.
4. **Bounded migration:** make the smallest reversible change, never modify
   immutable `raw\` evidence, and archive rather than delete.
5. **Acceptance:** run the audit from a fresh session, verify the owning wiki
   and CASTLE/Watchtower handoff, and record benefit evidence.

The machine-learning evidence adds operational requirements: stable IDs,
versioned interfaces, explicit neutral/abstain states, dependency-aware
outputs, human and heuristic baselines, measurable checkpoints, and
reproducible fresh-session tests. A move that cannot show those properties is
not ready for execution. If the measured interface cost exceeds the benefit,
reverse the bounded change using the checkpoint and retain the evidence in
`99-ARCHIVE\`.

---

## Critical Files for Implementation (later, separately approved)

- `C:\Users\chris\.ROOT\00-BRAIN\WHERE_IT_GOES.md` — where Section 3's rule gets inserted above the existing Decision Tree (line 41).
- `C:\Users\chris\.ROOT\00-BRAIN\AGENT.md` — where File Safety rule #3 gets the `path_reference_audit.py` completion clause added.
- `C:\Users\chris\.ROOT\00-BRAIN\CASTLE\OPERATIONS.md` — where the Session Close checklist gets the move/archive audit step added; its existing authority chain and standing rules are otherwise reused as-is.
- `C:\Users\chris\.ROOT\00-BRAIN\scripts\frontmatter_audit.py` — the convention template (baseline file, `--strict`, `--json`) `path_reference_audit.py` should follow exactly.
- `C:\Users\chris\.ROOT\00-BRAIN\scripts\validate_boot_chain.py` and `wiki_lint.py` — the two existing near-miss scripts whose narrower scope defines exactly what the new script must cover that they don't.
- `C:\Users\chris\.ROOT\00-BRAIN\WHERE_IT_GOES.md` Metadata Standard — where Section 7.1's `register: ai-directive` / `register: human-context` property would be added, if Chris approves it.
- `path_reference_audit.py`'s spec (Section 4) — where Section 7.4's anchor/register-regression check would extend the tool's scope, if approved.

The 2026-07-24 implementation packet records the approved meta-layer work and
the deferred physical-migration gate:
`00-BRAIN\Session_Logs\System Update Log\2026-07-24_ROOT_ARCHITECTURE_UPDATE\SESSION_INDEX.md`.
