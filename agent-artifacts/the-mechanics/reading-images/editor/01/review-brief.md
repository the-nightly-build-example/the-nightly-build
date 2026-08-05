# editor review-brief: the-mechanics/reading-images (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/writer/01/draft-handoff.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/library/the-mechanics/reading-images.html — the drafted article (includes asset-1.png, a ViT Figure 1 crop)
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/.nb-context/ — the effective template contract

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/editor/01/editorial-review.md

If your cuts leave the article publishable, the orchestrator runs nb stamp and
the final nb check; return to the writer only if the proof needs new prose.

This round's focus:
- The central editorial test: the article must NOT claim patchification causes
  miscounting/misreading. Confirm the grid is framed as a bounded budget (not a
  ceiling), the vendor-documented failures are reported empirically, the
  resolution-improves-accuracy link is called directional, and the causal
  question is marked open. If any sentence hardens that into a finding, cut or
  route it.
- No-code rule (series): confirm there is no code anywhere. The only arithmetic
  is the patch count (196 from a 224x224 image at 16x16 patches), which is
  allowed. Verify 196 is presented as an illustrative config, with OpenAI's real
  85+170-per-tile / 765-for-1024x1024 accounting cited for a real number.
- Inspect the source asset (asset-1.png): open it and compare with the ViT
  primary. The crop must retain the patch-to-projection evidence the argument
  spends and omit unrelated clutter; the caption must be a factual cited label,
  interpretation in prose only.
- The writer flagged one judgment: the closing ties the coarse-grid detail loss
  to the earlier letter-counting lesson as an uncited analogy (a course tie-in,
  not a causal claim). Decide whether it reads as reaching; trim if so.
- Confirm links to prior lessons (word-embeddings, attention, hallucination,
  letter-counting) are plain in-prose links, not numbered sources, per the press
  voice, and that no taught ground is re-taught as new.
- Confirm the takeaway bookend resolves the opener without a Verdict-style
  restatement block, and check heading cadence against the recent the-mechanics
  run.
