---
type: report
timeline: next
status: proposed
revised: 2026-08-02
tags: [system-review, efficiency, castle]
---

# Weekly System Improvement Recommendations — August 2, 2026

## Recommendation

Run one seven-day operating pilot aimed at **at least a 15% increase in completed scheduled school blocks, with 20% as the stretch threshold**, without increasing control-work blocks. Do not redesign `.ROOT`, add a dashboard, or open another architecture program.

The concrete throughput target is **15–16 completed core school blocks**, up from this week's 13 evidenced weekday blocks. At least **10 must produce independent evidence**—a cold build, solved problem, quiz, debug, explain-back, or usable workflow result—rather than reading alone. Plan **18 core blocks** so 16 completed blocks equals 89% core completion, then add separately labeled stretch blocks that do not turn into false failures when capacity is unavailable. Chris's declared availability and fixed commitments may reduce the core before the plan is approved; the system does not infer capacity from calendar space.

## Higher-Model Design Review

The first draft had three design defects, corrected in this revision:

1. **“Control-plane touches” was not measurable enough.** A two-minute cockpit refresh and a two-hour repair counted equally. The revised pilot uses the existing 50-minute block as the common unit and records only block-equivalents.
2. **“One full load per day” conflicted with governance.** Every fresh AI session still completes the required boot chain. The efficiency move is fewer fragmented sessions and handoffs, not weaker loading.
3. **One disrupted week was at risk of becoming a capacity ceiling.** The 13-block result is a throughput baseline under observed disruption, not Chris's permanent sustainable capacity. The 18-core-block plan is a one-week test with stretch capacity, not a lowered ambition rule.

## Why this wins now

The vault can already orient, teach, gate, log, validate, and preserve evidence. This week it completed about 41% of its planned weekday school blocks while producing extensive system work. The bottleneck is conversion, not missing capability.

The recurring failure chain was:

```text
owner proof changes
    -> dashboard/plan does not fully update
    -> next session reloads and reconciles
    -> another report or repair is produced
    -> planned proof loses time
```

## Seven-Day Pilot

### 1. Protected first proof

Begin each active day with one named learner or real-workflow artifact. Optional system work waits until it closes. A HIGH blocker, fixed commitment, or Chris's direct redirect may interrupt it; record the displacement once without treating Chris's choice as system failure.

### 2. Reduce session fragmentation without weakening the boot chain

Every fresh AI session completes the universal boot chain. Efficiency comes from using one lead surface for the active proof, avoiding parallel work on the same boundary, and writing a handoff only when continuity genuinely requires another session. Within one continuing session, reload only owner state that materially changed.

At close: update owner truth first, append one concise DAILY packet, then refresh the cockpit once if the actionable frontier changed. Do not write successive summaries of the same state.

### 3. Frontier propagation as an acceptance check

When a stage or gate closes, the same close is incomplete until:

- the owner current-position states the new frontier;
- `NOW.md` or `MORNING_BRIEF.md` exposes that frontier;
- the prior next action is no longer presented as live.

This is the recommended resolution pattern for flag #91. It should be implemented as a small interface rule after Chris approves the exact wording, not as a new dashboard.

### 4. Core, stretch, and a Wednesday reforecast

Start with **18 core school/value blocks** and separately labeled stretch blocks. The recommended default mix, subject to Chris's capacity approval, is:

| Lane | Core blocks | Required evidence |
|---|---:|---|
| Python / CSE lecture | 5 | Stage 4b survey plus at least two independent construction or trace checks |
| CSE Lab preparation | 2 | Two fresh lab-condition reps; no submitted course work |
| Physics / calculus bridge | 6 | Two carried-over validations plus calculus-connection work |
| TCOM | 2 | Reading plus one closed-source structure or audience explain-back |
| ECON | 2 | Reading plus one retrieval/application check, not reading only |
| Technology/business | 1 | One bounded workflow result with a named decision/user |
| **Total** | **18** | **At least 10 independent evidence-producing blocks overall** |

ENGR remains source-gated until its real Fall syllabus exists. Stretch opens only after core pace is intact. This week's 13 completions are a baseline, not a ceiling.

At Wednesday close, forecast the week from actual core completions and known remaining capacity:

- **Green:** at least 10 of 18 core blocks closed — continue.
- **Yellow:** 8–9 closed — remove stretch and protect the top three remaining proofs.
- **Red:** 7 or fewer closed — Chris and the AI explicitly re-scope the core rather than silently carrying an impossible plan to Sunday.

The reforecast changes the plan openly; it does not rewrite completed history or manufacture an 85% score by shrinking the denominator after the fact.

### 5. Bounded maintenance window

During Monday–Saturday, only HIGH health/integrity failures interrupt the protected first proof. MEDIUM and LOW flags, broad source intake, architecture review, and tool exploration wait for Sunday unless Chris redirects. A HIGH issue gets one bounded diagnosis/repair block before re-evaluation; it does not automatically consume the rest of the day.

## Measurements

Use the existing weekly plan and DAILY; create no tracker. Classify actual worked time in the same 50-minute units already used by the simulation:

- completed core blocks;
- completed stretch blocks;
- evidence-producing blocks versus reading/orientation blocks;
- control-work block-equivalents: loading/reconciliation, dashboard/report work, maintenance, configuration, or repair that consumes at least half a block;
- core proof blocks displaced by control work;
- stale or false `closed`, `fixed`, `committed`, `pushed`, or `verified` claims;
- frontier changes that reached the cockpit in the same close.

Incidental updates performed inside a proof block are not counted again as separate control work. A control task under 25 minutes is incidental; 25–49 minutes counts as half a block; each 50-minute unit counts as one. This prevents the metric from rewarding or punishing how finely a session is logged.

## Acceptance on August 9

Keep the pilot if all are true:

- at least 15 of 18 core blocks close; because blocks are discrete, 16 completions meets and slightly exceeds the 20% throughput-improvement threshold over the 13-block baseline;
- at least 10 completed blocks contain independent evidence, not reading/orientation alone;
- Monday–Saturday control work consumes no more than five block-equivalents and displaces no more than one core block;
- zero optional system work displaces the day's first proof;
- zero unsupported completion claims survive the same session;
- every stage/frontier change reaches the cockpit at close;
- one bounded workflow result has a named user/decision and either produces usable evidence or fails with a classified reason. External contact still requires Chris's approval.

Modify or reject the pilot if it adds recording burden without reducing reconciliation or displacement.

## Ranked Repair Backlog

1. **Health blockers, before the next system checkpoint:** decide the allowed home for Claude `skillOverrides`; repair the escaped Physics crash-course Markdown/frontmatter after inspecting and preserving its content. Do not let either consume Monday's first learner proof unless it actually blocks that proof.
2. **Flag #91, high leverage:** approve and implement same-close frontier propagation plus the pre-semester survey-mode wording through August 23.
3. **Weekly-plan evidence:** close or supersede the stale July 27–August 2 evidence table; future plans get one end-of-day count update, not multiple partial rewrites.
4. **Inbox:** route the four current items during Sunday maintenance only; reject duplicates and tool-content that does not serve a live gap.
5. **Sandbox:** #90 is retired by Chris. Use the functioning approved-escalation path; do not spend learner blocks investigating it unless access stops work or Chris reopens the issue.

## Risks and boundaries

- The 18-block core is a seven-day experimental commitment, not a permanent capacity judgment. Increase it after evidence, not optimism; decrease it only before approval or through the visible Wednesday reforecast.
- Survey mode before August 24 must still include one light independent check; exposure alone is not evidence.
- Do not treat the internal proof-to-control audit as a client case study until a measurable outcome exists and sensitive details are sanitized.
- Do not modify Claude tool configuration, raw evidence, or governance solely from this recommendation; each retains its normal approval boundary.

## Exact next action

Build the August 3–9 CASTLE weekly plan with the **18-block lane-balanced core** above, explicit stretch, the Wednesday **10/8/7** reforecast gate, and block-equivalent control measurement. Start Monday with the smallest carried-over learner proof before optional system maintenance.

## August 2 Decision Addendum — Accepted With a Material Allocation Revision

After recovering and comparing the interrupted Claude and Codex planning
conversations, Chris approved the 18-block pilot and Wednesday reforecast but
redirected the material mix to the two actual A-grade risks:

- 8 Physics/calculus bridge blocks;
- 8 Python/CSE blocks, including later-topic survey exposure without false
  stage advancement;
- 1 TCOM orientation block; and
- 1 ECON orientation block.

ENGR remains source-gated and optional technology/business work does not displace
this week's core. The live execution authority is
`00-BRAIN\CASTLE\wiki\weekly-plans\weekly-plan-2026-08-03-to-2026-08-09.md`.
The pilot measurements and 10/8/7 reforecast are unchanged.

---
*Status: proposed for the August 3–9 weekly plan; review on August 9, 2026.*
