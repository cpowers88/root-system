---
type: research
tags: [ai-automation, agent-architecture, self-evolution, landscape]
source: raw/GBrain - Garry Tan's Opinionated Agent Brain.md (garrytan/gbrain README, captured 2026-07-13); raw/loopany CLAUDE.md.md + raw/loopany INSTALL_FOR_AGENTS.md.md + raw/loopany part 1.md (README) + raw/loopany part 3.md (ONBOARDING.md) + raw/loopany part 4.md (loopany-resolver/SKILL.md), all superdesigndev/loopany, captured 2026-07-13; raw/How to build proactive agents and self-improving companies.md (AI Jason / YouTube transcript, captured 2026-07-13); plus one live fetch beyond the clippings, 2026-07-13: github.com/superdesigndev/loopany/blob/main/skills/loopany-reflect/SKILL.md (not in raw/ — the resolver in raw/ points to it but its content wasn't captured; fetched via `gh api` to verify the self-evolution mechanics this page and the linked proposal depend on)
---

# Self-Improving Agent Architectures: GBrain, loopany, and the Closed-Loop Pattern

**Sources, each read in full 2026-07-13** (see frontmatter). This page is the
full architectural ingest behind the shorter comparison already logged in
[[llm-wiki-pattern-and-second-brain-tools]] — that page stays the
pattern-history/verdict hub; this page holds the depth.

## The Framing: Open-Loop vs. Closed-Loop Agent Operations

The AI Jason video (a walkthrough of what YC's current batch is calling
"self-improving companies," reporting some portfolio companies at 5x revenue
per employee vs. 18 months prior) gives the framing both tools below
implement:

- **Open-loop (pre-agent and most current "AI-enhanced workflow"):** a human
  is the glue — decides what to do, triggers the task, reads the output.
  No feedback returns to the system.
- **Closed-loop:** an agent takes a goal-directed trigger, does the task,
  and — critically — **captures the outcome as feedback that changes what it
  does next time.**

Five components recur across working closed loops (video's framing,
generalized): a **data-ingestion layer**, a **policy/SOP layer** (the
contract for how the workflow should run), a **system-access layer** (tools
the agent can act through), **quality gates** (human or AI evaluation of
output before it counts as done), and a **feedback mechanism** that routes
learnings back into the policy layer. Two kinds of memory feed the loop:
**factual** (a log of what happened — the "did I do this already" record)
and **procedural** (the learnings that get promoted into a skill — the
"how do I do this better" record). Cited case studies: an Airbnb co-founder's
SEO agent loop reportedly tripled organic traffic in 1–2 months by running
research → content → monitor → re-strategize on a cron cycle; a separate ads
experiment went from testing 10 ad formats in week one to a converged
"ugly-asset" strategy generating 243 leads on a $1,500 budget in week two,
purely from the loop's own outcome log.

GBrain and loopany are both, in this framing, **memory-layer substrates**
for running that loop — they don't run the business logic, they give an
agent a place to record and query the state a closed loop needs to keep
turning.

## GBrain — Entity-Centric Agent Brain (Garry Tan / YC)

**What it answers:** *"what do I know."* An opinionated, database-backed
knowledge brain: 146,646 pages / 24,585 people / 5,339 companies in the
author's own production deployment, PGLite (zero-config, Postgres-via-WASM)
for personal scale up to ~50K pages, or Postgres+pgvector (Supabase or
self-hosted) for shared/large deployments. **Brain repo is the system of
record** — knowledge lives as markdown in a git repo; GBrain syncs it into
Postgres for retrieval, so deletes in git become soft-deletes in the DB, not
data loss.

**Architecture, the pieces worth knowing:**

- **Hybrid search + synthesis split.** `gbrain search` returns raw ranked
  pages (vector HNSW + BM25 + reciprocal-rank fusion + source-tier boost);
  `gbrain think` runs the same retrieval then composes a cited, synthesized
  answer *and* an explicit "what the brain doesn't know yet" gap-analysis
  note — the differentiator over plain RAG. Three named cost/quality
  presets (`conservative`/`balanced`/`tokenmax`).
- **Self-wiring knowledge graph, zero LLM calls.** Every page write extracts
  entity refs from markdown/wikilink syntax and writes typed edges
  (`attended`, `works_at`, `invested_in`, `founded`, `advises`) via pure
  pattern matching. Benchmarked (their own BrainBench numbers, treat as
  vendor-reported): **+31.4 points P@5** over a graph-disabled variant and
  over vector-only RAG — the graph is what turns "who mentions Acme" into
  "who works at Acme" as an answerable query.
- **Agent-authored schema packs.** No fixed page-type layout. Ships
  `gbrain-base-v2` (15-type canonical taxonomy: person/company/deal/
  email/etc.) by default, but an agent can run `gbrain schema detect` →
  `suggest` → `review-candidates --apply` to fit the brain's shape to
  whatever data actually exists — a human-gated three-command loop, not an
  autonomous rewrite of the taxonomy.
- **Minions job queue.** BullMQ-shaped, Postgres-native. Durable sub-agent
  tool loops that survive process crashes via two-phase pending→done
  persistence — the explicit contrast is "spawn subagent as fire-and-forget
  Promise," which recovers from nothing.
- **Eval framework.** `gbrain eval longmemeval` runs the public LongMemEval
  benchmark against the brain's own retrieval; `gbrain eval
  retrieval-quality` runs NamedThingBench, which hard-gates named-entity
  retrieval so a regression fails CI loudly rather than silently degrading
  answer quality over time. Worth citing as a concrete instance of
  "verify-before-scaling" applied to a memory system specifically — same
  principle [[openai-evals-and-red-teaming]] documents for agent
  architectures generally.
- **The dream cycle.** Cron-driven overnight job: dedupes person pages,
  fixes citations, scores salience, finds contradictions between pages,
  preps next-day tasks — all without a human in the loop until morning.
  **This is the piece already evaluated and rejected for `.ROOT` on
  2026-07-09** (same feature class as obsidian-second-brain's "nightly
  reconcile/synthesize/heal loop" — see
  [[llm-wiki-pattern-and-second-brain-tools]] and
  [[root-maturity-self-assessment]]). Not re-opened here; recorded for
  completeness since it's GBrain's own headline feature.

**Not evaluated for adoption, noted as landscape-only:** the multi-user/
team-scoped "company brain" mode, the 16-provider embedding matrix, the
voice/Twilio ingestion recipe, and the credential-gateway integration —
none map onto a single-user, git+markdown vault at `.ROOT`'s current scale.

## loopany — Action-and-Outcome Ledger (superdesigndev, ex-crewlet.io)

**What it answers:** *"what did I do, did it work, what should I change
next."* Not a knowledge wiki — a persistent record of the agent's own
actions and their outcomes, built specifically so a long-running or
resumed agent can reason over its own history instead of starting blind
each session. Markdown + frontmatter as the source of truth, append-only
JSONL (`references.jsonl`) for the relationship graph, no database — an
optional local SQLite index is a derived, disposable cache.

**The artifact model (three concepts, deliberately kept to three):**

1. **Artifact** — a markdown file with frontmatter; `kind` is an open
   registry (`signal`, `task`, `learning`, `skill-proposal`, `person`, and
   any kind a user or agent registers later). Everything the agent produces
   is an artifact.
2. **References** — append-only graph edges (`caused-by`, `led-to`,
   `follows-up`, `mentions`) — hard links captured automatically at tool
   boundaries, soft links declared in frontmatter or inline wiki-links.
3. **Domain** — a scope the agent notices in real usage (a sales pipeline,
   a research thread) and *proposes*, never pre-ships; the user accepts.
   Domain-local kinds (e.g. `contact`, `deal`) stay out of the global
   artifact namespace so a research-scope agent never has to reason about
   CRM fields.

**Core kinds, the primitives every agent gets regardless of domain:**
`mission` (intent — what's this for), `signal` (input), `brief` (output),
`task` (work, must write `## Outcome` on `status: done`), `learning`
(belief), `skill-proposal` (change), `person` (entity), `note` (fallback —
the deliberate default when nothing else fits).

**The "should this be a kind" test** (documented already in the 2026-07-13
update to [[llm-wiki-pattern-and-second-brain-tools]], repeated here since
it belongs with the full model): a candidate must pass a 4-question test
(state machine? identity/dedup? structured queries? required body shape?)
before it's a kind at all, then a further 3-question test (every agent
wants it? distinct lifecycle stage? about HOW not WHAT?) before it's a
*core* kind rather than a domain-local one. Default fallback is always
`note`.

## The Self-Evolution Loop — Confirmed Mechanics

This is the one piece genuinely novel relative to everything `.ROOT`
already evaluated on 2026-07-09, and the basis for
[[proposals/2026-07-13_belief-proposal-split-for-system-flags]]. The
raw clippings captured the *what* (CLAUDE.md's "Self-Evolution Loop"
section); the actual `skills/loopany-reflect/SKILL.md` — referenced by the
resolver in raw/ but not itself captured — was fetched live from GitHub to
confirm the *how* before this page or the proposal leaned on it further.

**Trigger:** user says "reflect" / "what have we learned", weekly cadence,
or after ≥3 tasks flip to `done` in a short window. Explicitly **not** run
reactively after every single task — the skill's own anti-pattern list
calls out "reflecting on a single task" as a failure mode.

**Step 1 — gather evidence.** Pull `done` tasks, all signals (including
dismissed ones), active learnings, and rejected proposals; filter out
evidence already cited by an existing active learning or non-rejected
proposal, so the same pattern doesn't get re-discovered every week.

**Step 2 — pattern thresholds** (this is the part not visible from the
CLAUDE.md summary alone): same class of outcome needs **≥3 tasks**; a
belief being refuted needs **≥2 tasks contradicting an existing learning**;
a signal repeatedly dismissed needs **≥3 dismissals over ≥2 weeks**. Below
threshold, it's not a pattern — explicitly, "1 bad outcome → not a
pattern."

**Step 3 — write a `learning`** — a declarative belief sentence as the
title, ≥2 evidence IDs, a `check_at` date 1–3 months out for "is this still
true?" revalidation.

**Step 4 — write a `skill-proposal` (only if warranted)** — many learnings
stop at "now I know" with no matching behavior change. When one is written,
required sections are `## Motivation` (cites the learning), `## Proposed
change` (target file + intent + location), `## Expected effect`, and
`## Check-at`.

**Step 5 — verify the evidence chain** — `loopany trace <proposal-slug>
--direction backward` before finalizing, so the proposal is provably
downstream of real evidence, not asserted.

**Accept/reject, the human gate:** on accept, the agent reads the proposal
and its cited learning, reads the current target file, applies *only* the
described edit, appends an `## Outcome` section to the proposal recording
what literally changed, flips status, and **commits the target file and
the proposal artifact together in one git commit** — the diff and the
rationale land atomically. On reject, the proposal gets an `## Outcome`
section recording the reason, and the skill's own rule is explicit: future
reflect passes check the rejected-proposal list first, so a declined idea
doesn't get re-proposed cold. **The agent never edits a skill file
directly — skill-proposal is the only path**, enforced as a stated
architectural constraint, not just a norm.

This is a more structured, threshold-gated version of what `.ROOT`'s own
`SYSTEM_FLAGS.md` does informally (flag re-raised after closing comes back
as HIGH priority) — see the proposal for the specific adaptation.

## Design Principles Worth Naming Even Without a Proposal

- **"Thin harness, fat skills"** (loopany's explicit framing of Garry Tan's
  own formulation) — the CLI/core is deliberately small (~2000 lines: file
  I/O, validation, graph indexing); all judgment, prompts, and process
  knowledge live in markdown skill files the agent reads on demand. This is
  the same shape `.ROOT` already runs (`AGENT.md` + skill files), arrived
  at independently by a third implementation — reinforces the finding
  already recorded in [[llm-wiki-pattern-and-second-brain-tools]] that
  three separate builders converged on the same raw/wiki/schema/index shape.
- **"Latent vs. deterministic"** — judgment/synthesis/pattern-matching
  belongs to the LLM; SQL-like queries, validation, and atomic writes
  belong to code; "forcing one into the other is the most common
  architecture mistake." A clean, reusable framing for judgment calls about
  what belongs in a skill file (latent) vs. a script (deterministic) —
  applicable to future `.ROOT` extension-type decisions via the existing
  Extension Trigger Table, not a new rule on its own.
- **Immutable-for-cited, mutable-for-current-understanding** — agent-
  produced artifacts (task, signal, learning, skill-proposal) are never
  edited in place, only appended/superseded; config and skill files are
  mutable + git-tracked, and skill files change *only* through an accepted
  skill-proposal. This is loopany's version of `.ROOT`'s own raw/-immutable
  vs. wiki/-mutable split, independently arrived at.
- **Onboarding "do more, ask less."** loopany's onboarding script explicitly
  bans multi-question interviews in favor of reading available context
  first, proposing a concrete setup, and only asking clarifying questions
  when genuinely stuck — "a user can always say 'no, change X' — they
  cannot un-answer a needless question." Relevant to any future `.ROOT`
  session-boot or new-hub-setup skill design, flagged for awareness, not a
  proposal — no current friction this would resolve.

## Comparison Table

| | GBrain | loopany |
|---|---|---|
| Answers | "what do I know" | "what did I do, did it work, what next" |
| Unit of memory | entity (person/company/deal) | artifact (action-and-outcome) |
| Storage | Postgres/pgvector (or PGLite) | markdown + append-only JSONL, no DB |
| Self-evolution mechanism | autonomous overnight "dream cycle" | human-gated `reflect` → learning + skill-proposal → accept/reject |
| Eyes-not-hands compliant? | **No** — dream cycle rewrites unattended | **Yes** — proposal-gated, evidence-chain verified |
| `.ROOT` verdict | Dream cycle rejected (2026-07-09, reaffirmed here); rest is landscape-only | Belief/proposal split proposed as an optional `SYSTEM_FLAGS.md` addition — pending review |

## Why This Matters for This Wiki / `.ROOT`

Confirms, a third time, that three independent teams (Karpathy's own
gist-documented pattern, GBrain, loopany) keep arriving at the same
raw-source / agent-owned-memory / skill-as-judgment shape `.ROOT` already
runs — the strongest available external validation of the architecture
without being self-referential about it. The one genuinely new mechanism
(loopany's belief/proposal split with pattern thresholds and an
evidence-chain verify step) is narrow enough to try as an optional
convention rather than a structural change — see the linked proposal for
the specific, scoped adaptation. GBrain's dream cycle stays a clean,
repeated negative example of the eyes-not-hands boundary this system holds
deliberately.

Related: [[llm-wiki-pattern-and-second-brain-tools]],
[[root-maturity-self-assessment]],
[[proposals/2026-07-13_belief-proposal-split-for-system-flags]],
[[openai-evals-and-red-teaming]].
