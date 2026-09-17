---
name: study-close
description: Close a `.ROOT` study block in 60 seconds — actual hours, resume point, any returned score routed to `04-SCHOOL\FallKSU.xlsx`, and any cold miss routed to `04-SCHOOL\miss-log.md` with its error class and a re-aimed next rep. Use when a study block or class ends, a grade comes back, or a rep fails cold. For the full day-end ceremony use `session-close` instead.
---

# Close a Study Block

The instruments in `04-SCHOOL` are read every Sunday by `CASTLE\OPERATIONS.md`
§ Reviews item 4. They are only as good as what reaches them at the moment the
block ends. This is that moment, and it is 60 seconds.

**This is not the session close.** No DAILY append, no wiki log, no `NOW.md`
refresh, no health gate. Step 5 says when to escalate.

## 1. Hours, course, resume point — always

Record actual minutes worked and the course. Every hour figure in
`04-SCHOOL\semester-workload-plan.md` is an estimate by that page's own
statement; these are the measurements that replace them.

State the exact resume point — the next unrun item, never a date. If an open
row in `04-SCHOOL\miss-log.md` is older than this block's work, **that row is
the resume point.**

## 2. The two gates

Ask both, once:

- **Did anything come back graded?** → step 3.
- **Did a rep fail cold** — attempted as if graded, would not have earned full
  marks? → step 4.

**Both no: state the resume point and stop.** Most blocks end here. A block
that returns nothing and fails nothing is a complete close in two lines.

## 3. A score came back

Give Chris the exact cell, and let him type the number:

- **`FallKSU.xlsx` § GRADE TRACKER** — the `Your %` column, column `D`, on that
  course's component row. Name the row and the cell.
- **`FallKSU.xlsx` § ASSIGNMENT TRACKER** — set that item's `Status` to `Done`
  and its `Score`.

**Hand over the cell rather than writing the workbook.** `FallKSU.xlsx` carries
live formulas and the conditional formatting that turns overdue rows red; an
`openpyxl` round-trip can drop that formatting silently, and a workbook open in
Excel rejects the write anyway. One number typed by Chris costs five seconds and
risks nothing.

Read the Status column after he enters it. `WATCH` or `ACTION` earns a named
corrective block in the next weekly plan — carry it into step 5.

## 4. A rep failed cold

**Check the aid before the learner.** `.ROOT`'s own study material has taught a
wrong rule four times in five days (`miss-log.md` § A miss class that is not
Chris's). Confirm the source said what the rep assumed it said. If the aid was
wrong, fix the aid, log it as an aid defect, and re-run rather than re-aim —
the rep reproduced a vault error, not a gap.

Otherwise append a row to `04-SCHOOL\miss-log.md` with its five fields. Take the
error class from that file's own register; add a new class only when no existing
one fits, and update the count.

**The re-aimed rep is the field that matters, and it is not a re-run.** Name the
one decision or move that actually failed, then build a rep that isolates it and
strips out everything that already worked. If the miss was equation *selection*,
the next rep forces selection and supplies nothing else; re-listing the original
problem re-tests what already passed.

Build that rep from fresh parameters. A graded item — WebAssign, a lab, a quiz —
is never the re-aimed rep, and the AI boundaries in `NOW.md` § Boundaries hold
inside this step exactly as they do everywhere else.

## 5. Escalate or stop

- **`WATCH` or `ACTION` on any course** → it goes in the next weekly plan as a
  named block, and `ACTION` reaches `MORNING_BRIEF`'s ATTENTION line.
- **A miss that has now sat open across two Sunday returns** → escalate it in
  the plan; an un-re-aimed miss is the failure the log exists to prevent.
- **AI taught in this block** → `HAT_EDUCATOR` § Session close also owns a
  `hat-performance-log.md` row. Learner truth and hat behaviour are separate
  evidence.
- **The day is genuinely over** → run `session-close`.

## Done when

Every score returned in this block is entered, every cold failure has a row
carrying an error class and a re-aimed rep, and the resume point is a named
unrun item.
