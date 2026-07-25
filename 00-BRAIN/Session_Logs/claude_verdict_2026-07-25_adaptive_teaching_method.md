---
type: report
timeline: now
status: complete
tags: [learning, python, system-evolution, bootcamp]
created: 2026-07-25
---

# Claude Independent Verdict — Codex Adaptive Teaching Method

**Gate:** 2026-07-25, set by `SESSION_REPORT_2026-07-21_CODEX_ADAPTIVE_TEACHING_METHOD.md`
**Protocol:** blind — written before reading any Codex July 25 verdict. I confirmed
none existed on disk when I started. Sources read: the July 21 method report, the
July 22 evidence file, `learning-format-notes.md` (the Claude comparison lane), the
PYTHON wiki log and `current-position.md`, and the raw `.py` artifacts themselves.

## Verdict

**Adopt as the PYTHON hub's teaching loop. Do not promote it to a universal `.ROOT`
learning system yet.**

The July 21 report named four things its evidence did not support. **Two of the four
are now closed by dated artifacts I verified directly**, one remains genuinely
unmeasured, and one is structurally unmeasurable as the experiment was built. That
is enough to adopt inside the subject it was tested on, and not enough to generalize.

## What I verified myself

I did not take the code results from any report. I read all ten learner `.py` files
in `02-LIBRARY\.PROJECTS\MCP_Bootcamp\Code\` and **executed the seven
non-interactive ones**. Every one produces correct output:

| File | Written | Produces | Correct |
|---|---|---|---|
| `practice.py` | Jul 21 14:34 | `First multiple found: 7` | yes |
| `practice2.py` | Jul 21 15:08 | `15` (1+2+3+4+5) | yes |
| `practice3.py` | Jul 21 15:14 | `30` (2+4+6+8+10) | yes |
| `count.py` | Jul 22 15:32 | `7` | yes |
| `for.py` | Jul 23 09:34 | `First match:  12` | yes |
| `for2.py` | Jul 23 10:28 | `7` | yes |
| `PT.py` | Jul 23 11:36 | matches + count `10` | yes |

`password.py` and `secret#.py` need stdin so I read rather than ran them. Both are
structurally correct; `secret#.py` handles **both** exit paths — it distinguishes a
win from an exhausted-attempts loss with a post-loop conditional, which is not a
beginner-obvious construction.

**Zero defects across all ten files.** No scaffold residue, no commented-out hints,
no copied-pattern seams. Naming is consistent and personal (`value`,
`current_guess`, `secret_number`, `attempts`), which is weak but real evidence of
authorship rather than transcription.

### The July 22 blocker is resolved

The July 22 handoff recorded an open blocker: *"saved `Code/for.py` contains a
malformed compound condition and an unconditional first-iteration `break`; it does
not explain the reported output `30`."*

The live file does not match that description. Its compound condition
(`number % 4 == 0 and number % 6 == 0`) is well-formed, the `break` sits correctly
inside the `if`, and it prints `12` — the expected first match. The file is
timestamped **Jul 23 09:34**, the morning after that handoff was written, and the
PYTHON log's July 23 entry records Chris running and tracing it correctly. The
blocker was closed by Chris the next morning; the handoff simply outlived it.

## The four unproven items, re-scored

**1. Durable retention after 24–72 hours — NOW SUPPORTED.**
`practice.py` (Jul 21 14:34) was the *assisted* stop-at-7 build. `for.py` and
`for2.py` (Jul 23, 09:34 and 10:28) are cold `break` constructions written
**43 hours later**, both correct, with no notes open per the log. `PT.py` (11:36)
then combines a compound `or` condition with a counter — the two Stage 3 skills
that had needed separate cues on July 21 and 22 — in one independent build.
That is the delayed-retention test the report said was missing, and it passes.

**2. Independent cold construction of `break` or an input-controlled `while` —
NOW SUPPORTED, both.**
`password.py` (Jul 22 14:34) is the fresh password-controlled `while` transfer the
report named as the exact resume point; the log records it as completed
independently, and it correctly initializes before the loop, tests, and updates
inside. `for.py`/`for2.py` supply the cold `break`. These were the two explicitly
named blockers and both have dated artifacts.

**3. Transfer to Physics or a different task type — STILL NOT SUPPORTED.**
The syllabus-neutral Physics rep (Next Test #2) was never run. Codex's July 25
Physics session was planning and repair work and states plainly that *"no learner
mastery moved in this planning/system session."* This gap is unchanged.

**4. Superiority over Claude's teaching format — STILL NOT SUPPORTED, and not
answerable from this experiment.**
`learning-format-notes.md` flags the problem against its own lane, correctly:
Codex's lane collected an explicit pace/depth rating and a written preference
statement; the Claude lane collected no equivalent rating on the same day. The
lanes also taught **different subjects** (Python Stage 3 loops vs. MCP contracts
and SQLite), so there is no comparable rep to difference. Any claim of superiority
either direction would be manufactured. I am not making one, and I would treat a
Codex verdict that does make one as overreaching.

## The evidence conflict, stated rather than resolved

Chris's account today: the `.py` files are *"mostly from the python block written
alone, no assistance other than 'write this program as a for loop'."*

Codex's report classifies several of the same files as assisted — `practice.py`
after concept and worked-step support, `practice2.py` after rebuilding the state
model, `practice4.py` after an initialize/test/update scaffold, `count.py` after a
focused counter cue, `secret#.py` through staged live guidance.

**I am not adjudicating whose memory is right, and it does not change the verdict** —
the four artifacts carrying the decisive weight (`password.py`, `for.py`, `for2.py`,
`PT.py`) are recorded as independent in Codex's own log *and* in Chris's account, so
they survive either reading.

But the disagreement is itself a finding, and it is the most important one I have:
**support level is the method's core instrument, and it is currently recorded only
by the teacher.** A method whose whole claim is "assistance decreased over time"
cannot be validated if the learner and the teacher disagree about how much
assistance was given. That is a measurement-integrity defect, not a personality
clash, and it is cheap to fix — have Chris rate the support level himself at the
end of each rep (none / cue / worked step), alongside pace and depth. If the two
ratings diverge again, that divergence is data.

## What earns adoption

- The **cold-attempt-before-instruction** rule. Every artifact above exists because
  an attempt was demanded before teaching, which is what makes the evidence real.
- The **support-escalation ladder** (no cue → concept cue → worked step), because it
  is what produced the strongest single signal in the whole file: assistance falling
  from worked-step to independent near transfer in about five minutes on the
  accumulator (`practice2.py` 15:08 → `practice3.py` 15:14 — six minutes by
  timestamp, which independently corroborates the report's "about five minutes").
- **Adaptive routing** (Accelerate / Deepen / Rebuild) chosen from the observed
  error rather than a schedule.
- **Keeping generated prompts separate from demonstrated output**, which is why this
  verdict could be written from artifacts at all.

## What I would not adopt yet

- Promotion to a standing `.ROOT` learning skill covering all subjects. One subject,
  one stage, one learner state is not a general result.
- Any claim that this beats the live-pairing format. Unmeasured, and the experiment
  cannot measure it.
- Retiring the pace/depth rating. Pace was **2.5/5 — slightly slow** on July 21,
  which sits oddly beside Chris's recollection today of "very fast." I think both
  are true and measuring different things: session *tempo* was slightly slow, while
  *assistance decay* was fast. Keep both instruments; they are not the same axis,
  and collapsing them would tune the wrong one.

## Recommendation

1. Adopt the loop as the PYTHON hub's teaching contract and write it into the stage
   template — this is the structure the Stage 4/5 restructure should be built on.
2. Add learner-rated support level to the rep record before the next rep.
3. Run the Physics rep before any cross-domain claim. Until then the method is
   validated for Python only.
4. Close the comparison question as **unanswerable from this experiment** rather
   than leaving it open to be quietly resolved by preference later.
5. Re-check at the August decision gate against whether Stage 4 functions evidence
   accumulated the same way Stage 3 loops evidence did.

## Confidence

**High** on the retention and cold-construction findings — I ran the code and the
timestamps are independent of anyone's memory. **Moderate** on the adoption call,
because n=1 subject. **Low/none** on any comparative claim, by construction.
