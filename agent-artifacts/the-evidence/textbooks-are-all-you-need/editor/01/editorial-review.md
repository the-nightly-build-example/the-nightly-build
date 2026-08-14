# Editorial review: the-evidence/textbooks-are-all-you-need (editor/01)

## Skeptic

Thesis, stated from the draft alone: phi-1's famous result is real but told at
the wrong size. A 1.3B-parameter model reached 50.6% on HumanEval and kept pace
with code models about twelve times larger, but the headline margin was
concentrated on benchmark problems resembling its own training exercises. On the
paper's own fair test, the non-similar problems, the lead falls to a few points
and reverses under the hardest pruning. And the training data was written by
GPT-3.5 and filtered through GPT-4, so a larger model's scale was relocated into
the data rather than eliminated. Curated data bought efficiency, not the
magnitude the "quality beats scale" slogan claims.

Claims it stands on, and how each held:

- **The scale figures (1.3B params, ~7B tokens, 50.6% HumanEval, 55.5% MBPP).**
  All confirmed against the phi-1 paper and the evidence record. The 12x anchor
  is StarCoder (15.5B / 1.3B = 11.9x). Held.

- **The 17-point headline gap over StarCoder (50.6 vs 33.6).** Confirmed
  arithmetic and both figures against Table 1. The article correctly presents
  this as the plain-StarCoder, full-set comparison the slogan rests on. Held.

- **The central interpretive move: the non-similar column is the fair test, and
  there the margin collapses to ~3 points and reverses.** This is the claim the
  round focus flagged for the hardest test. I checked it against the evidence
  record's Table 3 figures and the committed chart provenance. The four
  thresholds match exactly: retrained phi-1 non-similar 32.3 / 36.6 / 34.5 / 27.1
  against StarCoder-Prompted 29.0 / 32.4 / 31.0 / 31.2. The reversal at the
  hardest pruning (27.1 vs 31.2) is real and correctly reported. Held.

- **Baseline honesty (the sleight-of-hand test).** The 17-point figure is phi-1
  over *plain* StarCoder (Table 1); the non-similar comparison is against the
  stronger *StarCoder-Prompted* (Table 3). This baseline shift is the one place
  the "three points rather than seventeen" contrast could mislead. The article
  discloses it in the sentence immediately before the number ("StarCoder-Prompted,
  the same StarCoder run with a coaching prompt, which scores higher than the
  plain version above"), and the figure legend and caption both name
  StarCoder-Prompted and cite Table 3. Within each section the baseline is
  consistent across prose, caption, and chart. The disclosure is load-bearing and
  it is present, so the contrast is signposted, not hidden. Held; not sleight of
  hand.

- **Distillation, attributed to the owning primary.** The phi-4 report quote
  ("largely distill the capabilities of a teacher model (specifically GPT-4)") is
  verbatim, attributed to source 4 (the phi-4 report), and I opened the arXiv page
  to confirm the id resolves to that report and the sentence is in its abstract.
  The GPT-3.5 authorship of the textbooks and exercises is owned by the phi-1
  paper itself. Held.

- **Scope discipline on GSM1k / Maini.** Both are held to the later phi models
  (phi-1.5/2/3), and the section closes by stating plainly that "None of this
  measures phi-1's HumanEval score." GSM1k is not presented as a verdict on phi-1.
  The "systematic tendency rather than a large one" framing matches the evidence's
  own reading (worst offenders are other model families). Held.

One break found, and fixed directly:

- **A threshold mislabel that contradicted the article itself.** The pruning
  section called tau=0.95 "the strictest threshold" when introducing the 71-of-164
  similar count, then, two paragraphs later, correctly called the same tau=0.95
  "the loosest threshold" when giving its 32.3% score. Both the 71 count and the
  32.3% score sit at tau=0.95 (the evidence record and the chart's own "lower tau
  prunes more aggressively" both fix this). So the same threshold wore opposite
  labels, and the "strictest" one was wrong: tau=0.95 is the least aggressive
  pruning. Corrected "strictest" to "loosest." Value was at hand; no reporting
  needed.

Display text, descriptor by descriptor: headline, dek, and all five subheads
check out against the sources. The headline's actors and figures (phi-1, 12x) are
accurate. There is a mild tension worth naming but not fixing: the headline says
phi-1 matched larger models "mostly on problems like its training set," while the
body concedes it also roughly ties on the non-similar set ("a real result"). The
headline is about where the *dominance* lived; the body adds the nuance that the
*parity* is broader. The headline still commits to what the piece establishes, so
it stands. The two `data-nb-locator` values (Table 1 on the comparison table,
Table 3 on the figure) are correct.

Sourcing: all seven `data-nb-kind` labels are correct under the authorship-and-
stake test. Sources 1-6 are primary (Microsoft, OpenAI, Google, Scale AI own
their claims and benchmarks firsthand); source 7 (Maini) is correctly secondary,
an outside critique of a model he is not a party to. The article's cautious label
"the researcher Pratyush Maini," with no institution asserted, matches the
evidence's note that the page states no affiliation. Source policy is met: 7
sources, 6 primary, 1 secondary. Every citation href was checked; the three
load-bearing ones (phi-1 paper, phi-4 report, Maini) were opened and confirmed to
land on the source itself, and the remaining arXiv ids match the verified record.

## Cut

The prose is disciplined and sits close to the voice-guide register: short
declaratives, one idea per sentence, concede-the-earned-part-first (the Mitchell
move, at "did reach 50.6% ... and curated data is why. But ...") and
claim-with-its-limit (the Luu move, throughout the pruning section). No borrowed
clauses from the Lee, Mitchell, or Luu exemplars survived into the draft; the
piece takes their moves, not their words. Em-dash count is zero. No prompt leakage
against the commission or writer brief: the takeaway's "bought real efficiency ...
did not buy the magnitude" tracks the brief's framing in clause order, but the
point underneath is the article's own evidence-backed conclusion and is stated in
the piece's own nouns, so it stays.

Two sentences failed the slop / delete test and were cut or trimmed:

- A signpost tee-up, "The problems were written by hand for a reason," restated a
  fact established two sentences earlier and only promised a reason the next
  sentence already delivers ("Hand-written problems were meant to sit outside the
  training data"). Cut; the paragraph now opens directly on the reasoning.

- A reader-direction clause, "and it is worth keeping separate from phi-1's code
  result," told the reader how to read rather than reporting. The scoping it
  gestured at is carried substantively by the section's closing sentence ("None of
  this measures phi-1's HumanEval score"). Trimmed to "The later models are where
  independent scrutiny landed."

Everything else at the edges holds. "The scale did not vanish. It moved." reads
like negative parallelism but corrects the article's actual, named misconception
(that a small model is scale-free) and carries a reasoning step, so it stays. The
closer ("the paper's own numbers are where you can see the difference") states the
conclusion the argument built and resolves the opener's promise. Headings are
argument steps in phi-1's nouns and vary in build; none is a comma-and formula.
The dek is built in this piece's nouns (Microsoft, 1.3B, GPT-4 filtered, GPT-3.5
wrote, 50.6%) and avoids the recent "named-authors-reported-N-in-year" mold. The
desk's stock "the paper got its own explanation wrong" reveal is remade in phi-1's
own particulars (overall retrained score versus the non-similar subset), not the
stock framing. Furniture is purposeful and the piece reads as a continuous
article: the stat strip carries the thesis numbers, the table carries the
honest-scale comparison, the one chart carries the reversal. No Verdict block, as
the press directs; the takeaway lands the judgment.

One number was tightened for honesty, not slop: "The phi family dropped four to
six points" understated the spread. The owning primary's per-release figures run
2.0 to 6.3 (phi-3-medium-4k drops 2.0). Changed to "two to six points," which the
primary governs and which reinforces the article's own "not a large one" reading.

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: I can now say what "textbook-quality data" was as a
procedure, that a larger model wrote and filtered it, and that phi-1's headline
dominance was concentrated on training-like problems while its fair-test margin is
a few points that reverse under the strictest pruning. That requires reading Table
3's non-similar column against the Table 1 headline and joining it to the phi-4
distillation concession, which no single source hands over. The writer's
original-work sentence claims exactly this move, and the article delivers it. Both
answers survive, so the piece teaches rather than restates, and the prose sits
closer to the voice-guide exemplars than to a median summary. The headline, read
last as the largest claim, is defended by the pruning section.

## Edits

- Corrected "At the strictest threshold, 71 of the 164 problems" to "At the
  loosest threshold" (tau=0.95 is the least aggressive pruning; the article
  elsewhere labels the same threshold "loosest," and its own chart caption fixes
  the direction).
- Cut the signpost sentence "The problems were written by hand for a reason."
- Trimmed "and it is worth keeping separate from phi-1's code result" from "The
  later models are where independent scrutiny landed ...".
- Changed "dropped four to six points across releases" to "two to six points" to
  match the GSM1k paper's per-release figures (2.0 to 6.3).

## Required work

None. All items found were the editor's to fix and are done. No evidence gap for
the researcher; no reporting, redraft, chart, or provenance issue for the writer.
The chart provenance (chart-1.py) matches Table 3 exactly and the rendered image
reads honestly: labeled axes, a 0-40 scale, StarCoder-Prompted named in the
legend, and the tau=0.80 reversal visible.

## Decision

Approve. The central interpretive claim survives a hard test against the paper's
Table 1 and Table 3, the baseline shift is disclosed rather than hidden, and the
one factual mislabel and the minor slop and number items were fixed directly.
Prose changed, so the article should be re-proved before the PR.
