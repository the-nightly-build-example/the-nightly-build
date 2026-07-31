# Voice guide — the-instruments/bleu

## Directive

Write as someone walking a smart reader through a calculation they could
reproduce by hand, not as someone reporting a finding about a calculation.
Every sentence should sound like it's building the number in front of the
reader, one piece at a time, never summarizing a piece already built.

**Introduce each formula part by what it does before what it's called.**
Show the behavior first, name it second. Before the phrase "modified
n-gram precision" appears, the reader should already have watched a
sentence get scanned for repeated words and watched a repeat get capped.
The name then labels something the reader has already seen happen, instead
of announcing something they must now decode. Do the same for "clipping"
and "brevity penalty": demonstrate the effect on the worked example, then
give it its name in the same sentence or the next.

**Run one worked example the whole way through, not a fresh one per
section.** Pick one candidate sentence and one reference sentence at the
top of the computation and keep those exact words in play for every count,
every clipped precision, every penalty. When the lesson later shows a
paraphrase scoring low or a bad translation scoring high, reuse the same
sentence pair rather than introducing a new one — the reader should never
have to re-orient to new words while learning what a number means. Put the
n-gram counts in a table, not a paragraph of "1-grams: 5, 2-grams: 3" — a
sentence carrying more than one count has stopped explaining and started
listing.

**Turn every "this can mislead" claim into a quantified case, not an
assertion.** Don't write that BLEU differences can be meaningless and move
on. Give the actual numbers from the record: how many points of BLEU
separated the systems, what the human judges did instead, and what that
gap cost in research time or wrong conclusions. An abstract warning
("scores don't always reflect quality") is a sentence that could appear in
any article about any metric. A quantified one ("humans preferred the
rule-based system while BLEU ranked it lower") could only appear in this
one.

**Let a short declarative land the realization after a numeric build-up.**
When a paragraph has just walked through counts, precisions, or a penalty
calculation, close it with a short sentence that states what the number
now means, not a hedge and not a flourish. The arithmetic earns the
short sentence; without the arithmetic first, the same short sentence
would be an assertion wearing confidence it hasn't earned.

**Be specific about uncertainty instead of gesturing at it.** When a claim
about BLEU's reliability rests on a correlation study or a sample size,
say the sample size and the correlation, not "studies suggest." When
something about the metric's history or motivation is inferred rather than
documented, say so directly in one clause, and keep going — do not turn it
into a hedge that swallows the sentence.

**Define a term where the reader first needs it, and never again.** Once
"reference," "candidate," "clipping," or "corpus-level" is set, reuse the
exact word every time. A synonym reached for variety mid-explanation reads
as a second concept the reader now has to reconcile with the first.

Recently used, do not reuse: the shocking-swing opener ("the same model
scored X and Y"); a colon-subtitle headline; a "not X but Y" thesis
sentence; the comma-and-clause section-heading cadence recent Instruments
lessons have settled into; the openers used for the humaneval-pass-at-k,
mmlu, and swe-bench lessons.

---

## Ehud Reiter, blog posts on BLEU and NLG evaluation

Source: https://ehudreiter.com/2020/07/28/small-differences-in-bleu-are-meaningless/
and https://ehudreiter.com/2020/03/02/why-use-18-year-old-bleu/

Craft:
- cadence: Short paragraphs, each closing on the number that carries the
  argument forward rather than a transition sentence.
- argument: Builds from an accepted use of the metric to the specific
  place that use breaks, rather than attacking the metric wholesale first
  and qualifying later.
- evidence: His own published correlation study (284 correlations across
  34 papers) sits beside the specific numeric claim it supports, cited by
  its actual finding, not by "research shows."
- stance: Informed skeptic, not prosecutor. He states what BLEU is good
  for before stating what it isn't, and marks his own inference as
  inference ("I am guessing this by eyeballing their graphs").
- notice: Converts a vague complaint ("small BLEU differences don't
  matter") into a specific, falsifiable number: a 1-2 point gap carries
  about a 50% chance humans prefer the lower-scoring system.
- diction: Plain, almost spoken register; technical terms (Pearson
  correlation, outlier) arrive only once the reader has a concrete number
  to hang them on.
- reader: A researcher or engineer who already trusts BLEU and needs a
  specific reason to stop trusting a specific use of it.
- the missed move: he never asks the reader to accept a claim about
  reliability in the abstract. Every reliability claim in these posts
  arrives already converted into "how many points of difference before
  you can trust the ranking," which is the exact conversion this lesson
  needs for the Callison-Burch case and for the brevity penalty's blind
  spot.

Calibration: "If System A has a BLEU score that is 1-2 point higher than
System B (common in academic papers), then there is only a 50% chance
that human evaluators will prefer System A over System B."

---

## Jay Alammar, "The Illustrated Transformer"

Source: https://jalammar.github.io/illustrated-transformer/

Craft:
- cadence: Alternates a short question sentence with a medium explanatory
  sentence of fifteen to twenty words; the question sets up exactly what
  the next sentence answers.
- argument: Progressive disclosure — each mechanism is shown acting on a
  single running example before its formal description appears.
- evidence: Concrete dimensions stand in for evidence: 512-dimensional
  embeddings, 64-dimensional vectors, 8 heads. The specificity itself does
  the convincing; there's no appeal to authority.
- stance: A patient demonstrator, never a summarizer. He shows the
  computation happening rather than describing that it happens.
- notice: One example sentence — "The animal didn't cross the street
  because it was too tired" — threads through every section that follows,
  so a reader who has understood the first computation never has to
  re-learn the setup for the next.
- diction: Minimal symbolic notation. Vectors are labeled q1, k1, k2
  rather than left in pure mathematical notation, and each label is
  defined functionally (what it does) before it's used in a formula.
- reader: Someone who can follow arithmetic and wants to actually compute
  the thing, not just be told what it's for.
- the missed move: formulas are introduced only after the operation they
  describe has already been performed once by hand on the running
  example. The formula, when it finally appears, is a summary of
  something the reader already watched happen — never the reader's first
  encounter with the idea.

Calibration: "The score is calculated by taking the dot product of the
query vector with the key vector of the respective word we're scoring. So
if we're processing the self-attention for the word in position #1, the
first score would be the dot product of q1 and k1."

---

## Kalid Azad, "An Intuitive (and Short) Explanation of Bayes' Theorem"

Source: https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/

Craft:
- cadence: Builds suspense with a direct question ("what are the chances
  you actually have cancer?"), then resolves it through arithmetic before
  ever writing the formula.
- argument: Numbers first, formula last. The formal statement of Bayes'
  theorem arrives after the reader has already worked out the right
  answer by hand, so the formula reads as a name for something they
  already did.
- evidence: A single concrete population (100 people, 1% base rate, 80%
  test accuracy, 9.6% false-positive rate) supplies every number in the
  piece; nothing is imported from outside that one worked case.
- stance: A guide correcting a specific, common misreading, not a
  debunker. He names the exact wrong intuition (mistaking test accuracy
  for the odds of having the condition) before showing why it's wrong.
- notice: The reveal is a plain numeric contrast, not a rhetorical
  flourish: 80% test accuracy produces only a 7.8% chance of actually
  having the condition once the positive result comes back.
- diction: Short declarative sentences at the moment of realization,
  longer explanatory sentences in the build-up to it.
- reader: Someone with no statistics background who has heard "test
  accuracy" used loosely and never had it checked against a real
  calculation.
- the missed move: he sets up the wrong intuition explicitly, in the
  reader's own likely words, before disproving it with the same
  population he used to build the formula. The deception and the
  demonstration share one dataset, so nothing about the "reveal" requires
  the reader to trust a new set of numbers.

Calibration: "Interesting — a positive mammogram only means you have a
7.8% chance of cancer, rather than 80% (the supposed accuracy of the
test)."

---

## Neil Paine, "How My NHL Elo Ratings and Forecast Works"

Source: https://neilpaine.substack.com/p/how-my-nhl-elo-ratings-and-forecast

Craft:
- cadence: One component of the formula per section, added to the
  previous one rather than presented all at once — home-ice advantage,
  then the playoff multiplier, then the margin-of-victory weighting, each
  landing before the next is introduced.
- argument: Presents the base calculation as settled, then narrates the
  specific experiments that shaped each adjustment, so the reader sees
  which choices were tested and which were arbitrary.
- evidence: States what the research did and did not find as a discrete
  claim — "no predictive power in differentiating between one-goal
  results" in certain situations — rather than folding it into a general
  disclaimer.
- stance: A builder auditing his own instrument. He explains a design
  choice (the K-factor) by describing the failure mode on both sides of
  it — too high overreacts, too low lags — instead of just asserting the
  chosen value is correct.
- notice: Turns "the model can be tuned" into the actual trade-off a
  reader can picture: a K-factor too high makes ratings volatile, too low
  makes them slow to catch a team that's actually improved.
- diction: Technical but never jargon-first; each parameter (K-factor,
  1500 baseline) gets its behavior described before its number is given.
- reader: A sports-analytics reader comfortable with the idea of a
  rating but not with how one gets built or adjusted.
- the missed move: every limitation is attached to the specific
  mechanism that causes it, not offered as a general caveat at the end.
  The reader learns to distrust exactly the part of the number that
  deserves distrust, and to keep trusting the rest.

Calibration: "A K-factor that is too high creates volatile ratings that
overreact to recent results. A low K-factor has the opposite problem —
it's too slow to react to changes in team quality."
