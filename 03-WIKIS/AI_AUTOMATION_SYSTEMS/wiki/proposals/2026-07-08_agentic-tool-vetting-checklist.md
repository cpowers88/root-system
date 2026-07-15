---
type: proposal
tags: [ai-automation, proposal, approved, reference]
status: APPROVED & APPLIED 2026-07-08
---

# Proposal: Agentic-Tool Vetting Checklist for the Possibility Map

**Drafted:** July 8, 2026, by the AI_AUTOMATION_SYSTEMS wiki.
**Status: APPROVED & APPLIED July 8, 2026.** Chris approved with one
revision — he rewrote the draft blockquote below into the single compressed
bullet that follows it ("Agent-tool vetting screen"). That final text was
promoted verbatim into `TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10 the same
day. This wiki's first proposal to complete the full loop:
research → proposal → Chris review → promotion into a core file.

## Friction observed

`02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md`, Category 10,
names agent workflows as the "newest, highest risk/reward" AI capability —
but the file contains no criteria for judging that risk. The Recommendation
Ladder prices tools by cost; nothing prices them by agentic risk. This gap
has two edges:

1. **Client-facing:** when Chris recommends (or recommends *against*) an
   agent tool in an audit, he currently has no vendor-neutral risk lens to
   sell alongside the cost lens — even though the vendor-neutral moat is
   the file's stated selling strategy.
2. **`.ROOT`-facing:** the OS routes all tool-selection through this file,
   so any future agent tool adopted into Chris's own workflows passes
   through it with no safety screen.

The evidence this matters comes from [[2025-ai-agent-index]] (Staufer et
al., FAccT '26): across 30 major deployed agents, 135/240 safety fields had
no public information, only 4/30 had agent-specific safety evaluations,
21/30 don't disclose their AI nature by default, and the highest-autonomy
category (browser agents) is where documented incidents concentrate. The
market will not self-disclose; the buyer needs a checklist.

## File it would touch

`02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` — one additive
subsection under Category 10 (AI & Intelligent Automation). No other file
changes.

## Proposed change

Append a subsection, roughly this text (≤15 lines, matching the file's
compressed audit-usable style):

> **Vetting an agent tool (before recommending or adopting):**
> - **Form factor sets the risk floor:** chat-with-tools (lowest, turn-based)
>   → enterprise builder (guardrails become YOUR job once deployed) →
>   browser agent (highest autonomy, most documented incidents, highest
>   scrutiny).
> - **Five checks:** (1) agent-specific system card or safety eval exists —
>   not just base-model docs; (2) sandboxing/isolation documented;
>   (3) stop/pause controls at the single-agent level; (4) approval gates
>   on sensitive actions (payments, auth, file writes); (5) discloses or
>   identifies itself to third parties.
> - **Client math:** builder platforms (Copilot Studio, Agentforce, Zapier
>   AI) shift guardrail responsibility to the deploying business — that's a
>   hidden cost and liability line in the ROI math, not a footnote.
> - Failing checks isn't an automatic no — it prices the risk into the
>   recommendation. (Source: 2025 AI Agent Index; details in the
>   AI_AUTOMATION_SYSTEMS wiki.)

- **Agent-tool vetting screen:** before recommending or adopting an agent workflow, price risk as well as cost. Form factor sets   the risk floor: chat-with-tools → enterprise agent builder → browser/computer-use agent. Check for: agent-specific safety evals, sandboxing/isolation, single-agent stop/pause controls, approval gates for sensitive actions, and disclosure/identity behavior when interacting with third parties. Builder platforms shift guardrail responsibility to the deploying business; count that as hidden ROI/liability cost. Failed checks are not automatic rejection — they raise the risk price of the recommendation. Source detail lives in `03-WIKIS\AI_AUTOMATION_SYSTEMS`.

## Why better than status quo

- The file's own footer says "wiki refines; this file operationalizes" —
  this is precisely that hand-off: research already ingested in this wiki,
  compressed to audit-usable form.
- It extends the vendor-neutral moat into a dimension competitors don't
  sell (software salesmen never lead with "this agent can't be stopped
  mid-run").
- It gives `.ROOT` itself a safety screen for future agent-tool adoption
  at zero new-process cost — the file is already in the tool-selection
  path and already on a monthly review cadence.

## Risk / blast radius

- **Blast radius: one file, additive.** No governance rules, hats, or OS
  text change. Fully reversible by deleting the subsection.
- **Main risk: bloat.** The file is deliberately compressed; mitigation is
  the ≤15-line cap and the existing monthly review, which can prune or
  eject it to the wiki if unused.
- **Secondary risk: staleness.** The Agent Index is a Dec 2025 snapshot;
  the checklist criteria (system card, sandboxing, stop controls, gates,
  disclosure) are structural rather than vendor-specific, so they should
  age slowly. Vendor examples can be dropped if they date.

## Post-Change Check (added 2026-07-15, check_at discipline)

- **Expected behavior:** every new agentic tool considered for `.ROOT` gets the vetting screen applied before adoption; no tool enters use without a recorded system-card/sandboxing/stop-control review.
- **Evidence for improvement or regression:** DAILY/wiki-log entries for tool vettings citing the checklist. Regression = any tool adopted after 2026-07-08 with no vetting record.
- **check_at:** 2026-08-24 (first new-tool vetting event or the fall-semester toolset review, whichever comes first)
- **Outcome:** (blank until the check date — record what actually happened, with an evidence link)
- **Verdict:** (keep / modify / revert — blank until the check date)
