---
type: map
timeline: now
tags: [business, opportunities]
created: 2026-07-14
status: live
---

# Opportunity Queue

One visible queue for commercial and learning-to-application signals after
their source evidence has a permanent home. This page does not replace field
notes, wiki research, project files, or `SYSTEM_FLAGS.md`.

## Lifecycle

`captured → triaged → researching → worth testing → active build/offer → tested → won / lost / parked → asset harvested`

## Types

- **client lead** — a named prospect or real request;
- **observed waste** — a repeatable operational problem backed by a field note;
- **technology opportunity** — a tool/capability with a plausible value path;
- **learning-to-application** — knowledge ready for a real use or proof.

Internal `.ROOT` friction stays in `SYSTEM_FLAGS.md`. Link a flag here only when
it independently becomes a commercial or strategic opportunity.

## Entry Contract

- ID: `OPP-YYYYMMDD-##`.
- Every row links to evidence; a thought without evidence remains a note.
- Client leads enter at `triaged`, priority `urgent`, with an immediate next
  action. External contact, pricing, or commitment still requires Chris approval.
- Other signals enter at `captured` and move only when the named criterion is met.
- A build starts only after triage names an outcome, owner realm, and smallest test.
- Closing an opportunity records the result and asks what asset was harvested.

## Active Queue

| ID | Captured | Type | Signal | Evidence | Status | Priority | Owner realm | Next test/action | Review date | Result / asset |
|---|---|---|---|---|---|---|---|---|---|---|
| OPP-20260714-01 | 2026-07-14 | learning-to-application | Contractors may pay for remote estimating/change-order support, but Chris-specific demand is untested. | [[../../../03-WIKIS/REVENUE_LAB/wiki/revenue-lane-scorecard#B2 — Direct-network estimating / change-order support]] | parked | normal | `03-WIKIS\BUSINESS` + `REVENUE_LAB` evidence | The contractor friend approved for this conversation (2026-07-22) is ~1,000 miles away; Chris does not have time to travel or realistically coordinate a remote equivalent right now (confirmed directly with Chris, 2026-07-27). The designed test can't run as written — same access-blocked class as OPP-20260716-01, not a merit judgment. Do not resurface without a closer contact or a workable remote-conversation path. | 2026-08-14 | Parked 2026-07-27 for lack of access. Note the reverse dependency: OPP-20260716-01 (flippers) had pointed to *this* row as the reachable vertical for the same evidence-gathering method — both construction-adjacent tests are now access-blocked at the same time, worth flagging at the next opportunity-queue review rather than treating as two independent misses. |
| OPP-20260714-02 | 2026-07-14 | learning-to-application | A YouTube public-data outlier scanner compounds Python/SQL/API skill while testing whether a viable content niche exists. | [[../../../03-WIKIS/REVENUE_LAB/wiki/yt-outlier-scanner-first-findings-2026-07-14]] | parked | normal | `03-WIKIS\REVENUE_LAB` | No action while Chris's project folder remains explicitly `YT_Outlier_Scanner(Pause, chris)`. Reactivate only on Chris's direct instruction; then resume at human classification, not publishing or monetization. | 2026-08-14 | Paused by Chris before 2026-07-24. Internal scanner evidence remains valid; income/RPM and acquisition remain unverified. |
| OPP-20260716-01 | 2026-07-16 | learning-to-application | Residential flippers face compressed gross returns, creating a plausible need for deal-level margin-variance and cost-to-complete visibility. | [[../../../03-WIKIS/BUSINESS/wiki/evidence/market-map#Real-Estate Ecosystem Entry Ranking — 2026-07-16]] | parked | high | `03-WIKIS\BUSINESS` | No warm-network flipper contact currently exists (confirmed directly with Chris, 2026-07-23) — the designed test can't run as written. Do not resurface without a new contact or new evidence; if one surfaces, the smallest-honest-proof design above is still valid as-is. | 2026-08-01 | PASS at profit gate: Phase 2 service proof (verdict unchanged). Parked 2026-07-23 for lack of access, not lack of merit. The underlying method — reconstruct one completed job's original-vs-actual costs into a one-page variance finding — isn't exclusive to flippers: it's already live in construction via [[opportunity-queue#OPP-20260714-01|OPP-20260714-01]] (the approved B2 change-order/estimating conversation), which tests the same evidence-gathering pattern in a vertical Chris actually has access to. |
| OPP-20260716-02 | 2026-07-16 | technology opportunity | Cross-party closing handoffs may hide repeated missing-item chasing and delay, but existing transaction platforms and regulated ownership make the unsolved local problem unknown. | [[../../../03-WIKIS/BUSINESS/wiki/evidence/market-map#Real-Estate Ecosystem Entry Ranking — 2026-07-16]] | researching | normal | `03-WIKIS\BUSINESS` | **Chris approved advancing 2026-08-02.** Next concrete step: Chris identifies or arranges access to one safe, redacted delayed/failed transaction (agent, attorney, broker, or investor) to reconstruct. Still advance only if the same exception repeats, has a measurable consequence, and has a reachable process/budget owner. | 2026-08-16 | HOLD at profit gate: no platform build; unlock requires local workflow evidence and lawful data access. |
| OPP-20260727-01 | 2026-07-27 | technology opportunity | A trading card store POS plug-in app — Chris named it as a potentially large build with real payoff, but named no specific store/company and did not scope it. | [[../../../00-BRAIN/Session_Logs/DAILY_2026-07-27.md#Evening (after Watchtower review) — Claude Code — Watchtower reword, idea capture]] | captured | normal | `03-WIKIS\BUSINESS` or `03-WIKIS\TECHNOLOGY` (owner realm undetermined until scoped) | Chris said he wants a dedicated interview session soon — not urgent tonight. That session should establish: target store/company (or is this speculative-market, no lead yet), what "POS plug-in" actually means here (integration with an existing POS platform, or a standalone tool), rough technical size, and a payoff estimate before this can move to `triaged`. | — | — |
| OPP-20260730-01 | 2026-07-30 | technology opportunity | A parent-governed AI education partner could convert children’s existing device time into adaptive, proof-based learning while giving parents explicit rules and oversight. | [[../../../00-BRAIN/Session_Logs/DAILY_2026-07-30.md#Afternoon — Codex — profit gate: parent-governed AI education partner]] | researching | normal | `03-WIKIS\BUSINESS` + `AI_AUTOMATION_SYSTEMS` evidence; `.ROOT` learning engines are internal method evidence | Interview 1 of 5 completed with Chris as a parent (founder-bias caveat). Repeated problem still unproven across households. Manual suggestion protocol paused by Chris on 2026-07-30 before any content queue was populated. Resume only after Chris approves the trusted source set from which candidates may enter. Advance only after five adult interviews reveal the same job-to-be-done and at least three parents commit to an age-appropriate manual prototype. | 2026-08-30 | HOLD retained after interview 1. The interview established the parent job and constraints; it did not validate content sources. Demand, acquisition, cross-parent repetition, child safety, compliance, learning durability, and economics remain unproven. |

## Status Gates

| Status | Required evidence to enter |
|---|---|
| captured | permanent evidence link and one-sentence signal |
| triaged | type, displacement, owner realm, and next decision |
| researching | bounded question and source standard |
| worth testing | smallest test, success signal, and time/cost bound |
| active build/offer | Chris-approved outcome and execution home |
| tested | observed result recorded |
| won / lost / parked | decision and reason recorded |
| asset harvested | reusable output linked with honest maturity |

## Review Rules

- Urgent client leads: immediate triage.
- Active tests/builds: review at the named date.
- Captured general signals: weekly CASTLE review.
- Parked items: monthly review only; do not repeatedly resurface them without new evidence.
