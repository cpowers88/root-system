---
type: report
timeline: now
status: active
tags: [governance, castle, review]
---

# CASTLE Instruction-Layer Review — Pass 1 (Claude Code, 2026-08-22)

### Scope: CASTLE's own `.md` instruction files, then the metadata layer beneath them
### Hat: Software Engineer (`HAT_SOFTWARE_ENGINEER.md`) — read before touch, findings name the exact failure condition
### Status: **findings only. Nothing was fixed.** Held for reconciliation with Codex's parallel pass.

*This file carries no `register:` — it is a report, and per `WHERE_IT_GOES.md` a
non-instruction file carries none. That rule is also Finding S-1.*

---

## Headline

Chris's instinct was right, and it points one layer lower than he aimed it.

CASTLE's instruction prose is in **better** shape than expected — the Aug 19 and Aug 21
sessions did real work and `OPERATIONS.md` is genuinely current. The defects there are
narrow and cheap (§ CASTLE Findings, C-1…C-7).

**The rot is underneath.** `register:` — the property flag #84 was closed on — has a sixth
value on 22 files, all of them in the file class the closure rule explicitly prohibits. It
has been spreading since **the day the flag was closed**. Nothing detected it, because
`frontmatter_audit.py` claims to enforce the Metadata Standard and never checks `register:`
at all. Every "frontmatter CLEAN" line in the CASTLE log for the past four days is a green
light over an unmeasured field.

---

## What was verified, and how

| Check | Method | Result |
|---|---|---|
| Path references in CASTLE resolve | regex-extract every backticked `*.md` path in 24 CASTLE files, resolve against 8 candidate roots | **2 stale**, both in closed historical weekly plans. **CASTLE link hygiene is good** |
| CASTLE header dates vs body content | read each instruction file, compare stated revision date to dated body claims | **1 stale header** (C-1) |
| Loader-file inventory vs the Aug 10 sweep | `99-ARCHIVE\ARCHIVED_2026-08-10_hub-pointers\` contents vs live tree | 8 hubs stripped; **CASTLE is the only survivor** (C-6) |
| `type:` values vs `WHERE_IT_GOES.md` approved list | 1,546 typed `.md`, exclusions matching `frontmatter_audit.py` | **1,000 files on 57 unapproved values** (S-3) |
| `register:` values vs the five approved | same scope | **72 files, 6 values, 22 outliers** (S-1) |
| What `frontmatter_audit.py` actually enforces | read the source | **`type:` value and `register:` are never checked** (S-2) |
| Flag #84's closure claim | `CLOSED_FLAGS_2026-07.md:39` | verified-after was **"56 files, 5 values, zero outliers"** |

---

## System findings — the real ones

### 🔴 S-1. Flag #84 has re-opened. Its own closure record names the value that came back.

`WHERE_IT_GOES.md § Metadata Standard` states three rules:

1. "**Exactly five approved values**" — `ai-directive`, `ai-loader`, `ai-profile`,
   `human-context`, `compatibility-pointer`.
2. "**A file that is not an instruction interface does not carry `register:` at all.**
   Wiki content pages, reports, reviews, weekly plans, logs, and evidence are described by
   `type:`."
3. "If a file seems to need a sixth value, **that is the signal it should not carry the
   property**."

**Live state: 72 files, six values.** The sixth is `register: system-review`, on **22
files** — 17 `type: report`, 2 `type: proposal`, 1 `index`, 1 `plan`, 1 `report`. Every
one is a report, proposal, plan or index: precisely the class rule 2 prohibits.

This is not a new value drifting in. `CLOSED_FLAGS_2026-07.md:39` names it directly:

> *"the property had grown from 50 files/6 values to 61 files/8 values, with `system-review`
> and `weekly-plan` minted the same week by the July 24-25 update's own output"*

…and records the verified-after state as **"56 files, 5 values, zero outliers."**

`weekly-plan` was stripped and stayed stripped. `system-review` regrew. Its first commit is
**2026-07-25 (`0eefab1`) — the same day Chris scoped the property and closed the flag** —
then `9dc3cd5` (07-27), `91d69a2` (08-10), `4278d00` (08-11), and `2a9caf5` + `d5b06ff`
inside the August 12 update's own output. That last detail is verbatim what #84's forensics
said happened the first time: *propagation by sibling precedent, seeded by the update that
was supposed to be fixing it.*

**`SYSTEM_FLAGS.md`'s own rule: "If the same flag is re-raised after being closed, it comes
back as HIGH."** I am not raising it in the register unilaterally — see § What I Need From
Chris.

### 🔴 S-2. The instrument certifying the metadata layer does not measure two of its four vocabularies.

`frontmatter_audit.py` line 4 claims:

> *"Checks every live .md in .ROOT against WHERE_IT_GOES.md § Metadata Standard"*

What it actually enforces:

| Property | WHERE_IT_GOES defines | Audit enforces |
|---|---|---|
| `timeline:` | 6 values, exactly one per file | ✅ hardcoded set, dual-encoding check |
| `reference_priority:` | 3 values | ✅ hardcoded set |
| `stage:` / `status:` | optional, explicit non-empty scalar | ✅ non-empty + scalar |
| **`type:`** | **21-value list** | ❌ **presence only** (`^type:\s*\S+`) — any string passes |
| **`register:`** | **5 values + a scoping rule that closed a flag** | ❌ **the string `register` does not appear in the file** |

The two properties `WHERE_IT_GOES` spends the most words on — `register:` gets 30 lines
including flag #84's whole history — are the two with zero coverage. That is why S-1 grew
for four weeks in silence, and why `frontmatter_audit.py` reports **0 findings, CLEAN** over
it. That CLEAN is cited as passing evidence in `CASTLE\wiki\log.md` on Aug 19, Aug 21, and
Aug 21 night.

**Contrast worth preserving:** `root_health.py` does *not* have this problem. Its docstring
says *"Exit 0 means no blocker in the named scopes; it does not claim semantic freshness,"*
and it ships an explicit `NOT_EVALUATED` list. It is honest about its boundary.
`frontmatter_audit.py` overclaims its scope in the one line a session reads to decide
whether to trust it. **The defect is the docstring as much as the missing checks** — a
checker that said "enforces timeline and reference_priority only" would never have produced
a false green.

### 🟠 S-3. `type:` is a controlled vocabulary on paper and a free-text field in practice.

1,546 typed files. `WHERE_IT_GOES` publishes 21 values; 18 are in use, covering **546
files**. The remaining **1,000 files run on 57 values that are not on the list.**

The standard's entire escape hatch is four words: `(+ wiki-specific types)`. No registry, no
per-hub declaration, no validation. The signature of an uncontrolled vocabulary is visible
in the data:

- **Near-duplicate pairs:** `spec` / `specification` · `concept` / `concepts` ·
  `glossary` / `glossary-entry` · `tool` / `tool-capability` ·
  `evidence` / `evidence-log` / `evidence-report`
- **~20 values used exactly once:** `landscape-rep`, `decision-note`, `decision-response`,
  `private-proof-outline`, `work-order`, `law`, `runbook`, `brief`, `asset`…

And the hatch does **not** cover the governance layer, which is outside `03-WIKIS`:
`contract` (15 files — including `AGENT.md` and *every* `OPERATIONS.md`), `handoff` (20),
`index` (13), `instruction` (5), `phase` (5), `goal` (3), `person` (2).

**The estate is not wrong here — the authority is stale.** `contract` on `AGENT.md` is a
better label than `ops`. The fix is to ratify what is actually in use, not to rewrite 1,000
files. But it has to be *decided*, or the next audit inherits the same ambiguity.

### 🟠 S-4. `WHERE_IT_GOES.md` cites a file class that was deleted twelve days ago.

Its `register:` table gives `ai-directive` as applying to *"canonical machine contracts —
`AGENT.md`, `OPERATIONS.md`, **hub `CLAUDE.md`**."* Hub `CLAUDE.md` files were removed
2026-08-10 and archived. `WHERE_IT_GOES.md` was edited **2026-08-16** and still carries the
dead example. The naming authority is describing an estate that no longer exists.

### 🟢 S-5. `WHERE_IT_GOES.md` carries no `register:` of its own.

The file that invented the property, defines who must carry it, and is named in `AGENT.md`
File Safety 6 as placement and naming authority, is `type: map` with no register. It is
unambiguously a machine-executed instruction interface.

### 🟢 S-6. Flag #101, instance 11 — recorded live this session.

The bulk gate denied `git log -1 --format=%ad --date=short` in a `for` loop over 13 CASTLE
files. Read-only, zero writes, no wildcards. Denied for containing a loop; the offered
remedy was a WSL re-launch of a command that only reads. I completed the enumeration in
**PowerShell**, which prohibition 2 records as entirely ungated — identical in shape to
instance 7. Eleven instances. No new argument needed; this is a data point, not a new flag.

---

## CASTLE findings — narrower than feared

### C-1. `HOW_TO_USE.md`'s header is stale, and it went stale *in the session that fixed this exact defect elsewhere.*

Header: **"Last updated: July 24, 2026."** Body line 41 carries a correction dated
**2026-08-21**. The Aug 21 session logged repair **C1 — "Header dates corrected"** — fixing
`OPERATIONS.md` (which read July 19 while carrying Aug 19 and Aug 21 rules), `index.md`, and
`NOW.md`, and wrote the reason: *"A header date is what a session reads to judge freshness."*
It edited `HOW_TO_USE.md`'s body in the same pass (repair R3) and did not touch its header.

**The failure is the check's shape, not the session's care:** C1 was run as a list of known
stale files, not as a sweep over every file the session was about to modify. A repair that
enumerates targets in advance cannot catch the file it dirties on the way past.

### C-2. `HOW_TO_USE.md` does not know the semester exists. Classes start in two days.

CASTLE's machine contract gained an entire semester regime on Aug 19–21: Reviews item 4
(course standing + miss log, running *before* items 2 and 3 during term), the semester
maintenance budget, the return-to-cockpit gate. `HOW_TO_USE.md` is the **human** router —
the file Chris opens — and it carries none of it. Its "Ask the Right Owner" table has no row
for *"How am I doing in my courses?"* or *"What did I miss?"*, though those are now the
first two reads of every Sunday and the only ones carrying consequences Chris cannot recover
later.

This is the single most user-visible gap in CASTLE and the one I would fix first.

### C-3. `README.md` names the wrong Codex loader.

`README.md § Route` lists *"Claude loader: `CLAUDE.md` · Codex loader: `CODEX.md`."* Per
`AGENTS.md`'s own text, Codex tooling auto-discovers **`AGENTS.md`**, not `CODEX.md` — which
is why `AGENTS.md` exists. README names the file Codex does *not* load, and omits the one it
does.

### C-4. `wiki/index.md` calls itself "Every Live Page in CASTLE" and omits `AGENTS.md`.

§ CASTLE Root Files lists `OPERATIONS.md`, `README.md`, `HOW_TO_USE.md`, `CLAUDE.md`,
`CODEX.md`. `AGENTS.md` is live and is an instruction interface. The index that certifies
completeness is incomplete, and the missing file is a loader.

### C-5. `CODEX.md` is classed "pointer only, no rules" and carries four rules.

Frontmatter: `register: ai-loader`, which `WHERE_IT_GOES` defines as *"thin pointer files
whose only job is routing… **pointer only, no rules**."* Body carries four: `raw\`
immutability, template-change scope, structural-page approval, report placement. All four
duplicate `AGENT.md` / `OPERATIONS.md`.

The risk is not the duplication — it is that a session correctly treating loaders as pure
routing (which the register tells it to do) would skip a file that contains rules. Also
`type: instruction`, an unapproved value (S-3).

### C-6. CASTLE is the only folder in `.ROOT` still carrying per-folder AI loaders — and they are its only files untouched since Aug 10.

`99-ARCHIVE\ARCHIVED_2026-08-10_hub-pointers\` holds eight folders: all eight `03-WIKIS`
hubs. **No CASTLE folder.** `AGENT.md:142` scopes that removal to "hubs," and CASTLE is not
in `03-WIKIS`, so it reads exempt — but I find no record of the exemption being *decided*
rather than simply not reached.

The consequence is measurable regardless of intent: `CLAUDE.md`, `AGENTS.md` and `CODEX.md`
are the only CASTLE instruction files not opened since **2026-08-10**. They predate
OK-TO-START (Aug 17), the school-first ruling (Aug 19), and the whole semester regime.
Combined content: three files whose entire job is "go read `OPERATIONS.md`," one of which
(C-5) smuggles rules, one of which (C-3) the README misdescribes.

**This is exactly the shape Chris described** — the CASTLE instruction files that missed the
newest update. It is three small files, not a systemic failure, and the honest fix is
probably to collapse them the way the hubs were.

### C-7. `HOW_TO_USE.md:43` spells a path that does not exist.

`02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md`. Live folder:
`ref-AI-automation`. `current-position.md:96` spells it correctly. Windows hides the
mismatch; a WSL path (which is where `safe_shell.sh` runs) would not, and it contradicts
the resolved naming rule.

---

## What is genuinely healthy — stated so the fix does not over-correct

- **`OPERATIONS.md` is current and well-built.** The Aug 19–21 additions (return-to-cockpit
  gate, Reviews item 4, semester maintenance budget) are precise, dated, attributed, and
  each names its own reason. It even self-documents its own stale-header defect at lines
  17–19. This file does not need a rewrite.
- **Path/link integrity across CASTLE is good** — 2 stale refs in 24 files, both in closed
  historical plans.
- **`current-position.md`'s Aug 21 reconciliation is real work**, and its "Basis" column
  turning *unchanged* into a measured claim is a genuinely good design move.
- **`skill-map.md` correctly holds no state** and says so three times. The flag #103 fix held.
- **`root_health.py` is honest about its boundary.** Keep that pattern; it is the model for
  fixing S-2.

---

## What I need from Chris

**One decision, and it is a scheduling decision, not a technical one.**

S-1 is a re-raised closed flag. `SYSTEM_FLAGS.md`'s rule says it returns **HIGH**, and the
HIGH rule says *"do not close a session with an open HIGH flag."* Filing it today would
commit the session to fixing it today — on the Saturday dress rehearsal, two days before
classes, under an Aug 19 ruling that school outranks optional system work and that CASTLE
maintenance shrinks before learning does.

I did not file it unilaterally, because doing so would use a governance rule to override a
Chris ruling. Three options:

1. **File it 🔴 and fix it today.** The fix is ~40 lines in `frontmatter_audit.py` plus a
   `register:` ratification decision. Real, but it eats the rehearsal.
2. **File it 🟠 with the Aug 23 review as its check moment** — S-1 is metadata drift on
   report files. It is genuinely inert on Monday morning; nothing about Aug 24 D2L touches
   it. **This is my recommendation.**
3. **Hold both S-1 and S-2 until the Sunday close** and reconcile them there against Codex's
   findings, since Aug 23 already owns five closes and this would be a sixth.

**Recommendation: option 2.** File S-1 and S-2 as one 🟠 flag at the Aug 23 review, fix the
audit script first (it is the thing that lets the drift recur), then rule on the `type:` and
`register:` vocabularies as a single ratification. **The instrument before the estate** — S-2
is why S-1 survived, so fixing S-1 without S-2 buys four more weeks of silence.

Second, smaller decision: **C-6 — collapse CASTLE's three loaders the way the hubs were, or
keep them deliberately and record why?** Either is defensible; the current state is neither.

---

## Not examined in this pass — disclosed, not implied

`north-star-roadmap.md`, `source-map.md`, `opportunity-queue.md` and the five phase pages
were read for links and frontmatter only, not for semantic currency. The eight `03-WIKIS`
hubs were checked for file layout only. Of the scripts layer I read `frontmatter_audit.py`
in full and `root_health.py` only far enough to establish its honesty boundary;
`wiki_lint.py`, `path_reference_audit.py`, `validate_boot_chain.py` and `castle_freshness.py`
were not reviewed and may carry the same overclaim defect as S-2. **That is the obvious next
pass, and it is the one I would give Codex** — a coverage audit of every checker's docstring
against what it actually asserts.

No check was run that is not reported above. No file was modified.

---
*Claude Code · 2026-08-22 · Pass 1 of the pre-semester `.ROOT` review · Held for
reconciliation with Codex's parallel pass per `AGENT.md` Execution Discipline 6 — Chris
receives one reconciled answer.*
