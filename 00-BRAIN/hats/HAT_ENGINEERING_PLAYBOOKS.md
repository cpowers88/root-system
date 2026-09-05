---
type: reference
timeline: reference
tags: [governance, technology, engineering]
---

# HAT_ENGINEERING_PLAYBOOKS.md — Engineering Procedures (On Demand)
### Companion to the Technology Engineer and Software Engineer hats.
### Load only the procedure whose trigger fires; do not load this entire file by default.

## Procedure: Technical Discovery and Requirements

**Trigger:** a requested build or technology change does not yet have a verified
boundary or acceptance test.

1. Name the person/process outcome and current pain in observable terms.
2. Map the current path: actors, steps, systems, state, handoffs, and failures.
3. Separate stated request from underlying requirement.
4. Record functional requirements, quality attributes, constraints, non-goals,
   assumptions, and unresolved questions.
5. Rank quality attributes by consequence; “fast, secure, scalable, cheap” without
   priority is not a usable requirement.
6. Write acceptance checks and choose the smallest provable slice.

**Output:** a compact problem frame and acceptance contract in the owning project.
Do not create a new document when the repository already has the right home.

## Procedure: Architecture and Technology Decision

**Trigger:** selecting a stack, integration pattern, data boundary, platform, or
material technical design.

1. Load the verified requirements and Operator's Recommendation Ladder when the
   decision includes build-vs-buy.
2. Inspect existing systems, skills, licenses, data, and reusable components.
3. Model the minimum necessary components and trust/data boundaries.
4. Compare at least: keep/simplify existing, configure/integrate, and custom build
   when each is plausible.
5. Evaluate delivery time, lifecycle cost, reliability, security/privacy,
   operability, portability/vendor risk, and exit path.
6. Run a spike or proof when the riskiest assumption can be tested cheaply.
7. Record decision, forces, alternatives, tradeoff, assumptions, rollback, and
   review trigger.

**Rule:** architecture is a set of consequential decisions, not a diagram or a
list of fashionable tools.

## Procedure: Implementation Slice

**Trigger:** an approved or in-scope behavior is ready to build.

1. Read repository instructions and inspect working-tree state.
2. Trace the behavior through current code, tests, data, and callers.
3. Establish the baseline or failing check.
4. State the intended files/contracts and important non-goals.
5. Implement the smallest coherent slice using existing conventions.
6. Run focused checks, then the broader relevant suite.
7. Inspect the final diff for unintended changes, secrets, debug residue, and
   unnecessary complexity.
8. Demonstrate acceptance and update documentation/state that reality changed.

**Rule:** do not stop at scaffolding while a safe, relevant step remains to make
the slice work.

## Procedure: Debugging and Root-Cause Repair

**Trigger:** a defect, failing test, unreliable behavior, or unexplained incident.

1. Capture expected versus actual behavior and impact.
2. Reproduce the failure or gather the strongest available evidence.
3. Narrow the failing boundary using logs, tests, history, or controlled probes.
4. Form one falsifiable hypothesis and run the cheapest discriminating check.
5. Repair the cause at the narrowest correct boundary.
6. Add a regression check; validate adjacent and failure-path behavior.
7. Record cause, fix, proof, residual risk, and prevention lesson candidate.

**Rule:** correlation suggests where to inspect; it does not prove cause.

## Procedure: Legacy Change or Refactor

**Trigger:** changing poorly understood, weakly tested, or high-coupling code.

1. Identify the behavior that must not change.
2. Add characterization tests or capture a deterministic baseline.
3. Find seams and isolate one responsibility or dependency at a time.
4. Separate behavior change from structural cleanup when practical.
5. Keep every step runnable and reversible.
6. Compare behavior and performance before/after; document accepted differences.

**Rule:** a rewrite is a product decision with migration risk, not the default
answer to code that is unpleasant to read.

## Procedure: Technical Review

**Trigger:** architecture review, design review, code review, or pre-merge check.

Review in this order:

1. outcome and acceptance alignment;
2. correctness and data integrity;
3. security, privacy, permissions, and secrets;
4. failure behavior, concurrency/ordering, recovery, and rollback;
5. compatibility, migration, and affected consumers;
6. tests and evidence gaps;
7. operability and maintainability;
8. complexity and cost.

Report only actionable findings. Each finding states the failure condition,
impact, evidence/location, and smallest credible correction. If there are no
material findings, say so and name any validation limitation.

## Procedure: Production or External Change

**Trigger:** deployment, migration, production configuration, publication, or an
action affecting external users/systems.

1. Confirm Chris's explicit approval and exact target environment.
2. Verify backup/recovery, migration compatibility, secret handling, and access.
3. Define pre-change health, success signal, abort threshold, rollback steps, and
   responsible observer.
4. Prefer canary, staged, shadow, or otherwise limited exposure when risk warrants.
5. Execute one controlled change; observe the defined signals.
6. Roll back when the abort threshold is met—do not improvise through damage.
7. Record outcome, version/configuration, evidence, incident if any, and next
   review trigger.

**Rule:** “the command succeeded” is not evidence that the system is healthy.

## Procedure: Operational Readiness

**Trigger:** a system is approaching real use or handoff.

Confirm, in proportion to risk:

- owner, users, support path, and service expectation;
- configuration and secrets management;
- health signals, logs/metrics, alerts, and diagnostic path;
- permissions and data retention;
- backup, restore test, failure recovery, and rollback;
- dependency/vendor failure behavior;
- runbook for start, stop, deploy, common failure, and retirement;
- cost/usage guardrails and next maintenance/review date.

**Output:** readiness verdict: ready, ready with named debt, or not ready—with the
exact blocking evidence. Do not call internal testing “production ready.”

## Procedure: Engineering Close and Asset Harvest

**Trigger:** a technical build or material slice reaches acceptance.

1. Compare outcome with acceptance checks and record exact evidence.
2. State status honestly: prototype, tested internally, pilot, production, or
   retired. Do not promote maturity by tone.
3. Capture residual debt, owner, trigger, and next exact action.
4. Ask what reusable sanitized artifact emerged: pattern, template, test harness,
   checklist, component, or case-study evidence.
5. Route the Return Packet to the owning project/realm and use Operator's Project
   Completion & Asset Harvest procedure when the whole project is complete.

**Rule:** the proof and the return path are part of the build.

---
*Modes: HAT_TECHNOLOGY_ENGINEER.md and HAT_SOFTWARE_ENGINEER.md | Universal OS: AGENT.md*
