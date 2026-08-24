# Editorial review: the-mechanics/first-token-latency (editor/01)

## Skeptic

Thesis: the pause before a chatbot's first word barely tracks the prompt's
length at the lengths people actually type, and any published TTFT figure is a
sum of four separable costs -- new compute the prompt demands, load from other
users on the GPU, prefill skipped for a cached prefix, and the network round
trip.

The claims it stands on, and how each held:

1. **At ordinary prompt lengths one input token is worth about a hundredth of an
   output token.** This carries the headline, the dek, and the whole
   prompt-length section. Anyscale's Llama 2 70b regression gives 0.3-0.7 ms per
   input token against 30-60 ms per output token and a scatter with no visible
   input-length trend from 250 to 800 tokens. I opened the Anyscale post: the
   figures, the ~1% ratio, and the no-relationship scatter are all there as
   stated. Central claim, first-hand primary, holds. (Two quotation defects in
   this section, fixed below.)

2. **Attention is O(n^2 * d) per layer and the crossover with the linear
   O(n * d^2) term sits near n = d, several thousand tokens for today's models.**
   The conclusion is sound and the threshold is right: n^2 * d exceeds n * d^2
   only when n exceeds d. But the article attributes the arithmetic to Vaswani's
   Table 1 in a way the table does not support. Table 1 lists self-attention at
   O(n^2 * d) and the *recurrent* layer at O(n * d^2); it has no feed-forward row
   and no query/key/value-projection row. The draft writes that "Table 1 gives
   the per-layer arithmetic of a Transformer... the position-wise feed-forward
   and the query, key, and value projections cost O(n * d^2)," and then borrows
   Vaswani's self-attention-versus-recurrent sentence ("faster than recurrent
   layers when the sequence length n is smaller than the representation
   dimensionality d") to justify a claim about attention versus feed-forward
   inside one transformer. Those are two different comparisons that happen to
   share the n < d threshold. A reader who opens Table 1 to check will not find
   the feed-forward or projection costs there. The underlying fact (FFN and
   projections are linear in n at O(n * d^2)) is standard, but it is not in the
   cited source, and the evidence record repeats the same misattribution in its
   Numbers block. Routed: the researcher supplies a primary that states the
   feed-forward/projection per-layer cost, or confirms the argument should rest
   only on what Table 1 actually says; the writer then recasts so the article
   stops sourcing the linear term to Table 1. Recurs once more in the
   long-context section ("the regime in which the n^2 attention term outweighs
   the n * d^2 feed-forward term").

3. **Past a few tens of thousands of tokens the pause bends upward super-
   linearly.** NVIDIA's GH200 NVL32 Llama 3.1 70B benchmark, relayed by Wallace
   for Redis: 472 ms at 32,768 tokens, ~2.2 s at 122,880, so 3.8x the prompt for
   4.7x the wait. I opened the Redis post; the numbers and the "TTFT grew faster
   than the prompt itself" line are as quoted, and the post links the NVIDIA
   developer blog as the owner. The article states plainly that the measurement
   is NVIDIA's and Redis is the relay, and source 5 is filed secondary with a
   data-nb-note naming NVIDIA. This is the "yes, but at extreme lengths"
   counterweight, not the spine of the piece -- the spine (ordinary lengths)
   rests on Anyscale, a first-hand primary. Per the brief's own test, a
   supporting-not-central claim may stand on the relayed source. It stands; no
   route.

4. **One user's new prefill degrades every streaming user's decode, and the
   serving levers each touch only one side of the pause.** DistServe: a fresh
   prefill added to a decode batch stretches TPOT, "the slowdown intensifies
   with a longer prefill." Sarathi: a 512-token prefill saturates an A6000 at
   batch 1, and decode per token runs up to ~200x prefill per token. Speculative
   decoding (Leviathan, 2x-3x on T5-XXL) speeds decode and leaves prefill
   untouched; chunked prefill "trades TTFT for TPOT." All check against the
   evidence record. But the draft's own prose reversed one of these: it wrote
   "Prefill cost per token dwarfs decode cost per token" one clause before
   quoting that decode per token is ~200x prefill per token. The sentence
   contradicts the quote it introduces and states the direction backwards. Fixed
   directly (below): the mechanism that makes decodes wait is prefill saturating
   the GPU's compute, not a per-token cost that runs the other way.

5. **A cached prefix skips the prefill it already paid for.** PagedAttention's
   block sharing, with Kwon et al.'s 12%-of-KV-memory prompt-sharing figure.
   Quote and figure match the record; label primary is correct (the vLLM authors
   built and measured the system). Holds.

6. **A vendor's TTFT includes the network; academic prefill time does not.**
   Artificial Analysis holds up: I opened it and it says TTFT "is sensitive to
   server location" and "includes network latency," measured from a
   us-central1-a VM. The companion claim that "Anthropic's latency documentation
   lists network latency among the factors" does not hold: I opened that page and
   it names "the size of the model, the complexity of the prompt, and the
   underlying infrastructure supporting the model and point of interaction." The
   word network does not appear. The evidence record's Contradictions section
   asserts Anthropic lists network latency; the source disagrees, so I routed it
   rather than settling it. The network point itself survives on Artificial
   Analysis alone, so the repair is small.

Display text, descriptor by descriptor: the headline is a claim the piece
defends. The dek makes a claim about the world (the Anyscale ratio and the
long-context regime), not a grade of the article's method. Every section subhead
reconstructs a real step of the argument in the piece's own nouns. The three
Background link titles match the actual titles of the linked library lessons
(prefill-and-decode, attention, autoregressive-generation), all of which exist.
Source-kind labels all check: ten primaries that own their claims, one secondary
(Redis) correctly marked. Series minimums (>=8 sources, >=4 primary, >=1
secondary) are met at 11/10/1. Every citation href resolves to the source's own
page. No code anywhere; the O(...) terms are inline nb-math furniture and the two
`<code>` spans (`text_delta`, `us-central1-a`) are literal strings, both allowed.

## Cut

The prose is disciplined and mostly survives the slop test on its own strength.
Zero em-dashes; no banned lexical terms (checked the merged spec and press
lists, including the press ban on "machinery"). No prompt leakage: the "settled
engineering / open question" framing from the commission is enacted, not lifted,
and no sentence claims the article fulfilled its assignment.

The piece leans hard on the "not X, it is Y" construction -- the pause is not
thinking harder; the pause does not track length; a vendor's TTFT is not the
academic prefill time. Each correction names a real, held misconception (the
whole lesson exists to correct "the pause tracks prompt length"), so each earns
its contrast under the negative-parallelism rule rather than inventing a
strawman. The construction recurs enough to notice, but no instance is
unearned, so none is cut.

Edges, read alone and out of order: the why-card opener commits to the felt beat
rather than telling the reader what they have heard, and its closer avoids the
"by the end you will know A, B, C, D" enumeration the brief flagged. The
takeaway resolves the opener's four-part setup without the "the question was
whether" or "that is real, and it is what X" molds. The headline is a single
clause, not the comma-and pairing the recent record overuses; the dek avoids the
comma-triad, the semicolon reversal, and the suspended question. "That beat is
one of the few things about a chatbot a user has a direct experience of" is the
softest edge sentence, but it carries the lesson's motivation (this delay is
directly felt, unlike the internals) and sits inside the bookend that is licensed
to address the reader, so it stays. The colocation opener "A single request in
isolation is one picture" is a thin transition, but the sentence after it does
real work and the pair reads clean; left in place.

The worked-case imperatives ("Type a question into a chatbot, hit send, and
count," "Push the prompt into the tens of thousands," "Cut the round trip in
half") are the Somers-style grounding the voice guide explicitly asks for, and
they describe what the system does rather than gesturing at a hypothetical
reader. Considered against the template's "the body speaks to no one" and kept:
the voice guide holds up Somers's second-person accelerator passage as the model
for exactly this move.

Furniture: the stat strip earns its place -- it is the one image that makes the
hundred-to-one contrast land at a glance -- and the bookends are the template's
required cards. No component is decorative, and nothing reads as a stack of
blocks. No missed component: the piece deliberately argues in prose and numbers,
and the commission required no chart.

Two quotation defects failed the fidelity check and were fixed by de-quoting to
faithful paraphrase, having opened the source myself: the article quoted
"swamped by other latency sources" where Anyscale wrote "'swamped' by the random
noise in TTFT due to other causes" (words the source did not use, presented as
verbatim), and quoted "no discernible relationship..." where the source reads
"there does not seem to be any discernible relationship...". Both meanings were
faithful; the quotation marks were not.

## Reader

Read straight through as the paper's declared reader -- a smart adult who uses
chatbots and has never seen inside one -- the lesson gives something the sources
alone do not: a single account of the wait as a sum of four costs, with the
genuinely counterintuitive result up front (at the lengths you type, the prompt
barely moves the pause) and the honest boundary where that stops being true. The
draft-handoff's original-work sentence claims exactly this composition across
Anyscale, Vaswani, DistServe, Sarathi, Leviathan, PagedAttention, and the
network caveat, and both answers survive: no single cited source assembles the
four-part decomposition. The prose sits closer to the voice-guide exemplars than
to a median summary -- it names the folk belief and corrects it with a number in
the same breath, the Luu move -- rather than narrating itself. The headline, read
last as the largest claim, is one the body earns.

## Edits

- Prompt-length section: replaced the misquoted scatter line "no discernible
  relationship..." / "swamped by other latency sources" with a faithful unquoted
  paraphrase of Anyscale's actual wording.
- Colocation section: rewrote the reversed sentence "Sarathi's authors describe
  the reverse relationship. Prefill cost per token dwarfs decode cost per token."
  so the direction matches the cited quote -- a 512-token prefill saturates the
  GPU's compute at batch 1 (so decodes wait), and decode is the far more
  expensive phase per token (~200x). Quote and citation preserved verbatim.

## Required work

- **researcher.** Source the linear per-layer term the crossover argument rests
  on. The draft attributes the feed-forward and query/key/value-projection cost
  O(n * d^2) to Vaswani Table 1, which lists O(n * d^2) only for the recurrent
  layer and has no feed-forward row; the evidence record repeats this in its
  Numbers block. Supply a primary that states the feed-forward/projection
  per-layer complexity, or confirm the claim must rest only on Table 1's actual
  contents (self-attention O(n^2 * d) versus the O(n * d^2) alternative, faster
  when n < d). Also correct the Contradictions entry that says Anthropic's
  latency page "lists network latency among the factors": that page names model
  size, prompt complexity, and "the underlying infrastructure supporting the
  model and point of interaction," and does not mention network latency.

- **writer.** After the researcher resolves the source: recast the prompt-length
  section (and the one-clause echo in the long-context section) so the article no
  longer sources the linear O(n * d^2) term to Vaswani's Table 1, and so
  Vaswani's self-attention-versus-recurrent sentence is not repurposed as an
  attention-versus-feed-forward claim without support. Fix the network sentence
  in the prefix-cache section: either restate what Anthropic's page actually
  lists or drop the Anthropic clause and let Artificial Analysis (source 11,
  which does say TTFT "includes network latency") carry the network point.
  Verify the Together AI TTFT definition is quoted verbatim: the live page's
  wording I retrieved ("the pause between sending your request and the model
  showing you the first word of its reply") differs from the article's quoted
  string ("how long you wait between sending your request and seeing the first
  word of the response appear"); re-confirm against the source or de-quote. Re-run
  the proof after the recast.

## Decision

revise -- the crossover argument sources the feed-forward/projection cost to a
Vaswani table that does not contain it, and the Anthropic network-latency
attribution is unsupported by the cited page; both need the researcher and writer
before this can publish, even though the edits above cleared the reversed
prefill/decode claim and the two misquotations.
