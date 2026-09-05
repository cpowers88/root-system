---
type: report
timeline: now
status: proposed
tags: [governance, castle, challenge-packet, flag-103]
created: 2026-08-19
---

# Challenge Packet — Flag #103, CASTLE Ownership Collapse

### For an independent second seat. Cold-briefable. Every claim below is falsifiable; the falsifier is stated.

**Commissioned:** Chris, 2026-08-19, on a CASTLE seat review he directed.
**Lead:** Claude Code. **Charge to the challenger:** break the diagnosis, the timeline, or
the recommendation. Do not re-derive what is already measured — attack it.

Per `AGENT.md` § One AI Team rule 6, the lead integrates this response into one document
and names any real disagreement. Chris does not referee competing reports.

---

## The claim in one paragraph

CASTLE's core maps stopped being maintained on **2026-07-19**, five days before Chris took
any time off, because three files each name another as the owner of capability state — a
closed authority loop in which no file is anyone's job. The loop was completed by the
July 24 architecture update. The system's fast loop (weekly plans, profit gates, the
decision log) stayed healthy until **Aug 7**, which is why Chris's July 28 journal records
the system "running wonderfully" — that observation was correct at the time. On Aug 7 the
system entered six days of overlapping self-redesign and its decision log went silent the
same day. The defect is a **repeat** of one found and mis-cured on 2026-07-19.

---

## Claim 1 — The authority loop is real and closed

| File | Line | Says |
|---|---|---|
| `CASTLE\wiki\skill-map.md` | 20 | "The active register is **the only home** of current capability state." |
| `CASTLE\wiki\current-position.md` | 49 | "If states diverge mid-month, **[[skill-map]]'s register is live truth**; this table is the monthly snapshot." |
| `CASTLE\wiki\current-position.md` | 53 | "The July ranking remains **owned by** `capability_development_goal.md`" |
| `Goals & Milestones\capability_development_goal.md` | 19 | "cross-domain priority and **proof status: CASTLE**." |

**Falsifier:** produce a fourth file that unambiguously resolves the loop, or show that two
of these four sentences govern non-overlapping questions. (Lead's position: 49 and 20 govern
the *same* question and 19 returns authority to the realm that just delegated it away.)

## Claim 2 — The loop has a measured cost, not a theoretical one

`skill-map.md`'s register reads `Python | building — Stage 4`.
`03-WIKIS\PYTHON\wiki\current-position.md:104` reads `## Stage 4 — CLOSED (2026-07-29)`;
frontier is Stage 4b. **The file designated "live truth" has been wrong for 21 days.**

Identical class, same week: finding **N4** (2026-08-17) corrected this exact staleness in
`current-position.md` and **did not** correct the register that file defers to.

**Falsifier:** show the register was correct at any point after 2026-07-29, or show that
"Stage 4" in CASTLE means something other than the PYTHON stage number.

## Claim 3 — The defect and its cure were written the same day, in the same document

`System Update Log\2026-07-19_ROOT_INFORMATION_CASTLE_RECONCILIATION\CASTLE_B0_B1_CLAUDE_REVIEW_2026-07-19.md`

- Diagnosed the same failure in `PRE-SEMESTER_PREP_PLAN.md`: *"says Physics Stage 3 /
  Python Stage 2 (both closed July 16) … depended on a weekly reconciliation that didn't
  happen."*
- Prescribed the cure: **"gates + pointers, no copied state."**
- Then, under **"One optional polish,"** recommended adding the `current-position.md:49`
  line that makes a copied-state table authoritative.

**Falsifier:** show the polish was scoped to a case the cure did not cover.

## Claim 4 — The timeline, and why Chris's July 28 note is consistent

| Date | Event | Layer |
|---|---|---|
| Jul 19 | Maps reconciled; copied-state authority line added | slow |
| Jul 24 | Architecture update creates `Goals & Milestones`; loop closes; **all CASTLE maps freeze** | slow |
| Jul 24 – Aug 7 | Weekly plans written, profit gates logged (Jul 29, Jul 30 ×3, Aug 2, Aug 7), PYTHON Stage 4 closed Jul 29 | **fast — healthy** |
| **Jul 28** | **Chris's journal: system "running wonderfully"** | ✅ accurate |
| Aug 7 | ROOT V2 Digital Garden Review opens. **Last CASTLE log entry is the same day.** | — |
| Aug 7–13 | Four overlapping self-reviews in six days: V2 garden review, Tree Migration Gate 0, Council Review, ROOT UPDATE | inward |
| Aug 11 | Council (4 seats) names the general defect (see Claim 5) | — |
| Aug 12–17 | PAUSE + finding freeze | — |
| Aug 17 | `OK TO START` | — |
| Aug 19 | #103 raised — the specific instance of Aug 11's general finding, still open | — |

The two-layer split is the load-bearing part: **the slow layer (maps, registers, phase
gates) froze on Jul 19–24; the fast layer (plans, decisions, log) ran until Aug 7.** A user
experiences the fast layer daily and the slow layer monthly, which is exactly why Jul 28
felt fine and mid-August did not.

**Falsifier:** find a substantive (non-mechanical, non-path-repoint) edit to
`skill-map.md`, `source-map.md`, `north-star-roadmap.md`, or `phase-map.md` after
2026-07-25. Git is the arbiter, not file mtime — Drive sync rewrites mtimes.

## Claim 5 — The Aug 11 Council already found the general form of this

`2026-08-11_ROOT_COUNCIL_REVIEW\COUNCIL_RECONCILED_VERDICT.md`, verdict paragraph:

> "the governance layer is the **only** place knowledge converts … it repeatedly **detects
> its own defects and then fails to propagate the correction into the prose anyone reads.**"

Flag #103 is a measured instance of that sentence, found eight days later, still open.

**Falsifier:** show #103 was already covered by an accepted council remedy that has shipped.

## Claim 6 — Phase 0 names this failure mode in its own risk register

`CASTLE\wiki\phases\phase-0-current-position-and-baseline.md` § Risks and Distractions:

> "**Building the castle instead of the tracker** (planning-as-avoidance — named risk)"

Aug 7–13 ran four architecture reviews while the cockpit's own log went silent.

**Falsifier:** show the Aug 7–13 reviews produced shipped instruments rather than proposals.
(Lead has not audited this — it is the weakest claim in the packet and the one most worth
attacking.)

---

## Open state, dated

- `opportunity-queue.md` — 4 rows past review date (Aug 1 ×1, Aug 14 ×2, Aug 16 ×1);
  `OPP-20260727-01` has **no review date**, 23 days at `captured`. The Aug 16 row is the one
  Chris approved advancing on Aug 2.
- Phase 0 `status: active`, window Jul 2026, exit criterion "August 1 monthly review" never
  ran. Phase 1 `status: planned`, window opens **Aug 24** — 5 days.
- `CASTLE\wiki\log.md` — last entry Aug 7; 8 CASTLE-state-changing commits since, 0 entries.
- `session-close\SKILL.md` step 3 says "If a **wiki** changed" — does not fire for CASTLE,
  though the skill's own description promises "wiki/CASTLE log updates."
- `service-capabilities\` — empty folder, no page, not in `index.md`.

## The recommendation under challenge

**One file owns capability state: `CASTLE\wiki\current-position.md`.** Delete `:49`. Reduce
`skill-map.md` to horizon + activation criteria with no states. Leave
`capability_development_goal.md` owning the weak-link *ranking* only.

**Rationale:** `NOW.md`'s Owners footer points at `current-position` and at none of the other
three. Making the read path and the authority path the same file is the only version of this
that survives a month of nobody looking.

**Strongest counter-argument the lead can construct against its own recommendation:**
`capability_development_goal.md` is a North Star file and outranks CASTLE by the stack in
`OPERATIONS.md` § Authority; putting capability state in CASTLE may invert that. Rebuttal:
the two hold different objects — *ranking* (which weak link is #1) vs. *state* (which rung a
capability sits on). If the challenger judges that distinction too thin to survive, the
recommendation should flip to `capability_development_goal.md` as sole owner and CASTLE
holds pointers only. **This is the real decision, and it is Chris's.**

---

## What the challenger should return

1. Which claims survive, which break, and on what evidence.
2. A ruling on the ownership question, with the counter-argument addressed.
3. Anything in the "Open state" list that is worse than the lead assessed.
4. Whether HIGH is the correct priority with the semester starting Aug 24.

*Lead's disclosure: Claim 6 is unaudited. Claims 1–3 and 5 are direct quotations from live
files. Claim 4's fast/slow split is the lead's inference from commit history, not a
statement any file makes about itself.*
