---
type: template
tags: [later, ai-automation, client]
---

# ENGINEERING PROMPTS TO USE
#AIearlyPrompt 
## Setup
- Create a shared Project named “Engineering”.
- Paste the Master Prompt.
- Edit the variables to match your business.
- Start using prompts below to generate outputs.
## Prompts to Use
### 1. PR Review Summary
- Role: Act as a senior reviewer.
- Context: Repo [REPO]. Stack [STACK]. PR title [TITLE]. Diff notes [NOTES].
- Command: Produce a concise review that surfaces risks, tests to add, and merge readiness.
- Format: Risks, Suggestions, Tests, Merge checklist.
### 2. Bug Triage
- Role: Act as a triage lead.
- Context: Steps to reproduce [STEPS], expected [EXPECTED], actual [ACTUAL], severity [SEV].
- Command: Draft reproducible steps, likely root causes, and a minimal fix plan.
- Format: Repro, Suspects, Fix plan, Acceptance test.
### 3. Doc Update
- Role: Act as a docs scribe.
- Context: Feature [FEATURE], entry points [FILES/LINKS].
- Command: Update README/guide with setup, usage, and examples.
- Format: Section headings with short instructions and example blocks.
### 4. Test Plan Scaffold
- Role: Act as a QA lead.
- Context: Component [COMPONENT], behavior [BEHAVIOR], edge cases [EDGES].
- Command: Outline a pragmatic test plan that prevents regressions.
- Format: Unit cases, Integration cases, Edge cases, Data/fixtures.
### 5. Release Checklist
- Role: Act as a release manager.
- Context: Version [VERSION], envs [ENVS], CI/CD [TOOL].
- Command: Provide a pre-release checklist that is safe and fast.
- Format: Pre-checks, Steps, Rollback notes, Owner.
