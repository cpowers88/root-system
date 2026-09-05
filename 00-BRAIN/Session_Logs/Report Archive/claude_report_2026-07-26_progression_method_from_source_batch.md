---
type: report
timeline: now
status: complete
tags: [castle, learning, method, source-synthesis, system-evolution]
created: 2026-07-26
---

# A Progression Method, Sourced from the July 24 Book Batch

**Question asked:** what do the eight sources say about staged learning, mastery
gating, and retrieval — and how should it be implemented in what Chris has now,
to evolve toward what he wants to become?

**Sources read for this report:** the complete `ai-engineering`,
`ai-builders-handbook`, and `prompt-engineering-for-llms` intakes, plus the
index and targeted sections of `agentic-ai-for-engineers`. All are CASTLE
source-summaries from the 2026-07-24 batch (3,789 physical pages, 8 reports).

**Boundary this report respects:** the intake index states these reports
authorize no move, validator, metadata, or governance change on their own. This
is a method proposal for Chris's decision. Nothing here is adopted.

---

## The One-Sentence Finding

Every one of these books, written about machine systems, independently arrives at
the same three rules — **define the test before you build, score components not
totals, and add complexity only when a measured failure demands it** — and those
three rules describe mastery-gated learning exactly. Chris's system already
implements roughly two-thirds of this. The July failures were not gaps in the
method; they were places where a calendar, a plan, or an unchecked assumption was
allowed to override a gate the system already had.

That is the useful news. **This is a tightening job, not a rebuild.**

---

## Part 1 — What the Sources Actually Say

### 1.1 The gate is written before the work starts

Huyen names **"evaluation-driven development"** — defining evaluation criteria
before building, explicitly by analogy to test-driven development — and states
the consequence bluntly: *a deployed application nobody can evaluate is worse
than one never shipped; it costs to maintain and may cost more to remove.*

The learning translation is exact. **A stage opened without its gate written is
worse than a stage not started** — it consumes weeks and produces a feeling of
progress that no evidence supports.

Chris already does this. Every PHYSICS stage packet carries a Mastery Checklist
and a "Do Not Move On Until" clause, written before the stage was ever studied.
The defect this month was not a missing gate — it was the CASTLE weekly plan
scheduling a "cold Stage 4 checkpoint" for a Friday after teaching only 8 of the
13 checklist items. **The calendar was allowed to name a gate it hadn't earned.**

### 1.2 Never one aggregate score

Huyen decomposes evaluation into four buckets — domain-specific capability,
generation capability, instruction-following capability, and cost/latency — and
states that *a single aggregate "quality" score conflates these and cannot be
debugged.* He adds the pipeline rule: *evaluate every component independently; a
multi-step pipeline's end-to-end failure can originate in any stage, and only
per-component evaluation localizes it.*

"I got the physics problem wrong" is an aggregate score. It cannot be acted on.
The debuggable version asks which component failed: situation classification,
diagram, model selection, symbolic setup, unit handling, arithmetic, or the
reasonableness check.

**Chris's system already has this and should be told so.** The Stage 4 gate names
eight required evidence components, and every stage has a `common-errors` page
that classifies misses by type. This is the book's recommendation, already built.

### 1.3 Discrimination is not generation — the most important finding here

Huyen: *close-ended reformulation (multiple choice, classification) is easier to
verify than open-ended generation, but measures discrimination — "is this answer
better than that one" — not generation ability.* He notes MCQ scores are
additionally sensitive to incidental formatting.

This is precisely the July 22→23 `for.py` lesson, arrived at independently by a
book about language models. **Tracing a loop correctly and writing one cold are
different capabilities.** Recognizing a correct projectile setup and producing one
from a blank page are different capabilities.

It is also why Codex's proposed Stage 3 gate — *one fresh no-hint
loop-and-accumulator build from a plain-English problem* — is the right gate and a
trace exercise would not be. The gate must be generative because the claim is
generative.

### 1.4 The evaluation maturity ladder — permission to stay small

Berryman and Ziegler lay out an explicit ladder: ad hoc playground tinkering →
**example suite** (5–20 hand-picked representative inputs, run and diffed by eye,
*deliberately not automated pass/fail*) → full evaluation harness (hundreds to
thousands of examples, automated scoring, only once statistical power matters).

Their stated implication: **a small hand-curated example suite is a legitimate,
low-cost first evaluation step — it does not need to wait for a "real" test suite
to have value.**

Read that as written. Chris is a single learner with one subject active. **The
correct instrument at his scale is 5–20 representative problems per stage,
eyeballed.** Not an assessment system. This is the source giving explicit
permission to stop building infrastructure, from the book most likely to
recommend building it.

### 1.5 SOMA — a complete, adoptable rubric format

Berryman and Ziegler's named recipe for disciplined assessment:

- **S**pecific questions — ask about one independently verifiable aspect at a
  time, never "is this good."
- **O**rdinal scaled answers — a 1–5 scale with *an explicit written description
  of what each point means*. Never yes/no, because yes/no invites inconsistent
  private thresholds.
- **M**ulti-**A**spect coverage — decompose quality into named, separately scored
  aspects, since one response can be right on one axis and wrong on another
  simultaneously.

Plus a mechanical detail: **the rubric must be seen before the example being
graded**, because the reader moves forward once and cannot backtrack.

This is the direct fix for the measurement-integrity defect found in the July 25
verdict — support level being recorded only by the teacher, with Chris and Codex
disagreeing about how much help was given. SOMA supplies the format: Chris rates
support on an ordinal scale with written anchors (0 = no cue, 1 = concept cue,
2 = worked step, 3 = built with me), separately from pace and depth, recorded
before reading the AI's assessment.

### 1.6 Self-assessment is measurably biased — and there is a specific fix

Two findings that bear directly on how Chris's two-AI setup should run:

- *A model asked to grade its own output directly is measurably worse than the
  same model asked to grade a nominally third-party response — even when it is in
  fact grading itself.* Framing the work as someone else's produces more objective
  results.
- *If the same model that generates the test examples also produces or judges the
  candidate solutions, the evaluation is structurally biased toward that model.*

Today supplied live evidence for the first. My blind verdict on the MCP lane
missed three defects that Codex's independent pass caught, including a real
relative-path bug and an attribution I could not support. The blind-verdict
protocol is not ceremony — it is the documented control for a documented bias.
**Keep it, and add the second rule: the AI that writes a drill should not be the
AI that grades it.**

### 1.7 Start simple; the last mile is nonlinear

Huyen's stated selection principle: *start simple, then add complexity only to
address observed limitations.* The Builder's Handbook names the failure modes
directly: *a technology without a defined problem, no measurable baseline, no eval
discipline, and an oversized agent.*

And Huyen's warning about schedule: *the last mile is nonlinear — an impressive
demonstration may be quick, while the remaining reliability and operational work
can take months. Milestones must not extrapolate linearly from demo speed.*

That paragraph predicts the MCP bootcamp's exact shape. Days 1–4 produced visible
artifacts in four days. Days 5–8 were the last mile — tests, logging, security,
integration — and the plan extrapolated linearly from the demo pace. Eight lenses
in eight days was, in the Handbook's own vocabulary, an oversized agent.

### 1.8 Progressive context — and Chris's own recorded idea

The Handbook: *context windows, attention limits, and "lost in the middle"
behavior make information selection an architectural concern.* Its prescription is
just-in-time assembly — keep stable rules available, load current task context
directly, retrieve supporting evidence on demand, summarize older state.

Chris already wrote the right version of this, inline in that same intake file:

> *"we should move to a format where you tell me where in the book to obtain
> information and you worry about mapping the path forward rather than keeping
> track of what every piece of information is."*

That is progressive context, stated in his own words, and the sources support it.
It is also already running: the Evening Reading names a file, a physical page, a
focus, and a stop point rather than summarizing the content. **The method he asked
for is the one he already invented and partially deployed.**

It is equally the argument against building Stages 10–18 today: 78 pages generated
five stages ahead of need, against a Section 54 calendar nobody has seen, is
exactly the whole-vault context dumping the Handbook rejects as a default.

### 1.9 The single largest available upgrade: failures become fixtures

The Handbook, stated plainly: *a corrected failure should become a regression
fixture tied to the page, prompt, or workflow that caused it — not only a prose
lesson in a log.* Its improvement loop is: **trace failure → classify it → add it
to the eval set → change the system → rerun → observe.**

Right now, Chris's misses become prose. The `for.py` failure became a log entry.
The `%`/`_` wildcard defect became a flag. Flag #80 became a paragraph. All
correctly recorded, none of them retestable.

**Converting a miss into a permanent retest item is the highest-leverage change
available to this system**, and it costs one line per miss. It applies identically
to physics errors, Python defects, and system flags.

### 1.10 "Created is not operated" — the drift signal that names Chris's vault

The Handbook lists drift signals: *stale eval datasets, unreviewed guardrail logs,
rising unexplained cost, unresolved quality disagreement, and **features growing
faster than tests**.*

That last one describes `.ROOT` precisely: 1,429 files, 18 generated physics
stages, 8 bootcamp lenses planned — and one learner, whose demonstrated position
is Stage 4 physics and Stage 3 Python. The source's own phrase for this is
*"'created' is not the same as 'operated.'"*

This is not a criticism of the build-ahead. It is the named diagnostic for why the
system feels like it needs constant maintenance: **the built surface has outrun the
tested surface**, so status claims drift — which is exactly the defect found in the
PHYSICS control table this morning and in the July architecture update before it.

### 1.11 The value side — what "maximum value" actually resolves to

Chris's framing was *"how to produce max value from work and knowledge."* The
sources answer this concretely, and the answer is not "learn more AI."

- Huyen: *record the human baseline. "Faster" is meaningful only relative to the
  workflow being replaced or assisted.*
- Huyen: *internal-facing and closed-ended applications are safer initial
  deployments because mistakes are observable, evaluation is easier, and human
  correction is close at hand.*
- Huyen: *defensibility can come from technology, data, distribution, workflow
  integration, or accumulated usage insight. A thin feature resting on a temporary
  base-model limitation is vulnerable to being absorbed by a model provider.*
- Handbook: *a production design has four linked layers — named user and pain,
  measurable outcome, narrow AI intervention, and operating controls.*
- Handbook: *augment before automate. High-value patterns are narrow knowledge
  assistance, document processing, coding help, support, and research. Fully
  autonomous systems remain the exception.*

Put together: **the defensible layer is not the AI. It is the workflow knowledge
and the measured baseline.** Chris's construction experience — knowing what a
change order actually costs in lag, what crew oversight actually leaks — is the
part a model provider cannot absorb. The AI is the narrow intervention in the
middle, and it is the replaceable part.

This has one uncomfortable and correct implication. Of the four layers the
Handbook requires, Chris currently has strong material for the first (named user
and pain, from `observation_one.md`) and none for the second (measurable outcome
against a human baseline). **The B2 change-order conversation is the missing
layer**, and no amount of technical capability substitutes for it.

---

## Part 2 — What to Install, and When

### Install now — under an hour, total

| # | Change | Where | Cost |
|---|---|---|---|
| 1 | **Mastery gates the move, not the calendar.** A weekly plan allocates hours; it cannot hold a finished unit open or license leaving an unfinished one. | `PHYSICS/wiki/learning-path.md` | **done today** |
| 2 | **Learner-rated support level on every rep**, SOMA-style: ordinal 0–3 with written anchors, recorded by Chris before reading any AI assessment. | the rep record in each hub's `current-position.md` | 10 min |
| 3 | **Every miss becomes a retest item** in that stage's pool, not only a log line. One line per miss. | stage packets + `log.md` convention | 15 min |
| 4 | **The AI that writes a drill does not grade it.** Extends the blind-verdict protocol that already works. | `AGENT.md`, one line | 5 min |
| 5 | **A stage may not open until its gate is written.** Already true in PHYSICS; make it explicit so no plan can override it again. | `AGENT.md` or hub OPERATIONS | 5 min |

Items 4 and 5 fold naturally into the two-line `AGENT.md` edit already staged from
this morning's verdicts. That makes it four lines, still not a rewrite.

### Install at the August 2 or August 16 gate — only if evidence supports it

6. **A 5–20 problem example suite per active stage**, eyeballed, not automated.
   Build it for Stage 4 first and only extend if it proves useful.
7. **Four-bucket error decomposition** for physics and Python misses, replacing
   any aggregate "got it wrong."
8. **A stated cadence**: weekly evidence review, monthly method review. The
   Handbook's full four-tier cadence is enterprise-scaled; two tiers fit here.

### Do not install

- A full evaluation harness, automated scoring, or inter-rater statistics
  (Kendall's Tau). Real methods, wrong scale — Chris is n=1.
- The 78 Stage 10–18 pages, until Section 54's real calendar exists.
- A vault-wide instruction audit. The vault's tested surface is already behind
  its built surface; adding more built surface makes the named drift signal worse,
  not better.

---

## Part 3 — The Honest Assessment

**What the system already gets right, confirmed by eight independent sources:**
gates written before stages open; per-component error classification; immutable
raw evidence with provenance; read-only tools before write permissions; blind
independent verdicts; progressive context in the Evening Reading; human approval
on consequential actions; small reversible changes.

That is a substantial list, and most of it was built before these books were read.

**What is genuinely missing:** failures do not become fixtures; support level is
measured by the teacher rather than the learner; and there is no measured human
baseline on the business side, which is the one gap no technical work closes.

**What the sources say about the shape of the last two weeks:** an oversized
sprint with linear milestones extrapolated from demo pace, on a system whose built
surface already exceeded its tested surface. Both books name that pattern
explicitly as a common failure mode. It is not a character finding — it is a
documented, predictable engineering failure, and it has a documented fix, which is
to make the next thing smaller and gate it.

**The direction this points, toward what Chris wants to become:** the Advisor-
Builder thesis survives contact with these sources, but with the emphasis moved.
The durable asset is workflow knowledge plus measured baselines; AI is the narrow,
replaceable intervention in the middle. Which means the highest-value next action
is not more MCP, more physics build-ahead, or more system architecture — it is one
conversation with a contractor about what a change order actually costs him.

That conversation has been approved since July 22 and is still the open item.

---

*Method proposal only. Adoption is Chris's call; if adopted, items 1–5 belong in
their owning files and this report should be superseded by a CASTLE method page
rather than cited indefinitely from `Session_Logs`.*
