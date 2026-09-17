# writer brief: the-instruments/winogrande (01)

Inputs:
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/writing-coach/01/voice-guide.md` — how this piece should sound; read before drafting
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/researcher/01/evidence.md` — the complete claim set; use the Numbers section exactly
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/commission.md` — assignment, boundaries, habits to break
- Article to edit in place: `.nb-work/the-instruments/winogrande/library/the-instruments/winogrande.html`
- Template context: `.nb-work/the-instruments/winogrande/.nb-context/`

Output: `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/writer/01/draft-handoff.md`

Proof (run with links, until BLOCK: 0):
`./nb check .nb-work/the-instruments/winogrande/library/the-instruments/winogrande.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's exactness (the evidence forces these):
- Attribute the original WSC's size correctly: the 2012 paper describes "more than
  100" schemas; the familiar "273" is the later standardized WSC273 test set. Do
  not pin 273 on the 2012 paper.
- Use the firsthand figures from the Numbers section: 43,972 all / 12,282 debiased
  problems, 94.0% human, RoBERTa 79.1% as best-at-publication. For a near-human
  machine score use UNICORN's own-paper 86.6%; do not present the 91.2%
  leaderboard entry as verified (the AI2 leaderboard is offline and it could not
  be confirmed). The learning curve on the same filtered items (about 50.4% at
  160 examples to 79.1% at ~41K) is the spine: it shows the difficulty is a
  property of the construction and the training budget, not a fixed law.
- Steelman the counter-critique fairly: two original WSC authors ("The Defeat of
  the Winograd Schema Challenge") argue AFLite did not fully strip surface cues,
  and AFLite's authors concede it defines "hard" relative to one model's
  embeddings. This complicates any claim that WinoGrande is a clean reasoning-only
  meter, and it strengthens the core lesson that the number is engineered.
- The misled case, costed: WinoGrande exists because near-human WSC scores were
  hollow (the sole formal WSC competition, IJCAI-16, topped out at 58%), and the
  same pattern recurred on WinoGrande within about a year, even as model cards
  (GPT-3, Llama 2, which flag contamination in their own reports) still publish
  WinoGrande numbers. Treat the paper's "over 118K instances for human-level"
  extrapolation as the paper's claim, not endorsed arithmetic.
- Link, do not re-teach: the-evidence/bert (the shortcut-collapse case),
  the-instruments/glue and superglue (benchmark suites; WSC sits in SuperGLUE).
- Recent habits to break: do not close with clipscore's "What happens when the
  grade becomes the goal" move; avoid the compression-definition heading mold and
  the "checked on X, trusted on Y" phrasing.
- Set nb-meta `harness` to `claude-code`, `model` to the model you run as, date
  2026-09-17. Keep nb-meta `dek` identical to the rendered dekline.
