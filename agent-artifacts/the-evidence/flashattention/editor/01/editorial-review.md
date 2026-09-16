# Editorial review: the-evidence/flashattention (editor/01)

## Skeptic

Thesis: FlashAttention speeds up attention not by approximating or skipping
any of the arithmetic, but by never writing the full N-by-N score table to a
GPU's slow, large memory (HBM); it tiles the computation through fast, small
on-chip memory instead, and even does *more* floating-point work (recomputing
in the backward pass) to get there. Claims it stands on: (1) the N=1024
worked example produces a 1,048,576-entry table; (2) an A100 has ~20MB of
on-chip memory against 40-80GB of HBM, and the size gap is vendor-sourced on
both ends while the ~19TB/s SRAM-bandwidth figure is a third-party estimate
the paper itself flags; (3) FlashAttention returns the exact same output,
"with no approximation," while running *more* GFLOPs (75.2 vs. 66.6 on the
GPT-2 medium config) and far less HBM traffic (4.4GB vs. 40.3GB); (4) the
paper reports four differently-scoped "faster" numbers that a careless
retelling conflates; (5) FlashAttention-2 and -3 preserve exactness (FA-3's
FP8 mode is a different, bounded-error source, not the sparsity/approximation
kind).

I tried hardest to break claim 3 (the central "more math, less data"
correction), since it is the article's whole reason for existing and the
easiest to get backwards. I reread the FlashAttention paper's own abstract
directly (arXiv:2205.14135): "an IO-aware **exact** attention algorithm,"
with the recomputation trade stated explicitly in §3.2. It held. I pushed on
claim 2's asymmetry next, since a lazy pass could make "192KB SRAM at ~19TB/s"
and "40-80GB HBM at 1.5-2.0TB/s" look equally vendor-sourced. I opened both
NVIDIA PDFs directly (not just the evidence record's paraphrase): the
architecture whitepaper (p.15, p.19) confirms 192KB/SM and 108 of 128 SMs
shipped; the whitepaper and the product datasheet together confirm every HBM
capacity/bandwidth figure (1,555 / 1,935 / 1,555 / 2,039 GB/s across the four
SKUs); neither document states an on-chip SRAM bandwidth figure anywhere.
That distinction held and the article states it correctly and separately.

I recomputed the arithmetic the draft states as computed: 1,024×1,024 =
1,048,576 (correct); ~2.1MB at 2 bytes/entry FP16 (correct, and correctly
flagged in-text as the writer's own arithmetic, not a paper figure); 75.2/66.6
≈ "about 13% more" (correct, 12.9%); 41.7/7.3 ≈ "5.7-times" (correct); 9.5/2.7
≈ 3.5x and 4.7/2.7 ≈ 1.74x vs. Megatron for GPT-2 small, 21.0/6.9 ≈ 3.0x and
11.5/6.9 ≈ 1.67x for medium, so "roughly 1.7 to 1.8 times" against
Megatron-LM holds. 20.0/17.4 ≈ 1.149, so "15% faster" for BERT-large is the
correct speedup convention (not a naive time-delta percentage, which would
read 13%) and matches the paper's own stated figure.

I opened all seven source hrefs as printed. All seven land on the source
itself: the two arXiv abstract pages (FlashAttention, FlashAttention-2), the
FlashAttention-3 arXiv abstract, both NVIDIA PDFs (fetched and read directly,
not just trusted from the evidence record), the PyTorch blog post, and the
Hugging Face docs page. Every quoted fragment attributed to these sources
checks out verbatim, including the PyTorch head-dimension figures (3.4x at
head dim 8, 1.01x at 128) and the Hugging Face backend descriptions.

One break, fixed: the draft cited the PyTorch blog (source 4) for "In March
2023, PyTorch 2.0 added..." The fetched page shows only a "Last updated
2024-11-14" stamp and states no original publication date, which the
researcher had already flagged as unconfirmed. I independently verified via
web search that PyTorch 2.0 shipped March 15, 2023 (PyTorch's own release
post), so the fact is true, but the cited source does not itself support the
specific date and no source in the record does either. Rather than add an
uncited source, I cut the date; the sentence loses nothing essential. Fixed
directly (see Edits).

No claim broke. Author names, the paper title, and every figure I could check
against a primary matched. Every `data-nb-kind` label is correct by the
authorship/stake test: the three papers and both NVIDIA documents are
primary; the PyTorch blog and Hugging Face docs are secondary to
FlashAttention's own claims even though each also owns its subject's adoption
decision (the article cites them only for that adoption/benchmark reporting,
where "secondary" is the defensible reading, and the evidence record reasoned
through the same tension). No block-sparse FlashAttention material appears
anywhere in the piece, so the one real approximate variant the evidence
record warned about never gets a chance to blur into the exact algorithm the
piece is about.

## Cut

Two self-reference breaks, both fixed. The lesson template is explicit that
only the two bookends may refer to "the lesson"; the body never does. The
draft's body broke this twice: "the trade in **this lesson's headline**" and
"the GPT-2 configuration earlier **in this lesson**." Both are outside the
bookends. Fixed by rewriting each to state the point in the article's own
terms without naming the lesson or its own headline.

One leaked/lifted sentence, fixed. The opening bookend paragraph's first two
sentences tracked the commission's own framing almost clause for clause: the
commission's "The reader keeps meeting the word 'attention' and the claim
that a model's context window grew because of it... The paper says the
opposite. It computes the same attention, to the last bit, and wins by
moving less data" versus the draft's "People keep meeting the claim that a
model's context window grew because attention got faster... FlashAttention
computes the exact same attention a GPU always did, to the last bit, and
wins by moving less of a large table... rather than by doing less math." The
skeleton and even the phrase "to the last bit... wins by moving less" carried
over almost verbatim. The point underneath is real and evidence-backed, so I
rewrote it in the article's own terms rather than cutting it outright.

Ran the delete test and the edge-sentence pass (first/last sentence of every
paragraph, section, and the article, read out of order) against
`spec/slop.md`. Several "X, not Y" constructions recur ("not the number,"
"not arithmetic," "not zero," "not about whether the algorithm skips any of
the comparison," headline "does more arithmetic to move less data" pattern
echoed in the closer) but each corrects a misconception the piece names in
the surrounding prose — the exact-vs-approximate and FLOPs-vs-traffic
corrections the commission asks for — so none read as an invented strawman
or a decorative flourish; none were cut. No empty conclusions, puffery,
vague attribution, fluff openers, or unearned punchlines found elsewhere. No
em-dashes, "leverage," or "load-bearing" in the piece; the banned-terms
counts are all at zero.

Checked the recent-pattern notes. The headline ("FlashAttention does more
arithmetic to move less data") is a single declarative claim, not the
two-sentence numeric-reversal mold the desk has leaned on. The dek is one
lean sentence, not a semicolon reversal, suspended question, or comma triad.
Section headings are full declarative sentences carrying their own numbers
("One A100 has about 20MB of on-chip memory and 40 to 80GB of HBM," "The
paper reports four different speed numbers, not one") — a different
construction from both the recent numeric-reversal headline mold and the
short noun-phrase heading mold ("A parlor game, played by teleprinter"). No
repeated formula found.

Furniture: the stat strip, comparison table, numbered steps, and chart are
all documented components, each cited in nearby prose or its own caption, and
none reads as filler — each carries a distinct piece of the argument (size
gap, four scoped speedups, the tiling mechanism, the memory-scaling curve).
No Verdict block or other retired closing note, correctly, per
`press/editorial.md`'s standing instruction against it for this template.

## Reader

Reading it straight through as the declared reader (smart, widely read,
never written a CUDA kernel): what I have that the sources alone would not
give me is one built argument connecting a worked table size, to why a GPU's
two memory tiers matter, to what tiling and recomputation actually do step by
step, to the four scoped speed numbers kept honestly apart, closing on the
"more arithmetic, less data" correction grounded in the same GFLOPs figures
introduced earlier — a synthesis no single cited source states in this shape.
That matches the draft handoff's own original-work claim, opened at the third
read, and it survives in the article as edited: my changes were prose-level
and didn't touch the argument's spine.

The prose sits closer to the voice-guide exemplars than a median AI summary:
it gives the real SRAM/HBM numbers beside the "fast"/"slow" labels the way
Dan Luu gives the real multiple instead of "much faster," walks the tiling
steps concretely rather than summarizing them as "more efficient," and
states the exact-vs-approximate correction plainly rather than hedging it.
The headline, reread as the largest claim, is accurate and specific: the
paper's own numbers (75.2 vs. 66.6 GFLOPs, 4.4 vs. 40.3GB) are exactly what
it asserts.

## Edits

- Rewrote the "Why this matters" bookend's opening two sentences: replaced
  the near-verbatim echo of the commission's framing sentence ("keep meeting
  the claim that a model's context window grew because... computes the same
  attention, to the last bit, and wins by moving less data") with the same
  fact stated in the article's own clause order and wording.
- Rewrote "the trade in this lesson's headline is real, not a turn of
  phrase" to "the trade of more arithmetic for less data is real, not a
  turn of phrase," removing a body self-reference to the lesson/headline the
  template reserves for the bookends only.
- Rewrote "on the GPT-2 configuration earlier in this lesson" to "on the
  GPT-2 configuration described earlier," removing a second body
  self-reference to the lesson.
- Cut the unsupported "In March 2023" date claim from the PyTorch-adoption
  sentence; the cited source states no original publish date and no other
  source in the record confirms one. Changed the sentence's vague "moved
  into standard software fast" to "moved into standard software directly"
  since the timing claim it was leaning on is gone.

## Required work

None. All issues found were within the editor's remit and fixed directly.

## Decision

Approve. The claims, figures, and citations all held under testing; the
issues found (two template self-reference breaks, one lifted commission
sentence, one unsupported date) were prose-level and fixed in place without
touching a fact, a number, or the argument the writer built.
