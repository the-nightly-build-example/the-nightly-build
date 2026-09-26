# Editorial review: the-evidence/align-and-translate (editor/01)

## Correct

Thesis, read from the draft alone: the 2014 Bahdanau paper introduced soft
alignment as a fix to the fixed-vector encoder-decoder bottleneck, showed it only
inside one RNN translator on one language pair, and is now over-credited as the
place attention was invented; the evidence under that reputation is one table and
one length curve.

Claims under it, and how each held:

1. The fixed vector was the bottleneck, and the fix reads the source afresh per
   output word. Held. The bottleneck quote ("compress all the necessary
   information of a source sentence into a fixed-length vector", plus "a
   bottleneck") matches the record at Abstract/§1; the per-word context vector
   ("conditioned on a distinct context vector c_i for each target word y_i") and
   the bidirectional annotations match §3.1/§3.2. The alignment model as a jointly
   trained feedforward net matches §3.1.

2. The gain shows on long sentences; BLEU numbers. Held. Recomputed every Table 1
   cell against the Numbers block: RNNencdec-30 13.93/24.19, RNNsearch-30
   21.50/31.44, RNNencdec-50 17.82/26.71, RNNsearch-50 26.75/34.16, RNNsearch-50*
   28.45/36.15, Moses 33.30/35.63 — all exact. Prose readout (26.75 vs 17.82 all;
   34.16 vs 26.71 no-UNK; 28.45 starred; Moses 33.30 with 418M extra monolingual
   words) is correct. Corpus 348M of ~850M, 30,000-word shortlist, 1,000 hidden
   units/direction, 620-dim embeddings, news-test-2014 3,003 sentences: all match.
   Fig. 2 (RNNencdec falls with length, RNNsearch-50 holds) is described, not
   charted — correct, since the record has no per-bin series to build a chart from.

3. The BLEU caveat (tested hardest). Held and handled correctly. The piece states
   Sutskever's 34.8 and RNNsearch-50's 26.75 explicitly are "not a head-to-head"
   (different depth, reversed inputs, ensembling, differing BLEU protocol), and
   lands the honest in-paper contrast: the paper defeats its own RNNencdec
   baseline on length, not every fixed-vector model. Matches the record's
   contradiction note and the commission's numbers caveat. 34.8 is Sutskever's
   headline (ensemble) number, so "used an ensemble for its strongest scores"
   understates rather than overstates the non-comparability. No fix needed.

4. The scope-not-vocabulary correction (tested hardest). Held and handled
   correctly. The article explicitly says the paper DOES name "a mechanism of
   attention" (§3.1, quoted verbatim) and DOES credit Graves 2013 (§6.1, quoted
   verbatim); it never claims the authors spoke only of alignment. It corrects the
   sweeping "invented attention" and does not claim the paper "started the LLM
   era". Self-attention and LM pretraining are placed in Vaswani 2017 / later, by
   others. All quotations (Cho, Graves, Vaswani "based solely on attention
   mechanisms...") verified verbatim against the record.

Headline/dek/subheads: every label checks out. Headline (Bahdanau, 2014, the
per-word source-reading mechanism) is defensible. nb-meta dek and the rendered
dekline are identical, and both details (WMT'14 English-French; 2013 handwriting
network = Graves) are correct. All four subheads are accurate to their sections.

Citations: data-nb-kind audited against the primary/secondary test — Bahdanau,
Cho, Sutskever, Graves, Vaswani all primary; Semantic Scholar (a citation index,
authoring no claim) secondary. Correct, and meets the-evidence policy (6 sources,
5 primary, 1 secondary). Every href resolves under the full proof (links
included), BLOCK 0.

Captured asset: opened asset-1.png. It is Fig. 3(a) — English source across the
top, French down the left, bright diagonal, and the crossed block where "European
Economic Area" maps in reverse to "zone economique europeenne". Caption, alt
text, and prose all match the figure and the record; the locator carries a real
data-nb-url to the ar5iv full text.

No fact conflicts found between the record and the sources as printed. Nothing to
escalate to the orchestrator. The ~30,000 citation magnitude rests on one
secondary index and is reported as an approximate magnitude — appropriate, not a
block.

## Reads well

Ran the placeholder test across every paragraph, section, and article edge, and
read the piece once cold as a reader arriving from a link. The register sits at
the flat-confidence level the voice guide describes: field terms used and kept,
numbers given bare (BLEU 0-100, 348M, 30,000), the worked case (the Economic Area
reordering) left to carry itself. No voice-guide borrowings (no conveyor belt, no
Paul Graham, no "hit by a bus"). No briefing leaks: the architecture description
overlaps the commission only where the underlying technical fact forces it, not
on any reader-situation sentence taken whole. The opener commits to a checkable
claim ("In 2014 a neural translation model worked in two halves") and avoids the
"You have probably" / "Every large language model" / second-person molds; the
closer names the particular thing at stake and skips the generic moral.

One correctness-adjacent trim: "deliberately narrow" attributed an intent the
record does not support (the scope was a 2014 experiment's, not a stated choice to
keep evidence thin); cut to "narrow".

## The experience

The rendered page carries its argument with two pieces of furniture that both
earn their place: the Table 1 BLEU block (side-by-side numbers prose could not
show as fast) and the Fig. 3(a) alignment heatmap (makes soft alignment and the
learned reordering concrete). No chart was added for Fig. 2 because the record
supplies no verified per-bin series; describing it in prose is the honest call.
The long-sentences section is dense but every paragraph carries distinct content,
so I did not cut. What the piece gives beyond its sources: it separates what the
paper demonstrated (soft alignment on one language pair, one table, one curve)
from the "invented attention" origin story and puts the size of that evidence base
on the page — which is exactly the draft-handoff's original-work sentence, and the
page delivers it. Not a restatement of the sources; no redraft on that count.

Anti-echo confirmed against the live library: the neighbour attention-is-all-you-
need uses "credited with X / never did Y", "Eight authors, two language pairs...",
and "Five mentions of ..., zero about ..."; none of those molds appear here. The
dek is not a comma-triad, semicolon-reversal, or suspended-question mold and is
unmistakable for the recent elmo/deep-double-descent/mamba/llama-3 deks. (Noted
but left: the heading "One vector had to hold the whole sentence" shares two
opening words with elmo's "One vector for 'bank,'"; the constructions and points
differ, and it is the sharpest heading for this section — an incidental overlap,
not a formula.)

## Edits

- Cut "deliberately" from "The evidence for all this was deliberately narrow"
  (unsupported intent).
- Figure caption: "bright means the decoder drew heavily ... the crossed block
  shows the phrase reordering the model learned on its own" -> "brighter cells
  mean the decoder drew more heavily ... the crossed block is where the French
  phrase order inverts the English" (caption made a descriptive label; the
  "learned it on its own" interpretation already lives in the prose).
- Table caption: two chained semicolons -> periods (three plain sentences), per
  the punctuation default.

## Decision

approve — it is correct, reads at the guide's register, and does real work on its
sources; the scope correction and BLEU caveat both hold, and the proof runs
BLOCK 0 / WARN 0 with links.
