# Editorial review: the-instruments/mean-average-precision (editor/01)

## Skeptic

Thesis: "mAP" is not one measurement but a name that has covered at least
three incompatible computations (VOC's 11-point AP, VOC's all-point AP, and
COCO's ten-threshold average), so a reported mAP number licenses no claim
about a detector until the reader knows which of those computations produced
it. The claims it stands on:

1. The IoU overlap test and its 0.5 threshold are the gate for a detection to
   count at all, and that gate is loose by design.
2. Average Precision turns one class's ranked hits and misses into one number
   by taking the area under an interpolated precision-recall curve.
3. "mAP" has meant at least three different procedures across VOC and COCO,
   and none converts to another by a fixed formula.
4. The YOLOv3-vs-RetinaNet case shows two real detectors ranking oppositely
   under two "mAP" readings taken from the same paper, with no independent
   victim needed to make the point.
5. That reversal does not make mAP worthless: a controlled study found a
   detection-mAP analogue tracking real driving outcomes well (r = 0.80).

I tried to break each one:

- **IoU/AP mechanics (claim 1-2).** Recomputed the worked six-detection table
  against VOC's exact two-step procedure (Everingham et al. 2010, VOC2012
  devkit doc Sect. 3.4.1): precision/recall per row check out against 4 ground
  truths and hits at ranks 1, 2, 4; the interpolated-precision envelope is
  1.00 for recall in (0, 0.50] and 0.75 for recall in (0.50, 0.75]; the area
  (0.25·1.00 + 0.25·1.00 + 0.25·0.75) = 0.6875, matching the article's "about
  0.69" exactly. The IoU worked number (70/130 ≈ 0.54) also checks out. Held.
- **The three-computations claim.** Fetched every primary and read the exact
  passages: Everingham et al. 2010 (IoU formula, Eq. 3, and the 0.5 rationale,
  p. 313-314; the threshold-sensitivity result in Sect. 6.2.3/Fig. 19, "AP...
  increase... around 7.5%"); Everingham et al. 2015 (the 2010 interpolation
  change and "too crude to discriminate... at low AP," p. 104); VOC2012 devkit
  doc Sect. 3.4.1 (the exact two-step AP procedure, verbatim match to the
  article's description); COCO's detection-eval documentation (confirmed live:
  "AP at IoU=.50:.05:.95 (primary challenge metric)," "AP at IoU=.50 (PASCAL
  VOC metric)," "a break from tradition... rewards detectors with better
  localization," and "We make no distinction between AP and mAP"); cocoeval.py
  (confirmed `iouThrs`/`recThrs` and the plain `np.mean` in `summarize()`).
  Every definitional claim traces to and matches its owning primary. Held.
- **The misled case.** Pulled the YOLOv3 PDF's actual text (abstract, Fig. 1
  and Fig. 3 data tables, Sect. 3, Sect. 5, and the Rebuttal). Every figure
  the article cites is exact: 57.9/57.5 AP50, 33.0/37.8 COCO AP, "similar
  performance but 3.8x faster," "It's not as great on the COCO average AP
  between .5 and .95 IOU metric. But it's very good on the old detection
  metric of .5 IOU," and the rank-order rebuttal hypothetical. I pushed
  specifically on whether the piece claims a victim: it does not. "No
  independent reviewer is on record saying either number fooled them. What
  happened here needed no outside victim" is exactly the framing the brief
  required, and I found no sentence smuggling in an implied deceived party.
  Held.
- **The Schreier counterweight.** Read the actual paper's Table 1 and its own
  rounded prose ("NDS correlates more to the CARLA Driving Score than the
  standard mAP metric (0.85 vs. 0.80). Both metrics have similar correlations
  to the number of collisions (0.90)."). The article's r = 0.80/0.85/0.90
  figures match this source sentence for sentence, including the source's own
  rounding of 0.903/0.907 to "0.90" for both. The verdict is bounded exactly
  as the brief asked: "The YOLOv3 case does not show that mAP lies. It shows
  something narrower..." — never "mAP is worthless," never softened past what
  the record supports either. Held.
- **Named people and display text.** No named third party is accused. Redmon
  and Farhadi are correctly identified as YOLOv3's authors, the paper's own
  framing ("What This All Means") is quoted accurately, and the affiliation-
  free description of Schreier et al. as "researchers" (not named individuals
  in body prose) is appropriate since the finding, not the authors' identity,
  is what the paragraph needs.
- **data-nb-kind audit**, against the primary/secondary test in
  `nb-researcher/SKILL.md` ("a primary owns the claim, a secondary reports on
  it from outside the authoring party"): all 9 are correct. VOC papers/devkit
  (s1, s2, s6), COCO paper (s3), COCO eval docs (s4), cocoeval.py (s5), and
  YOLOv3 (s8) are primary and each owns the claim it is cited for. Padilla et
  al.'s companion repo (s7) and Schreier et al. (s9) are correctly secondary:
  independent parties reporting on or testing what the primaries define.
- **Every citation href**, opened as printed: all 9 resolve to the source
  itself (the two `robots.ox.ac.uk` VOC links 301-redirect to `thor.robots.ox.ac.uk`,
  a normal host migration a browser follows automatically, not a
  workaround endpoint). Content at each href matches what it is cited for,
  confirmed against extracted PDF text or live page content, not just the
  evidence record's paraphrase. The internal Background links (`f1-score.html`,
  `auroc.html`) resolve to real sibling files in the published library, and
  the f1-score lesson does teach precision/recall from a table of four counts
  as the article assumes.

No break found in any load-bearing claim. Nothing routed to the researcher or
writer from this read.

## Cut

Ran the slop test on every sentence, the edge-sentence pass in isolation, the
cold-reader pass, and the delete test. Findings:

- No em-dashes (limit 4), no banned/press-banned terms present.
- No self-reference in body prose; the two bookends' direct address to the
  reader is the template's documented exception and each sentence there still
  says something (the opener sets up "what a reported mAP licenses, and what
  it does not," which the takeaway resolves — a real setup/resolution pair,
  not a restatement).
- Three sentences use a "not X" shape and I tested each against the
  negative-parallelism entry rather than waving them through on tone:
  "COCO's version is not VOC's version," "The threshold was not the only
  thing that moved," and "COCO's own documentation... makes no distinction."
  All three name a real, specific distinction the piece has just built (not a
  strawman), and each is immediately followed by new concrete content rather
  than standing alone as a finding. Kept.
- Checked the headline, dek, and every heading against the recent-pattern
  notes. The headline and dek use this piece's own reversal (57.9/57.5 tied,
  33.0/37.8 split) rather than the "score doesn't travel between tests"
  framing used for mean-opinion-score, and none of the four section headings
  ("A detected box has to earn its match," "Turning a ranked list into one
  number," "COCO redefined what the average covers," "Same detectors,
  opposite rankings") fit the banned noun-phrase-plus-participle mold. No
  formula found.
- Compared authored text against the commission, brief, and voice guide for
  leakage. The bookend line "'mAP' has named at least three different
  computations since PASCAL VOC first defined it" restates a real fact about
  the world (mAP's history), not the commission's planning language, and the
  closing verdict is phrased in the article's own terms rather than the
  brief's "silently changed what it measures" sentence. No leaked planning
  language, selection rules, or self-congratulation found.
- Furniture audit against `templates/lesson/furniture.md` and the engine
  catalog: the table, figure/chart, and inline-math components are all used
  exactly as documented, Background rows correctly point into the library and
  Go deeper rows correctly point beyond the paper, and the bookends correctly
  carry no citations.
- Punctuation, grammar, and the "Literal strings" rule (no stray `<code>`
  use) checked clean throughout, including inside the table caption and
  figure caption.

Nothing failed the test badly enough to need deletion. The piece is at
2199/2200 words, so I made no changes that would require an offsetting cut.

## Reader

Read straight through as the declared reader (smart, widely read, no
codebase, already holding the f1-score lesson). What I have that no single
cited source gives me: I now know that when I see "mAP" on a leaderboard I
cannot compare it across papers or years without knowing which of at least
three procedures produced it, I have watched one concrete number get built
from raw hits and misses, and I have seen why two real detectors, evaluated
by their own authors, can trade places depending only on which "mAP" is
quoted — plus the tempering fact that this is a definitional trap, not
evidence the metric is generally unreliable. No single source states this as
one argument; the VOC/COCO primaries never discuss each other's numbers, and
the YOLOv3 paper does not connect its own reversal to the Schreier
counterweight. That synthesis is the draft handoff's claimed original work,
and it holds up under inspection, including the six-detection worked example,
which does not appear in the evidence record and which I independently
recomputed. The prose sits closer to the voice-guide exemplars than to a
median AI summary: it gives the ranked-detection numbers before naming what
they buy (Lee's move), lists what a single mAP averages away in flat
one-clause declaratives (Karpathy's move), and runs the "you want to know
X; mAP measures Y" triad exactly twice at real specificity (Thomas's move),
without a fourth repetition showing off the trick. The headline, reread as
the largest claim, is exactly what the piece proves: two named detectors, one
metric name, two rankings, both numbers real.

## Edits

None required. I read the article for factual, arithmetic, citation, chart,
furniture, and slop compliance and found no break, miscitation, malformed
data-nb-kind, chart discrepancy, or prose failure that needed a direct edit.
The piece already meets `spec/editorial.md`, `spec/slop.md`, and
`spec/headlines.md` as drafted.

## Required work

None. No item routes to the researcher, writer, or orchestrator.

## Decision

**Approve.** Every load-bearing claim traces to and matches its owning
primary (independently reverified by opening all 9 sources), the worked AP
arithmetic and IoU example are correct, the misled case is framed as
definitional with no named victim, the Schreier counterweight is addressed
and the verdict is properly bounded, the chart's numbers match its provenance
script and the YOLOv3 primary exactly, and the piece passes the slop,
headline, and furniture standards with no cuts needed.
