# Editorial review: the-evidence/seq2seq (editor/01)

## Skeptic

Thesis stated from the draft alone: the 2014 seq2seq paper gave the field a
durable thing (the encoder-decoder shape and the "sequence to sequence" name)
and a modest thing (one direction of one language pair, a single model that sat
below the statistical baseline, a headline number assembled by ensembling), and
the fixed-length vector it packed each sentence into was not a limitation the
paper conceded. The claims it stands on:

1. The encoder-decoder shape and name endured. Supported: the T5 line (s6) and
   the textbook framing (s4) carry it, both verified on the live pages.
2. The measured result was small and specific. This is the round's BLEU-
   decomposition focus. Re-derived against the record, descriptor by descriptor:
   single reversed model 30.59, below the SMT baseline 33.30; the 34.81 headline
   is five reversed networks voting at beam 12; 36.5 is that same ensemble
   re-ranking the SMT system's 1000-best list, not direct LSTM output. Prose,
   stat strip, and the Table 1 furniture all label these distinctly. The draft
   never presents 34.81 as a bare single-model number. Table rows (26.17 forward,
   30.59 reversed, 33.00 ensemble beam 1, 34.81 ensemble beam 12, 36.5 rescoring)
   match the evidence Numbers block exactly.
3. The reversing trick bought the largest single-model gain and signals strain.
   Figures match: perplexity 5.8 to 4.7, BLEU 25.9 to 30.6 (Section 3.3), and
   the paper's own "we do not have a complete explanation to this phenomenon" is
   quoted verbatim. The synthesis that a hand-patch of this size shows the fixed
   vector straining is the record's Contradiction 3, stated as a narrow
   admission, not overclaimed into the paper conceding a ceiling.
4. The corrected angle. Pushed hardest here, since it is the round's focus. The
   piece does NOT have seq2seq concede the bottleneck. It quotes the opposite
   claim ("We were surprised to discover that the LSTM did well on long
   sentences," Section 3.7, verbatim) and reassigns the diagnosis: the bottleneck
   conjecture to Bahdanau, Cho, and Bengio (s2), the measured degradation to Cho
   et al. (s3), explicitly noting the degradation was measured on a single-layer
   model without reversing, not on Sutskever's deep reversed system. This is the
   honest lineage the brief demanded, and it holds.

Scale figures re-checked against the record and all correct: ~384M parameters,
1000-number layers, 12M pairs (304M English against 348M French, direction
right), 160k source / 80k target vocab (input/output assignment right), 8 GPUs
~10 days.

Display text, descriptor by descriptor: headline "Google packed a whole sentence
into a single vector" is accurate (Google authors, fixed-vector encoding) and
breaks the series' quantified-result mold. Dek carries no banned mold and adds
the afterlife rather than restating the headline. Every subhead is a concrete
step in the piece's own nouns; none uses the comma-plus-"and" join. Named people
and affiliations check out: Sutskever, Vinyals, Le as Google researchers;
Bahdanau, Cho, Bengio as the different, same-month group.

data-nb-kind audit: s1/s2/s3/s5/s6 primary (each owns its claim), s4 secondary
(independent textbook). Source policy met (6 sources, 5 primary, 1 secondary).

Citations opened as printed. All six external hrefs land on the source itself:
the three arXiv abstract pages return the right titles and authors; d2l.ai
carries the exact "variable-length sequence as input... fixed-shape hidden state"
sentence; the Vaswani "dispensing with recurrence and convolutions entirely" and
the T5 "text-to-text format" lines are confirmed live. Every quoted fragment in
the draft is a verbatim substring of its source. The two internal
attention-is-all-you-need links are the published cross-links and were not
probed. No miscitation, no broken link, no sourcing failure to route.

## Cut

A dedicated slop pass over body, display text, and furniture prose found no
sentence that fails the placeholder test. The constructions that would usually
flag came up clean on inspection:

- "The durable part was the shape, not the score" is negative parallelism, but it
  corrects a real, named misconception (the honest-scale premise that the paper
  is invoked for a result its numbers do not support), so the contrast is earned.
- "So what did 2014 actually establish?" is a question the same paragraph
  answers, the earned kind the voice guide sanctions, not a Betteridge hedge.
- The bookend opener addresses the reader and states what the lesson will teach,
  which the lesson template allows for its two cards; both cards hold to this
  lesson's particulars (the fixed vector, the reversing hack, the attribution),
  not generic importance.

Edge pass (first/last sentences read out of order): every section edge carries a
fact or a reasoning step; none leans on its neighbors. The article's last
sentence is a balanced antithesis (what the paper is cited for against what
attention removed) that states the conclusion the argument built, so it stays.

Prompt-leakage pass against commission, briefs, and voice guide: no planning
label, selection rule, or assignment-fulfilled claim survives in the prose. The
opener's learning-objective sentence is the bookend's sanctioned function, phrased
in the article's terms, not a lifted instruction.

Formula pass against the recent-pattern notes: headline breaks the quantified-
result mold; dek avoids the three banned molds; no heading uses the comma-and
join; the closer lands in the takeaway bookend rather than a retired Verdict
block. No borrowed phrasing from the voice guide's quoted writers.

Furniture: stat strip and Table 1 both sit in the scale section and carry
different cuts (headline scale versus the full BLEU decomposition), so the
adjacency is justified rather than a stack of blocks; the note promotes the one
pivotal quote for deliberate emphasis. No component is decorative, and no
missed-component gap rises to blocking. The encoder-decoder diagram the evidence
flags would illustrate the mechanism but would not help the reader test the
honest-scale or attribution arguments the piece actually turns on, and the prose
plus the nutrition-label analogy carry the mechanism cleanly, so I did not
request it.

One edit made: a table caption joined two independent factual clauses with a
semicolon where the house punctuation default is a period. Changed to a period.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: I can now say what the 2014 seq2seq result
actually was (a single-language-pair LSTM translation that a single model ran
below the statistical baseline, pushed past it only by a five-model ensemble),
that it leaned on a reversing hack the authors could not fully explain, and,
crucially, that the fixed-vector bottleneck the field pins on this paper was
named and measured by a different same-month group while this paper claimed the
opposite for its own model. That correction and reorganization is exactly the
draft-handoff's original-work claim, and both survive the read. The prose sits
closer to the voice-guide exemplars (the vector introduced through a picture the
reader already holds, the baseline given before the paper's own number, real
figures delivered dryly) than to a median summary.

## Edits

- Table 1 caption: replaced the semicolon between "a five-network ensemble" and
  "A single network reaches 30.59" with a period, per the house punctuation
  default that the plainer mark governs two independent clauses.

## Required work

None. No item routed to researcher, writer, or orchestrator.

## Decision

approve. The corrected angle holds, the BLEU decomposition and every scale and
reversing figure match the record, all citations resolve to their sources with
verbatim quotation, and the one prose issue was a punctuation fix within remit.
