---
type: reference
tags: [ai-automation]
source: raw/LLM_WIKI_PATTERN_karpathy.md + raw/LLM WIKI.md + raw/Obsidian AI Second Brain Open-Source.md + raw/Second brain obsidian.md (each read in full, 2026-07-09); raw/GBrain - Garry Tan's Opinionated Agent Brain.md + raw/loopany CLAUDE.md.md + raw/loopany INSTALL_FOR_AGENTS.md.md + raw/loopany part 1-4.md + raw/How to build proactive agents and self-improving companies.md (each read in full, 2026-07-13; full architectural depth moved to [[self-improving-agent-architectures-gbrain-loopany-closed-loop]]); raw/Agentic Operating System File Structure A Practical Folder Layout.md + raw/Build Karpathy’s Self-Updating AI Knowledge Base in Just 90 Minutes.md (read in full and source-classified, 2026-07-14)
timeline: reference
---

# The LLM-Wiki Pattern and Its Second-Brain Implementations

**Sources (all in `raw/`, each read in full, July 9, 2026):**
`LLM_WIKI_PATTERN_karpathy.md` (the original pattern),
`LLM WIKI.md` (Rezvani's llm-wiki agent skill),
`Obsidian AI Second Brain Open-Source.md` (Agrici's claude-obsidian),
`Second brain obsidian.md` (Ghelbur's obsidian-second-brain).

## The Pattern in One Paragraph

Instead of RAG (retrieve fragments at query time, re-derive, forget), the
LLM incrementally builds and maintains a persistent, interlinked markdown
wiki: immutable `raw/` sources → LLM-owned `wiki/` pages → a schema file
(CLAUDE.md) that makes the LLM a disciplined maintainer. Three operations:
**ingest** (read source, update 10–15 pages, index, log), **query** (index
first, drill in, cite; file good answers back), **lint** (health check for
contradictions, orphans, stale claims, gaps). Knowledge compounds instead
of being re-derived. "Obsidian is the IDE; the LLM is the programmer; the
wiki is the codebase."

## Where `.ROOT` Already Implements It

The seven `03-WIKIS` hubs are independent, domain-specific instances of
this pattern and predate this ingest: immutable `raw/`, LLM-owned `wiki/`,
per-hub CLAUDE.md schema, `index.md` + `log.md`, disciplined ingest
protocols. `.ROOT` goes beyond the pattern in governance (castle review,
proposal gate, Chris as approver) and in continuity (NOW.md + DAILY task
blocks + handoffs outperform claude-obsidian's ~500-token `hot.md` cache).

## What Was Adopted (July 9, 2026 — see proposal)

Promoted into `00-BRAIN\AGENT.md § Wiki Shared Layer` (originally added before the
July 10 lane split), rules 5–8:

- **Prefer updating over creating** (generalized from BUSINESS §7A) —
  the anti-append discipline obsidian-second-brain identifies as the thing
  "missing from the original": append-only breaks at scale.
- **Contradiction flagging** — never silently overwrite a claim; mark
  "supersedes / contradicts X (source, date)". From claude-obsidian's
  `[!contradiction]` callout practice and Karpathy's provenance emphasis.
- **Recency markers** — "(as of YYYY-MM, source)" on volatile
  landscape/market claims. From the AI-first vault rule (bi-temporal
  facts, lightweight version).
- **Lint pass** — the operation `.ROOT` lacked entirely. Checklist drawn
  from claude-obsidian's eight categories: orphan pages, dead wikilinks,
  contradictions, missing pages, unlinked mentions, incomplete metadata,
  empty sections, stale index. Cadence: monthly review or on demand.
  The July 8 LINK_INTEGRITY scans (277 → 220 broken links) were ad-hoc
  lint passes before the rule existed.

## What Was Rejected, and Why

- **Hot cache (`hot.md`)** — `.ROOT`'s NOW.md + DAILY + handoff stack
  already carries session continuity with review built in.
- **Scheduled/background agents and the self-rewriting vault**
  (obsidian-second-brain's nightly reconcile/synthesize/heal loop) —
  directly violates the eyes-not-hands division and the July 8
  verification-capacity verdict: an unreviewed agent rewriting pages
  while Chris sleeps is unverifiable output, the exact failure mode the
  maturity self-assessment warns about. Contradiction *flagging* was
  adopted; contradiction *auto-resolution* was not — Chris resolves.
- **Slash-command tooling / vault scripts** (init, BM25 search,
  graph analyzer) — index-first navigation suffices at current scale
  (Karpathy: fine to ~100 sources / hundreds of pages per hub). Noted as
  a future option, not a need.

## Why This Matters for This Wiki / `.ROOT`

This batch is the self-evolution charter working as designed: external
pattern research → compared against `.ROOT`'s live practice → deltas
promoted through a Chris-approved proposal → rejects documented so the
question doesn't get re-litigated. It also independently validates the
`.ROOT` architecture: three separate implementations (skill, plugin,
cross-CLI toolkit) converged on the same raw/wiki/schema/index/log shape
`.ROOT` already runs — evidence from the Codex-paper page
([[shift-to-agentic-ai-codex]]) that persistent procedural context is
where agent value concentrates.

## 2026-07-13 Update: Two Newer Sibling Implementations (GBrain, loopany)

**Sources (all in `raw/`, each read in full, July 13, 2026):** `GBrain -
Garry Tan's Opinionated Agent Brain.md` (Garry Tan/YC, garrytan/gbrain),
`loopany CLAUDE.md.md` + `loopany INSTALL_FOR_AGENTS.md.md` + `loopany part
1-4.md` (superdesigndev/loopany), `How to build proactive agents and
self-improving companies.md` (AI Jason video transcript), plus one live
GitHub fetch beyond the clippings (`loopany-reflect/SKILL.md`, not itself
captured in raw/). Full architectural ingest — GBrain's schema packs/hybrid
search/Minions queue/eval framework, loopany's full artifact/kind/domain
model and the confirmed reflect-loop mechanics (pattern thresholds,
evidence-chain verification, accept/reject flow), and the AI Jason video's
closed-loop-operations framing — now lives in its own page rather than
here, to keep this page focused on pattern history:
[[self-improving-agent-architectures-gbrain-loopany-closed-loop]].

**Headline verdicts, in short:** GBrain's **"dream cycle"** (cron-driven
overnight autonomous rewrite) is the same feature class already evaluated
and rejected on 2026-07-09 (obsidian-second-brain's "nightly reconcile/
synthesize/heal loop" — violates eyes-not-hands, see
[[root-maturity-self-assessment]]); not re-litigated, verdict stands.
loopany's **belief/skill-proposal split** (a `reflect` skill that separates
a generalized `learning` from the specific `skill-proposal` behavior
change, human accept/reject, rejected reasons logged, accepted ones get a
`check_at` follow-up) is genuinely novel and stays inside the eyes-not-hands
boundary — proposal comparing it against `SYSTEM_FLAGS.md`'s current
mechanism: [[proposals/2026-07-13_belief-proposal-split-for-system-flags]].

## 2026-07-14 Clipping Review: What Earned Promotion

Two clippings supplied useful operating mechanics after their vendor/promotional
claims were separated from the ideas. MindStudio's folder-layout article
reinforced thin global rules, split process from context, and versioned writable
learnings. The Karpathy implementation article supplied two useful maintenance
prompts. `.ROOT` already had the larger architecture, so no new folder layer,
agent, heartbeat, or schema was added.

The promoted deltas are deliberately small:

1. **Prioritize sources before ingest.** Rank candidates by authority,
   information density, cross-reference potential, currency, and dependency
   order; flag whether each source is actually ready to ingest. Marketing pages
   can suggest leads but cannot establish a governance or revenue claim.
2. **Classify change before overwriting.** A newer statement may be a temporal
   update, a context-dependent variant, or a true contradiction. Preserve the
   older source/history, keep legitimate variants, and flag only true conflicts.
   Cross-source synthesis waits for repeated independent evidence.

This review also corrected an overbroad reading of “wiki instead of RAG.” The
current primary research shows a tradeoff, not a universal replacement:

- [WiCER (2026)](https://arxiv.org/abs/2605.07068) reports severe information
  loss from blind compilation and materially better results after diagnostic
  evaluation/refinement. This supports `.ROOT`'s validation gate and rejects
  unattended “compile and trust.”
- [Retrieval as Reasoning (2026)](https://arxiv.org/abs/2605.25480) reports
  gains from a compiled bidirectional wiki plus tool-based traversal and an
  error book. The evaluation/error-log idea is worth studying; autonomous
  self-repair is not approved here.
- [A preregistered RAG-vs-wiki comparison (2026)](https://arxiv.org/abs/2605.18490)
  found different strengths and substantially higher query-token cost for the
  tested wiki workflow. Architecture should follow the question and evidence.

### Research queue — primary/inspectable first

1. [Karpathy's original LLM-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f3)
   — re-check the baseline pattern against later interpretations.
2. [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — inspect source
   lineage, review-queue, immutable-raw, and read-only MCP defaults before
   borrowing any mechanism.
3. WiCER's released benchmark/code — test whether a small diagnostic probe set
   catches meaningful information loss in one `.ROOT` hub before considering
   tooling.
4. Retrieval as Reasoning's error-book design — compare with `SYSTEM_FLAGS.md`
   and wiki logs; do not duplicate unless a concrete gap appears.
5. *The Living Wiki* paper — read from a stable primary copy when accessible;
   it remains a lead, not evidence, until then.

Archived search-result pages and promotional duplicates remain provenance for
these leads. They do not count as independent confirmation.

## 2026-08-07 Addendum: Four Details a Closer Re-Read Surfaced

Re-read `Obsidian AI Second Brain Open-Source.md` and `Second brain obsidian.md`
in full again this session (prompted by the parallel `bojieli/ai-agent-book`
deep dive) to check for anything the July 9/14 pass compressed past. The
hot-cache and scheduled/self-rewriting-agent verdicts above stand unchanged —
not re-litigated. Four details genuinely weren't captured in the summary
above:

- **`/obsidian-challenge`** — before a decision, the tool searches the vault's
  own history for past failures or reversed decisions on the same topic and
  pushes back using the user's own prior words as evidence ("Your own notes
  say this failed. Still want to proceed?"). `.ROOT` has this as a stated
  behavioral instruction (`CHRIS_CORE.md` "Challenge Without Taking the
  Wheel"), not a mechanism that automatically searches session/DAILY history
  before a similar decision repeats. Worth naming as a real capability gap,
  not urgent.
- **Sentinel-marker pattern** (`<!-- @generated -->` / `<!-- @user -->`
  blocks) — lets an automated regeneration pass touch only its own marked
  region of a file, never a human-edited region, in the same document. A
  concrete technique for the general "don't clobber what a human added"
  problem `AGENT.md`'s file-safety rules already care about, if that need
  ever gets specific enough to want it.
- **`CRITICAL_FACTS.md`** — a tier even smaller than `CHRIS_CORE.md`, ~120
  tokens, always loaded first. Not adopted or rejected here — just noted as
  a granularity `.ROOT`'s current two-tier `CHRIS_CORE.md`/`CHRIS.md` split
  doesn't have a rung below.
- **Dual-track research** — deliberately running the same question through
  an open-web-only pass and a vault-grounded-only pass, then treating
  *disagreement between the two* as the actual signal worth investigating,
  not a nuisance to resolve. A genuinely different technique from anything
  `...projectSuccess\` (the Watchtower) currently does.

Related: [[root-maturity-self-assessment]], [[2025-ai-agent-index]],
[[work-trend-index-2024-2026]],
[[self-improving-agent-architectures-gbrain-loopany-closed-loop]].
