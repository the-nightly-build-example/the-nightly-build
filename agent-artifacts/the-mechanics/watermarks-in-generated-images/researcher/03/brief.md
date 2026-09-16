# researcher brief: the-mechanics/watermarks-in-generated-images (03)

Inputs:
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/researcher/02/evidence.md` — the prior record (already includes the Somepalli et al. eighth source); preserve all still-valid work
- `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/editorial-direction.md` — citation standard, series territory, declared reader

Output: `.nb-work/the-mechanics/watermarks-in-generated-images/agent-artifacts/the-mechanics/watermarks-in-generated-images/researcher/03/evidence.md`

Reason for this round: the editor found the draft's "never filtered / nothing
removing it / absence of any filter" claim about Stable Diffusion's training data
is not supported. LAION-5B's Appendix F.2 points to Stable Diffusion's own model
documentation for the recipe, and that documentation indicates some training
stages used data filtered by an estimated-watermark-probability threshold. Correct
the record so the writer can fix the causal claim.

Confirm to the citation standard, from Stable Diffusion's official model
documentation (the model card the LAION-5B Appendix F.2 recipe points to — e.g.
the CompVis/Stability Stable Diffusion v1 model card and its stated training
datasets), the following, each with its exact scope and an owning primary source:
- which training stages/subsets used watermark-filtered data and which did not
  (for example, the laion2B-en base pretraining vs. the laion-aesthetics /
  improved-aesthetics fine-tuning stages), and the step counts if stated;
- the exact watermark filter applied (the estimated-watermark-probability
  threshold, e.g. below 0.5) and that it is a probability estimate, not a
  guarantee;
- how this squares with the ghost watermark still appearing: a threshold near 0.5
  on an estimated probability, applied to only some stages, reduces watermarked
  content without removing it.

Add the model documentation as a source (classify primary/secondary with reason).
Write a complete new evidence.md preserving researcher/02's still-valid entries and
clearly recording this correction under Sources, Numbers, and Contradictions as
appropriate. Do not overwrite researcher/01 or researcher/02. If the documentation
does not in fact support a filtering correction, say so plainly.
