# Editorial review: the-mechanics/quantization (editor/01)

## Skeptic

Thesis: quantization rounds every weight to a coarser grid of allowed values;
down to about four bits a scheme that protects a few oversized values costs under
one percent of quality, and it breaks when the scheme is naive, the model is
large, or the grid drops below four bits, because a handful of outlier feature
dimensions carry the model and one of them stretches a single-scale grid too thin
for everything else.

Claims it stands on, and how each held:

- The memory pressure. GPT-3 at 175 billion weights times sixteen bits is 326 GB,
  more than one accelerator holds, five 80 GB A100s to load (#s1); an independent
  350 GB (#s2). Both figures own their claim in the cited papers; opened GPTQ and
  SmoothQuant and both land. The 7B drop from 13.0 GB to 3.80 GB at four bits
  (#s3) matches the llama.cpp table exactly.

- The near-flat top. The degradation table (16-bit 5.9066 baseline; 6-bit +0.1%;
  5-bit +0.2%; 4-bit +0.9%; 3-bit +4.1%; 2-bit +14.8%) reproduces the LLaMA-7B
  rows of PR #1684 to the digit. The writer selected one representative per
  bit-width and dropped the two Q*_K_S rows; every printed value is exact and the
  monotone climb below four bits is preserved, so the selection does not mislead.
  Four-bit as the near-universal optimum across 35,000 runs, 3-to-8 bit, 19M to
  176B parameters (#s5), verified against the abstract.

- The naive-at-scale break. OPT-175B WikiText2: 8.34 FP16, 8.37 careful 4-bit,
  10.54 naive 4-bit, roughly 73,000 at naive 3-bit (#s1, GPTQ Table 4 owns these).
  Naive 8-bit worse at 13B than 6.7B while the outlier-aware method holds the
  baseline at both (#s6). This is the claim I pushed hardest on, because "collapse
  at 73,000" is the article's most dramatic number; it is the primary's own
  RTN-3-bit figure (7.3e4), correctly attributed and correctly framed as naive,
  not as quantization in general.

- The outlier mechanism. Up to 20x larger, ~150,000 per 2,048-token pass in fewer
  than seven dimensions, phase shift between 6 and 6.7 billion parameters, every
  layer then affected; zeroing ~0.1% of features costs +600-1000% perplexity
  against ~0.1% for the same count of random features (#s6). All match the
  evidence Numbers block. The stat-strip figures (20x, <=7 dims / ~150,000,
  +600-1000%) each carry a citation in adjacent prose.

- What the good schemes do. Keep outliers in 16-bit and the other 99.9% in 8-bit,
  lossless to 175B, memory roughly halved (#s6); protect the ~1% of weight
  channels the largest activations flow through, chosen by activation not weight
  magnitude, group-scaled, pulling OPT-6.7B naive 3-bit from 23.54 to 11.39
  against the full model's 10.86 (#s7); shift the activation-side outliers into
  the weights by an offsetting rescale (#s2). The article uses the AWQ table pair
  (23.54 -> 11.39), not the figure-caption pair (43.2 -> 13.0) the evidence flags
  as illustrative. Correct choice.

- Below four bits. Llama-2-7B 5.47 -> 5.60 at four bits, -> 6.24 at three (#s7);
  2-bit near 15% (#s3); an image-captioning model losing 16.9 points at naive
  three-bit against 1.17 for a good four-bit scheme, perplexity understating task
  damage (#s7). All verified.

Correction carried accurately: the article states cheapness holds only for a good
scheme down to about four bits and breaks three ways (naive scheme, large model,
below four bits). That is the brief's required refinement of "usually cheap," and
it is delivered without contradicting the "sometimes costs a lot" step.

Both open questions are marked open: why outlier features arise (the 6.7B shift is
documented and the separator-token account (#s8) is partial, but no source settles
it) and where the accuracy floor sits below four bits (#s5). Neither is written
around; both are stated as unsettled.

Citations: all eight source hrefs opened as printed and land on the source, with
titles and authors matching the source entries. The four internal cross-lesson
links (gradient-descent, perplexity, parameter-count, knowledge-distillation)
resolve in the proof library, and the two Background reading-row titles match
their targets verbatim. Every data-nb-kind is correct: seven primaries (the six
papers plus the llama.cpp shipping-tool measurement) and one secondary
(Grootendorst, cited only for the weights-dominate-memory motivation, no number).
Source policy met: 8 sources, 7 primary, 1 secondary.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed from this read.

## Cut

The reporting is dense and the sentences mostly earn their place; the writer had
already split six density warnings before handoff. The one recurring pattern is a
"half the story / tidy version" signpost used three times. Two of the three are
pure signposting that grades the article's own structure, which spec/slop.md rules
out; the third carries the brief's required correction and stays.

Removed "It is only half the story, and" from the near-flat-top close, keeping the
substantive setup that "good" and "about four" are the load-bearing qualifiers
(that setup does real forward work, naming the two conditions the next two
sections unpack). Removed "This is the second half of the story the flat top hid"
from the below-four-bits section, where it only announced a turn the surrounding
sentences already make; the correction sentence now lands as the section's payoff.
Two sentences failed the delete test; both cut.

The intentionally-left W-SENTENCE-DENSITY warning, judged directly: keep, do not
split. "Rounding is cheap for good schemes down to about four bits, and it is
expensive when the scheme is naive, when the model is large, or when the grid
drops below four bits, three conditions the tidy version leaves out." The three
when-clauses are cleanly parallel and each names a condition the body already
taught, so the reader is recognizing, not decoding; it is one long sentence among
short ones, which is the varied-length ideal rather than a density fault; and the
three-way parallelism is the teaching payoff the brief asked to be carried whole.
Splitting it would scatter the correction. It is under control. Cutting the two
redundant "half the story" signposts around it also leaves this the single, clean
statement of the qualifier, which reduces the pressure the parallelism was
carrying.

Slop test elsewhere: edges checked out of order and in place. "whether those small
errors stay small is the entire question" leans toward the unearned-punchline
family but continues the argument from the just-stated facts (tiny per-weight
error against billions of weights) and names the exact question the rest of the
piece answers, so it stays. No negative-parallelism reflex, no decorative-analysis
trailing clauses, no vague attribution, no puffery. Headings reconstruct the
argument in the piece's own nouns and are varied in construction; none is a
scaffolding slot or a comma-and join. The dek states a finding and is not a
comma-triad. Against the recent-pattern notes: the piece does not close the body
on a "gap keeps closing" assessment (it closes on the two open questions), and the
section lengths vary rather than running a uniform row of short blocks. No prompt
leakage: the opener restates the reader's situation the commission describes, which
is legitimate subject matter, and the correction wording is the article's own.
Punctuation is plain, one tightly-bound semicolon, no stray em-dashes. Furniture
(one table, one stat strip, no chart) is right-sized and each element earns its
place.

## Reader

Read straight through as the paper's declared reader, who knows a number and a
small case and nothing about weights: the piece hands over one ordered causal
chain, from "the cheaper copy answers worse" down to "a few oversized values in a
single-scale grid decide the cost," that no one of its eight sources gives on its
own. The seven quantization findings are assembled into that chain and the loose
"usually cheap" is replaced with the exact conditions under which cheapness holds
and the three under which it breaks; the draft-handoff's original-work sentence
claims exactly that synthesis, and it survives the read. The prose sits with the
voice-guide exemplars rather than a median summary: the quarter-inch ruler is a
Sanglard everyday-picture substitution, the measured numbers reach the verdict on
their own in Luu's manner, and the "say the tidy version plainly, then show where
it breaks" structure is the Luu complexity move used deliberately. The headline,
read last as the largest claim, is defended by the body in both halves.

## Edits

- Removed the signpost fragment "It is only half the story, and" from the
  near-flat-top section close; kept the setup naming "good" and "about four" as
  the load-bearing qualifiers.
- Removed the signpost sentence "This is the second half of the story the flat top
  hid" from the below-four-bits section; the correction sentence now closes the
  paragraph directly.

## Required work

- writer: run a fresh proof. The two cuts drop the body by about eighteen words
  (still inside the 1200-2200 band) and the nb-meta word count will need
  restamping. The one documented W-SENTENCE-DENSITY warning is retained by editor
  decision; no new warnings are expected.

No researcher work. No orchestrator work.

## Decision

approve. The causal chain, the degradation table, the three-way correction, and
both open questions all hold against the evidence and its owning primaries; the
only edits were two redundant structural signposts, which need a fresh proof to
restamp the word count.
