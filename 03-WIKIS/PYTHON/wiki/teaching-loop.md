---
type: reference
timeline: reference
status: active
tags: [programming, governance, learning]
created: 2026-07-25
---

# Teaching Loop — How a Python Session Runs

Adopted 2026-07-25 after the July 21–25 evidence gate. Origin:
`00-BRAIN\Session_Logs\Report Archive\SESSION_REPORT_2026-07-21_CODEX_ADAPTIVE_TEACHING_METHOD.md`.
Verdict and evidence: `00-BRAIN\Session_Logs\Report Archive\claude_verdict_2026-07-25_adaptive_teaching_method.md`.
(Paths corrected 2026-07-27 — both files archived out of `Session_Logs\` root during system cleanup, content unchanged.)

**Scope: this hub only.** The method was tested on Python Stage 3 loops and is
validated there. It is not yet a general `.ROOT` learning system — no cross-domain
rep has been run.

## The loop

**1. Cold attempt first — always.**
Every topic opens with an attempt or a prediction *before* any instruction. Not a
warm-up; the real task. What Chris produces cold is the measurement, and nothing
else in this loop works without it.

**2. Escalate support only as far as the observed error requires.**

| Level | Give | Use when |
|---|---|---|
| **None** | nothing — let the attempt stand | the attempt is correct, or the error will surface on running |
| **Concept cue** | name the missing idea, not the code | one specific concept is missing and the rest is sound |
| **Worked step** | show the one step, then stop | the cue didn't land, or a prerequisite is genuinely absent |

Never jump to a worked step because it's faster. The distance between where the
attempt failed and the support given *is* the data.

**3. Route from the evidence, not from a schedule.**

- **Accelerate** — after correct independent performance, compress the explanation
  or increase transfer distance.
- **Deepen** — the foundation is working; target only the missing concept. Do not
  replay the lesson.
- **Rebuild** — reduce to the missing prerequisite, retry, and do **not** record a
  mastery claim that wasn't earned.

**4. Explain-back before moving on.**
In Chris's own words: what each variable holds, why the condition is where it is,
what ends the loop, why this construct and not another.

**5. Fresh transfer while it's hot.**
Immediately give a near-neighbor problem with no new scaffold. This is where
mastery either shows up or doesn't.

**6. Record what actually happened.**
Support level used, cold result, transfer result. Generated prompts stay separate
from Chris's demonstrated output — always, without exception. That separation is
the only reason the July 25 verdict could be written from artifacts.

## Why this loop and not the old one

Stages 0–3 were written read-concept → drill → mini-project. Chris beat that
structure rather than following it, and the evidence says why: the strongest
single signal in the whole experiment was assistance **falling from worked-step to
independent near transfer in about six minutes** on the accumulator
(`practice2.py` 15:08 → `practice3.py` 15:14, by file timestamp). Reading first
would have hidden that, because there'd have been no cold attempt to measure.

The delayed evidence is stronger still: the assisted stop-at-7 build on Jul 21
14:34 became **independent cold `break` construction 43 hours later** (`for.py`
09:34 and `for2.py` 10:28 on Jul 23), then a combined `or`-condition-plus-counter
build (`PT.py` 11:36) with no cue. All ten learner files run correctly.

## Two things to keep measuring

**Support level is rated by Chris, not only by the AI.** At the end of each rep
Chris records the support he felt he needed — none / cue / worked step — next to
pace and depth. This exists because the July 25 review found Chris's account of
assistance disagreeing with the teacher's record on five files. A method whose
central claim is "assistance decreased" cannot validate itself on the teacher's
word alone. If the two ratings diverge, that divergence is the finding.

**Pace and assistance-decay are different axes.** July 21 rated pace **2.5/5,
slightly slow**, while the same session's assistance decay was fast. Both were
true. Keep both numbers; tuning tempo when the real signal is decay would optimize
the wrong thing.

## What this loop does not authorize

- Writing code for Chris on graded CSE 1321/1321L work. The course prohibits it,
  `OPERATIONS.md` prohibits it, and generated code is never learner proof.
- Recording a stage as mastered on assisted performance. Assisted recovery and
  independent construction are different evidence classes and get logged
  differently.
- Extending the method to another subject before a rep there is measured.
