---
type: report
timeline: reference
status: draft
tags: [ai-automation, system-evolution, governance]
created: 2026-09-07
---

# `.SEED` — Building a `.ROOT`-Class AI Operating Vault That Cannot Get Fat

**Audience:** Chris, to hand to a friend who is starting from zero with similar
goals and similar learning attributes.
**Scope:** the architecture, the oversight model, the anti-bloat controls, the
Codex build sequence, and what `.ROOT` should take back if this proves out.
**Evidence base:** `.ROOT`'s own `03-WIKIS\AI_AUTOMATION_SYSTEMS` wiki — four
months of ingested primary research plus `.ROOT`'s own measured failures. Every
claim below that carries a number came from a file in this vault, not from
generic advice. Sources are listed at the end.

---

## 1. The one recommendation

**Build the friend a two-file kernel, one hub, and a growth gate — and forbid
everything else until a trigger fires.**

Not a smaller `.ROOT`. A `.ROOT`-*shaped* seed whose every folder, lane, agent,
and rule has to be *earned by an event that already happened*. The architecture
Chris described to him is correct: a thin oversight layer that mostly routes,
sub-agents that do the work in their own context, and a folder structure aimed
at the brain's goals. What kills that design in month two is not the design —
it's that nothing in it says **no**. `.ROOT` earned its size honestly over
four months of intense real work; a copy of `.ROOT`'s *current* size handed to a
beginner on day one is all of the maintenance cost with none of the evidence
that justified it.

So the deliverable is not "a vault." It is a vault **plus a gate**, and the gate
is the part that makes the difference.

---

## 2. Why `.ROOT` works — the six load-bearing mechanisms

These are the parts worth copying verbatim. Each has been independently
re-derived by other builders, which is the strongest available evidence that
they are structural and not personal taste.

### 2.1 Immutable `raw/` → agent-owned `wiki/` → `index.md` + `log.md`

The Karpathy LLM-wiki pattern. Three operations only: **ingest** (read a source,
update existing pages, update the index, append the log), **query** (enter
through the index, drill in, cite), **lint** (find contradictions, orphans,
stale claims). Knowledge compounds instead of being re-derived every session.

This shape has now been arrived at independently by at least six separate
implementations tracked in the AIAS wiki (Karpathy's gist, Rezvani's llm-wiki
skill, claude-obsidian, obsidian-second-brain, Garry Tan's GBrain, and
superdesigndev's loopany), plus `.ROOT` itself, which built it before reading
any of them. That is convergent validation, not fashion.

**Construction analogy:** `raw/` is the as-built survey — you never mark it up.
`wiki/` is the working set of drawings you revise. `index.md` is the sheet
index. `log.md` is the daily field log. A crew that keeps those four straight
can hand off to another crew; one that doesn't, can't.

### 2.2 Thin harness, fat skills

loopany's framing of Garry Tan's formulation: the always-loaded core stays
deliberately tiny (loopany's is ~2,000 lines of pure file I/O and validation);
all judgment, process, and prompts live in on-demand markdown that gets read
only when needed. `.ROOT` runs this as `AGENT.md` (kernel) + skill files +
per-hub `OPERATIONS.md`.

The mechanical reason this matters, from Anthropic's own docs: **every subagent
gets its own fresh copy of the root instruction file.** A heavy root file isn't
taxed once — it's taxed again by every fork you spawn. And the <200-line
discipline is a *quality* lever, not a capacity workaround: adherence degrades
as always-loaded files grow, independent of whether they'd technically fit in a
1M-token window. "There's room" was never the constraint being managed.

### 2.3 One owner per fact, and the read path must equal the authority path

This is `.ROOT`'s hardest-won lesson, recorded as learning **L-2026-01** after
three separate incidents:

- A copied "learner stages" table went stale because the weekly reconciliation
  it depended on never ran.
- A CASTLE map's copied Python row sat wrong for **19 days**.
- An ownership loop — three files each naming another as authority — froze four
  core maps for a month and measured **21 days wrong** on one subject.

The lesson, stated exactly: *state may live in exactly one file per object, and
that file must be the one the daily read path already touches.* A second table
that copies state and a pointer that declares some *other* file "live truth" are
the same defect in different costumes. Both create a home no ordinary session
opens, so it rots silently and its staleness is found by accident.

And the corollary that cost the most: **a "single home" declaration is not
enough on its own.** Flag #103's file *declared* itself the only home while a
sibling contradicted it. The declaration has to be paired with a mechanical
staleness check on the declared home, or it is just prose.

### 2.4 Non-shared-context agents coordinating through a shared filesystem

Chat, Codex, and Claude Code inherit none of each other's conversation. They
coordinate through the vault (data plane) plus handoff files and a flag register
(control plane). Chapter 10 of the AI Agent Book names the required handoff
package: task, confirmed facts and constraints, references to artifacts —
**deliberately excluding the full trajectory as noise.** `.ROOT`'s four-field
handoff ritual (current state / open question or blocker / next exact action /
details likely to be forgotten) is a line-for-line match, designed without
reference to that book.

Also from Ch. 10, and worth stating plainly to the friend: **the strongest model
and the most careful prompt go to the planner, not spread evenly across every
agent.** A weak planner is more damaging than a weak executor. Concentrate
planning authority; distribute execution.

### 2.5 Eyes, not hands — verification capacity gates progression

The agentic maturity ladder finding: progression is gated by **verification
capacity, not capability.** Companies that added agent capability faster than
they added the ability to check it got stuck with capabilities they couldn't
deploy. `.ROOT` sits at Level 1 solid / Level 2 emerging and deliberately
refuses Levels 4–5.

Concretely, this is why `.ROOT` evaluated and **rejected twice** the single most
seductive feature in this space: the overnight autonomous maintenance loop
(obsidian-second-brain's "nightly reconcile/synthesize/heal", GBrain's "dream
cycle"). An unreviewed agent rewriting pages while you sleep is unverifiable
output. Contradiction *flagging* was adopted; contradiction *auto-resolution*
was not.

Tell the friend this before he asks for it, because he will ask for it in week
three. It is the most attractive wrong turn available.

### 2.6 Safety mechanisms are not self-modifiable

Chapter 8's rule: an agent must not modify the validators, test cases, release
thresholds, audit logs, or backups that approve its own updates — because "an
agent can disguise regression as progress simply by lowering a test threshold or
deleting failing cases."

`.ROOT` holds the *spirit* of this (raw immutability, human approval on
governance) but has a real gap: `00-BRAIN\scripts\` is not raw-protected, so an
ordinary session edit could weaken `root_health.py` without extra approval. This
already happened once in miniature — an out-of-role settings key introduced
during a cleanup, caught and reverted the same session **by catch, not by
design.** The friend's vault can close this on day one, cheaply, because Codex
treats `.codex/` as vendor-protected read-only inside its own sandbox.

---

## 3. Why `.ROOT` got heavy — the seven failure modes to design out

This is the more useful half of the report. Each of these is a real, dated,
measured `.ROOT` incident. Copy the fixes, not the scars.

| # | Failure | Evidence in `.ROOT` | Design fix in `.SEED` |
|---|---|---|---|
| 1 | **Narrated state** — the AI summarizes "where things are" each session instead of computing it | Flag #91 (a retired flag kept showing as open across two dashboards, reproduced live days after the real fix); the Aug 5–6 evening-reading bug (primed the wrong day off a stale label) | `state.py` computes the derivable half of the dashboard between sentinel markers; prose is human/judgment only |
| 2 | **Governance eats the product** | The Aug 6 System-Cost Diagnostic: **94% of two weeks' commits touched governance/session machinery**, not the work the vault exists to support | The Ceremony Budget (§6.3): system-maintenance commits capped as a share of total; breaching it is a stop condition |
| 3 | **Instruction bloat** | The Sept 6 rewrite cut twelve control files from **20,439 to 6,258 words (−69.4%)** with no loss of function — meaning ~14,000 words had been loading into sessions for months, doing nothing | Hard line caps written into the kernel itself, enforced by `seed_health.py`, not by good intentions |
| 4 | **Two files claiming to be truth** | L-2026-01, three instances, 19 and 21 days wrong | One home per object + a mechanical freshness check on the declared home |
| 5 | **Verifying a capture on existence, not content** | Seven aid defects in eleven days (Aug 19–29), five introduced *at filing* — a file was verified on "it exists / it has the right name" and then trusted on its content | The three-check filing rule: open and read it, count its structure against the original, never assert a graded/consequential fact from the filed copy alone |
| 6 | **Cleanup that destroys evidence** | Flag #97: seven files in one `raw/` folder held only two articles between them. That was **capture loss, not duplication** — the clipper pre-filled names from the wrong browser tab. Five sources exist as a filename and nothing else. A hash-based dedupe would have deleted the only surviving record that they were ever attempted | `raw/` is immutable and never deduped by hash — written into the kernel as a prohibition, not a preference |
| 7 | **An AI reviewer substituted for the human on exactly the consequential actions** | `.ROOT`'s global Codex config was found set to `approvals_reviewer = "auto_review"` — an AI guardian, not Chris, reviewing approval prompts, in tension with the kernel's own human-approval rule, and invisible until a docs read surfaced it | `.SEED` ships `approvals_reviewer = "user"` explicitly, with a comment saying why |

There is an eighth, softer one worth naming out loud because it is the risk on
the far side of *any* well-built system. Ch. 10 calls it **cognitive
surrender**: "the designer grows accustomed to the loop doing the work,
gradually stops thinking and reviewing independently, and allows quality to
spiral downward." The remedy is that the human stays the engineer of the loop,
not the person who presses go. For a friend who is learning as he builds, this
is the actual thing to protect.

---

## 4. The `.SEED` architecture

### 4.1 The tree — day one, complete

```text
.SEED\
  AGENTS.md                  <- 25-line router. Codex auto-discovers this name.
  CLAUDE.md                  <- same router, 3 lines, points to AGENTS.md
  README.md                  <- human entrance, 20 lines
  STATE.md                   <- current picture. Half generated, half written.
  0-CORE\
    KERNEL.md                <- the ONE rule file. Hard cap 150 lines.
    ME.md                    <- who the operator is, how to work with him. 60 lines.
    FLAGS.md                 <- open defects + live prohibitions. Starts near-empty.
    LEARNINGS.md             <- promoted patterns only. Starts empty. Threshold-gated.
    PLACEMENT.md             <- where files go and what they're named. 40 lines.
    scripts\
      seed_health.py         <- the deterministic gate
      state.py               <- computes STATE.md's generated block
    logs\                    <- session handoffs, only when continuity would be lost
  1-AIM\
    NORTH_STAR.md            <- durable direction. Human-owned. AI may not write.
  2-WORK\
    <one hub>\               <- see 4.3
  3-BUILD\                   <- projects with a deliverable
  8-IN\                      <- intake. Untrusted until routed. Cleared weekly.
  9-KEEP\                    <- archive. Nothing is deleted, ever.
  .private\                  <- AI never reads or writes. Enforced, not requested.
  .codex\
    config.toml              <- sandbox, approvals, permissions
    rules\guard.rules        <- execpolicy: forbid destructive commands
```

Nine top-level entries. `.ROOT` has nine sections and eight hubs; it got there
over four months of heavy use and the friend should not start there.

Two deliberate omissions the friend will want and should not get yet: **a second
lane**, and **a review cockpit.** `.ROOT`'s three-entrance design (TUTOR / VALUE
/ CASTLE) is correct *for `.ROOT`*, which serves a full course load plus a
business plus a research program. A vault with one hub and no evidence yet does
not have two lanes to separate or a portfolio to review. Both are in the growth
gate (§6) with the exact trigger that unlocks them.

### 4.2 The context budget — the number that actually governs everything

| File | When loaded | Line cap | Why |
|---|---|---|---|
| `AGENTS.md` | every session, first turn | **25** | Codex reads this at project level automatically; a fork re-pays it |
| `0-CORE\KERNEL.md` | every session | **150** | the whole rule set. If it needs more, something else is wrong |
| `0-CORE\ME.md` | teaching/strategy/substantial work | **60** | who the operator is; skipped on narrow continuations |
| `0-CORE\FLAGS.md` | file-writing, system, or risk work | **60** | conditional, not defensive |
| `STATE.md` | when "what's going on" matters | **40** | half of it is machine-written |
| hub `OPERATIONS.md` | only inside that hub | **80** | the local contract |
| **Always-loaded total** | | **~175 lines** | |

`.ROOT`'s equivalent always-loaded payload after its September rewrite is
roughly 6,258 words across twelve control files. `.SEED` starts at about a
tenth of that. It is allowed to grow — but only through §6.

One free trick from Anthropic's docs, worth using from day one: **HTML comments
are stripped before injection.** `<!-- why this rule exists, reviewed 2026-11 -->`
costs zero tokens in every session but stays visible to a human opening the file
and to an agent that deliberately Reads it. All rationale goes in comments. Only
the rule itself goes in prose.

### 4.3 One hub, and how a hub is shaped

```text
2-WORK\<HUB_NAME>\
  OPERATIONS.md            <- the machine contract for this hub (80 lines)
  raw\                     <- immutable. Human puts sources here. AI never writes.
  wiki\
    index.md               <- the canonical catalog. Entry point for every query.
    log.md                 <- append-only operational history
    <cohort>\*.md          <- the pages
```

The hub's `OPERATIONS.md` carries five sections and nothing else: **Function**
(what this hub owns, and explicitly what it does not), **Authority** (a table
of what other file owns each adjacent thing), **INGEST** (the numbered
procedure), **QUERY** (the numbered procedure), **LINT** (the checklist). That
is the exact shape of `.ROOT`'s hub contracts and it holds up.

**Which hub first?** Whichever one has real sources sitting on his disk right
now and a question he actually needs answered this month. Not the one that
sounds most impressive. A hub with no `raw/` is a folder, not a hub.

### 4.4 Two rules that go in at write time, not at lint time

`.ROOT` learned this one from ByteDance's OpenViking work and hasn't fully
adopted it yet — the friend should start with it:

> A filesystem knowledge base only works if links and indexes are **actively
> maintained between files**. If knowledge is split into a pile of independent
> text files without cross-references, the agent has almost no way to navigate —
> and models vary in whether they do this by default, so **the knowledge-writing
> prompt must explicitly require it.**

So: **every new wiki page links its related existing pages and updates the
parent index in the same edit that creates it.** Not caught later by lint —
lint catching an orphan is a different and much weaker guarantee.

And second, from the same lesson set: **classify the change before overwriting.**
A newer statement is one of three things — a temporal update, a
context-dependent variant, or a true contradiction. Only the third is a
conflict. Flag it on the page (`supersedes / contradicts X — source, date`)
rather than quietly replacing it. Volatile claims (prices, versions, adoption
stats) carry `(as of YYYY-MM, source)`.

---

## 5. The oversight model — what Chris actually described, made concrete

Chris's framing was right: the top instruction layer should be *mostly a
router*, and the real work should happen in isolated sub-agents whose context
never pollutes the main thread. Here is that as a contract.

### 5.1 Four tiers, and what each is allowed to say

| Tier | File | Says | Never says |
|---|---|---|---|
| **Router** | `AGENTS.md` | which file to read next, in what order | any rule |
| **Kernel** | `KERNEL.md` | universal behavior, safety, the action loop, the growth gate | anything true of only one hub |
| **Lane / hub** | `OPERATIONS.md` | this hub's procedure and authority table | anything the kernel already said |
| **Skill** | `SKILL.md` | one repeatable procedure, on demand | anything not in that procedure |

The one test that keeps this clean: **if a rule appears in two tiers, delete the
lower copy and point up.** `.ROOT`'s September rewrite was, in essence, three
days of applying exactly that test and recovering 69% of the payload.

### 5.2 Sub-agent lanes — the coordination contract

```text
LEAD (one per task)          reads, decides, and is the ONLY writer
  ├── researcher (read-only) returns an evidence packet; may not edit any owner
  ├── researcher (read-only) same
  └── challenger (read-only) re-derives the conclusion from evidence alone,
                             ignoring the lead's reasoning trace
```

Four rules, all of which come from named `.ROOT` incidents:

1. **One lead writer per live task.** Delegated agents are read-only and return
   packets. This is the fix for the semantic-conflict failure mode, where three
   separate sessions independently re-derived the same weekly plan on one Sunday
   because none of them owned it.
2. **Handoff carries four fields, never the trajectory.** Current state / open
   question or blocker / next exact action / details likely to be forgotten.
3. **Consequential work gets an independent challenger by default.** Agent
   failures are *Byzantine, not crash* — a session doesn't stop and announce an
   error, it keeps producing plausible-looking output while quietly wrong. The
   only defense that catches that is a second agent re-checking whether the
   evidence and the conclusion agree, without seeing the reasoning. If no
   challenger is available, run the deterministic checks, **say so**, and let
   the human decide whether that's sufficient.
4. **Isolation over compression.** When exploration will generate a lot of
   context that won't be needed again, fork it to a sub-agent and take back only
   the summary. This is not a cost trick; it's the reason the main thread stays
   coherent over a long session.

### 5.3 Latent vs. deterministic — the line that decides what becomes a script

loopany's framing, and the cleanest heuristic in this whole body of research:

> Judgment, synthesis, and pattern-matching belong to the model. Queries,
> validation, and atomic writes belong to code. **Forcing one into the other is
> the most common architecture mistake.**

The status-bar experiment is the empirical version. A 20-line regex function
matched ground-truth accuracy on maintaining a state summary; a frontier model
asked to summarize the same history in one pass produced errors and made
downstream accuracy **worse than having no status bar at all** — because
summarizing a long history is retrieval, not reasoning, so asking a model to do
it relocates the problem instead of solving it.

**This is the single most actionable finding in the vault**, and it is the
mechanism behind failure #1 in §3. So `.SEED` ships `state.py` on day one:

```text
STATE.md
  <!-- @generated: do not edit below; written by 0-CORE\scripts\state.py -->
  open flags: 2 (0 HIGH)      hub pages: 14      raw sources undisposed: 1
  last log entry: 2026-09-06  days since: 1      index/tree mismatch: none
  <!-- @end-generated -->

  ## What's actually going on          <- human + AI prose. Judgment only.
  ## Next exact action
  ## Decision the operator owes
```

The sentinel-marker pattern (`@generated` / `@user` blocks) is itself borrowed
from claude-obsidian: it lets a regeneration pass touch only its own region and
never a human-edited one, in the same file. Two findings, one mechanism.

---

## 6. The growth gate — the part that makes this different from `.ROOT`

### 6.1 The rule

> Nothing new — folder, lane, hub, rule, script, agent, or skill — comes into
> existence without **(a)** a named owner, **(b)** a trigger that has *already
> fired* at least twice, and **(c)** a check that could retire it later.
>
> One bad session is not a trigger. One good idea is not a trigger.

This is loopany's reflect-loop threshold discipline, generalized from beliefs to
structure. Their exact numbers, worth copying: a pattern needs **≥3 tasks with
the same class of outcome**; refuting an existing belief needs **≥2 contradicting
tasks**; a repeatedly-dismissed signal needs **≥3 dismissals over ≥2 weeks**.
Below threshold, it explicitly is not a pattern — *"1 bad outcome → not a
pattern."*

### 6.2 The pre-written unlock table

Give the friend the triggers up front so he isn't guessing, and so a "no" today
doesn't feel arbitrary:

| Want | Unlocks when | Not before |
|---|---|---|
| A second hub | 3+ sources that the existing hub's `index.md` cannot file without mixing two subjects, **and** a question the current hub answered wrong because of that mixing | 3 weeks of use |
| A second lane (separate entrance) | The same session repeatedly loads two disjoint sets of files, measured across 5+ sessions, **and** the operator has named a real conflict between them | A second hub exists |
| A review cockpit / CASTLE equivalent | 3+ open decisions that no single owner file can sequence | Two lanes exist |
| A new skill file | The same multi-step procedure has been typed out by hand 3 times | — |
| A new script | A check has been performed manually 3 times and the result was wrong once | — |
| A scheduled/background job | Never, at this maturity level. See §2.5 | — |
| A new metadata property | The existing five cannot express it *and* something will query it | — |

### 6.3 The ceremony budget

The hardest number in this report, and the one worth putting in the kernel:

> If, over any two-week window, **more than 25% of the vault's changes are to
> the vault's own machinery**, the system is eating the work. Stop expanding.
> Diagnose the runtime and simplify the smallest responsible layer.

`.ROOT` measured **94%** in one such window. That is what this number exists to
prevent, and it is measurable with one `git log` command, which means
`seed_health.py` can report it.

### 6.4 The stop rule, copied nearly verbatim from `.ROOT` because it is good

> If the vault creates two owners for one fact, hides the next action, invents
> certainty it doesn't have, confuses output with proof, or consumes more effort
> than the work it supports — stop expanding it.

Add one line `.ROOT` learned later and should have had earlier: **if operating
the vault takes longer than starting the work, that is a defect in the vault,
not in the operator.** Report it as a flag.

---

## 7. Deterministic guards — the Codex-specific layer

Prose rules are advisory. These are enforced by the tool, and they are cheap to
set up on day one. All of this is from the official Codex configuration docs as
captured in `.ROOT`'s wiki (July 2026 — **re-verify against current docs before
implementing**, this is a fast-moving surface).

**Configuration precedence**, highest first: CLI flags → project
`.codex/config.toml` (root to cwd, closest wins) → `--profile` files → user
`~/.codex/config.toml` → system → defaults.

**The trust gate is load-bearing.** Project-scoped `.codex/` layers — config,
hooks, and rules — load *only when the project is trusted*
(`projects.<path>.trust_level = "trusted"` in the user config). So a checked-in
policy that isn't armed by a trust grant is decoration. Conversely, every stale
trust grant arms that directory's checked-in layers, which is its own hygiene
item.

Project config **cannot** override machine-owned keys (auth, providers, base
URL, telemetry, notify) — they're ignored with a startup warning. A malicious
repo can't redirect credentials via checked-in config.

**Set these:**

| Setting | Value | Why |
|---|---|---|
| `sandbox_mode` | `workspace-write` | writes inside the vault, nowhere else |
| network | **off** (the default in `workspace-write`) | opt in per-task, never globally |
| `approval_policy` | `on-request` | the "Auto" preset |
| `approvals_reviewer` | **`user`** | *not* `auto_review`. See §3, failure #7 |
| `[windows] sandbox` | `elevated` | the vendor's own recommendation; `/setup-default-sandbox` performs it |
| permission profile (beta) | `raw/` → `read`, `.private/` → `deny` | `deny` blocks reads, not just writes |
| `.codex/rules/guard.rules` | forbid `Remove-Item`, `rm -rf`, `git push --force`; prompt on `git push` | prefix rules with `allow` / `prompt` / `forbidden` |

Three vendor facts worth knowing precisely:

- **`.git/`, `.codex/`, and `.agents/` are vendor-protected read-only inside the
  writable workspace**, recursively. Codex cannot edit its own project config
  from inside its sandbox. That is the mechanism that closes §2.6's gap — put
  the health-gate baseline where the agent can't quietly relax it.
- **Verification commands exist**: `/status` (active model, approval policy,
  writable roots), `/debug-config` (layer order, on/off state, policy sources),
  `codex doctor`. The question "is my instruction file actually loading?" is
  answerable, not a guess. Have the friend run `/debug-config` on day one and
  *look at it*, so he never has to wonder later.
- **`execpolicy` rules are a guard, not a wall** — `--ignore-rules` exists for
  exec runs. Treat them as the second layer under the sandbox, not the first.

And two mechanics that will confuse him at exactly the wrong moment if nobody
warns him:

1. **`AGENTS.md` is what Codex reads; `CLAUDE.md` is what Claude Code reads.**
   Neither reads the other's file. Keep both at root; make the second one three
   lines pointing at the first, and never let rules live in both.
2. **An instruction-file edit does not apply to the session that made it.**
   Root-level instruction files are read once at launch and held in memory. The
   editing session keeps operating on the pre-edit version — the change is safely
   on disk and behaviorally absent until `/clear`, `/compact`, or a restart. So a
   session that both changes a rule and wants to *verify* the new behavior must
   start fresh. `.ROOT` burned real hours on this before it was written down.

---

## 8. The build sequence

Five phases, each with a gate. The friend does not proceed to the next phase
because he feels ready; he proceeds because the gate passed.

### Phase 0 — Scaffold (one sitting, ~60–90 minutes)

Hand Codex the companion file, `SEED_BOOTSTRAP_FOR_CODEX.md`. It creates the
tree, writes the kernel files, writes `seed_health.py` and `state.py`, writes
the `.codex` config, and stops.

**Gate:** `python 0-CORE\scripts\seed_health.py` exits 0. `/debug-config` shows
the project layer loading. A **fresh** Codex session, given only "read your
instructions and tell me what this vault is for and what you may not do,"
answers correctly without being told where to look.

That last check is the real one. If a cold session can't route itself, nothing
built on top of it will work.

### Phase 1 — First real work, zero new structure (2 weeks)

Do actual work in the one hub. Ingest real sources. Answer real questions.
**Create no new folder, rule, skill, or script for fourteen days**, no matter how
obviously good the idea is. Write the ideas into `FLAGS.md` as candidates
instead; most of them will look different in two weeks, and the ones that don't
will have fired their trigger twice by then.

**Gate:** at least 5 sessions logged, at least 3 real sources ingested, and the
answer to "did the vault help, or did I spend the session maintaining it?" is
honestly the former.

### Phase 2 — First earned growth (weeks 3–6)

Now run the unlock table (§6.2). Whatever triggered, build **one** of them. Not
two.

**Gate:** health script still passes; ceremony budget under 25%; a cold session
still routes correctly *after* the addition. That last one catches the most
common regression — a new file that quietly makes the router ambiguous.

### Phase 3 — Deterministic guards (week 6+, or immediately on first near-miss)

Permission profile, execpolicy rules, `state.py` extended to compute whatever
turned out to be the thing that kept going stale.

**Trigger to pull this forward:** the first time the agent does something the
prose rules said it shouldn't. Then the rule wasn't the fix — it was never the
fix — and the guard is.

### Phase 4 — The reflect loop (month 3+, optional, and genuinely optional)

Only after there's enough history for thresholds to mean anything. The mechanic,
copied from loopany because it's the only self-improvement design reviewed here
that stays inside the eyes-not-hands boundary:

```text
trigger (weekly, or ≥3 tasks completed)
  → gather evidence, EXCLUDING evidence already cited by an active learning
  → apply thresholds (≥3 same-class outcomes; ≥2 to refute a belief)
  → write a LEARNING: a declarative sentence, ≥2 evidence IDs, a check_at date
  → write a PROPOSAL only if a behavior change is actually warranted
  → verify the evidence chain points backward to real events
  → human accepts or rejects
  → on accept: apply ONLY the described edit; record what literally changed;
    commit the target file and the proposal together in one commit
  → on reject: record the reason. Future passes check rejections FIRST,
    so a declined idea never gets re-proposed cold.
```

Two constraints that make it safe: **the agent never edits a rule file directly
— a proposal is the only path**, and many learnings correctly stop at "now I
know" with no behavior change attached.

---

## 9. What will actually go wrong, and what to say when it does

| Week | The thing he'll want | The honest answer |
|---|---|---|
| 1 | "Let's add hubs for all six subjects now" | A hub with no `raw/` is a folder. Build one, fill it, then earn the next |
| 2 | "The kernel should explain *why* each rule exists" | Put the why in `<!-- -->` comments. Zero context cost, full readability |
| 3 | "Have it run overnight and clean itself up" | Rejected twice in `.ROOT` on real analysis. Unreviewed rewrites are unverifiable output. This is the most attractive wrong turn available |
| 4 | "It keeps forgetting where we left off" | That's failure #1. It's a `state.py` problem, not a prompt problem. Compute it |
| 5 | "It's fighting me — I ask for X and it re-plans" | Real, and `.ROOT` has the same complaint on record. The fix is a direct-execution escape hatch in the kernel: a named prefix that means *do the stated task, no proposal, no challenge* — safety boundaries unchanged |
| 6 | "There are two files that both look current" | Stop everything and fix it. That's L-2026-01 and it costs weeks, not hours |
| 8 | "Should I move this to a database / add vector search?" | Measured need only. Grep and index-first reading are documented as sufficient to roughly 50–100K curated tokens. Filesystem is truth; any index is derived, disposable, and rebuildable |

---

## 10. What `.ROOT` should take back if this works

The honest position first: **`.ROOT`'s architecture is not the problem and
should not be rebuilt.** Every external framework it has been audited against —
Karpathy's pattern, Building a Second Brain, the agentic maturity ladder, four
chapters of the AI Agent Book, six independent implementations — has *validated*
it, five times independently on specific mechanisms. A structural rebuild is not
supported by any evidence in the vault.

What `.SEED` is genuinely useful for is being a **clean-room test bed** for six
changes that are already sitting in `.ROOT`'s own wiki as unadopted candidates,
where testing them in `.ROOT` would mean experimenting on a live system in the
middle of a semester:

1. **Computed state.** Split `NOW.md` into a generated block and a judgment
   block. This is the biggest one, it's already identified in the vault as a
   scoped proposal that was never drafted, and it directly attacks the failure
   mode behind flag #91 and the evening-reading bug. Also — it is exactly what
   Chris has said he wants from the planning layer: a bare dated deadline list
   instead of a re-planning cockpit. Computing the dates and writing nothing
   else *is* that request, implemented.
2. **Link-and-index at write time**, not at lint time. Named as a gap; never
   promoted to a rule.
3. **`approvals_reviewer = "user"`.** Currently `auto_review` and flagged as in
   tension with `AGENT.md`. This one needs a decision either way — it isn't a
   test, it's an open conflict.
4. **Protect the validators.** `00-BRAIN\scripts\` is editable by the sessions
   it checks. Move the baseline under a vendor-protected path or add a
   separate approval, and close the gap that was previously caught by luck.
5. **Negative examples in skill descriptions.** Flagged as unchecked across all
   seven `.ROOT` skills; "do NOT use when" is described in the source as *not
   optional* for routing accuracy as a skill library grows. `.ROOT` has seven
   skills. That's already the size where this starts to matter.
6. **A rung below `CHRIS_CORE.md`** — a ~120-token always-first facts file. Noted
   as a granularity `.ROOT` doesn't have. Cheap to test on someone else's vault
   first.

And one structural idea that only becomes testable now: Chris has said he wants
**school and value separated far enough that two agents can run in two windows
on the same PC without loading each other's files.** `.SEED`'s one-hub start
makes the lane-isolation boundary obvious, because there's nothing else in the
way. Whatever shape the second lane takes when it's *earned* in `.SEED` is a
much better model for splitting `.ROOT`'s lanes than redesigning them in place
mid-semester.

**Recommendation: build `.SEED` for the friend, run it for 30 days, then bring
items 1 and 2 back to `.ROOT` through the normal proposal gate.** Items 3 and 4
shouldn't wait on the friend's vault — they're open conflicts in `.ROOT` today.

---

## 11. Sources

All from `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\` unless noted.

- `agents/ai-agent-book-ch2-context-engineering.md` — status-bar experiment;
  static-prefix ordering; isolation over compression; skill routing and negative
  examples; third-party skills as an injection surface
- `agents/ai-agent-book-ch10-multi-agent-collaboration.md` — shared vs.
  non-shared context; handoff package; Byzantine failure and cross-validation;
  planner concentration; cognitive surrender
- `agents/ai-agent-book-ch3-ch8-memory-and-evolution.md` — filesystem paradigm
  and link maintenance; two-tier memory; safety mechanisms not self-modifiable;
  smallest-attributable-fix escalation ladder
- `agents/self-improving-agent-architectures-gbrain-loopany-closed-loop.md` —
  thin harness / fat skills; latent vs. deterministic; reflect-loop thresholds
  and the proposal-only path; dream cycle rejected
- `agents/agentic-automation-architecture-reliability-and-economic-evidence.md`
  — deterministic steps by default, bounded agent decisions, orchestration ≠
  autonomy
- `system-evolution/llm-wiki-pattern-and-second-brain-tools.md` — the pattern;
  what was adopted and rejected; filesystem-truth / derived-index boundary;
  grep sufficiency to ~50–100K tokens; sentinel markers; dual-track research
- `system-evolution/root-maturity-self-assessment.md` — verification capacity
  gates progression; L1/L2 position
- `system-evolution/building-a-second-brain-root-application.md` — capture
  filter; handoff merge; what was declined
- `platforms/anthropic/claude-code-context-and-instruction-economics.md` —
  subagent re-pays the root file; <200-line discipline as a quality lever;
  HTML-comment stripping; the mid-session-edit gotcha
- `platforms/codex/codex-app-configuration-and-security.md` — precedence stack;
  trust gate; sandbox and approvals; permission profiles; execpolicy; hooks;
  protected paths; `/status` and `/debug-config`
- `00-BRAIN\AGENT.md`, `00-BRAIN\WIKI_SHARED_LAYER.md`,
  `00-BRAIN\SYSTEM_FLAGS.md`, `00-BRAIN\SYSTEM_LEARNINGS.md` (L-2026-01),
  `00-BRAIN\WHERE_IT_GOES.md`, `ROOT_OPERATING_MANUAL.md`, `NOW.md` — `.ROOT`'s
  own contracts, measured incidents, and the September rewrite figures

**Recency caveat:** the Codex and Claude Code platform pages were processed in
July 2026. Both surfaces move fast. Re-verify §7's exact key names against
current vendor docs before the friend commits them to a config file.
