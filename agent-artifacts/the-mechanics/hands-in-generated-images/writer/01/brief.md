# writer brief: the-mechanics/hands-in-generated-images (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the causal chain, boundaries, source policy, nb-meta values, habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- the initialized article: /home/user/the-nightly-build/.nb-work/the-mechanics/hands-in-generated-images/library/the-mechanics/hands-in-generated-images.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/hands-in-generated-images/.nb-context/

Output: draft-handoff.md (in this directory), plus the edited article.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/the-mechanics/hands-in-generated-images/library/the-mechanics/hands-in-generated-images.html --series the-mechanics
  (iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.)

This round's focus — precision the evidence forces (see evidence limitation and Contradictions):
- No source measures a base rate of malformed hands. Keep the frequency
  qualitative; do not assert a percentage of wrong hands. In particular,
  HandRefiner's "97 of 100" is topology recovered from images already selected as
  malformed, NOT a 97% correct-hand rate — do not use it as one.
- Hold step 3's two causes apart: (a) hands are scarce/underrepresented in
  training data (the model builder's account) and (b) hands are few-pixel and
  high-articulation, so the learned distribution over hand pixels is diffuse
  (FoundHand / HanDiffuser). Present both, distinctly, not blurred into one.
- Do not frame the failure as a permanent or hard limit. It recedes with scale,
  better data, and pose/mesh guidance (2023-2025 fixes). Mark settled-vs-open
  honestly.
- Attribute the "16 joints, 27 degrees of freedom" hand figure to its owner
  (ElKoura & Singh 2003), not to a paper that merely repeats it.
- Build on, don't re-teach: link the-mechanics/image-generation for the diffusion
  denoising mechanism; take it as given here.

nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
series `the-mechanics`, slug `hands-in-generated-images`. Dek must match the
rendered dekline exactly. Only the two bookends address the reader; no Verdict
block at the body's close.
