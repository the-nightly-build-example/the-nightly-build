# review brief: the-evidence/vision-transformer (editor/01)

Inputs (read in the order the editor skill names):
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound (read first).
- `commission.md` (artifact root) — the assignment, boundaries, and reader situation.
- `writer/01/brief.md` — the exact writer brief (so a leak is visible against it).
- `researcher/02/evidence.md` — the evidence record to audit against (02 supersedes 01;
  it adds the required secondary). Leave closed until the skeptic read calls for it.
- `writer/01/draft-handoff.md` — the writer's handoff (original-work sentence closed until third read).
- The article: `.nb-work/the-evidence/vision-transformer/library/the-evidence/vision-transformer.html`.
- Template context under `.nb-work/the-evidence/vision-transformer/.nb-context/`.

Output: `.nb-work/the-evidence/vision-transformer/agent-artifacts/the-evidence/vision-transformer/editor/01/editorial-review.md`

Round focus:
- This lesson reads one paper (ViT). Verify it states the data condition as what the
  2020 paper SHOWED, not as a standing present-tense law, and that DeiT/ConvNeXt are
  used to draw the line between what holds and what was oversold. Push on any sentence
  that lets "Transformers beat CNNs" stand unconditionally.
- Numbers: every accuracy pinned to its exact model, dataset (ImageNet-1k / -21k /
  JFT-300M), and resolution. The two JFT snapshots (303M/18k in ViT; ~300M/375M in Sun
  et al.) must stay separate, not merged. Recompute/compare figures against the record.
- The secondary (Khan et al. survey, cited as s4) must be used only for the qualitative
  "received view" claim, NOT for its unverified "13% drop" figure. Confirm the writer
  did not carry the unverified number. Audit every data-nb-kind.
- Adjacency: CLIP must be linked once, not re-covered. `the-mechanics/reading-images`
  and the attention lesson should be linked rather than re-taught. Flag any re-teaching.

Recent-pattern notes (compare edges, headings, dek, furniture against these):
- House tics forming across the paper, cut on sight if present: the why-bookend closer
  "By the end you will be able to..."; the takeaway mold "Read [the number] as X ... and
  ask separately whether Y" / "Read as X it holds; read as Y it does not"; the phrase
  "doing the work" ("the data, not the objective, did the work"); the device "It is
  tempting to say X. That goes too far."; the negative-parallelism reflex where the "not"
  clause is an invented strawman.
- The last three Evidence pieces were clip, retrieval-augmented-generation, adam-optimizer.
  clip opened "You have probably seen X used as shorthand for... Both the model and the
  number are real." and closed on the "Read as X... Read as Y..." mold. If this draft's
  opener or takeaway is built to either shape, it is a formula — break it without copying
  prior structure.
