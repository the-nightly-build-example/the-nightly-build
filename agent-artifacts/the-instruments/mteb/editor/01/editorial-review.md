# Editorial review: the-instruments/mteb (editor/01)

## Skeptic

Thesis: the number that sorts the MTEB leaderboard is one flat average over
datasets scored in unlike metrics, so a high rank tells a retrieval buyer less
than it seems to, and the maintainers themselves have moved to repair the two
places it bends. The piece stands on four claims.

1. **The overall score is a plain unweighted average across all datasets, and the
   leaderboard sorts on it.** Held. The MTEB paper (s1) owns it; the counts (8
   task types, 58 datasets, 112 languages, 33 models) match the abstract I opened
   and the evidence record's v3 scope. The per-task metric table matches the
   record's Numbers section descriptor for descriptor, and the dataset counts sum
   to 58. The 56-vs-58 English-table nuance is stated correctly (the two
   multilingual bitext sets drop out).

2. **The average weights a task by its dataset count, not its importance:
   retrieval 15, summarization 1.** Held, and attributed to the original 2022
   authors' own limitations appendix, which is where the record places it. The
   quote in the note is verbatim against the record. This is the correctness spine
   the review-brief flagged, and the piece gets the attribution right: imbalance
   is the authors' own day-one limitation, not a later discovery.

3. **A model can top the mean while being ordinary at retrieval.** Held as a
   property of averaging, framed in both directions and never as a named scandal,
   which is exactly what the record requires (no single chart-topper weak at
   retrieval is documented). The Modal quote (s3, secondary) carries the
   opposite-direction case verbatim. The headline says "can," a possibility the
   mechanism supports; it does not imply a named case. Nothing here needs the
   researcher.

4. **The authors dismissed contamination in 2022, then reversed by 2025 and
   rebuilt the benchmark.** Held, and told as a self-reversal over time, not a
   steady critique. The 2022 dismissal quote (s1) and the 2025 same-source
   training-split mechanism (s5) are verbatim against the record. MMTEB is
   described as adding Borda-count ranking and a category-weighted average on top
   of the mean, with the flat average still present — matching the record's
   Contradictions caution against saying MMTEB "removed" the mean. RTEB's private
   datasets (s8) and the zero-shot exclusion of MS MARCO and Natural Questions
   (s7) are correct.

Citations: I opened all eight hrefs as the article prints them. Every one
resolves and lands on the source itself. s1, s5, and s7 land on the arXiv
abstract pages for their papers (the source's own landing); the load-bearing
quotes live in the full text and are verified verbatim in the evidence record.
Every `data-nb-kind` matches the record's kind (six primary, two secondary),
meeting the series floor.

One discrepancy, the writer's flag (1): the e5-mistral 95% zero-shot / ~5% leak
figure is computed on the legacy English MTEB (v2), while the rest of the piece
is pinned to v3, and the draft called it "5% of the benchmark's datasets" as if
it were the v3 benchmark under discussion. The record scopes it to "legacy
English MTEB." I fixed this in prose (see Edits) by naming the legacy English
benchmark, using only wording the record carries. The figure stays: it is the
maintainers' own worked illustration of the zero-shot score, which is what the
section teaches, and scoping it is enough. No researcher work.

## Cut

Slop pass, every sentence including display text and the two notes. The prose is
disciplined: em-dash count is 0, no banned terms, no vague attribution, no
puffery, no decorative-analysis copulas. Three sentences drew scrutiny and two
were cut.

- **"Two costs follow"** (end of the construction section): a forward signpost
  that fails the delete test, and imprecise besides — only one of the two
  following sections (imbalance) is a cost of averaging; contamination is a
  separate weakness. Cut. The section now lands on its earned closer, "The single
  MTEB number exists only by averaging across that difference," and the reversal
  section's "The second weakness was not" still reads cleanly against the
  imbalance section just before it.
- **"The concern is not only the maintainers' own second-guessing"**: a
  negative-parallelism edge sentence at a paragraph seam whose only content — that
  outsiders corroborate — is delivered by the "Outside groups note..." sentence
  right after it. Cut.
- **"Look again at the last column of the table"**: the body addresses the
  reader, which the lesson template reserves for the two bookends. Rewritten to
  "The table's last column shows the imbalance: retrieval holds 15 datasets,
  summarization holds 1," which carries the fact, points to the table, and drops
  the second person. The semicolon also became the plainer colon-and-comma.

Edges, deks, headings against the recent-pattern notes: the dek is a single claim
with a participial tail, not a two-clause "and/but" dek and none of the three
banned molds. The four section headings are built in the piece's own nouns, none
open with How/What/Where, and the contamination section is named for what it
argues ("The authors changed their minds about contamination") rather than the
desk's late "when the leaderboard rewrote its own answers" reveal. The negative
contrasts that remain ("not a hidden scandal," "not evidence that the number is
fake," "not the same as being the best model for one particular job") each
correct a real, named misconception the piece is built to answer — the cynical
reading the voice guide's Harford register exists to head off — so they stay.

Prompt-leakage check against commission and brief: the "top the mean, ordinary at
retrieval" framing is the piece's own sourced thesis, not lifted instruction; no
planning labels or assignment-fulfilled claims appear. Borrowed-phrasing check
against the voice-guide exemplars: the Luu "no single dimension" idea is applied
in the article's own words ("Text embedding has no single dimension along
which..."), not lifted.

Furniture: a metric table plus two labeled quote-notes across ~2000 words is
proportionate and reads as a continuous lesson, not a stack of blocks. The
evidence record offered a Figure 2 (mean-vs-zero-shot scatter) source asset for
the contamination point; the prose and the e5-mistral worked case carry that
argument without it, so it stays an option for a later pass rather than required
work.

## Reader

Read straight through as the paper's declared reader, someone deciding which
embedding model to trust and meeting the leaderboard number for the first time:
what I have that the sources alone would not give me is the single rank rebuilt
as a chain of folds — a per-dataset metric, a grouping into task types, a flat
mean — with the benchmark's two famous flaws pulled apart by their timelines
(imbalance stated on day one, contamination dismissed then reversed) and a usable
rule at the end (filter the board, judge on your own data). That is the
draft-handoff's original-work sentence, and it survives comparison with the
article. The prose sits closer to the voice-guide exemplars than a median
summary: it gives the usable half of the average its due before showing where it
bends, in the Harford register the guide asked for, and it earns each correction
with a worked case rather than an assertion. The headline, read as the largest
claim, is honest: "can" states a possibility the averaging mechanism supports.

## Edits

- Cut the forward signpost "Two costs follow." at the end of the construction section.
- Rewrote the retrieval-slice opener from "Look again at the last column of the table. Retrieval holds 15 datasets; summarization holds 1." to "The table's last column shows the imbalance: retrieval holds 15 datasets, summarization holds 1." — removing the body's reader-address and the semicolon.
- Scoped the e5-mistral zero-shot figure to its version: "which scores 95% zero-shot on the legacy English benchmark, meaning it trained on only about 5% of that benchmark's datasets."
- Cut the negative-parallelism seam sentence "The concern is not only the maintainers' own second-guessing."

## Required work

None. The two writer flags are resolved: the version discrepancy is fixed in
prose within editing scope, and the retrieval example was already framed as a
mechanism, so no researcher or writer action is outstanding. The orchestrator
stamps after these edits.

## Decision

Approve — the four load-bearing claims hold against their opened sources, the
timeline and averaging mechanics are told exactly as the record requires, and the
remaining prose and version issues were fixable in place.
