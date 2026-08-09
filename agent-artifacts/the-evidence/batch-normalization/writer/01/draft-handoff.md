# Draft handoff: the-evidence/batch-normalization (01)

## Original work

This article separates the technique from its explanation and stages "internal
covariate shift" as a name that outlived the mechanism it labeled: it sets the
paper's own title-claim against the one controlled experiment that drives that
distribution shift up on purpose and finds training unmoved, then holds the
technique's intact standing and the explanation's failure in the same frame
rather than letting the correction erase either. The evidence record supplies
every part; the staging, and the judgment that the phrase persists while the
explanation does not, are the article's.

## Proof result

`./nb check … --series the-evidence --library <checkout>` (links included):
`BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. Stamped words=1877,
reading_minutes=8, sources=6 (5 primary, 1 secondary). No warning left standing.

Two warnings were raised mid-iteration and both fixed, not waived: a 55-word
dense sentence (split into three) and a citation-order violation (d2l was cited
before Wu & He; renumbered so d2l=s5, Wu & He=s6, matching first appearance).

## Choices worth flagging to the editor

- Both evidence cautions honored. The paper's *distributional* internal
  covariate shift and Santurkar's *gradient-based* redefinition are named as
  different quantities in the "test" section, with the note that the noise
  experiment strikes the distributional version directly. The "beats human
  5.1%" figure is attributed to Russakovsky (s2), with its one-annotator,
  1,500-image denominator stated in prose beside the ensemble number.
- The one earned "method right, reason wrong" contrast lands twice by design:
  once on the smoothing claim ("smoothing is real … but not something only
  batch normalization does") and once in the takeaway close ("The technique is
  not in doubt. The explanation printed in its title is."). I recast a third,
  formulaic "X rather than Y" (the Wu & He limit) into a plain statement to keep
  the count to a couple.
- No chart or source asset. The evidence identifies Figure 2 (the training
  curves) as a candidate, but I hold only two verified points per curve
  (steps-to-72.2% and final accuracy), not an honest full series, so a chart
  would either invent the curve or duplicate the stat strip. The 14x and 4.82%
  numbers ride the stat strip instead; the one annotated equation carries the
  mechanism.
- Author first names were pulled out to match the evidence exactly (last names
  only for Santurkar/Tsipras/Ilyas/Madry, Bjorck, Wu & He), since the record
  does not supply first names.

## Open questions

None blocking. The evidence's unverified adversarial-training lead (a setting
where ICS-like shift may matter) is left uncited per the record's own
instruction; if a later brief resolves it, it would bound the "clean-training"
scope of Santurkar's conclusion and could earn a sentence.
