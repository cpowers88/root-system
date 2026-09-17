---
type: reference
timeline: reference
status: active
tags: [governance]
---

# Third-Party Notices — Vendored Skills

Skills in `00-BRAIN\SKILLS\` authored outside `.ROOT` and copied in under their
original open-source license. `.ROOT`'s own skills carry no entry here.

## writing-for-agents

- Source: https://github.com/mattpocock/skills (`skills/productivity/writing-for-agents/`)
- Author: Matt Pocock
- License: MIT (Copyright (c) 2026 Matt Pocock)
- Pulled: 2026-08-06, verbatim except frontmatter is unchanged (already
  `name`/`description` only, compliant with `sync_shared_skills.py`).

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## handoff — resolved as original content, not vendored

`mattpocock/skills` had a `handoff` skill (MIT), but its process didn't match
`.ROOT`'s: user-invoked only via `disable-model-invocation: true` (a field
`.ROOT`'s validator doesn't support), saves to the OS temp directory, no
fixed structure. Importing it as-is would have silently gone model-invoked
and conflicted with the existing four-field `HANDOFF_MMDD_WHO.md` convention
`session-close` already enforces (`AGENT.md`, `WHERE_IT_GOES.md`).

Chris's call 2026-08-06: rewrite it to actually follow `.ROOT`'s own
convention instead. `00-BRAIN\SKILLS\handoff\SKILL.md` is the result —
original content (four fields, save path, and frontmatter drawn straight from
`AGENT.md` and the live `HANDOFF_0801_CODEX.md` example, not from the source
repo's text). No MIT text carried over; this entry stays only as the
provenance note for where the idea to add a dedicated handoff skill came
from.
