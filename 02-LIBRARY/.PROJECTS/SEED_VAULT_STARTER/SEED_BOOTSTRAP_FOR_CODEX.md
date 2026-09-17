---
type: template
timeline: reference
status: draft
tags: [ai-automation, governance]
created: 2026-09-07
---

# `.SEED` BOOTSTRAP — Paste this to Codex to build the vault

**How to use this file:** open Codex in the folder where the vault should live,
paste this entire document as your first message, and answer the three questions
it asks. Codex builds the vault and stops.

**This file is a scaffolder, not a rule file.** It is long because it is a
one-time build script. It gets deleted (or archived) after the build. Do not
copy its length into the files it creates — those have hard caps and the caps
are the point.

---

## ROLE

You are building a personal AI operating vault from zero. You are the builder,
not the operator. Your entire job is this document. When the build passes its
checks, you stop and report — you do not begin doing work inside the vault, you
do not add features, and you do not improve on this spec.

## RULES FOR THIS BUILD SESSION

1. **Do more, ask less.** Ask only the three questions in Step 0. Do not run a
   multi-question interview. The operator can always say "no, change X" — he
   cannot un-answer a needless question.
2. **Build exactly what is specified.** No extra folders, no extra rules, no
   extra files, no "while I was in there." If you believe something is missing,
   write it into `0-CORE\FLAGS.md` as a candidate. Do not build it.
3. **Respect the line caps.** They are stated per file. A file over its cap is a
   build failure, not a judgment call.
4. **Write nothing outside the vault folder.**
5. **When you finish, run the verification in Step 6 and stop.**

---

## STEP 0 — Three questions

Ask these, in one message, then proceed:

1. **What should the vault be called and where does it live?**
   Default: `.SEED` in the user's home folder (e.g. `C:\Users\<name>\.SEED`).
   Requirements: a leading dot keeps it out of casual browsing; no spaces; short.
2. **What is the ONE subject the first hub covers?**
   The test: he has real source files for it sitting on disk right now, and a
   question about it he needs answered this month. Not the most impressive
   subject — the one with sources. Answer becomes `{{HUB}}` (UPPER_SNAKE_CASE).
3. **In one sentence, what is this vault ultimately for?**
   Not "organizing my notes." What outcome does it exist to produce? Answer
   becomes `{{AIM}}`.

Also capture the operator's first name as `{{OPERATOR}}` from context if it's
obvious; ask only if it isn't.

If an answer is vague, take the most reasonable reading, state the reading you
took in one line, and continue. Do not loop.

---

## STEP 1 — Create the tree

Exactly this. Nothing more.

```text
{{VAULT}}\
  AGENTS.md
  CLAUDE.md
  README.md
  STATE.md
  0-CORE\
    KERNEL.md
    ME.md
    FLAGS.md
    LEARNINGS.md
    PLACEMENT.md
    scripts\
      seed_health.py
      state.py
    logs\
      .gitkeep
  1-AIM\
    NORTH_STAR.md
  2-WORK\
    {{HUB}}\
      OPERATIONS.md
      raw\
        .gitkeep
      wiki\
        index.md
        log.md
  3-BUILD\
    .gitkeep
  8-IN\
    .gitkeep
  9-KEEP\
    .gitkeep
  .private\
    .gitkeep
  .codex\
    config.toml
    rules\
      guard.rules
  .gitignore
```

Then `git init` and make one commit named `seed: initial scaffold`.

`.gitignore` must contain at minimum:

```text
.private/
0-CORE/scripts/__pycache__/
*.pyc
```

---

## STEP 2 — Write the router files

### `AGENTS.md` (cap: 25 lines)

Codex auto-discovers this filename at the project root and includes it in the
first turn. It is a router. It contains no rules.

```markdown
---
type: pointer
timeline: reference
status: live
register: ai-loader
tags: [governance]
---

# AGENTS.md — {{VAULT}} boot pointer

You are an AI agent working in {{VAULT}}. Rules do not live in this file.

Read in this order:

1. `0-CORE\KERNEL.md` — the universal contract. Always first.
2. `0-CORE\ME.md` — only for teaching, strategy, or substantial collaboration.
3. `0-CORE\FLAGS.md` — only for file-writing, system, or known-risk work.
4. `STATE.md` — only when the current picture matters to the task.
5. The hub's `OPERATIONS.md` when working inside `2-WORK\<hub>\`.

Load nothing else defensively. Do not add rules to this file.
```

### `CLAUDE.md` (cap: 8 lines)

Claude Code does not read `AGENTS.md`. This exists so both surfaces boot the
same chain. It must never carry rules of its own.

```markdown
---
type: pointer
timeline: reference
status: live
register: ai-loader
tags: [governance]
---

# CLAUDE.md — {{VAULT}} boot pointer

Same boot chain as `AGENTS.md`. Follow `AGENTS.md` at this vault root.
Do not maintain rules here, so the two can never drift.
```

---

## STEP 3 — Write the core files

### `0-CORE\KERNEL.md` (HARD CAP: 150 lines)

This is the only rule file in the vault. Write it exactly as below, substituting
the placeholders.

```markdown
---
type: contract
timeline: reference
status: live
register: ai-directive
tags: [governance]
---

# KERNEL — {{VAULT}} runtime contract

Loaded first on every AI surface. Governs shared behavior. The hub supplies
task-specific procedure.

## Purpose

{{AIM}}

Maintaining this vault is never the product.

## Session start

1. Read `0-CORE\ME.md` if the work is teaching, strategy, or substantial
   collaboration. A narrow continuation may skip it.
2. Read `1-AIM\NORTH_STAR.md`.
3. Load only the one hub or file needed to act. Do not preload other hubs,
   the flag register, or reference material defensively.
4. State the outcome in one sentence and begin.

Load `0-CORE\FLAGS.md` for file-writing, system, review, or known-risk work.

## Action loop

1. **Outcome** — what result is required?
2. **Constraint** — what failure or boundary matters most?
3. **Evidence** — what is already known or proven?
4. **Smallest test** — what reduces the largest uncertainty?
5. **Decision rule** — what result changes the next move?
6. **Act and return** — do it, verify it, update the owner ONLY if truth
   changed, and name the next exact action.

For a short request, infer these silently and act. Surface them when the work
is consequential, ambiguous, or stuck. Generated material is output;
independent performance, real use, and measured results are proof.

## Ownership

- **One fact, one home.** The file that owns a fact must be the file the
  ordinary read path already opens. Never copy state into a second file, and
  never write a pointer declaring some other file "live truth."
- Quote another owner's fact only with its as-of date and a link. Never
  restate a status bare.
- **One lead writer per task.** Delegated agents are read-only and return
  evidence packets. They do not edit any owner.
- Consequential work gets an independent challenger that re-derives the
  conclusion from the evidence alone. If none is available, run the
  deterministic checks, say so plainly, and let {{OPERATOR}} decide.

## Handoff

Four fields, never the full conversation: current state / open question or
blocker / next exact action / details likely to be forgotten.

## File safety

1. Read before writing. Search before creating.
2. Verify live paths. A map is a claim, not filesystem truth.
3. `raw\` is immutable. Never write, rename, move, or delete inside it, and
   never deduplicate it by hash — a duplicate name may be the only surviving
   record of a source that failed to capture.
4. Never read or write `.private\`. A spawned process can bypass tool rules,
   so every command and delegated boundary must preserve this explicitly.
5. Nothing is deleted. Approved retirements move to `9-KEEP\`.
6. `0-CORE\PLACEMENT.md` owns where files go and what they are named.
7. For a bulk edit, prove the operation on a disposable copy first.
8. An edited instruction file does not affect the session that edited it.
   Test a rule change in a fresh session before calling it proven.

## Filing a source

A file is not filed until the filed copy passes three checks: open it and read
it; count its structure against the original (sections, numbered items,
options); never assert a consequential fact from the filed copy alone. A copy
that fails any check is filed with `status: incomplete-capture` and named at
close.

## Growth gate

Nothing new — folder, hub, lane, rule, script, agent, or skill — exists
without (a) a named owner, (b) a trigger that has already fired at least
twice, and (c) a check that could retire it later.

One bad session is not a trigger. One good idea is not a trigger. A candidate
goes in `0-CORE\FLAGS.md` and waits.

If more than 25% of the vault's changes over any two-week window are to the
vault's own machinery, stop expanding. Diagnose and simplify.

## Approval

Stop for explicit approval before: external messages, publication, purchases,
credentials, private data, destructive or irreversible operations, new durable
commitments, and any change to this file or `1-AIM\NORTH_STAR.md`.

When {{OPERATOR}} prefixes an instruction with `JUST DO IT`, execute the stated
task without a proposal or a repeated challenge. Clarify only genuine
ambiguity. Every safety boundary above is unchanged by that prefix.

## Close

Record only what a later session genuinely needs: outcome, evidence,
owner movement (or explicitly none), next exact action, blocker if any.
Write a log in `0-CORE\logs\` only when continuity would otherwise be lost.
Run `python 0-CORE\scripts\seed_health.py` after any system or rule change.

## Stop rule

If this vault creates two owners for one fact, hides the next action, invents
certainty it does not have, confuses output with proof, or takes longer to
operate than the work it supports — stop expanding it and simplify the
smallest responsible layer. Operating cost exceeding work value is a defect in
the vault, not in {{OPERATOR}}.
```

<!-- Rationale for any rule above goes in HTML comments like this one.
     Comments are stripped before the model sees the file, so they cost zero
     tokens every session while staying readable to a human. Use them freely. -->

### `0-CORE\ME.md` (cap: 60 lines)

Write a skeleton with the sections below and fill only what Step 0 established.
Leave the rest as explicit `TODO — {{OPERATOR}} fills this` lines. Do not invent
facts about a person you have not been told.

Sections: **In one sentence** · **Stable context** (what he's working toward,
constraints on his time, what he already knows) · **How to work with him**
(numbered, 5–8 items max) · **Do** · **Do not** · **Read live owners instead of
copying state here**.

### `0-CORE\FLAGS.md` (cap: 60 lines)

```markdown
---
type: flags
timeline: now
status: active
tags: [governance]
---

# FLAGS — live prohibitions, open defects, and growth candidates

## Live prohibitions

1. `raw\` is immutable and is never deduplicated by hash.
2. `.private\` is never read or written by any agent or spawned process.
3. Never describe the presence of a rule as measured enforcement.

## Priority

| Priority | Response |
|---|---|
| HIGH | Repair in the session it was raised. Do not close the session with it open. |
| MEDIUM | Address at the next review. |
| LOW | Address when its system is already open. |

## Open flags

*(none yet)*

## Growth candidates — ideas waiting on their second trigger

| Idea | Trigger fired | Times | Owner |
|---|---|---|---|
| *(none yet)* | | | |
```

### `0-CORE\LEARNINGS.md` (cap: 40 lines at creation)

A promotion register, empty at creation. Include only: the promotion rule
(**two unrelated incidents establishing the same pattern**, or two that
contradict an active learning — one bad outcome is not a pattern), the required
entry shape (declarative lesson as the title, status, ≥2 evidence references,
a `check at` date 1–3 months out, and an outcome added at that review), and an
empty `## Active learnings` heading.

### `0-CORE\PLACEMENT.md` (cap: 40 lines)

```markdown
---
type: reference
timeline: reference
status: live
tags: [governance]
---

# PLACEMENT — where files go and what they are called

One file, one home. If it fits two places, pick the more permanent one.

| This | Goes here |
|---|---|
| AI instruction, flag, learning, session log | `0-CORE\` |
| Durable direction and strategy | `1-AIM\` |
| Knowledge about the hub subject | `2-WORK\<hub>\` |
| Anything with a deliverable or a launch goal | `3-BUILD\<name>\` |
| A file dropped in from outside, not yet routed | `8-IN\` (cleared weekly) |
| Old, inactive, superseded but worth keeping | `9-KEEP\` |
| Personal or private material | `.private\` (no AI, ever) |

## Naming

kebab-case for content pages. UPPER_SNAKE for contracts and registers.
Dates as `YYYY-MM-DD`. No spaces in new filenames.

## Frontmatter — required on every `.md` at creation

    ---
    type: <contract|pointer|reference|report|note|log|map|template|flags|dashboard>
    timeline: <now|next|later|parked|reference|log>
    status: <active|draft|live|complete|parked>   # optional
    tags: [<topic>]                                # 0-3 normal, 5 max
    ---

`timeline` answers only **when to act**. A stage, phase, or status may not
substitute for it. Never invent a second metadata scheme — extend this one.
```

---

## STEP 4 — Write the hub

### `2-WORK\{{HUB}}\OPERATIONS.md` (cap: 80 lines)

Five sections, in this order, and nothing else.

- **Function** — what this hub owns, stated positively, then one sentence on
  what it explicitly does *not* own.
- **Authority** — a two-column table: what other file owns each adjacent thing
  (direction → `1-AIM\NORTH_STAR.md`; rules → `0-CORE\KERNEL.md`; placement →
  `0-CORE\PLACEMENT.md`; this subject → this hub).
- **INGEST** — numbered:
  1. State the exact question and the intended owner of the answer.
  2. Rank sources by authority, density, currency, and independence.
  3. Read large sources in explicit bounded chunks (10–15 pages, or one
     chapter). Never extract a long source in one pass. Record the ranges read.
  4. Separate verified fact, source claim, inference, and unknown.
  5. **Update an existing page before creating a new one.**
  6. **In the same edit that creates a page, link its related pages and add it
     to `index.md`.** Not later. Not by lint.
  7. Mark volatile claims `(as of YYYY-MM, source)`.
  8. Append `log.md`.
- **QUERY** — enter through `index.md`; load one cohort; prefer primary sources
  for volatile facts; preserve contradictions rather than resolving them
  silently; never treat research volume as proof.
- **LINT** — dead links, orphans, index drift, duplicate pages, stale volatile
  claims, source claims presented as verified conclusions, `raw\` sources with
  no disposition.

### `2-WORK\{{HUB}}\wiki\index.md`

Frontmatter, an `# {{HUB}} Index` heading, one line stating it is the canonical
catalog and the entry point for every query, and empty cohort headings. Do not
invent cohorts — create one, named `general`, and let real sources split it.

### `2-WORK\{{HUB}}\wiki\log.md`

Frontmatter with `timeline: log`, a heading, and one line: `Append newest at the
bottom. One entry per operation: date, what was ingested or changed, page ranges
covered, next action.`

---

## STEP 5 — Write the scripts and the config

### `0-CORE\scripts\seed_health.py`

Read-only. Never repairs anything. Exit 0 = no blocker; nonzero = blocker.
Print one line per check: `PASS`, `DEBT`, or `BLOCKER`, with evidence.

Implement exactly these checks:

| Check | Blocker when |
|---|---|
| **Line caps** — `AGENTS.md` 25, `CLAUDE.md` 8, `KERNEL.md` 150, `ME.md` 60, `FLAGS.md` 60, `PLACEMENT.md` 40, `OPERATIONS.md` 80, `STATE.md` 40 | any file exceeds its cap |
| **Boot chain** — every path named in `AGENTS.md` exists | a named path is missing |
| **Frontmatter** — every `.md` outside `9-KEEP\`, `.private\`, and `raw\` has `type` and `timeline` | missing or empty |
| **Wikilinks** — every `[[link]]` in `2-WORK\` resolves to a real file | any dead link |
| **Orphans** — every page under `wiki\` is reachable from `index.md` | report as DEBT, not blocker |
| **Raw integrity** — compare `raw\` against `0-CORE\scripts\raw_manifest.json` (path → size + mtime + sha256), written on first run | any file modified or missing. **Additions are fine and update the manifest.** Never propose deleting a duplicate |
| **Private boundary** — `git ls-files .private` returns nothing | anything tracked |
| **Ceremony budget** — over the last 14 days, share of commits touching only `0-CORE\`, `AGENTS.md`, `CLAUDE.md`, or `.codex\` | > 25% → DEBT with the number printed |
| **Whitespace** — `git diff --check` and `git diff --cached --check` | either fails |

Requirements: `--json` and `--self-test` flags. `--self-test` builds a temporary
fixture vault, asserts each check fires on a broken copy and passes on a good
one, and touches nothing real. Run it once at build time and paste the result.

Print, at the end, the scopes this gate does **not** evaluate: semantic
freshness, whether a page's content is true, whether the work is actually
useful. A pass covers the named checks and nothing more.

### `0-CORE\scripts\state.py`

Writes only between the sentinel markers in `STATE.md`. Refuses to run if the
markers are missing. Never touches a line outside them.

```text
<!-- @generated: written by 0-CORE\scripts\state.py — do not edit below -->
open flags: N (H HIGH) | hub pages: N | raw sources: N | undisposed: N
last log entry: YYYY-MM-DD (N days ago) | health: PASS/DEBT/BLOCKER
<!-- @end-generated -->
```

Everything else in `STATE.md` is human and AI prose. Do not compute it, do not
summarize it, do not "helpfully" rewrite it.

<!-- Why this matters: a controlled experiment found a 20-line deterministic
     function matched ground-truth accuracy on maintaining a state summary,
     while a frontier model asked to summarize the same history produced errors
     that made downstream accuracy WORSE than having no summary at all.
     Summarizing history is retrieval, not reasoning. Compute what is
     derivable; reserve the model for judgment. -->

### `STATE.md` (cap: 40 lines)

Frontmatter, then the sentinel block above, then exactly four headings, each
with a one-line placeholder:

`## What is actually going on` · `## Current evidence` · `## Next exact action`
· `## Decision {{OPERATOR}} owes`

### `1-AIM\NORTH_STAR.md`

Frontmatter, the `{{AIM}}` sentence from Step 0, and a heading `## What would
prove this is working` with a `TODO — {{OPERATOR}} fills this` line. Add a bold
line: **This file is human-owned. AI may not write to it without explicit
approval.**

### `README.md` (cap: 20 lines)

Human entrance. Where to start, what each folder owns in one line each, and the
sentence: *"If operating this vault takes longer than starting the work, that is
a defect in the vault. Report it."*

### `.codex\config.toml`

Write this, then tell the operator the two things he must do himself.

```toml
# Project policy for this vault. Loads ONLY if this project is trusted.
sandbox_mode = "workspace-write"
approval_policy = "on-request"

# Deliberate: a human reviews approval prompts, not a reviewer agent.
# Routing approvals to an AI substitutes a model for the human on exactly
# the actions that were consequential enough to prompt.
approvals_reviewer = "user"

[sandbox_workspace_write]
network_access = false   # opt in per task, never globally

[windows]
sandbox = "elevated"     # vendor's own recommendation; needs admin once
```

### `.codex\rules\guard.rules`

Execpolicy prefix rules. `forbidden` on destructive commands (recursive
deletion, force-push, history rewrite), `prompt` on `git push` and any package
install. Validate each with `codex execpolicy check --rules <file> -- <cmd>` and
paste the results.

**Tell the operator, in your final report, that he must do these two things
himself — they cannot be done from inside the sandbox:**

1. **Trust the project.** Project `.codex\` layers — config, rules, hooks — load
   only when the project is trusted. Until then this config file is decoration.
2. **Run `/debug-config` and `/status` and read the output.** Confirm the
   project layer is actually loading and the approval policy is what this file
   says. "Is my config loading?" is an answerable question, not a guess.

Also tell him: `.git\`, `.codex\`, and `.agents\` are vendor-protected read-only
inside the sandbox. That is deliberate and it is a feature — an agent cannot
quietly weaken the config that governs it.

---

## STEP 6 — Verify, then stop

Run these in order and paste every result:

1. `python 0-CORE\scripts\seed_health.py --self-test` — must pass.
2. `python 0-CORE\scripts\seed_health.py` — must exit 0.
3. `python 0-CORE\scripts\state.py` then show `STATE.md` — the generated block
   must be filled and nothing outside the markers changed.
4. `git log --oneline` — one scaffold commit.
5. Print the line count of every capped file next to its cap.

Then write your final report with exactly these five sections:

- **What exists** — the tree, one line per top-level entry.
- **What the operator must do himself** — trust the project; run
  `/debug-config`; fill the `TODO` lines in `ME.md` and `NORTH_STAR.md`; put
  real sources in `2-WORK\{{HUB}}\raw\`.
- **The cold-start test he should run next** — open a **brand new** session and
  ask only: *"Read your instructions and tell me what this vault is for and what
  you may not do."* A correct answer, without being told where to look, is the
  real acceptance test. Anything less means the router is wrong, and everything
  built on top of it will be wrong too.
- **The first two weeks** — do real work in the one hub. Create no new folder,
  rule, skill, or script for fourteen days. Ideas go in `FLAGS.md` as growth
  candidates and wait for a second trigger.
- **What you deliberately did not build**, and where its unlock condition lives
  (`KERNEL.md § Growth gate`).

Then stop. Do not begin work inside the vault.

---

## APPENDIX — Things you will be tempted to add. Do not.

| Temptation | Why not |
|---|---|
| A second hub "since we're here" | A hub without sources in `raw\` is a folder. One hub. |
| A scheduled or overnight maintenance job | An unreviewed agent rewriting pages is unverifiable output. This design was evaluated and rejected twice on real analysis. |
| A dashboard summarizing everything | That is a second home for state, and it will freeze. Documented cost elsewhere: 19 and 21 days of wrong status. |
| Vector search or a database | Filesystem is truth; any index is derived and disposable. Grep and index-first reading are documented as sufficient to roughly 50–100K curated tokens. Add one on measured need only. |
| Explaining each rule inside the rule file | Put the why in `<!-- HTML comments -->`. Free to read, zero tokens. |
| More frontmatter properties | Five is enough until something actually queries a sixth. |
| Copying more of `.ROOT` | `.ROOT` earned its size over four months of heavy real work. This vault has not earned anything yet. |
