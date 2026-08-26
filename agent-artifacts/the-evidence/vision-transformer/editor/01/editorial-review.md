# Editorial review: the-evidence/vision-transformer (editor/01)

## Skeptic

Thesis: the ViT paper's 2020 finding was conditional. Trained on mid-size
ImageNet without strong regularization, the Transformer trails comparable
ResNets; it matches or beats them only after pre-training at JFT scale. The
condition was a fact about the 2020 recipe, and the citation history hardened it
into a property of the architecture the paper never claimed.

Claims it stands on, and how each held:

- Headline, "The Vision Transformer lost to a plain CNN until it was fed 300
  million images." The paper's own summary puts ViT "a few percentage points
  below ResNets" at mid-size scale and reverses at JFT; the crossover the article
  cites (ViT-L/16 87.76 and ViT-H/14 88.55 vs BiT-L 87.54, all on JFT) lands ViT
  ahead only at the 303M end. The headline is conditional and accurate.
- The scale ladder and every accuracy figure. Checked each against the Numbers
  block of researcher/02: ImageNet ~1.3M / 1,000 classes; JFT 303M / 18k classes
  cited to ViT (s1); Sun et al.'s ~300M images / 375M noisy labels cited
  separately to s2; ViT-L/16 85.30 (ImageNet-21k) and 87.76 (JFT); ViT-H/14
  88.55; BiT-L 87.54 cited to the BiT paper (s3), which owns the number. The
  same-model delta 87.76 - 85.30 = 2.46 recomputes correctly. The two JFT
  snapshots are kept apart, not merged. Every figure is pinned to its model,
  dataset, and where it matters its recipe.
- The compute half of the finding ("substantially fewer computational resources
  to train"). Present and sourced to s1; matches contradiction 4 in the record,
  which flags that a pure-data framing drops half the claim. The article keeps
  both halves.
- The correctives. DeiT reaching 83.1% on ImageNet-1k alone (s5) and ConvNeXt
  reaching 87.8% with public ImageNet-22k (s6) are stated as the record has them.
  The article uses 83.1% no-distillation as the fair headline and does not
  overquote the 1000-epoch distilled 85.2% row, per the record's caveat. The
  distillation-teacher-is-a-CNN point is carried in one honest clause.
- The received-view claim. The 2022 survey (s4) is quoted only for its
  qualitative "pre-training ViT on a medium-range dataset would not give
  competitive results," used to show the strong reading persisted after DeiT. The
  survey's unverified "13% drop" figure is not carried anywhere in the piece.
  Confirmed by reading the full draft.

Tried hardest to break the headline and the "recipe not architecture" turn. Both
hold: the paper's own hedge ("without strong regularization"), quoted in the
note, is what DeiT later supplied, so DeiT reads as filling the authors' named
gap rather than refuting them; ConvNeXt closes the architecture half at equal
data. No sentence lets "Transformers beat CNNs" stand unconditionally.

Opened all six citation hrefs as printed. Each resolves to the source it claims:
2010.11929 (ViT), 1707.02968 (Sun et al., 375M labels / 300M images confirmed),
1912.11370 (BiT, 87.5% confirmed), 2101.01169 (Khan survey), 2012.12877 (DeiT,
83.1% / 86M params / single computer under 3 days confirmed), 2201.03545
(ConvNeXt, 87.8% and "standard ConvNet modules" confirmed). The four in-prose
library links (reading-images, word-order, attention-is-all-you-need, clip) all
resolve to existing files in the checkout library. Audited every data-nb-kind:
five primary, one secondary; the survey is correctly secondary by the
authorship-and-stake test, and BiT is correctly primary for the 87.54 it owns.
No sourcing break to route.

## Cut

Made a sentence-by-sentence slop pass, then walked the edges out of order, then
read the piece cold as an arrival-from-a-link. Three failures, all editor-fixed:

- Body self-reference (two sentences). The template allows self-reference only in
  the two bookend cards; the body speaks to no one. "This lesson is about none of
  that. It is about the number the paper got..." and "Everything below is what
  those two clauses mean..." both narrated the piece from inside the orientation
  body. Rewrote the first as a claim about the paper ("The paper is remembered
  for none of that. It is remembered for the accuracy it reached and the amount
  of data it took to get there.") and cut the second down to the thesis it
  carried ("The first of those two clauses turned out to matter more than the
  citation history remembers"), dropping the roadmap.
- Formula closer in the Why bookend. "Read it and you will be able to say what
  the paper proved, how large a foundation..., and where the common way of citing
  it runs past what it showed" is the "you will be able to" why-bookend closer the
  recent-pattern notes flag on sight (prior form: "By the end you will be
  able to..."). The template still requires the bookend to say what the reader
  gains, so I reshaped rather than deleted, breaking the three-item mold.
- Reader gestures (two). "means a jump most readers have never had to picture"
  and "What carries for the reader is the ratio" both gesture at a hypothetical
  reader; the second was also a signpost for a figure the next sentence states.
  Replaced the first with a plain magnitude clause and deleted the second (the
  ratio survives in the following sentence).

Checked the flagged tics: the takeaway does not use the "Read as X... Read as
Y..." mold and lands the judgment in the article's own frame; the CLIP link
appears once with no second pass over CLIP's argument; the banned "doing the
work" phrase is absent. "The word doing the damage is 'need'" is a near neighbor
of that tic but is a distinct, specific sentence carrying a real reasoning step
(the word "need" is what converts a recipe-fact into an architecture-law), so I
kept it. The negative-parallelism instances ("not a requirement of the
architecture," "not a property of the architecture," "never convolution against
attention in the abstract") each correct a misconception the piece names and
sources, so they are earned, not reflex. No borrowed phrasing from the
voice-guide exemplars. No prompt leakage against the commission or brief. No
em-dashes; the few semicolons join tightly bound clauses. Grammar and syntax
clean throughout, display text and furniture included. Furniture (one stat
strip, one table, one note) each does distinct work and does not stack.

## Reader

Read straight through as the paper's declared reader. What I have that the four
papers and the survey would not give me on their own: the paper's conditional
result reassembled against the shorthand that dropped the condition, with the
paper's own throwaway qualifier turned into the hinge, so DeiT reads as supplying
the ingredient the ViT authors named as missing and ConvNeXt as closing the
architecture half at equal data. That is the article's own contribution, and it
matches the original-work sentence in the handoff. The prose sits closer to the
voice-guide exemplars than to a median summary: it stops on the word "need" the
way Yong stops on "immunity," pins each accuracy to its exact model and dataset
the way Luu defines his metric before reporting it, and names the DeiT/ConvNeXt
exceptions the way Potter names the years his trend reverses. The headline, read
as the largest claim, is conditional and supported.

## Edits

- Why bookend: replaced the "you will be able to say X, Y, and Z" closer with a
  reshaped promise ("...the headline number stops being a slogan: you can see how
  large a foundation sits under it, and where the common way of citing it claims
  more than the paper proved").
- Orientation para 1: replaced the body self-reference "This lesson is about none
  of that. It is about the number the paper got and the price it paid to get it"
  with "The paper is remembered for none of that. It is remembered for the
  accuracy it reached and the amount of data it took to get there."
- Orientation para 2: cut the roadmap "Everything below is what those two clauses
  mean, how far the picture changes, and" leaving the thesis "The first of those
  two clauses turned out to matter more than the citation history remembers."
- Section "How far the picture changes": replaced the reader gesture "means a
  jump most readers have never had to picture" with "means a very large jump in
  scale."
- Same section: deleted the reader-gesture signpost "What carries for the reader
  is the ratio."

## Required work

None. Every issue found was prose or structure and is fixed in place. No evidence
gap, broken central claim, or source-policy failure to route to the researcher or
writer. The orchestrator re-stamps the article after these edits (the nb-meta
word count predates them); the proof runs clean (BLOCK: 0, WARN: 0) as edited.

## Decision

approve — the figures, citations, and sourcing all hold, and the three prose
failures found (body self-reference, a formula bookend closer, reader gestures)
were editor-fixable and are fixed.
