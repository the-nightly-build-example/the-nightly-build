# draft-handoff: when-ai-breaks/amazon-rekognition-congress (01)

## Original-work sentence

The article turns the ACLU's two bare counts into the more than thirteen million
one-to-one comparisons the test actually ran, so the 28 false matches read as the
arithmetic of a loose cutoff against a large gallery rather than as a headline;
and it draws the line the raw sources leave implicit, separating the
gender-classification error rates (Gender Shades, Actionable Auditing) from the
face-matching false-positive gap NIST measured across other developers but never
on Rekognition, which Amazon declined to submit.

This work is visible in the "A bigger gallery buys more chances to be wrong"
section (the 535 x 25,000 comparison count) and in "The wrong hits did not fall
evenly" plus the Verdict note (the measured-vs-inferred line).

## Proof result

`nb check` with links: **BLOCK: 0**, verdict PUBLISHABLE. All nine source URLs
resolved.

One warning intentionally left:

- **W-SENTENCE-DENSITY** on the takeaway's 48-word, three-join sentence
  ("It proved something narrower and more useful: that a face 'match' is ...,
  that searching thousands ..., and that where face systems have been measured
  ..."). It is a deliberate three-part parallel that names the three mechanisms
  the lesson taught and sets up the three questions the reader is handed next.
  Splitting it would break the parallel the takeaway is built on. All other
  density warnings from earlier passes were fixed by splitting.

Correctness caveats from the brief were held: the 31.37% / 34.7% / 0.8% figures
are stated only as gender-classification error, never as Rekognition's
face-match error rate; NIST carries the matching gap in general and is stated as
never having tested Rekognition; the ACLU's ~40%/20% skew is presented as a
description of the 28, not a per-group rate; the test is dated July 2018
throughout (the MIT Technology Review 2019 misdate was not followed).

## Open evidence / voice questions

- The 95% row in the threshold table rests on the ACLU reply's paraphrase of
  Amazon ("saying yesterday it should be 95 percent," s3), not on an Amazon
  primary that states 95% directly. It is attributed to the ACLU reply and
  labeled "Amazon, the day it disputed the test." No Amazon primary in the
  evidence record states 95%; if the editor wants the figure dropped to only the
  documented 80/85/99, the table row can go without harming the argument.
- The Verdict note says "other developers submitted theirs" rather than naming a
  count; the "99 other developers" figure appears in the evidence record's
  contradiction narrative but is not tied to a citable source quote, so it was
  left out.

No blocking evidence or voice gap. No source asset was used: the argument's
demographic section leans on NIST for the matching gap and keeps the
classification figures in prose, so capturing the Actionable Auditing table or a
NISTIR 8280 plot risked presenting a classification chart as a match-rate visual,
the exact conflation the brief rules out. Furniture is one table (the shifting
threshold) and one Verdict note, chosen to avoid the recent nb-note/nb-figure/nb-stat reflex.
