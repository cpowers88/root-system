---
type: note
timeline: reference
status: active
tags: [business, audit]
created: 2026-07-18
---

# NAICS 238220 Technology Intake — Plumbing, Heating & AC Contractors

### What this is

An intake dataset of technology implementations and adoption data for NAICS
238220 (plumbing/HVAC/refrigeration contractors), gathered by live web research
July 18, 2026 during the MCP Bootcamp after-target enrichment block. Data file:
`238220_tech_intake.csv` (same folder). This is external reference research —
NOT a sprint artifact and NOT a substitute for a real workflow observation.

### Schema

| Column | Meaning |
|---|---|
| `business_type` | Vertical/segment the claim applies to |
| `company` | Named company, or "industry-wide" for aggregate stats |
| `technology` / `tech_category` | Tool and its class (FSM platform, AI voice agent, payments, pricebook…) |
| `workflow_step` | Mapped to the Day 1 swimlane vocabulary (1-first-contact … 7-invoice-payment, cross-cutting) |
| `use_description` | What the technology does in the workflow |
| `reported_effect` / `effect_type` | The claimed result and its metric class |
| `claim_type` | Evidence strength — see ranking below |
| `source_url` / `date_collected` | Provenance |

### Claim-type ranking (strongest → weakest)

1. `government-survey` (Census BTOS) — national, methodical, no sales motive
2. `platform-transaction-data` (Jobber Q1 reports) — measured, large-n, but one platform's customers
3. `platform-report` / `market-research` / `trade-association` — aggregated, some selection bias
4. `vendor-case-study` — real named company, but chosen because it succeeded
5. `vendor-claimed` / `vendor-testimonial` — weakest; directional only
6. `survey-aggregator` — third-party stat roundups; verify the primary source before citing to a client

Sort or filter on `claim_type` before using any number in client-facing work.

### How to use it Monday (Day 3 bonus rep)

Import into SQLite alongside the bootcamp fixture tables:

```
sqlite3 bootcamp.db
.mode csv
.import "238220_tech_intake.csv" tech_intake
```

Then real queries against real data, e.g. which workflow step attracts the most
technology (`GROUP BY workflow_step`), or effects filtered to strong claim types
only (`WHERE claim_type IN ('government-survey','platform-transaction-data')`).

### Standing observations from the first pull

- The adoption gap is the market: 37% AI use at 250+ employee firms vs. <20%
  at ≤4-employee firms (Census). The tools exist; small operators don't adopt.
- Step 1 (first contact) attracts the most AI money right now — Avoca at a $1B
  valuation on missed-call capture alone.
- Jobber's own data confirms the Day 1 waste finding: documented optional line
  items upsell at 25–50%, yet only 16% of pros use tiered pricing.

### Second pull — July 18 evening (rows 18–27)

Sources from the accepted `BUSINESS_WORKFLOW_AND_TECHNOLOGY_STACK_RESEARCH_REPORT_2026-07-18.md`
evidence architecture: Census BTOS official pages, both Jobber 2026 reports
(official links per the report's corrections), and industry-structure data.

**The discrepancy worth understanding (rows 13 vs 18):** Census BTOS says
<20% of very small firms use AI; Jobber's survey says 52% of home-service
owners do. Both can be true — different populations (all employer businesses
vs. 1,050 surveyed home-service pros, skewed toward software-adopting Jobber
users), different definitions (formal business AI use vs. "I use ChatGPT for
quotes"), and self-report inflation. Never average them; cite the population
with the claim. This is a live example of why `claim_type` exists.

**Market-structure takeaway (row 26):** ~89–105K companies, ~1M workers, and
an SBA small-business ceiling of $19M receipts — meaning nearly the entire
industry sits in the small/owner-operator maturity band where the adoption
gap lives.

**Parked:** Census API key registration (free, needed for CBP/BTOS API pulls);
BTOS data download for a construction-sector AI cut.

### Third pull — July 18 evening (rows 28–39): named-company sweep

Swept the vendor case-study libraries directly (ServiceTitan case-study index +
HVAC success-stories roundup, Avoca customer page, Housecall Pro testimonials,
Jobber customer stories). Scope note: the `naics` column now does real work —
rows 36/38 are electrical (238210) and row 39 tree service (561730), included
where the *workflow mechanism* transfers even though the vertical differs.

Veins still unmined: ServiceTitan's case-study library paginates (pages 2–5
unfetched); Rilla's case-study page 404s (site moved — row 9's ACCA citation
stands). All rows remain `vendor-case-study`/`vendor-testimonial` grade —
selection bias applies to every one; none prove sole causal attribution.

### Refresh path

Census BTOS releases biweekly; Jobber reports quarterly. Re-pull when a real
prospect conversation needs current numbers, not on a schedule.
