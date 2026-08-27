# writer brief: the-mechanics/structured-output (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, series prompt
- ../../commission.md — the behavior, the four-rung causal chain, boundaries, source policy, and the recent habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/02/evidence.md — USE THIS ONE (the round-02 record; researcher/01 is superseded). The complete set of claims available to you; use its Numbers section exactly.
- article to edit: /home/user/the-nightly-build/.nb-work/the-mechanics/structured-output/library/the-mechanics/structured-output.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/structured-output/.nb-context

Output: draft-handoff.md (this directory)

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-mechanics/structured-output/library/the-mechanics/structured-output.html --series the-mechanics --library /home/user/library-checkout

This round's focus: read researcher/02/evidence.md, not 01. The settled/disputed
split is the spine. Settled: constrained decoding masks logits before the draw.
Disputed: the size of the pure-formatting penalty. The largest figures (the Tam
et al. ~63-point Haiku drop) are contested and partly an artifact of a schema
that put the answer before the reasoning; do not present them as the settled
cost of formatting, and the record marks the OpenAI announcement's eval
percentages NOT-TO-BE-QUOTED. Handle the terminology collision explicitly:
reserve "JSON mode" for OpenAI's weaker feature and call the hard-constrained
thing constrained decoding or schema-constrained structured outputs. The honest
finding is that the behavior is real, the cause is lost reasoning room, and the
fix is to let the model reason before it is forced into the format. Background
links, not re-teaching: prefill-and-decode, thinking-out-loud, tool-use.
