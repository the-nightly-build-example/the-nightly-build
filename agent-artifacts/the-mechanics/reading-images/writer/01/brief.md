# writer brief: the-mechanics/reading-images (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/editorial-direction.md — house standard, paper voice, series prompt
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/commission.md — behavior, angle, ideas to teach, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/writing-coach/01/voice-guide.md — the craft standard (single downward trace; reader does the patch arithmetic)
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/researcher/01/evidence.md — the complete, verified claim set
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/library/the-mechanics/reading-images.html — the initialized article to edit in place
- /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/.nb-context/ — the effective template contract and runtime assets

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/agent-artifacts/the-mechanics/reading-images/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-mechanics/reading-images/library/the-mechanics/reading-images.html --series the-mechanics --library /home/user/library-checkout
(iterate with --no-check-links; final pass with links, until BLOCK: 0)

nb-meta to fill: date 2026-08-05, harness claude-code-routine, model claude-opus-4-8. Run nb stamp for the counts.

This round's focus — the evidence record corrects the commission's causal
punchline. Follow the evidence, not the commission, where they differ:
- Do NOT write that the model "never gets more detail than the patch grid, which
  is exactly why it miscounts and misreads." No primary owns that causal claim,
  and LLaVA-NeXT shows the opposite direction: more tiles at higher resolution
  measurably improve detail and cut OCR errors. Soften to: the model sees only as
  fine as the chosen grid, and that grid is a token-cost tradeoff, not a hard
  ceiling. Report the miscount/misread failures as empirically documented (the
  GPT-4V system card documents them without naming a cause), and treat the
  resolution-improves-accuracy link as directional evidence, not mechanistic
  proof. This is a genuinely open question — mark it as one, per the series rule.
- The 196-token figure is ViT's illustrative config; real systems run from ~64 to
  2880+ tokens per image. Use 196 to teach the arithmetic, but say plainly it is
  an example configuration, and cite OpenAI's documented tile accounting (85 base
  + 170 per 512px tile; 1024x1024 = 765 tokens) for a real number.
- The internal mechanism is undisclosed for the closed consumer models the reader
  uses (GPT-4V/4o, Claude, Gemini). Teach patchify-project-attend as the field's
  documented method, not as an asserted fact about any specific product.
