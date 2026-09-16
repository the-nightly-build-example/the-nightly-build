# Editorial review: the-mechanics/watermarks-in-generated-images (editor/01)

## Skeptic

Thesis: the ghost watermark on a generated image is not evidence that one
specific photo got copied. It is almost always a statistical regularity a
diffusion model learned from a training set where a stock-photo mark is
common, a mechanism distinct from the rarer case where a model reproduces one
training image nearly whole, and a widely circulated piece of "proof" for
copying (Getty's own lawsuit exhibit) turns out, read directly, to support the
first mechanism rather than the second.

Claims it stands on, and how each held:

1. **Distributional learning explains the mark.** A diffusion model trains to
   match a data distribution, with no step that targets one training example
   (cited to Rombach et al., Sec. 3.2, quote verified verbatim against the
   paper). Applying that objective to a training set where a mark co-occurs
   with a class of images is the article's own earned inference, not a
   source's direct claim about watermarks specifically, and it is written
   that way — held.
2. **Verbatim memorization is a separate, rarer mechanism.** Checked every
   number against Carlini et al. directly: 350,000 captions × 500 generations
   = 175,000,000 (correct), 94 cleared the strict threshold, and the paper's
   own text states "a further 13 (for a total of 109 images)" — I fetched the
   paper's full section text and confirmed this exact wording; the 94+13=107
   vs. stated 109 gap is the source's own arithmetic, faithfully quoted, not
   an error introduced in the draft. The "one in a million," "duplicated at
   least 100 times," and CIFAR-10 1,280→986 figures all check out with
   correct scope (CIFAR-10 only, not Stable Diffusion) — held.
3. **The two mechanisms stay distinct, with settled marked correctly and open
   marked correctly.** The draft states the training objective as settled and
   "which mechanism produced a given output" as open, and grounds the open
   claim in Carlini's own "remains open" line (quote verified) rather than
   overclaiming a stronger, more specific statement than the source makes —
   held.
4. **The Getty exhibit correction.** Verified against the actual asset: the
   left and right images in the paragraph-52 exhibit are two different
   photographs (different players, poses, and a fictitious "AA" crest against
   a real sponsor mark), exactly as the article and evidence record describe,
   and Getty's allegation stays attributed to Getty throughout, quoted
   directly in a note block with its own paragraph citation — held, and it is
   fair.
5. **"A dataset never filtered to remove them" / "the absence of any filter
   for a pervasive mark" (the causal link that puts the mark into Stable
   Diffusion specifically).** This broke. The LAION-5B paper's own Appendix
   F.2 (source 2, confirmed by fetching the paper's full text directly) lists
   Stable Diffusion's four training stages by step count and subset name but
   states no filtering criteria for any of them, which is exactly what the
   evidence record says — the paper is silent, not confirming "no filter."
   Checking further (Stable Diffusion's own published model documentation,
   which the LAION-5B paper's own footnote points readers to for "further
   technical detail"), the two stages that used "laion-improved-aesthetics"
   — 515,000 and 390,000 of the model's roughly 1.3 million total training
   steps, more than half the recipe — are documented there as filtered to an
   estimated watermark probability below 0.5. That is a real filter, on the
   majority of Stable Diffusion's own training data, and the draft's "never
   filtered to remove them," "nothing removing it," and "the absence of any
   filter for a pervasive mark are enough to produce" do not hold as written.
   This source is outside the evidence record's four required primaries and
   was not read to the researcher's citation standard, so I have not settled
   it or rewritten around it; I am routing it. It does not erase the
   thesis — a threshold of "probability < 0.5" is lenient, the earlier
   unfiltered stage still ran first, and the mark still visibly surfaces per
   Getty's own exhibits — but the article currently states a stronger and
   inaccurate claim than the record supports, on the load-bearing sentence
   that ties the mechanism to this specific model. See Required work.

Display text checked descriptor by descriptor: headline, dek, and every
subhead state claims the piece establishes, none scaffolding-generic. Named
person/entity checks: Getty Images as filer, Stability AI as defendant, D.
Del. case number, Rombach/Schuhmann/Carlini author lists — all correct except
one, caught and fixed: source 4 was captioned "Black et al." in the Sources
list and "Outside researchers" in body prose. I fetched the paper directly
(arXiv:2406.09548) and its full author list is a single name, A. Feder
Cooper — a Ph.D. dissertation, not a multi-author paper. Fixed both the
citation label and the body-prose plural to match. Every href was opened as
printed: all seven land on the source itself (arXiv abstract pages, the
LAION blog, the CourtListener docket and filing, both confirmed reachable and
matching the cited content). `data-nb-kind` audited against the primary/
secondary test in each case — all seven correctly classified (LAION-5B paper,
LAION's own blog, Rombach et al., Carlini et al., the complaint, and the
docket as primary by authorship and stake; the Cooper dissertation as
secondary, since it reports LAION's figure rather than owning it).

## Cut

Ran the slop test on every sentence, both edges of every paragraph/section
read in and out of order, and the delete test. Two findings, both fixed
directly:

- The "Why this matters" opener ("You have probably seen it without knowing
  what you were looking at...") is exactly the "second-person observation as
  the opening move" the commission and brief flagged as a recent-pattern
  formula to break, despite the draft-handoff's claim to have avoided it.
  Relocating the address inside the mandatory-address bookend does not change
  the rhetorical shape. Rewrote the opening sentence to lead with the
  phenomenon itself and hold the direct address for the required "what you'll
  know by the end" sentence at the paragraph's close, which is the bookend's
  actual job.
- A prompt-leak: "Nothing below that level changes the answer" (closing
  section) lifts the commission's own "Ground and present day" language
  ("nothing below changes the answer") nearly verbatim rather than reporting
  it in the article's own terms. I am not rewriting this sentence now,
  because it sits inside the same paragraph that needs a factual correction
  (see Required work) and will be rewritten once that correction lands;
  flagging it here so the writer fixes both in one pass rather than two.

No other sentence failed the test on either edge pass or the straight read.
The negative-parallelism constructions present ("not because one photo got
copied, but because...", "not the training objective alone, but...") each
correct a misconception the piece explicitly names (that a watermark proves
one photo was copied; that the training objective alone explains
memorization), so both are earned under the exception `spec/slop.md` states,
not cut. No unearned punchlines, vague attribution, or decorative analysis
found. No banned-terms or em-dash issues (none appear in the draft; `nb
check` already cleared this). No repeated pattern against the recent library
beyond the opener above; the closing heading avoids the flagged "So look
again..." callback shape, and the takeaway's closing sentence earns its place
as the conclusion the argument built rather than a generic moral.

## Reader

Reading it straight through as the declared reader: what I have that the
sources alone would not give me is the specific comparison that makes Getty's
own exhibit better evidence for the opposite of what the complaint argues —
no single cited source makes that comparison, and the piece earns it by
placing the memorization citation, the exhibit's own two photographs, and the
distributional mechanism side by side. That comparison, checked against the
draft-handoff's original-work sentence, is what the sentence claims and what
the piece actually does. The prose sits closer to the voice-guide exemplars
than a median AI summary: it commits to one worked case per mechanism before
generalizing (the stock-sports-photo hypothetical, the soccer-photo exhibit,
the CIFAR-10 number), reuses one comparison ("grass reading green") instead of
stacking several, and states the settled/open cut in a sentence or two rather
than a paragraph of hedging, exactly as the voice guide asked. The headline,
reread as the largest claim, holds: "millions" undersells the actual scale
(single-digit-percent of a multi-billion-pair dataset is closer to a hundred
million-plus images) but is not wrong, and I left it rather than add an
un-recorded multiplication as a headline figure.

## Edits

- Fixed source 4's citation label from "Black et al." to "Cooper" (Sources
  list), after confirming via the paper itself that arXiv:2406.09548 is
  solely authored by A. Feder Cooper.
- Changed "Outside researchers assessing large training sets cite the same
  number" to "A separate assessment of data risk in large training sets cites
  the same number," matching the corrected single-author attribution.
- Rewrote the "Why this matters" bookend's opening sentence to remove the
  "You have probably seen it..." second-person-observation opener (a flagged
  recent-pattern formula), leading with the phenomenon itself instead and
  keeping the required reader-facing close.

## Required work

- **Researcher:** Confirm, to the citation standard, what filtering (if any)
  applied to each LAION-5B subset actually used in Stable Diffusion's
  training recipe, especially "laion-improved-aesthetics" (515,000 + 390,000
  of the recipe's roughly 1.3 million steps). The LAION-5B paper's Appendix
  F.2 names the subsets and step counts but states no filtering criteria and
  points readers to the Stable Diffusion GitHub repository "for more
  technical detail" — that repository, or Stable Diffusion's own official
  model documentation, is the primary to read and cite. Confirm or correct
  the article's current claim that this training data was never filtered for
  watermarks.
- **Writer:** Once that evidence lands, revise the training-data section's
  "in a dataset never filtered to remove them" and "nothing removing it"
  sentences and the closing section's "the absence of any filter for a
  pervasive mark are enough to produce" sentence to state accurately what was
  and was not filtered, and why the mark still surfaces despite it (a lenient
  threshold, an earlier unfiltered stage, an imperfect classifier — whatever
  the confirmed record actually supports). In the same pass, rewrite "Nothing
  below that level changes the answer," which currently lifts the
  commission's own phrasing rather than reporting it.
- **Writer (next revision, non-blocking):** `W-SOURCES-MIN` — 7 sources
  against the series' 8-source floor. Per the round brief, a researcher round
  is adding an eighth primary in parallel; this is recorded here as the
  writer's item to cite once that source lands, not a blocker on this review.

## Decision

Revise. One load-bearing claim about Stable Diffusion's own training data —
that nothing filtered the pervasive watermark before the model trained on
it — does not hold against Stable Diffusion's own documented training
recipe, and it sits under the article's central mechanism for the concrete
case (not just the general "any model trained on unfiltered data" point,
which can stand once the specific claim is corrected). Everything else in
this round's focus (the two mechanisms held distinct with settled/open
marked correctly, the Getty-exhibit correction, the source asset's crop and
accuracy, every href, every source's kind) held up under verification.
