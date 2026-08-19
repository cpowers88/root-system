---
type: handoff
timeline: now
status: active
tags: [governance, castle, handoff]
created: 2026-08-19
---

# Handoff — Codex: CASTLE full reconciliation

**From:** Claude Code, 2026-08-19 afternoon
**To:** Codex (Sol, high reasoning)
**Authorizing:** Chris, 2026-08-19 — routed here rather than to Claude because this is an
audit/validate task, because the Claude session has a *measured* miss on the target file today,
and because running it on a separate surface is what leaves Chris's remaining blocks for TCOM.

---

## Current state

Your plan at `C:\Users\chris\Documents\The strongest plan is to run the fu.md` is **approved in
content**. Claude reviewed it and endorsed **Phases 3, 6 and 7 unchanged** — the refusal to
fake-activate Phase 1, the second-session reconstruction as the strongest acceptance test, and
Aug 23 as an acceptance checkpoint rather than the first reconciliation.

**One change Chris approved: timing.** The plan runs **Friday Aug 21**, folded into the
semester-format build, not today. Reason: it would spend 60–90 minutes plus a work block on
CASTLE in a week where **TCOM is 0 of 6 blocks with three graded items on Aug 25** — breaking
the semester maintenance budget added to `CASTLE\OPERATIONS.md` *this morning* as part of
#103's own repair, and `phase-map`'s guardrail that maintenance is what shrinks when it
displaces learning. Friday still beats Aug 23 by two days, so your core argument — don't wait
four days to discover whether CASTLE works — survives intact.

## Open question / blocker

**None blocking.** Two items need Chris directly and are not yours to decide:

1. **The weekly plan's two approval gates** (learner-hub alignment, instruction protocol) are
   still unratified, so `weekly-plan-2026-08-17-to-2026-08-23.md` correctly calls itself
   provisional. Two minutes of Chris's time; do not resolve it by inference.
2. **Whether `castle_freshness.py` earns integration into `root_health.py`.** Deliberately
   deferred past Aug 24 (stale_overwrite_guard's shipping pattern). Decide at Aug 23, not now.

## Next exact action

Run Phases 1–2 of your plan on **Friday Aug 21**, then Phase 4's validation. Phase 5's
CASTLE-first test and Phase 6's return-path check follow from a genuinely fresh session.

---

## Details likely to be forgotten — YOUR PLAN'S BASELINE IS STALE

It says *"No files have been changed yet."* That was true when written. Since then, on Aug 19:

| Changed | What |
|---|---|
| `CASTLE\wiki\current-position.md` | **Two** repairs. (a) The Physics row was a day stale — row 2 now `proven (durable)` 2026-08-18, row 3 `passed (immediate)` with the check owed. (b) **`:95` Owner Pointers still routed capability state to `[[skill-map]]`** — the last surviving half of #103's loop, which you caught and Claude had missed. Now states ownership lives in the table above. |
| `CASTLE\wiki\log.md` | Resolution note appended to your own review entry (text unchanged, per append-only) — it read as pending because it was appended *after* the ruling entry. Plus a new decision entry for this afternoon. |
| `PHYSICS\wiki\current-position.md` + `log.md` | **Row 3 MISSED its durability check at 12:00 and reopened**, new window Fri Aug 21 – Sat Aug 22, error class *concept — set structure*. |
| `HAT_TCOM.md`, `HAT_EDUCATOR.md`, weekly plan | TCOM's AI policy corrected from "verify per assignment" to the syllabus's actual blanket rule. |
| Weekly plan | CSE material scope corrected — the full semester is on disk. |

### Three findings of yours, independently verified — use these, they are confirmed

1. **The weak-link contradiction is real and worse than you stated.**
   `current-position.md` § July Weak Links prints **1. SQL … 5. Python depth.**
   `capability_development_goal.md:44` ranks **1. Independent programming, 2. Calculus-based
   physical reasoning.** Physics does not appear in CASTLE's copy at all. The section opens by
   saying the ranking is owned by the goal file, then prints a stale copy underneath.
   **This is the third pointer-then-copied-state instance in that single file today** (`:49`
   deleted this morning, `:95` this afternoon, this one still live). Deleting the copy and
   replacing it with a pointer is the fix — it is *not* a re-ranking, and no ranking authority
   moves.
2. **`capability_development_goal.md` frontmatter carries `review_trigger: 2026-08-01`** —
   expired. Confirmed.
3. **This morning's opportunity re-dating was a blanket sweep**, five rows to Aug 23 regardless
   of status. Your criticism lands; a parked row and a `researching` row should not share a
   trigger. Note that no status or verdict was changed in that sweep, so you are re-dating, not
   re-adjudicating.

### A coverage gap worth a check in Phase 4

The `:95` miss is instructive: **the #103 repair and `castle_freshness.py` both hunt
state-carrying *claims* — a table, a status, a stage number. Neither inspects outbound
*pointers*.** So a file can declare itself the owner of X and route the reader elsewhere for X,
and nothing objects. A mechanical check — *does any file declaring ownership of X also contain
an outbound pointer for X?* — would have caught this at 08:00. Proposed for Aug 23; build it
only if Chris approves, it is not in your approved scope.

### Boundaries that have not moved

- `raw\` is immutable — and prohibition 1 is live: **do not sweep `(1)`-suffixed files.** One
  sits in `PYTHON\raw\lab_instructions\`.
- `88-JOURNAL` is never read.
- No push to GitHub without Chris's separate explicit approval — your plan already excludes it;
  it still holds.
- Do not activate Phase 1 before Aug 24. Your Phase 3 is right.
- **Do not close #103 from file edits.** It closes at Aug 23 only if the cockpit stayed truthful
  through actual use.

### Where the acceptance test already has data

This morning's cold Claude load *was* a partial Phase 5 — but only partial, because Chris named
the target rather than asking CASTLE to choose. It caught one stale row and missed one pointer.
Treat that as one measured data point, not as the test having run.
