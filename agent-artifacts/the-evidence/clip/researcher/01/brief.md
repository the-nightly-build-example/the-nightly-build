# researcher brief: the-evidence/clip (01)

Inputs:
- commission.md (at the artifact root): the angle, the three candidate teach
  points, the boundaries, and the source floor.
- editorial-direction.md (at the artifact root): the citation standard,
  primary/secondary test, the reader, and the-evidence series territory.

Output: agent-artifacts/the-evidence/clip/researcher/01/evidence.md

This round's focus:
- Get CLIP's own numbers from the CLIP paper (and its appendices/figures):
  the 400M WIT training-pair count, the contrastive objective, the zero-shot
  ImageNet top-1 figure and what supervised baseline it matched, the prompt-
  engineering/ensembling gain (bare label vs "a photo of a {label}" vs
  ensembled prompts), and the per-task spread where zero-shot is weak
  (counting, satellite/aerial, fine-grained, abstract tasks). Record exact
  figures with their denominators and the table/section they come from.
- Verify the WIT dataset was proprietary/unreleased and record what the paper
  says about its construction and scale.
- Find at least one line of later primary work bearing on the headline
  claims: for example prompt-sensitivity or robustness follow-ups, dataset-
  contamination analyses, or a public reproduction (OpenCLIP / LAION-trained
  CLIP) and what it did or did not reproduce. Classify each primary or
  secondary and say why.
- Hunt for what breaks the angle: evidence that zero-shot transfer is more
  robust or more general than the "it borrowed from prompt engineering and
  scale" reading suggests. Record it in Contradictions.
