---
type: proposal
timeline: reference
status: implemented
tags: [governance, architecture, boot-chain, execution-discipline]
created: 2026-07-26
---

# Proposal — Execution Discipline and Boot-Chain Repair

**For:** Chris's approval, Codex's review.
**Authority:** Chris's 2026-07-26 interview (`claude_and_chris_direction.md`),
the July 24 architecture packet, and the eight-source intake synthesis.
**Nothing in this document has been applied.** No instruction file has been
edited. Every change below is proposed text awaiting explicit approval, per
Chris's rule: *never update `.md` or other system instructional files without
approval from Chris.*

**What this supersedes:** nothing. The July 24 packet is a closed historical
record; its retired migration gates stay retired. This proposal adds operating
discipline and repairs a boot-chain gap. It proposes no structural move.

---

# Part 1 — The Exact Edits

## Edit 1 — `00-BRAIN\AGENT.md`, new section

**Placement:** immediately after `## Direction and Priority Policy`, before
`## One AI Team`.

```markdown
## Execution Discipline

Approved by Chris 2026-07-26 after a full-system interview. These rules govern
how work is selected and sequenced. They do not change the priority order above.

1. **Work first.** No optional `.ROOT` update begins before the day's primary
   learner or value proof is complete and recorded. A HIGH blocker may
   interrupt; stale prose, an attractive redesign, or ordinary discomfort may
   not.
2. **Sunday owns system work.** System updates, weekly planning, and LIFE/
   business exploration happen Sunday. Monday through Saturday execute the
   plan. An off-cycle change requires a HIGH flag (patch only) or an
   evidence-backed system report. Chris may override; ask him to confirm each
   time an override falls outside those two categories.
3. **One visible lane.** The active cockpit shows the current lane only. Other
   lanes stay one navigation step away, never on the same page.
4. **Decide the operational, propose the directional.** Reading, order, drills,
   formatting, and sequencing are decided for Chris, not offered as a menu.
   Direction Chris can set — school, family, time, what matters this month —
   stays his. Direction he has no map for yet — how a business gets built, what
   capability compounds next — is proposed with a recommendation and reasoning,
   never handed back as a blank page and never decided silently. Chris holds
   veto and every major change.
5. **Proof moves the stage immediately.** A gate is available whenever Chris is
   ready. Do not wait for a scheduled day if the gate passes early; do not
   advance because a calendar says to. A stage may not open until its gate is
   written.
6. **Chris receives one reconciled answer.** Consequential work is reviewed
   independently — by a second model, or by a fresh session shown the work as a
   third party's when no second model is available. One lead then integrates and
   names any real disagreement inside a single document. Integrating competing
   reports is AI work, not Chris's.
7. **Every stop rule names an owner and a check moment.** A dated trigger nobody
   is assigned to evaluate does not exist.
8. **The AI that writes a drill does not grade it.** Same reason as 6:
   self-assessment is measurably weaker than third-party assessment.
```

**What this edit is meant to do.** Every rule here is a repair for a failure
that actually happened this month, not a preference. Rule 1 and 2 exist because
July 24–25 spent two days on architecture while the Python benchmark and MCP
Days 5–8 went unrun — both Claude and Codex independently identified that
displacement as the primary failure of the week. Rule 2 in particular gives the
work-first gate a calendar home so it does not depend on judgment in the moment,
which is what failed last time. Rule 3 comes directly from Chris's own report
that seeing every available lane produces tangents. Rule 4 is the correction
Chris made to Claude's first draft, which wrongly assigned all directional
decisions to him and would have stranded him on exactly the questions he has no
map for. Rule 5 resolves the physics gate-day conflict and Chris's
wheel-spinning complaint at once: performance moves the frontier, the calendar
only allocates hours. Rules 6 and 8 preserve the blind-review protocol that
caught three real errors today while removing the integration burden it placed
on Chris. Rule 7 is the July 23 honest-floor failure — a well-written stop rule
with a date and a defined cut that never fired because nobody was assigned to
check it.

---

## Edit 2 — Eight new files: `03-WIKIS\<HUB>\AGENTS.md`

**This is the boot-chain repair, and it is the most consequential item here.**

Every hub currently contains `CLAUDE.md` as its loader. **No hub contains
`AGENTS.md`.** Codex tooling auto-discovers `AGENTS.md`, not `CLAUDE.md`. So a
Codex session started inside `03-WIKIS\PHYSICS\` loads no local contract at all.

`AGENT.md` currently papers over this with a rule — *"a wiki file named
`CLAUDE.md` is the domain operating contract for every AI working there; its
historical filename does not make it Claude-exclusive."* That rule is correct
and it does not work, because Codex never opens the file that contains it.

Proposed file, identical in each hub except the hub name (PHYSICS shown):

```markdown
---
type: pointer
timeline: reference
status: live
register: ai-loader
tags: [governance, physics]
---

# AGENTS.md — PHYSICS Codex Auto-Load Pointer

This file and `CLAUDE.md` are the same boot pointer for this hub. Both are
surface-neutral; neither reserves the hub for one model. Load order:

1. `..\..\00-BRAIN\AGENT.md` — universal OS, always first
2. `..\..\00-BRAIN\CODEX.md` — surface profile
3. `..\..\00-BRAIN\CHRIS_CORE.md` and `..\..\00-BRAIN\SYSTEM_FLAGS.md`
4. `OPERATIONS.md` — this hub's canonical local contract
5. `wiki\current-position.md` — sole learner-truth authority
6. `wiki\learning-path.md`

Do not maintain rules here. `OPERATIONS.md` is the local contract.
```

**What this edit is meant to do.** It closes a real asymmetry: Claude boots a
hub's local rules automatically and Codex does not. That is a plausible
mechanical contributor to "we are extremely misaligned sometimes when all three
of us are working together" — the two models have not been reading the same
local contract, and neither of them would necessarily notice. The fix is eight
thin pointer files with no rules of their own, so there is nothing to drift.
Once these exist, `AGENT.md`'s filename-neutrality rule becomes a description of
what the files actually do rather than a workaround for what they don't.

---

## Edit 3 — `NOW.md` restructure to single-lane

Current `NOW.md` is 188 lines and presents, on one page: school, the MCP
bootcamp, business hypotheses, revenue lanes, parked opportunities, open flags,
a six-row current-picture table, a fourteen-item week list, and twelve upcoming
dates. Chris reports he has largely stopped opening it.

Proposed structure (content to be filled from live owners, not invented):

```markdown
# NOW — <day>, <date>

## Today
<the single lane. One heading. What is being worked, the first action, and the
exact file it lives in. Nothing else.>

## Today's Gate
<what would count as done, stated before the work starts>

## If Today Breaks
<the one fallback action, and who to tell>

---
## Not Today
<a plain list of links only — no status, no detail, no dates. Other lanes are
reachable in one click and invisible until clicked.>

## Owners
<pointer list to the live authority files, unchanged from current NOW.md>
```

**What this edit is meant to do.** It converts the cockpit from a status
dashboard into a work surface. The current file's failure is not inaccuracy —
it was rebuilt and verified yesterday — it is that a person who has stated that
visible options generate tangents is handed the full menu every morning and
asked not to look at it. Everything currently in `NOW.md` stays reachable; only
the same-page visibility changes. The "Today's Gate" line is new and enforces
Execution Discipline rule 5 at the place work actually starts. This is also the
edit most likely to need a second pass after a week of real use, so it should be
treated as a test with a `check_at`, not a permanent shape.

---

# Part 2 — The Boot Chain and the Remaining Files

## 2.1 What the boot chain looks like now

| Level | Claude | Codex | Status |
|---|---|---|---|
| Root pointer | `CLAUDE.md` | `AGENTS.md` (canonical), `CODEX.md` (stub) | correct |
| Universal OS | `00-BRAIN\AGENT.md` | same | correct |
| Surface profile | `00-BRAIN\CLAUDE.md` | `00-BRAIN\CODEX.md` | correct |
| Person + flags | `CHRIS_CORE.md`, `SYSTEM_FLAGS.md` | same | correct |
| Hub local | `03-WIKIS\<HUB>\CLAUDE.md` | **nothing** | **GAP — Edit 2** |
| Hub contract | `OPERATIONS.md` | reachable only via the missing loader | blocked by the gap |
| CASTLE local | `CASTLE\CLAUDE.md` + `CASTLE\CODEX.md` | both present | correct |

CASTLE has both loaders. The eight hubs have one. That inconsistency appears to
be an oversight from the July 10 lane split rather than a decision — CASTLE was
converted with both, the hubs with one, and nothing since has checked.

## 2.2 The wiki-as-operating-system goal — built, not pivoted

Chris's recollection was that the plan was to make wiki folders near-self-
contained operating systems, with CASTLE overseeing the wikis and `.ROOT`
itself, and that the update pivoted away from it.

**Verified: all eight hubs are converted.** `AI_AUTOMATION_SYSTEMS`, `BUSINESS`,
`EDUCATION`, `PHYSICS`, `PYTHON`, `REVENUE_LAB`, `SYSTEMS`, and `TECHNOLOGY`
each carry a loader, `OPERATIONS.md`, `README.md`, `HOW_TO_USE.md`, `wiki\`, and
`raw\`. Uniform, no exceptions.

**CASTLE's oversight role is defined as described.** `CASTLE\OPERATIONS.md`:
*"CASTLE maintains maps, gates opportunities, sequences capability, records
proof movement, and holds the integration pointers between realms. Domain wikis
own research and learner truth… CASTLE points to owner truth instead of copying
it."*

So the goal was reached. What is missing is not the architecture but two
mechanical pieces: the Codex loader above, and the fact that **CASTLE has no
scheduled moment where it actually inspects hub health.** It has the authority
and the role; it has no recurring check. That is Execution Discipline rule 7
applied to CASTLE itself, and it is the honest answer to "did we pivot" — the
structure was built and never given an operating cadence.

## 2.3 What yesterday actually left behind

Reviewing the July 24 packet against the live tree, three things were mixed or
missed:

1. **Two architecture working files are still sitting at the vault root.**
   `vault-skeleton-design.md` (37 KB) and `newvaultstructureclaude.md` (13 KB)
   are design artifacts, not entry surfaces. Root is supposed to hold interfaces
   only. Deferred housekeeping item 4 — *"review whether root-level entry
   surfaces are all still necessary"* — was raised on July 24 and never run.
   These two are the answer to it. **Proposed: move both to the July 24 packet
   folder, leave a pointer if anything references them.** Not urgent, but it is
   the exact clutter the roadmap says root should not accumulate.
2. **Deferred items 6 and 7 are no longer hypotheses.** Item 6 proposed a
   human-facing area for Chris-specific operating rules and readable reports;
   item 7 proposed an end-of-day human reporting surface. Both were parked July
   24 for lack of evidence. **Today's interview is that evidence** — the daily
   stepped checklist, the weekly map, and the "requirements to do the school
   work" are precisely this artifact. The packet's own acceptance test still
   applies: adopt only if Chris finds daily state faster, machine instructions
   get less noisy, and no duplicate authoritative facts appear. Recommend
   treating the weekly map + daily checklist as the pilot rather than opening a
   new `04-Chris` folder.
3. **Deferred item 9 is still open.** Atlas is retired as a named lane in
   practice but still appears as an owner in `SYSTEM_FLAGS.md` #16. One-line
   fix, no urgency.

## 2.4 What is explicitly not proposed

- No CASTLE move. The relocation stays retired; the July 24 packet's Gates 2/4/5
  and Runbook Phases 4–5 remain do-not-execute.
- No second LIFE system. Gated on evidence that single-lane visibility was
  insufficient — see Part 3.
- No new folders, no `04-Chris`, no `human_eye_log`.
- No North Star change of any kind.
- No vault-wide instruction rewrite. Three edits and eight pointer files.
- No build-out of PHYSICS Stages 10–18.

---

# Part 3 — The LIFE Split, Recorded as a Gated Decision

Chris's stated reason for wanting two systems is attention, not coordination:
*"the problem is not you it is me — if I want to do school I want to do school,
if I want to explore I want to explore."* He also asked the right technical
question: whether two folders would confuse the AIs.

**They would not.** Both tools boot from their working directory; a second
folder with its own `AGENTS.md`/`CLAUDE.md` would cleanly load its own chain.
The cost is not confusion — it is duplicated governance: two North Stars, two
file-safety rule sets, two flag lists, two places learner truth can drift. That
doubles the surface where "all the pieces working as one team" already hurts.

Because the stated need is *the other option being invisible while working*,
Execution Discipline rule 3 and the `NOW.md` restructure address it directly and
reversibly. Codex reached the same conclusion independently and by a different
route.

**Decision recorded as gated, not declined.** Test single-lane visibility through
the school-simulation week. If Chris still reports lane-bleed after two measured
weeks — and the cause is genuinely attention rather than an unused daily plan —
a separate LIFE workspace becomes an evidence-backed proposal, and it goes
through the North Star Ratchet rather than an informal folder change.

`check_at`: **August 9, 2026** (joint weekly review 3), owner: Chris, with
Claude or Codex presenting the two weeks of lane-bleed evidence.

---

# Part 4 — Approval Checklist

| # | Change | Files | Reversible | Chris |
|---|---|---|---|---|
| 1 | Execution Discipline section | `00-BRAIN\AGENT.md` | yes — delete section | ☐ |
| 2 | Codex hub loaders | 8 new `03-WIKIS\<HUB>\AGENTS.md` | yes — delete files | ☐ |
| 3 | `NOW.md` single-lane rebuild | `NOW.md` | yes — git restore | ☐ |
| 4 | Move 2 design files off root | `vault-skeleton-design.md`, `newvaultstructureclaude.md` | yes — move back | ☐ |
| 5 | Atlas lane retirement | `SYSTEM_FLAGS.md` #16 owner field | yes | ☐ |

Items 1–3 are what Monday runs on. Items 4–5 are housekeeping and can wait for
any Sunday.

**Not in this checklist, still owed today if approved:** this week's weekly map
and tonight's evening reading. Those are content, not governance, and they are
the actual deliverables the simulation week starts from.

---

*Proposal only. Awaiting Chris's approval and Codex's review. If Codex
disagrees on any item, per Execution Discipline rule 6 the disagreement should
be named inside one reconciled document rather than returned to Chris as a
competing plan.*
