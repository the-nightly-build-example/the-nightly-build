# writer brief: the-mechanics/false-confidence (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/editorial-direction.md — house standard, press voice, series prompt, template identity
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/commission.md — assignment, the behavior-to-cause chain, boundaries, and recent shapes/phrasing to break
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/writing-coach/01/voice-guide.md — how this piece should sound, with exemplars
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/researcher/01/evidence.md — the complete claim set
- Article to edit in place: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/library/the-mechanics/false-confidence.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/library/the-mechanics/false-confidence.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/97d053c3-1b59-5f4b-8b78-5c56b444e4a1/scratchpad/library-checkout

This round's focus — the evidence record narrows two claims the commission stated
too absolutely. Write the narrower, defensible version:
- Do NOT write that stated confidence carries "zero" information about
  correctness. The defensible claim is narrower: the default assertive *tone*,
  and an unsolicited "I'm 95% sure," is uninformative (Xiong et al.), while a
  numeric confidence the user explicitly asks for can be better calibrated than
  the model's own token probabilities (Tian et al., roughly a 50% relative ECE
  reduction, though uneven across datasets — large on TruthfulQA, negligible on
  TriviaQA). The behavior the lesson explains is the confident *tone* of a fixed
  answer, not a claim that a model can never surface useful uncertainty.
- Do NOT write that the softmax is the "only" internal quantity resembling
  confidence. What is true: there is no verified truth-checking module, and the
  printed confidence words are not read off the logits. But additional internal
  uncertainty signals exist that a model can be trained to surface (Kadavath's
  P(True)/P(IK); Lin's latent representations). Say that honestly.
- The GPT-4 technical report gives NO numeric ECE for its Figure 8 — only two
  reliability diagrams and the words "highly calibrated" (base) and calibration
  "reduced" (post-RLHF). Do not invent a base-vs-RLHF ECE number. For the worked
  calibration example, use the Figure 8 result qualitatively, Guo et al.'s
  definition/figures for what calibration means, and Tian's abstract-owned ECE
  figures where a number is needed — never a fabricated GPT-4 number.
- Mark the open question honestly: *why* RLHF degrades calibration is observed,
  not explained; the "RL concentrates probability mass" line is a hypothesis, not
  a demonstrated cause.

Everything else per your skill. Fill nb-meta: date 2026-08-23, harness
`claude-code-routine`, model `claude-opus-4-8`, tags per the commission. Write the
one-sentence original-work statement in draft-handoff.md. Iterate with
--no-check-links, then run full `nb stamp` + `nb check` until `BLOCK: 0`, and do
the display-text self-test before handing off.
