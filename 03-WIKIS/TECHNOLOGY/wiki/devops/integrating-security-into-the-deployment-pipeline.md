---
domain: tech
type: concept
tags: [subject/devops, subject/security, subject/devsecops]
timeline: later
status: wiki-only
---

# Integrating Security into the Deployment Pipeline (DevSecOps)

**Summary**: The Handbook's Part VI treatment of security — Twitter's
Infosec team integrating automated vulnerability scanning directly into
the developer build process (a 60% reduction in found vulnerabilities),
and the software-supply-chain risk of inherited dependencies. More
technical/mechanical than [[security-work-and-business-outcomes]]'s
narrative treatment of the same Third Way idea via "Evil Chaos Monkey."

**Sources**: DEvOpsHandbook.pdf (Kim, Humble, Debois, Willis, *The DevOps
Handbook*, 2016), Part VI, "Integrating Security..." chapters

**Last updated**: 2026-07-13

---

## The Twitter Case Study — Integrating Scanning Into the Build

Following a 2010 FTC consent decree (20-year information-security
compliance obligation after intrusion incidents), Twitter's Infosec team
had to solve a specific, recurring failure mode: the same code
vulnerabilities kept getting reintroduced, because the existing process
was "run a scanner, generate a huge PDF report, email it to someone in
Development" — too slow, too disconnected from the actual point of
failure, and too easy to ignore or lose track of.

Their stated design goals, directly transferable as a checklist for any
security-integration effort:
- **Prevent the same mistake from repeating** — fix the system of work,
  not just the individual defect.
- **Integrate into tools developers already use** — give the developer
  who introduced the vulnerability the exact fix information at the point
  of work, not a report routed elsewhere.
- **Preserve Development's trust** — false positives cost credibility;
  track and fix the scanner's own error rate, don't just tolerate noise.
- **Automate to keep Infosec's own flow fast** — manual wait-scan-
  interpret-route cycles don't scale and don't get redone when code
  changes.
- **Make security self-service** — assume good intent; give people the
  context to fix their own issues rather than gatekeeping.

**The mechanism**: during a company hack week, Twitter integrated
Brakeman (a Ruby-on-Rails static vulnerability scanner) directly into the
build process — scanning at the earliest development stage, not at
commit time. Result: a **60% reduction** in vulnerabilities found over
subsequent years, because developers got fast, specific feedback exactly
where and when they wrote the insecure code, the same fast-feedback logic
[[deployment-pipeline-and-continuous-delivery]] already applies to
functional test failures, just applied to security.

## Software Supply Chain Risk

Josh Corman's framing, quoted directly: "we are no longer writing
customized software — instead, we assemble what we need from open source
parts." Every dependency inherited is also every dependency's
vulnerabilities inherited. The practical response: track which
components/libraries a project depends on, prefer ones with a
demonstrated history of fast vulnerability fixes, and watch specifically
for multiple/older versions of the same library coexisting in production
(a common way old, patched vulnerabilities silently persist). The 2014
Verizon PCI Data Breach Investigation Report figure cited: ten known CVEs
accounted for nearly 97% of the breaches studied — the exploited
vulnerabilities were overwhelmingly *known and unpatched*, not novel
zero-days.

## Why This Matters Beyond the Phoenix Project's Version

[[security-work-and-business-outcomes]] already covers this wiki's
existing security material, but via the Phoenix Project's narrative
"Evil Chaos Monkey" framing (continuous penetration-style attack
practice against test/production). This page covers a different,
earlier-in-the-pipeline practice: catching vulnerabilities *before* they
ship, via automated scanning integrated into the build itself, rather
than finding them after deployment via adversarial testing. The two are
complementary stages of the same DevSecOps posture (shift-left detection
+ continuous adversarial validation), not competing approaches.

## Connects to

- [[security-work-and-business-outcomes]] — the existing narrative
  security page (Evil Chaos Monkey / continuous adversarial testing);
  this page is the earlier-stage, build-integrated detection practice.
- [[deployment-pipeline-and-continuous-delivery]] — the same fast-
  feedback-at-commit-time logic already covered for functional tests,
  here applied to static security scanning.
- [[devops-reading-map]] — no prior entry covers software-supply-chain
  risk; this closes that gap.

## North Star Connection

Direct, concrete audit item for any client shipping custom software: "do
you know what open-source components you depend on, and are any of them
carrying known CVEs" is a specific, answerable diagnostic question — and
the Twitter case study's design checklist (fix the system not the
instance, integrate into existing tools, preserve trust via low false
positives, automate, make it self-service) is directly reusable for
recommending *any* new tooling to a client team, not just security
scanners.
