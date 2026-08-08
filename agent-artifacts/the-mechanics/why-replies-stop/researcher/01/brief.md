# researcher brief: the-mechanics/why-replies-stop (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/editorial-direction.md — citation standard, series territory, declared reader
- /home/user/the-nightly-build/.nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/commission.md — subject, angle, required contribution, source policy
- this brief

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/researcher/01/evidence.md

Establish firsthand from primaries: (1) that generation halts when the model emits a
special end-of-sequence / end-of-turn token that is part of the vocabulary and
sampled like any other token - use an API reference documenting stop reasons
(e.g. Anthropic Messages API `stop_reason` values end_turn / max_tokens /
stop_sequence) and a tokenizer/chat-template primary showing the actual end-of-turn
special token id (a model card or HF tokenizer/chat-template docs). (2) That emitting
EOS at sensible places is LEARNED in post-training, not architectural - find a
primary establishing that base/pre-trained LMs do not reliably stop and that
instruction/chat tuning teaches turn-ending. (3) The serving cap: how max_tokens /
max-output truncates mid-generation, and how caller stop sequences work, from
authoritative API docs. Supply a concrete, checkable micro-example of a stop token's
probability rising as an answer completes (from a primary or a defensible worked
illustration). Confirm every URL resolves. Source policy: min 8, primary >= 4,
secondary >= 1. Note where popular explanations blur "the model decided to stop" with
"the length cap cut it off."
