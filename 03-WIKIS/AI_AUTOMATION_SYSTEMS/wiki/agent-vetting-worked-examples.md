---
type: research
tags: [ai-automation, agentic-ai, vetting, tools, now]
source: raw/2025 Index*.md (aiagentindex.mit.edu clippings, snapshot Dec 31 2025) + raw/Further Details — 2025 AI Agent Index.md
---

# Agent-Tool Vetting — Worked Examples from the 2025 AI Agent Index

Operationalizes the **Agent-tool vetting screen** promoted into
`TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10 (July 8, 2026). Eight agents
scored against the screen's five checks, using the per-agent annotation data
Chris clipped from aiagentindex.mit.edu. Chosen set: the two CLI agents in
`.ROOT`'s own orbit, one bonus CLI comparator, the four enterprise builders
most likely to appear in an SMB audit, and one browser agent as the
what-failing-looks-like row.

## The scorecard

✅ documented · ⚠️ partial/conditional · ❌ none found · — not applicable

| Agent (form factor) | 1. Agent-specific safety evals | 2. Sandboxing / isolation | 3. Stop/pause a running agent | 4. Approval gates on sensitive actions | 5. Discloses / identifies to third parties |
|---|---|---|---|---|---|
| **Claude Code** (chat/CLI) | ✅ system card w/ agentic-misuse section + Gray Swan third-party red-team | ✅ sandboxed bash (filesystem+network isolation); writes only in start folder | ✅ anytime | ✅ read-only by default; permission for bash/edits/out-of-dir reads | ⚠️ published UA tokens, no fixed IPs; policy bans human impersonation |
| **OpenAI Codex** (chat/CLI) | ✅ system-card addendum (cyber, data destruction, CBRN) + Irregular external evals | ✅ OS-level sandbox by default | ✅ anytime | ✅ read-only until directory explicitly trusted | ❌ none found |
| **Gemini CLI** (chat/CLI) | ⚠️ model-card level only (not agent-specific) | ⚠️ optional sandbox; untrusted folders run in "safe mode" | ✅ anytime | ✅ confirm before shell/edit operations | ❌ none found; robots.txt behavior unspecified |
| **Zapier Agents** (builder) | ❌ | ❌ | ✅ pause/stop + activity log & run history | ⚠️ agent asks on ambiguity/error; otherwise runs in background once configured | ❌ |
| **n8n Agents** (builder) | ❌ | ⚠️ code runners in VMs; Guardrails node exists but user must wire it | ❌ **no stop once running** (only pause whole system) | ⚠️ approve/decline gates exist but are designer-configured | ❌ default headers, author-configurable |
| **MS Copilot Studio/Agents** (builder) | ⚠️ internal RAI evals + OWASP-LLM pentest claimed, results not public | ❌ | ✅ + admin-center monitoring | ⚠️ agent returns for confirmation/next steps | ✅ AI-content disclaimer in UI; C2PA on images; web via Bing (robots.txt) |
| **HubSpot Breeze** (builder) | ⚠️ red-team claimed (no details); PacketLabs pentest — prompt injection NOT remediated | ❌ (natural sandbox = CRM scope only) | ❌ **no stop once running** (pause system only) | ⚠️ default ON at creation, but auto-triggered agents skip approval | ⚠️ "Powered by AI" label on customer-facing chat only |
| **Perplexity Comet** (browser) | ❌ mitigations blogged, no evals/results, no third-party testing | ❌ | ✅ | — (L4–L5: no user involvement during execution) | ❌ Chrome-like UA, residential IPs; robots.txt behavior undocumented in the index (the "ignored for user-driven fetches" claim traces to third-party reporting, not the index — cite accordingly) |

## What the table says (audit-usable readout)

1. **The CLI agents are the only clean passes.** Claude Code and Codex pass
   all five checks — agent-specific system cards, default sandboxes,
   permission-gated writes. This is what "priced-in risk ≈ low" looks like,
   and both charge $20–200/mo. Gemini CLI is close behind (model-level evals
   only).
2. **Builder platforms fail on evals and sandboxing, not on controls.**
   All four builders have monitoring/logging, but none publishes
   agent-specific safety evaluations, and none sandboxes the deployed agent
   itself — confirming the promoted screen's "guardrails become YOUR job"
   warning. Extra confirmation: Zapier's bug bounty explicitly lists
   agents.zapier.com as *out of scope*; n8n has no bounty at all (email
   only).
3. **The stop-control check earns its place.** Two of four builders (n8n,
   HubSpot Breeze) cannot stop an individual running agent — only pause the
   entire system. For a client running an auto-triggered agent on live CRM
   data, that's a concrete liability line, not a theoretical one.
4. **The auto-trigger loophole is the builder pattern to flag in audits.**
   HubSpot defaults approvals ON at design time, but automatically triggered
   agents (on data change, inbound email, etc.) run with *no* approval. The
   design-time setting quietly stops applying at run time — exactly the
   L1-design / L5-deployed split the Index paper documented.
5. **Comet fails everything but the stop button** — and has the incident
   record to match: a hidden MCP API allowing local command execution
   (found by third parties) and Brave-documented indirect prompt injection.
   The risk price on browser agents is not hypothetical.
6. **Known incidents are not disqualifiers by themselves** — Claude Code
   (espionage campaign disclosed by Anthropic itself) and Copilot
   (CVE-2025-32711) both have incidents *and* strong disclosure. Per the
   screen: failed checks price risk; how the vendor handled the incident is
   part of that price.

## Coverage and provenance notes

- Source clippings are category-per-file exports: `2025 Index.md` (full
  Claude Code card), `1` = autonomy & control, `2` = product overview,
  `3` = company & accountability, `4` = technical capabilities,
  `5` = ecosystem interaction, `6` = safety/evaluation. Entries inside each
  file are unlabeled; matches to agents were made by content (e.g., cited
  vendor URLs). ~22 of 30 agents came through — enough for this set, not
  the full Index.
- Snapshot: Dec 31, 2025. Live corrections land at aiagentindex.mit.edu.
- **Spot-checked against the live site July 8, 2026 (all 8 rows,
  per-agent pages `aiagentindex.mit.edu/2025/<agent>`).** Every scored
  cell confirmed verbatim or near-verbatim — including both no-stop
  findings (n8n: "doesn't seem to be an option to stop agent after it
  starts running"; Breeze: pause is "the system as a whole"), the Breeze
  auto-trigger loophole ("if automatically triggered agents, there is no
  user approval") and unremediated prompt injection ("everything except
  for prompt injection was remediated"), Zapier's bounty exclusion
  (agents.zapier.com "out of scope"), and the full Claude Code / Codex
  clean-pass rows. One correction applied: the Comet robots.txt cell —
  the index itself records no robots.txt behavior; that claim is
  third-party reporting. Verdicts unchanged. Table is quotable in client
  deliverables as of this date.
- Pricing (monthly, from product-overview clippings): Claude Code 20/100/200
  · Codex bundled in ChatGPT 20/200 · Gemini CLI free/20/125 · Zapier
  Agents free/50/custom · n8n 25/60/800 (self-hostable) · Breeze inside
  HubSpot Pro 216 / Ent 587 (OpenAI models only, auto-selected) · Comet
  free/20/200.

Related: [[2025-ai-agent-index]] (the source study),
[[agentic-ai-industry-adoption-barriers]] (why verification is the gate),
proposal `proposals/2026-07-08_agentic-tool-vetting-checklist.md` (the
screen this operationalizes).
