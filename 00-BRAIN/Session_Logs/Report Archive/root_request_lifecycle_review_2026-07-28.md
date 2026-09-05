---
type: report
timeline: reference
status: complete
tags: [governance, system-review, ai-automation]
created: 2026-07-28
---

# `.ROOT` Request Lifecycle Review

## Executive Verdict

The GitLab support lifecycle is a useful **request-handling lens** for `.ROOT`,
but it should not become a second operating loop.

`.ROOT` already has:

- one canonical lifecycle: the **System Loop** in
  `01-NORTH_STAR/System Contracts/ROOT_CAPABILITY_CONTRACT.md`;
- one information-state view: Intent through Learn in
  `ROOT_INFORMATION_FLOW_CONTRACT.md`;
- one session protocol:
  `ORIENT -> ROUTE -> WORK -> PROVE/PACKAGE -> CLOSE`;
- one five-field Return Packet;
- named owners for direction, routing, research, builds, proof, and system
  learning.

The best use of the GitLab pattern is therefore a compact checklist or visual
interface over those existing controls:

```text
CAPTURE -> ROUTE -> AUTHORIZE -> DIAGNOSE
        -> RESOLVE -> VALIDATE -> CLOSE -> IMPROVE
```

It may help a human or AI handle one request consistently. It may not redefine
the `.ROOT` System Loop, create new ownership, add new metadata, or become a new
required logging burden.

## Scope and Evidence

Reviewed live:

- `00-BRAIN/AGENT.md`
- `00-BRAIN/CODEX.md`
- `00-BRAIN/CHRIS_CORE.md`
- `00-BRAIN/SYSTEM_FLAGS.md`
- `01-NORTH_STAR/NORTH_STAR.md`
- `01-NORTH_STAR/System Contracts/ROOT_CAPABILITY_CONTRACT.md`
- `01-NORTH_STAR/System Contracts/ROOT_INFORMATION_FLOW_CONTRACT.md`
- `01-NORTH_STAR/Goals & Milestones/CURRENT_STRATEGY.md`
- `00-BRAIN/CASTLE/OPERATIONS.md`
- `.ROOT/NOW.md`
- `00-BRAIN/WHERE_IT_GOES.md`
- `00-BRAIN/Session_Logs/README.md`
- the July 19 information-system reconciliation packet;
- the July 20 wording and production-direction audit;
- the July 24 architecture evidence refinery.

No private or raw material was read. No operating instruction, governance
contract, folder structure, metadata schema, or active task state was changed.

## Existing Architecture

### Whole-system lifecycle

```text
SENSE -> RESEARCH -> TEACH -> STRUCTURE -> DECIDE -> BUILD -> PROVE
  ^                                                        |
  |                                                        v
EVOLVE <- REVIEW <- LEARN <- MEASURED OUTCOME <- DEPLOY / USE
```

This describes what the complete capability-and-value system does over time.

### Information states

```text
Intent -> Capture -> Trust -> Structure
       -> Understand -> Decide -> Act -> Learn
```

This describes where one meaningful item is and what transformation comes
next.

### Session protocol

```text
ORIENT -> ROUTE -> WORK -> PROVE/PACKAGE -> CLOSE
```

This describes how one bounded working session proceeds.

### Return contract

Every meaningful operation returns:

1. outcome;
2. evidence link;
3. capability or status movement;
4. reusable-asset candidate;
5. system-learning candidate.

These layers already cover the substance of the proposed request lifecycle.
The missing opportunity is not another architecture. It is a simpler
human-facing view of the controls that already exist.

## Proposed Mapping

| Request lens | Existing `.ROOT` mechanism | Primary question |
|---|---|---|
| Capture | Intent/Capture states; `77-INBOX`; current user request | What entered, from whom, and what outcome is wanted? |
| Route | ORIENT/ROUTE; `WHERE_IT_GOES.md`; realm owners | Who owns truth, work, proof, and return? |
| Authorize | North Star authority; `AGENT.md` hard stops; local contracts | What may AI do, and what requires Chris? |
| Diagnose | Trust/Understand; live-file inspection; learner or system diagnosis | What is actually happening, and what evidence supports it? |
| Resolve | WORK; DECIDE/BUILD/TEACH/STRUCTURE | What is the smallest sound response? |
| Validate | PROVE; deterministic checks; semantic verification | Did it work in the target, and what remains uncertain? |
| Close | CLOSE; Return Packet; DAILY/local log | What changed, where is the evidence, and what is next? |
| Improve | LEARN/REVIEW/EVOLVE; flags and system learnings | Is this reusable evidence or merely one-time noise? |

### Physical analogy

Treat the System Loop as the full construction program and the request lens as
the foreman's work ticket:

- the program controls design, procurement, construction, inspection, turnover,
  and lessons learned;
- the work ticket makes sure one incoming problem is received, assigned,
  authorized, diagnosed, completed, inspected, and closed.

The ticket does not replace the project schedule or building code.

## Options Considered

### Option A — Install the request lifecycle as new governance

| Dimension | Assessment |
|---|---|
| Complexity | High |
| Maintenance | High |
| Discoverability | Initially clear, then likely confusing |
| Fit with current contracts | Poor |
| Reversibility | Medium |

Advantages:

- memorable vocabulary;
- explicit authorization and validation steps;
- potentially consistent request handling.

Disadvantages:

- competes with the canonical System Loop;
- creates a fifth translated view after `.ROOT` recently reconciled four;
- requires updates across the information-flow translation table and consumers;
- increases instruction load and drift risk;
- solves no demonstrated routing or proof failure yet.

Verdict: **reject**.

### Option B — Use it as an optional request-handling lens

| Dimension | Assessment |
|---|---|
| Complexity | Low |
| Maintenance | Low |
| Discoverability | High if displayed once |
| Fit with current contracts | Strong |
| Reversibility | High |

Advantages:

- gives Chris a compact visual model;
- makes authorization and validation visible;
- translates cleanly to existing owners and vocabulary;
- can be tested without modifying governance;
- resembles a real operational service-ticket flow and may become a useful
  business-analysis teaching example.

Disadvantages:

- can still become duplicate doctrine if copied into many files;
- adds little value if used as paperwork on routine learning reps;
- needs a bounded real-use test before becoming a recurring interface.

Verdict: **recommended**.

### Option C — Make no use of the pattern

| Dimension | Assessment |
|---|---|
| Complexity | None |
| Maintenance | None |
| Discoverability | Unchanged |
| Fit with current contracts | Strong |
| Opportunity cost | Moderate |

Advantages:

- zero additional vocabulary;
- no chance of architectural duplication.

Disadvantages:

- leaves a useful simple mental model unused;
- authorization and validation remain distributed across several contracts;
- misses an accessible way to teach workflow analysis and test a business
  method on `.ROOT`.

Verdict: **safe but unnecessarily conservative**.

## Recommended Design

Keep the System Loop authoritative. Pilot the request lens as a **non-governing
work-ticket view**:

```text
Request or signal
      |
      v
[Capture] What arrived and what outcome is wanted?
      |
      v
[Route] Who owns truth, action, proof, and return?
      |
      v
[Authorize] Is the action permitted and properly bounded?
      |
      v
[Diagnose] What is actually happening?
      |
      v
[Resolve] What is the smallest sound response?
      |
      v
[Validate] Did it work in the real target?
      |
      v
[Close] What changed, what is next, and where is the evidence?
      |
      v
[Improve] Reusable lesson, flag, asset—or no promotion?
      |
      +---------------------------> next request
```

### Instruction-set candidate

For evaluation only:

> For each meaningful request, capture the intended outcome; route truth,
> action, proof, and return to their existing owners; check the applicable
> authority boundary; diagnose from live evidence; execute the smallest sound
> response; validate it in the target; close with the canonical Return Packet;
> and promote only reusable or repeated learning. This is a request-handling
> lens over the canonical System Loop, not a competing lifecycle.

This instruction should not be installed unless a real pilot shows that it
improves completeness or reduces recovery time without increasing friction.

## Pilot

Run the lens manually on three different request classes:

1. a learning request;
2. a safe file-maintenance request;
3. a technology or business analysis request.

For each, record only:

- missed or recovered step;
- time or confusion added;
- error or rework prevented;
- whether a fresh session can find the owner, evidence, and next action.

### Acceptance

Keep the lens only if, across the three pilots:

- it catches at least one real omission or materially improves handoff clarity;
- it adds no duplicate owner or state;
- it requires no new metadata;
- it does not displace the primary learning or value proof;
- Chris finds the diagram easier to use than the underlying contract language.

### Stop conditions

Stop or simplify if:

- routine tasks become longer because every label must be narrated;
- agents treat it as a second lifecycle;
- the same state must be updated in two places;
- it generates reports without changing outcomes;
- it conflicts with the System Loop or Return Packet.

## Business and Technology Value

This is valuable beyond `.ROOT` if treated as a small workflow-analysis proof:

- **Client problem:** requests enter through inconsistent channels, ownership is
  unclear, approvals are skipped, and work closes without usable data.
- **Measurable outcome:** routing time, waiting time, rework, unauthorized
  actions, reopen rate, and knowledge reuse.
- **Deliverable:** current-state request map, failure analysis, improved
  work-ticket design, and decision-ready report.
- **Technology path:** model work tickets in Python, validate required fields,
  store state transitions in SQLite, and report bottlenecks.
- **Reusable asset:** a sanitized request-lifecycle assessment method.
- **Revenue mechanism:** a bounded workflow diagnosis first; implementation
  only when evidence shows that process, software, or integration work is
  justified.

This matches the Advisor-Builder method without claiming market proof.

## Architecture Decision

**Status:** Proposed  
**Date:** 2026-07-28  
**Decider:** Chris

Adopt Option B for a manual three-case pilot. Do not modify governance,
metadata, folder structure, CASTLE, or the canonical contracts during the
pilot.

## Exact Next Action

At a time Chris activates system work after the primary learner/value proof,
run the first pilot on one normal `.ROOT` maintenance request and record only
the four acceptance observations. Do not install the instruction set yet.

## Return Packet

1. **Outcome:** The GitLab-style lifecycle is useful as an optional
   request-handling lens, not as new `.ROOT` architecture.
2. **Evidence link:** this report.
3. **Capability/status movement:** architecture candidate moved from idea to
   proposed bounded pilot; no live system status or governance changed.
4. **Reusable-asset candidate:** yes—a work-ticket assessment pattern, after
   successful pilots; possible home:
   `05-BUSINESS/06-Capability Library`.
5. **System-learning candidate:** not yet. Promote only if pilot evidence shows
   repeated value or friction.
