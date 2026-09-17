# Editorial review: the-evidence/gpt-1 (editor/01)

## Skeptic

Thesis: a single 2018 OpenAI report introduced generative pre-training, pre-train
one model on unlabeled text and then fine-tune it per task, beat purpose-built
systems on nine of twelve datasets, and left a two-part recipe whose pre-training
half every later GPT kept and whose per-task fine-tuning half they dropped.

The claims it stands on, and how each held:

- **Nine of twelve datasets improved (headline and results).** Holds. The
  evidence record and the paper's abstract and Sec. 4.2 both give "9 out of 12."
  The losses are named exactly as the record has them: RTE 56.0 vs 61.7, MRPC,
  SST-2 91.3 vs 93.2, called "competitive." GLUE is given the body's 72.8 vs 68.9,
  not the intro's unreconcilable 5.5%, exactly as this round required. CoLA 45.4
  vs 35.0 checks out. The spread claim (8.9 down to 0.6) matches the Numbers
  block.

- **The paper states no total parameter count; "117 million" is the GPT-2
  report's figure.** Holds, and is handled well. The article says the figure
  "does not appear in this paper at all" and sources it to the 2019 GPT-2 report
  ("equivalent to the original GPT"), cited to s3. The later reuse of "roughly 117
  million" for the scaling arc is hedged and carries the s3/s5 citations, so it
  does not reintroduce the figure as GPT-1's own. This was the round's hardest
  point and the draft does not slip on it.

- **The corpus is "over 7,000 unique unpublished books," not the origin's
  11,038.** Holds. The article cites the paper's own phrase to s1 and the origin
  count to s2, flags the gap as unexplained, and refuses to blend them. Matches
  the Contradictions note.

- **The ablation shows pre-training carried the result; the auxiliary objective
  was a wash.** Holds. 74.7 to 59.9 without pre-training (~15 points), and the
  auxiliary next-word objective held 74.7 against 75.0 without it. Both match the
  Numbers block and the record's honesty warning.

- **The surviving half is pre-training; fine-tuning and input transformations
  were dropped.** Holds, cited firsthand: GPT-2 "without any parameter or
  architecture modification" (s3), GPT-3 "without any gradient updates or
  fine-tuning" (s5), GPT-4 discloses no architecture and adds RLHF (s6). The Liu
  survey names the "pre-train, fine-tune" to "pre-train, prompt, and predict"
  shift from outside OpenAI (s8).

I pushed hardest on the point the piece most wants to keep, that the reception
read GPT-1 as a paradigm shift. The article holds the "ImageNet moment" reception
(Ruder, s7) apart from the modest 2018 margins in as many words: the reading "was
about the method's reach," "ran well ahead of GPT-1's own tables, where several
gains were under two points," and "was never a claim that the 2018 margins
themselves were large." No sentence lets the paradigm framing borrow the small
numbers' authority. This is the round's central risk and the draft closes it.

Display text, descriptor by descriptor: headline, dek, and all five subheads
check out against the record. The one break was in the **dek**, which claimed the
preprint "introduced the per-task fine-tuning." The record does not support GPT-1
inventing fine-tuning; it groups GPT-1 with ELMo and ULMFiT, and ULMFiT already
fine-tuned a pre-trained language model. The commission also treats fine-tuning
as taught, pre-existing ground. Fixed directly (see Edits) to "paired it with,"
which the paper's own two-stage method supports, and tightened "pre-training" to
"generative pre-training" to name the paradigm the sources actually establish.

Sourcing labels: all eight `data-nb-kind` values match the record. The two
secondaries (Ruder, Liu) are correctly outside the authoring lab; the six
primaries own the numbers cited from them. The BERT head-to-head is linked in
Background only, not rebuilt; the decoder, tokenization, and embeddings are
linked, not re-taught. Every load-bearing citation URL resolves 200 as printed
(the two cdn PDFs, thegradient, and the arXiv `/abs/` pages), and the Fig. 1
locator deep-links page 4 of the paper.

## Cut

The article is lean and specific; the slop pass found signposts at edges rather
than pattern writing. Direct cuts:

- "That phrasing is worth pausing on" — a lecture-the-reader signpost. The
  11,038-vs-7,000 discrepancy makes the point itself; deleting the pointer loses
  no fact.
- "The field saw the shape of this early" — an empty paragraph opener ("the X saw
  the shape of this early"). The concrete Ruder sentence that follows carries the
  reception claim without it.
- "and the order matters" — a signpost promising significance the next two
  sentences deliver on their own (stage two depends on stage one).

That is three edge sentences or clauses failing the delete test, all at
paragraph or section seams, none in the middles. One punctuation repair: a
semicolon joining two independent clauses ("...appeared on arXiv; the version
OpenAI posted...") became the period the editorial direction prefers.

Furniture: the "In plain language" note is the documented note component used for
its documented purpose, a plain-language rendering of the work's claim, and it
does real work reframing next-word prediction as "teaching a model to write." The
Fig. 1 source asset and Fig. 2 chart are the documented figure component. None
reads as a filler block; the piece is not over-furnished.

Edge and heading rhythm against the recent-pattern notes: no lead-figure-plus-
reversal dek, no comma-triad-with-"and" dek, no "[Claim]. [Terse rebuttal]."
headline mold, no "The one number in the paper" heading, and no full-sentence-
with-a-figure rhythm repeated across subheads. The five headings are built five
different ways (time clause, imperative pair, "one X for four Y," "N did, M did
not," bare noun phrase). No echo to break.

Voice: the prose matches the guide's register, plain and teacherly, landing
figures with their source and no adjective (the Somers move) and holding the two
times apart without triumph or alarm (the Lee calibration). I compared the
distinctive phrasing against the guide's quoted exemplars and found no borrowed
clause. Grammar and syntax are clean throughout, including display text and
furniture.

## Reader

Reading what survives straight through, what I have that the sources alone would
not give me: GPT-1's recipe split into two halves and each traced across the
GPT-2, GPT-3, and GPT-4 reports, so I can see that the half the paper labors over
is the half its own line discarded, while the half it treats almost in passing is
the one that lasted. The GPT-1 paper alone does not draw that line; the later
reports alone do not point back to it. The draft-handoff's original-work sentence
claims exactly this split, and it survives intact in the body and the takeaway.
The prose sits closer to the voice-guide exemplars than to a median summary: it
teaches from worked cases (the entailment sequence before the general shape) and
commits to the specific number over the adjective. The headline, read as the
largest claim, is accurate, actor-named, and specific, and is not the paper's
recent two-sentence mold.

## Edits

- Dek (rendered dekline and nb-meta `dek`, kept identical): "made pre-training
  the default ... and introduced the per-task fine-tuning" changed to "made
  generative pre-training the default ... and paired it with the per-task
  fine-tuning." Removes an unsupported invention claim; names the paradigm the
  sources establish.
- Orientation: "...never appeared on arXiv; the version OpenAI posted is the
  release." semicolon changed to a period.
- Recipe: "The method has two stages, and the order matters." cut to "The method
  has two stages." (signpost removed).
- Recipe/corpus: cut the signpost "That phrasing is worth pausing on."
- What-survived: "the task-specific fine-tuning that GPT-1 spends its longest
  section building" changed to "...that GPT-1 builds out in such detail." Removes
  an unverified superlative about the paper's structure (the record does not
  establish which section is longest); keeps the supported contrast with "almost
  takes for granted."
- What-survived: cut the empty opener "The field saw the shape of this early."

## Required work

- **Orchestrator:** re-stamp and re-prove. The dek changed and the cuts reduced
  the body by several sentences, so nb-meta `words`/`reading_minutes` need the
  standing re-stamp, and the link/proof pass should be re-run after the direct
  edits. No content gap remains for the researcher, and no reporting, recrop, or
  chart-provenance work remains for the writer.

## Decision

approve — every round-focus item (parameter attribution, corpus figure, results
honesty, reception held apart from the margins, taught ground linked) holds, and
the visual evidence and chart provenance are honest and match the record; the
remaining fixes were all inside editor scope and are made.
