---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/business-systems, subject/risk-management, start]
---

# IT Risk and Business Value Chains

**Summary**: *The Phoenix Project* turns "IT risk" into business-risk mapping: start from executive business measures, trace the value chains and systems they depend on, then define leading indicators and controls that show whether IT is helping or jeopardizing the business outcome.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 25-27, 35; pp. 246-270, 330-334)

**Last updated**: 2026-06-18

---

## Start from executive measures, not IT complaints

John's turnaround begins when he asks Dick what his job is and what goals he manages. Dick's company-level measures are not IT measures: revenue, market share, average order size, profitability, return on assets, customer needs/wants, product portfolio, R&D effectiveness, time to market, sales pipeline, customer on-time delivery, customer retention, and sales forecast accuracy (source: thePhoenixProject.pdf, pp. 248-251).

That list changes the frame. Bill realizes that Dick can sense IT as a vague pain but has not localized which business outcomes depend on which IT systems and processes (source: thePhoenixProject.pdf, pp. 252-253). Erik names the underlying principle as Deming's "appreciation for the system": as part of the First Way, IT has to understand the business system it operates inside (source: thePhoenixProject.pdf, p. 253).

## Under-scoping and over-scoping

Erik gives Bill and John paired missions. Bill must find where IT is under-scoped: places where technology or operational process actively jeopardizes Dick's business measures but nobody has made the dependency explicit. John must find where IT is over-scoped: places where controls or audit work are being imposed even though other business controls already mitigate the risk (source: thePhoenixProject.pdf, pp. 253-255).

The shared idea is scoping what matters. The point is not "more IT involvement" or "less compliance" in the abstract; it is matching attention to the actual value chain and actual control reliance (source: thePhoenixProject.pdf, pp. 253-255).

## Value-chain interviews

Bill and Patty interview Ron, the VP of Manufacturing Sales, and Maggie, a major Phoenix business sponsor, as business process owners. Ron ties sales forecast accuracy, sales pipeline, and customer retention to stockout data, MRP availability, phone/voicemail reliability, CRM reporting, and customer order changes; outages translate into delayed orders, canceled orders, rebids, and quota misses (source: thePhoenixProject.pdf, pp. 256-260).

Maggie ties customer understanding, product portfolio, market share, and average order size to accurate and timely order/inventory data. Her "magic wand" is daily, reliable channel data that can feed A/B tested promotions, inventory decisions, and product bets; she also exposes the core Phoenix problem: the reporting/data features that would create business value are being delayed while the project continues to accumulate WIP (source: thePhoenixProject.pdf, pp. 260-264).

## IT risks are business risks

Bill turns the interviews into a table with four columns: business performance measure, area of IT reliance, business risk due to IT, and IT controls relied upon (source: thePhoenixProject.pdf, pp. 265-266). Examples include order-entry and inventory systems creating inaccurate or late customer-needs data, CRM/phone/MRP systems impairing sales pipeline and on-time delivery, and Phoenix's three-year cycle time making it unlikely to clear the internal hurdle rate (source: thePhoenixProject.pdf, pp. 265-266).

The critical language shift comes in the meeting with Dick: operational risks posed by IT are not merely IT risks; they are business risks (source: thePhoenixProject.pdf, p. 269). Dick's immediate realization is strategic: Parts Unlimited cannot even write a sane IT outsourcing contract if it has not defined what the business needs IT to protect and enable (source: thePhoenixProject.pdf, p. 269).

## Leading indicators

The team starts designing predictive measures that connect IT work to business outcomes. For phone and MRP systems, proposed measures include change-management compliance, production-change review, completion of scheduled maintenance, and elimination of single points of failure (source: thePhoenixProject.pdf, p. 267). For customer-needs data, proposed measures include Phoenix's ability to support weekly and eventually daily reporting and the percentage of valid SKUs created by Marketing (source: thePhoenixProject.pdf, p. 267).

The logic is the same as Erik's vehicle-maintenance analogy: on-time delivery is the business KPI, but oil-change compliance is a forward-looking indicator that predicts whether the fleet will keep delivering (source: thePhoenixProject.pdf, pp. 254-255). In IT, preventive patching, change discipline, data-quality checks, and environment controls become business-facing leading indicators when they are linked to the value chain they protect.

## North Star application

For a digital audit/integration practice, this is one of the most directly promotable patterns in the wiki. A serious audit should not start by asking "what software do you use?" It should start from the business outcomes the owner cares about, identify the value chains behind them, map the systems and data those chains rely on, name the business risks created by weak IT/process design, and propose leading indicators or controls that reduce those risks.

## IT as a business competency

The novel's executive conclusion is not "make a better IT department." Steve argues that IT is pervasive like electricity and literacy: every part of the business uses technology, so business and IT cannot make decisions separately (source: thePhoenixProject.pdf, pp. 331-333). He offers Bill a path toward COO because an operations leader who does not understand the IT systems that run the business is relying on someone else to do the job (source: thePhoenixProject.pdf, pp. 332-334).

For this wiki's North Star, that is the target state: not merely being the technical person who fixes systems, but becoming the operator who can connect systems, process, finance, market response, and execution into one business machine.

## Connects to

- [[the-three-ways-devops]] - this is the First Way expanded beyond IT Operations flow into appreciation for the larger business system IT serves.
- [[security-work-and-business-outcomes]] - John's over-scoping/under-scoping lesson is the security/compliance version of the same value-chain mapping.
- [[deployment-pain-and-deploy-frequency]] - Phoenix's long release cycle becomes a financial business risk because capital is locked in WIP too long to clear the hurdle rate.
- [[it-work-centers-and-kanban]] - work-center visibility helps IT explain which systems, people, routings, and controls a business value chain depends on.
- [[theory-of-constraints]] - the page applies constraint thinking to business measures: improve what governs the goal, not whatever is locally visible.
- business-model-and-barringer-ireland-template - both pages force technology choices to be evaluated through the business model and value-delivery logic, not as isolated technical preferences.
- [[business-experimentation-and-project-unicorn]] - Unicorn is the value-chain mapping converted into a revenue-generating experiment.
