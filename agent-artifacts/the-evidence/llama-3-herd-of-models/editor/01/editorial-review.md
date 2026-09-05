# Editorial review: the-evidence/llama-3-herd-of-models (editor/01)

## Skeptic

Thesis: the Llama 3.1 report is two documents at once, an unusually detailed
engineering record and a company scoring its own product, and the reader can
tell the disclosed figures from the selected framing. The piece stands on four
claims.

1. Meta scored the benchmark comparison itself and picked each rival's best
   result. The report's own words in §5.2 ("we evaluate the performance of
   other models ourselves and compare the results with the reported numbers,
   selecting the best score") carry this. Verified against the full report at
   arxiv.org/html/2407.21783v3.

2. On the general, code, and reasoning rows the closed models usually hold the
   top score, so the table shows parity-to-slightly-behind, not a lead. Every
   printed Table 2 value (MMLU, MMLU-Pro, HumanEval, MATH, GPQA, GSM8K, all
   four columns) matches the evidence record's direct read of the PDF. The best
   cell on MMLU, MMLU-Pro, HumanEval, and GPQA belongs to Claude 3.5 Sonnet;
   the 405B leads GSM8K, which the piece concedes. The report's own §5.3
   concession ("trails Claude 3.5 Sonnet in capabilities such as coding and
   reasoning") is quoted accurately.

3. The report cannot certify four of its headline benchmarks. Table 15 prints
   dashes for MMLU, MMLU-Pro, HumanEval, and MBPP, and the report explains why:
   "even with higher thresholds, 8-gram overlap gives such high contamination
   scores that it is impossible to get a good performance gain estimate." All
   four sit in the flagship Table 2. This is the piece's original move, reading
   Table 2 against Table 15, and it is supported by the record and not pushed
   past what the tables show. The draft-handoff's original-work sentence claims
   exactly this, and the article delivers it.

4. "Open" means open weights under a conditional community license, and "open
   source" is a contested label. The license text (opened directly) grants
   weights and code, not training data; requires the "Llama" naming and "Built
   with Llama" attribution; and carries the 700M-MAU carve-out. It contains no
   ban on training a competitor on Llama outputs, so the piece is right that the
   Llama 2 prohibition is gone. Meta's "first frontier-level open source AI
   model" is on the launch blog; the OSI rejection is on the OSI post.

Pushing hardest on claim 4, I opened the OSI post twice. The article's position
card said the license "discriminates against groups through the 700-million-user
clause." The OSI post does not ground its point-5 objection in that clause; its
stated discrimination example is the exclusion of persons in the European Union.
The 700M clause is the article's own (correctly sourced, in the body, to the
license). Attributing it to OSI as OSI's discrimination reasoning is a
miscitation. The right source is at hand and settles it, so I removed the false
mechanism and left OSI's three OSD points stated as OSI states them. No other
break survived: every figure, quote, and direction checks against the owning
primary.

Display text and labels: the headline names its actor (Meta) and states a
finding the contamination section defends. The dek adds the self-scoring fact
and names three of the four blanked benchmarks; it restates nothing the headline
already committed. The Llama 3 vs 3.1 hazard is handled exactly, using Table 1's
own correcting line, in the orientation and throughout. data-nb-kind audit: five
primary (abstract, full report, model card, license, launch blog) and two
secondary (OSI, LMSYS/LMArena); LMArena and OSI are correctly secondary, and the
launch blog is correctly primary as the owner of Meta's own positioning
language. All seven source hrefs resolve to the document each cites (report HTML,
GitHub model card and LICENSE, Meta blog, OSI post, LMSYS style-control post).

## Cut

The prose is clean and concrete; the slop pass turned up punctuation and two
signposts rather than empty conclusions.

- Chained semicolons in the contamination section (HellaSwag / GSM8K / SQuAD)
  broke the house rule against chaining. Split into three sentences.
- One antithesis semicolon ("The weights are public; the data...") converted to
  the house-default period.
- "Now line that against the previous section" narrated the article's own
  structure and addressed the reader, which the body may not do. Deleted; the
  next sentence already makes the cross-table connection.
- "Two checks from outside Meta's own scoring" mislabeled Meta's own
  human-preference evaluation as external. Changed to "beyond the benchmark
  table," which is true of both the human eval (Meta's) and LMArena
  (independent).
- Trimmed two low-content clauses by the delete test: "so the training pulled a
  large amount of electricity" (magnitude, no figure; the emissions numbers
  carry it) and "and it pays to be exact about what it grants" (method
  narration).

Formula check against the recent-pattern notes: the opener is the piece's own
(no striking-number or reversal lead), the dek matches no banned mold, and the
close is a takeaway bookend with no "How much survived" heading or holds-up
grid. Three section headings, though, shared the prior article's "The NOUN
[subject] VERB" construction. Broke one, retitling "The scale Meta put on the
record" to "What the 405B took to build," which keeps the section's own nouns
and a different build. Furniture earns its place: two tables where the numbers
are the point, a stat strip of the headline figures, one position card. No
borrowed phrasing from the voice-guide quotations, and no prompt leakage: the
"engineering record / scorecard" framing is the article's own, evidence-grounded
wording of the angle.

## Reader

Read straight through, the piece gives what no single source hands over: that
Meta ran its rivals' evaluations itself and kept their best scores, that the
405B is competitive-but-behind on the hardest tasks rather than a clean winner,
and that Meta's own contamination check cannot vouch for four of the benchmarks
in its headline table. The Table 2 against Table 15 reading is the article's, and
it matches the draft-handoff's original-work claim. The prose sits closer to the
voice-guide exemplars than a median summary: real figures where an adjective
would do (405B, 15.6T tokens, 3.8x10^25 FLOPs, 30.84M GPU-hours), the standing
objection attributed rather than dramatized, and the desk's judgment stated
plainly with its mechanism beside it ("rests on Meta's own scoring of its own
rivals, and the numbers in it do not carry that far"). The headline reads true
as the largest claim: Meta's own report cannot certify four of its headline
scores, and the piece proves it from the report's own table.

## Edits

- Retitled section heading "The scale Meta put on the record" to "What the 405B
  took to build" (break the recent heading formula).
- Removed "through the 700-million-user clause" from the OSI position card; the
  OSI post grounds its discrimination point in EU exclusion, not that clause.
- Split the chained-semicolon HellaSwag/GSM8K/SQuAD sentence into three
  sentences.
- Changed the semicolon in "The weights are public; the data..." to a period.
- Changed "Two checks from outside Meta's own scoring" to "Two checks beyond the
  benchmark table" (the human eval is Meta's, not external).
- Deleted "Now line that against the previous section" (self-narration; the body
  addresses no reader).
- Cut "so the training pulled a large amount of electricity" and rephrased "it
  emitted" to "the training emitted" for a clear referent.
- Cut "and it pays to be exact about what it grants" (method narration).

## Required work

None. Every issue was fixable directly from the evidence record and the sources
opened in the first read; nothing requires new reporting, a source asset, chart
provenance, or a redraft.

- researcher: none.
- writer: none.
- orchestrator: none beyond the standard post-edit stamp + check. My edits are
  prose-only and drop roughly thirty words, leaving the piece inside the
  1200-2200 band; re-stamp will refresh the word and reading-minute counts in
  nb-meta.

## Decision

approve. The claims hold against the owning primaries, the one attribution error
is corrected, and the slop and formula passes are resolved by direct edit.
