# Commission: the-mechanics/why-replies-stop

## Authorization
Scheduled run for 2026-08-08 (Sat). `nb duty` returned the-mechanics as an open
section: choose a topic within the beat, do not repeat a published slug. Verified
against the FULL published shelf (22 slugs); `why-replies-stop` is not among them
and no existing article owns the stopping mechanic (autoregressive-generation,
prefill-and-decode, and sampling-temperature are neighbors, not this). One article
only. Template `lesson`.

## Subject
The behavior everyone has seen: a chatbot's reply ends on its own at a natural
place - and sometimes stops dead in the middle of a word or a code block. Work
backward from "why did it stop there" to the cause.

## Angle (the desk's shape: from the behavior to ground, marking settled engineering vs open questions)
- The behavior: two kinds of ending - a clean finish, and a mid-sentence cutoff.
- Step 1 - the model chooses when to stop the same way it chooses every word. The
  vocabulary includes a special end-of-sequence / end-of-turn token (e.g. the chat
  template's end-of-turn marker). At each position the model puts probability on
  that token like any other; when it samples it, generation halts. So "stopping" is
  just next-token prediction selecting the stop token. (This course teaches
  next-token generation elsewhere; link autoregressive-generation, do not re-teach.)
  Worked example: a short completion where the stop token's probability rises as the
  answer completes.
- Step 2 - where the stop token comes from: it is not grammar the model deduced;
  post-training (instruction/chat tuning on examples that end turns) taught the model
  to emit the end-of-turn token at sensible places. Mark this as settled engineering
  and name the honest wrinkle: base (pre-trained) models often do NOT stop well and
  ramble, which is why the same architecture behaves differently after chat tuning.
- Step 3 - the other cause, the hard cutoff. The serving system enforces a
  max_tokens / max-output cap; when the count is hit, generation is truncated
  regardless of whether the stop token came, producing the mid-word cutoff. Explain
  stop sequences too (caller-supplied strings that force a halt). Ground: nothing
  below "the model emitted the stop token" or "the cap was reached" changes where the
  reply ends.

## Required contribution
The reader can explain that a reply ends either because the model sampled a stop
token (a learned behavior, not a rule) or because a length cap truncated it, and can
tell a natural finish from a truncation. Settled mechanism stays distinct from the
serving-layer cap. No code.

## Sources and policy
Source policy (lesson/the-mechanics): min 8 sources; primary >= 4, secondary >= 1.
Primaries: authoritative model/API references defining stop reasons and max_tokens
(e.g. Anthropic Messages API stop_reason = end_turn / max_tokens / stop_sequence;
a tokenizer/chat-template primary showing the end-of-turn special token, e.g. a
model card or the HF chat-template/tokenizer docs); a primary establishing that
base LMs do not naturally stop / that EOS is learned. Verify the stop-token and
cap definitions against primaries.

## Boundaries
Link, do not re-teach, next-token generation (autoregressive-generation), sampling
(sampling-temperature), and prefill/decode. This piece owns the stopping mechanic
only. Probability assumed. Two to three ideas, fully.

## Neighboring articles this edition
the-evidence/word2vec, the-instruments/needle-in-a-haystack,
what-could-go-wrong/data-poisoning, when-ai-breaks/optum-health-algorithm. Keep to
the stopping mechanic; do not drift into general generation or context limits.

## Habits not to inherit (recent the-mechanics shapes)
Recent pieces (thinking-out-loud, memorization, prefill-and-decode) open on an
observed behavior then run declarative headings, sometimes with an nb-table walking
a token example. A token/probability table may serve, but do not copy the "watch a
product appear one line at a time" framing or the heading cadence. Name headings
from this piece's own descent.

## Harness and model
harness `claude-code-routine`; model `claude-opus-4-8` for every role. Balanced
production policy; per-role effort not independently settable in this harness
(mechanism deviation only, model unchanged).
