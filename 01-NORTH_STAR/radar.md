---
type: board
timeline: now
tags: [watchtower]
---

# RADAR — Live Signal Board
### 🔥 HOT · 👁 WATCHING · ⏸ COOLING · ✅ GATED/TESTING · 🧪 OUTCOME · 🗑 PRUNED

Only rows that pass the four-part promotion threshold in
[WATCHTOWER.md](WATCHTOWER.md) belong here. Newest first. Link to evidence; do not
copy the research into this board.

| Date | Signal | Evidence home / source tier | Affects | Consequence or bounded test | Status | Next review | CASTLE gate / outcome |
|---|---|---|---|---|---|---|---|
| 2026-07-16 | MCP (Model Context Protocol) is now the multi-vendor open standard for exposing business systems to AI: Linux Foundation governance; Anthropic/OpenAI/Google/Microsoft/AWS support; next spec (stateless core, extensions, enterprise-managed auth) is an RC locked May 21 with final publication expected 2026-07-28; Zapier and Make already expose their connector catalogs as MCP tools; SAP embedded n8n at a $5.2B valuation. Raw "connect the AI to the thing" labor is commoditizing into config. | [TECHNOLOGY evidence](../03-WIKIS/TECHNOLOGY/wiki/api-integration-layer-2026-landscape.md) / Tier 1 official spec blog for status; Tier 2-3 vendor docs and press for adoption/valuation numbers | `TECHNOLOGY_LIBRARY_STRATEGY` Category 9 (what the INTEGRATE rung contains) and the Category 10 agent-tool vetting screen; capability-trace rung 4 (custom glue vs. commodity config boundary) | Before any custom AI-system glue is recommended or built, first check whether an MCP/connector config already covers it (new ladder discipline, applies immediately). **2026-07-17 update:** the anticipated bounded rep is now underway (see CASTLE gate/outcome column) — not a scanner query as originally sketched here, but a small purpose-built fixture derived from `05-BUSINESS\02-Field Notes\observation_one.md`, avoiding any scanner-boundary risk. Tool-poisoning risk (OWASP LLM Top 10 #1) prices into any recommendation per the vetting screen, and the proof standard explicitly excludes write actions, arbitrary SQL, and credentials. **2026-07-28 close:** the final spec published on schedule (Tier 1, `https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/`) — stateless core, MCP Apps + Tasks extensions, OAuth/OIDC-aligned auth, formal deprecation policy, all four Tier-1 SDKs (TS/Python/Go/C#) day-one compliant. Matches the May 21 RC prediction; no surprise. | 🗑 PRUNED | closed — no further review | 2026-07-17: CASTLE profit gate PASSED (bounded) for one local Python MCP server as an integration capstone inside a Jul 18–25 pre-D2L technology sprint, corrected same-day by Claude's independent review (`00-BRAIN\Session_Logs\Report Archive\ADVISOR_BUILDER_INTEGRATION_BOOT_CAMP_REVIEW_2026-07-17.md` — path corrected 2026-07-27). **Closed 2026-07-27:** the July 25 weekly cutoff found real gaps (tests, security handoff, Day 5 explain-back), but a July 26 post-review pass finished the missing engineering (14 green tests, full stdio verification, security/operator handoff, Product/Value + Integration layers) and Chris supplied the cold explain-back himself, correctly tracing the full host/client/server/tool/SQLite chain — **Final post-review bootcamp verdict: COMPLETE** (`02-LIBRARY\.PROJECTS\MCP_Bootcamp\Docs\weekly-code-learning-review-2026-07-20-to-2026-07-25.md`, "Post-review MCP machine completion — July 26"). Scope caveat stated in that same record: this closes the *bounded learning capstone* only — no production readiness, client demand, or market validation claimed. Build stays capped ≤3 hrs, one read-only resource + two read-only tools, real host connection, no remote deployment. **2026-07-28: spec-finalization confirmation received, row pruned — the learning capstone was already COMPLETE; this was the last open thread on this signal.** |
*(The July 6 product rumor has no verified evidence home and is not promoted;
research belongs in AI_AUTOMATION_SYSTEMS if it resumes. The internal Watchtower
seed event remains system history, not an external signal.)*

## Parked Gate Verdicts

When CASTLE says no or not yet, keep one concise record here: signal, verdict,
reason, and reconsideration trigger. The full decision remains in CASTLE.

| Date parked | Signal | Verdict | Reason | Reconsideration trigger |
|---|---|---|---|---|
| 2026-07-27 | AGC's 2026 contractor outlook (61% AI use/investment, concentrated in office/admin, estimating, preconstruction) | PARKED — not pruned as invalid, just access-blocked | The bounded test this row depended on was one specific contractor's approved change-order conversation (`opportunity-queue.md` OPP-20260714-01). That contact is ~1,000 miles away; Chris does not have time to travel or realistically coordinate a remote equivalent right now. The underlying AGC signal itself is not disputed — only this one access path is closed. | A closer/reachable contractor or construction contact becomes available through Heather's network or elsewhere. No date-based re-check — this waits on access, not time. |

## Standing Scan Questions

1. Did an AI capability, agent platform, price, or policy change alter what Chris or
   a client can economically build?
2. Did a tool in the active automation/data stack materially improve, degrade, or
   become replaceable?
3. Did a real-estate, construction, field-service, or open-market change strengthen
   or weaken an Advisor-Builder access or demand assumption?
4. Did regulation, security guidance, or buyer behavior change the safe offer?
5. Did a KSU/ISYE-adjacent technology become important enough to test as capability?
