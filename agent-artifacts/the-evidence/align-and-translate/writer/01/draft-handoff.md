# Draft handoff: the-evidence/align-and-translate (writer 01)

## The one thing this article does that the evidence does not

It separates what the 2014 paper actually demonstrated (soft alignment as a fix
to the fixed-vector bottleneck, measured in BLEU on one language pair, with the
mechanism named "attention" only in one passing passage and a 2013 precursor
credited) from the "invented attention" origin story now told about it, and puts
the real size of that evidence base on the page: one language pair, one Table 1,
and one BLEU-vs-length curve. The scope correction is made visible in the last
body section ("A fix for one translator, not the Transformer") and quantified in
"The gain showed up on the long sentences."

## How the draft honors this round's focus

- Scope, not vocabulary. The draft states plainly that the paper does name "a
  mechanism of attention" (Section 3.1) and credits Graves 2013 (Section 6.1).
  The correction it presses is the sweeping "invented attention / origin of the
  architecture," not the word choice.
- BLEU caveat honored. The in-paper contrast is RNNsearch vs RNNencdec (Table 1)
  and the length curve (Fig. 2). Sutskever's 34.8 vs RNNsearch-50's 26.75 is
  given explicitly as NOT a head-to-head (different depth, reversed inputs,
  ensembling, differing BLEU protocol), and the material contradiction
  (Sutskever's fixed-vector LSTM reporting no long-sentence difficulty) is
  weighed in prose.
- Anti-echo. Headline, dek, and all four body headings avoid the neighbour's
  "credited with X / never did Y" mold, its "N authors, M language pairs"
  heading, and its "X mentions of Y, zero about Z" heading. attention-is-all-you-need
  is linked in Background and the line between the two papers is drawn in the
  body. Opener avoids the "Every X" / second-person defaults and the
  "By the end you will know A, B, and C" tricolon; dek checked against elmo,
  deep-double-descent, mamba, and llama-3 for mold.

## Furniture used

- One source asset (Fig. 1): Figure 3, panel (a) of Bahdanau et al., captured
  with `nb asset pdf` from the arXiv PDF and inspected. It shows the
  English-French alignment heatmap with the "European Economic Area" ->
  "zone économique européenne" reordering. Axis word labels retained; cited to
  the paper at a real locator (Fig. 3(a)).
- One nb-table: Table 1 BLEU results (RNNencdec vs RNNsearch at 30/50, the
  starred best, Moses), both columns, caption notes Moses's extra 418M-word
  monolingual corpus.
- No chart: the record does not supply the per-bin numeric series for Fig. 2, so
  a data chart could not be built from verified data; the length curve is
  described in prose and cited to Fig. 2 instead.

## Proof result

`nb check ... --series the-evidence` (full run, links included): **BLOCK: 0,
WARN: 0, verdict PUBLISHABLE.** No warnings left standing. Render probe was
skipped (no Chrome in this environment); CI will run it.

Sources: 6 total, 5 primary (Bahdanau 1409.0473, Cho 1406.1078, Sutskever
1409.3215, Graves 1308.0850, Vaswani 1706.03762), 1 secondary (Semantic Scholar
citation record). Meets the-evidence policy (>=6, >=3 primary, >=1 secondary).
Numbered in first-citation order.

## Open questions for the orchestrator

None blocking. One note: the citation magnitude (~30,000) rests on a single
secondary index (Semantic Scholar, 30,066 at retrieval 2026-09-26) and is
reported as an approximate magnitude, per the evidence record.
