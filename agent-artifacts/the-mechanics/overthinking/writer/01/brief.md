# writer brief: the-mechanics/overthinking (01)

Inputs:
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/editorial-direction.md
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/commission.md
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/writing-coach/01/voice-guide.md
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/researcher/01/evidence.md
- Article to edit: .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html
- Template context dir: .nb-work/the-mechanics/overthinking/.nb-context/

Output:
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/writer/01/draft-handoff.md

Proof:
- ./nb stamp .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html
- ./nb check .nb-work/the-mechanics/overthinking/library/the-mechanics/overthinking.html --series the-mechanics --library /home/user/library-checkout
  (iterate --no-check-links; final proof with links, to BLOCK: 0)

nb-meta: harness="Claude Code", model="claude-opus-4-8". Tags e.g. reasoning-models, test-time-compute, overthinking, inverse-scaling, reinforcement-learning.

This round's focus: work backward from the behavior to its cause step by step, marking settled vs open.

CRITICAL accuracy from the evidence record (do not conflate two different phenomena):
- Trivial-input overthinking is an EFFICIENCY cost, not a wrong-answer cost. On genuinely simple inputs the first solution round is correct over 92% of the time and extra reasoning barely moves accuracy. Do NOT imply a model gets a trivial question wrong by overthinking. The everyday "spends ages on 2+2" behavior is wasted compute/latency.
- The accuracy COLLAPSES appear only on tasks Anthropic CONSTRUCTED to carry distractors, spurious features, or long constraint chains (Claude Opus 4 ~100%→85-90%; DeepSeek R1 ~70%→30%), and the same paper reports accuracy is MAINTAINED under extended reasoning on standard benchmarks (GSM8K, ASDiv, MultiArith, GSM-IC). State "more reasoning can hurt" as real but CONDITIONAL, with the conditions.
- A second, inverted failure on hard problems: underthinking (models abandon a correct line; ~418% more thought-switching on wrong AIME answers). So "more tokens hurts" has more than one mechanism.
- Cause attribution: RL length reward is well supported for the WASTED-COMPUTE behavior, but the inverse-scaling paper attributes the accuracy DROPS to extended reasoning amplifying flawed heuristics, not to the length reward. Keep those causes distinct. The best framing of overthinking (RL length bias vs missing difficulty estimate vs budget policy) is still open — mark it so.

Settled half to teach firmly: test-time compute scales with generated tokens; RL trained/selected for long chains. Link the-mechanics/thinking-out-loud (in the library) for why steps buy computation; do not re-teach it. Do not drift into the safety/monitoring angle.

Habits not to inherit (from commission): vary heading construction; avoid the "Nothing turns X into Y" negative-closer and "the model renders the most likely X" rhythm; avoid comma-triad and negative-parallelism deks.
