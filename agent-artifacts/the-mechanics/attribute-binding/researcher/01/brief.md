# researcher brief: the-mechanics/attribute-binding (01)

Inputs:
- editorial-direction.md (artifact root) — citation standard, series territory, declared reader.
- commission.md (artifact root) — the behavior, the angle, what to teach, the source floor.

Output: researcher/01/evidence.md

Research questions, answered from the primary source that owns each claim:

1. That attribute and relation binding fails systematically in text-to-image
   models, with a measured rate on a real prompt set. Pin to a compositional
   benchmark primary (e.g., Huang et al., T2I-CompBench, 2023) and/or relational
   studies (e.g., Conwell & Ullman, "Testing Relational Understanding in
   Text-Guided Image Generation," 2022). Get concrete numbers: accuracy on
   attribute-binding vs single-object prompts, and on spatial relations.
2. How a modern text-to-image pipeline maps text to image at the needed level:
   the text encoder produces token embeddings; the generator (latent diffusion)
   denoises while attending to those embeddings via cross-attention. Pin the
   pipeline to a primary (Rombach et al., latent diffusion / Stable Diffusion,
   2022) and the CLIP-style text encoder to its primary (Radford et al., CLIP,
   2021).
3. Evidence localizing the cause: findings that the text encoder's representations
   entangle neighboring words, and that cross-attention maps misassign attributes.
   Method papers that fix binding by intervening on exactly these parts are
   evidence for where the fault lives: Chefer et al., Attend-and-Excite (2023),
   which manipulates cross-attention; Feng et al., StructureDiffusion (2022),
   which restructures the text encoding. Record what each shows and its measured
   improvement.
4. The settled/open line: what reproduces across systems (settled), and what is
   still disputed (the exact split of blame between encoder and cross-attention,
   whether fixes generalize). Record contradictory findings in full.

For a source asset: identify one exact figure from a cited primary that shows a
prompt and its wrong image (or a before/after from a fix paper), with what a crop
must retain. If none is usable, write None found. Classify each source
primary/secondary with the reason; meet the floor in commission.md. Reproducible
model outputs count as primary observations if you generate or a paper reports
them; record exactly what was prompted and produced.
