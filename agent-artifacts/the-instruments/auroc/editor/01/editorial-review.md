# Editorial review: the-instruments/auroc (editor/01)

## Skeptic

Thesis: AUROC measures one thing, ranking, and is read as if it measured three;
Epic's two AUROC figures and its bedside failure are the predictable payoff of
that single definition, not a contradiction. The piece stands on four claims.

1. AUROC equals the probability the model scores a random positive above a
   random negative, the quantity the Wilcoxon statistic estimates. Checked
   against Hanley & McNeil (s3): the evidence quotes the ranking-probability and
   Wilcoxon-equivalence language verbatim. The 1982 date and the "names for one
   number" claim hold. The 0.5/1.0 boundary is pinned to Saito & Rehmsmeier (s2),
   which states it in words, matching the evidence note that Hanley is a scanned
   PDF and the boundary reading belongs to Saito. Correct.

2. Ranking-only means AUROC is blind to calibration, to the deployed threshold,
   and to prevalence. Calibration- and threshold-independence follow from the
   definition and the evidence says they need no separate source. Prevalence is
   carried by Saito & Rehmsmeier's worked example: identical outputs, ROC and its
   area unchanged between balanced and imbalanced data, precision falling 0.60 to
   0.33. The article prints 0.60 and 0.33 and attributes the move to negatives
   piling up, which is the evidence's mechanism. Correct.

3. The Epic figures. I checked every one descriptor by descriptor against the
   Wong entry and the Numbers block: vendor "as high as 0.83" (vendor 0.76-0.83);
   external 0.63; 38,455 hospitalizations; alarm set at score 6; sensitivity 33
   percent; missed 1,709 of 2,552, close to two in three; 1,030 of those got
   timely antibiotics; sepsis about 7 percent of stays; PPV 12 percent; 8 patients
   worked up per case at one alert per stay and 109 with re-firing over a
   four-hour window; alarm on 18 percent of hospitalizations; STAT's undisclosed
   antibiotics-ordered input; Ostermayer's 145,885 encounters, two Texas county
   EDs, 2023, sensitivity 14.7 percent, median lead time zero minutes. Every one
   matches. The 0.76-0.83 range is cited to Wong (primary) for the figure and to
   Habib (s6, secondary) for the joint Epic / University of Colorado Health
   attribution, exactly as the evidence assigns them. This was the failure with
   the highest cost and it held.

4. The imbalance point is framed as the fact, not the prescription. The article
   states plainly that a precision-recall view is more informative on skewed data
   (Davis & Goadrich, s4) but that the blanket "always prefer AUPRC" rule is wrong
   (McDermott, s5), and lands on the narrow durable fact: AUROC does not move with
   prevalence, precision does. No metric horse-race, no Epic rebuttal attributed
   without a cite. Correct, and it satisfies the round focus.

I pushed hardest on the Epic numbers and the chart, the places a wrong label
would reach every reader. Display text: the headline ("0.63 AUROC", "one case in
three", "the threshold hospitals used") is a claim the body defends and carries
no colon subtitle; the dek makes a claim about what AUROC is and stays silent on,
not a grade of the article. Every section heading is a step of the argument in
the piece's own nouns. data-nb-kind on all eight sources is right: Wong, Saito &
Rehmsmeier, Hanley & McNeil, Davis & Goadrich, McDermott, and Ostermayer are
primary; Habib's editorial and STAT's reporting are secondary, and the contested
0.76-0.83 range rests on a primary. Source floor met (8 sources, 6 primary, 2
secondary).

I opened every href. The six non-JAMA source URLs, both Go-deeper links (Fawcett
DOI, Google crash course), and both Background library links resolve; the two
library targets exist in the proof's library checkout. The two jamanetwork URLs
(Wong 2781307, Habib 2781313) return a Cloudflare interstitial to an automated
fetch but are the correct canonical article IDs and land on the source for a
human who clicks, so they pass the "lands on the source itself" test for a
reader. No break to route.

No claim broke. No miscitation. Nothing routed from this read.

## Cut

Three cuts, all self-reference or signpost the lesson template and slop spec
forbid in the body. The orientation section closed on "Same model, two numbers,
and the space between them is what this lesson is about" — the body naming the
lesson and pointing at its own subject, which the template reserves to the two
bookends. Cut whole; the paragraph now ends on the concrete "the area came out at
0.63." In the blind-spots section, "here the point is only that a strong AUROC
promises nothing about it" was a signpost describing what the piece was doing,
carried on a rare semicolon; rewritten to state the fact plainly and name its
subject ("Calibration is a subject of its own..."), losing the signpost and the
semicolon. In the Epic section, "This is the imbalance effect from the previous
section, now with a bedside price" carried a structural pointer; trimmed to "the
imbalance effect, now with a bedside price," which keeps the connection and drops
the direction to the reader.

Three sentences failed a dedicated slop pass, all of the self-reference and
signpost kind, none in the body's reporting. The pattern is one the body was
otherwise clean of: the drafter reached for the lesson's own scaffolding at
section seams. No empty conclusions, no negative-parallelism strawmen, no
decorative analysis, no puffery in the surviving prose. Edges read clean on the
second walk. The dek was checked against the recent comma-and mold flagged in the
brief: it is a single main clause with an appositive ("a measure that stays
silent on X and on Z"), not two independent clauses joined by comma-and, so it is
not that formula. Headings vary in construction (fragment, gerund, full sentence,
noun phrase) and avoid the "The one thing X never shows" closer mold. The chart
caption, bookends, and the "In plain language" note read clean.

## Reader

Reading straight through as the reader who has read only this: I can now say what
AUROC counts (the order of a random sick/well pair) before I judge it, and I can
hold that apart from calibration, from the one threshold a ward runs at, and from
how many alarms are false when the disease is rare. I can explain why Epic's 0.83
and 0.63 and its missed two-thirds are one story, not three. That is more than
any single source gives; the synthesis across eight is the article's own, and it
matches the original-work sentence in the handoff. The prose sits closer to the
voice-guide exemplars than a median summary: it breaks rates into whole people
(1,709 of 2,552; 8 or 109 worked up per case), grounds the ranking idea in a
concrete pair, and delivers its verdict with restraint ("a fair ranking and a
poor alarm"). The headline as the largest claim is true and defended.

## Edits

- Cut the orientation closer "Same model, two numbers, and the space between them is what this lesson is about" (body self-reference and signpost).
- Rewrote "That is a subject of its own, taught in calibration error; here the point is only that a strong AUROC promises nothing about it" to "Calibration is a subject of its own, taught in calibration error. A strong AUROC promises nothing about it" (dropped the signpost and the rare semicolon; kept the calibration-error link).
- Trimmed "This is the imbalance effect from the previous section, now with a bedside price" to "This is the imbalance effect, now with a bedside price" (dropped the structural signpost).

## Required work

None. The chart is honest (a single verified operating point against the
definitional diagonal, no fabricated curve, provenance and caption match the
evidence), the Epic figures are exact, the imbalance point is the fact not the
prescription, every href resolves for a reader, and structure passes
(nb check --no-check-links: BLOCK 0, WARN 0). The writer runs the final proof to
restamp the word count after the cuts; the orchestrator stamps the article.

## Decision

approve — the argument holds claim by claim, the Epic figures and the chart are
exact and honest, and the only defects were three body signposts, which I cut
directly.
