# editor review-brief: the-evidence/gans (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../writer/01/brief.md — the exact writer brief (check for instruction leakage)
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the evidence record (open as an opponent)
- ../../writer/01/draft-handoff.md — original-work sentence + proof notes
- ../../library/the-evidence/gans.html — the article to review
- ../../library/the-evidence/gans/asset-1.png — the captured source asset (Fig. 2 panels)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Proof (writer owns proof; you run nb stamp after direct cuts):
./nb check .nb-work/the-evidence/gans/library/the-evidence/gans.html --series the-evidence --library /home/user/library-checkout

This round's focus:
- Load-bearing distinction: confirm the piece separates origin-of-technique
  (true — the DCGAN→ProGAN→StyleGAN photoreal lineage is genuine GAN descent)
  from origin-of-photoreal-images (false — photoreal faces arrived 2017-2019),
  and states today's leading generators are diffusion, not GANs. If it lets "GANs
  made deepfakes" stand unqualified, that is a required fix.
- Numbers/labels against evidence: title is "Generative Adversarial Nets" (not
  Networks); the Parzen scores (MNIST 225±2, TFD 2057±26) and the fact GANs LOSE
  the TFD column to Stacked CAE (2110±50); the theory results are in the
  infinite-capacity limit with the paper's own "no theoretical guarantees" /
  "Helvetica scenario" concession; citation count presented as order-of-magnitude
  (~97,000, Google Scholar). Confirm no resolution is attributed to the paper's
  own text (resolutions belong to the datasets; only CIFAR-10 32×32 is used).
- Source asset: inspect asset-1.png against the article's argument and caption.
  The crop must retain the evidence the argument spends (the blurry/low-res
  sample panels) and the caption must be a factual cited label. Confirm
  data-nb-kind labels match the evidence record's primary/secondary classes.
- Recent-pattern notes to enforce: no "won on N GPUs" / "X on N of M" headline
  shape; no "the real X was Y" dek reveal; vary section headings away from
  comma-and pairs.

Decision: approve only when no publication-blocking issue remains. Record the
review at ../../editor/01/editorial-review.md.
