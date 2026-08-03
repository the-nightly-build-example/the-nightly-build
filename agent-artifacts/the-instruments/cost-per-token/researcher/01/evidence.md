# Evidence: the-instruments/cost-per-token (researcher 01)

The record strongly supports the commissioned angle: a headline "$X per million
tokens" figure does not tell you the cost of a workload, because the real bill
depends on three things the sticker hides — the input:output split (output is
priced 4–8x higher than input across every lab I checked), whether caching and
batch discounts apply (caching cuts repeated input to 10% of sticker; batch cuts
both sides 50%; the two stack), and which tokenizer counted the text (Anthropic's
own docs state the same text produces ~30% more tokens under its newer tokenizer,
and reasoning models bill "thinking" tokens the user pays for but never sees).
All current per-token prices are confirmed firsthand on each lab's own pricing or
docs page, dated below. The record is thin in two honest places: (1) I could not
run a live tokenizer to produce a controlled fixed-string count under two *named
third-party* tokenizers, so the tokenizer-dependence claim rests on Anthropic's
first-party "~30% more tokens" statement (two Anthropic tokenizers, same text)
plus the model-specific count-tokens tool, not a hand-run cross-vendor demo; and
(2) a single, named, public buyer-decision-that-went-wrong with a dollar figure
for the loss is not cleanly sourceable — I documented the misuse as a *class* with
two dated secondary instances carrying concrete numbers (Kimi K2 vs GPT-5.1 near-
parity despite half the sticker; the o-series reasoning-token cost multiplier),
which is what the brief permits. One important volatility caveat runs through
everything: Claude Sonnet 5 is on introductory pricing that expires 2026-08-31,
and the OpenAI pages carry no visible "last updated" date — every figure is dated
by retrieval (2026-08-03) and by internal page cues.

## Sources

```text
URL:         https://platform.claude.com/docs/en/about-claude/pricing
Kind:        primary — Anthropic is the owner of Claude API prices; this is its own pricing page.
Establishes: The full Claude API price table (base input, 5m/1h cache write, cache hit, output),
             the prompt-caching multipliers, the Batch API 50% discount, and worked cost examples.
Paraphrase:  Per MTok — Claude Opus 5: $5 input / $6.25 (5m write) / $10 (1h write) / $0.50 (cache
             hit) / $25 output. Claude Sonnet 5: $2 / $2.50 / $4 / $0.20 / $10 through 2026-08-31,
             then $3 / $3.75 / $6 / $0.30 / $15 from 2026-09-01. Claude Haiku 4.5: $1 / $1.25 / $2 /
             $0.10 / $5. Claude Fable 5: $10 / $12.50 / $20 / $1 / $50. Batch API is a 50% discount on
             both input and output (Opus 5 batch = $2.50 input / $12.50 output). Caching multipliers:
             5m write 1.25x base input, 1h write 2x, cache hit 0.1x; "these multipliers stack with
             other pricing modifiers, including the Batch API discount." Tokenizer note: "Claude 4.7
             and later models ... use a newer tokenizer ... This tokenizer produces approximately 30%
             more tokens for the same text."
Locators:    Sections "Model pricing", "Feature-specific pricing → Prompt caching", "→ Batch processing".
Quote:       "The Batch API allows asynchronous processing of large volumes of requests with a 50%
             discount on both input and output tokens."
             "Cache read (hit) | 0.1x base input price"
```

```text
URL:         https://platform.claude.com/docs/en/about-claude/models/overview
Kind:        primary — Anthropic's own model catalog.
Establishes: Model IDs, the sticker input/output prices, tokenizer generation, and the Sonnet 5
             introductory-pricing footnote (the volatility flag).
Paraphrase:  Claude Fable 5 ($10/$50, GA 2026-06-09, most capable), Claude Opus 5 ($5/$25), Claude
             Sonnet 5 ($3/$15, with a footnote: "Introductory pricing of $2 / $10 per MTok applies to
             Claude Sonnet 5 through August 31, 2026"), Claude Haiku 4.5 ($1/$5). Legacy table: Opus
             4.8/4.7/4.6/4.5 all $5/$25; Opus 4.1 (deprecated) $15/$75; Sonnet 4.6/4.5 $3/$15. Confirms
             Opus 4.7+ "uses a new tokenizer."
Locators:    "Latest models comparison" table + footnote 4; "Legacy models" accordion.
Quote:       "Introductory pricing of $2 / $10 per MTok applies to Claude Sonnet 5 through August 31, 2026."
```

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/prompt-caching
Kind:        primary — Anthropic's own caching documentation.
Establishes: The exact caching multipliers, independent of the pricing page.
Paraphrase:  5-minute cache write = 1.25x base input; 1-hour cache write = 2x base input; cache read
             (hit) = 0.1x base input. A 5m cache pays off after one read (1.25x + 0.1x < 2x); a 1h
             cache pays off after two reads.
Locators:    Prompt-caching pricing table.
Quote:       "Cache read tokens are 0.1 times the base input tokens price."
```

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/token-counting
Kind:        primary — Anthropic's own tokenizer/counting documentation.
Establishes: That token counts are tokenizer/model-specific and the same text yields different counts
             under different tokenizers — the core tokenizer-dependence claim, firsthand.
Paraphrase:  The count-tokens endpoint returns the count "under the tokenizer of the `model` you pass."
             Claude 4.7+ and Fable 5/Mythos 5 use a newer tokenizer that "produces approximately 30%
             more tokens for the same text" than earlier Claude models; the exact increase depends on
             content. Anthropic instructs: "Recount prompts against the model you plan to use rather
             than reusing counts measured against earlier models." Illustrative tool output: system
             "You are a scientist" + user "Hello, Claude" = 14 input tokens under claude-opus-5.
             Previous-turn thinking tokens do not count as input; current-turn thinking does.
Locators:    "Supported models" note; "Token counts on Claude Fable 5 and Claude Mythos 5" section.
Quote:       "The same input text produces approximately 30 percent more tokens than on earlier models.
             The exact increase depends on the content and workload shape."
```

```text
URL:         https://developers.openai.com/api/docs/pricing
Kind:        primary — OpenAI's own API pricing page (platform.openai.com/docs/pricing 301-redirects here).
Establishes: OpenAI per-MTok prices with a cached-input column and a Batch discount, for the output:input
             premium comparison and the caching-discount question.
Paraphrase:  Per MTok — gpt-5: $1.25 input / $0.125 cached / $10 output (output = 8x input; cached input
             = 10% of input). gpt-5-mini: $0.25 / $0.025 / $2. gpt-4.1: $2 / $0.50 / $8 (output 4x).
             gpt-4o: $2.50 / $1.25 / $10 (output 4x). o1: $15 / $7.50 / $60. o3: $2 / $0.50 / $8. Batch
             API = "50% reduction from Standard rates across all models." Cached input runs 80–90%
             below standard input.
Locators:    Standard pricing tables; "Batch API Discounts"; "Prompt Caching Discounts".
Quote:       "Batch pricing represents a 50% reduction from Standard rates across all models listed."
             NOTE: page shows NO publication or "last updated" date — dated by retrieval 2026-08-03.
```

```text
URL:         https://developers.openai.com/api/docs/guides/reasoning
Kind:        primary — OpenAI's own reasoning-models guide.
Establishes: That reasoning ("thinking") tokens are billed as output tokens the user pays for but does
             not see — the reasoning-token question, firsthand.
Paraphrase:  Reasoning tokens are not returned to the user but occupy the context window and are billed
             as output tokens; their count appears in the response usage object under
             `output_tokens_details`. Optional plain-language reasoning *summaries* are separate from the
             hidden reasoning tokens themselves.
Locators:    "How reasoning works" / billing subsection.
Quote:       "While reasoning tokens are not visible via the API, they still occupy space in the model's
             context window and are billed as output tokens."
             NOTE: no visible page date — dated by retrieval 2026-08-03.
```

```text
URL:         https://ai.google.dev/gemini-api/docs/pricing
Kind:        primary — Google's own Gemini API pricing page.
Establishes: A third lab's prices, including size-tiered sticker pricing (the sticker itself is
             conditional on prompt size), context caching, and a batch discount. Carries an explicit date.
Paraphrase:  Gemini 2.5 Pro is tiered: prompts ≤200k tokens $1.25 input / $10 output; >200k tokens $2.50
             input / $15 output (output = 8x / 6x input). Gemini 2.5 Flash $0.30 / $2.50 (output 8.3x).
             Gemini 3.6 Flash $1.50 / $7.50 (output 5x). Batch mode = 50% discount. Context caching:
             $0.15/MTok input tier + $1.00/hour storage on Flash. "All prices current as of 2026-07-30 UTC."
Locators:    Production-models pricing table; footer date line.
Quote:       "All prices current as of 2026-07-30 UTC."
```

```text
URL:         https://www.cloudzero.com/blog/openai-pricing/
Kind:        secondary — cloud-cost vendor's analysis of OpenAI pricing; reports on prices it does not own.
Establishes: The misuse *pattern*, with concrete multipliers: output >> input, reasoning-token inflation,
             underused caching, and long-context premiums that all make the sticker understate real cost.
Paraphrase:  "Output tokens usually cost 4 to 6 times more than input tokens." o-series models "bill
             internal reasoning tokens at output rates, which can multiply effective costs by 3-10x
             depending on task complexity." Cached tokens can be a 90% discount teams miss. Deep-context
             requests past ~270K tokens trigger a 2x input / 1.5x output premium for the whole session.
Locators:    "Every Model Compared" body sections.
Quote:       "o-series models also bill internal reasoning tokens at output rates, which can multiply
             effective costs by 3-10x depending on task complexity."
             Publication: CloudZero. Date: July 10, 2026, "last updated July 29, 2026."
```

```text
URL:         https://www.mindstudio.ai/blog/ai-token-cost-optimization-strategy
Kind:        secondary — vendor blog; reports a benchmark it ran, not a price it owns.
Establishes: A concrete instance of sticker ordering failing on effective cost: a model with half the
             per-token price cost about the same per completed task because it emitted ~2x the tokens.
Paraphrase:  On their benchmark, Kimi K2 averaged ~$0.95 per completed task vs ~$1.04 for a GPT-5.1-class
             model, even though Kimi K2's per-token sticker is ~half the GPT model's — because Kimi K2
             "tends to take roughly twice as many tokens to solve the same task." Also: output tokens
             cost far more than input, so the output-heavy execution stage is where a cheaper model saves
             most.
Locators:    "Token density" / benchmark section.
Quote:       "Kimi K2's per-token price is roughly half that of the GPT model, but it tends to take
             roughly twice as many tokens to solve the same task. Half the price times twice the tokens
             nets out to roughly the same total cost."
             Publication: MindStudio Blog. Date: July 24, 2026.
```

Source count: 9 total — 7 primary (Anthropic pricing, Anthropic models overview,
Anthropic prompt-caching, Anthropic token-counting, OpenAI pricing, OpenAI
reasoning guide, Google Gemini pricing), 2 secondary (CloudZero, MindStudio).
Floor (>=8 total, >=4 primary, >=1 secondary) met.

## Contradictions

- **The sticker does not always mislead in the direction "cheap looks cheap but
  is expensive."** The MindStudio Kimi K2 case shows the opposite of a dramatic
  reversal: half the sticker price netted to *near parity* on effective cost
  ($0.95 vs $1.04), not a flip. So the honest claim is "the sticker is not a
  reliable predictor of effective cost," not "the cheap model is always secretly
  the expensive one." A writer must not overclaim a reversal.

- **"Output dominates the bill" depends on the workload's mix, and can invert.**
  Output is priced 4–8x higher *per token*, but classification/extraction/RAG
  workloads emit very few output tokens against a large input, so input dominates
  there; long-generation and reasoning workloads are where output dominates. The
  worked example below shows a case where input and output cost are *equal*. The
  general rule is "you must know the mix," not "output is always the bigger line."

- **Caching and batch discounts are conditional, so a comparison that assumes
  them can mislead too.** Anthropic's caching only helps on repeated prefixes
  (≥ the model's cacheable minimum); batch (both labs, 50%) requires tolerating
  asynchronous, non-real-time processing. Interactive, latency-sensitive, or
  unique-prompt workloads get neither. A vendor quoting the cached or batch rate
  is as one-sided as one quoting input-only.

- **The sticker itself can be conditional on prompt size.** Google's Gemini 2.5
  Pro has two-tier pricing (≤200k vs >200k tokens: $1.25→$2.50 input, $10→$15
  output), and OpenAI (per CloudZero) applies a long-context premium past ~270K
  tokens. So even "the sticker price" is not always a single number.

- **Dating risk / freshness.** Claude Sonnet 5's $2/$10 is *introductory* and
  reverts to $3/$15 on 2026-09-01 — an article published in August 2026 will be
  stale within weeks. The two OpenAI pages carry no visible date at all. This is
  the record's single most important limitation: price figures rot fast.

## Numbers

```text
Figure: Claude Opus 5 — $5.00 / MTok input, $25.00 / MTok output (output = 5x input)
Owner:  Anthropic (platform.claude.com/docs/en/about-claude/pricing)
Scope:  Per 1,000,000 tokens, standard real-time API, retrieved 2026-08-03
```
```text
Figure: Claude Opus 5 — cache hit $0.50 / MTok (0.1x input); 5m cache write $6.25 (1.25x); 1h write $10 (2x)
Owner:  Anthropic (pricing + prompt-caching docs)
Scope:  Per 1,000,000 tokens; multipliers relative to $5 base input
```
```text
Figure: Claude Opus 5 — Batch API: $2.50 / MTok input, $12.50 / MTok output (50% of sticker)
Owner:  Anthropic (pricing doc, Batch processing table)
Scope:  Per 1,000,000 tokens, asynchronous batch tier
```
```text
Figure: Claude Sonnet 5 — $2.00 in / $10.00 out (introductory, through 2026-08-31); $3.00 / $15.00 from 2026-09-01
Owner:  Anthropic (pricing doc + models overview footnote 4)
Scope:  Per 1,000,000 tokens; output = 5x input in both regimes
```
```text
Figure: Claude Haiku 4.5 — $1.00 in / $5.00 out; Claude Fable 5 — $10.00 in / $50.00 out (both 5x)
Owner:  Anthropic (pricing doc)
Scope:  Per 1,000,000 tokens
```
```text
Figure: OpenAI gpt-5 — $1.25 in / $0.125 cached in / $10.00 out (output = 8x input; cached = 0.1x input)
Owner:  OpenAI (developers.openai.com/api/docs/pricing)
Scope:  Per 1,000,000 tokens, standard tier; Batch = 50% off; page undated, retrieved 2026-08-03
```
```text
Figure: OpenAI gpt-4o — $2.50 in / $1.25 cached / $10.00 out (output = 4x); gpt-4.1 — $2 / $0.50 / $8 (4x); o1 — $15 / $7.50 / $60 (4x)
Owner:  OpenAI (same page)
Scope:  Per 1,000,000 tokens
```
```text
Figure: Google Gemini 2.5 Pro — ≤200k tokens: $1.25 in / $10 out (8x); >200k: $2.50 in / $15 out (6x)
Owner:  Google (ai.google.dev/gemini-api/docs/pricing), "current as of 2026-07-30 UTC"
Scope:  Per 1,000,000 tokens; size-tiered; Batch mode = 50% off
```
```text
Figure: Google Gemini 2.5 Flash — $0.30 in / $2.50 out (output = 8.3x input); Gemini 3.6 Flash — $1.50 / $7.50 (5x)
Owner:  Google (same page)
Scope:  Per 1,000,000 tokens
```
```text
Figure: Output:input price premium across labs = 4x to 8x
Owner:  Derived from Anthropic, OpenAI, Google pricing pages above
Scope:  Ratio of output $/MTok to input $/MTok, current frontier text models
```
```text
Figure: Tokenizer effect — same text yields ~30% MORE tokens under Claude's newer (Opus 4.7+/Fable 5) tokenizer vs earlier Claude tokenizer
Owner:  Anthropic (token-counting doc; pricing-doc note)
Scope:  Same input text, two Anthropic tokenizer generations; exact increase content-dependent
```
```text
Figure: Reasoning tokens billed as OUTPUT tokens, invisible to the user; effective-cost multiplier ~3–10x depending on task
Owner:  Billing rule: OpenAI reasoning guide (primary). Magnitude "3–10x": CloudZero (secondary).
Scope:  o-series / reasoning models; multiplier is task-complexity-dependent, secondary estimate
```
```text
Figure: Misuse instance — Kimi K2 ~$0.95 / task vs GPT-5.1-class ~$1.04 / task despite Kimi's ~half sticker price (≈2x tokens per task)
Owner:  MindStudio (secondary, benchmark they ran), July 24, 2026
Scope:  Their internal benchmark, per completed task
```

### Worked example (exact arithmetic; writer/editor can recompute)

Fixed task, held constant across all accounting choices:
**a 10,000-token input (e.g. a document + question) that produces a 2,000-token
answer, on Claude Opus 5**, run many times over the SAME 10,000-token context.
Opus 5 rates (per MTok): input $5, output $25, cache-hit $0.50, batch input $2.50,
batch output $12.50. Cost = tokens ÷ 1,000,000 × rate.

- **(a) Sticker / input-rate-only (the naive quote):**
  10,000 × $5 / 1,000,000 = **$0.0500**. (Ignores output entirely.)

- **(b) Correct input + output, real-time, uncached:**
  input 10,000 × $5/1e6 = $0.0500; output 2,000 × $25/1e6 = $0.0500;
  total = **$0.1000**. Output is 2,000 of 12,000 tokens (17%) but **half** the
  cost — and the input-only sticker (a) understated the true real-time cost by 2x.

- **(c) With prompt caching on the repeated context (warm call, cache hit):**
  cache-read input 10,000 × $0.50/1e6 = $0.0050; output 2,000 × $25/1e6 = $0.0500;
  total = **$0.0550**. Caching collapsed the input line 10x ($0.0500 → $0.0050);
  output now dominates at 91% of the bill.

- **(d) With Batch API (50% off both), uncached:**
  input 10,000 × $2.50/1e6 = $0.0250; output 2,000 × $12.50/1e6 = $0.0250;
  total = **$0.0500**.

- **(e) Caching + batch stacked (0.1x × 0.5 = 0.05x base input on reads):**
  cache-read 10,000 × $0.25/1e6 = $0.0025; output 2,000 × $12.50/1e6 = $0.0250;
  total = **$0.0275**.

Swing on one fixed task: the correct real-time cost **$0.1000** is **3.6x** the
fully-optimized cost **$0.0275**; the input-only "sticker" **$0.0500** is exactly
**half** the true real-time number yet, by coincidence, equals the batch total —
a clean illustration that the headline number is not a cost. (Add the tokenizer
dimension to taste: if the 10,000-token count were estimated with a *different*
tokenizer than the one that bills, every figure above shifts proportionally —
Anthropic quotes ~30% for a tokenizer change.)

## Source assets

```text
Asset: Anthropic "Model pricing" table (platform.claude.com/docs/en/about-claude/pricing),
       columns Base Input | 5m Cache Writes | 1h Cache Writes | Cache Hits & Refreshes | Output.
Shows: In one grid, that a single model carries five different per-token prices — the strongest
       single visual for "there is no one price."
Crop:  Keep the column headers and the Opus 5 + Sonnet 5 + Haiku 4.5 rows; the Fable/legacy rows can
       be omitted. Do not crop away the cache columns — they are the point.
```
```text
Asset: The worked-example five-line cost breakdown (above), rendered as a bar/waterfall of $0.05 →
       $0.10 → $0.055 → $0.05 → $0.0275 for the identical task.
Shows: The cost swing on ONE fixed task across accounting choices — the commission's required visual.
Crop:  Label each bar with its accounting choice; keep the exact dollar figures visible.
```
```text
Asset: A small output:input premium table across labs (Opus 5 5x, gpt-5 8x, Gemini 2.5 Pro 8x/6x,
       gpt-4o 4x), built from the three pricing pages.
Shows: That output is universally 4–8x input — the reason input-only quotes systematically understate.
Crop:  Two columns (input $, output $) plus the ratio; one row per model.
```
```text
Asset: None found for the tokenizer claim beyond prose — Anthropic states "~30% more tokens" in text,
       with no chart. A writer could build a simple two-bar "same sentence, two tokenizers" figure,
       but I have no firsthand controlled count to populate it (see Discarded).
Shows: —
Crop:  —
```

## Discarded

```text
URL: https://www.anthropic.com/pricing — 301-redirects to claude.com/pricing; the marketing page
     shows only consumer plan tiers (Free/Pro/Max), no per-MTok API prices. Superseded by the docs
     pricing page, which owns the numbers.
```
```text
URL: https://claude.com/pricing and https://claude.com/pricing#api — marketing page; returned only
     consumer/enterprise plan copy, not the API per-token table. The docs pricing page is the primary
     that owns the figures.
```
```text
URL: https://platform.claude.com/docs/en/pricing.md — 404 (wrong path). Correct primary is
     /docs/en/about-claude/pricing.
```
```text
URL: https://openai.com/api/pricing/ — 403 Forbidden via fetch. platform.openai.com/docs/pricing
     301-redirects to developers.openai.com/api/docs/pricing, which is the resolvable primary used above.
```
```text
CLAIM DISCARDED (not sourced firsthand): "o3-mini generates 110M completion tokens, 11.7x more than
     GPT-4o-mini." Surfaced only in a web-search synthesis, not on a page I opened; not cited. The
     reasoning-inflation magnitude is instead carried by CloudZero's firsthand "3–10x" and OpenAI's
     own "billed as output tokens" statement.
```
```text
GAP (recorded, not resolved): No live, controlled fixed-string token count under two NAMED third-party
     tokenizers (e.g. Claude vs a GPT tokenizer). I could not run a tokenizer in this environment. The
     tokenizer-dependence claim is therefore anchored on Anthropic's first-party "~30% more tokens for
     the same text" (two Anthropic tokenizer generations) and the model-specific count-tokens tool —
     sufficient to establish the principle, but the writer should not present a specific cross-vendor
     per-string number as measured.
```
