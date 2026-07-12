---
type: error-log
stage: 07
status: draft
tags: [stage-07, errors, process-mistakes]
---

# Stage 7 Common "Errors" (Process Mistakes, Not Tracebacks)

This stage's mistakes are mostly process problems, not Python errors with messages — they show up as wasted time, confusion, or programs that are hard to fix.

## 1. Writing the whole program before running any of it

**Symptom:** dozens of lines written at once, then the first run produces a wall of confusing behavior or a traceback that's hard to localize.

**Why it happens:** skipping incremental development — there's no way to know which of the many new lines caused the problem.

**Fix:** go back to building one step at a time, confirming each before adding the next (this stage's whole point).

## 2. Skipping the planning step entirely

**Symptom:** getting partway through coding and realizing the approach doesn't actually work, or forgetting a whole piece of the original problem.

**Why it happens:** decomposition wasn't done first, so the "map" of the problem was being discovered live, mid-code.

**Fix:** stop, write the decomposition/pseudocode now (even partway through), then resume.

## 3. Vague pseudocode that doesn't actually help

**Symptom:** a pseudocode step like "handle the game logic" that doesn't tell you what to actually type.

**Why it happens:** the decomposition stopped too early — that "step" is really still a whole sub-problem.

**Fix:** decompose that step further, until each one is concrete enough to code directly.

## 4. No test cases, just "eyeballing" the output

**Symptom:** a program that "looks right" but has a subtle bug nobody caught because nobody checked a specific expected answer.

**Why it happens:** no test case was written down in advance to compare against.

**Fix:** before considering something "done," write down at least one specific input and its exact expected output, and check it.

## How to Read Any of These

Unlike Stage 6, none of these produce an error message — they're symptoms you notice in your own process: confusion, getting stuck, or a program that "mostly" works. The fix is almost always to step back to the planning phase, not to push forward by guessing.

## Related

- [[concepts/decomposition-and-pseudocode]]
- [[concepts/incremental-development-and-testing]]
