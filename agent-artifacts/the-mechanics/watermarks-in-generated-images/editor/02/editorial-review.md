# Editorial review: the-mechanics/watermarks-in-generated-images (editor/02)

## Skeptic

This round's job was narrow: confirm the writer's three round-02 fixes against
their sources, then bring the piece back inside the word band. I did not
reopen the thesis, the Getty-exhibit correction, or any other finding editor/01
already settled.

**Fix 1: the filtering account.** I fetched the Stable Diffusion v1 Model
Card directly (raw.githubusercontent.com/CompVis/stable-diffusion, the exact
file the evidence record cites) rather than trusting the record's paraphrase.
It confirms, word for word: `sd-v1-1` ran 237k steps on `laion2B-en` at
256x256 then 194k steps on `laion-high-resolution` at 512x512, with no
watermark filter stated for either; `sd-v1-2` (515k steps) is the first stage
trained on "laion-aesthetics v2 5+," defined as filtered to "an estimated
watermark probability < 0.5," with the estimate sourced to LAION-5B metadata;
`sd-v1-2` states "Resumed from sd-v1-1.ckpt," and both `sd-v1-3` and `sd-v1-4`
state "Resumed from sd-v1-2.ckpt" (siblings off v1-2, not a further chain);
the Limitations section states no deduplication was used. Every element the
brief asked me to check — the unfiltered base, every later checkpoint's
lineage running back through it, the 0.5 threshold on the aesthetics subset,
and "estimated" rather than a checked label — holds exactly as the article
states it. The article's comparison of 0.5 against LAION's own 0.8 threshold
for its conservative watermark estimate was verified in round 02's own read
of the LAION blog and is reproduced accurately here. This was the one load-
bearing correction from editor/01's revise decision, and it is sound.

**Fix 2: the leaked sentence.** "Nothing below that level changes the
answer," which lifted the commission's "Ground and present day" phrasing
nearly verbatim, is gone. In its place: "Go one level deeper and there is
nothing left to find. The objective, the data, and how much of that data was
screened before training account for the whole behavior." This reports the
same ground-floor claim in the article's own clause order and, correctly,
now names the screening rather than an absent filter — fixed and accurate.

**Fix 3: the eighth source.** Somepalli et al. (source 8) carries
`data-nb-kind="primary"`, matching the evidence record's own classification
(the researchers who built the detection framework and ran it on Stable
Diffusion directly — primary by authorship and method, not a report on
someone else's work). The citation is not bare: "A second, independent
study of that same reproduction, using an entirely different detection
method, does not mention watermarks either. Its own examples are full
images and objects, a sofa, a Hokusai wave print, a celebrity portrait,
never a mark alone." That is exactly the further-gap point the draft-handoff
describes the citation adding, and it is the same pairing Getty's own
footnote 6 cites — checked against the evidence record's Contradictions
entry on this point, which it matches.

**The two mechanisms stay distinct**, checked again straight through:
distributional learning is introduced and marked settled in its own section;
memorization is introduced as "a distinct mechanism" (now stated via the
section's opening claim rather than a signpost sentence, see Cut) and marked
open only as to which mechanism produced a given output, in Carlini's own
"remains open" language. Nothing in this round's trims merges or blurs the
two.

**The Getty allegation stays attributed to Getty** throughout: the direct
quote sits in a labeled "Getty's own framing" note with its own paragraph
citation, and every reference to the central claim is phrased as Getty's
("Getty's own exhibit," "Getty's later exhibits," "Getty's broader copyright
claim"), never adopted as the article's own assertion.

## Cut

The published draft stood at 2367 words against the lesson band's 2200
ceiling — 167 words over, entirely the documented cost of round 02's
corrections. The brief was explicit about what could not be cut: the
filtering scope, the 0.5 threshold, the probabilistic-estimate point, and the
Somepalli citation's own explanation. I left all four untouched and trimmed
everything else, from the middles of paragraphs, not by truncating the
piece.

What came out:
- Two restatements of the same finding stacked back to back: the orientation
  paragraph's list of scene types duplicated the Getty-exhibit list two
  sentences later, and "Nobody put it there by hand" duplicated a claim the
  Why-this-matters bookend had just made. Cut the duplication, kept the
  concrete Getty examples.
- A signpost with no reasoning in it: "So: several percent of each subset is
  watermarked, by LAION's own conservative estimate" recapped the prior
  paragraph's own finding without adding anything the reader didn't already
  have. Cut; the paragraph now opens directly on the filter finding.
- A second signpost: "That is a distinct mechanism from the one above,"
  opening the memorization section's second paragraph, reported where the
  argument stood without doing any of the reasoning — the section heading
  and the surrounding sentences already establish the distinction. Cut.
- A restated conclusion: the Getty-exhibit paragraph stated its core finding
  three times in close succession (para-opening "does not hold up as a
  copy," mid-paragraph "better evidence for the other mechanism," and a
  closing sentence repeating the same conclusion in different words). Cut
  the third restatement, kept the fairness caveat that followed it (the
  exhibit doesn't settle Getty's broader legal claim), which is a real,
  separate point, not a restatement.
- Two stacked comparisons where the voice guide asked for one, reused: "the
  same kind of regularity as grass reading green or a stadium crowd reading
  blurry in the background" stacked a second image onto the one the guide
  singled out for reuse. Cut the second, kept "grass reading green," which
  also recurs in the takeaway.
- Several sentence-level tightenings that lost no fact: merged two sentences
  introducing the diffusion training loop, shortened the NSFW/watermark
  score comparison and the CIFAR-10 duplication description, trimmed
  connective tissue in the bookends. None of these touch a number, a name, a
  quotation, or a citation's target — I checked all nine sources are still
  cited in the body after trimming.

One trim produced a new problem I had to fix before this round could close:
combining the NSFW and LAION-blog sentences left a 54-word, two-clause-join
sentence that `nb check` flagged as W-SENTENCE-DENSITY. Split it back into
two clean sentences at the natural break (the classified-subsets list, then
the threshold-and-direction claim), which cleared the warning without adding
words back.

Final count: 2188 words, 12 under the 2200 ceiling. No sentence, edge, or
furniture component failed the slop test on a fresh pass after trimming;
the closer, dek, and headings are unchanged from editor/01's settled review
and were not reopened.

## Reader

Reading the trimmed piece straight through as the declared reader: what I
have that the sources alone would not give me is unchanged from editor/01's
finding — the specific comparison that makes Getty's own exhibit better
evidence for the opposite of what the complaint argues. That comparison
survived every cut intact, including its fairness caveat. The corrected
filtering account reads as a strength now, not a liability: "partial in
scope, permissive in threshold, probabilistic rather than exact" lands in
three tight sentences instead of a hedge-heavy paragraph, closer to the
Lee-and-Trott "clean cut" the voice guide asks for. The prose still sits
closer to the voice-guide exemplars than a median AI summary: one comparison
carried through rather than stacked, one worked case per mechanism before
the general claim, and the settled/open distinction stated plainly rather
than hedged. The headline, reread as the largest claim, still holds under
the corrected filtering account: "millions" is not undercut by "filtered
only in later stages" — the unfiltered first stage alone trained on 2.3
billion pairs.

## Edits

- Cut duplicated phenomenon description in the orientation paragraph (the
  scene-type list and "nobody put it there by hand," both already stated in
  the Why-this-matters bookend).
- Cut the recap sentence opening the corrected-filtering paragraph ("So:
  several percent of each subset is watermarked...").
- Cut the signpost sentence opening the memorization section's second
  paragraph ("That is a distinct mechanism from the one above").
- Cut the third, repeated restatement of the Getty-exhibit finding, keeping
  the fairness caveat about the broader copyright claim.
- Cut the stacked "stadium crowd" comparison, keeping "grass reading green."
- Tightened the NSFW/watermark-score paragraph, the training-recipe intro
  sentence, the CIFAR-10 duplication sentence, the distributional-learning
  training-loop sentences, and both bookends' connective prose, without
  dropping any fact, figure, name, or citation.
- Fixed a grammar slip introduced by my own edit ("not a class of image but
  one photo" → "not a class of images but one photo," matching the plural
  used elsewhere in the same section).
- Split a 54-word, two-clause sentence flagged by `nb check`
  (W-SENTENCE-DENSITY) into two sentences at its natural break.
- Ran `./nb stamp` and `./nb check --check-links` after trimming; final
  state is 2188 words, BLOCK: 0, WARN: 0.

## Required work

None. All three round-02 fixes verified sound against their sources
(including a direct fetch of the Stable Diffusion v1 Model Card, not just
the evidence record's paraphrase), the two mechanisms remain distinct, the
Getty allegation remains attributed to Getty, and the piece is back inside
the 1200-2200 lesson band at 2188 words with a clean proof.

## Decision

Approve. The three fixes hold against their sources, nothing required by the
brief was dropped in trimming, and the proof is clean: BLOCK: 0, WARN: 0,
2188 words, verdict PUBLISHABLE.
