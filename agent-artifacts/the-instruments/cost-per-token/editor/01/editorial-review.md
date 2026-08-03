# Editorial review: the-instruments/cost-per-token (editor/01)

## Skeptic

Thesis: a "$X per million tokens" sticker is a rate card, not a bill, so the
same fixed task swings 3.6x on accounting alone and a lower sticker cannot
promise a lower cost. It stands on four load-bearing claims, all of which held.

1. **Opus 5 publishes five per-token prices (the headline).** The body lists
   them: $5 input, $6.25/$10 cache write, $0.50 cache read, $25 output. Five
   distinct rates, matching the evidence's Anthropic pricing entry. The headline
   descriptor is literally true, and it is a finding, not the series' banned
   twin-number reveal.

2. **The five-way worked example.** I recomputed every figure independently from
   the Opus 5 rates (input $5, output $25, cache-hit $0.50, batch $2.50/$12.50,
   cached+batch read $0.25), cost = tokens / 1e6 x rate:
   - (a) input only: 10,000 x 5 / 1e6 = $0.0500
   - (b) input+output: 0.05 + 2,000 x 25 / 1e6 = $0.1000 (output 2,000 of 12,000
     tokens = one sixth, yet half the bill; sticker understates real-time by half)
   - (c) caching: 10,000 x 0.50 / 1e6 (=0.005) + 0.05 = $0.0550
   - (d) batch: 10,000 x 2.50 / 1e6 (=0.025) + 2,000 x 12.50 / 1e6 (=0.025) = $0.0500
   - (e) cached+batch: 10,000 x 0.25 / 1e6 (=0.0025) + 0.025 = $0.0275
   Swing $0.10 / $0.0275 = 3.636 = 3.6x. The "sticker equals batch total" ($0.05)
   coincidence is real. Every number in prose matches. Every rate traces to
   Anthropic's pricing page (s1) and the article dates the figures (retrieved
   early August 2026). No price is printed as permanent.

3. **Output costs 4-8x input across labs.** Table checks: Opus 5 $5/$25 = 5x;
   gpt-5 $1.25/$10 = 8x; Gemini 2.5 Pro $1.25/$10 = 8x (correctly flagged as the
   200k tier, with the >200k $2.50/$15 rise noted); gpt-4o $2.50/$10 = 4x. All
   match the evidence. The autoregressive explanation for the premium is sound
   and links the mechanism lesson.

4. **The misuse pattern.** Kimi K2 ~$0.95/task vs the GPT-5.1-class ~$1.04/task
   at ~half the sticker and ~2x the tokens. The article frames this as "near
   parity rather than the half-price win the sticker advertised" — convergence,
   not a dramatic flip, exactly as the brief requires. The derived line "banked
   about nine [percent]" ($1.04 to $0.95 = 8.65%) is correct and carries no
   adjective judging the buyer. Reasoning tokens: OpenAI's "billed as output
   tokens" (primary, s8) plus CloudZero's 3-10x magnitude (secondary, s9) — the
   billing rule and the estimate are attributed to the right kinds. Discounts:
   correctly stated as conditional.

**Tokenizer scope (brief's focus).** The claim rests only on Anthropic's
first-party "~30% more tokens for the same text" across two Anthropic tokenizer
generations (Opus 4.7+/Fable 5 vs earlier). No cross-vendor fixed-string count is
presented as measured. Scope is honest and matches the evidence's recorded gap.

**Display text.** Headline, dek, and all four subheads verified descriptor by
descriptor. Every model name, price, date, and ratio in display and furniture
traces to its owning primary. The dek makes a world-claim (cost swings 3.6-fold),
complements rather than restates the headline, and grades nothing about method.

**data-nb-kind audit.** All nine correct: s1/s2/s5/s6 Anthropic own the Claude
figures (primary); s3/s4 OpenAI and Google own their prices (primary); s8 OpenAI
owns the reasoning-billing rule (primary); s7 MindStudio and s9 CloudZero report
on prices they do not own (secondary). No independent-source failure hidden by a
label.

**Citation hrefs.** All nine source hrefs are ordinary document URLs (no raw
endpoints, no artifact exception needed). The three internal cross-links resolve
in the library and their anchor texts match the linked articles' real titles
("A transformer never reads the letters in strawberry", "Groq's 270 tokens a
second and Anyscale's 185 are both true"). `nb check` with links returns BLOCK 0.

No claim retired; nothing routed to researcher.

## Cut

One direct cut. The orientation paragraph closed on "The distance between the two
is what this lesson measures" — the piece narrating its own method, which the
house standard bans as self-reference. Removing it lets the earned line "a rate
card, not a receipt" land the paragraph.

Worst tell considered and cleared: the density of "X is not Y" shapes (two
subheads, plus "rate card, not a receipt"). Each corrects a real, named reader
misconception (a price list read as a bill; a token read as a fixed unit; a
sticker read as a bill), and the "rate card, not a receipt" echo between
orientation and takeaway is a deliberate bookend, not a formula. Within the
earned-contrast ceiling; not routed.

No prompt leakage: the pattern framing and the three questions are executed
content, not copied instruction labels. Furniture holds — stat-strip, one table,
the chart, and the "Three questions" note each serve a distinct purpose, all are
catalog components, and the piece correctly avoids the banned Verdict block. The
single output:input table earns its place (substantiates "four to eight times"
with the numbers) and the worked-example steps live in the chart, not a second
table. Two semicolons, both joining tightly-bound clauses; within "rare," left
as the house standard tolerates.

## Chart

`chart-1.py` is committed beside the article with its provenance header stating
the task and rates. Its five costs (0.05, 0.10, 0.055, 0.05, 0.0275) recompute
exactly against the evidence and the cited primary (s1). Read as a reader: the
y-axis is linear from zero, labeled "US$ per run of the task"; each bar carries
its exact dollar value; the caption states the task, the formula, and cites the
data source. No scale distortion, no misleading implication. No correction
requested.

## Reader

Straight through, what the piece gives beyond its sources: a single fixed task
carried through five accounting regimes with each move pinned to one named cause,
plus three portable questions to put to any per-token claim. The sources give
scattered rates; the article gives a repeatable method to read them. That answer
survives, and it matches the draft-handoff's original-work sentence. The prose
sits closer to the voice-guide exemplars (SemiAnalysis's single-anchor
recomputation, Willison's flat cost-calc clause) than a median summary. The
headline as the largest claim holds.

## Edits

- Cut "The distance between the two is what this lesson measures." (self-narration) from the orientation section; re-ran `nb stamp` (words 1759 -> 1749).

## Required work

None.

## Decision

approve — every load-bearing claim recomputes to the evidence and its owning
primary, the chart is honest and its provenance committed, the misuse reads as a
pattern and the tokenizer claim stays in first-party scope, and the one
self-narration line is cut; the article is ready for the deterministic proof.
