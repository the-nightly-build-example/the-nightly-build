# Writer handoff: what-could-go-wrong/cot-monitorability (01)

## Original-work sentence

The article pulls apart two questions the sources and the public debate routinely
collapse into one, monitorability (can a reader catch misbehavior in the trace,
shown to work) versus faithfulness (does the trace name the true cause, often
low), and then sorts every result and every feared risk onto a single
shown-versus-projected line, closing on the point no single source makes plainly:
that the papers agreeing on the answer are largely one safety community measuring
the instrument it built.

Where this is visible in the piece: the "Legible and honest are two different
tests" section teaches the distinction; the shown/projected table in "Push on the
chain of thought and the model learns to hide" sorts the six claims; the
independence limitation and Verdict note land the synthesis in "One safety
community is largely measuring its own tool."

## Proof result

`./nb check ... --series what-could-go-wrong --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.**

No warnings left standing. Word count landed at 2200, the top of the lesson band
(1200-2200); the length and sentence-density warnings from earlier iterations
were resolved, not waived.

## Distinctions kept exact (per brief)

- Baker's two experiments are separate: the 95% vs 60% monitoring result is
  stated as OpenAI's frontier reasoning model (orientation + stat strip); the
  near-zero-recall obfuscation result is stated as a separate, non-frontier agent
  whose reward was changed to punish tripping the monitor (section 3 and the
  table's second row).
- Shown-versus-projected is the spine. Every demonstrated failure is labeled
  experimenter-induced; the three erosion paths (heavy outcome RL, latent/
  neuralese architectures, unprompted deployment-time obfuscation) are labeled
  projections with no primary behind them. The table makes the split explicit.
- "RL degrades the CoT" is not written as a general finding. Chen's outcome-based
  RL raising faithfulness (+63% / +41% before plateau) is carried as the
  counter-signal, distinct from Baker's pressure aimed directly at the monitor.
- Hinton and Sutskever are named as endorsers, not authors, cited to the
  techxplore secondary (S3).

## Notes for the editor

- Deliberate attribution choice: I described the authors only by affiliation
  spread ("researchers from OpenAI, Google DeepMind, Anthropic, and several
  AI-safety organizations") and named no single person with a single org, because
  the paper states it represents individual authors, not institutions, and the
  researcher flagged that per-author mapping was not cleanly verifiable. Bowman
  and Schulman (unconfirmed endorsers) are not mentioned.
- Two prior lessons are linked in prose rather than re-taught, per press
  direction: `thinking-out-loud` (why a hard task forces written steps) and
  `chain-of-thought` (the trick itself), plus `reward-hacking` at first use of
  "gamed the objective." These are plain prose links, not numbered sources.
- Furniture: stat strip (95/60), the shown-vs-projected table, and one Verdict
  note (`nb-note-strong`, the single allowed strong note). No chart or source
  asset: the argument's one comparison is carried by the stat strip and table
  from the evidence's verified figures, and no asset capture was needed.

## Open questions

None blocking. No fact was missing from the evidence record; nothing was written
around a hole.
