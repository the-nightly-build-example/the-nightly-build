# Draft handoff: the-instruments/cost-per-token (writer 01)

## Original work (one sentence)

The article takes one fixed task — a 10,000-token input answered in 2,000
tokens on Claude Opus 5 — and prices it five ways from the model's own
published rates, isolating each accounting choice as a single named cause that
moves the cost (counting output, cache hit, batch, and the two stacked), so
the 3.6x swing from $0.10 real-time to $0.0275 reads as five deliberate
decisions rather than five numbers, then distills that into the three questions
a reader can put to any "$X per million tokens" claim. The work is visible in
the worked-task section, its chart, and the "Three questions" note.

## Proof result

Final `nb check` (series the-instruments, links included): **BLOCK: 0, WARN: 0,
verdict PUBLISHABLE**. `nb stamp` written (words 1759, reading 8 min, sources 9;
7 primary / 2 secondary, floor met). No warnings left standing. Chart rendered
with `nb chart` and inspected; `chart-1.py` provenance committed beside the
article. No source asset used (the researcher recorded no firsthand controlled
tokenizer count, so no captured visual was warranted).

## Notes on decisions the brief flagged

- Misuse handled as a **pattern**, not a single dollar-loss incident. The Kimi
  K2 case is stated as near-parity ($0.95 vs $1.04 per task, ~half sticker, ~2x
  tokens), explicitly "not the half-price win the sticker advertised" — no flip
  overclaimed. Reasoning-token and caching/batch conditionality carry the rest
  of the pattern.
- Tokenizer-dependence rests on Anthropic's first-party "~30% more tokens"
  across two Anthropic tokenizer generations; no cross-vendor per-string count
  is presented as measured.
- Every price is dated (early August 2026) and the Sonnet 5 introductory
  $2/$10-reverting-to-$3/$15-on-2026-09-01 example carries the volatility point
  concretely (source 2).

## Open questions for the orchestrator

- **Publication timing / freshness (evidence caveat, not a blocker):** the
  researcher's single biggest limitation is that these prices rot fast — Sonnet
  5's introductory rate reverts 2026-09-01, and the two OpenAI pages carry no
  visible "last updated" date. The article dates every figure and names the
  reversion, but if this ships at/after the September price change the Sonnet 5
  sentence and the "lists $2 and $10 today" phrasing will need a same-day check.
- No named-buyer dollar-loss exists to source (recorded as a gap by the
  researcher); if the editor wants a harder-hitting misuse consequence, that
  requires new researcher evidence, not writer invention.
