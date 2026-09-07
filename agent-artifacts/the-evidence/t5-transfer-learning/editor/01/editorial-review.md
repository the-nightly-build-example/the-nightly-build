# Editorial review: the-evidence/t5-transfer-learning (editor/01)

## Skeptic

Thesis: T5's contribution is two separable things people merge into one. The
text-to-text interface (every task cast as text-in, text-out, one loss and one
decoder) held and is still how the model is addressed today. The narrower
empirical claim, that the encoder-decoder architecture is the one to build, won a
controlled comparison at modest scale but did not survive the field's move to
larger decoder-only models. So T5 is cited for a "winning recipe" broader than
what it showed; it reached the best result of its time on 18 of 24 tasks and lost
all three WMT translation tasks.

Claims it stands on, and how each held:

- **Text-to-text framing, with worked examples.** The four Figure 1 examples
  (translate, cola, stsb, summarize) match the evidence record verbatim, as does
  the STS-B trick (round to nearest 0.2, 2.57 trained as the string "2.6"). The
  table rows match. Held.
- **C4 scale and cleaning.** Paper's ~750 GB (Sec. 2.2), released 806.87 GiB /
  ~365M examples / 6.21 TiB uncleaned (TFDS), ~20 TB/month Common Crawl (Sec. 1),
  seven-eighths discarded (computed from the TFDS figures). All trace to the
  record and to the owning source. Held. One unit slip fixed (see Edits).
- **The controlled comparison and the encoder-decoder finding.** Change one
  ingredient at a time; encoder-decoder best, ~2x the parameters of encoder-only
  or decoder-only at similar compute (Sec. 4). Matches the record. Held.
- **Scale in tokens, not compute.** Baseline ~34B, BERT ~137B, RoBERTa ~2.2T,
  final ~1T (~32x). The article correctly refuses a flops-and-days figure the
  paper never states. 11B shape (d_model 1024, d_ff 65,536, 128 heads) confirmed
  against the paper and, independently, the released config.json (opened; values
  match). Held.
- **Results and the translation loss.** GLUE 90.3/89.4, SuperGLUE 88.9/84.6,
  SQuAD F1 96.22/95.5, WMT EnDe 32.1/33.8, EnFr 43.4/43.8, EnRo 28.1/38.5, SOTA
  18/24, all against the previous best as of 24 Oct 2019. Every figure matches
  the record and Table 14. The verbatim caveat quote matches (p. 39). Held.
- **Present-day reckoning.** 2019-era scores since surpassed, some above cited
  human baselines; decoder-only consolidation; Flan-T5 (2022) as later
  instruction-tuning work the original paper did not study. All supported. Held.

Citations: I opened all seven hrefs as printed. Each resolves and lands on the
source it claims. Display-text descriptors match their owning primaries (JMLR
2020 / Raffel et al. / nine authors confirmed; arXiv v1 submitted 23 Oct 2019;
TFDS c4/en 806.87 GiB and 6.21 TiB confirmed; config.json values confirmed;
Flan-T5 abstract quote confirmed; HF T5 docs prefix quote confirmed). The
`data-nb-kind` labels hold: six primaries (the paper, the preprint, the released
dataset, the released config, the code repo, the Flan-T5 paper) and one secondary
(HF docs), meeting the series floor of 6 sources / 3 primary / 1 secondary.

Breaks found and handled (all fixable in place; none required new reporting):

- The 11B "second place" for decoder-only was an unsupported ranking. The record
  establishes only that encoder-decoder worked best, not that decoder-only ranked
  second. Recast to "the decoder-only design that comparison passed over."
- "the paper's most-cited line" is an unsupported citation-frequency superlative.
  Replaced with a claim the record and commission do support (the finding T5 is
  still cited to settle), which also bookends the later "did not settle the
  architecture question at scale."
- "the wins were not marginal" is contradicted by the article's own printed
  figures: GLUE +0.9 and SQuAD F1 +0.72 are narrow. Cut; the numbers stand on
  their own.
- The 2019/2020 provenance was muddled ("In 2019 ... published," cited to the
  2020 JMLR version) and the 67-page count was attributed to the arXiv preprint,
  whose page count the abstract page does not state. Rewritten so the October
  2019 preprint carries the arXiv cite and the 67-page JMLR paper (pp. 1-67)
  carries the JMLR cite.

No central-claim break, no evidence gap, nothing routed to the researcher.

## Cut

Ran the slop pass over body, display text, captions, and furniture prose. The
piece is mostly clean and concrete; the failures clustered at edges and in
exposition self-narration, which the review brief flagged (only the two bookends
may address the reader).

Cuts and rewrites (about a dozen sentences touched, net trim):

- **Borrowed phrasing.** "The four examples the paper puts on its first page
  carry the whole idea at a glance" lifts "carry the whole idea at a glance"
  straight from the evidence record's asset note. Rewritten to the plain fact
  ("The paper puts all four in the diagram on its first page").
- **Invented negative parallelism.** "This is not a historical curiosity" sets up
  a strawman; deleted (the real content, that you still address T5 this way,
  stands alone).
- **Empty edges.** "and the two are not the same" (restates "larger claim"),
  "and it is what the paper actually contributes" (restates the section opener),
  and "The paper is candid about it" (the quoted caveat already shows it) were
  each cut.
- **Self-grading / method narration.** "the honest way to state the scale is in
  tokens" grades the method; recast to state it plainly. "in the same spirit as
  the two corpus sizes" narrates the article's own structure; cut.
- **Reader-address / exposition signposts in the body.** "Start with the easy
  case" -> "Translation is the easy case"; "The third row is the one worth
  slowing down on" -> "The third row is the odd one out"; "it is worth keeping
  them straight" cut; "When you see a figure attached to T5, ask whether ..."
  recast as a statement, not an instruction to the reader. Generic instructional
  "you" (how the model is used) is left in place: it matches the voice-guide
  exemplars and describes the subject rather than gesturing at the lesson's
  reader.

Punctuation: four semicolons joining independent clauses were replaced with the
plainer period the editorial direction defaults to. No em-dash count issue (none
in prose).

Formula check against the recent-pattern notes: the dek was the one hit. It read
"Google's 2019 study built a 750-gigabyte web corpus and crowned a single
encoder-decoder Transformer ... the architecture the field soon abandoned" — the
banned "<Authors>'s <year> paper did X and Y" skeleton with "Google's 2019 study"
swapped for "Raffel et al.'s 2020 paper," and "abandoned" overstated the record's
"consolidated on / mostly stopped using." Rewritten to lead with the surprise and
match the body's strength: "Google's controlled bake-off, run on 750 gigabytes of
web text the team cleaned itself, crowned the encoder-decoder architecture that
large language models would soon move past." Headline, section headings, and the
other edges are clear of the flagged molds.

Furniture: two tables and one labeled note, all documented components used
correctly (the note's "The paper's own caveat" label names the move and carries
the verbatim quote with `nb-note-who`). Figure 1 rendered as a two-column table
rather than a captured asset is a sound call: the content is text, the table
preserves all four input/output pairs verbatim as the evidence crop guidance
required, and no clean PDF capture was in hand. No component is doing no work; no
missing component would help.

## Reader

Read straight through, the piece gives the reader something no single source
does: it holds the paper, its released artifacts, and later work side by side to
separate what T5 demonstrated (a text-to-text interface, and an encoder-decoder
win at modest, matched scale) from what it gets cited to have settled (the
architecture question for the scale the field later reached). A reader finishes
able to say what T5 measured, how big the study was, what "text-to-text"
concretely means down to a number printed as a string, and when a T5 citation is
carrying more than the paper showed. That matches the draft-handoff's
original-work sentence, and both survive. The prose sits closer to the
voice-guide exemplars than to a median summary: it puts the literal case first
(the STS-B number-as-text, the calculator, the token comparisons) and reports the
translation shortfall at the strength the paper gives it rather than rounding up.
The headline, read as the largest claim, is defended by the body: T5 did recast
its tasks as text-in/text-out, and it did lose all three translation tasks.

## Edits

- Rewrote the dek (both the rendered dekline and nb-meta `dek`) to break the
  banned mold and drop the "abandoned" overstatement.
- Rewrote the opening two sentences so the October 2019 preprint carries the
  arXiv cite and the 67-page JMLR paper carries the JMLR cite (fixes the
  2019/2020 provenance and the page-count attribution).
- Cut "and the two are not the same" (orientation close).
- "Start with the easy case. To translate, you feed" -> "Translation is the easy
  case. You feed".
- "The four examples the paper puts on its first page carry the whole idea at a
  glance" -> "The paper puts all four in the diagram on its first page".
- "The third row is the one worth slowing down on" -> "The third row is the odd
  one out".
- Deleted "This is not a historical curiosity."
- "and it is worth keeping them straight" cut from the paper-vs-download
  sentence.
- "6.21 terabytes" -> "6.21 tebibytes" (TFDS reports TiB; the article already
  used "gibibytes" for 806.87).
- "When you see a figure attached to T5, ask whether ..." -> "A figure attached
  to T5 belongs either to ... and the two do not always match."
- Cut "and it is what the paper actually contributes" (bake-off).
- "its answer is the paper's most-cited line" -> "its answer is the one T5 still
  gets cited to settle".
- "the honest way to state the scale is in tokens" -> "the scale is given in
  tokens instead"; "the flops-and-days form you sometimes see quoted" -> "the
  flops-and-days form sometimes quoted".
- "in the same spirit as the two corpus sizes" cut.
- "T5's 18-of-24 result is real, and the wins were not marginal" -> "T5's
  18-of-24 result is real".
- Deleted "The paper is candid about it."
- "the decoder-only design that comparison put in second place" -> "... that
  comparison passed over".
- "which the authors report reach strong few-shot performance" -> "which their
  authors report reach ..." (the referent is the Flan-T5 authors, not T5's);
  "instruction finetuning" -> "instruction fine-tuning" (hyphenation consistent
  with the rest of the body; the source title keeps its own spelling).
- Four semicolons between independent clauses changed to periods (pretraining/
  adapting; "Nothing surprising there"; scaling-work/T5's-number; "That idea
  held").

## Required work

- **orchestrator:** Re-stamp before proofing. The edits are a net cut (the draft
  sat at the 2200 ceiling), so `nb stamp` needs to refresh `words` and
  `reading_minutes`; `nb check` then confirms. The nb-meta `dek` was updated to
  match the new dekline, so the two remain identical.
- **writer:** none required.
- **researcher:** none required.

## Decision

approve — the thesis holds, every figure and citation checks out against the
owning sources, and the remaining prose and provenance issues were fixable in
place; only a re-stamp and proof remain.
