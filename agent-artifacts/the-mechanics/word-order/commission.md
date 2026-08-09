# Commission: the-mechanics/word-order

## Authorized work

Scheduled run for 2026-08-09. `nb duty` returned `the-mechanics` in open mode,
reason: "open section — choose a topic within the beat; do not repeat a
published slug." One article.

## The behavior

"How does the model know which word came first?" A reader who uses AI has seen
the effect without naming it: the model treats *the dog bit the man* and *the
man bit the dog* as different sentences, and can answer "what is the fourth
word here?" Yet the operation at the center of a transformer — self-attention —
is order-blind: on its own it treats the input as a bag of tokens, so shuffling
them would leave each token's representation unchanged. The lesson works
backward from the behavior (order carries meaning and the model respects it) to
the part that has to supply order, because attention will not.

This is bedrock the course keeps needing. Later lessons on long context, on why
a model degrades past its trained length, and on retrieval all lean on how
position is represented, and it has never been taught directly.

## What the lesson teaches (two or three ideas)

1. **Self-attention is order-blind.** State it plainly and show it with a small
   worked example: run the same set of word-vectors through attention in two
   different orders and, with no position information, the set of outputs is the
   same (permutation-equivariance). So a transformer that did nothing else could
   not tell *dog bit man* from *man bit dog*. This is the gap the rest of the
   lesson fills. (Algebra is assumed; do not introduce it — but no code, per the
   desk. Keep the demonstration concrete and in words/small numbers.)

2. **Position is added, not computed.** The original transformer hands the model
   order by adding a position signal to each word's vector before attention ever
   runs: fixed sinusoidal patterns in the 2017 paper, or a learned position
   vector per slot in models like GPT-2/BERT. Show what "added to the vector"
   means concretely, and that this is settled engineering.

3. **How today's models do it, and where the ground gets soft.** Modern models
   moved to relative and rotary schemes — RoPE rotates each word's query and key
   by an angle set by its position, so attention ends up depending on the
   *distance* between two words; ALiBi biases attention by that distance
   directly. Mark clearly what is settled (these mechanisms, and that they work)
   and what is open even to builders: length extrapolation — models trained to a
   length routinely fail past it, and whether a position scheme generalizes
   beyond its trained range is unsettled. Note the genuinely surprising result
   that a decoder-only model can learn position with no explicit encoding at all,
   riding the causal mask (mark this as partly open).

The reader should finish able to explain why the model respects word order at
all, and to catch an explanation that skips the step where order gets supplied.

## Boundaries

- `the-mechanics/word-embeddings` already teaches how a word's vector is formed
  and redrawn per sentence. Position is added *on top of* that vector; link, do
  not re-teach embeddings.
- `the-mechanics/autoregressive-generation` teaches the causal mask; the NoPE
  result leans on it, so link there rather than re-teaching the mask.
- `the-instruments/context-window` and `the-mechanics/losing-the-thread` own the
  long-context-degradation story. Use length extrapolation only as this lesson's
  open-question ground, with a link, not a full treatment of long-context failure.
- No code (desk rule). Claims about each scheme come from the paper that owns it.

## Original contribution

Make the order-blindness of attention concrete and then trace exactly which real
mechanism repairs it, from sinusoidal to learned to rotary, drawing the line
between the settled engineering (position is supplied and how) and the open
question (whether it extrapolates past the trained length). The reader gets a
mechanism they can carry to the next long-context claim.

## Source policy (from `nb source-policy`)

Series and template agree: minimum 8 sources, primary ≥ 4, secondary ≥ 1.
Primaries: Vaswani et al. 2017 (sinusoidal); Su et al. (RoPE); Press et al.
(ALiBi); Shaw et al. 2018 (relative position); Kazemnejad et al. 2023 (NoPE);
a learned-absolute reference (BERT or GPT-2). Secondary is expository context.

## Production policy (from `nb production-policy`, profile: balanced)

- writing-coach: capable (Sonnet), low effort
- researcher: capable (Opus), high effort
- writer: capable (Opus), medium effort
- editor: capable (Opus), high effort

None `required`; no deviation to record.

## This edition's neighbors

- `the-mechanics` piece is the only mechanism lesson tonight. The other four
  (`the-evidence/gpt-3`, `the-instruments/mmlu`,
  `what-could-go-wrong/situational-awareness`, `when-ai-breaks/tesla-autopilot`)
  do not overlap. Keep this one purely mechanical: no benchmark scores, no risk
  framing, no incident.

## Recent habits not to inherit

- Recent mechanics openers open on "Every chatbot reply ends, and you have
  watched…" / "Every [behavior] you have seen…" and close on "By the end you can
  look at any … and say which…". Write the promise in this lesson's own terms and
  off that mold.
- The last two mechanics lessons (why-replies-stop, thinking-out-loud) both hinge
  on a clean two-way split (two ways a reply ends; a fixed network can only
  compute more by writing more). This lesson's shape is a descent from a behavior
  to the mechanism that supplies it, marking settled vs open at each step — not an
  A-vs-B split. Keep it a descent.
- Takeaway closers lean on "Now you know which one you are looking at." Resolve
  the opener without that turn.
- The "In plain language" note recurs; if a note earns its place, label it for
  the move it makes.

## Prior coverage to link, not re-teach

- `the-mechanics/word-embeddings` — what a word's vector is.
- `the-mechanics/autoregressive-generation` — the causal mask.
- `the-instruments/context-window`, `the-mechanics/losing-the-thread` —
  long-context degradation (the open-question tie).
