# writer brief: the-evidence/lottery-ticket-hypothesis (01)

Inputs (all paths under this article's artifact root unless absolute):

- `editorial-direction.md` — house standard, slop, headline standard, press voice,
  lesson identity, series prompt. Binds every sentence.
- `commission.md` — the document, angle, neighbors, required contribution.
- `writing-coach/01/voice-guide.md` — how this piece should sound; read before
  drafting; reuse the subject's terms, never the exemplars' phrasings.
- `researcher/01/evidence.md` — the complete set of claims available to you.
- Article to edit in place:
  `/home/user/the-nightly-build/.nb-work/the-evidence/lottery-ticket-hypothesis/library/the-evidence/lottery-ticket-hypothesis.html`
- Template context: `/home/user/the-nightly-build/.nb-work/the-evidence/lottery-ticket-hypothesis/.nb-context/`

Output: `writer/01/draft-handoff.md`.

Proof: `./nb check /home/user/the-nightly-build/.nb-work/the-evidence/lottery-ticket-hypothesis/library/the-evidence/lottery-ticket-hypothesis.html --series the-evidence --library /home/user/library-checkout`
(run from `/home/user/the-nightly-build`).

This round's focus:

- Keep the sparsity frame straight, a hazard the evidence flags: the 2019 paper's
  "P_m" is the percentage of weights *remaining*, while later papers report
  "sparsity" as the percentage *pruned*. The same network reads as 10% or 90%
  depending on frame. State which frame each figure uses and do not blur them.
- Hold the line the evidence draws: the narrow existence result (a small trainable
  subnetwork exists, found by pruning after training, on small vision nets) held
  and extended; the special-weights and cheap-up-front-ticket readings did not.
  Carry both accurately. The reset-to-original-initialization step and the random-
  reinit failure are the paper's real surprise; teach them concretely. Include the
  2019 Section 4 scaling failure, Frankle 2020's rewinding fix, and the Liu/Zhou
  critiques as the evidence records them.
- Verified figures come from the evidence record; where it marks a number as "the
  paper's reported reading," attribute it that way rather than as an independent
  recomputation.

Habits not to inherit (from the commission and the recent shelf):

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula. Do not order the body orientation -> a section
  named for a scale/parameter figure -> findings by reflex. Do not land the
  takeaway on negative parallelism ("It is a real X. It is not yet a Y"). Deks:
  avoid the banned molds in the headline standard.

Set nb-meta `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`.
Make the display-text pass before proving, and prove to `BLOCK: 0` with links
included.
