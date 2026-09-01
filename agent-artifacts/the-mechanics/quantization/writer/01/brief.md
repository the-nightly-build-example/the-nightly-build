# writer brief: the-mechanics/quantization (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
- ../../commission.md — angle, course boundary, and the recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available; use its Numbers section exactly
- ../../../../library/the-mechanics/quantization.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract, runtime assets, and furniture catalogs

Output: ./draft-handoff.md

Proof: nb check .nb-work/the-mechanics/quantization/library/the-mechanics/quantization.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/c80f7a7e-0800-5248-bdf5-999f03f80465/scratchpad/library-checkout

Run the proof from /home/user/the-nightly-build with the checkout's ./nb; iterate
with --no-check-links, then finish on the full command until BLOCK: 0. No code
listings anywhere in the article.

Follow the evidence on the one wording correction: "usually cheap" holds only for
good schemes down to about 4 bits. Naive round-to-nearest is not cheap at scale
(the record has the exploding-perplexity figure), and even good schemes lose real
accuracy below 4 bits, where perplexity can understate task collapse. That is the
"sometimes costs a lot" step, not a contradiction of it. Mark two things open, as
the evidence does: why outlier features arise, and the accuracy floor below 4
bits. The degradation-versus-bits series and the two memory anchors are verified
in the evidence if a chart earns its place; build any chart only from those
series with nb chart, and inspect the rendered image.
