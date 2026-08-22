# Editorial review: the-instruments/imagenet-top-5-accuracy (editor/01)

## Skeptic

Thesis: a top-5 score records only whether one of a model's five guesses matched
the single label an image was assigned, so it cannot certify that the label was
right or that the model beats human vision; by 2015 the winning scores had fallen
below both the thin 5.1% human figure and into the range where the answer key's
own errors sit.

The claims it rests on, and how each held:

- Top-5 counts a hit when any of five guesses matches the one ground-truth label.
  Checked against Russakovsky et al. (s1), Sec 4.1 and the strawberry/apple
  passage the article quotes verbatim. Holds.
- The single-label key is thin, and in three distinct senses: Beyer's ~29%
  multi-label/synonym ambiguity (s5), Northcutt's ~6% outright wrong labels
  (2,916/50,000, s6), and Russakovsky's own ~0.3% small-sample estimate (s1). I
  opened all three and confirmed the article keeps them as three measurements of
  different things, never one blended "error rate." Holds, and cleanly.
- The winning error fell 28.2% (2010) to 3.57% (2015), crossing 5.1% and nearing
  the ~6% floor. The 3.57% traces to ResNet (s3); the year series to Russakovsky
  Tables 6-7 (s1). Holds.
- The 5.1% human figure was one trained annotator (Karpathy), not a population,
  with a second annotator at ~12%. Opened Karpathy's account (s7) and confirmed
  5.1% vs GoogLeNet 6.8%, the 500/1,500 training-and-labeling split, the
  "#forscience" line, the ~37% fine-grained share, and the "not a point ... a
  tradeoff curve" note. Holds.
- Correcting labels does not reorder the whole leaderboard; only near-top
  comparisons destabilize (ResNet-18 over ResNet-50 once the mislabeled share
  rises 6%). Opened Northcutt (s6): "unaffected ... however ... unstable" and the
  exact ResNet-18/50 threshold. The article states this precisely and does not
  overreach into "corrected labels flip the leaderboard." Holds.

Display text, checked descriptor by descriptor: the headline is an accurate,
defended claim. The dek carried two faults that reach every reader. First, "just
as independent relabelings found" placed the 2020/2021 relabelings in temporal
lockstep with the 2015 crossing, which is false — the relabelings are
retrospective, years later. Second, "did not fit the one label" pushed Beyer's
29% (under-description) toward the wrongness reading the whole lesson exists to
prevent, blurring it into Northcutt's 6%. I recast the dek to fix the chronology
("later relabelings") and to state the 29% as images that "fit more than the
single label," which is what multi-label/synonym ambiguity actually is. The
takeaway called the 5.1% "one tired annotator's afternoon," but the body
establishes 1,500 images at about one a minute (many hours, not an afternoon); I
corrected it to "over many hours" to match the article's own reporting.

data-nb-kind audit: 7 primary, 2 secondary, as the brief specifies. Each primary
owns the claim it carries (Karpathy is firsthand on the human baseline, so
primary is right); both secondaries (Forbes, MIT Technology Review) report the
milestone from outside. All correct.

Every citation href opened as printed. All nine resolve to the source itself:
the six arXiv/NeurIPS primaries, Karpathy's post, the Forbes headline verbatim,
and the MIT Technology Review piece with its Baidu rule-break note. No routed
sourcing failures.

Chart: opened chart-1.py and chart-1.png. Every plotted point (28.2, 25.8, 15.3,
11.7, 6.66, 3.57) traces to the evidence and its owning primary; the 5.1% human
line and ~6% label band are drawn from Russakovsky and Northcutt respectively.
The excluded 2016-2017 figures do not appear. The y-axis is linear 0-30 and
labeled, both reference lines are labeled, and the visual claim (the curve ends
below both bands by 2015) is honest. No chart correction to route.

## Cut

Ten sentences failed the reads and were removed or recast. The recurring pattern
was the structural signpost: sentences that narrate where the argument stands
rather than advance it. "It draws the first line of the lesson," "The next two
sections take those in turn ... The labels come first," and "it is worth stating
flatly before any criticism of the score" all describe the article's own moves
and violate the template's rule that the body never mentions the lesson; I cut
the scaffolding and kept the substantive clause each was wrapped around. A second
pattern was the reader gesture the body is not allowed: "Keep them apart" and "A
reader who collapses them ... has lost the point" both address a hypothetical
reader, and the second merely restated a separation the three-definition passage
already lands, so I recast the first without the imperative and deleted the
second. Two more failed the placeholder test outright: "For a few years the
number moved faster than almost anyone expected" (vague attribution, no checkable
fact) and "It also does something worth naming next to it, in the way a good
critic separates what a score records from what people read into it" (a
method-describing preface with no content). Both went, and the concrete sentences
behind them now lead. I also tightened the human-baseline sentence so the 5.1% is
attributed to the better of two annotators rather than reading as an average of
the pair.

Formula check against the recent record: the recast dek does not use the "A
[perfect] X score means Y" mold and carries no negative-parallelism reflex; the
orientation heading is in ImageNet's nouns, not the "The number on the model
card" mold. Earned "not X" contrasts (top-5 "was not a hedge," the strawberry
problem "was not an edge case," the line was "one motivated person ... not a
population") each correct a misreading the piece actually names, so they stay.

## Reader

Read straight through, the piece gives what no single source does: it sets the
year-by-year fall against both the human line and the label-error floor in one
figure, and holds Russakovsky's, Beyer's, and Northcutt's three numbers apart in
one passage, so a reader sees that once the score dropped past the floor it was
scoring the answer key as much as the model. The draft-handoff's original-work
sentence claims exactly that fusion, and the article delivers it. The prose sits
close to the voice-guide exemplars: each term is defined on a concrete instance
(the husky ranked under Eskimo dog, the strawberry that also holds an apple), the
metric is credited before it is faulted in Roser's register, and the misled case
is one identifiable overreach (the Forbes headline, the Baidu rule-break for a
quarter-point lead) rather than a general lament. Well above a median summary.

## Edits

- Recast the dek (nb-meta and rendered dekline, kept verbatim identical): fixed the false "just as" contemporaneity of the relabelings and changed "did not fit the one label" to "fit more than the single label" so the 29% reads as ambiguity, not error.
- Cut the signpost "It draws the first line of the lesson:" from the orientation close, keeping the substantive sentence.
- Cut "It also does something worth naming next to it, in the way a good critic separates what a score records from what people read into it," and bridged the pivot with "But."
- Cut the weak opener "For a few years the number moved faster than almost anyone expected."
- Cut "and it is worth stating flatly before any criticism of the score" from the AlexNet paragraph.
- Cut the structural signpost "The next two sections take those in turn ... The labels come first."
- Recast "Keep them apart, because they are often blurred into a single scary statistic ..." to remove the reader address and the loose "scary."
- Cut "A reader who collapses them into a single 'the labels are wrong X% of the time' has lost the point."
- Tightened "The 5.1% came from two trained expert annotators. The better of the two was Andrej Karpathy ..." so the figure is attributed to the better annotator, not read as a pair average.
- Corrected the takeaway's "one tired annotator's afternoon" to "over many hours," matching the body's own 1,500-images-at-one-a-minute reporting.

## Required work

None. The label-noise-first framing, the three-error separation, the exact
ranking point, the secondary human-baseline crack in ImageNet's own record, the
required Background link to the GLUE lesson, and the chart provenance all hold.
Word count in nb-meta is now stale after the cuts; the stamp recomputes it.

## Decision

approve — the claims trace to the sources, the three error measurements and the
label-first framing hold, the chart is honest, and the display-text and slop
faults were fixable in place; only stamping remains.
