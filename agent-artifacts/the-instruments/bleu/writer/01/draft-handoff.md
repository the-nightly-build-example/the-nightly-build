# Draft handoff — writer 01 — the-instruments/bleu

## Original work

This article builds a single self-authored, hand-verified BLEU computation
(candidate "the small brown dog chased the red ball across the yard" against
reference "...quickly chased...") and carries it through every mechanical
step — clipped n-gram precision for n=1..4, the geometric mean, the brevity
penalty, and the final score of 0.742/74 — that the evidence record verified
against Papineni et al. 2002's own formulas but that no single source states
as one worked run; it then uses that same arithmetic (clipping's blindness to
a word absent from the reference) to explain, in the reader's own terms, why
the 2005 NIST evaluation's hybrid entry could match fewer n-grams with fluent
synonyms and still deserve the human judges' 1st-place ranking that BLEU
denied it. Connecting the toy arithmetic to the real misranking case, rather
than presenting them as two separate facts, is the article's own work: the
evidence record supplies the verified numbers on both sides, but not that
link.

## Article and asset paths changed

- `.nb-work/the-instruments/bleu/library/the-instruments/bleu.html` (edited
  from the initialized skeleton; no assets/charts used, none warranted by
  the evidence record's Source assets notes).

## Proof result

```
nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
BLOCK: 0
WARN: 0
verdict: PUBLISHABLE
```

No warnings left outstanding. Notable fixes made en route to a clean proof:

- Caught and corrected a fabricated detail during self-review: an early
  draft paragraph invented a "78 to 80" sub-range inside Google Cloud's
  practitioner BLEU quality tier. The evidence record only supports a ">60:
  quality often better than human" open-ended tier. Rewrote the sentence to
  cite the real boundary (60) and use the actual irony it supports: the
  worked example's score of 74 already falls inside that tier.
- Trimmed from an initial 2,831 words to the top of the lesson band (2,200)
  by cutting a supplementary Systran-vs-SMT paragraph (kept the primary 2005
  NIST case, which carries the required contribution) and tightening prose
  throughout without dropping any cited claim.
- Split a 43-word, 2-clause-join sentence in the takeaway (flagged by
  W-SENTENCE-DENSITY) into three shorter sentences.

## Editorial requests addressed

None — this is round 1, no prior editorial-review.md exists yet.

## Remaining evidence or voice questions

None. The evidence record's "Numbers" section covered every figure the
commission's three ideas needed, including the steelman/critique tension
(Reiter vs. Mathur), which the article holds via a holds-up grid and a single
Verdict note rather than resolving into a false single answer, per the
evidence file's own instruction. The one deliberately unused evidence detail
is source 2's Systran case (cut for word budget, not for doubt about it).
