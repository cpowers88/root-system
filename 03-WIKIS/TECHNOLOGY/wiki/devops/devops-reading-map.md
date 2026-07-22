---
domain: tech
type: reference
tags: [subject/devops, subject/theory-of-constraints]
timeline: later
status: wiki-only
---

# DevOps Reading Map

**Summary**: The Phoenix Project Resource Guide's further-reading section maps the book's ideas back to the books and communities behind them: Theory of Constraints, team trust, Toyota Kata, Continuous Delivery, production-readiness engineering, Visible Ops/ITIL, and kanban.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Resource Guide "Further Reading", pp. 367-379)

**Last updated**: 2026-06-18

---

## Recommended bodies of knowledge

- **Theory of Constraints**: Goldratt's *The Goal* is the explicit structural model for *The Phoenix Project*. The appendix restates the five focusing steps and maps the Phoenix constraints from Brent to deployment process to outsourced MRP support (source: thePhoenixProject.pdf, pp. 367-369).
- **Leadership trust**: Lencioni's *The Five Dysfunctions of a Team* is the model behind Steve's Part 2 off-site and the trust/conflict reset among the executives (source: thePhoenixProject.pdf, pp. 369-371).
- **Toyota Kata / Improvement Kata**: Mike Rother's *Toyota Kata* supplies the daily-practice and two-week improvement-cycle logic behind Patty's recurring improvement cadence and Erik's Third Way emphasis on repetition (source: thePhoenixProject.pdf, pp. 370-373).
- **Continuous Delivery**: Humble and Farley's *Continuous Delivery* is the clearest technical embodiment of the Three Ways: small batches, stopping the line when builds/tests/deployments fail, automated validation, and a deployment pipeline that keeps software releasable (source: thePhoenixProject.pdf, pp. 373-374).
- **Production-readiness engineering**: Michael Nygard's *Release It!* helps bridge Development and Operations by showing how architecture and code decisions create production outcomes (source: thePhoenixProject.pdf, pp. 374-375).
- **Visible Ops and ITIL service support**: the Visible Ops series turns ITIL's descriptive framework into ordered projects for reproducing high-performing IT outcomes, including service levels, change success, information security integration, compliance posture, and IT efficiency (source: thePhoenixProject.pdf, pp. 375-376).
- **Kanban**: *Personal Kanban* gives the lightweight personal WIP-control version; David J. Anderson's *Kanban* gives the organizational value-stream version and includes a Microsoft IT case study where WIP reduction and constraint-aware handoffs cut lead time sharply (source: thePhoenixProject.pdf, pp. 376-379).

## How to use this page

This is not a priority reading queue. It is a dependency map: when a Phoenix concept needs deeper treatment, this page points to the source tradition that would strengthen it. For the North Star, the highest-leverage follow-ups are TOC/kanban for audit flow, Continuous Delivery for technical remediation, and Toyota Kata for making improvements stick.

## Connects to

- [[the-phoenix-project]] - source tracker; this page covers the Resource Guide's further-reading appendix.
- [[theory-of-constraints|The Goal (Goldratt) — Theory of Constraints]] - the book's core narrative and TOC structure comes directly from Goldratt.
- [[theory-of-constraints]] - the shared constraint-management backbone across the business and tech pages.
- [[the-three-ways-devops]] - each Way has a reading lineage here: flow/TOC/CD, feedback/CD/Visible Ops, learning/Toyota Kata/resilience practice.
- [[it-work-centers-and-kanban]] - kanban and WIP-control references deepen the operational mechanics.
- [[deployment-pipeline-and-continuous-delivery]] - Continuous Delivery is the formal technical reference behind Unicorn's pipeline work.
- [[conways-law-and-organizational-design]], [[production-telemetry-and-monitoring-architecture]], [[just-culture-and-blameless-postmortems]], [[integrating-security-into-the-deployment-pipeline]] - *The DevOps Handbook* (Kim/Humble/Debois/Willis), the same authors' prescriptive companion to *The Phoenix Project* — this reading map's own missing entry, added 2026-07-13.
