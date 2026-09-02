# researcher brief: the-mechanics/counting-objects-in-images (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — citation standard,
  series territory, declared reader
- commission.md (../../commission.md) — the behavior, angle, source floor

Output: evidence.md (this directory)

Build the evidence record for why text-to-image models miscount discrete objects.
Each link in the causal chain must be backed by a source that owns it:

- That CLIP-style text encoders encode presence far more reliably than exact
  quantity and behave close to bag-of-words on order/count (Yuksekgonul et al.
  2023 or equivalent; the CLIP paper for what the encoder is and does). Get a
  concrete measured example of the failure if the source provides one.
- That diffusion generates by denoising from noise steered by the text embedding
  through cross-attention (latent diffusion / Stable Diffusion primary), with no
  component that maintains or verifies a count.
- Official acknowledgement that leading systems fail at counting/compositional
  prompts (DALL-E 3 system card, Imagen/DrawBench, or a T2I compositional
  benchmark), with any reported numbers on how often counting fails.
- What, if anything, has been shown to improve counting (a counting-guidance or
  better-captioning result), so the writer can mark the open-question boundary
  honestly rather than overclaiming a fix.

Source floor: at least 8 sources, at least 4 primary, at least 1 secondary.
Classify each and say why. In Contradictions, record any evidence that counting is
substantially solved in current models (test the "still broken" angle). Note in
Numbers any measured counting-accuracy figures with scope. Flag clearly if the
mechanism claims cannot all be primary-sourced, so the orchestrator can adjust
before drafting.
