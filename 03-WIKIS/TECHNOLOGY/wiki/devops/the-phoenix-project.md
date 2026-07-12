---
domain: tech
type: reference
tags: [priority/later, status/wiki-only, subject/devops]
---

# The Phoenix Project (Gene Kim, Kevin Behr & George Spafford)

**Summary**: Source tracker for *The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win* (2013), a business novel structurally modeled on Goldratt's *The Goal* that teaches DevOps principles through a fictional IT turnaround at Parts Unlimited.

**Sources**: The Phoenix Project, thePhoenixProject.pdf

**Last updated**: 2026-06-18

---

## About this source

The source contains roughly 340 narrative pages plus a Resource Guide appendix: Introduction, Why Do DevOps?, Where DevOps Came From, The Three Ways Explained, Top DevOps Myths, The Four Types of Work, and Further Reading. Like *The Goal*, the narrative arc carries most of the teaching through a mentor character, Erik Reid, while the Resource Guide formalizes what the story dramatizes (source: thePhoenixProject.pdf).

This source is now fully ingested: narrative pages 1-339 and Resource Guide pages 347-379 have been systematically read and reflected into the wiki.

## What's been ingested

| Concept | Page | Chapters / pages covered |
|---|---|---|
| Cast, setup, inciting incident (payroll outage), and the structural dysfunctions it exposes: key-man dependency, dead change management, Dev/Ops/Security tribal warfare, date-driven projects | [[it-operations-bottleneck-management]], [[change-management-failure-modes]] | Front matter, Ch. 1-6 (pp. 1-83) |
| Erik Reid's introduction; explicit citation of Goldratt's *The Goal* and the bottleneck principle applied to IT; naming of the Four Types of Work and the Three Ways | [[it-operations-bottleneck-management]], [[four-types-of-work]] | Ch. 7-8 (pp. 84-99) |
| Risk-tiered change management, Brent containment, mandatory documentation, WIP pileup, and the practical collapse of over-broad CAB control | [[change-management-failure-modes]], [[it-operations-bottleneck-management]] | Ch. 8-11 (pp. 100-124) |
| The Phoenix launch goes ahead over Bill's objection and fails publicly: POS outage, manual fallback, double/triple-charged customers, and credit-card data exposure | [[date-driven-launch-failure]] | Ch. 12-13 (pp. 125-139) |
| Fallout compounds: PCI breach, 90-day outsourcing ultimatum, Bill/Chris reconciliation, the deployment-interval downward spiral, and unplanned work as the fourth work type | [[date-driven-launch-failure]], [[deployment-pain-and-deploy-frequency]], [[four-types-of-work]] | Ch. 14-15 (pp. 140-159) |
| Erik formally teaches the Three Ways, explicitly mapped onto Goldratt's Five Focusing Steps; Bill quits after Steve's command-and-control crisis response | [[the-three-ways-devops]] | Ch. 16 (pp. 166-173) |
| Steve apologizes and brings Bill back under a 90-day mandate; the leadership off-site reframes IT as a company competency and trust problem | [[the-phoenix-project]], [[the-three-ways-devops]] | Ch. 17-19 (pp. 176-193) |
| Erik teaches work centers, bills of resources, safe work release, monitoring as constraint elevation, queue-time visibility, and Improvement Kata; security/compliance is reframed around business protection | [[it-work-centers-and-kanban]], [[security-work-and-business-outcomes]], [[the-three-ways-devops]] | Ch. 20-21 (pp. 194-223) |
| Patty converts the lessons into practice: service-request kanban, checklists, measured laptop provisioning, two-week PDCA improvement cycles, colored work cards, and project-release rules | [[it-work-centers-and-kanban]], [[change-management-failure-modes]], [[it-operations-bottleneck-management]] | Ch. 22 (pp. 224-233) |
| The Phoenix test-environment delay exposes touch time vs. total process time; queueing and handoffs become visible through kanban lanes and expediting | [[it-work-centers-and-kanban]], [[the-three-ways-devops]] | Ch. 23 (pp. 234-238) |
| John recovers by learning the business first; Bill and John map Dick's business measures to IT dependencies, distinguish under-scoped business risk from over-scoped compliance work, and reframe IT operational risk as business risk | [[it-risk-and-business-value-chains]], [[security-work-and-business-outcomes]], [[the-three-ways-devops]] | Ch. 24-27 (pp. 239-273) |
| Part 2 closes with visible improvement but a second Phoenix deployment still creates emergency recovery work; Erik names oversized batches and too-slow feedback as the next obstacle | [[deployment-pain-and-deploy-frequency]], [[the-three-ways-devops]] | Ch. 28-29 (pp. 274-289) |
| Part 3 turns the batch-size lesson into the Unicorn fast path: deployment-pipeline value-stream mapping, environment/build/deploy automation, security tests in the pipeline, cloud elasticity, A/B-tested promotions, and fast business learning | [[deployment-pipeline-and-continuous-delivery]], [[business-experimentation-and-project-unicorn]], [[security-work-and-business-outcomes]] | Ch. 30-34 (pp. 293-328) |
| The narrative closes with resilience engineering/chaos testing, record business results, Sarah's exit, Bill's COO path, and Erik's "DevOps Cookbook" request | [[resilience-engineering-and-chaos-testing]], [[it-risk-and-business-value-chains]], [[the-three-ways-devops]] | Ch. 35 (pp. 328-339) |
| Resource Guide formalization: DevOps business case, formal Three Ways, origins, myths, full Four Types definitions, wait-time/WIP explanation, and further-reading map | [[deployment-pain-and-deploy-frequency]], [[the-three-ways-devops]], [[devops-origins-and-myths]], [[four-types-of-work]], [[devops-reading-map]] | Resource Guide pp. 347-379 |

## RESUME HERE

**Phoenix source complete.** No narrative or appendix pages remain. The related thread gap in `python-crash-course.pdf` is also now closed; python-crash-course marks Ch. 1-20 fully ingested.

## Connects to

- [[theory-of-constraints]] - Erik explicitly invokes Goldratt's bottleneck principle to frame how Bill should think about IT Operations capacity.
- [[theory-of-constraints|The Goal (Goldratt) — Theory of Constraints]] - same novel-as-teaching-tool structure; Erik's plant-floor story is presented as a direct retelling of *The Goal*'s bottleneck logic.
- [[it-operations-bottleneck-management]] - the IT-specific application of TOC this book builds toward.
- [[four-types-of-work]] - the book's core diagnostic framework for why IT Operations is always overloaded.
- [[change-management-failure-modes]] - why change management programs collapse in practice, and what Bill tries instead.
- [[date-driven-launch-failure]] - the Phoenix launch disaster: what happens when a fixed date forces testing and ops readiness to be cut.
- [[deployment-pain-and-deploy-frequency]] - Chris's deployment-pain symptom, the Resource Guide benchmark data, and the business case for smaller batches.
- [[the-three-ways-devops]] - the Three Ways formally explained, with the First Way mapped step-by-step onto Goldratt's Five Focusing Steps.
- [[it-work-centers-and-kanban]] - Part 2's concrete operating model for recurring IT work, kanban, queue-time visibility, and constraint-aware project release.
- [[security-work-and-business-outcomes]] - Part 2's security/compliance reframe: protect the business without flooding IT with meaningless work.
- [[it-risk-and-business-value-chains]] - Part 2's audit/integration pattern: map business outcomes to IT dependencies, risks, and leading indicators.
- [[deployment-pipeline-and-continuous-delivery]] - Part 3's technical mechanism for smaller batches and faster feedback.
- [[business-experimentation-and-project-unicorn]] - the narrative business case for DevOps as market experimentation and revenue impact.
- [[resilience-engineering-and-chaos-testing]] - the final Third Way pattern: deliberate operational and security fault injection.
- [[devops-origins-and-myths]] - the Resource Guide's explanation of DevOps origins and common enterprise misconceptions.
- [[devops-reading-map]] - the Resource Guide's further-reading map behind the book's concepts.
