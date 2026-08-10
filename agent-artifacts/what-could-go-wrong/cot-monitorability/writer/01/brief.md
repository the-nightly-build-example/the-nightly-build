# writer brief: what-could-go-wrong/cot-monitorability (01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the what-could-go-wrong prompt, template identity.
- writing-coach/01/voice-guide.md — how this lesson should sound, with exemplar passages.
- researcher/01/evidence.md — the complete claim set: what is shown versus projected, contradictions, source kinds.
- The initialized article at library/what-could-go-wrong/cot-monitorability.html and its .nb-context/ contract.

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/what-could-go-wrong/cot-monitorability/library/what-could-go-wrong/cot-monitorability.html --library /home/user/library-checkout
(run from /home/user/the-nightly-build; use --no-check-links while iterating, links included until BLOCK: 0)

Set nb-meta the engine cannot compute: date 2026-08-10, harness claude-code-routine, model
"Claude Opus 4.8", and tags ["chain-of-thought", "oversight", "interpretability"]. nb stamp writes the counts.

Distinctions the evidence flags that the draft must keep exact:
- Keep Baker's two experiments separate. The 95 percent versus 60 percent monitoring result was on
  a frontier model; the obfuscation-under-pressure result was a separate agent trained with a reward
  that directly penalized tripping the monitor, and not the same frontier model. Do not merge them.
- Every failure shown in a real model was experimenter-induced (a penalty on the chain-of-thought,
  or an injected cue in the faithfulness studies). The three risks the piece turns on (heavy
  outcome-based RL erasing legibility, latent/"neuralese" architectures, unprompted deployment-time
  obfuscation) are stated by the position paper as future possibilities and demonstrated by no
  primary. That shown-versus-projected line is the spine.
- Do not write "RL degrades the chain-of-thought" as a general finding. Chen finds outcome-based RL
  not aimed at the chain-of-thought can raise faithfulness before plateauing, a counter-signal.
- Attribution care: Hinton and Sutskever are endorsers of the position paper, not among its authors.
  Check every named person's affiliation against the paper header before naming them with an org.
- Independence limitation the piece should acknowledge: much of this evidence is one safety community
  measuring its own tool, so agreement across these papers is closer to one confirmation than several.

Recent habits to break (from what-could-go-wrong and the house record; the voice guide does not carry these):
- Do not reuse the dek/finding reversal mold "scores above chance... yet no one has caught..."
  (situational-awareness) or "never run in the same experiment" (data-poisoning). State this
  argument's honest finding in its own terms.
- Do not open the takeaway on "Two things are true at once," and do not use the opener move "What you
  can carry away is one question to put to any 'X' claim" (situational-awareness).
- Do not end the opener with an enumerated roadmap. State stakes without touring the sections.
