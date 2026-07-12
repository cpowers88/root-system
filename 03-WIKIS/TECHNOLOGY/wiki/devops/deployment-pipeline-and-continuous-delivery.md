---
domain: tech
type: framework
tags: [priority/later, status/wiki-only, subject/devops, subject/continuous-delivery, subject/deployment]
---

# Deployment Pipeline and Continuous Delivery

**Summary**: *The Phoenix Project* turns the painful Phoenix release process into a visible deployment pipeline, then shows the Continuous Delivery answer: versioned environments, automated builds, automated deployments, integrated tests, and smaller batches so code can move safely to production many times per day.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 30-33; pp. 293-321)

**Last updated**: 2026-06-18

---

## The deployment pipeline is a value stream

Erik pushes Bill to stop thinking like a work-center supervisor and start thinking like the person responsible for the whole plant: the full flow from product definition, design, Development, QA, IT Operations, and the customer (source: thePhoenixProject.pdf, pp. 294-296). In IT terms, this becomes the deployment pipeline.

The SWAT team maps the pipeline from code commit through Development testing, QA environment creation, staging, load testing, Operations handoff, packaging, server creation, OS/database/application configuration, network/firewall/load-balancer changes, and final deployment validation (source: thePhoenixProject.pdf, pp. 300-303). When Bill marks every step that caused previous launch problems, nearly every step gets a red star (source: thePhoenixProject.pdf, p. 303).

Patty recognizes the map as a value stream map: boxes for steps, durations over the boxes, and triangles where work waits in WIP (source: thePhoenixProject.pdf, pp. 303-304). The insight is simple but powerful: invisible IT work can still be mapped and improved like plant work.

## Two core causes: environments and deployment packaging

The map reveals two recurring failure sources. First, environments are not available when needed, and when they are available, Dev, QA, staging, and Production are not synchronized (source: thePhoenixProject.pdf, pp. 303-305). Second, Operations receives code/configuration through brittle release instructions, then rewrites installers and scripts through multiple failed turns (source: thePhoenixProject.pdf, pp. 304-305).

The initial fix is a common build procedure that can create Dev, QA, and Production-like environments from the same source, so developers write and test against something that resembles Production (source: thePhoenixProject.pdf, p. 305). Brent's hidden environment knowledge becomes encoded into build procedures rather than staying in his head (source: thePhoenixProject.pdf, pp. 298-299, 305).

## Package once, deploy repeatedly

William proposes moving package creation upstream: when code is labeled ready to test, Development/QA generates and commits packaged code that can automatically deploy into QA, and eventually Production (source: thePhoenixProject.pdf, pp. 306-307). This removes a major backward handoff between Dev and Ops and turns "release instructions" into executable deployment tooling.

Within the first Unicorn sprint, developers can check out a virtual machine with the right OS, libraries, database settings, and other dependencies, rather than spending weeks getting local builds running (source: thePhoenixProject.pdf, pp. 309-310). QA environments that match Dev can be spun up early, and most environment differences become explicit resource differences rather than mysterious configuration drift (source: thePhoenixProject.pdf, p. 310).

## Ten deploys a day is an agility target

Erik gives Bill an intentionally aggressive target: ten deploys per day (source: thePhoenixProject.pdf, pp. 297-299). The point is not vanity speed. Business agility means detecting/responding to market change, taking larger but more calculated risks, and paying back invested capital faster by getting features into production and learning from them (source: thePhoenixProject.pdf, p. 299).

John's security work validates the same pattern. Once security tests are integrated into the automated build/test process, Unicorn can test security-relevant changes on every commit instead of waiting weeks for application-security review (source: thePhoenixProject.pdf, pp. 320-321). The team ends up with better visibility and coverage than with the old, slower review process (source: thePhoenixProject.pdf, p. 321).

## Connects to

- [[deployment-pain-and-deploy-frequency]] - this page is the solution pattern for the painful long-interval release cycle.
- [[the-three-ways-devops]] - Continuous Delivery operationalizes the Second Way through fast feedback and the First Way through smoother left-to-right flow.
- [[it-work-centers-and-kanban]] - the deployment pipeline is the larger value stream that recurring work centers and kanban lanes sit inside.
- [[security-work-and-business-outcomes]] - automated security tests show how security can be embedded in the flow rather than bolted on after deployment.
- [[business-experimentation-and-project-unicorn]] - Unicorn uses this pipeline to run smaller market experiments and get business value faster.
