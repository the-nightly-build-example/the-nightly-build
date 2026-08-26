# writer brief: the-evidence/vision-transformer (01)

Inputs:
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages.
- `researcher/02/evidence.md` — the complete claim set (supersedes 01; 02 adds the required secondary source and is the record to draft from); draft only from what it opened.
- The initialized article: `.nb-work/the-evidence/vision-transformer/library/the-evidence/vision-transformer.html` — edit in place; do not recreate the skeleton.
- Effective template contract and furniture catalogs under `.nb-work/the-evidence/vision-transformer/.nb-context/`.

Output: `.nb-work/the-evidence/vision-transformer/agent-artifacts/the-evidence/vision-transformer/writer/01/draft-handoff.md` (and the edited article in place).

Proof (run from repo root `/home/user/the-nightly-build`):
`./nb check --series the-evidence --library /home/user/library-checkout .nb-work/the-evidence/vision-transformer/library/the-evidence/vision-transformer.html`
Iterate with `--no-check-links`; run the full command (links on) to `BLOCK: 0` before handing off. Run `nb stamp` before the final check.

This document is the ViT paper. Teach what it measured and the condition it attached.
Do NOT re-teach the Transformer, self-attention, or how a picture becomes tokens —
link `the-mechanics/reading-images` (patch embedding), `the-mechanics/word-order` and
`the-evidence/attention-is-all-you-need` at first use.

Adjacency alert: `the-evidence/clip` (published 2026-08-25) is the neighbor and its
best model is a ViT. Stay on ViT's own territory (supervised classification and the
pretraining-data threshold). A single link to the CLIP piece is welcome; a second
pass over CLIP's contrastive/robustness argument is repetition — do not do it.

Evidence caveats you must respect (from the record):
- State "ViT trails CNNs on mid-size data and matches/beats them only after
  large-scale pretraining" as what the 2020 paper SHOWED, not as a standing
  present-tense law. The present-day correctives soften it: DeiT reaches 83.1% on
  ImageNet-1k alone with no JFT (use 83.1% no-distillation as the fair headline;
  "up to 85.2%" is a 1000-epoch distilled row — do not overquote it). ConvNeXt, a
  modernized CNN, matches Transformers at equal data.
- JFT-300M is Google-internal; the two owning papers report slightly different
  snapshots (303M images / 18k classes in ViT; ~300M images / 375M labels in Sun et
  al.). Keep them separate; do not merge into one figure.
- Pin every accuracy to its exact model, dataset, and resolution (e.g. BiT-L =
  ResNet152x4 on JFT-300M at 87.54%). The Contradictions section carries the
  qualifications the editor will test — address them.

Set the nb-meta writer model field to `claude-opus-4-8`.

Recent Evidence habits to break (do not inherit; the last three pieces were
clip, retrieval-augmented-generation, adam-optimizer):
- The opener mold "You have probably seen X used as shorthand for... Both the model
  and the number are real." — find a different way in, and do not use "By the end
  you will be able to...".
- The takeaway mold "Read as X, the number holds. Read as Y, it does not." /
  "Read [the number] as ..." — do not reuse it; land the judgment in this article's
  own frame.
- The phrase "doing the work" ("the data, not the objective, did the work") is a
  house tic (the CLIP piece used it twice); do not use it.
Name your one original-work sentence in the handoff.
