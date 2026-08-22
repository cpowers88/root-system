---
type: report
timeline: now
register: system-review
status: proposed
tags: [governance, castle, flag-103, optimization]
created: 2026-08-19
---

# CASTLE Repair and `.ROOT` Optimization — Claude's Independent Report

### Commissioned by Chris 2026-08-19, alongside a Codex second opinion. Per `AGENT.md` § One AI Team rule 6, this document is the lead's integration: my own analysis first, the reconciliation with Codex named explicitly, one decision list at the end.

**Evidence base:** flag #103 and its challenge packet
(`claude_challenge_packet_2026-08-19_castle_ownership.md`), the 2026-07-19 CASTLE
reconciliation, the 2026-07-24 architecture update, the 2026-08-11 Council verdict,
`ROOT_CAPABILITY_CONTRACT.md`, `CASTLE\OPERATIONS.md`, git history through `9aa9a71`,
and the live CASTLE wiki read in full this morning.

---

## 1. What CASTLE is contractually — the target we are repairing toward

`ROOT_CAPABILITY_CONTRACT.md` gives the System Loop one owner per stage. CASTLE owns
exactly one: **DECIDE** — "maps, profit gate, opportunity queue, `NOW.md`."

That is the whole job. Watchtower senses; wikis research and hold learner truth;
projects build; drills prove; reviews learn. CASTLE receives all of it and answers one
question: *what is the highest-value next action; who owns it; what proof closes it;
where does the result return?* It holds **sequence and proof status, never duplicate
domain evidence** (Standing Rule 2).

So the repair target is not "make CASTLE bigger" or "make CASTLE current everywhere."
It is: **make the DECIDE stage cheap to keep true.** Every proposal below is tested
against that.

## 2. Root cause — three failures, not one

Flag #103 (the ownership loop) is the finding that started this, but repairing it alone
would not have prevented the last month. Three distinct mechanisms failed:

### 2a. Ownership: capability state has three homes and therefore none

The measured loop (#103, quotes in the challenge packet): `skill-map:20` claims to be
the only home → `current-position:49` names skill-map live truth → `:53` hands the
ranking to `capability_development_goal.md` → its line 19 returns "proof status:
CASTLE." Cost: the "live truth" register is 21 days wrong about Python. The defect is
a **repeat** — the 2026-07-19 review diagnosed the identical failure in
`PRE-SEMESTER_PREP_PLAN.md`, prescribed *"gates + pointers, no copied state,"* and then
added the `:49` line as an "optional polish" the same day.

### 2b. Cadence: the reviews that read the slow layer stopped running

CASTLE has two speeds. The fast layer — `NOW.md`, weekly plans, hub frontiers — is
read daily and stayed healthy through Aug 7 (Chris's July 28 journal note of a system
"running wonderfully" was an accurate reading of it). The slow layer — the maps,
registers, queue, phases — is read **only by the review cadence**. That cadence died:

- Last weekly report: `WEEKLY_AUGUST3-9.md`. None for Aug 10–16 or 17–23.
- The July monthly was an explicit early close (Jul 25) whose "next packet" was never
  written; Phase 0's exit checkbox points at an "August 1 monthly review" that
  therefore never existed.
- `OPERATIONS.md` § Reviews and Routing requires Sunday planning to **open with the
  due-`check_at` return** — but `templates\weekly-plan-template.md`, the file a
  Sunday session actually copies, carries no such section. The Aug 16 Sunday produced
  a full plan and skipped the due-checks, exactly as the template predicts.
- Consequence measured today: 4 opportunity-queue rows past their review dates
  (Aug 1, Aug 14 ×2, Aug 16 — the last one Chris approved advancing on Aug 2), one row
  with no date at all, Phase 0 `active` past its window with Phase 1 opening Aug 24.

This is `AGENT.md` ED7 failing on CASTLE's own pages: dated triggers, no assigned
evaluator at the moment of evaluation.

### 2c. Detection: no instrument measures slow-layer staleness

The Aug 11 Council's C1/C2, verified still true: the vault's validators confirm
*presence and internal consistency*, never *freshness or function*. `root_health.py`
passed this morning — 0 blockers across 1,559 files — over a cockpit whose central
register was three weeks wrong and whose queue held five dead triggers. Everything
that finally surfaced #103 was a human-directed manual read. The Council's step 3
(the proof instrument) was the remedy for this class and is one of the two items from
its sequence that never shipped.

**Why all three matter:** 2a made the maps rot; 2b removed the process that would have
noticed; 2c means nothing mechanical notices when 2b fails. Codex's recommendation
repairs 2a. Repairing 2a alone recreates July 19 — a correct map with nobody assigned
to notice when it rots again.

## 3. The recommendation

### R1 — Ownership (agrees with Codex; the wording below is the implementable form)

1. **`CASTLE\wiki\current-position.md` is the single home of cross-domain capability
   state** — which proof rung each active capability sits on, per the ladder
   (explain → guided → independent → integration → real workflow → client outcome →
   asset).
2. **Delete `current-position.md:49`** (the skill-map-is-live-truth line).
3. **`skill-map.md` keeps horizons and activation criteria only** — the eight category
   tables and the Activation Rule stay; the Active Capability Register's *state* column
   moves to current-position; the register table itself is replaced by a pointer. Not
   retired: it remains the map of what could activate and what proof activates it.
4. **`capability_development_goal.md` keeps the weak-link *ranking* only** — which gap
   is #1 is a different object from what rung a capability sits on. Its line 19 is
   reworded so "proof status: CASTLE" names `current-position.md` explicitly.
5. **Copied-state rule, applied to CASTLE itself:** any fact current-position quotes
   from a hub carries its as-of date and owner link. Learner *stage numbers* are cited
   ("per PYTHON current-position, 2026-08-19"), never restated bare — the July 19 cure,
   this time without the polish that undid it.

*Why current-position and not `capability_development_goal.md` (the counter-argument
from the challenge packet, resolved):* the goal file is North Star territory and
outranks CASTLE — but it owns the *ranking question*, reviewed monthly. State is a
sequencing object, updated whenever proof moves, and `NOW.md`'s Owners footer already
points at current-position. Making the read path and the authority path the same file
is the property that survives a month of nobody looking. The authority stack is not
inverted because the two files hold different objects.

### R2 — Cadence (beyond Codex's recommendation)

6. **Put the due-checks return into the weekly plan template.** One new section at the
   top: *"Due checks this week"* — every `check_at`/review date due, opportunity rows
   at or past review, any phase whose window opens or closes, the two approval gates
   (learner-hub alignment, instruction protocol). The rule already exists in
   `OPERATIONS.md`; this puts it in the file a Sunday session actually copies. Same
   failure class and same fix shape as the `session-close` step-3 defect.
7. **Fix `session-close\SKILL.md` step 3** to read "If CASTLE or any domain wiki
   changed…" and re-sync the mirrors.
8. **Log discipline, ruled not drifted-into: the CASTLE log records decisions, not
   sessions.** Its own history supports this — profit gates, protocol activations,
   plan conversions. Backfill exactly two entries (Aug 16 Week D re-anchor, Aug 17
   OK TO START); the other six unlogged commits were maintenance and stay in the
   DAILYs.
9. **Semester maintenance budget, stated in `OPERATIONS.md`:** the Sunday due-checks
   return (~15–30 min) plus the monthly reconciliation (one session). Nothing else is
   scheduled CASTLE work during the semester. The phase-map's own guardrail — *"if
   CASTLE maintenance displaces learning, reduce the maintenance scope"* — becomes
   enforceable only when the scope is named.

### R3 — Detection (beyond Codex's recommendation; the part that makes R1 durable)

10. **A deterministic CASTLE freshness check**, added to `root_health.py` (or a small
    `castle_freshness.py` it calls), run by the existing morning-brief generation and
    session close. Four checks, all mechanical:
    - `current-position.md` reconciled date ≤ 35 days old;
    - no `opportunity-queue.md` review date in the past without a same-row disposition;
    - no phase page `status: active` whose window closed > 14 days ago, and no
      `status: planned` phase whose window opened;
    - `CASTLE\wiki\log.md` has an entry within 14 days whenever git shows
      CASTLE-state-changing commits in that window.

    A failure emits one ATTENTION line in `MORNING_BRIEF.md` — the surface Chris
    already reads. `MORNING_LAUNCH_INSTRUCTIONS.md` already requires the brief
    generator to read CASTLE's current-position and opportunity queue, so this is
    giving an existing read a teeth, not adding a new surface. Estimated cost:
    2–3 hours, patterned on `stale_overwrite_guard.py`. This is the Council's step 3
    scoped down to the single subsystem where staleness was just measured to cost a
    month — and it converts this entire failure class from "noticed by accident" to
    "detected at gate."

### R4 — Immediate state repairs (mostly scheduled for Aug 23 already)

11. **Close Phase 0 now.** Move its D2L-data criterion to Phase 1 (which already owns
    the same outcome in two of its own exit criteria); record the Aug 1 review
    checkbox as superseded by the Jul 25 early close + Aug 11 Council. Open Phase 1
    on Aug 24 with `status: active`.
12. **Aug 23 pass, in this order:** full monthly reconciliation of current-position
    (already scheduled) → implement R1's file edits → sweep the five queue rows →
    the two log backfills → template and skill fixes (R2) if not already done.
13. **Do not:** relocate CASTLE (retired 2026-07-25, stays retired); build any new
    dashboard, register, or folder; restructure anything. The Council's T2 resolution
    binds here — this vault reliably does architecture instead of output, and the
    repair must not itself be the failure mode. Everything above edits existing files
    except one ~100-line check script.

## 4. Reconciliation with Codex — per rule 6

**Agreement, arrived at independently (this is genuine convergence, not deference):**
all five bullets of Codex's recommendation — Watchtower senses / wikis hold truth /
CASTLE decides, sequences, and governs `NOW.md` / current-position as the single
capability register / skill-map retained as horizon-and-activation map / the goal file
ranks without duplicating state. My pre-packet recommendation and Codex's differ only
in that I had proposed reducing skill-map harder; Codex's "not retired" framing is
better — the horizon tables and activation criteria are real content with no other
home, and deleting them would be motion, not repair. **Adopted.**

**Named disagreement — incompleteness, not error:** Codex's recommendation repairs
ownership (2a) and is silent on cadence (2b) and detection (2c). The evidence says the
ownership defect ran unnoticed for a month *because* 2b and 2c were already broken:
correct-map-plus-no-evaluator is exactly the state the system was in on July 20. If we
ship R1 without R2/R3, the honest forecast is a correct cockpit in August and this
same conversation in November — mid-semester, at higher cost. R2 costs two small file
edits; R3 costs one evening. They are the cheap half and the durable half.

**One caution I hold against both of us:** every mechanism in this report is prose
until the template edit, the skill fix, and the freshness check actually exist. The
Council's C4 finding — *"knowledge that converts into a governance rule gets applied
within days; knowledge that requires building something stays on the page"* — applies
to this report. R3 is the only item here that requires building something. Track it
accordingly: if everything ships except the check script, C4 claimed another one.

## 5. On the time-saving claim

Chris's expectation — that this repair saves substantial semester time — is supported,
with honest bounds. Three mechanisms:

- **Re-derivation stops.** This morning spent ~2 hours of session work re-deriving
  state the cockpit should have held. Every future session that trusts the cockpit
  instead of auditing it saves that. At even one such episode a month, the repair pays
  for itself before Unit Exam 1.
- **Wrong-work stops.** A stale frontier sends sessions at closed stages and drills
  already proven (the register would have had Chris "in Stage 4" three weeks after he
  closed it). During a 13-credit semester the scarce unit is the study block; a wrong
  block is unrecoverable.
- **Trust compounds.** The "system feels off" cost of the last week was not hours, it
  was Chris auditing his own instruments instead of using them. A cockpit with a
  freshness gate is one he can stop checking.

Against this: ~15–30 min every Sunday plus one evening for the check script. The
asymmetry is large and favors the repair.

## 6. Decisions for Chris

1. **Ratify R1** (ownership: current-position sole state home; :49 deleted; skill-map
   horizon-only; goal file ranks only). Codex and Claude agree; this is the settled
   part. — *recommend YES*
2. **Ratify R2 + R3** (template due-checks section; session-close fix; log = decisions;
   named maintenance budget; the freshness check). This is the part beyond Codex's
   recommendation and the part I argue makes R1 durable. — *recommend YES; if trimming,
   cut R3 last, not first*
3. **Phase 0 close as specified in R4-11** — criterion moved, not deleted; close on
   work that happened. — *recommend YES, today or Aug 23, before Aug 24*
4. **Flag #103 disposition:** on ratification, #103's fix lands partly in-session
   (R1 edits) and partly Aug 23 (R4-12); the flag closes when the freshness check
   passes against the reconciled cockpit — verified fix in target files, per the
   flag rules. — *recommend this closure standard*

Nothing in this report is implemented. The only prior in-session change is flag #103's
registration in `SYSTEM_FLAGS.md` (this morning, already recorded).
