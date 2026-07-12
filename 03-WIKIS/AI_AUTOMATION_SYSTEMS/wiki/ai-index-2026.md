---
type: research
tags: [ai-automation, adoption-evidence, benchmarks, governance, landscape, audit-vocabulary]
source: 03-WIKIS\TECHNOLOGY\raw\ai_index_report_2026.pdf (Stanford HAI AI Index 2026, 9th ed., pub. April 2026, 425 pp., arXiv:2606.15708; also pre-split chunks in same raw/) — ingested 2026-07-09 at the report's own summary layer: Top Takeaways + all nine Chapter Highlights read in full; chapter bodies classified for lookup. Raw stays in TECHNOLOGY per file location; research routed HERE per the July 9 AI-lane closure.
---

# Stanford AI Index 2026 — The Measurement-Gap Edition

The ninth AI Index (Stanford HAI, April 2026 — the most neutral, most-cited
annual dataset in the field; CC-licensed with public raw data). The
co-chairs' own frame is this wiki's thesis verbatim: *"a field that is
scaling faster than the systems around it can adapt"* — governance,
evaluation, education, and measurement all trailing capability. Fifteen Top
Takeaways plus nine chapters; the numbers below carry "(as of the report's
data, 2025–early 2026)" implicitly — recency-mark anything quoted onward.

## Capability and Its Measurement (Ch. 1–2)

- Industry produced **>90% of notable frontier models**; the most capable
  are now the **least transparent** (no training code, parameters, data
  disclosures from OpenAI/Anthropic/Google). Foundation Model Transparency
  Index *fell* 58 → 40 in 2025.
- **Frontier convergence:** four companies within 25 Elo points (Anthropic
  1,503 · xAI 1,495 · Google 1,494 · OpenAI 1,481, as of 2026-03) —
  competition shifts to **cost, reliability, and domain performance**. The
  US–China gap is effectively closed (2.7%); open-weight trails closed by
  3.3%.
- **Benchmarks are breaking as instruments:** Humanity's Last Exam jumped
  30 points in a year; evaluations meant to last years saturate in months;
  invalid-question rates run 2%–42% on widely used benchmarks; leaderboard
  standing may partly reflect platform adaptation. Independent testing
  doesn't always confirm developer claims.
- **The jagged frontier, quantified:** IMO gold medal (Gemini Deep Think,
  35 pts) vs. 50.6% at reading analog clocks. Professional-domain evals
  (tax, mortgage, corporate finance, law) run 60–90% — capable, not
  reliable. **Agents leapt 12% → ~66% on OSWorld** (real computer tasks)
  but still fail ~1 in 3 attempts. Robots: 89.4% in simulation, **12% on
  household tasks**.
- Infrastructure: global compute growing 3.3×/year (17.1M H100-equivalents,
  Nvidia >60%); US hosts 5,427 data centers (>10× any country); **almost
  every leading AI chip comes from one foundry (TSMC)**; AI datacenter
  power = 29.6 GW (~New York state at peak). US inbound AI-talent migration
  **down 89% since 2017** (−80% in the last year).

## Responsible AI (Ch. 3) — feeds the vetting screen

- **Documented incidents rose 362 vs. 233 in 2024** (AI Incident Database —
  the same failure-evidence stream as [[oecd-ai-incidents-monitor]]).
- Capability benchmarks get reported by nearly all frontier labs;
  **responsible-AI benchmarks stay spotty** — the WTI/Codex
  verification-capacity story at the measurement layer.
- **Belief-vs-fact failure:** hallucination rates across 26 top models run
  22–94%; models handle "X believes [false thing]" fine in third person and
  **collapse when the user asserts it** (GPT-4o 98.2% → 64.4%) — directly
  relevant to any client-facing assistant that will be told wrong things
  confidently.
- Org practice is formalizing: businesses with *no* RAI policies fell
  24% → 11%; AI-governance roles +17%. Cited frameworks: GDPR 60%,
  **ISO/IEC 42001 36%, NIST AI RMF 33%** ([[nist-ai-rmf]] is now a named
  market signal, not just theory). Barriers: knowledge gaps 59%, budget
  48%, regulatory uncertainty 41%.
- Safety scores look good under normal use and **degrade under jailbreak
  across all models tested**; improving one RAI dimension (safety) can
  measurably degrade another (accuracy) — tradeoffs are real and poorly
  understood.

## Economy (Ch. 4) — the adoption arc, third source

Extends the [[work-trend-index-2024-2026]] arc with independent numbers:

- **Fastest mass adoption in tech history:** generative AI hit **53%
  population adoption in three years** (faster than PC or internet) — but
  the **US ranks 24th at 28.3%**, well behind Singapore 61% / UAE 64%.
- **Organizational adoption 88%**; GenAI in ≥1 business function at 70%;
  **agent deployment single-digit across nearly all functions** — the same
  agents-gap Deloitte/McKinsey found (74% plan, 21% governed).
- Investment: global corporate AI investment **more than doubled in 2025**;
  US private investment **$285.9B** (23× China's private figure); 1,953
  newly funded US AI companies; consumer surplus est. **$172B/yr** (+54%).
- **Productivity gains are real and lopsided:** 14–15% customer support,
  26% software development, 50% marketing output — largest in structured,
  measurable work; weak or negative where judgment dominates; early
  evidence that heavy reliance may slow skill development.
- **The labor signal:** employment for US software developers **ages 22–25
  fell ~20% from 2024** while older cohorts grew; one-third of orgs expect
  workforce reductions within a year (service ops, supply chain, software
  engineering highest). Anticipated cuts exceed observed ones everywhere.

## The Rest, In One Paragraph Each

- **Science (Ch. 5):** AI-for-science publications +26%; frontier models
  beat average human chemists on ChemBench yet score <20% on replicating
  actual papers — capability vs. verification again. Small specialized
  models beat giants (111M-param MSAPairformer; 200M GPN-Star over a
  40B model): scale is not destiny in vertical domains.
- **Medicine (Ch. 6):** ambient AI scribes scaled across health systems
  (up to 83% less note-writing time, less burnout) — but ~half of 500+
  clinical AI studies used exam-style questions, only **5% real clinical
  data**. Deployment ahead of evidence.
- **Education (Ch. 7):** 80%+ of US students use AI for schoolwork; only
  half of schools have AI policies, 6% of teachers call them clear. CS
  enrollment −11%; AI-related master's +17%. (Detail routed to
  EDUCATION → `ai-programs-us-2026.md`.)
- **Policy (Ch. 8):** divergence, not convergence — EU AI Act prohibitions
  in force, US deregulating, Japan/South Korea/Italy passed national laws;
  **AI sovereignty** is the new organizing principle, and most new national
  strategies now come from developing economies. US public AI investment
  ($20.4B over 2013–24) is a rounding error against private ($285.9B in
  2025 alone).
- **Public opinion (Ch. 9):** optimism 59% *and* nervousness 52%, both
  rising; **50-point expert–public gap** on AI's job impact (73% vs 23%
  positive); US has the *lowest* trust of any surveyed country in its own
  government to regulate AI (31%).

## Why This Matters for This Wiki / `.ROOT`

1. **The measurement gap is the report's spine — and this system's.** The
   AI Index's central finding (evaluation, governance, and education
   trailing capability) is the fourth independent confirmation of the
   verification-capacity verdict, and the first stated at ecosystem scale
   with neutral data. Benchmarks saturating + labs disclosing less =
   *independent verification becomes the scarce good* — which is what the
   vetting screen, the lint pass, and the audit business each sell at
   their own scale.
2. **Tier-1 citation ammunition.** For client conversations: 88% org
   adoption vs single-digit agents; US 24th in consumer adoption;
   productivity gains concentrated in structured work; incidents +55%
   YoY; ISO 42001/NIST RMF as rising named standards. All citable to
   Stanford, not a vendor.
3. **Frontier convergence favors the integrator.** When four labs sit
   within 25 Elo points, model choice stops being the decision that
   matters — cost, reliability, integration, and governance become the
   game. That is precisely the layer Chris's business operates at.
4. **The entry-level software squeeze** (−20% for devs 22–25) plus "AI
   integration specialist" appearing in both the Pereira book and WTI role
   lists says the window Chris is building toward is the one growing.

Related: [[work-trend-index-2024-2026]] (the Microsoft-lens adoption arc),
[[2025-ai-agent-index]] (agent census), [[nist-ai-rmf]] (now market-cited),
[[oecd-ai-incidents-monitor]] (incident stream),
[[generative-ai-for-software-development-pereira]] (practitioner view of
the same convergence), [[agent-vetting-worked-examples]].
