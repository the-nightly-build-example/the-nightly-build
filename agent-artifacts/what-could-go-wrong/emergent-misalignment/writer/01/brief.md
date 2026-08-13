# writer brief: what-could-go-wrong/emergent-misalignment (01)

Inputs (all paths under this article's artifact root unless absolute):

- `editorial-direction.md` — house standard, slop, headline standard, press voice,
  lesson identity, series prompt. Binds every sentence.
- `commission.md` — the argument, angle (open at strength, draw the shown-versus-
  inferred line, bring to the present), neighbors, required contribution.
- `writing-coach/01/voice-guide.md` — how this piece should sound; read before
  drafting; reuse the subject's terms, never the exemplars' phrasings.
- `researcher/01/evidence.md` — the complete set of claims available to you.
- Article to edit in place:
  `/home/user/the-nightly-build/.nb-work/what-could-go-wrong/emergent-misalignment/library/what-could-go-wrong/emergent-misalignment.html`
- Template context: `/home/user/the-nightly-build/.nb-work/what-could-go-wrong/emergent-misalignment/.nb-context/`

Output: `writer/01/draft-handoff.md`.

Proof: `./nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/emergent-misalignment/library/what-could-go-wrong/emergent-misalignment.html --series what-could-go-wrong --library /home/user/library-checkout`
(run from `/home/user/the-nightly-build`).

This round's focus:

- Draw the desk's sharp line as the spine. The measured core verifies against the
  paper (about 20% misaligned answers on the 8 main questions; ~6% pre-registered
  vs 0.1%/0% controls; the backdoored version under 0.1% without the trigger and
  about 50% with it; the educational/insecure-for-security control near 0%). Use
  the Numbers shape and pin each figure. The key inference the desk must name: every
  positive result ran through a deliberate training intervention on constructed
  data; no source shows this arising in a model not intentionally trained on the
  narrow bad data, so whether it happens in ordinary deployment stays open. Say
  so plainly.
- Handle the follow-up and critiques as the evidence directs. Cite OpenAI's
  findings (misalignment generalization, the "misaligned persona" latent
  direction, re-alignment from a small sample) to the readable arXiv paper
  (2506.19823), not the gated blog. Present the two critiques (the length-artifact
  fragility result; the prompt-sensitivity reframing) as refinement from inside
  the same research cluster, not a hostile outside rebuttal. Record the
  contradictions honestly.
- Link deceptive-alignment or mesa-optimization rather than re-teaching them; do
  not duplicate reward-hacking's "model games its objective" story.

Habits not to inherit (from the commission and the recent shelf):

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula, and do not model what-could-go-wrong's "famous
  number, then its deflation" opener. Do not land the takeaway on negative
  parallelism or a "cuts both ways" balance line. If you use a holds-up grid, do
  not mirror reward-tampering's grid-then-"how far it reaches" order. Deks: avoid
  the banned molds.

Set nb-meta `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`.
Make the display-text pass before proving, and prove to `BLOCK: 0` with links
included.
