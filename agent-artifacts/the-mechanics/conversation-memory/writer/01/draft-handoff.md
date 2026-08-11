# Draft handoff: the-mechanics/conversation-memory (01)

## Original work

This article takes the researcher's separately-owned findings and assembles them
into one backward causal chain — from a single observed behavior (a chatbot
"remembering" something you said several turns earlier) down to the stateless
resend — then derives the blank new chat, the long chat that loses its start, and
the product "memory" feature as consequences of that one fact, marking each rung
settled or product-dependent; the evidence records those as discrete owned claims
but never performs the derivation.

## Proof result

Final `nb check` with links included: `BLOCK: 0  WARN: 0` (PUBLISHABLE). Stamped
words=2197, reading_minutes=10, sources=9 (8 primary, 1 secondary — Hugging Face
KV-cache reference is the one secondary, corroborating the vLLM primary from
outside the vendors whose products the lesson explains).

No warning intentionally left; the earlier W-LENGTH-HIGH (band ceiling 2200) was
resolved by trimming to 2197 words.

## Notes for the editor

- Per the brief's orchestrator correction, the four Background neighbors
  (`the-mechanics/prefill-and-decode`, `the-mechanics/knowledge-cutoff`,
  `the-mechanics/retrieval`, `the-instruments/context-window`) were linked and all
  resolve under the links-included check, overriding the evidence record's
  course-placement note that claimed only `word-order` was published.
- "Memory features store facts outside the weights" is written as reasoning from
  the owned Anthropic context-window and memory-tool pages (the window is working
  memory, marked distinct from the training corpus; saved facts live in files read
  back into the prompt), not as a quotation. The product-memory mechanism is cited
  to the Anthropic memory-tool page, not the gated OpenAI memory FAQ.

## Open question

The only evidence boundary: OpenAI's consumer ChatGPT memory FAQ was gated (HTTP
403) and could not be opened, so no OpenAI-specific product-memory citation is
carried. If the desk later wants one, that page needs a browser-capable fetch by a
human or a new researcher pass; the mechanism itself is sourced firsthand from
Anthropic's memory tool and stands without it.
