---
type: report
timeline: log
status: complete
tags: [business, technology, research, audit]
---

# Business Workflow and Technology Stack Research Report
### Systems + Technology Engineer assessment | July 18, 2026

**Closed July 21:** Chris accepted the report July 18 and its active deliverables
now live in the MCP Bootcamp plan/blueprint and Technology Strategy. Triggered future
work remains with those owners; this file is the retained research decision record.

## Decision

Build a reusable **workflow-to-stack evidence system**, not a catalog of popular
business software.

The controlling research question is:

> Given a specific workflow failure, what is the smallest technology architecture
> that fixes it at the business's current maturity level, and what evidence
> justifies moving to a more advanced layer?

This directly supports the Advisor-Builder sequence:

```text
observe the real workflow
-> diagnose the constraint and economic consequence
-> identify where state and evidence should live
-> select the cheapest valid intervention
-> measure whether it worked
-> retain, revise, retire, or escalate the stack
```

The research product should eventually become a library of evidence-backed workflow
patterns. Each pattern can support an audit, recommendation, implementation,
retainer, training asset, or later product without locking the business to one
industry or vendor.

## Why This Is the Right Direction

The current reports agree on three points:

1. The vault already contains broad technology knowledge. The gap is integrated,
   operating proof against real workflows.
2. Workflow reality is upstream of technology. Value-stream mapping, system
   inventories, data-flow tracing, constraint analysis, and process mining are
   diagnostic instruments; software is a possible response.
3. A stack is not a shopping list. Two businesses can have the same workflow problem
   but need different responses because their volume, data, existing systems,
   internal skills, control needs, and failure costs differ.

The July 18 construction case produced a useful first pattern: durable approval
information disappears when the phone call ends, contributing to undocumented
extras, late billing, short payment, and disputes. That finding is a better starting
point than researching "construction technology" in the abstract.

## The Research Model

### 1. Business context

Record the industry, NAICS level, geography, size, revenue/maturity band, operating
model, demand conditions, labor constraints, and data availability. These fields
separate a national market pattern from a claim about one actual business.

### 2. Workflow context

Name one bounded flow with a trigger, case/object, actors, steps, handoffs, systems,
inputs, outputs, decision owner, endpoint, exception path, and measurable outcome.
Examples include lead-to-estimate, estimate-to-approval, change-order-to-cash,
dispatch-to-completion, invoice-to-payment, and issue-to-resolution.

### 3. Current technology stack

Inventory each tool by its actual job in the workflow, not by its marketing category.
For every important fact, name the source of truth, who may change it, where it is
copied, and what happens when the tool or handoff fails.

### 4. Effectiveness evidence

"They use it" and "it works" are different claims. Grade evidence separately:

| Level | Evidence | What may be claimed |
|---:|---|---|
| 0 | Unknown or vendor assertion | Capability exists; effectiveness unknown |
| 1 | Owner/worker opinion | Perceived usefulness or friction |
| 2 | Direct observation or artifact trace | The workflow and failure pattern are real |
| 3 | Reconciled operating data | Frequency, delay, cost, quality, or adoption can be quantified |
| 4 | Before/after intervention measurement | The change is associated with a measured outcome |
| 5 | Repeated or comparison-backed result | The pattern is durable enough to reuse cautiously |

Correlation is not automatically causation. A high-performing group may use more
technology because it is already better managed; the technology may be one part of
the operating system rather than the sole cause.

### 5. Recommendation

Run the Recommendation Ladder in order:

```text
eliminate -> simplify -> use what they own -> configure
-> integrate -> build light -> build real
```

Every recommendation must include the expected outcome, owner, cost, risk, failure
behavior, maintenance burden, acceptance check, and rollback or exit path.

## Workflow-to-Stack Layers

| Layer | Business question | Typical evidence/tools |
|---|---|---|
| Observe | What actually happens? | Field notes, interviews, swimlanes, VSM, Forms, Sheets |
| Diagnose | Where does work wait, fail, repeat, or lose value? | TOC, Little's Law, SQL, SQLite, process mining when justified |
| Establish truth | Where should each fact permanently live? | Existing vertical SaaS, CRM/ERP, Airtable, SQLite/Postgres |
| Integrate | Where is information manually transferred? | Native integrations, Make, Zapier, n8n, APIs, webhooks |
| Decide | What must someone see or act on? | SQL, spreadsheets, Looker Studio, Power BI |
| Build | What required capability is not available cheaply? | Python, Flask, SQLAlchemy, bounded internal tools |
| Add AI | Where does bounded judgment-like work exist? | Model APIs, structured outputs, MCP, evals, human approval |
| Operate | How will the system be monitored and recovered? | Git, pytest, CI, logs, alerts, backups, restore, runbooks |

## Evidence Architecture

No single source can answer market adoption, workflow reality, stack configuration,
and realized effectiveness. Use a layered evidence model.

| Evidence layer | Source role | Initial sources | Main limit |
|---|---|---|---|
| National business baseline | Adoption and conditions across employer businesses | Census Bureau BTOS core + 2026 AI Supplement | Aggregate and mostly self-reported; not a workflow audit |
| AI diffusion mechanism | Function/task breadth, augmentation, investment, firm-size patterns | Census working paper CES-26-25 | Correlational research; not proof a specific tool caused performance |
| Vertical operating benchmark | Demand, revenue, new work, invoice size, payments | Jobber Home Service Economic Report 2026 Q1 | Proprietary Jobber-user cohort, not all home-service firms |
| Vertical workflow sentiment | Challenges, practices, AI uses, response/quote behaviors | Jobber 2026 Home Service Trends Report | Survey of 1,050 owners; self-report and vendor-published |
| Industry structure | Establishments, employment, wages, business formation | Census CBP/BFS and BLS QCEW | Describes the market, not technology effectiveness |
| Workflow truth | Steps, handoffs, delays, workarounds, exceptions | Approved observation, artifacts, system exports | Small/local sample until repeated |
| Technology truth | Features, APIs, permissions, integrations, limits | Official vendor documentation and controlled tests | Capability does not prove adoption or business value |
| Outcome proof | Before/after metrics and user behavior | Client-approved measurements or internal practice proof | Requires consistent definitions and sufficient time |

### Census BTOS role

BTOS is the strongest national baseline in this plan. The Census Bureau describes it
as a high-frequency, nationally representative survey of U.S. employer businesses
excluding farms, with roughly 1.2 million businesses divided across six panels. The
2026 AI Supplement supports cuts by industry, geography, and firm size and examines
business-function and worker-task use. Use BTOS to answer **where adoption and
business conditions differ**, not whether a specific workflow tool worked.

Official entry points:

- https://www.census.gov/programs-surveys/btos.html
- https://www.census.gov/hfp/btos/data_downloads
- https://lehd.ces.census.gov/applications/creat/paper-profile/1413

### Jobber role

Use two Jobber products separately:

1. The **2026 Q1 Home Service Economic Report** supplies proprietary operating
   benchmarks from a cohort of Jobber users: median revenue, new work scheduled,
   invoice size, and digital-payment adoption across Green, Cleaning, Contracting,
   and Construction. It is useful for vertical timing and operating context.
2. The **2026 Home Service Trends Report** supplies owner-survey evidence about
   pricing, lead response, quoting, operational challenges, AI uses, and differences
   among business maturity and performance cohorts. It is useful for forming
   workflow hypotheses.

Neither source by itself proves that Jobber, AI, or automation caused a performance
result. Preserve the vendor role, population, cohort rules, survey confidence level,
and measurement definitions beside every extracted claim.

Official entry points:

- https://www.getjobber.com/home-service-reports/may-2026/
- https://www.getjobber.com/home-service-trends-report/

## Initial Research Lane

Start with **estimate/change-order approval -> work authorization -> billing ->
collection** across three operating maturities:

| Maturity | Typical current state | Research focus |
|---|---|---|
| Small owner-operator | Phone/text/email, memory, QuickBooks, shared files | Capture approval durably with the fewest new steps |
| Growing contractor | Jobber, JobTread, Buildertrend, Contractor Foreman, accounting system | Remove duplicate entry and connect scope, job cost, invoice, and status |
| Larger contractor | Procore, Autodesk Construction Cloud, Viewpoint/ERP, reporting stack | Use event histories, controls, integrations, conformance, and process mining |

For each maturity, answer:

- Where does scope become authoritative?
- What event proves customer authorization?
- How does the approved amount reach job costing and billing?
- Where is information copied or re-entered?
- What happens when the approval, invoice, or payment event is missing?
- Can an existing feature solve the problem?
- What measured threshold would justify integration or custom development?

## Amendment — NAICS 238220 Technology Intake Review

**Added July 18, 2026.** Claude produced a 17-row research intake at
`05-BUSINESS\03-Case Studies\238220_tech_intake.csv` for NAICS 238220
(Plumbing, Heating, and Air-Conditioning Contractors). The file is a strong source
and hypothesis queue, but it is not yet a collection of 17 proven case studies.

The intake spans five distinct evidence roles that must remain labeled:

| Evidence role | Included sources | Appropriate use |
|---|---|---|
| National baseline | Census BTOS AI-use data | Compare adoption by firm size and sector; establish national context |
| Vertical operating benchmark | Jobber Q1 2026 Economic Report and 2026 Trends Report | Form home-service workflow, demand, payment, pricing, and adoption hypotheses |
| Named vendor case | Interstate AC, ENCON, Bill Joplin's, Avoca/Yost & Campbell | Show a plausible implementation mechanism and reported outcome worth testing |
| Vendor testimonial/aggregate | Housecall Pro testimonials and ServiceTitan Five-Year Club | Supporting pattern evidence only; attribution and selection bias remain material |
| Category/market signal | ACCA, FSM statistics roundup, Mordor FSM market, Avoca funding | Establish category attention or market momentum; not workflow-effectiveness proof |

### Source-strength decision

#### Use as baseline evidence

- **Census BTOS** — strongest adoption baseline in the file. It supports overall,
  firm-size, and sector comparisons but does not prove that a particular tool caused
  a result.
- **Jobber Q1 2026 Home Service Economic Report** — useful proprietary transaction
  evidence for median revenue, new work scheduled, invoice size, and digital-payment
  adoption. Its cohort is Jobber users rather than the entire home-service market.
- **Jobber 2026 Home Service Trends Report** — useful owner-survey and proprietary
  benchmark evidence for pricing, quoting, lead response, workflow friction, and AI
  use. Self-report and vendor-publication limitations remain visible.

#### Use as named implementation cases with vendor-bias labels

- **Interstate AC / ServiceTitan** — reported 33% first-full-year revenue growth,
  billing accelerated by two to three weeks, and payroll completed in 24 hours. This
  is the strongest case in the intake for the current construction finding because
  it connects durable field records to billing cycle time and visibility.
- **ENCON / ServiceTitan** — reported technician efficiency improvement from
  approximately 60-65% to 70%. Use as a scheduling/measurement hypothesis, not an
  independent causal estimate.
- **Bill Joplin's / ServiceTitan AI Agent** — the primary ServiceTitan source reports
  more than 1,300 calls handled, more than 90% resulting in booked jobs, 72%
  completed without human intervention, and company-estimated incremental booked
  revenue and operating-cost effects. This is a strong named example but remains a
  vendor announcement using company-reported results.
- **Avoca / Yost & Campbell and the answering-service replacement case** — useful
  evidence for missed-call capture and AI-to-FSM integration. The reported 40%-to-
  95% booking improvement and 20% revenue-growth case remain vendor case claims.
- **Housecall Pro testimonials** — useful for identifying owner-perceived time,
  booking, and scaling benefits. Do not treat testimonial growth as software-only
  attribution.

#### Use only as supporting market signals

- **ACCA HVACR article** — trade-association evidence that AI use cases have moved
  into real HVACR operations. Its Rilla figures came from a vendor presenter and
  show correlations between process adherence and outcomes; they are not an
  independent industry adoption study.
- **ServiceTitan Five-Year Club** — its 21% average first-two-year revenue claim is
  vendor-published without enough visible methodology to use as a neutral benchmark.
- **Avoca funding** — category validation only. Avoca announced more than $125
  million raised across funding rounds **at a $1 billion valuation**; it did not
  raise $1 billion. Funding does not establish customer ROI or workflow fitness.

#### Park pending primary evidence

- **FSM statistics roundups** — the 48% overall adoption and enterprise/SME split
  should not enter client-facing work until their original surveys, definitions,
  samples, and dates are located.
- **Mordor field-service-management forecast** — useful only as a directional market
  estimate. Market size and CAGR do not demonstrate operational need, adoption, or
  effectiveness for a specific business.

### Intake corrections and verification notes

| CSV row | Required treatment |
|---:|---|
| 1 | Keep the Interstate figures, but map the case across field capture, work tracking, billing, payroll, and reporting rather than only `7-invoice-payment`. |
| 3 | Retain `vendor-claimed`; do not promote the 21% average to an independent benchmark without cohort and method detail. |
| 4 | Replace the Simply Wall St link with the primary ServiceTitan press/case source. |
| 5 | Mark the Bayshore 13-to-42 employees/tripled-income claim unverified until the underlying video or transcript is preserved and reviewed. |
| 6 | The 90% year-over-year jobs-booked testimonial names **OC Tasker**; it is not an unnamed customer. |
| 7 | Correct all shorthand to `$125M+ raised at a $1B valuation`; keep funding separate from customer-outcome evidence. |
| 9 | Keep ACCA as trade-association reporting of a vendor presentation; label the 70,000-appointment result correlational. |
| 10-11 | Park the FSM adoption percentages until primary sources are found. |
| 14 | Prefer the official Jobber Q1 report over a syndicated press release. |
| 15 | Jobber publishes the 25-50% optional-line-item upsell benchmark and 16% tiered-pricing rate; preserve its proprietary-platform source role. |

### Verified primary/source-owner links

| Source | Link |
|---|---|
| Census AI use by firm size and sector | https://www.census.gov/library/stories/2026/05/ai-use-businesses.html |
| Census BTOS downloads and documentation | https://www.census.gov/hfp/btos/data_downloads |
| Interstate AC case | https://www.servicetitan.com/case-studies/interstate-ac |
| ENCON case | https://www.servicetitan.com/case-studies/encon |
| ServiceTitan Five-Year Club | https://www.servicetitan.com/blog/success-story-five-year-club-commercial-customers |
| Bill Joplin's AI Agent announcement | https://www.servicetitan.com/press/bill-joplins-air-conditioning-and-heating-books-over-90-of-calls-with-servicetitan-ai-voice-agent |
| Housecall Pro testimonials | https://www.housecallpro.com/about/testimonials-reviews/ |
| Avoca answering-service case discussion | https://getavoca.ai/blog/avocas-ai-answers-the-phones-100-of-the-time-tyson-chen-avoca-rilla-labs-episode-15 |
| Avoca/Yost & Campbell case | https://www.avoca.ai/customers/granite-comfort-people |
| ACCA HVACR AI implementation article | https://hvac-blog.acca.org/ai-implementation-moves-from-experimental-to-operational-in-hvacr-industry/ |
| Jobber Q1 2026 Economic Report | https://www.getjobber.com/home-service-reports/may-2026/ |
| Jobber 2026 Trends Report | https://www.getjobber.com/home-service-trends-report/ |
| Avoca funding announcement | https://www.prnewswire.com/news-releases/avoca-raises-125m-at-1b-valuation-to-power-americas-services-economy-with-ai-302753962.html |

### Two workflow lanes exposed by the intake

The data is most valuable when reorganized by workflow rather than vendor.

#### Lane A — lead to booked job

```text
lead/call -> answer -> qualify -> schedule -> dispatch -> follow up
```

Relevant evidence: Bill Joplin's ServiceTitan AI Agent, Avoca answering and booking
cases, Housecall Pro online-booking testimonial, ACCA/Rilla coaching evidence, and
Jobber lead-response and conversion benchmarks.

The technical pattern is an AI or automated front door connected to the live
customer, capacity, scheduling, and dispatch source of truth, with explicit human
escalation and measurable booking, abandonment, error, revenue, and exception rates.

#### Lane B — estimate/change order to cash

```text
scope -> estimate/options -> approval -> work record -> invoice -> payment
```

Relevant evidence: the July 18 Day 1 construction finding, Interstate AC,
ServiceTitan's full workflow platform, Jobber's optional-line-item/tiered-pricing
benchmark, and Jobber's digital-payment data.

This remains the first research lane because it directly matches the observed root-
cause hypothesis: no durable record is created at the moment of price or change
agreement. The smallest response may be a disciplined existing-tool configuration;
integration, AI, or custom software must earn escalation through measured failure.

### Normalized intake requirements

Before the CSV becomes an analytical dataset or client-facing source ledger, add or
derive these fields in a reviewed V2 rather than overwriting Claude's original:

| Field | Purpose |
|---|---|
| `source_title` / `publisher` | Identify who made the claim and in what artifact |
| `primary_source_url` | Replace aggregators or financial press when an original source exists |
| `population_sample` / `reference_period` | Define what the result actually represents |
| `baseline` / `post_value` / `unit` | Separate measurable change from narrative shorthand |
| `evidence_level` | Apply this report's 0-5 evidence scale |
| `verification_status` | verified / partially verified / unverified / parked |
| `attribution_limit` | State why the technology cannot receive sole causal credit |
| `research_lane` | lead-to-booked-job / estimate-change-order-to-cash / other |
| `freshness_trigger` | State when the claim must be refreshed or rechecked |

The normalized file should preserve each reported claim exactly while adding a
separate reviewed interpretation. Never silently rewrite the source's language into
a stronger claim.

## Process Mining Position

Process mining is a future differentiator, not the first diagnostic offered to a
small business. Use the maturity path:

```text
observation -> swimlane/VSM -> basic case and timestamp capture
-> SQL/dashboard analysis -> validated event log -> process mining
-> conformance monitoring and measured improvement
```

PM4Py becomes appropriate when a business has repeatable digitally mediated work,
a credible case/object identifier, trustworthy activity events and timestamps, and a
decision worth the extraction cost. Without that evidence, a polished process model
would create false precision.

## Deliverables to Build

1. Reusable workflow-and-stack research template — created with this report as
   `05-BUSINESS\06-Capability Library\APQC_13_1_WORKFLOW_TECHNOLOGY_STACK_EVIDENCE_TEMPLATE.md`.
2. One completed internal example using the July 18 construction workflow evidence.
3. A reviewed V2 of `238220_tech_intake.csv` with evidence, verification,
   attribution, population, period, and workflow-lane fields; preserve the original.
4. A small source ledger for BTOS, Jobber, and later sources with population,
   measurement definitions, release cadence, limitations, and freshness triggers.
5. Only after the first completed example: decide whether repeated structured data
   warrants a spreadsheet, SQLite schema, or dashboard.

## Acceptance and Next Decision

This research system earns continuation when one completed template:

- keeps market evidence separate from observed business evidence;
- maps one bounded workflow and its current stack;
- distinguishes adoption, use, and measured effectiveness;
- produces a Recommendation-Ladder decision with a named test;
- can be explained to a nontechnical owner without the source caveats disappearing.

### Acceptance decision — July 18, 2026 (evening)

Chris accepted this report after Claude's independent review (verdict: accept,
one sequencing challenge). Sequencing amendment adopted: deliverable 3 (reviewed
V2 of the intake CSV) folds into **Bootcamp Day 3 (Mon Jul 20, Data
Engineering)** as live-paired material; deliverable 2 (completed internal
template on change-order-to-cash) folds into **Day 7 (Fri Jul 24, Product &
Value)**. No parallel track runs beside the sprint this week; remaining
deliverables (source ledger, database decision) wait for their named triggers.
Claude's CSV row corrections (rows 4, 5, 6, 7, 10-11) are accepted and will be
applied in the V2, not by editing the original.

**Next exact action:** preserve Claude's original intake and create a reviewed V2
with the normalized fields above, organized first by the two workflow lanes. Then
complete one internal template copy for the construction change-order-to-cash pattern
using existing sanitized Day 1 artifacts. Add BTOS and Jobber figures only where they
inform the industry baseline or a testable hypothesis; do not let aggregate reports
overwrite what the observed workflow says.
