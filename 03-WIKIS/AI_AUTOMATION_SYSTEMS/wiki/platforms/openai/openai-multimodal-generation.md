---
type: research
timeline: reference
tags: [ai-automation, openai, vision, image-generation, audio, voice-agents]
source: raw/OPEN_AI-CHATGPT_CODEX_FILES/ (OpenAI official docs, moved from CASTLE raw/ to this wiki July 12, 2026 — "Images and vision  OpenAI API.md", "Image generation  OpenAI API.md", "Audio and speech  OpenAI API.md", "Voice agents  OpenAI API.md")
---

# OpenAI Multimodal Generation — Vision, Image, Audio, and Voice Agents

**Official OpenAI documentation, read in full July 12, 2026.** Companion to
[[openai-model-lineup-and-selection]], which covers text/model selection
from the same docs pack. No `.ROOT` use case exists for any of this today
(text-only, Windows-based system) — recorded as landscape inventory for
if/when a proof project needs multimodal input or output.

## One-paragraph summary

OpenAI splits multimodal work into three independent capability axes —
vision (image *understanding*, via the `detail` parameter and per-model
patch-budget tokenization), image generation (`gpt-image-2`/`1.5`/`1`/
`1-mini`, invoked as a Responses API tool, not a standalone model field),
and audio (four modalities — audio in, audio out, transcript, and
text-prompt-to-speech — split into request-based APIs for file/bounded
work vs. realtime sessions for live low-latency work) — each with its own
model-support matrix and cost mechanics, so "does this model support X" is
never a single yes/no across the whole product line.

## Vision — image understanding

- **Three APIs, three use cases**: Responses API (analyze + optionally
  generate), Images API (generate only, image input optional), Chat
  Completions (analyze → text or audio out).
- **`detail` parameter** (`low`/`high`/`original`/`auto`) controls
  processing cost and fidelity. On GPT-5.6 and `gpt-5.5`, **`auto` and the
  omitted default both now mean `original`** (full input dimensions, no
  resize to a patch/pixel budget) — a change from `gpt-5.4` and earlier,
  where omitted/`auto` meant `high`. This is a real behavior change worth
  knowing before assuming "just don't set detail" is safe across model
  versions — large images under `original`/`auto` on GPT-5.6 can cost
  *more* tokens than the same image did on older models.
- **Patch-based tokenization** (GPT-5.6/5.5/5.4 family): images are
  covered in 32×32px patches; cost = patch count × a per-model multiplier
  (1.62–2.46× for mini/nano tiers). Formula given precisely enough to
  budget from: `patches = ceil(width/32) × ceil(height/32)`, then scaled
  down proportionally if it exceeds the model's patch budget. Older
  models (GPT-4o family, computer-use-preview, most o-series) use a
  simpler tile-based scheme instead (base tokens + per-512px-tile tokens).
- **Named limitations**: not for medical images (CT scans etc.), weak on
  non-Latin text, struggles with rotated text, dashed/dotted line charts,
  precise spatial localization (e.g. chess positions), panoramic/fisheye
  images, and exact object counts (approximate only). CAPTCHAs are
  blocked outright for safety reasons.
- **Input limits**: PNG/JPEG/WEBP/non-animated GIF only, ≤512MB total
  payload, ≤1,500 images per request, no watermarks/logos/NSFW content.

## Image generation

- **`gpt-image-2`** is the current state-of-the-art generation model —
  invoked via the Responses API `image_generation` tool (not a `model`
  field value; you call a text model like `gpt-5.6` *with* the tool, and
  the tool itself routes to a GPT Image model under the hood).
- **Configurable per-call**: size, quality (low/medium/high), format,
  compression (0-100% for JPEG/WebP), background (transparent/opaque —
  `gpt-image-2` does NOT support transparent, that request fails
  outright), and `action` (auto/generate/edit).
- **Automatic prompt revision**: the mainline model rewrites the prompt
  before generation; the rewritten version is returned in
  `revised_prompt` — useful for debugging why an image didn't match
  intent.
- **Multi-turn editing** via `previous_response_id` — "now make it look
  realistic" as a follow-up call, no need to re-describe the whole image.
- **Streaming partial images** (`partial_images: 1-3`) for progressive
  visual feedback during generation — a UX pattern, not just a backend
  detail.
- Editing prompts should use `edit`/`draw`-style verbs ("edit the first
  image by adding X from the second") rather than `combine`/`merge`,
  which the docs say work less reliably.

## Audio — four-modality vocabulary

The audio guide's real contribution is a shared vocabulary that
disambiguates otherwise-overloaded terms:

| Task | What it does |
|---|---|
| Speech to text | speech → text (captions, transcripts, search) |
| Text to speech | text → spoken audio (narration, assistants) |
| Speech to speech | listen + reason + speak in one low-latency session (conversational voice agents) |
| Speech translation | speech in language A → translated speech/transcript in language B |

**Two architectures, not a spectrum**: request-based APIs (bounded file
or text input — simpler, no live interaction) vs. realtime sessions (live
audio, low-latency partial events, WebRTC/WebSocket transport). Natively
multimodal models (`gpt-realtime-2.1`, `gpt-audio-1.5`) understand and
generate both audio and text directly; Chat Completions can also be
extended with `modalities: ["text","audio"]` for an existing text-only
chat app that needs to add spoken input/output without a full realtime
rebuild.

## Voice agents — two architecture choices, not a default

| Architecture | Best for | Trade-off |
|---|---|---|
| Speech-to-speech (live audio session, `RealtimeAgent`/`RealtimeSession`) | Natural, low-latency, barge-in-capable conversation | Model handles audio directly — less visibility into intermediate text |
| Chained pipeline (STT → text agent → TTS, `VoicePipeline`) | Support flows, approval-heavy flows, reusing an existing text agent | Full control/visibility at each stage, but more integration surface |

Voice agents reuse the *same* SDK building blocks as text agents (tools,
handoffs, guardrails, orchestration) — only the transport layer changes.
TypeScript's fastest path is `RealtimeAgent`/`RealtimeSession` (browser,
WebRTC); Python's simplest path to extend an existing text agent is the
chained `VoicePipeline`. This voice surface is explicitly noted as
SDK-first, not the (deprecated) Agent Builder path.

## Why this matters for this wiki / `.ROOT`

- **Honest finding: no current relevance.** `.ROOT` is a text-only,
  document-based system; nothing here changes current practice. Recorded
  purely as inventory-depth landscape for a future multimodal proof
  project (e.g., a client-facing tool that needs image/voice input).
- **The `detail: auto` behavior change (GPT-5.6 vs. GPT-5.4) is the one
  fact worth remembering** even without a current use case — it's the
  kind of silent-default-shift that breaks a working integration on model
  upgrade, exactly the class of thing `.ROOT`'s "verify live models,
  prices, limits before implementation" recheck rule (already in the
  CASTLE source-summary) exists to catch.
- **Voice agents reusing the text-agent SDK core** is a reminder that
  modality is a transport-layer decision, not an architecture-layer one —
  relevant framing if a future client audit ever needs to explain "can we
  add voice to what you already built" in plain terms.
- Companion page: [[openai-model-lineup-and-selection]] covers the
  model-selection and prompting-technique material from the same pack.

---
*Processed July 12, 2026. Source in raw/ (immutable).*
