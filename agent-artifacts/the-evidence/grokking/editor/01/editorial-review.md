# Editorial review: the-evidence/grokking (editor/01)

## Skeptic

Thesis: grokking is a real, reproducible, small laboratory effect (delayed
generalization on a toy modular-arithmetic task), and the popular use of the word
as evidence that large models harbor a hidden switch runs past what any of the
work shows. The piece stands on four claims, each of which held.

1. The measured result and its scale. A ~400k-parameter, 2-layer transformer on
   division mod 97 with half of the 9,409-entry table shown fits the training half
   within ~10^3 steps and reaches near-perfect held-out accuracy only near 10^6
   steps, a ~1000x gap. Every figure matches the evidence record and the Power et
   al. caption it quotes (97, 9,409, 50%, ~400k, 2 layers/width 128/4 heads, AdamW
   with weight decay, the 25-30% / 40-50% data-efficiency point). No arithmetic or
   denominator error found.

2. Suddenness is a property of the watched curve. The article locates the abrupt
   jump in the test-accuracy metric and shows, via Nanda et al.'s progress measures
   and the three-phase table (memorization / circuit formation / cleanup, epochs
   0-1.4k / 1.4k-9.4k / 9.4k-14k), that the generalizing circuit forms gradually
   underneath. It never claims generalization is literally instantaneous. The
   round-focus boundary survived. The Nanda quote is an accurate substring of the
   evidence-record quote.

3. Weight decay. "Most effective" (more than halving samples needed) is attributed
   to the original paper and cited to s1; "necessary in their setup" is attributed
   to Nanda et al. and cited to s2. The two are held distinct and synthesized only
   as far as "the main force," not merged into a single stronger claim. Boundary
   survived. Minor note below on citation ordering, not blocking.

4. The word outruns the result. The Omnigrok on/off control result (s4) and the
   2025 7B result (s5) are weighed honestly: the 7B finding is presented as a
   separate 2025 result the 2022 scale cannot carry, and as local, asynchronous,
   per-domain delayed generalization that cuts against the "single switch"
   shorthand rather than confirming it. The article does not turn it into "big
   models grok." Boundary survived.

Tried to break the thesis on its strongest challenge, the 7B result, and it holds:
the piece extends the phenomenon's reach and denies the sudden-unlock reading in
the same breath, matching the source.

Citations and kinds (first-read requirement). I opened all six hrefs as printed.
All resolve to the source itself with matching titles and author lines:
- s1 2201.02177 Power, Burda, Edwards, Babuschkin, Misra — title verbatim; author
  line is Burda, not "Burns," in display text, body, and sources. Round-focus name
  boundary survived.
- s2 2301.05217 Nanda, Chan, Lieberum, Smith, Steinhardt — resolves, title matches.
- s3 2205.10343 Liu, Kitouni, Nolte, Michaud, Tegmark, Williams — resolves, matches.
- s4 2210.01117 "Omnigrok: Grokking Beyond Algorithmic Data," Liu, Michaud, Tegmark
  — the title the evidence record omitted; verified live, matches the article.
- s5 2506.21551 "Grokking in LLM Pretraining? Monitor Memorization-to-Generalization
  without Test," Li, Fan, Zhou — the other omitted title; verified live, matches;
  abstract confirms MoE LLM pretraining.
- s6 Quanta "How Do Machines 'Grok' Data?," Anil Ananthaswamy — headline verified
  live; "only extremely small networks" and Belkin's "a drop in the ocean" both
  confirmed on the page.
Kinds are right: s1-s5 primary (each paper's own authors reporting their own
result), s6 secondary (independent journalism, not a restatement of any one
paper). No miscitation, no broken href, no missing independent source.

## Cut

Ran the slop test sentence by sentence, then walked the edges out of order, then a
dangling-referent read from a cold open, then the delete test. The draft is clean.
No sentence failed the placeholder test; the edges carry facts or reasoning steps
(the opener defines grokking in the same sentence it names it, so no dangling
referent; the takeaway closer states the conclusion the argument built and does not
land on a portable "so when someone tells you X" rebuttal). Negative-parallelism
constructions were checked individually: "a property of the training landscape a
researcher can dial, not a threshold a network crosses by getting big" and "did not
merely slow the network a little" both correct a misconception the piece names (the
scale-unlock reading; the assumption that less data slows things only mildly), so
they earn their place. No prompt leakage: no brief/commission phrasing lifted, no
"this desk," no body self-reference, the bookends are the only reader-addressing
prose and that is the lesson template's documented allowance. No borrowed phrasing
from the voice-guide exemplars. Furniture (stat strip, three-phase table, one "In
plain language" note) each does clarifying work and does not read as a stack of
blocks.

Two direct punctuation edits: two semicolons joined independent clauses that stand
alone, where the house standard makes the period the default. Changed both to
periods. No lexical banned-term or em-dash issues.

Formula check against the recent-pattern notes: opener is not nostalgic/second-
person and does not pivot on "this lesson reads/shows"; the opener does not close on
a measured-result-beside-famous-story line; the takeaway does not land on a portable
rebuttal; no body self-reference. The dek is a single scale-stating clause, not the
concessive-reversal mold. Headings are steps in the lesson's own nouns and avoid the
"The X that Y" and "noun, the appositive" molds. Nothing survived that the run is
breaking.

## Reader

Read straight through as the paper's declared reader. What I have that the six
sources alone would not give me: a calibrated picture that grokking is real,
reproducible, and small; that the "sudden" jump is only sudden in the one metric
being watched while a generalizing circuit forms gradually beneath it and weight
decay clears the memorized solution away; and that the popular "big models grok"
reading outruns the evidence, with even the single 7B result reframing the effect as
local and asynchronous. The original-work sentence claims exactly this synthesis
across the separate papers, and the article delivers it; both answers survive, so
the piece is not a restatement of its sources. The prose sits closer to the
voice-guide exemplars than a median summary: concrete figures carry the judgment
(400k against hundreds of billions, ~1000x, many-millions-of-times-larger) and the
rotation algorithm is worked out in the network's own terms rather than summarized
as a "phase change." The headline is the largest claim and the piece defends it.

## Edits

- Changed the semicolon to a period in "did not merely slow the network a little; it
  pushed" (honest-scale section), per the house punctuation standard.
- Changed the semicolon to a period in "The suddenness is mostly in the measurement;
  beneath a flat test curve" (takeaway), per the house punctuation standard.

## Required work

None. The writer's open question about linking `the-evidence/scaling-laws-kaplan` in
Background needs no action: it was offered as optional and the lesson works without
it. The evidence record's two omitted source titles were verified correct against
the live sources during this review; updating the researcher artifact to carry those
strings is optional housekeeping for the orchestrator, not a publication blocker.

## Decision

approve — the four load-bearing claims held, all six citations resolve to the right
source with correct kind labels and the Burda/sudden/weight-decay/7B boundaries
intact, and the prose passed the slop and formula reads with only two direct
punctuation fixes.
