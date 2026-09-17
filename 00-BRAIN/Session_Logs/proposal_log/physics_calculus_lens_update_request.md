---
type: report
timeline: now
status: review-request
tags: [physics, education, calculus, learning-design, governance]
created: 2026-07-30
---

# Physics Calculus-Lens Update Request

> **REVIEW REQUEST — NO PHYSICS OPERATING FILES HAVE BEEN CHANGED**

## Direct Request

Review and challenge a bounded update to the PHYSICS learning engine:

> Keep the syllabus as the authority for required coverage, dates, and academic
> constraints, but make calculus reconstruction—not syllabus order alone—the
> primary instructional lens for each topic.

This is not a request to copy the PYTHON teaching loop. Physics is spatial,
mathematical, and model-based. It needs its own method.

## Why This Update Is Being Considered

Chris has already completed introductory Physics concepts and principles. His
goal this year is not another pass through formula selection and plug-and-chug
execution. It is to understand how the familiar formulas arise from physical
principles through calculus and how the mathematics describes the system.

A live July 30 session showed that the immediate constraint was calculus
mechanics recall—especially derivative/integral rules, constants of integration,
and boundary conditions—not basic Physics concepts.

The current PHYSICS architecture contains strong calculus resources, but the
normal execution path is still substantially organized as:

```text
syllabus topic -> textbook concept -> equation -> calculus connection
-> problem type -> drill -> mastery gate
```

That is appropriate for course coverage, but it risks making calculus a support
layer instead of the lens through which the Physics is reconstructed.

## Proposed Governing Relationship

```text
SYLLABUS
  controls: required coverage, deadlines, policy, exam constraints

CALCULUS LENS
  controls: how a topic is explained, derived, connected, and practiced

MASTERY EVIDENCE
  controls: when learner status advances
```

Recommended wording:

> PHYSICS is syllabus-bounded and mastery-gated, but taught through a
> calculus-reconstruction lens wherever calculus represents physical change,
> accumulation, dependence, approximation, or constraint.

The syllabus should define the destination. It should not automatically define
the best learning route for Chris.

## Proposed Topic Learning Sequence

For each calculus-bearing topic:

1. **Structured reading:** read a short, named section for the physical system,
   governing principle, assumptions, and calculus operation—not a broad chapter.
2. **Concept anchor:** state what the system is doing physically using a machine,
   construction, motion, flow, force, or energy analogy where useful.
3. **Quantities and representation:** identify variables, units, axes, signs,
   dependencies, and initial or boundary conditions.
4. **Calculus bridge:** identify whether the relationship is a derivative,
   integral, differential equation, vector operation, approximation, or
   constraint.
5. **Formula reconstruction:** derive the familiar working equation and explain
   where each term and constant came from.
6. **Assumption audit:** state what must be true for that form of the equation to
   hold.
7. **Worked problem:** solve symbolically before substituting numbers.
8. **Variation:** change one condition and predict how the model or formula
   changes.
9. **Cold proof:** reconstruct or apply the relationship later without following
   the worked example.

Topics that do not require calculus should not receive forced or decorative
calculus. The lens should clarify Physics, not add ceremony.

## Structured Reading Block

Each active topic should provide one compact reading assignment with this shape:

```markdown
## Read

- Source: exact section and pages
- Read for: the physical system and governing principle
- Calculus question: what is changing or accumulating, with respect to what?
- Formula question: which familiar equation should emerge, and under what
  assumptions?
- Stop condition: stop when those questions can be answered; do not read the
  entire chapter by default.
```

After reading, Chris should return four short statements:

1. The physical principle in plain language.
2. The relevant derivative, integral, vector relationship, or constraint.
3. The initial/boundary conditions or assumptions.
4. The resulting formula and what it means physically.

This keeps reading purposeful and makes it feed directly into construction and
problem work.

## Collaborative Markdown Problem Pages

Markdown can be the shared reasoning surface without replacing handwritten
Physics.

A collaborative problem page can hold:

```markdown
# Problem

## Given situation

## What Chris thinks first

## Diagram artifact
Linked iPad PNG/PDF:

## Governing principle

## Calculus construction

## Symbolic derivation

## Numerical work

## Physical check

## Chris's first error or uncertainty

## Correction

## Cold retest
```

Chris does not need to draw axes in Markdown. The representation should remain
handwritten on the iPad:

1. Chris draws the system, axes, vectors, signs, and first attempt.
2. He exports a PNG or PDF to the existing `wiki/handwritten/` route.
3. The Markdown problem page links to that artifact.
4. Chris and the AI build the derivation and explanation together in Markdown.
5. The original handwritten attempt remains visible as learning evidence.

Simple text or LaTeX diagrams may be supplied by AI when they help explain an
idea, but they do not replace Chris's spatial construction or count as his
mastery evidence.

## Example: Constant-Acceleration Kinematics

Do not begin with a list of three formulas to memorize.

Begin with:

```text
constant physical acceleration
-> a = dv/dt
-> integrate using the velocity boundary condition
-> v(t) = v0 + at
-> v = dx/dt
-> integrate using the position boundary condition
-> x(t) = x0 + v0*t + (1/2)at^2
```

Then establish that:

```text
v^2 = v0^2 + 2a(x - x0)
```

is obtained by eliminating time under the same constant-acceleration
assumptions, rather than by treating it as an unrelated third rule.

The instructional target is both physical interpretation and usable formula
fluency.

## Existing Assets to Preserve

- `03-WIKIS/PHYSICS/OPERATIONS.md` already defines a calculus-based engine,
  physical-context explanations, and independent mastery.
- `03-WIKIS/PHYSICS/wiki/math-readiness-path.md` already contains the active
  Calculus–Physics Bridge and existing calculus-link sequence.
- `03-WIKIS/PHYSICS/wiki/ipad-handwritten-physics-method.md` already preserves
  spatial reasoning, symbolic-first work, and corrected first attempts.
- `03-WIKIS/PHYSICS/wiki/current-position.md` remains the sole learner-truth
  authority.
- Existing concept, equation, calculus-link, problem-type, example, drill, and
  error pages remain the durable content architecture.

This proposal should tighten the relationship among those assets rather than
create another learning framework.

## Exact Files Proposed for a Later Approved Update

No edits are requested until this report is reviewed and Chris approves the
final scope.

1. `03-WIKIS/PHYSICS/OPERATIONS.md`
   - Clarify that the syllabus bounds coverage while the calculus lens controls
     instruction.
   - Add the topic learning sequence and the rule against decorative calculus.
2. `03-WIKIS/PHYSICS/HOW_TO_USE.md`
   - Add the compact structured-reading block.
   - Add the Markdown-plus-iPad collaboration workflow.
3. `03-WIKIS/PHYSICS/wiki/current-position.md`
   - State Chris's durable objective: calculus-connected reconstruction and
     formula fluency, not introductory concept repetition.
   - Ensure the August 24 return resumes a revised method rather than reverting
     to syllabus-led pedagogy.
4. `03-WIKIS/PHYSICS/wiki/math-readiness-path.md`
   - Preserve the current 25-evening bridge.
   - Make its output feed the relevant Physics topic and formula explicitly.
5. `03-WIKIS/PHYSICS/wiki/ipad-handwritten-physics-method.md`
   - Add only a short pointer describing how a handwritten artifact connects to
     a collaborative Markdown problem page.

No new top-level folder, wiki, general education framework, or application is
proposed.

## Questions for Claude's Review

1. Does this correctly distinguish course coverage from instructional method?
2. Does the calculus lens match Chris's stated learning objective without
   weakening practical problem-solving or formula fluency?
3. Which current PHYSICS rules would conflict with this change?
4. Is the five-file change the smallest coherent implementation?
5. How should structured reading be inserted without making every topic page
   repetitive?
6. Should collaborative Markdown problem pages be temporary session artifacts,
   reusable worked examples, or promoted only after a cold retest?
7. What safeguard would prevent excessive derivation from displacing the
   course problems Chris must still solve efficiently?
8. What exact acceptance test should be passed before the revised method becomes
   the durable post-August-24 path?

## Proposed Acceptance Test

Before adopting the update broadly, test it on one bounded Physics relationship:

1. Chris completes the structured reading block.
2. Chris creates the diagram and first attempt on the iPad.
3. Chris and AI construct the derivation in one Markdown problem page.
4. Chris solves one application problem.
5. Two days later, Chris reconstructs the relationship or solves a transfer
   problem cold.
6. Chris states whether the method improved conceptual connection, formula
   recall, and problem-solving speed.

Accept the method only if the cold result improves without making the study block
unreasonably longer. Otherwise revise the method before changing PHYSICS
governance.

## Requested Decision

Claude should return one recommendation:

- **ACCEPT** the bounded five-file update;
- **REVISE** it with exact changes and reasons; or
- **HOLD** it because the current Calculus–Physics Bridge needs more learner
  evidence first.

