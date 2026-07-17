---
type: report
timeline: now
status: confirmed-go-locking-in-record
tags: [technology, business, mcp, boot-camp, advisor-builder]
created: 2026-07-17
reviewer: Claude
---

# Advisor-Builder Integration Boot Camp — Claude Edit and Review Packet

## Review Request

Chris asked Codex to determine whether the final pre-D2L window should become a
technology boot camp and then corrected the proposed focus toward MCP and the dream
business in `01-NORTH_STAR\NORTH_STAR.md`.

Claude should independently edit and challenge this proposal before it becomes the
execution plan. Specifically:

1. Verify that the stack serves the Advisor-Builder business rather than technology
   novelty.
2. Check whether MCP is correctly positioned as the integration capstone instead of
   the business or the entire curriculum.
3. Reduce or reorder anything that exceeds the real July 17–25 capacity.
4. Preserve learning depth: Chris wants to move rapidly without losing the material.
5. Recommend the exact proof vehicle and dated sequence.
6. Identify any conflict with the pre-semester plan, current phases, or July 26 D2L
   transition.

This report is a proposal. It does not authorize a new project, remote deployment,
account creation, paid services, or changes to `NOW.md`.

## Time Box

- **Remainder of Friday, July 17:** review, finalize the stack, and establish the
  starting baseline.
- **Eight full working days, July 18–25:** boot-camp execution.
- **Sunday, July 26:** hard transition to D2L document intake, syllabus and AI-policy
  verification, Academic Tracker population, and the first real school-prep week.
- Preserve one focused school proof block daily during the sprint: finish Python
  Stage 3 first and keep Physics Stage 4 moving.

## Controlling Direction

The durable mission is the Advisor-Builder in `01-NORTH_STAR\NORTH_STAR.md`; the
current vehicle and execution loop are in
`01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md`:

`Observe -> Diagnose -> Engineer -> Deploy -> Train and Retain -> Harvest`

The business enters a real operation, maps the work, finds measurable waste,
recommends the cheapest valid response, builds or integrates technology only when
earned, trains the people involved, maintains what works, and harvests reusable
assets. Construction credibility and Heather's real-estate network are current
access wedges, not permanent market boundaries.

The most important alignment warning comes from CASTLE Phase 2: **diagnosis is the
first product; building is downstream.** A successful MCP server proves a technical
capability, not client readiness or demand.

## Decision Trail and Correction

Two July 16 decisions were initially conflated:

1. The goal-aligned technology gap audit selected the existing YouTube scanner's
   SQL/reliability chain as the next conventional application proof.
2. The Category 9 landscape rep promoted MCP to `...projectSuccess\radar.md` as a
   material multi-vendor integration signal. Its recorded state was WATCHING until
   the July 28 specification finalization, with no build absent a CASTLE gate and a
   possible later <=90-minute local rep.

Codex first drafted the boot camp around the scanner. Chris correctly pushed back
that the important prior conversation concerned MCP. The corrected proposal is:

- MCP becomes the boot camp's **integration capstone**.
- Python, SQL, testing, CI, security, and operating discipline remain the supporting
  structure.
- The YouTube API, content/channel decisions, further harvesting, and dashboard work
  are removed from the sprint.
- Existing scanner data could supply one harmless read-only query, but only as test
  data. MCP—not YouTube—is the subject. Claude should recommend a better proof
  vehicle if one serves the North Star with less baggage or risk.

## Durable Advisor-Builder Technology Architecture

| Business movement | Required capability | Technology layer |
|---|---|---|
| Observe the real workflow | Capture facts, steps, handoffs, delays | Field notes, Forms, Sheets, process maps, VSM |
| Diagnose the waste | Organize and interrogate evidence | Python, CSV/JSON, SQL, SQLite, later pandas |
| Quantify the consequence | Calculate time, cost, margin, risk | Python calculations, SQL aggregation, conservative ROI models |
| Recommend the smallest fix | Compare eliminate/configure/integrate/build | Recommendation Ladder and vendor-neutral application map |
| Connect existing systems | Move information safely | Native integrations, Make/Zapier/n8n, REST APIs, webhooks, MCP |
| Build when justified | Create bounded internal tools | Python, Flask, SQLAlchemy, REST, HTML/CSS |
| Make the result usable | Show the decision clearly | Sheets, Looker Studio, Markdown/PDF reports |
| Operate and maintain | Keep systems reliable | Git, pytest, CI, logs, backups, restore, monitoring |
| Add AI responsibly | Automate judgment-flavored work | MCP, model APIs, structured outputs, evals, approval, rollback |
| Harvest the asset | Reuse proven work | Repositories, templates, playbooks, sanitized case studies |

This architecture follows the Recommendation Ladder: eliminate -> simplify -> use
what exists -> configure -> integrate -> build light -> build real. MCP sits inside
the integration/AI boundary; it is plumbing, not the house.

## Proposed Boot-Camp Stack

### Primary build spine

`Python 3 -> SQL/SQLite -> typed data/JSON -> API and tool boundaries -> official
MCP Python SDK/FastMCP -> local stdio -> MCP Inspector -> pytest -> Git/GitHub
Actions -> logging/permissions/operator handoff`

### Workbench

- VS Code and PowerShell/terminal
- Git and GitHub
- Codex/Claude Code as build multipliers, with Chris explain-back and independent
  work required before capability credit

### Application-network awareness

- Google Forms, Sheets, and Looker Studio
- Zapier, Make, and n8n
- conventional REST APIs and webhooks
- MCP hosts, clients, and servers
- Flask/internal applications
- governed model/API features

These are mapped, not all built. Each exposure must answer: problem solved, input
and output, cheapest prior rung, maintenance owner, failure/security risk, and the
evidence that would justify adoption.

## Proposed MCP Proof Standard

Build one small local MCP server that exposes:

- one read-only resource;
- two narrowly defined read-only tools;
- typed and validated inputs;
- structured outputs and meaningful error responses;
- tests for normal, edge, invalid, and prohibited operations;
- successful use through the official MCP Inspector;
- successful connection from one real MCP host;
- tool-call logging and an explicit least-privilege boundary;
- a short security and operator handoff.

Do not expose arbitrary SQL, broad filesystem access, credentials, or write actions.
For stdio, never log to stdout; use stderr or files so JSON-RPC traffic is not
corrupted. MCP roots are advisory coordination, not a security boundary.

## July 28 Specification Boundary

The official MCP release candidate is locked, with final publication scheduled for
July 28 and documented breaking changes. The sprint may safely practice durable
local fundamentals: server, tools/resources, stdio, schema validation, tests,
Inspector, host connection, logging, and least privilege.

Defer until after finalization and a later gate:

- production remote deployment;
- OAuth or enterprise authorization architecture;
- MCP Apps and release-candidate extensions;
- public hosting or a production client integration;
- any claim that the prototype is client-ready.

Official references checked by Codex July 17:

- `https://modelcontextprotocol.io/docs/sdk`
- `https://modelcontextprotocol.io/docs/tools/inspector`
- `https://py.sdk.modelcontextprotocol.io/`
- `https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/`

## Learning-Speed Contract

Chris wants to move quickly without losing the material. Each major concept should
pass this loop:

1. One exact plain-language meaning.
2. Construction or real-workflow physical anchor.
3. Guided use inside a visible skeleton.
4. Independent change or rebuild by Chris.
5. Explain-back: what sits where, what flows, and why.
6. Deliberate failure and diagnosis.
7. Next-day cold check without yesterday's notes.
8. Evidence artifact: code, test, diagram, commit, or operating note.

Terms should be reinforced through working code rather than isolated documentation.
No stage or capability closes because AI generated the artifact.

## Displacement and Stop Rules

The sprint displaces:

- broad technology reading;
- `.ROOT` architecture work;
- unrelated app tours or new projects;
- new YouTube research/content decisions;
- decorative dashboard iteration;
- speculative business expansion.

It does not displace the daily school proof floor or the July 26 D2L transition.

Stop or scope down when:

- two sessions in a row are stuck at the same boundary;
- Chris cannot independently explain the previous layer;
- the build requires production auth/remote deployment before July 28;
- the proof vehicle creates more work than the MCP learning itself;
- the work begins replacing Python/Physics proof or D2L readiness.

## Open Decisions for Claude and Chris

1. What exact data/proof vehicle should the local MCP server expose?
   - one harmless read-only query against existing scanner data;
   - a different existing, authorized internal dataset;
   - a deliberately small neutral fixture;
   - another better North-Star-aligned option Claude identifies.
2. Should the sprint build only a server, or also a minimal client after one host
   connection works?
3. How much time should application-network mapping receive each day without
   weakening the build and learning proof?
4. What is the minimum honest finish line for July 25?
5. Does the sprint need a named repository/project, or can it remain a bounded lab
   until the proof earns continuation?

## Technology Raw/Source Readiness Audit — Codex Addendum

Codex reconciled all 39 physical content files in
`03-WIKIS\TECHNOLOGY\raw` against the hub ledger. One new file was absent from
the 38-row ledger: Microsoft's `Install Hyper-V in Windows and Windows Server.md`.
It is now registered as reference-only. Hyper-V is not required for the proposed
local MCP stdio proof and enabling it would be a separate administrator/restart
decision with possible hypervisor conflicts.

**Verdict: no new raw ingest or book compilation is needed for the boot camp.**
The useful packet is already retrievable:

- `TECHNOLOGY/wiki/database-sql/practical-sql.md` and its schema, relationship,
  constraint, grouping, transaction, and query pages;
- `TECHNOLOGY/wiki/software-engineering/software-testing-levels-and-techniques.md`;
- `TECHNOLOGY/wiki/software-engineering/reliable-programming-techniques.md`;
- `TECHNOLOGY/wiki/software-craft/clean-code-error-handling-testing-and-smells-checklist.md`;
- `TECHNOLOGY/wiki/security/api-security-testing-engagement-scoping-and-checklist.md`;
- `TECHNOLOGY/wiki/api-integration-layer-2026-landscape.md` for retries,
  idempotency, authentication, and the MCP/connector decision boundary;
- `AI_AUTOMATION_SYSTEMS/wiki/mcp-landscape-architecture-and-patterns.md`;
- `AI_AUTOMATION_SYSTEMS/wiki/mcp-client-primitives-and-build-notes.md`;
- `AI_AUTOMATION_SYSTEMS/wiki/mcp-security-and-authorization.md`;
- the PYTHON staged path for actual Python mechanics and retention gates.

Use these as just-in-time references, not a reading syllabus. OAuth, Flask,
distributed systems, Hyper-V, industrial/IoT volumes, and advanced methods remain
behind the live build trigger.

## Requested Claude Return

Return an edited recommendation with:

- **Verdict:** approve, modify, or reject the proposed stack;
- **Critical correction:** the largest misalignment or overload risk;
- **Final stack:** core, awareness-only, deferred;
- **Proof vehicle:** exact source, boundary, and reason;
- **Dated July 17–26 sequence:** one primary outcome per day;
- **Daily learning gate:** what Chris must explain or do independently;
- **July 25 acceptance test:** observable pass/fail evidence;
- **July 26 transition checklist:** D2L/syllabi/tracker/school activation;
- **Files to update after approval:** `NOW.md`, CASTLE log/status, owning project
  record, and today's DAILY—no structural page unless Chris separately approves it.

## Claude Independent Review — July 17, 2026 (Operator hat)

Reviewed against `NORTH_STAR.md`, `CURRENT_STRATEGY.md`, `NOW.md`,
`00-BRAIN\CASTLE\wiki\current-position.md`, `PRE-SEMESTER_PREP_PLAN.md`, the
PYTHON/PHYSICS `current-position.md` pages, `...projectSuccess\radar.md` (the
MCP row directly), and this hub's own MCP wiki pages
([[mcp-landscape-architecture-and-patterns]],
[[mcp-security-and-authorization]],
[[mcp-client-primitives-and-build-notes]]). One live fetch confirmed the
`blog.modelcontextprotocol.io` RC post Codex cited — verifying the date claim
also surfaced a spec detail the proposal didn't have, folded in below.

### Verdict: **Approve, with one required correction and four bounded modifications.**

The stack architecture, learning-speed contract, and July 28 deferral
boundary are sound and evidence-grounded. It needs one factual correction
against the radar record before it's on-record, plus tighter time-boxing so
"MCP capstone" stays true in practice, not just in prose.

### Critical correction — the radar row's own gate, not yet closed

`radar.md`'s MCP row (2026-07-16) states the build consequence explicitly:
*"No build from this row: after the July 28 spec finalizes, CASTLE decides
whether one bounded MCP rep... is worth ≤90 min."* Two things follow:

1. **The row anticipated a ≤90-minute bounded rep, not an 8-day sprint.**
   The proposal is not actually in conflict with this — MCP is correctly
   scoped as the *capstone*, not the sprint's subject — but the current
   document never states how many actual hours go to the MCP build itself
   versus general Python/SQL/Git/CI fundamentals (which were already
   independently authorized by the July 16 heavy-tech-stack rebalance in
   `NOW.md` and need no Watchtower gate at all). Without an explicit hour
   cap, "capstone" can silently become "curriculum" by July 22. **Fix:**
   state the MCP-specific budget as ≤3 hours total across 2 sessions near
   the end of the window — close enough to the radar's own ≤90-min framing
   to count as satisfying it twice over, not stretched across 8 days.
2. **The CASTLE gate fired July 17 — before July 28 spec finalization**,
   while the radar row's stated trigger was "after the July 28 spec
   finalizes... CASTLE decides." Read literally, the gate ran early. This
   is defensible in substance (the proposal correctly scopes to durable
   pre-RC-lock fundamentals and explicitly defers everything the RC is
   still moving on), but the radar board itself has not been updated to
   reflect that CASTLE already exercised its half of that trigger — the row
   still reads WATCHING with an open "no build" condition. **This is a
   record-keeping gap the original file list missed: `radar.md` needs its
   own row update** (status → `✅ GATED/TESTING`, CASTLE gate/outcome column
   filled, next-review date reset) alongside `NOW.md`/CASTLE log/DAILY, or
   the Watchtower board goes stale the way `AGENT.md`'s Review Cadence
   section names as a drift symptom.

### New technical finding from live verification (folds into scope, not a blocker)

The fetched RC post confirms May 21 lock / July 28 final publication as
stated, but also documents that the RC formally **deprecates Roots,
Sampling, and Logging as protocol capabilities** (12-month sunset) and
**removes the `initialize`/`initialized` handshake and `Mcp-Session-Id`
entirely** in favor of a stateless model. None of this breaks the sprint —
the proof standard already avoids Roots as a security boundary (correctly,
per the existing wiki page) and doesn't touch Sampling — but it does mean:

- **Day 1 must record the exact installed SDK/`fastmcp` version** and
  confirm whether it targets the outgoing stateful `2025-11-25` spec or the
  new stateless RC before any handshake-dependent code is written. Building
  fundamentals against a spec mid-transition is fine; building them without
  knowing which side of the transition you're on is not.
- Protocol-level **Logging** (server-to-client log notifications) is
  deprecated — this is unrelated to the proof standard's stderr/file
  logging hygiene (a server-side implementation practice, not the MCP
  Logging capability), so no change needed there, but don't teach the
  protocol Logging capability as a durable primitive.

### Final stack

**Core (build it):** Python fundamentals in service of the fixture below →
SQLite (fixture DB, not the scanner) → typed/validated function boundaries →
pytest → official MCP Python SDK, local stdio only → MCP Inspector → one
real host connection → stderr/file tool-call logging → Git/GitHub commit
discipline → a one-page operator/security handoff.

**Awareness-only (map it, ≤20 min/day, table entries not deep dives):**
Google Forms/Sheets/Looker Studio, Zapier/Make/n8n, generic REST/webhooks,
Flask as a concept, governed-AI-feature vocabulary. Each entry: problem
solved, cheapest prior rung, maintenance owner, risk — exactly as the
proposal already specifies; just cap the daily time.

**Deferred (explicitly, past this sprint):** remote MCP deployment, OAuth/
enterprise authorization, MCP Apps and RC extensions, a custom MCP *client*
(the Inspector plus one host connection already satisfies "client-side
proof" — building a second full component adds scope with no incremental
learning value at this stage), any claim of client-readiness, YouTube/
scanner API work, dashboard iteration, new business-lane exploration.

### Proof vehicle: REVISED — extracted from Chris's own field notes, not a synthetic fixture, not the scanner

**Superseded July 17 (evening) after Chris clarified "simulation intake off
my memory."** He was recalling a real, already-documented construction
workflow — not proposing new weekend fieldwork (correctly ruled out: family
capacity does not support a live observation this window). Two files
already exist in `05-BUSINESS\02-Field Notes\`:

- `observation_one.md` (July 14, 2026) — a first-call → estimate → approval →
  payment workflow, with a structured Amendment Follow-up Questions section
  (first-call capture, where it's recorded, turnaround time, who approves
  pricing, what breaks estimates, how change orders get documented, how
  often payment is late/short) **and an already-scaffolded, currently-empty
  `OBSERVATION LOG` table** (`# | Date | Business Type | Core Problem |
  Follow Up?`).
- `FIELDNOTES_JUNE5_CONSTRUCTION_TECH.md` — broader friction inventory
  (field productivity visibility, change-order lag, material tracking,
  untracked time corrupting estimates) — secondary source, richer
  vocabulary if the primary table needs more columns.

**Final proof vehicle: build the MCP server's fixture SQLite DB by
structuring `observation_one.md`'s real content into 2-3 tables** — e.g.
`jobs` (call date, scope description, estimate turnaround days, approval
method, payment status/delay) and `friction_log` (category, description,
source note) — then fill the note's own blank `OBSERVATION LOG` table as
part of that work. The MCP server's one resource + two read-only tools then
query this real (if small and general-pattern, not client-identifying)
dataset.

This beats both prior options: no scanner-boundary risk at all, no
invented data, it's real Python/SQL practice against Chris's own domain
knowledge, it fills in a field note he already started and left blank, and
the harvested schema becomes a genuine template shape for a future real
audit intake — directly serving `CURRENT_STRATEGY.md` S-01/S-02 evidence
questions (pricing standardization, estimate-to-payment friction) rather
than a throwaway exercise. Structuring it is itself Day 1-2 work, done live
— see Working Method below.

### Working Method — added July 17 evening, per Chris, binding for the whole sprint

Chris's own words: *"I don't want either of you to just be doing these
things while I watch — we need to work through the understandings of why
we need what as we go, even if it is just a couple words or sentences on a
certain term."*

This is a standing rule, not a preference, for every session in this
sprint (Codex and Claude both):

- **No silent batch-building.** Neither AI writes the fixture, the server,
  the tools, or the tests unsupervised and then presents a finished result.
  Chris types/decides the substantive steps; AI explains, scaffolds, and
  reviews alongside him.
- **Every new term or decision gets a short live explanation before or as
  it's used** — a couple of sentences is enough (what it means, why this
  step needs it), not a lecture. This is the existing Learning-Speed
  Contract's steps 1-2 (plain-language meaning, physical/real anchor),
  just made mandatory-live rather than optional-if-time.
- **Mechanical infrastructure is the one exception**: folder scaffolding,
  git init, dependency files, empty test stubs — reversible, non-teaching
  setup — may be prepared ahead of a session so the paired time goes to
  the actual concepts, not typing boilerplate. Nothing that represents a
  build decision or a new concept goes in that bucket.
- Also confirmed by Chris this same exchange: **Python fundamentals do not
  need dedicated isolated days** — "python I am good with for now... if it
  gets advanced I can ask, that is why I have you all." Fold Python/SQL
  practice directly into building the real fixture and server starting
  Day 1-2, rather than front-loading abstract fundamentals drills. Ask-when-
  stuck replaces teach-everything-first for anything already solid.

### Dated July 17–26 sequence (one primary outcome per day) — REVISED same evening

| Date | Primary outcome |
|---|---|
| Fri Jul 17 (rest of day) | Infrastructure only (no pairing needed): confirm installed MCP SDK version + spec side; scaffold `02-LIBRARY\.PROJECTS\mcp-bootcamp\`, git init, pytest stub; lock this plan |
| Sat Jul 18 | **Live, paired.** Read `observation_one.md` together; design the `jobs`/`friction_log` table shape from its real content (why these columns, from which answer); Chris writes the `CREATE TABLE` + insert statements |
| Sun Jul 19 | **Live, paired.** Fill the note's own blank `OBSERVATION LOG` table using the structured data now in SQLite; first pytest checks against the fixture *(metadata-regression recurrence review also lands today per `NOW.md` — unrelated, low-effort, does not displace this)* |
| Mon Jul 20 | **Live, paired.** Define the 1 resource + 2 read-only tools as typed function signatures against the fixture — no SDK yet, just the contract and why each boundary is read-only; short app-network mapping entries |
| Tue Jul 21 | **Live, paired.** MCP server build session 1 (of the ≤3-hr budget): wire the SDK to the already-designed tools, stdio, stderr logging — explain each SDK concept as it's used *(OPP-20260714-01 B2 review lands today — Chris's call, not sprint-displacing)* |
| Wed Jul 22 | **Live, paired.** Finish server; full pytest coverage (normal/edge/invalid/prohibited) — Chris writes the prohibited/edge cases himself, since those are the ones that teach the boundary; Inspector verification |
| Thu Jul 23 | **Live, paired.** MCP server build session 2: one real host connection; write the operator/security handoff together *(flip-margin replay OPP-20260716-01, if it fires today, outranks this per North Star priority #3 — see Displacement Rules addition below)* |
| Fri Jul 24 | Buffer/consolidation only — close any gap from Tue/Wed/Thu, cold explain-back rehearsal; do not start new material |
| Sat Jul 25 | July 25 acceptance test (below); harvest write-up; scope does not extend into Jul 26 under any circumstance |
| Sun Jul 26 | Hard transition — D2L intake begins, per Time Box (unchanged) |

Every "Live, paired" day follows the Working Method above — no session
produces a finished artifact Chris hasn't typed, decided, or explained back
piece by piece.

Every day still opens with the one protected school-proof block (Python
Stage 3 close-out, then Physics Stage 4) before sprint work, per the
existing Time Box — unchanged from the proposal.

### Daily learning gate

Apply the proposal's existing 8-step Learning-Speed Contract per concept
block, not forced per calendar day (a day that's mostly fundamentals
practice may only complete steps 1-4; a day that closes a build session
should reach 5-8). Non-negotiable per session regardless of pace: **step
5 (explain-back: what sits where, what flows, and why)** — this is the one
step that catches "AI generated it, Chris didn't internalize it," which is
the proposal's own stated risk.

### July 25 acceptance test — observable pass/fail

**Pass requires all of:**
- Local MCP server (stdio) exposing exactly 1 resource + 2 read-only tools
  against the purpose-built fixture, typed/validated inputs, structured
  outputs and error responses.
- pytest suite green: normal, edge, invalid, and prohibited-operation cases.
- Verified working through MCP Inspector.
- One successful connection from a real MCP host.
- Tool-call logging to stderr/file only (verified stdout is never touched).
- One-page written operator/security handoff: what's exposed, what's
  explicitly not, the least-privilege boundary, known risks.
- Chris cold-explains the full flow (host → client → server → tool →
  result) without notes, and separately explains why this proves a
  **technical capability, not client readiness or demand** — the
  proposal's own line, restated back correctly.

**Honest floor if time runs short:** the date does not move. If by end of
Thu Jul 23 the server/tests/Inspector triad isn't solid, cut the
host-connection step and/or the written handoff before cutting into Jul 26
— scope flexes down, the July 26 D2L boundary does not.

**Explicitly not proof of:** client demand, willingness to pay, or
readiness to deploy anything real. Record the harvest as "MCP fundamentals
capability + a reusable fixture-audit-table pattern," not as Advisor-Builder
market evidence — keeps `CURRENT_STRATEGY.md`'s assumption ledger honest.

### July 26 transition checklist (unchanged from `PRE-SEMESTER_PREP_PLAN.md`, restated for continuity)

- D2L document intake for all six Fall courses.
- Syllabus and AI-policy re-verification against current official sources
  (ENGR 1000's Fall 2025-vs-2026 gap and TCOM's date/weights issues are
  already flagged open in `SYSTEM_FLAGS.md` #57 — this is where that flag
  closes).
- Academic Tracker populated with real course data — the sprint's Python/
  SQL reps are direct preparation for this, not a detour from it.
- Physics Stage 4 / Python Stage 3+ progress carries forward exactly as-is;
  the sprint does not touch either stage's proof.

### Displacement Rules — one addition

Add to the existing Stop Rules: **an approved real workflow-observation
opportunity (e.g., the Jul 23 flip-margin replay, OPP-20260716-01, if
Chris's approval and access land during the window) immediately outranks
sprint technology practice for that session** — this follows directly from
`NORTH_STAR.md`'s priority order ("urgent client and revenue evidence
outranks routine queue work") and is real Advisor-Builder proof in a way
the MCP build explicitly is not. The original Stop Rules list didn't
carve this out; it should.

### Open Decision #5 — resolved

**Yes, a named project: `02-LIBRARY\.PROJECTS\mcp-bootcamp\`**, per
`WHERE_IT_GOES.md`'s "has a deliverable, build, or launch goal" rule. Docs\
holds a pointer to this review file as the live plan (not a duplicate);
Code\ holds small scripts per the Format Rules exception. Real project code
conventionally lives "local + GitHub," but creating a new GitHub remote is
a visible/consequential action this report does not authorize on its own —
local git only for now. If the proof earns continuation past July 25, a
GitHub home is a one-line ask, not a structural decision.

### Files to update after approval (corrects/extends the original list)

`NOW.md` (also: its header date is stale — "Thursday, July 16" while today
is Friday the 17th; fix on the same edit), CASTLE log/status,
**`...projectSuccess\radar.md`'s MCP row** (added — see Critical Correction
above), **the new `02-LIBRARY\.PROJECTS\mcp-bootcamp\` project record**
(added), and today's `DAILY_2026-07-17.md`. No structural page changes
beyond these, per the original request.

## Second Revision — July 17, 2026 (late evening): Codex's lens structure restored, fused with the locked discipline

Chris asked for one more honest look at Codex's very first draft
(`claudereadcodexplan.md`, a root-level "Chris's Eight-Day Advisor-Builder
Technology Boot Camp" file that this packet's earlier text treated as
superseded), checked against `NORTH_STAR.md` and Chris's YouScience
`Christopher_Aptitude_Results.pdf` strengths profile — not against style
preference.

**Verdict: Codex's shape was right; only its specifics were wrong.** A
build track compressed into one narrow technology (MCP) is a specialist
week. Chris's profile is Extrovert + Generalist + Future Focuser (wants one
continuous case, wide-lens, always visible against the long horizon) + 3D
Visualizer (wants a blueprint that accumulates in layers he can see) +
Process Supporter (needs the full skeleton in place before starting, not a
single day-by-day build-step list). Codex's original eight engineering
lenses, one continuous construction case, accumulating master blueprint,
and reusable Standard Artifact Contracts fit that profile better than the
MCP-only build sequence this packet had locked. Codex's Recommendation
Ladder and Displacement/Stop Rules concepts had already migrated into this
packet independently — the two drafts were never as opposed as the first
read treated them.

**What does NOT change — Chris's own explicit decisions, not style, still
binding:**
- Proof vehicle is `observation_one.md`'s real content, never invented data
  and never the scanner.
- MCP is scoped as the Automation/AI lens's capstone, ≤3 hours total build
  budget — a lens within the week, not the subject of the week.
- The Working Method (live pairing; no session produces a finished artifact
  Chris didn't type/decide/explain-back live) governs every session,
  unchanged.
- July 26 is still the hard, non-flexing D2L transition boundary; the daily
  protected school-proof block is unchanged; the Displacement/Stop Rules,
  including the flip-margin-replay carve-out, are unchanged.

**Fused day-by-day sequence — replaces the prior Sat–Sat build-step table.**
Each day is now one of Codex's eight lenses, mapped onto the Advisor-Builder
loop from `CURRENT_STRATEGY.md`/`NORTH_STAR.md`
(Observe → Diagnose → Engineer → Deploy → Train and Retain → Harvest), built
on the same real data throughout:

| Date | Lens | Loop stage | Real-data build | Daily gate |
|---|---|---|---|---|
| Sat 7/18 | Systems Audit | Observe | Swimlane + systems inventory + data-flow map, built from `observation_one.md` | Distinguish symptom / waste / root-cause hypothesis / constraint in the real note |
| Sun 7/19 | Strategic Logic | Diagnose (why) | Fill the note's own blank OBSERVATION LOG table; problem statement (goal → condition → constraint → consequence → evidence needed) | Reject a tempting technology the business case doesn't justify — test it against `CURRENT_STRATEGY.md` assumptions S-01/S-02 |
| Mon 7/20 | Data Engineering | Diagnose (evidence) | Structure the note into `jobs`/`friction_log` SQLite tables (primary). Secondary, clearly separate: retrieve BLS series WPUIP2311001 as a labeled external-market-context ETL exercise — official public data, never blended with or presented as client evidence | Trace one conclusion source → transform → query → finding, on both datasets, without losing provenance |
| Tue 7/21 | Automation & Operations | Engineer (nervous system) | Define the 1 resource + 2 read-only tool contracts as typed function signatures against the fixture — no SDK yet | Explain where state lives, what happens on failure, who owns recovery |
| Wed 7/22 | AI Infrastructure | Engineer (judgment layer) | Wire the MCP SDK to the Day-4 contract: stdio, stderr logging, full pytest coverage, Inspector verification — MCP-specific time counts against the ≤3 hr budget starting here | Why AI/MCP is necessary here, what it may access, how a human catches failure |
| Thu 7/23 | Cybersecurity & Governance | Protect what's deployed | One real host connection; threat model the Day 4–5 system; access-control matrix; operator/security handoff written together. *(Flip-margin replay OPP-20260716-01 outranks this session if it fires — unchanged rule.)* | Explain how the system prevents, detects, contains, and recovers from misuse |
| Fri 7/24 | Product & Value | Train, Retain, quantify | Minimum Viable Transformation framing; conservative cost/benefit/payback against S-01/S-02; pilot success/stop criteria; 30/60/90-day roadmap; cold explain-back rehearsal | Defend why this is the smallest justified response and name the evidence that would stop it |
| Sat 7/25 | Integration | Harvest + present | Assemble all seven layers into the one master blueprint; simulated owner discovery + 15–20 min findings presentation; independent AI challenge; keep/revise/reject verdict | Unchanged July 25 acceptance test below, now inside the full lens frame instead of a standalone checklist |
| Sun 7/26 | — | — | Hard transition — D2L intake begins. Unchanged. | — |

The July 25 acceptance test (pass conditions, honest floor, what it does
and does not prove) is unchanged from the section above — Day 8 now
delivers it inside the owner-presentation format instead of as a bare
checklist.

**New stipulation from Chris, this session — does not change the sprint's
design, changes what gets recorded alongside it:** do not design the sprint
to make `.ROOT` inspect or upgrade itself to adopt this teaching format —
that would add meta-scope to an already time-boxed week and risks
`NORTH_STAR.md`'s own named risk, "planning can imitate progress." Instead,
keep a running, lightweight development-notes track across all eight days —
separate from the content harvest — recording what worked and didn't in the
fast-paced multi-lens format itself (the daily rhythm, the artifact
contracts, the lens sequencing), so reusable pieces can be named honestly
once it's clear what they're actually for, not designed in on faith. Chris
is keeping his own notes in parallel. If the format proves itself by July
25, promoting it to a standing `.ROOT` skill is a Day-8-or-later proposal
decided with real evidence, following `AGENT.md`'s AI-initiated
system-evolution path (log friction/success → gather repeated evidence →
draft proposal → Chris approval) — not decided now. Running log:
`02-LIBRARY\.PROJECTS\MCP_Bootcamp\Docs\learning-format-notes.md`.

**Standard Artifact Contracts restored** (from Codex's original draft, not
carried into the first locked version) — Evidence, Workflow step, System,
Finding, Recommendation, Automation event, AI evaluation, Control. These
are the reusable field templates that accumulate into the Day 8 master
blueprint; use them across all eight lenses, not just the build days.

`claudereadcodexplan.md` (the root-level stray copy of Codex's original
draft) is archived to `99-ARCHIVE\` this session — its content is now fully
incorporated above; the loose root copy was never filed per
`WHERE_IT_GOES.md` and is no longer the live version of anything.

## Current State

- **Current state:** Plan is now the fused version above — Codex's
  eight-lens structure carrying the locked plan's discipline (real
  field-note data, MCP scoped as a ≤3 hr capstone inside the AI lens,
  mandatory live-pairing Working Method, July 26 hard boundary). A separate
  format-effectiveness notes track is added, explicitly not baked into the
  curriculum as a goal. Chris confirmed go on all of it.
- **Open question:** none. Proceeding to the record pass across `NOW.md`,
  CASTLE log, DAILY, and the project's `Docs\learning-format-notes.md`.
- **Next exact action:** first live-paired session, Sat Jul 18 — Systems
  Audit lens, build the current-state swimlane/systems-inventory/data-flow
  map directly from `observation_one.md`.
- **Details likely to be forgotten:** July 26 is a hard boundary that does
  not flex even if the build runs long — cut scope, not the date; the
  MCP-specific build budget is ≤3 hours total, inside Wed 7/22, not spread
  across all 8 days; the fixture is `observation_one.md`'s real content,
  structured — never the scanner, never invented data; BLS data is a
  separate, secondary, clearly-labeled exercise, never blended with client
  evidence; the flip-margin replay (if it fires) outranks the sprint for
  that session; **no session in this sprint produces a finished artifact
  Chris didn't type/decide/explain-back live** — a hard rule, not a style
  preference; whether this teaching format becomes a standing `.ROOT`
  capability is an evidence-gated Day-8-or-later question, not a goal of
  the sprint itself.

---
*Prepared by Codex for Claude edit and independent review — July 17, 2026.*
*Claude independent review appended same day — Operator hat, per Chris's request.*
*Second revision (Codex-lens fusion + format-notes stipulation) appended same evening, per Chris's direction.*
