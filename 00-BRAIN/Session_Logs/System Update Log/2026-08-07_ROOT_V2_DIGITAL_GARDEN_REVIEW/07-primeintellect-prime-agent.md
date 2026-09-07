---
type: architecture-decision
timeline: log
status: proposed
tags: [architecture, agent-runtime, continual-learning, root-v2, security]
created: 2026-08-07
---

# Review 07 — Prime Intellect Prime Agent

## Verdict

**Extract its architecture patterns; do not install it into the live `.ROOT`
environment now.** Prime Agent is the strongest agent-operated comparison in
this packet and validates several V2 runtime ideas. It is not currently a safe
or necessary replacement for Codex, Claude, or `.ROOT` governance.

## Sources

- Inbox capture: `77-INBOX/PrimeIntellect-aiprime-agent A self-improving RLM
  agent for coding workflows and long-running autonomous tasks.md`
- Repository: [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)
- [Architecture overview](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/architecture.md)
- [RLM programming model](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/rlm.md)
- [Long-running agents](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/long-running-agents.md)
- [Skills](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/skills.md)
- Accessed: 2026-08-07

## Why it matters to `.ROOT V2`

Claude's challenge found that the original six-case sample lacked an explicit
“agent-operated versus human-only” axis. Prime Agent fills that gap. It is not
primarily a digital garden; it is an agent runtime designed to preserve useful
state, coordinate recursive workers, refine its harness, and continue bounded
work across terminal sessions.

## Reusable mechanisms

### 1. Context as program state

The parent model keeps its immediate context small while a persistent Python
environment holds variables, parsed results, functions, and child handles.
This supports the V2 context-compiler thesis: context should be selected and
operated on as data, not accumulated indiscriminately in one prompt.

### 2. Durable but separated state

Transcripts and artifacts are appended to session storage. The TypeScript host
retains authority over provider calls, credentials, scheduling, routing, and
state transitions while the model uses a Python control surface. This is a
useful ownership boundary: model-facing tools should request authoritative
operations rather than directly owning every state transition.

### 3. Evidence-bounded self-refinement

The continual harness may add small supplemental prompts, memories, skill
descriptions, and reusable subagent specifications. The base system prompt is
immutable and refinement snapshots support review and rollback. `.ROOT V2`
should borrow this narrow pattern:

`observed failure or repeated success -> proposed lesson -> evidence -> human
review -> versioned supplemental rule -> evaluation -> retain or roll back`

Self-improvement must not mean autonomous rewriting of governance, canonical
knowledge, or the North Star.

### 4. Goals are not completion

Persistent goals, autonomous continuation, compaction, and quality gates are
separate mechanisms. Hitting a time/token limit is not success, compaction is
not completion, and a passed gate proves only what that gate tests. These are
strong operating invariants for `.ROOT V2`.

### 5. Skills use progressive disclosure

Only skill metadata is loaded at startup; full instructions load when the task
matches. Executable skills are packaged and reviewed separately from informal
harness memories. This supports shrinking `.ROOT`'s universal boot burden and
keeping reusable automation distinct from remembered advice.

## Risks and incompatibilities

1. **No security sandbox.** Model-generated Python and project commands run
   with the worker's operating-system permissions. Process isolation is for
   lifecycle recovery, not security containment.
2. **Current `.ROOT` blocker.** Claude's sandbox is already missing eight
   explicit wiki `raw/` write-deny paths. Adding another full-permission agent
   before closing that blocker increases the exact risk governance is intended
   to prevent.
3. **Platform mismatch.** The documented stable installer targets macOS and
   Linux; `.ROOT` currently lives on Windows. WSL or a virtual machine would add
   path, permission, synchronization, and recovery complexity.
4. **Instruction drift.** A self-refining supplemental harness can preserve a
   mistaken lesson, malicious instruction, or local workaround unless every
   refinement has provenance, bounded scope, tests, approval, and rollback.
5. **Capability duplication.** Current Codex/Claude workflows already provide
   skills, goals, compaction, subagents, task continuity, and governance. A new
   runtime would create another control plane before its incremental value is
   proven.
6. **Economic neutrality.** Long-running autonomy can increase throughput, but
   it does not choose a valuable SMB problem, verify adoption, measure outcome,
   or create revenue by itself.

## Options considered

| Option | Complexity | Safety | Learning value | Decision |
|---|---:|---:|---:|---|
| Replace the current agent surfaces with Prime Agent | High | Low | Medium | Reject |
| Install it directly against live `.ROOT` | Medium | Low | High | Reject now |
| Run an isolated comparison on a disposable repository | Medium | Medium-High | High | Later, approval-gated |
| Extract patterns into the V2 design without installation | Low | High | High | Recommend |

## Architecture deltas added by this case

1. Add **agent-operated design** as a comparison axis for future systems.
2. Separate immutable constitutional instructions, approved supplemental rules,
   episodic session memory, executable skills, and generated working state.
3. Require a refinement ledger containing trigger, evidence, proposed change,
   approver, tests, result, version, and rollback pointer.
4. Make every autonomous loop declare budgets, stop conditions, quality gates,
   and a human-escalation condition.
5. Run agent code behind a permission boundary; process separation alone is not
   a sandbox.

## Smallest safe evaluation

Do not point Prime Agent at `.ROOT`. If Chris later approves a product trial,
use a disposable Linux/WSL repository containing non-sensitive copied fixtures
and one bounded long-running coding task. Compare it with the existing Codex
workflow on completion correctness, human interventions, token/cost usage,
recovery after interruption, and unsafe or unauthorized actions. No result from
that trial should write back to `.ROOT` automatically.

## Consequence for the current V2 decision

This case strengthens—rather than replaces—the current recommendation:
canonical `.ROOT` knowledge plus a bounded, read-only compiled runtime. It adds
a controlled refinement layer and sharper runtime boundaries. It does not
justify a new live vault or a new agent platform today.
