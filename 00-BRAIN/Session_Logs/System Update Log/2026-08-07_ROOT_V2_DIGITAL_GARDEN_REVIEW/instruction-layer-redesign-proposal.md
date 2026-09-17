---
type: proposal
timeline: log
status: draft
tags: [architecture, governance, instruction-layer, root-v2, claude]
created: 2026-08-07
---

# `.ROOT` Instruction-Layer Redesign — Draft Proposal

## Status

**Draft only. Nothing in `.ROOT` changes because of this file.** Written at
Chris's request ("go look up the best wiki instruction .md files... have it
look at .ROOT and build itself from that"), scoped down to research + draft
after a scope check: the existing `.ROOT V2` packet's own plan says write an
ADR and get explicit approval before any live change, and two of the five
interview decisions in `comparison-and-root-v2-deltas.md` are still soft.
This file is the ADR-equivalent artifact for the instruction layer
specifically. Route through CASTLE review and Chris's explicit authorization
per `01-NORTH_STAR\NORTH_STAR.md` §5 before implementing anything below.

## What this covers

Not the wikis, not the maturity lifecycle (that's `comparison-and-root-v2-deltas.md`'s
job) — specifically the files that govern *how Codex, Claude, and Claude Code
operate the shared space*: root `AGENTS.md`/`CLAUDE.md`, `00-BRAIN\AGENT.md`
(universal contract), `00-BRAIN\CLAUDE.md`/`CODEX.md` (surface profiles), and
the per-hub `AGENTS.md`/`CLAUDE.md` pairs under `03-WIKIS\*`.

## External evidence

**The AGENTS.md open format** (agents.md spec, adopted across multiple coding
agents): a standardized "place an agent looks first," meant to complement a
human-facing README rather than replace it. Typical content is project
overview, build/test commands, code style, testing, security notes — but the
spec's own language allows a broader scope too ("details you'd tell a new
teammate"). Length is explicitly unspecified, "living documentation."
**Nested per-directory AGENTS.md is the official pattern, not an
improvisation** — "closest file to the edited path wins." OpenAI's own repo
reportedly ships 88 of them.

**MaggieAppleton/maggieappleton.com-V3** — root `AGENTS.md` (~50 lines) is
pure spec-standard: stack, build commands, content layout. Behavior rules live
separately in `.cursor/rules/*.mdc` — small, single-topic files loaded
on-demand via a `fetch_rules` tool, not all at once. Also ships `.claude/skills/`
(dozens of scoped skill files) and a cron-triggered autonomous maintenance
agent (`agentics-maintenance.yml`).

**aporb/second-brain-starter-template** — `AGENTS.md` is explicitly
"Agent-Agnostic Instructions" for "Claude Code, OpenAI Codex, OpenCode,
Cursor, GitHub Copilot, or any other agentic harness," and immediately
delegates: *"All operating rules live in `/schema/agent-protocol.md`. That
file is the single source of truth."* Defines a four-zone access table:

| Zone | Path | Owner | Agent Access |
|---|---|---|---|
| Sources | `/sources/` | Human | Read only |
| Wiki | `/wiki/` | Agent | Read + write |
| Journal | `/journal/` | Human | Read only |
| Schema | `/schema/` | Human | Read only |

Plus named workflows with frontmatter status transitions, e.g. "Ingest a
Source": read → mark `status: reading` → synthesize into `/wiki/` with
`[[citations]]` → mark `status: processed`.

**AEVYRA/llm-wiki-coordination** — a reusable protocol for multi-LLM vault
governance: `discussion -> structured entries -> peer review -> crystallized
knowledge -> audit`. Agents peer-review the *prior* contribution instead of
self-scoring; a separate audit step checks link/frontmatter/consensus-block
integrity before something becomes canon.

**frankxai/second-brain-os** — `AGENTS.md` documents named autonomous agents
with declared I/O contracts: e.g. `people-map` triggers on a slash command or
weekly schedule, reads `brain/_inbox/**` and `brain/notes/**`, writes one file
per person to `brain/people/{slug}.md`. Agents as named, contracted units with
explicit reads/writes, not prose instructions.

## What `.ROOT` already does right (validated, not new)

- **Per-hub `AGENTS.md` nesting matches the spec exactly** — `03-WIKIS\PYTHON\AGENTS.md`
  pointing to a local `CLAUDE.md` is the same "closest file wins" pattern the
  open standard itself recommends. Nothing to change here structurally.
- **The existing wiki intake flow** (`raw material -> relevance filter ->
  extraction -> classification -> wiki update -> index/log update -> gaps ->
  next action`, `00-BRAIN\AGENT.md` § Wiki Shared Layer) is the same shape as
  aporb's "Ingest a Source" workflow — .ROOT already has the workflow, just
  not the machine-checkable status markers (see Delta 5).
- **The "independent challenger by default" rule** (`AGENT.md` § One AI Team,
  § Task Completion) is the same instinct as AEVYRA's peer-review-before-canon
  step — this session's own challenge-packet/response pair is a live instance
  of it working.

## Concrete debt found in `.ROOT` today

**Root `AGENTS.md` contradicts itself.** It opens by declaring itself a thin
pointer — *"On July 10, 2026 this slot held the post-split review prompt; it
was executed and archived... Do not add rules to this file"* — then carries
roughly 150 more lines of real operating rules (Mission, Authority Order,
Operating Priorities, Change Control, Response Standard) that duplicate or
predate what now lives properly in `00-BRAIN\AGENT.md`. The parallel root
`CLAUDE.md` file *is* a genuine thin pointer, three lines of substance. This
is exactly the failure mode the AGENTS.md spec's nesting convention is meant
to prevent — a root file should be the smallest orienting pointer, not a
second copy of the universal contract.

## Proposed deltas

1. **Make root `AGENTS.md` match root `CLAUDE.md`'s shape.** Audit the ~150
   lines of Mission/Authority/Change-Control/Response-Standard content:
   confirm each point is already covered in `00-BRAIN\AGENT.md` or the
   `CODEX.md` profile; archive what's superseded, port what isn't, then cut
   the root file down to the same three-line pointer pattern already proven
   at root `CLAUDE.md`. This is the single highest-value, lowest-risk
   correction here — it's cleanup of dead weight, not a new design.

2. **Add a compact zone/access table to `AGENT.md` § File Safety**, modeled on
   aporb's four-zone table. Not a new rule — every fact in it already exists
   in prose (raw is immutable, `88-JOURNAL` is human-only, wiki is agent
   read+write, governance files need approval) — just made scannable in one
   place instead of scattered across ten numbered points.

3. **Decompose `AGENT.md`'s low-frequency sections into on-demand files.**
   Sections like § Communication Development and § Advisory High-Load Window
   are read every session (`AGENT.md` is mandatory first-load) but rarely
   apply. Following Maggie Appleton's many-small-files-loaded-on-demand
   pattern, move these into the existing `00-BRAIN\SKILLS\` mechanism and
   leave a one-line reference. This directly serves candidate gate 3 from
   `comparison-and-root-v2-deltas.md` (reduce irrelevant boot material ≥50%
   without missing a controlling instruction) — it's the same gate, applied
   to the instruction layer instead of the wikis.

4. **Add a lightweight automation-contract registry.** `.ROOT` already runs
   several recurring automations (evening-reading, session-close checks,
   `root_health.py`, `frontmatter_audit.py`, `sync_shared_skills.py`) each
   documented separately, in prose, in different files. Following frankxai's
   named-agent-contract pattern, one short table — trigger, reads, writes,
   owner file — would make the growing automation set auditable at a glance.
   Low cost, additive only.

5. **Give the raw-to-wiki intake flow visible status markers.** Adopt
   aporb's `status: reading` / `status: processed` frontmatter pattern for
   material moving from inbox through `raw\` into a wiki. This is also the
   direct fix for something you raised this session: raw items are moved
   there "after inbox review," but that review currently leaves no mark
   anywhere. A status field makes the vetting step visible without touching
   raw's immutability.

## What not to take

- **Maggie Appleton's fully autonomous scheduled maintenance agent** —
  interesting precedent that such things exist safely in the wild, but
  `.ROOT`'s `AGENT.md` § Agent Evaluation Gate already requires supervised use
  before autonomous, unsupervised, recurring runs; adopting this before that
  gate is satisfied would be a governance violation, not a feature.
- **AEVYRA's full protocol** (structured thread directories, per-contribution
  transcript files, formal consensus blocks) — heavier than `.ROOT` needs.
  The DAILY/handoff ritual already does the job at a fraction of the
  overhead; only the *audit-before-canon* instinct is worth keeping (Delta 5
  is the lightweight version of it).
- **junghan0611/agent-config**'s portable cross-harness identity layer — real
  pattern, but the repo's content is Korean-language and not directly
  excerptable; worth a second look only if `.ROOT` ever needs to survive a
  harness migration, which is not the current problem.

## Explicit non-application note

This file proposes; it does not implement. Per `NORTH_STAR.md` §5's change
path (signal → evidence home → CASTLE review → Chris's explicit authorization
→ live direction updates), the next step is a CASTLE review of Deltas 1–5,
not a direct edit to any governance file. Delta 1 (root `AGENTS.md` cleanup)
is the smallest, most self-contained item here and a reasonable candidate for
a first approved pass if Chris wants to greenlight anything from this
proposal individually rather than all at once.

## Sources

- https://agents.md
- https://github.com/MaggieAppleton/maggieappleton.com-V3
- https://github.com/aporb/second-brain-starter-template
- https://github.com/AEVYRA/llm-wiki-coordination
- https://github.com/frankxai/second-brain-os
- `AGENTS.md` (`.ROOT` root)
- `CLAUDE.md` (`.ROOT` root)
- `00-BRAIN\AGENT.md`
- `03-WIKIS\PYTHON\AGENTS.md`, `03-WIKIS\PYTHON\CLAUDE.md`
- `01-NORTH_STAR\NORTH_STAR.md`
- `00-BRAIN\Session_Logs\System Update Log\2026-08-07_ROOT_V2_DIGITAL_GARDEN_REVIEW\comparison-and-root-v2-deltas.md`
