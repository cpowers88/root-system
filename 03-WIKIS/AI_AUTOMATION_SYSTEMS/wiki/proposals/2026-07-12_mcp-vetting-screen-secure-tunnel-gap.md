---
type: proposal
tags: [ai-automation, proposal, mcp, technology-landscape]
---

# Proposal: Add the Private-Network MCP Gap to the Category 10 Vetting Screen

**Status: APPROVED & APPLIED July 12, 2026** — Chris approved with a wording
revision: folded into the existing "Check for:" list (matching the
document's actual flowing-prose style) rather than a separate bold-header
bullet, and genericized away from naming a single vendor product, since
product names/availability drift (the same ingest that found Secure MCP
Tunnel also found Agent Builder and Prompt objects both sunsetting
November 30, 2026). Applied wording: "...and — when the target system
isn't internet-reachable — whether the vendor has any no-inbound-port
private-network bridge at all; coverage varies by vendor, and specific
offerings should be reverified against current docs rather than assumed
from memory."

## Friction / Drift Observed

`02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` Category 10
already carries an approved agent-tool vetting screen (itself the first
proposal this wiki ever got promoted, July 8, 2026). It currently prices
risk by form factor (chat-with-tools → enterprise agent builder →
browser/computer-use agent) but says nothing about *connectivity* to
private/on-prem systems specifically.

OpenAI ships **Secure MCP Tunnel** — an outbound-only client that lets a
private, non-internet-reachable MCP server receive work by polling OpenAI
for queued requests, rather than exposing an inbound port (see
[[openai-mcp-and-chatgpt-apps]]). No documented Anthropic-side equivalent
was found anywhere in either official docs pack ingested this session
(Claude Code or the MCP spec pages already in this wiki). This is a real,
current ecosystem-maturity gap, not a naming difference — a client audit
question like "can I connect this AI to something behind our firewall
without opening a port" has a materially different answer depending on
vendor, and the existing vetting screen has no line item for it.

## Files Touched

`02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md` — Category 10,
one additional bullet under the existing vetting screen, e.g.:

> **Private-network reachability**: if the target system isn't
> internet-reachable, check whether the vendor has a no-inbound-port bridge
> (e.g. OpenAI's Secure MCP Tunnel) before assuming a workaround is needed —
> this varies by vendor and isn't guaranteed to exist.

## Why Better Than Status Quo

The vetting screen currently has no answer for a connectivity question a
real client engagement could plausibly raise. One bullet closes it without
restructuring anything already approved.

## Risk / Blast Radius

Trivial. One additive bullet to an already-approved section of a
non-governance reference file. No restructuring, no removal of existing
content.

## Source Basis

[[openai-mcp-and-chatgpt-apps]] — Secure MCP Tunnel section.
