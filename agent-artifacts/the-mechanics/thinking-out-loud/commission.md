# Commission: the-mechanics/thinking-out-loud

## Assignment
Start from a behavior everyone has seen: ask a model a hard question and it
often gets it wrong, but tell it to "think step by step" (or watch a reasoning
model print a long "thinking" trace) and the answer improves. Work backward to
the cause. A transformer does a fixed, bounded amount of computation per token
it emits. A hard problem needs more computation than one token's worth, and the
only way the model can spend more is to generate more tokens and read its own
intermediate work back in. Writing the steps IS the extra computation. Keep
going down to ground, and mark clearly what is settled and what is open,
including the load-bearing open question: whether the written steps are the
computation that produced the answer, or a story told alongside it.

## Why this behavior, now
Reasoning models that "think" before answering are the current frontier, and
the plausible-but-wrong folk explanation ("it reasons like a person when told
to") hides a mechanical fact: generation is where a transformer's compute
lives, so more tokens can mean more compute. Understanding this lets the reader
judge when a printed "chain of thought" is trustworthy and when it is theater.

## Angle boundaries
- The subject is the **mechanism behind the behavior**: why emitting
  intermediate tokens changes what the model can compute. Trace behavior ->
  fixed compute per token / bounded depth -> serial computation across
  generated tokens -> conditioning on its own output.
- Distinct from neighbors: the-mechanics/autoregressive-generation owns "a
  generated token becomes input and is never revised"; prefill-and-decode owns
  the per-token cost of decoding; in-context-learning owns learning from
  examples in the prompt. Reference them; this lesson owns why MORE generated
  tokens buy MORE computation on a single hard problem.
- The-evidence/chain-of-thought is the DOCUMENT (Wei 2022: the finding, the
  ~100B-parameter threshold, and that it left open whether steps are faithful).
  Link it; do not re-report the paper. This lesson explains the mechanism the
  paper observed.
- Mark settled vs open honestly. Settled: a transformer's computation per token
  is bounded, so serial reasoning requires generating tokens (there is
  theory-of-computation work supporting this — cite it). Open: faithfulness —
  whether the verbalized steps caused the answer (cite the unfaithfulness
  evidence). Do not resolve the open question.
- No code (series rule). A worked example (a multi-step arithmetic or logic
  problem the model gets right only when it writes the steps) is fine as prose.

## Required contribution
The reader should be able to explain why a fluent model does better when it
writes its reasoning, name the exact mechanical reason (bounded compute per
token; extra tokens buy extra serial computation and re-readable notes), and
recognize the open question of whether a printed chain of thought reflects the
real computation.

## This edition (neighbors — keep distinct)
- the-evidence/resnet — a landmark paper as a document
- the-instruments/hallucination-rate — how a reliability number is manufactured
- what-could-go-wrong/sharp-left-turn — a capability jump outrunning safety
- when-ai-breaks/apple-card — algorithmic credit-limit bias

## Template & policy
- Template: lesson.
- Source policy: min 8 sources; >=4 primary, >=1 secondary. Primary: the
  chain-of-thought and reasoning-model papers, the theory papers on
  transformer expressivity / CoT compute (e.g. Feng et al. 2023; Merrill &
  Sabharwal 2023), the faithfulness studies (e.g. Turpin et al. 2023;
  Lanham/Anthropic 2023). Secondary: explainers that held up.
- Production policy (balanced): coach low, researcher high, writer medium,
  editor high; model "capable"; none required.
- Actual harness/model: `claude-code-routine`, `claude-opus-4-8` for all roles.
  Record in nb-meta (date 2026-08-07).

## Habits not to inherit (for the writer brief)
Recent the-mechanics pieces open on a one-sentence "a chatbot does X surprising
thing" dek and run a five-beat body. Do not inherit that dek mold or the fixed
beat count. Name this lesson's own steps from the backward trace. Check the
recent library's deks and headings first.
