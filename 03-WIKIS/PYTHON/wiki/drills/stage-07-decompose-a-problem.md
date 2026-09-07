---
type: drill
stage: 07
status: draft
concepts: ["decomposition", "pseudocode", "flowchart", "incremental-development", "test-case"]
difficulty: beginner
solution_included: false
timeline: reference
---

# Drill: Decompose Before You Code

## Objective

Practice planning a program — decomposing it into steps and writing pseudocode (or a flowchart for the branchy one) — entirely *before* writing any real Python.

## Concepts Practiced

- decomposition
- pseudocode
- flowcharts (for the branching problem)
- thinking through test cases in advance

## Starter Prompt

For each problem below, write the plan **first** — do not write any real Python code yet.

1. "Build a program that asks for three test scores and reports the average, and whether that average is a passing grade (60 or above)." — Write a numbered pseudocode list of steps.
2. "Build a simple rock-paper-scissors game against the computer." — Draw (or describe in words) a flowchart, since this has several decision points (what beats what).
3. For problem 1, write down 3 test cases *before* coding: specific sets of scores and the exact average/pass-fail result you'd expect.

Only after completing all three planning steps above, build problem 1 incrementally: write step 1's code, run it, confirm it, then add step 2, and so on.

## Requirements

- Plans must be written before any code, and kept as you build (don't throw them away once typing starts).
- Problem 1's build must be done incrementally — confirm each added piece works before adding the next. Note, in a comment or on paper, what you checked at each step.
- All 3 test cases for problem 1 must actually be run against the finished code to confirm they pass.

## Constraints

- Problem 2 (rock-paper-scissors) only needs the flowchart/plan for this drill — building it can be a follow-up exercise or folded into the mini-project.
- Use only Stage 1-6 tools (functions, conditionals, loops, basic I/O) — no new syntax needed for this drill.

## Expected Behavior

Problem 1's finished program should correctly compute the average and pass/fail status for all 3 of your pre-written test cases.

## Self-Check Questions

1. Which step of problem 1's plan, if any, turned out to need revising once you actually started coding it?
2. For problem 2, how many decision diamonds did your flowchart end up needing?
3. Did building problem 1 incrementally actually catch a bug earlier than it would have if you'd written the whole thing at once? What happened?

## Answer Policy

Do not include the final solution unless Chris explicitly requests a separate answer key and confirms this is not graded school work.
