# writer brief: the-evidence/t5-transfer-learning (01)

Inputs:
- `editorial-direction.md` — house standard, this paper's voice, the series direction
- `writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting
- `researcher/01/evidence.md` — the complete set of claims available to you
- the initialized article at
  `.nb-work/the-evidence/t5-transfer-learning/library/the-evidence/t5-transfer-learning.html`
- the effective template context under
  `.nb-work/the-evidence/t5-transfer-learning/.nb-context/`

Output: `writer/01/draft-handoff.md`

Proof (run from `/home/user/the-nightly-build`; iterate with `--no-check-links`,
then a final run with links until `BLOCK: 0`):

```text
./nb stamp .nb-work/the-evidence/t5-transfer-learning/library/the-evidence/t5-transfer-learning.html
./nb check .nb-work/the-evidence/t5-transfer-learning/library/the-evidence/t5-transfer-learning.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/7638a680-eec9-5b00-bc28-2a2eeb252ef4/scratchpad/library-checkout
```

nb-meta to fill: date `2026-09-07`, harness `Claude Code`, model `claude-opus-4-8`,
and subject tags of your choosing. Keep nb-meta `dek` identical to the rendered
dekline.

This round's focus: teach what T5 is, the text-to-text framing with a worked
example the reader can follow, the C4 dataset and the study's scale, then the
honest present-day reckoning. Respect the record's constraints:

- The paper reports no single absolute pretraining-compute figure. Give the scale
  in tokens and the token comparisons the record verified (roughly a trillion
  tokens for the final model, against the baselines the record names), not in
  petaflop-days the paper never states.
- Attribute each figure to the source that owns it. The paper says C4 is about
  750 GB; the released dataset ships larger (about 807 GiB). If you cite both,
  distinguish them. The same care applies to t5.1.0 (paper) versus t5.1.1
  (released) checkpoints.
- The "cited for more than it showed" thread is well supported: T5 reached the
  best result of its time on 18 of 24 tasks but lost on all three WMT translation
  tasks; its scores are 2019-era records since surpassed; its finding that the
  encoder-decoder form worked best sits in real tension with the field's later
  move to decoder-only models; and instruction tuning came later (Flan-T5), which
  the original paper did not study. Say these plainly.

Recent shapes to break (checked against the last eight lessons in this series):

- Do not open the dek with "<Authors>'s <year> paper <did X>, then/and <measured
  Y>" (dropout, constitutional-ai, denoising-diffusion, adversarial-examples). Do
  not reach for the "the company's own report can't/does X" headline
  (llama-3-herd-of-models), or the phrasings "measured it directly" / "in its own
  experiments." Find the surprise T5 actually holds and lead with it.

Link rather than re-teach: the-mechanics/attention, the-evidence/bert,
the-evidence/gpt-3-few-shot, the-evidence/scaling-laws-kaplan. Background links use
a relative `../<series>/<slug>.html` href; Go deeper links point beyond the paper.
