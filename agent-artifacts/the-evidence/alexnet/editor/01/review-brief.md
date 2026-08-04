# editor review-brief: the-evidence/alexnet (editor/01)

Inputs:
  ../../commission.md — the document, angle, boundaries
  ../../editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
  ../../writer/01/brief.md — the exact writer brief (for prompt-leakage comparison)
  ../../writing-coach/01/voice-guide.md — credit-then-correct register, licenses, do-not-reuse list
  ../../researcher/01/evidence.md — the claim set to test against
  ../../writer/01/draft-handoff.md — original-work sentence, proof state, the "gaming GPUs" flag
  ../../../../library/the-evidence/alexnet.html — the drafted article (includes chart-1.png + chart-1.py)
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs
Output: ./editorial-review.md

Recent-pattern notes: the-evidence has overused the negative-reveal dek mold and
the "shorthand overshoots" framing (the immediately prior AlphaFold piece); and
the "What X actually says/proved" heading mold with the "actually" reflex. Check
dek and headings against the coach's do-not-reuse list — the finding here must
not read as a debunk.

Round focus: verify the two sharpening findings hold exactly — (1) the famous
15.3% top-5 is the seven-CNN ensemble (two nets pre-trained on Fall-2011 data)
while the single model scored 18.2%, still ~8 points ahead of the 26.2%
runner-up; do not let 15.3% stand in for the single model; (2) GPU-trained deep
CNNs (Ciresan/DanNet) won vision contests before AlexNet and AlexNet cites them —
method predates the paper, not an invention story. Confirm BatchNorm, ViT, and
Recht et al. are each attributed to their own primary and none overstated as a
universal verdict. Inspect the committed chart: open chart-1.py and chart-1.png,
compare every number to the evidence and the owning primary, and read the image
as a reader (labels, scale, honesty). Weigh the writer's flag: the headline calls
the two GTX 580 3GB cards "gaming GPUs" — accurate for the consumer GeForce line
and a 2026 reader's handle, but editorial framing; decide keep / "consumer" /
bare model name. Approve only if no publication-blocking work remains.
