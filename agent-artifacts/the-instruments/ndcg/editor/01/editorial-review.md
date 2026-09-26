# Editorial review: the-instruments/ndcg (editor/01)

## Correct

Thesis, read from the draft alone: an nDCG@10 is not a single measurement but a
compound of separable choices (which documents were judged, the grade scale, the
gain convention, the discount convention, the rank cutoff), and it can move far
enough to reorder a leaderboard without any retrieval system getting better. The
claims under it: (1) the score is built from a graded gain and a position
discount, normalized against the ideal ordering, and follows from arithmetic a
reader already has; (2) two convention axes, gain and discount, give the same
ranking different numbers, so two nDCG@10s are comparable only when computed the
same way; (3) the score counts only judged documents, and filling judgment holes
alone flipped a real ranking; (4) despite all this nDCG is still the ranking
measure that best matches user preference. The claims are all stated in the
draft.

I recomputed the arithmetic in Python against the record's worked example B and
the definitions, and found two table cells wrong. The linear worked table gave
rank 6's grade contribution as 0.713; 2/log2(7) = 0.7124, which displays 0.712.
The ideal column gave rank 2 as 1.892; 3/log2(3) = 1.8928, which displays 1.893.
Both were mis-rounded in the last digit: with them uncorrected the printed
columns summed to 6.862 and 7.140, not to the stated DCG 6.861 and IDCG 7.141.
Corrected, the columns now sum exactly to the stated totals. The stated totals,
the exponential row (13.848 / 14.595 / 0.949), the linear-vs-exponential pair
(0.961 vs 0.949), the shallow-pool values (1.000, 0.631, 0.500, 0.289) and the
TREC-COVID cells (ANCE 0.654 to 0.735 at 14.4% holes; docT5query 0.713 to 0.714
at 2.8%; BM25 6.4%, ColBERT +5.8, 980 pairs, 6.7 points) all check against the
record.

The BEIR table caption claims only what its two rows show ("before and after 980
missing relevance judgments were filled in ... systems left unchanged") and
carries BM25 and ColBERT in prose, not in the cells. It does not overclaim; the
choice to build the two-row table from the figures the record owns rather than
capture BEIR Table 4 (which the record cannot fill for BM25/TAS-B) holds.

The narrow angle is intact. The piece never argues nDCG is a bad metric: the
"What nDCG still gets right" section opens "None of this makes nDCG a poor
measure" and the takeaway states "This is not a case against the measure." The
Sanderson 2010 defense is represented with its own numbers (63%, 160/252,
significantly above MRR's 53% and P(10)'s 50%) and its own limit (the edge leans
on the zero-relevant case; ~two in three at best). Wang 2013 is represented
precisely: distinguishes substantially different rankers even as the raw value
drifts to 1, and the discount is load-bearing past the critical decay rate. The
"collapses to a measure of one thing, how high the single answer landed" point is
presented as a derivation from the definitions plus documented sparsity, not
attributed to a source that does not state it.

One citation fix. "Some collections judge fewer than two relevant documents per
query" is BEIR's statement (s2, "< 2"), but the sentence cited only Craswell
(s6), whose firsthand claim is the click-log "one positive label per query." I
attached s2 to the first clause and left s6 on the second, so each clause is
cited to the document that owns it.

Headline, dek and subheads verified against the record: 980, ANCE/BM25, 0.961/
0.949, MTEB and BEIR as the leaderboards nDCG@10 sorts. "Judging 980 more
documents" is standard IR usage for adding 980 relevance judgments and the count
is BEIR's; the dek's nb-meta and rendered deklines are identical. All nine
`data-nb-kind` labels match the record (eight primary, one secondary: Wikipedia,
correctly secondary), meeting the the-instruments policy (>=8 sources, >=4
primary, >=1 secondary). Every citation href is the record's owning-document
address: seven arXiv/MSR/Wikipedia links resolve 200; the two ACM DOIs (s3
Järvelin & Kekäläinen, s8 Sanderson) 403 the probe and are the gated canonical
homes the brief allows. The Go-deeper trec_eval GitHub link 403s the probe the
same way (a bot block, not a dead link) and is furniture, not a numbered source.

## Reads well

The prose is already lean and I found no slop to cut. I ran the placeholder test
on every paragraph, section and article edge and on the last sentence hardest:
the openers ("Every team that builds a search feature", "Start with the wrong
version", "Every score so far assumed the answer key was complete", "None of this
makes nDCG a poor measure") and the closer ("It is the reason to ask, every time,
which judged pool produced the number") all depend on their nouns and survive.
The one-off antitheses ("progress had been in the metric, not in the systems";
"This is not a case against the measure") each correct a misconception the piece
actually built and stated, so they stay. I checked commission.md and the voice
guide for borrowed clauses and found none carried into the draft; the voice
guide's "state the wrong intuition, then the numbers that break it" move is used
in the writer's own words to open the construction.

Against the recent record: the opener avoids the "When a chipmaker says" and "You
have probably" molds and the "By the end you will know A, B, and C" tricolon
closer. The dek is built as a definition plus its hidden dependence rather than
the recent instruments number-and-reversal mold, and does not restate the
headline. The five headings are each a distinct step of the argument, built
differently from each other, with none of the comma-and stamping the standard
warns about.

I changed one semicolon to a period in the orientation section ("... to rank
retrieval systems. MTEB takes ...") where two separate facts were chained,
honoring the house preference for the period. The remaining semicolon (the 2002
vs modern discount contrast) is a tight parallel comparison and earns its place.

## The experience

The rendered page carries its weight in three tables read in order: the worked
calculation, the same ranking under two gain conventions, and TREC-COVID before
and after. Each shows faster than prose what the section argues, and the captions
stay factual labels while the interpretation lives in the surrounding text.
Nothing drags; the piece builds the metric, shows two ways its number moves
(conventions, then judgments), spends its central case on the BEIR hole
experiment, and lands on the defense before the takeaway.

What it gives beyond its sources: it makes the compound visible on one page,
scoring a single ranking to two numbers under the two gain conventions and
setting BEIR's re-judging beside it, so a reader sees the number move twice with
no system changed. That is the original-work sentence in draft-handoff.md, and
the page delivers it.

## Edits

- Corrected worked-table cell: rank 6 grade contribution 0.713 to 0.712
  (2/log2(7) = 0.7124), so the column sums to the stated DCG 6.861.
- Corrected worked-table cell: rank 2 ideal contribution 1.892 to 1.893
  (3/log2(3) = 1.8928), so the column sums to the stated IDCG 7.141.
- Added citation s2 (BEIR) to "Some collections judge fewer than two relevant
  documents per query," which BEIR owns; left s6 (Craswell) on the click-log
  clause it owns.
- Changed the orientation semicolon to a period ("... retrieval systems. MTEB
  takes both its datasets and that metric from BEIR.").

## Decision

approve. The argument is sound and correctly narrow, the two table-cell
arithmetic errors and the miscited clause are fixed, and the proof runs to
BLOCK: 0 with links included. No different argument is needed.
