# Editorial review: the-mechanics/multilingual-gap (editor/01)

## Skeptic

Thesis: the multilingual gap a reader has felt, a chatbot that is sharp in
English and vaguer, more error-prone, and dearer in other languages, resolves
into two parts of the system. The training corpus sets how much the model ever
saw of a language, and the tokenizer sets how many tokens each message costs.
The gap is worst where both go wrong at once, low-resource non-Latin scripts,
and nobody can yet say how much of it each cause owns.

The claims it stands on, and how each held:

- **The performance instance: GPT-4 scores 85.5% in English and 62.0% in Telugu
  on the same translated MMLU questions.** Held. The figures match the evidence
  Numbers block and the GPT-4 report (Figure 5). The intermediate anchors check
  out: Spanish 84.0 (a point and a half), Arabic 80.0 (five and a half), Bengali
  73.2 (twelve), Telugu 62.0 (23 points). The progress reading, "GPT-4 in most of
  these languages beats the English scores of the models just before it," is
  guarded correctly by "most": the prior-best English baseline is GPT-3.5 at 70.1,
  and only Marathi (66.7) and Telugu (62.0) fall below it. Had the draft said "in
  these languages" without "most" it would have been false; the qualifier is
  load-bearing and correct.

- **Training-data distribution, the lead cause: GPT-3 is 93% English by word
  count; the raw web it is filtered from is ~41% English.** Held, and handled to
  the round's requirement. The 93% figure is explicitly attributed to GPT-3
  (2020), flagged as a two-generations-old proxy no current frontier model
  discloses, and paired with the current Common Crawl raw-web share (40.6%
  English, Russian next at 6.8%, CC-MAIN-2026-30). The raw-web-to-corpus jump
  (~41% to 93%) is carried as its own finding and correctly attributed to
  English-favoring quality filters plus oversampled English Wikipedia/books, which
  the GPT-3 paper's dataset mix supports.

- **The token tax, the amplifier: the same UDHR paragraph costs 33 tokens in
  English and 512 in Burmese under cl100k_base, 15.5x.** Held. The full series
  matches the evidence Numbers block and the committed chart provenance exactly.
  The downstream consequences (up to 4x cost in Telugu/Amharic, ~5x for an Andhra
  Pradesh user, cost >=2.5x, latency ~2x, an order of magnitude less context) each
  trace to Ahia §4 and Petrov §1. The Shan "you" = 9 tokens example matches
  Petrov's §4.1.

- **The premium is a tokenizer-training property, not a script property (MuRIL
  1.21x Telugu).** Held, and correctly framed as the correction to a real, named
  misconception (that non-Latin characters are inherently expensive), so the
  contrast earns itself rather than reading as invented negative parallelism.

- **Nobody can yet split the blame; data leads because it explains variance the
  tokenizer cannot (French 72.1% vs Japanese 67.0%, near-equal fertility, 3.5B vs
  214M tokens).** Held. MEGA measures both and declines to rank them, and the
  article says so plainly ("Anyone who tells you it is 70% data and 30% tokenizer
  is making the numbers up").

One break with the argument, fixed in place. The orientation asserted "The larger
effect comes first" as the reason data leads. That claims a magnitude ranking the
evidence does not support and the article's own closing section explicitly denies
("nobody can yet say by how much"; MEGA refuses to rank the two causes). The
presentational order is legitimately earned later by the French/Japanese case, so
I cut the unsupported magnitude claim rather than route it. The remaining "Take
them in that order" states the order without asserting which cause is bigger.

Display text checks out descriptor by descriptor. Headline: GPT-4 named, MMLU is
an exam, 23 points is the real gap (85.5 to 62.0), present tense. The
machine-translation caveat it omits is carried in the first body paragraph under
it. Dek: names both mechanisms, restates nothing from the headline, "15 times"
matches the 15.5x ceiling, and it avoids the banned molds (no semicolon reversal,
no suspended question, no comma triad). Subheads reconstruct the argument in the
piece's own nouns and are varied in build.

`data-nb-kind` audit: 8 primary, 1 secondary (s9, ai-tldr.dev, correctly
secondary and used only to establish the finding reached practitioner material).
Meets the commission's floor (>=8 sources, >=4 primary, >=1 secondary). The
tiktoken citation (s6) points to the instrument for a firsthand reproduction whose
provenance is the committed chart-1.py; that is a fair primary for a reproduced
measurement, not a hidden secondary.

I opened all nine citation hrefs as printed. Every one lands on the source itself:
GPT-4 Technical Report (s1), "Do All Languages Cost the Same?" (s2), GPT-3 (s3),
Common Crawl language statistics showing 40.58% English on CC-MAIN-2026-30 (s4),
MEGA (s5), tiktoken/cl100k_base (s6), Petrov "Language Model Tokenizers Introduce
Unfairness Between Languages" (s7), Teklehaymanot and Nejdl "Tokenization
Disparities as Infrastructure Bias" across 200+ languages (s8), and the ai-tldr.dev
page carrying the exact 4-5-to-15-20 token claim (s9).

## Cut

Slop pass, every sentence including display text and both bookends. Two sentences
failed and were cut:

- "Two honest caveats travel with that number." A structural signpost that also
  grades the article's own honesty; the two caveats state themselves in the
  sentences that follow, so the label carried nothing. The paragraph now opens on
  the concrete caveat ("The questions were machine-translated").
- "The larger effect comes first." Cut as the unsupported magnitude claim above;
  it also functioned as a slop edge, restating the ordering "Take them in that
  order" had already given.

Edge sweep held up otherwise. The emphatic fragments ("A worse answer and a
larger bill, for the same message"; "Same script, different training, most of the
tax gone"; "The same paragraph, the same meaning, several times the pieces to
carry it") each depend on the specific nouns and the mechanism just shown, so they
survive the placeholder test and are deliberate emphasis, not filler. The closing
sentence of the takeaway ("puts the data first, and admits that nobody can yet say
by how much") is the conclusion the argument built, and now agrees with the
orientation after the cut above.

Negative-parallelism check: the one earned contrast (the MuRIL "it is tempting to
read this off the script... They are not") corrects a real, named misconception
with a cited figure, so it stays. No banned dek or heading mold. Em-dash count is
zero; the two semicolons are legitimate parallel constructions.

Prompt-leakage check against the commission and briefs: the article's "work back
from that experience" is the reader's situation restated in the article's own
terms, not a lifted instruction, and "settled"/"not settled" report the epistemic
state rather than echo a planning label. No leak.

Voice and formula: the opener avoids the paper-wide "By the end you will know X"
mold and the Mechanics "the thing that feels like X is not what happens" mold; the
closing section is named for its content ("Nobody can yet split the blame between
the two causes"), not a stock "where this lives now" heading. The register sits
where the voice guide directs, plain and numeric, committing to figures (33 to
512, 1.21x, 3.5B vs 214M) rather than reaching for "far more." No borrowed
phrasing from the Ciechanowski/Evans/Patel exemplars.

Furniture: one figure (the token-count chart), earned as the natural carrier of
the token series; no component stacking. I inspected the committed chart-1.py and
read chart-1.png as a reader. Axes are labeled, the scale is linear and honest, the
13 bars and their multipliers match the evidence Numbers block exactly (33/44/44/
50/50/74/85/88/93/182/281/305/512; 1.0x to 15.5x), the source is cited in the
caption, and the alt text is complete. No chart correction needed.

## Reader

Read straight through as the paper's declared reader, someone smart with no time
in a codebase: what I have that the sources alone would not give me is a working
diagnostic. I can now predict which languages come out worst (low-resource,
non-Latin, where the corpus is thin and the tokenizer least fitted) and, hearing
any explanation of the gap, tell whether it is reaching for the data cause (the
French/Japanese split is its evidence) or the tokenizer cause (the 33-to-512 count
is its evidence), while knowing the split between them is unquantified. The
original-work sentence claims exactly this: it assembles the evidence record's
separated figures into one ordered diagnostic and foregrounds the raw-web-to-corpus
jump the record never built into an argument. Both answers survive; the piece
teaches rather than restates. The prose sits closer to the voice-guide exemplars
than to a median summary: it works backward from a felt behavior, pins down what
the model and tokenizer operate on before explaining the gap, and rates its own
confidence out loud. The headline, read last as the largest claim, states a real
finding with its actor named and its number as the surprise.

## Edits

- Orientation, second paragraph: deleted the opening signpost "Two honest caveats
  travel with that number." so the paragraph opens on the concrete caveat.
- Orientation, fourth paragraph: deleted "The larger effect comes first." as an
  unsupported magnitude claim that contradicted the article's own "nobody can yet
  say by how much"; the presentational order remains stated and is earned later by
  the French/Japanese case.

## Required work

None. No evidence gap, no broken central claim, no chart correction, no redraft.

## Decision

approve. The two-part mechanism is sourced, correctly ordered with the magnitude
overclaim removed, all four caveats survive marked settled versus open, the dated
proxy is handled honestly, every citation resolves to its source, and the chart is
faithful to the evidence.
