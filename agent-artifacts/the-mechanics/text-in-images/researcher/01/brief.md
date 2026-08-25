# researcher brief: the-mechanics/text-in-images (01)

Inputs:
- commission.md (at the artifact root): the causal chain to pin down, the
  boundaries, and the source floor.
- editorial-direction.md (at the artifact root): citation standard,
  primary/secondary test, reader, the-mechanics series territory.

Output: agent-artifacts/the-mechanics/text-in-images/researcher/01/evidence.md

This round's focus:
- Establish, from primary sources, that the text encoder choice governs text
  rendering: what encoder Stable Diffusion / latent diffusion used (CLIP text
  encoder) versus what Imagen used (a large T5 encoder) and what each reported
  about rendering legible text. Record exact claims and where they appear.
- Get the "Character-Aware Models Improve Visual Text Rendering" result: what
  it changed (character-aware vs character-blind text encoder), and the
  measured improvement in rendering, with figures and their scope.
- Establish the tokenization/character-blindness link cleanly enough to state
  plainly why the spelling is gone before any pixel is drawn. Connect to the
  already-taught letter-counting mechanism without re-deriving it.
- Get a concrete current-system account (DALL·E 3 system card, DeepFloyd IF
  notes, or a 2024-2025 model's own documentation) of how text rendering
  improved and where it still fails (long strings, rare words). Record what is
  settled versus still open.
- Provide 2-3 small concrete examples a reader can picture (a specific short
  word that renders now vs a longer phrase that garbles), sourced or clearly
  marked as illustrative.
- Hunt for what breaks the angle: evidence that the failure is NOT mainly the
  text encoder (e.g. a character-blind encoder that still renders text well,
  or a claim the bottleneck is the diffusion decoder). Record in Contradictions.
