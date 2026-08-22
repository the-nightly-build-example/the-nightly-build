# Commission: the-instruments/imagenet-top-5-accuracy

## Assignment

One lesson on a single measurement: top-5 accuracy (equivalently top-5 error) on
the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), the number behind
"AI has beaten humans at image recognition." The Instruments teaches how a number
is made and what it can and cannot support, with at least one real case where it
misled people and what that cost. The reader is smart, widely read, new to
computer-vision benchmarks. Define the terms (top-1 vs top-5, error vs accuracy,
the 1,000-class single-label task) at first use.

## Why this measurement, now

Top-5 error is the metric that scored AlexNet's 2012 win and the 2015 "superhuman"
milestone, and it is still cited as proof that machine vision matched or passed
people. The number has two well-documented cracks: the human baseline it was
measured against, and the test's own labels. Both matter to anyone who reads a
"model X reaches Y% on ImageNet" claim today.

## Angle

Explain exactly how the number is produced: 1,000 classes, one ground-truth label
per image, top-5 counts a hit if any of the model's five guesses matches that one
label. Then show what it cannot support. Lead the "misled" case with the labels,
not the human baseline, so the lesson does not repeat the GLUE lesson's
"human line was a hurried estimate" finding: many ImageNet images contain more
than one real object but carry a single label, and independent relabeling found
the validation set's labels are wrong or ambiguous often enough that models near
the top were being scored against a noisy key (Beyer et al., *Are we done with
ImageNet?*, 2020; Northcutt et al. on pervasive label errors, 2021). Top-5 was
designed partly to paper over exactly this single-label-multi-object problem, and
it saturated once model error fell near the label-error floor. Bring in the human
baseline as a supporting crack, told in its own terms: the ~5.1% top-5 human
figure came from a very small annotation effort (Russakovsky et al., 2015;
Karpathy's write-up), so "superhuman" compared a 2015 model against one or two
trained annotators, not "humans." The cost: a decade of "machines see better than
people" claims resting on a single-label test scored against a flawed key.

## What to teach (short, complete)

1. The task and the metric: ILSVRC's 1,000 classes, one label per image, ~1.2M
   training and 50,000 validation images; top-1 vs top-5, with a worked example of
   why top-5 forgives a plausible near-miss.
2. Why top-5 existed: the single-label / multiple-objects mismatch, with a
   concrete image example, and how top-5 hides it.
3. The label problem: independent relabeling and cleaned-label results (multi-
   label accuracy, measured label-error rate), and what happens to the ranking of
   top models when the key is corrected.
4. The human-baseline crack, in proportion: where 5.1% came from and why "beat
   humans" overreads it.
5. The cost / present use: how the metric still gets cited, and what a careful
   reader should take a stated ImageNet number to mean now.

## Boundaries and non-overlap

- Do not restate the GLUE lesson (the-instruments/glue), whose finding is that a
  language benchmark's "human level" was a hurried crowd estimate on leaky tasks.
  The human-baseline point here is secondary and told through ImageNet's own
  annotation record; the primary finding is label noise and single-label scoring.
  Require a Background link to the GLUE lesson rather than re-arguing it.
- alexnet appears in the-evidence and canon-papers as a document; this lesson is
  about the *metric*, not the AlexNet paper. Do not turn it into a paper reading.
- Teach top-1/top-5 and label noise here; link, don't re-teach, anything the
  library already covers (researcher to check via `nb history`).

## Source policy

Lesson in The Instruments: at least 8 sources, at least 4 primary and at least 1
secondary. Primary: the ILSVRC paper (Russakovsky et al., IJCV 2015), *Are we
done with ImageNet?* (Beyer et al., 2020), the label-errors paper (Northcutt,
Athalye, Mueller, 2021) and/or labelerrors.com, the AlexNet result for the metric
value, cleaned-label leaderboards. Secondary: contemporaneous reporting of the
"superhuman" milestone for the misled-case framing.

## Habits to avoid (break these, from the recent record)

- The recent Instruments deks lead with "A [perfect/faithful] X score means Y" or
  "An X rate/win rate is Z" (needle-in-a-haystack, hallucination-rate, alpacaeval,
  rouge). Do not copy that mold. Write a dek in ImageNet's own nouns that states
  the concrete finding (the labels, the single annotator, the saturation).
- Vary the orientation heading from the recent "The number on the model card" /
  "What X actually names" openers.
- Furniture: a small table (top-1 vs top-5, or year-by-year winning error) or a
  single figure earns its place only if it changes understanding; do not stack.

## This run's neighbors

Also publishing tonight: the-evidence/whisper, the-mechanics/overused-words,
what-could-go-wrong/value-lock-in, when-ai-breaks/itutorgroup-age-discrimination.
One paper, one register; do not converge on a shared dek shape.

## Production record

- Harness: claude-code-routine. Writer model: claude-opus-4-8 (production policy
  asks "capable"; no pinned model, so no deviation).
- Effort per balanced policy: coach low, researcher high, writer medium, editor
  high. None required. Template: lesson.
