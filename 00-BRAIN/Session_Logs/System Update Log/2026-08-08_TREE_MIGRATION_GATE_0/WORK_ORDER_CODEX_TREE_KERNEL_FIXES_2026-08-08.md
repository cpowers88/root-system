---
type: work-order
timeline: now
status: completed-b1-b6-plus-pattern-hardening
tags: [tree, codex, gate-0, kernel-fixes]
created: 2026-08-08
owner: Codex
---

# Work Order — `.tree` Kernel Fixes

**To Codex, from Chris.** This is a work order, not a discussion document. The
decisions in Part A are settled — do not reopen them. Execute Part B in order.
Part C is out of scope and owned by Claude.

Full reasoning and verification method: `CLAUDE_REVIEW_TREE_V1_KERNEL_2026-08-08.md`
in this folder. Read it for context, but this file is the instruction.

**The reconciliation table from step 4 of the conversation packet is waived.**
Chris has decided the open items directly. Proceed to execution.

---

## Part A — Settled. Do not reopen.

| # | Decision |
|---|---|
| A1 | Vault path is `C:\Users\chris\.tree`. Obsidian is the human view; Markdown is canonical; Python validates and assembles. |
| A2 | `water/` = intake, outside material before classification. `leaves/` = testing, projects, deliverables. Siblings, never nested. |
| A3 | `journal/my_log/` is **readable by AI** — Chris's deliberate observational feed. `journal/private/` is **never read, never indexed, never summarized**. This is a split, not a blanket exclusion. |
| A4 | `branches/` has three peers: `school/`, `craft/`, `life/`. `craft` = business + technology through a value lens. `life` = the personal lens (family, money, home, personal). One tree, three branches. This closes the July 26 split question. |
| A5 | Course folders use the **course code** (`PHYS2211/`). The readable name lives in frontmatter. |
| A6 | Retrieval **assembles, never answers**. No embeddings in V1. |
| A7 | `.tree` wikis **point at `.ROOT`'s `raw/` as read-only evidence**. No evidence is copied. Evidence moves only at a dated capability transfer. |
| A8 | `.ROOT` remains canonical for every existing fact until a dated per-capability transfer. `.ROOT\00-BRAIN\NOW.md` owns Chris's active state. |
| A9 | The wiki interface is **three namespaced files**, not five. See B6. |
| A10 | `treeq` is a **controlling-context resolver, not a search tool**. See B4. |

### A10 rationale, because it is the largest change

Chris drives this from a CLI agent that already has ripgrep, file reads, and glob.
Verified comparison: ripgrep for `torque` across `.tree` returns *no files found* —
the correct answer, one call. `treeq ask` for the same question returned six
governance files and reported nothing missing.

A search command is therefore redundant and worse than what is installed. What an
agent cannot do alone is know what it is **required** to load: the controlling
instruction a question never mentions. A student asking about torque will never
grep their way to PHYS 2211's academic-integrity boundary. That is the tool's job.

Content search is delegated to ripgrep, explicitly, in the contract.

---

## Part B — Execute in this order

Do not begin B7 until B1–B6 are complete and validated.

### B1 — Strip the `00-turnk` references

The folder does not exist. Verified: recursive search for `*turnk*` across `.tree`
returns nothing; `treeq validate` prints no warning because the path is absent.
It existed as `00-TRUNK`, was misspelled, and Chris deleted it.

**The archive-move approval is withdrawn. Do not execute it.**

Remove all four references:

- `00-trunk/ai_os/runtime/treeq.py` lines 105–107 (the hardcoded warning)
- `README.md` — "Current gate" paragraph
- `00-trunk/STATE.md` — **Blocker**
- `00-trunk/STATE.md` — **Next exact action**

**Acceptance:** no occurrence of `turnk` anywhere in `.tree`; `validate` still
exits 0.

### B2 — Replace the frontmatter parser — *highest priority*

`treeq.py` `read_page()` (lines 57–63) is a hand-rolled YAML reader. It skips
indented lines and splits on the first colon.

Verified failure: a page whose `tags:` is written in block form — **the format
Obsidian's Properties editor writes by default** — parses to `'tags': ''`.
Silently empty. No error. `validate` still passes.

This means the moment Chris edits a property in Obsidian, the resolver stops
seeing it and nothing reports the loss. Under B4 this becomes fatal rather than
cosmetic, because metadata resolution becomes the tool's entire job.

**Do one of:**

1. Use a real YAML parser (`PyYAML` / `python-frontmatter`), **or**
2. If a dependency is unacceptable under local-first: forbid block-style lists in
   `PAGE_CONTRACT.md` **and** make `validate` **error** on any indented
   frontmatter line.

Silent skipping is the one option that cannot remain.

**Acceptance:** a page with block-style `tags:` either parses correctly or fails
validation loudly. It must not pass silently.

### B3 — Scope `STATE.md`

`SYSTEM.md` currently says both *"`00-trunk/STATE.md` is the only owner of what is
active now"* and *".ROOT remains canonical for 100% of existing facts."* Both
cannot hold. `.ROOT\00-BRAIN\NOW.md` owns active state today, and `.tree`'s
STATE.md became a fourth surface claiming it — the same failure class logged three
times already this month.

- Rewrite `STATE.md` to own **only the state of building `.tree`**. Not Chris's
  active work, not the semester, not learner state.
- Add an explicit line naming `.ROOT\00-BRAIN\NOW.md` as the owner of Chris's
  active state until a dated capability transfer.
- Correct the `SYSTEM.md` sentence so the two statements no longer conflict.

**Acceptance:** a fresh session reading `STATE.md` cannot mistake it for the
current-work record.

### B4 — Rewrite `RETRIEVAL_CONTRACT.md` around context resolution

Current acceptance criterion #10 — *"a missing answer is reported as missing, not
invented"* — fails on first use. Verified: `ask "what does my physics wiki say
about torque"` returned 6 files, `"missing": []`, exit 0, matching on the word
*wiki* inside the governance contracts. `missing` populates only when `ranked` is
empty (`treeq.py:166`), so with any common word present the branch is unreachable.

**New command surface:**

| Command | Job |
|---|---|
| `treeq check` | Validation. Unchanged. |
| `treeq wiki <ID>` | Emit the wiki's controlling context: local AI contract, current learner state, proof gate, integrity boundary, page inventory. **The pre-session command.** Not a search. |
| `treeq ask "<q>"` | Resolve the question to its **owning wiki**, then behave as `treeq wiki`. No owning wiki → **nonzero exit, named**. |

**Required behavior:**

- Scope resolution to a wiki happens **before** any page ranking.
- A minimum score threshold exists. Below it, nothing is returned.
- "No wiki owns this" is a **first-class successful outcome** with a nonzero exit
  code — during a semester it is the most useful answer available, because it says
  what to write next.
- Content search is delegated to ripgrep. State this in the contract.
- Most of the current `ask()` scorer can be deleted.

**Acceptance test, and it is the one that matters:**

> `treeq wiki PHYS2211` returns the academic-integrity boundary and the current
> learner frontier **without the question mentioning either**.

Plus: `ask` on a subject no wiki owns exits nonzero and names the gap.

### B5 — Implement the privacy split

The kernel closes all of `journal/`. That predates decision A3.

- `ROOT.md` Law 5 — rewrite for the split. `my_log/` readable; `private/`
  absolute, no exception, no unlock clause.
- `SYSTEM.md` ownership table — one row each.
- `treeq.py` `EXCLUDED_DIRS` — exclude `journal/private/` by **path**, not by
  directory name. Name-matching would exclude any folder called `private`
  anywhere, and would not distinguish the two children.
- `.gitignore` — ignore `journal/private/` only. Note that `my_log/` currently has
  no version history and no recovery path under the blanket ignore.
- Remove the `88-JOURNAL/` line. That folder has never existed in `.tree`.

**Acceptance:** `treeq` can read a file in `my_log/` and cannot reach
`journal/private/` by any command or flag.

### B6 — Contract and template repairs

**Add to `PAGE_CONTRACT.md`:** a required `summary` field. One sentence, under 25
words, stands alone with no context. Reason: the resolver currently emits a path
and a score, and a human reading that packet cannot tell why a file was selected
without opening it.

**Add to `WIKI_CONTRACT.md`:** a required **"Does not own"** section on every wiki
index — what a reader might expect to find there but will find elsewhere, each
with a link. This is how someone who guessed wrong reaches the right wiki in one
hop. `.ROOT` invented this independently in
`03-WIKIS\EDUCATION\wiki\pre-semester-coverage-plan.md` and it has proved out.

**Reduce the wiki interface to three namespaced files.** `.ROOT` runs five per
wiki (`README` + `HOW_TO_USE` + `OPERATIONS` + `CLAUDE` + `AGENTS`), which is
forty governance files across eight wikis. Namespacing also removes the
duplicate-basename problem at the source instead of warning about it.

| File | Replaces | Owns |
|---|---|---|
| `<ID>.md` | README + HOW_TO_USE + index | Human entrance, charter, owns / does not own |
| `<ID>-ai.md` | CLAUDE + AGENTS + OPERATIONS | Local AI contract: load order, boundary, proof rule, integrity stop line |
| `<ID>-state.md` | current-position | Sole learner-truth authority for that wiki |

**Unfence the templates.** They currently wrap the template inside a
```` ```markdown ```` block, so Obsidian's Templates plugin cannot insert them —
they document a template rather than being one. Make each template file *be* the
template. Then point Obsidian's Templates plugin at
`00-trunk/ai_os/templates/`.

**Also fix:**

- `type` is unenumerated. Enumerate the permitted values and validate them.
  `treeq`'s state filter currently hardcodes `{state, plan, flags, tracker,
  guide}`; `flags` and `tracker` exist in no contract and no file.
- `created` is required by `PAGE_CONTRACT` but absent from `REQUIRED_FIELDS`.
- `LINK_RE` validates only `[](path)`. Add `[[wikilink]]` resolution, or state
  plainly in the contract that wikilinks are unvalidated.
- `SYSTEM.md`'s ownership table lists `00-trunk/branches/`, which does not exist.
- Set `PYTHONDONTWRITEBYTECODE` or move the runtime; `__pycache__` is being
  written inside the canonical tree.

### B7 — Stop

Do not build `branches/`. Do not create course folders. Do not create `craft/` or
`life/`. Do not pre-build empty domains — this is Codex's own rule and it is
correct.

Report completion of B1–B6 with the validator output.

---

## Part C — Out of scope for Codex

Claude is building these from `.ROOT` in parallel. **Do not create, modify, or
scaffold anything under `00-trunk/branches/`.**

- The full PHYS 2211 Fall 2026 semester mapped as physics↔calculus links, built
  from `.ROOT\03-WIKIS\PHYSICS\templates\calculus-link-template.md`.
- The CSE 1321 / Python wiki governance, continuing the progression already
  running in `.ROOT`.

**Collision rule:** Codex owns `ROOT.md`, `SYSTEM.md`, `AI_CONTRACT.md`,
`README.md`, `AGENTS.md`, `CLAUDE.md`, `treeq.ps1`, and everything under
`00-trunk/ai_os/` and `00-trunk/wiki/`. Claude owns everything under
`00-trunk/branches/`. Neither writes into the other's area without saying so
first.

---

## Part D — Standing constraints

- **Nothing migrates from `.ROOT`.** Evidence is referenced read-only, never
  copied. `.ROOT` stays live and canonical.
- **Do not push `.tree`.** Chris is holding the first push deliberately. `.ROOT`
  was pushed 2026-08-08 and is current.
- **KSU begins August 24.** Sixteen days. `.tree` must carry a real semester load
  or `.ROOT` carries Fall 2026 and `.tree` resumes after the semester starts.
- **The gate that decides it:** by Sunday night, does `treeq wiki PHYS2211` give
  Chris something better than opening `.ROOT\03-WIKIS\PHYSICS\` and reading
  `current-position.md`? If not, `.tree` waits. That test needs B1–B6 done and
  Part C content in place to be answerable at all.

---

*Prepared by Claude Code, 2026-08-08, at Chris's direction. Authority is Chris's.
Nothing here authorizes a push, a migration, a deletion, or a device connection.*

---

## Codex execution return — B1–B6 complete

**Executed:** 2026-08-08  
**Result:** PASS  
**Stop:** B7 enforced; `00-trunk/branches/` remains absent and untouched.

### Outcome by work-order item

| Item | Result |
|---|---|
| B1 — stale scaffold references | Removed all four `00-turnk` references. No archive action was attempted. A vault-wide `rg` search, respecting the private ignore boundary, returns no occurrence. |
| B2 — YAML parser | Replaced the hand parser with `yaml.safe_load`; added explicit PyYAML dependency declaration, required-field/type/schema checks, ISO creation-date validation, block-list support, and loud YAML failures. |
| B3 — state scope | `STATE.md` now owns only `.tree` build/operating state and points explicitly to `.ROOT\00-BRAIN\NOW.md` as Chris's active-state owner until dated transfer. `SYSTEM.md` matches. |
| B4 — resolver | Replaced body lexical ranking with `check`, exact `wiki <ID>`, and metadata-only ownership `ask`. Unknown ownership returns `NO_WIKI_OWNER` and exit 3; ambiguity returns nonzero; page bodies cannot manufacture ownership. |
| B5 — privacy | Law, ownership table, loader behavior, and ignore policy now distinguish AI-readable `journal/my_log/` from absolute-private `journal/private/`. Traversal prunes the exact private path before descent; arbitrary declared paths cannot cross it. |
| B6 — contracts/templates | Added required summaries, enumerated types, required `created`, typed lists, Markdown-link and wikilink checks, duplicate active-basename and wiki-ID errors, three namespaced interfaces, insertable unfenced templates, Obsidian template-folder configuration, and bytecode suppression. |

### Acceptance evidence

```text
17 deterministic tests: PASS
treeq check: Checked 16 Markdown files, 12 stable IDs,
             and 4 insertion templates. Exit 0.
treeq validate compatibility alias: exit 0.
treeq ask "what does my physics wiki say about torque":
  NO_WIKI_OWNER, exit 3.
turnk search: no match.
00-trunk/branches exists: false.
tests/__pycache__ exists after test run: false.
git diff --check: exit 0.
```

The fixtures cover Obsidian block YAML, malformed YAML, wrong list types,
required `created`, type enumeration, Markdown links, wikilinks, code-span link
literals, broken links, duplicate basenames, readable `my_log`, pruned `private`,
declared-path privacy escape, exact wiki packets, metadata-only ownership,
unknown ownership, ambiguous ownership, and unprompted integrity/frontier/proof.

### Files and boundaries

- Updated only Codex-owned kernel files named in Part C's collision rule plus
  `.gitignore`, `.obsidian/templates.json`, `.tree/00-trunk/STATE.md`, and this
  work-order return.
- Added `00-trunk/ai_os/runtime/requirements.txt` and
  `00-trunk/ai_os/tests/test_treeq.py`.
- Renamed the obsolete human-guide template to `WIKI_STATE_TEMPLATE.md` and made
  all four templates directly insertable.
- Did not create or modify `00-trunk/branches/`.
- Did not read or write `.tree/journal/private/`.
- Did not migrate or copy `.ROOT` evidence.
- Did not commit, push, back up, connect a device, or delete anything.

One pre-existing ignored cache file remains at
`00-trunk/ai_os/runtime/__pycache__/treeq.cpython-314.pyc` with its prior
2026-08-08 14:13 timestamp. It was not deleted because this work order authorizes
no deletion. The launcher now uses `PYTHONDONTWRITEBYTECODE=1` and `python -B`, the
runtime sets `sys.dont_write_bytecode`, and the full test run created no test cache.

### State movement and next gate

The kernel is ready to consume a correctly formed wiki but no registered wiki
exists yet. Part C remains Claude-owned. The next integrated acceptance command is:

```powershell
.\treeq.ps1 wiki PHYS2211
```

It must return the academic-integrity boundary, learner frontier, proof gate,
semester map, evidence roots, and page inventory without the invocation naming
them. Until Part C content exists and passes that test, B7 remains the stop.

---

## Codex post-work-order return — repository-pattern hardening complete

**Authorized by Chris:** 2026-08-08  
**Result:** PASS  
**Scope:** shared kernel only; Claude-owned branch content remained read-only.

### Review verdict

| Source | Adopted | Rejected or deferred |
|---|---|---|
| Google Open Knowledge Format v0.2 | Optional structured sources, producer and verifier events, derived trust tier, lifecycle validation, absolute freshness date, stable claim-source keys | Full OKF conformance, data-catalog taxonomy, attested-computation machinery |
| `bitbonsai/mcpvault` | Strict resolved-target containment, including private and out-of-vault alias/symlink targets | General write/delete MCP surface and broad vault permissions |
| Foam | Deterministic edge counts and orphan warnings, building on existing broken/ambiguous link errors | Automatic link repair and a second editor/runtime |
| SilverBullet | Metadata-rich page catalog inside the existing wiki packet | Query DSL, database, server, or replacement human interface |

The decision and reversal path are recorded in
`C:\Users\chris\.tree\00-trunk\wiki\adr-002-governed-knowledge-metadata.md`.

### Files changed

- `00-trunk/ai_os/contracts/PAGE_CONTRACT.md`
- `00-trunk/ai_os/contracts/RETRIEVAL_CONTRACT.md`
- `00-trunk/ai_os/templates/PAGE_TEMPLATE.md`
- `00-trunk/ai_os/runtime/treeq.py`
- `00-trunk/ai_os/tests/test_treeq.py`
- `00-trunk/wiki/adr-001-obsidian-markdown.md`
- `00-trunk/wiki/adr-002-governed-knowledge-metadata.md` (new)
- `00-trunk/wiki/WIKI_INDEX.md`
- `00-trunk/STATE.md`
- this governed work-order return

No file under `00-trunk/branches/`, `journal/private/`, `journal/my_log/`,
`water/`, `.ROOT\88-JOURNAL\`, or any `.ROOT\...\raw\` folder was modified.

### Validation evidence

```text
22 executed tests: PASS
1 platform-dependent real-symlink fixture: SKIPPED because native Windows denied
  symlink creation (23 fixtures total)
resolved private/out-of-vault target fixture: PASS
treeq check: 25 Markdown files, 21 stable IDs, 4 insertion templates,
  49 graph edges, 0 orphan pages; exit 0
treeq wiki PHYS2211: exit 0; original controlling fields preserved; page catalog added
treeq wiki CSE1321: exit 0
git diff --check: exit 0 (existing LF/CRLF warning on .gitignore only)
```

### State movement

The separately owned PHYS2211 and CSE1321 branches appeared during this session
and both packets pass technically. `00-trunk/STATE.md` and `WIKI_INDEX.md` now
reflect that live reality. Gate 0 is no longer blocked by missing branch content;
its remaining gate is Chris's value verdict on the PHYS2211 launch packet.

### Boundaries and residual risk

- No install, dependency change, database, embedding index, MCP service, commit,
  push, backup, device connection, migration, deletion, or archive occurred.
- Because the entire `.tree` kernel remains untracked, Git cannot provide a
  file-level pre-change diff or rollback until Chris authorizes the first commit.
  The changes are small and reversible per ADR-002, but this is the principal
  residual recovery risk.
- The real Windows symlink integration case still needs a run on a machine/session
  permitted to create symlinks; the strict-resolution behavior itself has a
  deterministic passing fixture.
