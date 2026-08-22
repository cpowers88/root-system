---
type: research
timeline: reference
tags: [ai-automation, agentic-ai, adoption, workflows, skills]
source: raw/2606.26959v1.pdf
---

# The Shift to Agentic AI: Evidence from Codex

**Johnston, Holtz, Richmond, Ong, Tambe & Chatterji (OpenAI / Columbia /
Wharton / Duke), arXiv:2606.26959, June 2026.**
Large-scale usage-data study of OpenAI's Codex across three populations:
individual users, organizational users, and OpenAI's own workers (a preview
of "frictionless adoption").

## One-paragraph summary

Agentic AI is a different mode of use from conversational AI: **delegation of
work, not consultation for answers**. Adoption is rapid but uneven — inside
OpenAI, Codex has essentially replaced ChatGPT for work (99.8% of output
tokens); among external organizations it's 63.3%; among individuals 16.5%.
The frontier pattern is a person managing a *portfolio* of agents: parallel
threads, long runtimes, and codified reusable workflows ("skills"). The
authors frame this with the electrification analogy (David 1990): the big
gains come not from substituting the new tool into old workflows but from
reorganizing work around it.

## Four stylized facts

1. **Rapid but uneven shift.** 5x weekly active user growth in H1 2026;
   fastest growth *outside* the initial developer audience. Technical roles
   adopt first; non-technical roles later but then converge fast (OpenAI's
   legal/recruiting went ~20% → 75% of tokens in about a month once internal
   training and feedback loops kicked in).
2. **Delegated production, not consultation.** Users ask the agent to *do*
   work (debug, refactor, configure, draft, analyze), inverting the
   ask-vs-do balance documented for ChatGPT. Task complexity is climbing:
   share of individual users submitting at least one 8-hour-plus task rose
   ~10x (2.1% → 25.6%) in about six months. Most complex requests come as
   the *first* turn of a thread; refinements follow.
3. **Anchored in software, broadening where adoption is deepest.** Software
   tasks dominate everywhere, but far beyond code generation: understanding
   systems, configuring environments, validating changes, docs. At OpenAI,
   use extends into research, planning, communication, recruiting, sales.
4. **Intensive users systematize.** Three margins of workflow reorganization:
   - **Concurrency**: >10% of users run 3+ concurrent agents weekly; inside
     OpenAI 28.6% peak at 5+ concurrent agents; 99th-percentile employees run
     ~71 agent-hours per day.
   - **Long-running work**: median OpenAI employee has agents active 2.5
     hrs/day — meaningful blocks, not around-the-clock autonomy.
   - **Skills**: reusable instruction packages. 96.2% of OpenAI Codex users
     invoke skills weekly vs ~26-30% externally; growth concentrated in
     *custom* skills encoding org-specific procedural context. Skill use
     overall rose 5.4% → 26.6% of users in about three months.

## The load-bearing concepts

- **Measurement shift**: active users/chats become uninformative for agentic
  tools; the meaningful metrics are delegated task complexity, runtime,
  concurrency, workflow reuse, and output.
- **Systematization**: the step from ad-hoc prompting to codified, shareable
  workflow infrastructure is what makes delegation scale — custom skills are
  most valuable in high-context organizational environments.
- **Role shift**: intensive users move from executing tasks to delegating,
  supervising, reviewing, and integrating streams of agent work.

## Why this matters for this wiki / `.ROOT`

- `.ROOT` is, structurally, a **custom-skills system**: CLAUDE.md routers,
  hats, session protocols, and operating files are exactly the "persistent
  procedural context attached to repeated tasks" the paper finds is the
  strongest lever in high-context environments. The paper is empirical
  validation that this pattern is where frontier value concentrates.
- The near-universal internal skill usage at OpenAI vs ~27% externally
  suggests the gap is organizational practice (training, feedback loops,
  shared skills), not tool capability — relevant to how Chris ramps his own
  usage patterns.
- Watch-item: concurrency/parallel-agent workflows are the frontier pattern
  `.ROOT` doesn't yet exploit (sessions are serial today). A future proposal
  could explore where parallel sessions would help vs. add drift risk.

Related: [[agentic-ai-industry-adoption-barriers]] (why orgs can't deploy what
they can build — verification), [[2025-ai-agent-index]] (the product ecosystem
this usage runs on).
