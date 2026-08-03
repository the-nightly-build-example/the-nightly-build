# Commission: the-instruments/cost-per-token

## Assignment
Teach how the number "$X per million tokens" is made and what it can and cannot
support. This is the the-instruments desk: one measurement used in public to
compare AI systems, explained step by step (who produces it, from what, by what
procedure), then at least one real case where the number misled people and what
that cost.

## Why this measurement, now
Dollar cost per token is the number every buyer, journalist, and lab uses to
compare model economics, and it is quietly the most gameable comparison on the
board. Published price lists put one headline figure next to a model name, but
the real cost of a workload depends on the split the price list hides: input
tokens are billed at one rate and output tokens at another (often 3–5x higher),
prompt caching and batch tiers cut the input rate sharply, and "tokens" are not
a fixed unit — a different tokenizer counts the same text differently.

## Angle and required contribution
The one act of original work: take a single, fixed real task and show its cost
swing by a large factor across defensible accounting choices, isolating each
choice (input vs output rate; cached vs uncached input; batch vs real-time;
tokenizer differences; reasoning/"thinking" tokens the user pays for but never
sees). The reader should leave able to look at any "$X/M tokens" comparison and
ask the three questions that decide whether it means anything.

## Teach these, completely (2–3 ideas, not six)
1. What a token is here and why the count is not fixed (tokenizer dependence);
   input tokens vs output tokens and why output is priced higher.
2. The blended/effective cost of a real workload vs the headline sticker: work
   a concrete example with real published per-token prices and a realistic
   input:output ratio; show cached-input and batch discounts moving it.
3. The misuse case: a specific public comparison (or a class of them) that
   ranked models on a headline price and got the real-cost ordering wrong, plus
   the cost of that error to whoever relied on it.

## Boundaries
- One lesson, lesson template, 1200–2200 words. No code.
- Distinct from the published the-instruments pieces on energy-per-query
  (energy, not dollars) and tokens-per-second (speed, not dollars): this is the
  dollar-price axis. Do not re-teach what a benchmark is; teach what a price is.
- Use real, currently-published prices, dated. Do not invent numbers.

## Source policy (from `nb source-policy --series the-instruments`)
- Minimum 8 sources; primary >= 4, secondary >= 1.
- Primary = the labs' own pricing pages and tokenizer docs (OpenAI, Anthropic,
  Google) as the owners of their prices; batch/caching documentation; any
  first-party spec that owns a number. Secondary = analyst/journalist
  comparisons, ideally the ones that got it wrong (as the misuse case).

## Production policy (from `nb production-policy --series the-instruments`, profile balanced)
- writing-coach: capable / low  → claude (sonnet)
- researcher: capable / high     → claude (opus, claude-opus-4-8)
- writer: capable / medium       → claude (opus, claude-opus-4-8)
- editor: capable / high         → claude (opus, claude-opus-4-8)
No `required` directive; capable tier honored, no deviation.

## Tags
No tag prompt-fragments configured for this series; ships with empty tag list.

## This edition's neighbors (keep distinct, one paper)
Runs tonight with the-evidence/alphafold, the-mechanics/prefill-and-decode,
what-could-go-wrong/self-replication, when-ai-breaks/amazon-hiring-tool. Nearest
neighbor is prefill-and-decode (also touches tokens and inference), but that
piece is about *latency mechanism*; this one is about *dollars*. Keep the seam
clean: do not explain the decode loop here beyond the one sentence needed to say
why output tokens cost more to produce.

## Recent shapes in this series to break (do not inherit)
The series overuses the twin-number reveal headline: "both are true" /
"the same X scored A and B" (tokens-per-second, arc-agi, aime, bleu). Do not
headline this with a "two prices are both true" twin. Avoid the comma-triad and
semicolon-reversal deks.
