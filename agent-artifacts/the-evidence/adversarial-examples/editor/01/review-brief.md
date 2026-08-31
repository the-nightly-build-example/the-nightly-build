# editor review-brief: the-evidence/adversarial-examples (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the assignment, boundaries, and the reader's situation
- ../../writer/01/brief.md — the exact writer brief (needed to catch leakage and framing)
- ../../writing-coach/01/voice-guide.md — read first; the sound the piece should hold
- ../../researcher/01/evidence.md — the claim set to test the draft against
- ../../writer/01/draft-handoff.md — open the original-work sentence only on the third read
- the article: /home/user/the-nightly-build/.nb-work/the-evidence/adversarial-examples/library/the-evidence/adversarial-examples.html
- the source asset: /home/user/the-nightly-build/.nb-work/the-evidence/adversarial-examples/library/the-evidence/adversarial-examples/asset-1.png (the paper's Figure 1 panda example)
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/adversarial-examples/.nb-context/

Round focus:
- Push hardest on the "still unsolved" framing: confirm it reads as a wide gap WITH
  real, measured progress (Madry PGD; certified defenses; CIFAR-10 robust accuracy
  ~46% in 2018 to ~74% in 2024 vs ~94% clean), not "nothing works," and that the
  ceiling-is-real point is attributed to Bartoldson.
- Confirm the paper's linear explanation is presented as its claim and marked
  contested (boundary-tilting; non-robust features; no consensus), not stated as
  settled; and that the paper's own single-step FGSM defense is correctly
  downgraded (gradient masking; the "harnessing" held only in the later multi-step
  PGD form).
- Provenance: confirm the piece frames the 2013→2015 relation as the same
  researchers (Goodfellow, Szegedy on both) advancing their own work, not a rival
  correction.
- Verify display-text figures against the evidence: perturbation epsilon 0.007;
  panda 57.7% to gibbon 99.3% on GoogLeNet; the MNIST figures.
- Inspect the source asset as evidence, not decoration: the crop must retain what
  the argument spends (the three-panel panda + perturbation + gibbon) and the
  caption must be a factual cited label. A KaTeX FGSM equation and an nb-table are
  used; confirm both are documented furniture and correct.
- Body addresses no one; only the two bookends speak to the reader; no Verdict.

Recent-pattern notes (compare edges, headings, dek; flag any formula):
Recent the-evidence deks/headlines this piece must not echo in mold —
- "The diffusion paper behind today's image generators could not take a prompt"
- "Tested on Atari and robots in 2017, PPO now tunes billion-parameter models"
- "Google packed a whole sentence into a single vector"
- "LoRA matched full fine-tuning by training 4.7M of GPT-3's 175 billion weights"
- "The Vision Transformer lost to a plain CNN until it was fed 300 million images"
The most recent piece (denoising-diffusion) used an nb-stat-strip opener and a
"where the X actually comes from" closer; check this piece's shape differs.
