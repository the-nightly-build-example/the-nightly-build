# Editorial review: the-evidence/deep-double-descent (editor/01)

## Skeptic

Thesis: double descent is a real, reproducible curve, test error falls, peaks
right where a model becomes just able to fit its training data, then falls a
second time, but the strong moral now hung on it ("more parameters or more data
always help") is not what the papers showed, and the papers refute it
themselves.

The claims it stands on, and how each held:

- The classical rule (drive training error to zero and you have overfit; a sweet
  spot lies between too small and too large). Anchored on Belkin's textbook
  corollary, cited to s1, and matches the record's quote exactly. Per the
  brief's caution, the classical view rests only on sources actually opened
  (Belkin, and Nakkiran's framing); Geman 1992 is not cited. Held.

- Belkin named and drew the curve; showed it on random features on MNIST with
  the peak where feature count equals training-point count. Cited s1, matches
  the record (n = 10^4, peak at N = n). The draft attached "10,000" to "random
  features," but the 10,000 is the training-point count and the feature count is
  what is swept. This misdescribes the setup (a fixed 10,000-feature predictor
  produces no curve). Fixed directly: the number now labels the training
  examples and the peak lands where the feature count rises to equal that count.
  No number or citation changed.

- Nakkiran drew it on real nets: ResNet18 on CIFAR-10 with 15% label noise, test
  error dips near k = 4, peaks near k = 10 as training error falls toward zero,
  floors near 0.29 at k = 64. Verified against chart-1.py and the chart image
  (below). Held.

- Mechanism: one fragile interpolating solution at the threshold, many smooth
  ones past it, peak arises under model mis-specification. Cited s2, matches the
  record's Section 5 intuition. Held.

- More data can hurt: IWSLT'14 Transformer, 4.5x data (4k -> 18k pairs) raised
  test loss across a band of model sizes. Cited s2, matches the record's Numbers
  entry and quote. The draft correctly reserves "test error" for the classifiers
  and calls the Transformer's measure "test loss." Held.

- Label noise sharpens the peak (0/5/10/15/20% sweep, plateau to peak), but
  clean data still peaks on CIFAR-100 and IWSLT'14; noise not strictly required.
  Cited s2, matches the record and its "not too strong" line. Held.

- Corrections: optimal ridge regularization can remove the peak (s5); Curth et
  al. argue the classical second descent is a parameter-counting artifact,
  scope limited to classical methods (s6). Both match the record. One
  overreach: the draft said Curth found "two separate axes" of complexity; the
  record says "multiple." Softened to "more than one axis," removing a specific
  count the source does not support.

- Boundary: none of this was measured on an LLM; the emergence debate is a
  separate question of metric choice. Matches the commission's boundaries and
  the linked lesson. Held.

Display text, descriptor by descriptor. Headline ("A network's error peaks where
it can just fit its training data, then falls again") is a claim the piece
defends, subject and verb with the surprise up front, no colon mold, no
question, no triad. It holds. Every subhead names a real step in the piece's own
nouns. One subhead read "Where four times the data made it worse": "four times"
rounds the sourced 4.5x down, and a wrong quantity in a heading reaches every
skimmer, plus the standalone "it" dangles. Retitled to "Where more data made the
model worse," dropping the mislabelled number and the dangling referent. Names
and affiliations (Belkin/Hsu/Ma/Mandal; Nakkiran and coauthors; "a team at
Harvard and OpenAI") check against the record. The quoted title is verbatim.

Every data-nb-kind audited: s1, s2, s5, s6 are primaries that own their claims;
s3 (a survey) and s4 (Wikipedia) are secondaries reporting from outside the
authoring parties. Correct, and the series floor (6 sources, >=3 primary) is met
with 4 primary, 2 secondary.

Every citation href opened as printed. All four arXiv links resolve to the
correct abstract pages with matching titles and authors (1912.02292, 1812.11118,
2003.01897, 2310.18988, 2109.02355); the Wikipedia article resolves and carries
the framing s4 is cited for; the GitLab repo (chart data-nb-url and a Go-deeper
row) resolves to the Harvard-ML double-descent release. All land on the source
itself, not a fetch endpoint. The three Background/prose cross-links
(scaling-laws-kaplan, grokking, emergent-abilities) all exist on the published
library.

## Cut

The draft is clean; the slop pass turned up few failures, all at edges.

- The dek was the one formula finding. It read "Belkin's group named the shape
  in 2019 and Nakkiran's drew it ... including a band of sizes where 4.5 times
  the training data made the network worse." Against the last five Evidence deks
  (mixture-of-experts, constitutional-ai, segment-anything, adversarial-examples,
  denoising-diffusion) this reproduces the exact stamped shape the commission
  named: a possessive-author opening ("X's group ... Y's"), a year, a measured
  number, and a trailing reversal clause. Every one of the five opens the same
  way. Rewrote it to lead with the concrete surprise and drop the author-and-year
  opener: "Feed a network 4.5 times the training data and it can get worse, a
  limit one of the two 2019 papers behind double descent measured directly." It
  commits to a claim, adds the sample-wise result the headline omits rather than
  restating the headline's model-wise peak, and names the phenomenon. Both the
  visible dekline and the nb-meta dek were updated to match.

- Two edge signposts cut. "The honest statement:" prefaced the label-noise
  conclusion and graded the piece's own calibration; removed, leaving the fact
  ("Noise sharpens the peak and moves where it lands, but a clean dataset does
  not erase it"). "One boundary is worth stating." opened the LLM paragraph as a
  signpost; removed, so the paragraph opens on the fact ("None of this was
  measured on a large language model").

- One punctuation repair in the takeaway (the article's last-tested position). A
  three-clause comma splice ("a wider model is worse, more training data can
  push ..., and the sharpest version ... leans on ...") became a coordinated
  pair plus its own sentence, per the house period-default.

Checked the negative-parallelism reflex on every "not" clause: "not how long it
ran" and "not a law of nature ... a property of training with little restraint"
both correct real, named misconceptions (grokking's training-time axis; the
belief the peak is inevitable), so both earn their place and stay. The imperative
"Feed a network ..." dek opener is a concrete conditional in the voice guide's
register (Lee's "Suppose you're going to take a shower"), not a lecture opener.
No borrowed phrasing from the voice-guide exemplars. No prompt leakage: the
reader's "bigger is better" belief is reported fact about the reader, not a
lifted instruction. Furniture (the chart, the "In plain language" note, the
holds-up grid, the two bookends) is documented and each does real work; the note
and bookends use the body's established generic "you," not lesson
self-reference.

## Visual evidence

Opened chart-1.png and read it as a reader. Axes are labelled (width k with the
standard k = 64 called out; error on CIFAR-10 with 15% label noise), the y-axis
is anchored at zero (rangemode tozero), and both series are distinguished. The
test curve shows the full shape: ~0.53 at k = 1, dip to ~0.34 at k = 4, peak
~0.41 near k = 10, decline to ~0.29 at k = 64; train error falls to near zero by
k ~ 17. These match chart-1.py's committed series (test_error[3] = 0.3397,
max 0.4127 at k = 10, test_error[63] = 0.2911) and the caption. The provenance
header documents the released-data bucket and the paper's own clean-to-noisy
remap at p = 0.15, and the caption cites s2 with a data-nb-url to the release.
The prose "peak near k = 10 ... where training error is plunging toward zero" is
honest: at k = 10 train error is 0.083, on its way down from 0.53. The chart's
verified values supersede the record's approximate figure-reads exactly as the
brief directed. The visual is honest and needs no correction; no recrop
requested.

## Reader

Read straight through as the paper's reader. What I have that the sources alone
would not give me: the classical sweet-spot rule set as the left half of one
curve, the peak located precisely at the point where a model can just fit its
(noisy) data, a plain-language reason the threshold model is the fragile one,
and the line drawn between the reproducible curve and the "bigger always wins"
slogan, with the papers' own counter-results (a wider model that is worse, 4.5x
data that hurts, tuned regularization that erases the peak) doing the work. The
verified chart hands me the actual numbers instead of a figure-read. The
handoff's original-work sentence (a verified curve from the released runs, set
against the papers' own limits) survives the read. The prose sits with the
voice-guide exemplars, not a median summary: short declaratives, real figures
(k = 4, k = 10, 0.29, 15%, 4.5x), and homely concreteness ("a cat stamped
'truck'"). The headline as the largest claim is accurate and defended.

## Edits

- Rewrote the dek (nb-meta and the visible dekline) to break the recurring
  author+year+number+reversal mold and lead on the sample-wise surprise.
- Corrected the Belkin random-features sentence so 10,000 labels the training
  examples (not the feature count) and the peak lands where the feature count
  reaches that number.
- Retitled the subhead "Where four times the data made it worse" to "Where more
  data made the model worse", dropping the down-rounded number and the dangling
  "it".
- Changed "two separate axes of complexity" to "more than one axis of
  complexity" to match the record's "multiple" and drop an unsupported count.
- Cut the self-grading lead-in "The honest statement:" from the label-noise
  conclusion.
- Cut the signpost "One boundary is worth stating." from the LLM-boundary
  paragraph.
- Repaired a three-clause comma splice in the takeaway into a coordinated pair
  plus a separate sentence.

## Required work

None. All items were the editor's to fix and are fixed. Chart, script, styles,
and provenance were left to the writer; none needed correction.

## Decision

approve. The finding holds in its real shape, every figure and citation checks
against the owning primary, the chart is honest, and the remaining prose issues
(one formula dek, two signposts, a comma splice, two accuracy labels) were all
inside the editor's remit and have been fixed directly.
