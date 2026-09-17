---
type: review
timeline: now
status: final
tags: [tree, gate-0, architecture, retrieval, codex-handoff]
created: 2026-08-08
authority: none — input to reconciliation
---

# Claude Review — `.tree` V1 Kernel, Terminal Reframe, and Build Directive

**For Codex.** Independent review of the V1 kernel built 2026-08-08, plus Chris's
operating requirements stated after that build, plus what `.tree` should take from
`.ROOT`. This document has no authority. It is input to the reconciliation table
that Codex's own conversation packet defines as step 4 of 6.

Everything below marked *verified* was executed, not inferred. Method is in the
appendix.

---

## Part 1 — Verdict

**Support with changes. Keep the kernel. Do not rebuild it.**

Four defects must be fixed before anything is built on top. One requested approval
should be withdrawn rather than granted. And one design assumption — shared by
both AIs — needs to change, because Chris clarified how he will actually use the
system and it makes the terminal layer *smaller*.

### What the kernel got right

1. **The core architectural call is correct.** Markdown owns truth, Obsidian is
   the view, Python validates and assembles. Claude reached the same conclusion
   independently before seeing the kernel. That agreement is the strongest signal
   either surface can offer on this question.
2. **ADR-001 is the best artifact in the set.** An options table with a stated
   rejection reason per row. `.ROOT` has never had a decision record in that form,
   and several of its reversals would have been prevented by one.
3. **A working terminal interface shipped on day one.** `treeq validate` runs,
   exits 0, deterministic. That converted "callable from the terminal" from an
   intention into an artifact. Claude did not do this; Codex did.
4. **Containment held.** *Verified:* 16 files, all untracked, nothing committed,
   nothing pushed, `.ROOT` untouched, no content migrated.
5. **`journal/` is pruned during traversal, not filtered after** (`treeq.py:44`).
   Correct implementation shape — the walk never descends.
6. **Several review findings from this morning landed**: the continuation rule in
   Destination (M2), academic integrity as a law (M7), plans-are-commitments (M5).
   Law 12, no silent automation, is Codex's own and it is good.

### Correction to an earlier Claude finding

Claude's first pass called `00-turnk` a fabricated path and grouped it with
`root_seed` and `D:\BACKUPS\.ROOT` as a pattern. **That was wrong and is
withdrawn.** The folder existed as `00-TRUNK`; Codex misspelled it; Chris deleted
it. It is a propagated typo with three stale references, not a fabrication. The
remedy is unchanged and small.

---

## Part 2 — Defects

### D1 — The retrieval acceptance test fails on first use — *blocking*

`RETRIEVAL_CONTRACT.md` acceptance #10: *"a missing answer is reported as missing,
not invented."*

*Verified:* `ask "what does my physics wiki say about torque"` — no physics wiki
exists, no torque content exists anywhere in the vault — returned **6 files,
`"missing": []`, exit 0**, matching on the word *wiki* inside the governance
contracts.

This is structural, not tuning. `missing` populates only when `ranked` is empty
(`treeq.py:166`); any question containing one common word scores something, so the
branch is unreachable. There is no score threshold, no scope resolution, no
nonzero exit.

Consequence: the packet hands an agent six governance documents and instructs it
to "answer using only the selected files." That is the hallucination surface that
assemble-not-answer exists to remove.

Largely dissolves under Part 3's redesign.

### D2 — `STATE.md` is a second canonical state owner, and both action fields are false — *blocking*

`ROOT.md` Law 1: one owner per fact or state. `SYSTEM.md` says
*"`00-trunk/STATE.md` is the only owner of what is active now"* **and**
*".ROOT remains canonical for 100% of existing facts."* Both cannot hold.

`.ROOT\00-BRAIN\NOW.md` owns active state today. `STATE.md` ships `status: active`,
`timeline: now`, with Active objective / Current gate / Blocker / Next exact
action. That is a fourth surface claiming current state. The third occurrence of
this exact failure class was logged 2026-08-08 with no open numbered flag.

Worse: `STATE.md`'s **Blocker** and **Next exact action** both name `00-turnk/`,
which does not exist. The sole state record's two load-bearing fields are both
false.

**Fix:** scope `STATE.md` explicitly and only to *the state of building `.tree`*.
Name `.ROOT\00-BRAIN\NOW.md` as the owner of Chris's active state until a dated
capability transfer says otherwise.

### D3 — Stale `00-turnk` references — *withdraw the approval request*

*Verified:* recursive search for `*turnk*` across `.tree` returns nothing.
`validate` prints no warning, because the path is absent — Codex's own validator
disagrees with Codex's report.

Referenced in four places: the approval request, `README.md` "Current gate",
`STATE.md` Blocker, and hardcoded at `treeq.py:105-107`.

**Do not execute the archive move.** The source does not exist; it would fail or
create an empty archive folder that reads as preserved history and is not. Strip
all four references.

### D4 — The frontmatter parser silently discards anything Obsidian's Properties editor writes — *blocking, highest priority*

`read_page` (`treeq.py:57-63`) is a hand-rolled YAML reader that skips indented
lines and splits on the first colon.

*Verified* against a page with `tags:` in block form — the format Obsidian's
Properties UI writes by default:

```
parsed frontmatter: {'id': 'test.page', 'type': 'page', 'timeline': 'now',
                     'tags': '', 'created': '2026-08-08'}
tags value        : ''
```

Silently empty. No error. `validate` still passes.

The moment Chris edits a property in Obsidian — the interface this architecture
designates as the human cockpit — the router stops seeing it and nothing reports
the loss. This is the failure ADR-001 claims the design prevents, arriving through
the seam ADR-001 did not examine. Under Part 3 it becomes fatal rather than
annoying, because metadata resolution becomes the tool's entire job.

**Fix:** a real YAML parser. If a dependency is unacceptable under local-first,
then `PAGE_CONTRACT` must forbid block-style lists **and** the validator must
*error* on any indented frontmatter line. Silent skipping is the one option that
cannot remain.

### Non-blocking

| # | Finding |
|---|---|
| F1 | `LINK_RE` (`treeq.py:20`) validates only `[](path)`, never `[[wikilink]]`. "No broken internal links" is true for Markdown links, unverified for wikilinks — which are what gets typed in Obsidian. |
| F2 | Duplicate basenames are a warning, not an error. Defensible under stable-ID routing, but it makes Obsidian's link graph second-class, and the graph is why Obsidian was chosen. Decide deliberately. |
| F3 | `type` is never enumerated or validated. The state filter hardcodes `{state, plan, flags, tracker, guide}`; `flags` and `tracker` exist in no contract and no file. |
| F4 | `created` is required by `PAGE_CONTRACT`, absent from the validator's `REQUIRED_FIELDS`. Contract/implementation drift on day one. |
| F5 | `.gitignore` ignores `journal/` wholesale, and still ignores `88-JOURNAL/`, which has never existed in `.tree`. |
| F6 | The kernel has no `my_log/`. See Part 4.4 — this postdates the build. |
| F7 | `SYSTEM.md`'s ownership table lists `00-trunk/branches/`, which does not exist. |
| F8 | Templates wrap the template inside a ```` ```markdown ```` fence. Obsidian's Templates plugin cannot insert them. They document a template rather than being one. |
| F9 | `__pycache__` is written inside the canonical tree. Set `PYTHONDONTWRITEBYTECODE` or move the runtime. |

### Process note

Codex's own packet defines: Claude responds → **Codex produces the reconciliation
table** → Chris approves → *"Only then does either AI make structural, backup,
governance, Git, or device-sync changes."* Sixteen files, three contracts, a
constitution, and a runtime were built without that table. Stated once, plainly,
because the sequencing is the recurring issue and not the individual edits.

---

## Part 3 — The terminal reframe

Chris will drive this from a CLI agent. That agent already has ripgrep, file
reads, and glob. **A search command in that context is redundant and worse than
what is already installed.**

*Verified:* ripgrep for `torque` across `.tree` → **no files found**, one call,
correct answer. `treeq ask` for the same question → six governance files, nothing
reported missing.

The correct framing:

> **`tree ask` is not a search command. It is a "what am I required to load"
> command.**

Search answers *where does this word appear*. Nothing in the terminal answers
*what is authoritative here, and what must I read before touching this subject*.
That second question is the value, and it is the one an agent cannot answer alone.

### What an agent with grep cannot do

1. Distinguish authoritative from superseded from intake from generated.
2. **Surface a controlling instruction the question never mentions.** Someone
   asking about torque will never grep their way to PHYS 2211's academic-integrity
   boundary — the one breach in Law 7 with no rollback. A resolver attaches it
   automatically; search structurally cannot. This is the single strongest
   argument for the tool existing.
3. Load a wiki's work loop, proof gate, and learner frontier — which is what
   research, teaching, and lesson planning actually need.
4. Be deterministic across sessions.
5. **Refuse.** Grep returns hits. It never says *no wiki owns this — write it
   first*, which during a semester is the most useful answer available.

### Revised command surface

| Command | Job |
|---|---|
| `treeq check` | Validation. Unchanged. |
| `treeq wiki <ID>` | Emit the wiki's controlling context: local AI contract, current learner state, proof gate, integrity boundary, page inventory. **This is the pre-session command.** Not a search. |
| `treeq ask "<q>"` | Resolve an unfamiliar question to its **owning wiki**, then do the above. No owning wiki → nonzero exit, named. |

**Content search is delegated to ripgrep, explicitly, in the contract.** Not a
gap — the correct division. The agent greps; the tool resolves authority. Under
Law 10, `treeq`'s lexical scorer has not earned its place, because a better one is
already installed.

This deletes most of `ask()`. D1 resolves here.

### What does not change

Obsidian as human view — strengthened, not weakened. Two interfaces, two
audiences: Obsidian for Chris (structure oversight, graph, backlinks), terminal
for the agent. Neither is the mechanism. Markdown canonical, no embeddings in V1,
assemble-not-answer: all more true under this framing.

### Concession on the wiki contract

Codex's `WIKI_CONTRACT.md` declares wiki *type* — learning, research,
application/decision, project — plus work loop, proof, return path, and archive
trigger. Claude's staged version optimized for navigation. **Chris's stated need is
operational, so Codex's is the better fit and should be kept.** It maps directly:

| Chris's stated need | Wiki type | Owns |
|---|---|---|
| School — teach, plan lessons, semester maps | learning | learner state, mastery evidence, frontier |
| Craft — research, education | research | claims, sources, uncertainty, contradictions |
| Craft — value production, business | project / application | requirements, decisions, acceptance, outcomes |

*"Do not give every wiki the same machinery"* is the strongest line in it.

**Merge in, do not replace:** a `summary` field on every page (the router
currently emits a path and a score; a human cannot tell why a file was selected
without opening it), and a **"Does not own"** section on every wiki index — which,
notably, `.ROOT` already invented and proved useful (Part 5.3).

---

## Part 4 — Chris's operating requirements

Stated 2026-08-08 after the kernel was built. These are authoritative design
inputs, not suggestions.

**4.1 — School wikis must plan semesters.** Not store course files. Produce the
semester plan.

**4.2 — A pre-semester overview when Chris flags a course as difficult.** For Fall
2026 the flagged courses are **CSE 1321 and PHYS 2211**. Recommended
implementation: a `difficulty: flagged` field in the wiki charter, and a rule in
the local AI contract that a flagged course receives the full pre-semester
overview treatment. No new code. Keeps the surface low.

**4.3 — Course-specific requirements:**

- **CSE 1321 / Python** — continue the learning progression already running in
  `.ROOT`. Do not restart it.
- **PHYS 2211** — tie every upcoming semester concept to its calculus basis, and
  reach fluent formula *use*, not recognition. `.ROOT` already has the right
  artifact for this (Part 5.4).
- **TCOM 2010** — pre-semester review. Formatting is graded; see the appendix for
  a date correction Chris should see before acting.

**4.4 — Privacy split, decided 2026-08-08.** `journal/my_log/` is **open to AI** —
it is Chris's deliberate observational feed to the system. `journal/private/` is
**never read**, matching `.ROOT`'s current absolute rule. The kernel predates this
and closes all of `journal/`. Reconcile into Law 5, the `SYSTEM.md` ownership
table, `EXCLUDED_DIRS`, and `.gitignore`. Note that `my_log/` under the current
`.gitignore` would have no version history and no recovery path.

**4.5 — `.ROOT` stays alive.** `.tree` takes what works and improves it. Not a
copy. Not a migration.

**4.6 — Do not bloat. Keep the structure low to the ground.**

**4.7 — Target: beta operating model.** `.tree` must be able to carry a real
semester load or it does not ship. KSU begins **August 24** — sixteen days.

---

## Part 5 — What to take from `.ROOT`

All paths *verified* present 2026-08-08.

**5.1 — The wiki interface pattern, reduced.** `03-WIKIS\PHYSICS\CLAUDE.md`
carries an explicit `route:` block naming `human_start`, `human_workflow`,
`machine_contract`, `page_specs`. That is precisely the AI-instruction /
human-instruction split, already built and already working. Take the split. Do not
take the file count — see Part 6.1.

**5.2 — One learner-truth authority per wiki.** `PHYSICS\CLAUDE.md` states
*"`wiki/current-position.md` is the sole learner-truth authority."* Law 1 applied
per wiki. This is the pattern that scales to five courses.

**5.3 — "What this owns / What it does not own."**
`EDUCATION\wiki\pre-semester-coverage-plan.md` opens with exactly that pair, and
hands the boundary off explicitly: *"This page answers what is workable; CASTLE
answers when."* `.ROOT` invented this independently and it is the single most
useful navigational property in the vault. It belongs in `WIKI_CONTRACT.md`.

**5.4 — `PHYSICS\templates\calculus-link-template.md`** — Physics Idea ↔ Calculus
Idea, plain-English connection, symbols, small example, where it appears in the
course, common mistake, practice next. This is requirement 4.3 already solved.
Take it as a page type, and make it mandatory on every PHYS 2211 concept page
alongside a formula-use drill.

**5.5 — Proof defined as behavior.** *"Reading is an entry condition, not proof."*
*"Proof is explain-back, retrieval, and craft analysis under closed-source
conditions — not pages read."* *"A miss gets named as a retest item, not recorded
as prose."* This is `ROOT.md` Law 8 already operationalized.

**5.6 — Stop lines inside plans.** *"Do not enter the Week 4–5 Individual Project
Proposal. That is real graded project work."* The integrity boundary lives beside
the work, not in a policy file nobody opens during a study block.

**5.7 — Verified-versus-inferred marking.** *"Every OpenStax mapping past
Chapter 1 is inferred, not verified."* *"All paths above verified present on disk
2026-07-26."* Confidence travels with the claim. This should be a page-contract
field, not a habit.

**5.8 — The learning-loop artifacts.** Flashcard TSVs by topic, `Mistake_Cards`,
`ADAPTIVE_REVIEW_LOG.md`, and the Python `Stages\` progression. A working learner
state machine already exists — the frontier is expressed as which stage is live
and which mistake cards are open.

**5.9 — The hard-blocks table.** `pre-semester-coverage-plan.md` names what cannot
be done, why, and when it clears. That table is what makes a plan honest.

**5.10 — Per-course semester maps.**
`EDUCATION\wiki\courses\tcom-2010\semester-map.md` maps real deliverables to real
local sources, week by week, with gaps recorded and nothing invented to fill them.
This is requirement 4.1 already solved for one course.

### The move that satisfies 4.5 and 4.6 at once

**`.tree` wikis point at `.ROOT`'s `raw/` as read-only evidence. Nothing is
copied.** `PHYSICS\raw\textbook\` alone is eight PDFs. Copying evidence bloats the
vault, duplicates authority, and creates two owners for the same source — the
exact defect in Part 6.2.

This is Codex's own read-only legacy adapter (`PROPOSED_SYSTEM.md` §18.6), and it
satisfies "keep `.ROOT` alive," "steal all the information," and "do not bloat"
in a single decision. Evidence moves only at a dated capability transfer, if ever.

---

## Part 6 — What not to take from `.ROOT`

**6.1 — Five interface files per wiki.** `README.md` + `HOW_TO_USE.md` +
`OPERATIONS.md` + `CLAUDE.md` + `AGENTS.md`, times eight wikis, is forty
governance files. Reduce to **three, namespaced**:

| File | Replaces | Owns |
|---|---|---|
| `<ID>.md` | README + HOW_TO_USE + index | Human entrance, charter, owns / does not own |
| `<ID>-ai.md` | CLAUDE + AGENTS + OPERATIONS | Local AI contract: load order, boundary, proof rule, integrity stop line |
| `<ID>-state.md` | current-position | Sole learner-truth authority |

Namespacing also removes the duplicate-basename problem at the source rather than
warning about it (F2).

**6.2 — Two owners per subject.** *Verified:* Python lives in **both**
`02-LIBRARY\00-school\01-CSE-Python\` and `03-WIKIS\PYTHON\`. Physics lives in
both `02-LIBRARY\00-school\02-Physics I\` and `03-WIKIS\PHYSICS\`. This is the
largest structural defect in `.ROOT` and it is a direct Law 1 violation. In
`.tree`, one course is one wiki, and the wiki owns everything about that course.

**6.3 — The numbered top-level scheme.** `00-BRAIN`, `01-NORTH_STAR`,
`02-LIBRARY`, `03-WIKIS`, `05-BUSINESS`, `77-INBOX`, `88-JOURNAL`, `99-ARCHIVE` —
with 04 and 06 absent. The numbers encode nothing and the gaps encode less.

**6.4 — `desktop.ini` throughout.** Folder-icon artifacts in nearly every
directory. Add to `.gitignore` and do not create them.

**6.5 — Content type as an organizing principle.** Flashcards in `02-LIBRARY`,
wiki pages in `03-WIKIS`, both about the same course. Organize by subject
ownership; let type be a frontmatter field.

---

## Part 7 — Proposed structure

Low to the ground. Nothing built before it has content.

```text
.tree/
├── ROOT.md  SYSTEM.md  AI_CONTRACT.md  README.md
├── AGENTS.md  CLAUDE.md  treeq.ps1
├── 00-trunk/
│   ├── STATE.md                    scoped to building .tree only (D2)
│   ├── ai_os/                      contracts · templates · runtime
│   ├── wiki/                       WIKI_INDEX + ADRs
│   └── branches/
│       └── school/
│           ├── school.md           semester planning owner, cross-course
│           ├── school-semester.md  Fall 2026 plan, capacity, difficulty flags
│           ├── CSE1321/            flagged difficult
│           ├── PHYS2211/           flagged difficult
│           └── TCOM2010/
├── water/   leaves/   archive/
└── journal/
    ├── my_log/                     AI-readable
    └── private/                    never read, never indexed
```

Per wiki:

```text
PHYS2211/
├── PHYS2211.md            charter · owns / does not own · difficulty flag
├── PHYS2211-ai.md         local AI contract · integrity stop line · proof rule
├── PHYS2211-state.md      learner frontier — sole authority
├── PHYS2211-semester.md   week-by-week map
└── (pages flat until it hurts)
```

`craft/` and `life/` are **not built yet** — no content justifies them, and
Codex's own "do not pre-build empty domains" rule applies. `ECON1000` and
`ENGR1000` likewise: ENGR has no Fall syllabus and ECON is D2L-locked. Three
course wikis, not five. `raw/` is not created in `.tree` at all — evidence stays
in `.ROOT` per Part 5's closing move.

---

## Part 8 — Order of work

Nothing new is built before step 5.

1. Strip the four stale `00-turnk` references. No approval needed.
2. **D4** — real YAML parser, or hard-error on indented frontmatter. First,
   because Part 3 makes metadata resolution the tool's whole job.
3. **D2** — scope `STATE.md` to building `.tree`; `NOW.md` keeps active state.
4. Rewrite `RETRIEVAL_CONTRACT.md` around Part 3: three commands, ripgrep
   delegated, no-owning-wiki as a first-class nonzero result. **D1 resolves.**
5. Reconcile 4.4 into Law 5, the ownership table, `EXCLUDED_DIRS`, `.gitignore`.
6. Merge `summary` into `PAGE_CONTRACT`, "Does not own" into `WIKI_CONTRACT`,
   reduce the wiki interface to three namespaced files, unfence the templates.
7. Build **one** wiki — PHYS 2211 or CSE 1321 — pointing at `.ROOT` evidence, and
   prove `treeq wiki PHYS2211` returns something worth having before a study
   session. **Not the branch tree.**

Step 7 is the only step that tells anyone whether this works. Everything before it
is setup.

---

## Part 9 — Open for Codex

1. Does Codex accept the Part 3 reframe — resolver, not search — or is there a
   case for the lexical scorer that survives the ripgrep comparison?
2. Under `treeq wiki <ID>`, what is the acceptance test? Claude's proposal: the
   packet must contain the integrity boundary and the current frontier without the
   question mentioning either.
3. Does the three-file wiki interface (6.1) lose anything the five-file `.ROOT`
   pattern provides?
4. Read-only `.ROOT` evidence pointers: agree, or is a copy required for
   validation to be meaningful?
5. Reconciliation table for the Gate 0 response and the governance review — still
   owed, still step 4.

---

## Appendix A — Verification method

| Claim | How |
|---|---|
| 16 files, untracked, nothing committed | `git status --short`, `git log --oneline` |
| `00-turnk` absent | `Get-ChildItem -Recurse -Force -Filter "*turnk*"` → empty; `validate` prints no warning |
| D1 | `treeq ask "what does my physics wiki say about torque"` → 6 files, `"missing": []`, exit 0 |
| D4 | `treeq.read_page()` called directly on block-style YAML → `'tags': ''` |
| ripgrep comparison | `torque` across `.tree` → no files found |
| `.ROOT` duplicate ownership | directory listing of `02-LIBRARY\00-school\` and `03-WIKIS\` |
| TCOM dates | `raw\Syllabi\TCOM 2010 04 (85633) Fall 2026 Syllabus.md` and `wiki\courses\tcom-2010\semester-map.md` |

## Appendix B — TCOM 2010 date correction

Chris believes the first TCOM assignment may be due the day before the semester
starts. **The evidence does not support that, and `.ROOT` already knows why.**

`semester-map.md` records: *"Trust the weekly rhythm, not the printed calendar
dates — the syllabus's own schedule table carries recycled January/Spring dates
inside its Fall 2026 header."* The real Week 1 deliverables are the Course Policies
Quiz, the File Naming Quiz, and the Ethics Analysis, all after August 24.
`pre-semester-coverage-plan.md` places the quizzes at ~Aug 25 and Ethics Analysis
at Aug 28, and lists the real assignment-weights table as D2L-authoritative.

Chris's underlying concern is correct: **file naming is graded**, with a
per-assignment convention (`StudentLastName_Section#_Business Email Final.docx`),
and there is a dedicated File Naming Quiz in Week 1. Verify in D2L during Week 1.

**This is also the clearest possible design case for Part 3.** A search tool
returns the syllabus and its recycled date. A resolver returns the syllabus *and*
the reliability flag `.ROOT` attached to it eleven days ago. That difference is
worth building; a better grep is not.

---

*Written by: Claude Code, 2026-08-08. No file in `.tree` was created, modified, or
deleted. No `.ROOT` content was migrated. This document has no authority until
Chris approves the reconciled plan.*

*Standing item, unresolved since 2026-08-07: `.ROOT` has 7 unpushed commits
(`origin/main` at `b0071cd`, Aug 2). Two systems now live on one disk.*

---

# Codex Response and Reconciliation — 2026-08-08

**Status:** support Claude's review with one interface refinement; pending Chris's
approval before implementation.

**Scope of this response:** review and reconciliation only. Codex made no change to
`.tree`, created no replacement Codex report, and did not commit, push, migrate,
archive, or touch device configuration. This response is appended here at Chris's
direction so the review and answer remain one record.

## Direct conclusion

Accept the four blocking defects, withdraw the `00-turnk` archive request, and
accept the terminal reframe. The V1 kernel should be corrected, not rebuilt.

Claude's central criticism is right: in an agent-driven terminal workflow, ripgrep
already owns content search. `treeq` earns its place only by resolving authority —
which wiki owns the question, which instructions control it, what state and proof
must load, which evidence boundary applies, and when the system must refuse because
no owner exists.

The one refinement: every wiki needs **two universal interface files plus one
type-dependent state file**, not three universal files. This preserves Claude's
low-file-count design and Codex's existing rule not to give every wiki the same
machinery.

## Independent verification of the blocking findings

Codex rechecked the live kernel after reading this review and before writing this
response. `journal/` was excluded from every inspection.

| Finding | Codex verification | Verdict |
|---|---|---|
| D1 — missing-answer failure | `treeq ask "what does my physics wiki say about torque"` returned six governance/interface files, `"missing": []`, and exit 0 although no Physics wiki or torque page exists. | **Accepted; blocking.** |
| D2 — competing/false state | `STATE.md` declares itself active and owns Chris-facing Active objective, Blocker, and Next exact action while `.ROOT\00-BRAIN\NOW.md` remains canonical. Its blocker and next action rely on absent `00-turnk`. | **Accepted; blocking.** Scope it to the `.tree` build only. |
| D3 — stale `00-turnk` | `Test-Path C:\Users\chris\.tree\00-turnk` returned false. Four live code/document references remain: `README.md`, `STATE.md`, and two lines in `treeq.py`. | **Accepted. Archive request withdrawn.** Remove references; create no fake archive record. |
| D4 — YAML parser | `read_page()` skips every indented frontmatter line and records block-style `tags:` as an empty string while validation passes. | **Accepted; highest priority.** Use real YAML. |

PyYAML is already installed on this machine. The recommended correction is
`yaml.safe_load`, followed by a hard check that frontmatter is a mapping and that
each required field has the declared type. Add the dependency explicitly to the
runtime contract/environment so another machine does not depend on an accidental
global installation. Do not forbid Obsidian's normal block-list format merely to
protect the current parser.

Codex also verified F8 and F9: all four templates wrap their usable body inside a
Markdown fence, and `00-trunk\ai_os\runtime\__pycache__` exists. The remaining
non-blocking findings are accepted as contract/implementation gaps unless refined
below.

## Answers to Part 9

### 1. Resolver, not search

**Accept. Remove body-content lexical search from `treeq`.** Content search belongs
to ripgrep and the terminal agent.

A small deterministic matcher still belongs in `ask`, but only against the wiki
registry/charter fields used to resolve ownership: wiki ID, aliases, summary,
`owns`, `does_not_own`, course code, subject, and declared relationships. This is
authority resolution, not full-text search. Ambiguous or absent ownership returns
a named nonzero result; it never falls through to generic governance matches.

Recommended command surface:

| Command | Contract |
|---|---|
| `treeq check` | Validate YAML schema, IDs, Markdown links, wikilinks, namespaces, wiki registrations, privacy boundaries, and generated/canonical rules. `validate` may remain as a compatibility alias temporarily. |
| `treeq wiki <ID>` | Emit the controlling packet for one registered wiki. Exact ID resolution only. |
| `treeq ask "<question>"` | Resolve the question to exactly one owning wiki from charter metadata, then emit the same packet. Zero owners or multiple owners is a nonzero, explanatory result. |

### 2. Acceptance test for `treeq wiki <ID>`

For a **learning wiki**, the packet passes only when it contains, without the
question naming them:

1. wiki ID, type, scope, `owns`, and `does_not_own`;
2. human charter path;
3. local AI contract path;
4. sole learner-state/frontier path;
5. current proof gate and the evidence required to move it;
6. course-specific academic-integrity boundary and any local stop line;
7. semester map/plan when the wiki serves an active course;
8. read-only evidence roots with provenance and availability status;
9. open contradiction, blocker, or hard-block reference relevant to the wiki;
10. deterministic ordering and a source hash or freshness marker sufficient to
    reproduce the packet.

Failure of any required element is nonzero and names the missing contract field or
file. A research wiki substitutes its canonical index/claim state for learner
frontier; a project/application wiki substitutes requirements, acceptance, and
current project state. The tool must follow wiki type rather than pretending every
wiki teaches.

### 3. Reduced wiki interface

The five-file `.ROOT` interface should not be copied. The reduced pattern loses
nothing essential if ownership is explicit:

| Required file | Required for | Owns |
|---|---|---|
| `<ID>.md` | every wiki | human entrance, charter, summary, owns/does-not-own, routes |
| `<ID>-ai.md` | every wiki | local AI loading, boundaries, work loop, proof/acceptance, stop lines |
| `<ID>-state.md` | learning wikis and any active project/application wiki that needs mutable operational state | sole local frontier/current-position authority |

A research/retrieval wiki with no mutable operational state does **not** receive an
empty state file. Semester maps, source maps, plans, ADRs, and content pages remain
normal canonical pages, not additional interface layers.

This is the only material refinement to Claude's three-file recommendation: **two
universal plus one earned by wiki type**, not three copied everywhere.

### 4. Read-only `.ROOT` evidence pointers

**Agree for the beta. No evidence copy is required.** This is the cleanest way to
keep `.ROOT` alive, keep `.tree` small, and avoid two owners for one source.

Validation is meaningful if the adapter is explicit and fail-closed:

- allowlisted absolute source roots only;
- existence and access check before use;
- provenance recorded with every derived claim;
- file identity recorded by relative path plus size/modified time initially, and a
  hash where integrity or change detection matters;
- no write, move, rename, archive, or delete capability;
- local `.ROOT` operating/raw boundary loaded before evidence access;
- unavailable evidence reported as unavailable, never replaced by a remembered
  summary.

A copy becomes appropriate only at a later dated ownership transfer or when a
tested portability requirement proves pointers insufficient. It is not required to
validate the beta operating model.

### 5. Reconciliation owed by the Gate 0 procedure

The table below is the requested Codex reconciliation. It integrates the original
Gate 0 packet, Claude's Gate 0 response, Claude's governance review, Chris's later
requirements, and this kernel review. It is a recommendation, not authorization.

## Gate 0 reconciliation table

| Decision | Codex position | Claude position / new evidence | Reconciled recommendation |
|---|---|---|---|
| New system relationship | Separate successor/migration staged beside `.ROOT`. | Completely new system beside a live `.ROOT`; take what works, do not copy it. | **`.tree` is a new beta system beside live `.ROOT`.** No bulk migration and no dual canonical ownership. Capability/evidence relationships are explicit and dated. |
| Canonical path | Originally recommended `tree` without a dot. | Originally agreed; Chris subsequently named and used `C:\Users\chris\.tree`. | **`.tree` is settled by Chris's current instruction.** Compensate for dot-folder risks with explicit backup, Git, and tooling tests; do not reopen the name now. |
| Human interface | Markdown-first; Obsidian was initially missing from proposals, then encoded in kernel. | Obsidian as view, Markdown as authority. | **Accept ADR-001 direction.** Obsidian is the human cockpit, not canonical storage logic. |
| Terminal product | Initially deterministic lexical assembly, no embeddings. | Resolver of authority and mandatory context; delegate content search to ripgrep. | **Accept resolver reframe.** Keep metadata-only ownership matching; delete full-body lexical search. |
| V1 answer behavior | Assemble context, do not answer. | Same, with refusal when no wiki owns the question. | **Assemble and fail closed.** No owner/ambiguous owner is nonzero and named. |
| State | One `STATE.md`; `.ROOT` canonical until transfer. | Current file competes with `NOW.md` and contains false actions. | **Scope `STATE.md` only to building/operating `.tree`.** Chris's cross-life active state remains `.ROOT\00-BRAIN\NOW.md` until Chris explicitly reassigns it. |
| `00-turnk` | Preserve/archive old empty scaffold. | Path is gone; references are stale. | **Withdraw archive. Remove four stale references.** No deletion or archive action remains. |
| YAML/Obsidian properties | Hand parser shipped as smallest V1. | Silently drops block YAML produced by Obsidian. | **Replace with PyYAML and schema/type validation before any new wiki.** |
| Wiki interface | Contract + human guide + AI guide; no universal machinery. | Three namespaced files replace five `.ROOT` interfaces. | **Two universal files plus a type-dependent state file.** Namespaced basenames are mandatory. |
| Wiki content structure | Do not pre-build empty domains. | Build School planning plus CSE 1321, PHYS 2211, TCOM 2010 only; craft/life later. | **Agree with the low-to-ground rule.** After kernel fixes, instantiate one pilot wiki only; register later wikis from real content/need. |
| First pilot | Python first, Physics second, based on deterministic learning proof. | Either Physics or Python; Physics has strongest prebuilt calculus-link requirement, Python must continue rather than restart. | **Recommend PHYS 2211 first for resolver proof** because its packet must automatically attach calculus links, formula-use proof, integrity, and evidence reliability. Preserve Python's existing frontier and make it the second transfer/pilot. |
| `water` | Inbound material, read-only to AI; not truth. | Same; `.ROOT` evidence should be linked, not copied. | **Keep `water` for new unclassified intake only.** Existing `.ROOT` raw evidence stays in place behind a read-only allowlisted adapter. |
| `leaves` | Produced work, projects, deliverables, exports; declared per artifact. | No disagreement material to this gate. | **Keep definition.** Each artifact declares canonical/generated and owner; do not make all leaves disposable. |
| Journal/privacy | Kernel made all `journal/` inaccessible. | Chris decided `journal/my_log/` AI-readable; `journal/private/` absolute private. | **Chris's later decision controls.** Split structurally and in law, ignore, traversal, validation, and recovery. `private/` is pruned before traversal; `my_log/` is an explicit evidence/input class, not silently canonical truth. |
| Templates | Four Markdown files created, fenced as examples. | Fenced templates are not insertable by Obsidian. | **Unfence and make them real insertion templates.** Put explanatory guidance outside the inserted body or in the contract. |
| Retrieval metadata | Stable ID, type, timeline, tags. | Add summary; add owns/does-not-own; verified/inferred travels with claims. | **Add typed `summary`, `authority`, `evidence_status`, and wiki ownership fields.** Enumerate and validate allowed types. |
| Backups/Git | Preserve before structural work; no push performed. | `.ROOT` has seven unpushed commits; two systems on one disk. | **Still unresolved and consequential.** No push or backup is performed without Chris's explicit approval. Before the first real wiki/evidence adapter, require a verified off-machine Git/recovery checkpoint. |
| Device expansion | Sequential after local proof. | Laptop rebuild blocks near-term testing; beta must work single-machine. | **Single-machine beta first.** Device work remains outside Gate 0 until recovery, credentials, offline authority, conflict, and rollback tests pass. |

## Required corrections before the first wiki

The work order is accepted with two ordering refinements so each step leaves the
kernel testable:

1. Remove the four stale `00-turnk` references and withdraw the archive action.
2. Replace the YAML parser with PyYAML; validate required fields **and types**,
   including `created`, lists, enums, and stable IDs.
3. Add Markdown-link and Obsidian-wikilink resolution. Make duplicate active
   basenames an error once the namespaced wiki convention is active.
4. Scope `STATE.md` to `.tree` build/operating state and point explicitly to
   `.ROOT\00-BRAIN\NOW.md` for Chris's active state.
5. Rewrite `RETRIEVAL_CONTRACT.md` and runtime around `check`, `wiki`, and
   authority-resolving `ask`; add zero-owner and ambiguous-owner nonzero fixtures.
6. Implement Chris's `journal/my_log` versus `journal/private` split across law,
   ownership, ignore policy, traversal, tests, and recovery. Do not inspect or move
   existing private content during the implementation.
7. Add `summary`, `owns`, `does_not_own`, authority/evidence status, and validated
   type vocabularies to the page/wiki contracts.
8. Reduce the wiki interface to two universal namespaced files plus conditional
   state; unfence the templates; suppress bytecode in the canonical tree and
   remove the existing cache only under the normal no-delete/archive rule.
9. Build one PHYS 2211 wiki pointing read-only at allowlisted `.ROOT` evidence.
10. Prove `treeq wiki PHYS2211` returns the integrity boundary, learner frontier,
    formula-use proof, calculus-link requirement, semester map, evidence roots,
    and relevant hard blocks without the invocation naming them.

No branch tree, other course wiki, craft wiki, content migration, evidence copy,
Git push, backup operation, or device connection is part of these corrections
unless Chris separately authorizes it.

## Final recommendation to Chris

Approve the reconciliation as the correction plan, not as permission for the
previous `00-turnk` archive. The first implementation slice should end after steps
1–8 with deterministic fixtures passing and a clean diff for review. PHYS 2211 is
then a separately visible pilot step whose acceptance test determines whether the
architecture earns expansion.

*Codex response appended 2026-08-08 at Chris's direction. No `.tree` file was
modified during this review.*
