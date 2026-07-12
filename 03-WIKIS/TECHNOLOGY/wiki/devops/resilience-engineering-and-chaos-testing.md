---
domain: tech
type: concept
tags: [priority/later, status/wiki-only, subject/devops, subject/resilience, subject/security]
---

# Resilience Engineering and Chaos Testing

**Summary**: *The Phoenix Project*'s final Third Way example is deliberate fault injection: teams improve daily work by repeatedly breaking systems in controlled ways, forcing Development, Operations, and Security to build services that recover and resist failure.

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 35; pp. 328-330)

**Last updated**: 2026-06-18

---

## Preventive work becomes a habit

By the end of the narrative, Bill's group is consistently spending 15% of its time on preventive infrastructure projects, closing monitoring gaps, and refactoring/replacing the top ten fragile artifacts (source: thePhoenixProject.pdf, pp. 328-330). This is the Third Way becoming ordinary management practice rather than an emergency program.

The key shift is that quiet days are not treated as idle time. Bill uses them to coach managers through two-week improvement cycles, continuing the Improvement Kata pattern introduced earlier (source: thePhoenixProject.pdf, p. 329).

## Chaos Monkey for operations

Project Narwhal, also called the "Simian Army Chaos Monkey" project, deliberately creates large-scale faults by randomly killing processes or entire servers (source: thePhoenixProject.pdf, p. 330). At first, this causes test and occasional production infrastructure to crash, but over time the repeated failures force Development and IT Operations to make services resilient, rugged, and durable (source: thePhoenixProject.pdf, p. 330).

This is not failure theater. It is practice under stress, designed to make the organization better at detecting, absorbing, and recovering from the failures that will happen anyway.

## Evil Chaos Monkey for security

John extends the pattern into security with "Evil Chaos Monkey": tools that constantly try to exploit security holes, fuzz applications with malformed packets, install backdoors, and gain access to confidential data (source: thePhoenixProject.pdf, p. 330). The purpose is to move security from periodic penetration-test theater into continuous evidence about whether the system can resist attack.

Wes initially wants such testing limited to scheduled windows, but Bill argues that continuous fault/security injection is how the Third Way becomes institutionalized: risk-taking, learning from failure, repetition, and practice embedded in daily work (source: thePhoenixProject.pdf, p. 330).

## Connects to

- [[the-three-ways-devops]] - this is the clearest narrative realization of the Third Way: repeated practice, experimentation, and learning from failure.
- [[security-work-and-business-outcomes]] - Evil Chaos Monkey embeds security assurance into daily operations instead of relying only on late reviews.
- [[deployment-pipeline-and-continuous-delivery]] - frequent deployability and reproducible environments make controlled fault injection survivable.
- [[it-work-centers-and-kanban]] - preventive work and improvement cycles need visible capacity, WIP limits, and work lanes to avoid being crowded out.
- [[final-tips-for-success]] - the scalable-systems source also links DevOps automation and observability to resilient operations.
