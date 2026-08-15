# writer brief: the-evidence/knowledge-distillation (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/agent-artifacts/the-evidence/knowledge-distillation/editorial-direction.md — house standard, slop standard, headline standard, this paper's voice, the lesson template identity, and the series prompt.
- /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/agent-artifacts/the-evidence/knowledge-distillation/writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages to read for register before drafting.
- /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/agent-artifacts/the-evidence/knowledge-distillation/researcher/01/evidence.md — the complete set of claims available to you. Its Contradictions and Numbers sections govern.
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/library/the-evidence/knowledge-distillation.html
- Effective template contract and furniture catalogs under: /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/agent-artifacts/the-evidence/knowledge-distillation/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-evidence/knowledge-distillation/library/the-evidence/knowledge-distillation.html --series the-evidence --library /home/user/library-checkout
       (iterate with --no-check-links; run `./nb stamp <article>` before the final check; the final proof must pass with links included, BLOCK: 0)

Framing guardrails from the evidence record (follow the evidence, not the commission where they differ):
- Do not attribute the phrase "dark knowledge" to the paper. It is not in the text.
  Teach the idea in the paper's own words: "soft targets," and that the relative
  probabilities the model assigns to the wrong answers carry information about how
  it generalizes (the BMW / garbage-truck / carrot example is the paper's own).
- Do not present the JFT specialists experiment as a completed distillation. The
  paper states it had not yet distilled the specialists back into one network. JFT
  shows the 61-specialist ensemble raising accuracy (25.0% to 26.1%) and specialists
  training in days rather than about six months. The two experiments that
  demonstrate distillation end to end are MNIST (146 to 74 errors, and the digit the
  student recognized without ever seeing a labeled example of it) and speech (a
  single net recovering most of a ten-model ensemble's gain). Present JFT as the
  ensemble/specialists result, not as proof the small net learned from the big one.
- Keep the drift claim to the sourced, narrower version. The honest gap is not
  "people misuse the word." It is that distillation became a family of methods, of
  which the paper's soft-target matching is the original member, and the broadening
  began in peer-reviewed work within a year (Kim & Rush 2016, a hard-target method
  still called knowledge distillation). Draw the present-day gap between two real
  cases: DistilBERT keeps the mechanism (temperature-softened soft targets), while
  DeepSeek-R1 keeps only the name (plain supervised fine-tuning on generated
  samples, no soft targets, no temperature). Do not overreach into blanket misuse.

Recent habits to break (from the commission's read of the library):
- The house "Why this matters" bookend has hardened into a catchphrase promising
  what the reader "will be able to" do "by the end." Do not use it. Give a real,
  particular reason to read.
- The most recent the-evidence piece closed on a matched split ("the existence
  result held; the special-weights reading did not"). This paper's corrected framing
  (soft-target method is real and original; the name later broadened) invites the
  same move. Do not reuse that semicolon-split sentence or a heading built like it;
  make the point in this paper's own particulars.
- Vary the headline from the recent comma-continuation and "X, not Y" molds. State
  the finding about this paper directly.
