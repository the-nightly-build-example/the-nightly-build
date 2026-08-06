# writer brief: the-evidence/gans (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../commission.md — subject, angle, required contribution, boundaries
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../library/the-evidence/gans.html — the initialized article to edit (relative to workspace root)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md (and the edited article HTML)

Proof: ./nb check .nb-work/the-evidence/gans/library/the-evidence/gans.html --series the-evidence --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --no-check-links while iterating, then full command with links until BLOCK: 0)

Decisions the inputs do not carry:
- Title is "Generative Adversarial Nets" (not "Networks"); the arXiv HTML landing
  page mislabels it. Use "Nets" for the paper's title.
- The paper's whole quantitative case is four Parzen-window numbers under a metric
  its own authors disclaim, and it never claims high-res or photoreal output.
  Resolutions (CIFAR-10 32x32, etc.) belong to the DATASETS, not the paper — do
  not attribute a resolution to the paper's own text. GANs actually LOSE the TFD
  column to Stacked CAE (2110±50 vs 2057±26); that is a strong thin-foundation
  detail worth using.
- Hold the key distinction the evidence draws: origin-of-technique (true — the
  DCGAN→ProGAN→StyleGAN photoreal lineage is genuine GAN descent) vs
  origin-of-photorealism (false — photoreal faces arrived 2017-2019, years later),
  and today's leading generators are diffusion, not GANs. Make that separation.
- The theory results (optimum -log 4 at pg=pdata) are explicitly in the
  infinite-capacity limit; the paper itself concedes real MLP generators have "no
  theoretical guarantees" and can collapse ("the Helvetica scenario"). Represent
  the theory/practice gap in the paper's own terms.
- Citation count rests on Google Scholar alone (~96,878, read 2026-08-06);
  present as an order-of-magnitude fame indicator, not exact.
- nb-meta: date 2026-08-06; harness "claude-code-routine"; model set to the model
  you are actually running on. `nb stamp` writes counts.
- Recent habits to break: do not reuse the "won on N GPUs" / "X on N of M"
  headline shape; a number in the headline only if it is the story. Vary section
  headings away from comma-and pairs; avoid the "the real X was Y" dek reveal.
- Link, do not re-teach: the-mechanics/word-embeddings and reading-images exist;
  link if useful as Background rather than re-teaching. Do NOT drift into a GAN
  mechanics tutorial — this is a lesson about the document.
