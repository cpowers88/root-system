---
tags:
  - phase-2
  - execution
  - finance
  - pricing
---

# Financial Model

> The money math: unit economics per offer, client lifetime value, break-even points, and the simple monthly model to run the business on.

## Purpose
Put real arithmetic under the roadmap targets so decisions (pricing, hiring, how much outreach is enough) are calculations instead of vibes. Every number here is adjustable — the *structure* of the math is the point.

## Key Idea
This business has exactly one economic engine: **a client enters at a small ticket and compounds into a large lifetime value at improving margins.** If you know your numbers at each stage — cost to acquire, margin per offer, conversion between rungs — then revenue targets decompose into weekly activity targets, and every roadmap page becomes checkable arithmetic.

## Unit Economics Per Offer (Solo-Stage Baseline)

| Offer | Price | Your hours | Effective $/hr | Direct costs | Margin |
|---|---|---|---|---|---|
| Audit (early) | $2,000 | 25 | $80 | ~$0 | ~100% |
| Audit (templated, month 6+) | $3,000 | 12 | $250 | ~$0 | ~100% |
| Quick-win automation | $3,500 | 25 | $140 | ~$50/mo tools (passed through) | ~95% |
| Multi-workflow package | $12,000 | 70 | $170 | pass-through | ~95% |
| Document pipeline | $10,000 | 60 | $165 | API costs (passed through) | ~90% |
| Retainer Tier 1 | $1,000/mo | 3–5/mo | $200–330 | monitoring stack | ~85% |
| Retainer Tier 2 | $2,500/mo | 8–12/mo | $210–310 | — | ~80% |

Two lessons in the table: **templating the audit triples its hourly yield** (why [[first-90-days|First 90 Days]] obsesses over harvesting templates), and **retainers beat projects on $/hr once monitoring is automated** (why the [[retainer-model|Retainer Model]] is the destination).

## Client Lifetime Value (The Number That Runs Everything)
A median good-fit client over 24 months:

```
Audit                    $2,500
Quick-win project        $4,000
Core project             $15,000
Retainer ($1,500 × 18mo) $27,000
Expansion project        $8,000
─────────────────────────────────
24-month LTV             ~$56,500
```

Even the conservative case (audit + one project + 12 months Tier 1 retainer) is ~$18K. **This is why you can afford to spend real hours on outreach and audits**: at $18–56K LTV, acquiring a client for 20–30 hours of sales effort is an outstanding trade.

## The Funnel Math (Activity → Revenue)
Work backward from a revenue target using your own conversion rates (starting assumptions below — replace with actuals by month 4):

```
outreach touches → conversations:      10–15%  (warm) / 2–5% (cold)
conversations → audit proposals:       50%
audit proposals → audits sold:         40–50%
audits → projects:                     50–70%
projects → retainers:                  50–60%
```

**Worked example — "$10K/month by month 6":**
≈ 2 audits ($3K ea) + 1 project ($6K avg monthly slice) + 3 retainers ($1K ea)
→ needs ~4–5 audit proposals/month → ~8–10 conversations → **~60–80 warm touches or ~200 cold touches per month**.
That's the whole secret: the [[sales-system|Sales System]] weekly minimums aren't arbitrary — they're this arithmetic.

## Break-Even and Cash Targets

### Personal break-even (solo)
`(personal monthly costs + business fixed costs ~$300–500/mo) ÷ (1 − 0.30 tax reserve)`.
Example: $5,000 personal + $400 business → **~$7,700/mo revenue needed**. Per the funnel math above, that's reliably reachable in months 4–8 of disciplined execution — which is what the [[one-year-plan|One-Year Plan]] assumes.

### The three cash milestones
1. **Floor:** retainer revenue ≥ business fixed costs (month ~4–6) — the business can idle without dying
2. **Ramen:** retainer revenue ≥ personal break-even (month ~10–16) — projects become pure upside
3. **Buffer:** 3 months total costs in the bank — unlocks hiring per the [[three-year-plan|Three-Year Plan]]

### Hire #1 math
A $30/hr delivery contractor billed into $150+/hr fixed-fee work is ~80% gross margin on their hours. The rule: **hire when 3 consecutive months show ≥ $6–8K/mo of delivery work you could delegate** — the hire funds themselves from month one or the playbooks aren't ready ([[fulfillment-system|Fulfillment System]]).

## The Monthly Model (30 Minutes, First Business Day of the Month)
Track six numbers on one row per month (spreadsheet or your own [[data-and-dashboard-pathway|dashboard]] — you should be client #1):

| Metric | Why |
|---|---|
| Revenue (project / retainer split) | The quality of revenue, not just quantity |
| Recurring monthly revenue | The enterprise-value line ([[ten-year-scale-plan|Ten-Year Plan]]) |
| Pipeline coverage (proposals out ÷ next-month target) | ≥2× or sales gets the week's surplus hours |
| Hours by type (sales / delivery / admin) | Feeds real unit economics + the hire decision |
| Effective $/hr per completed engagement | Pricing feedback ([[pricing-models|Pricing Models]]) |
| Cash + tax reserve | Solvency, no surprises in April |

## Practical Actions
- Build the one-tab spreadsheet today: unit-economics table, funnel assumptions, monthly tracking rows. Update conversions with actuals monthly — by month 4 the model is *yours*, not this page's.
- Compute your personal break-even number now and write it on the [[weekly-scorecard|weekly scorecard]].
- Before quoting anything, sanity-check against the unit table: if an engagement prices below ~$100/hr effective at your current stage, rescope or decline.

## Beginner Version
Track three numbers weekly (outreach, proposals out, cash) and six monthly (table above). Resist building a beautiful 12-tab projection model — that's [[risks-and-failure-modes|builder's procrastination]] wearing a finance costume.

## Advanced Version
Margin per product line, utilization per team member, CAC by channel, NRR, and a rolling 13-week cash forecast — produced by your own systems as a living demo of the [[data-and-dashboard-pathway|Data & Dashboard Pathway]]. The same model, extended, becomes the diligence financial package at exit.

## Revenue Connection
This page *is* the revenue connection for the whole wiki: LTV justifies the sales effort, unit economics set the prices, funnel math sets the weekly activity, and the cash milestones time every scaling decision. When a roadmap number feels arbitrary, this page is where to check it.

## Related Pages
- [[pricing-models|Pricing Models]] — the prices the unit economics assume
- [[sales-system|Sales System]] — the activity the funnel math demands
- [[retainer-model|Retainer Model]] — the recurring line that changes everything
- [[business-setup|Business Setup]] — the hygiene that keeps these numbers true
- [[cash-flow-audit-method|Cash Flow Audit Method]] — the same Profit First discipline (allocate first, operate on the remainder) applied to your own business, not just clients'
