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

*Review dates re-set 2026-08-19 (flag #103): all six rows had passed or missing review
dates — Aug 1 ×1, Aug 14 ×2, Aug 16 ×1, one undated — because the weekly review cadence
stopped on Aug 7. No status, verdict, or priority changed in that sweep.
`castle_freshness.py` now fails on any past-date row.*

*Corrected 2026-08-22: the sentence here claimed **every** row points at the Aug 23
pre-semester review. The rows below do not, and never did after re-dating — **Aug 23 ×2**
(OPP-20260716-02, OPP-20260727-01, both live) · **Aug 30 ×1** (OPP-20260730-01) ·
**Sep 21 ×3** (the parked rows, which take the monthly review per § Review Rules). CASTLE's
`current-position.md` had inherited the wrong Aug 23 date for OPP-20260714-02 from that
sentence; fixed at both ends the same day.*

*✅ **Both Aug 23 rows disposed 2026-08-23** at the semester transition review, on Chris's
rulings. OPP-20260716-02 `researching → parked` (no access); OPP-20260727-01 held at
`captured`, re-dated. **The queue now carries no past review date**, which is what
`castle_freshness.py` checks on Monday. Standing shape: **`parked` ×4 · `researching` ×1
(OPP-20260730-01, Aug 30) · `captured` ×1.** Four of six rows are parked and **three of those
four are parked for the same reason — no warm-network access to the vertical the test needs.**
That is the single most useful fact this queue currently holds; it is recorded in
OPP-20260716-02's Result cell so it travels with a row rather than living only in a note.*

| ID | Captured | Type | Signal | Evidence | Status | Priority | Owner realm | Next test/action | Review date | Result / asset |
|---|---|---|---|---|---|---|---|---|---|---|
| OPP-20260714-01 | 2026-07-14 | learning-to-application | Contractors may pay for remote estimating/change-order support, but Chris-specific demand is untested. | [[../../../03-WIKIS/REVENUE_LAB/wiki/revenue-lane-scorecard#B2 — Direct-network estimating / change-order support]] | parked | normal | `03-WIKIS\BUSINESS` + `REVENUE_LAB` evidence | The contractor friend approved for this conversation (2026-07-22) is ~1,000 miles away; Chris does not have time to travel or realistically coordinate a remote equivalent right now (confirmed directly with Chris, 2026-07-27). The designed test can't run as written — same access-blocked class as OPP-20260716-01, not a merit judgment. Do not resurface without a closer contact or a workable remote-conversation path. | 2026-09-21 | Parked 2026-07-27 for lack of access. Note the reverse dependency: OPP-20260716-01 (flippers) had pointed to *this* row as the reachable vertical for the same evidence-gathering method — both construction-adjacent tests are now access-blocked at the same time, worth flagging at the next opportunity-queue review rather than treating as two independent misses. |
| OPP-20260714-02 | 2026-07-14 | learning-to-application | A YouTube public-data outlier scanner compounds Python/SQL/API skill while testing whether a viable content niche exists. | [[../../../03-WIKIS/REVENUE_LAB/wiki/yt-outlier-scanner-first-findings-2026-07-14]] | parked | normal | `03-WIKIS\REVENUE_LAB` | No action while Chris's project folder remains explicitly `YT_Outlier_Scanner(Pause, chris)`. Reactivate only on Chris's direct instruction; then resume at human classification, not publishing or monetization. | 2026-09-21 | Paused by Chris before 2026-07-24. Internal scanner evidence remains valid; income/RPM and acquisition remain unverified. |
| OPP-20260716-01 | 2026-07-16 | learning-to-application | Residential flippers face compressed gross returns, creating a plausible need for deal-level margin-variance and cost-to-complete visibility. | [[../../../03-WIKIS/BUSINESS/wiki/evidence/market-map#Real-Estate Ecosystem Entry Ranking — 2026-07-16]] | parked | high | `03-WIKIS\BUSINESS` | No warm-network flipper contact currently exists (confirmed directly with Chris, 2026-07-23) — the designed test can't run as written. Do not resurface without a new contact or new evidence; if one surfaces, the smallest-honest-proof design above is still valid as-is. | 2026-09-21 | PASS at profit gate: Phase 2 service proof (verdict unchanged). Parked 2026-07-23 for lack of access, not lack of merit. The underlying method — reconstruct one completed job's original-vs-actual costs into a one-page variance finding — isn't exclusive to flippers: it's already live in construction via [[opportunity-queue#OPP-20260714-01|OPP-20260714-01]] (the approved B2 change-order/estimating conversation), which tests the same evidence-gathering pattern in a vertical Chris actually has access to. |
| OPP-20260716-02 | 2026-07-16 | technology opportunity | Cross-party closing handoffs may hide repeated missing-item chasing and delay, but existing transaction platforms and regulated ownership make the unsolved local problem unknown. | [[../../../03-WIKIS/BUSINESS/wiki/evidence/market-map#Real-Estate Ecosystem Entry Ranking — 2026-07-16]] | parked | normal | `03-WIKIS\BUSINESS` | **Parked 2026-08-23 for lack of access — not a merit judgment.** Chris approved advancing 2026-08-02 and the designed next step was to arrange access to one safe, redacted delayed/failed transaction to reconstruct. **Confirmed directly with Chris 2026-08-23: no such access exists.** The test cannot run as written. Do not resurface without a reachable transaction or a new access path; if one surfaces, the step above is still valid as-is. Advance only if the same exception repeats, has a measurable consequence, and has a reachable process/budget owner. | 2026-09-21 | HOLD at profit gate retained: no platform build; unlock requires local workflow evidence and lawful data access. **Parked 2026-08-23.** ⚠ **Pattern, recorded once rather than as three separate misses:** this is the *third* construction/real-estate-adjacent test blocked on access simultaneously — with OPP-20260714-01 (parked 2026-07-27) and OPP-20260716-01 (parked 2026-07-23). All three designed a sound smallest test and all three failed at the same gate: **Chris has no warm-network access to the vertical the method needs.** That is one finding about the access constraint, not three about the ideas. It is the real input to any future Advisor-Builder lane choice. |
| OPP-20260727-01 | 2026-07-27 | technology opportunity | A trading card store POS plug-in app — Chris named it as a potentially large build with real payoff, but named no specific store/company and did not scope it. | [[../../../00-BRAIN/Session_Logs/Report Archive/ARCHIVED_2026-07-27_DAILY_2026-07-27.md#Evening (after Watchtower review) — Claude Code — Watchtower reword, idea capture]] | captured | normal | `03-WIKIS\BUSINESS` or `03-WIKIS\TECHNOLOGY` (owner realm undetermined until scoped) | **Held at `captured` and re-dated 2026-08-23 — deliberately, with the reason stated.** Moving to `triaged` requires type, displacement, owner realm and next decision (§ Status Gates); **none of those exist without the scoping interview this row itself calls for**, and that interview needs a real hour the semester ramp does not have. That session must establish: target store/company (or speculative-market with no lead yet), what "POS plug-in" actually means here (integration with an existing POS platform, or a standalone tool), rough technical size, and a payoff estimate. | 2026-09-21 | **Re-dated 2026-08-23 to the monthly review, not disposed.** Still the thinnest row in the queue — an idea named, never scoped. It has now been re-dated twice without the interview; **if Sep 21 arrives with no scoping session, park it rather than re-date a third time.** An indefinitely re-dated row is how a queue starts lying. |
| OPP-20260730-01 | 2026-07-30 | technology opportunity | A parent-governed AI education partner could convert children’s existing device time into adaptive, proof-based learning while giving parents explicit rules and oversight. | [[../../../00-BRAIN/Session_Logs/Report Archive/ARCHIVED_2026-07-30_DAILY_2026-07-30.md#Afternoon — Codex — profit gate: parent-governed AI education partner]] | researching | normal | `03-WIKIS\BUSINESS` + `AI_AUTOMATION_SYSTEMS` evidence; `.ROOT` learning engines are internal method evidence | Interview 1 of 5 completed with Chris as a parent (founder-bias caveat). Repeated problem still unproven across households. Manual suggestion protocol paused by Chris on 2026-07-30 before any content queue was populated. Resume only after Chris approves the trusted source set from which candidates may enter. Advance only after five adult interviews reveal the same job-to-be-done and at least three parents commit to an age-appropriate manual prototype. | 2026-09-21 | **Hold confirmed at the 2026-08-30 Sunday return** — four interviews still outstanding and the weeks 1–4 surplus is committed to the assessment lead, so no interview hour exists before the Sep 21 monthly review; re-dated to ride with it. Prior: HOLD retained after interview 1. The interview established the parent job and constraints; it did not validate content sources. Demand, acquisition, cross-parent repetition, child safety, compliance, learning durability, and economics remain unproven. |

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
