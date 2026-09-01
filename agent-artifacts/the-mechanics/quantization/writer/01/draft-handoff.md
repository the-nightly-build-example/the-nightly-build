# Draft handoff: the-mechanics/quantization (01)

## Original work

The draft turns seven separate quantization findings (spread across the LLM.int8(),
GPTQ, AWQ, SmoothQuant, k-bit scaling, Bondarenko papers and the llama.cpp
measurements) into one ordered causal chain a newcomer can follow from a coarser
grid down to the few oversized values that decide the cost, and it replaces the
loose "usually cheap" with the exact conditions under which cheapness holds (a
good scheme, at least four bits) and the three under which it breaks (naive
rounding, a large model, below four bits). The synthesis is visible in the
section order and in the "three conditions the tidy version leaves out" sentence.

## Proof result

Full command from the brief, links included:
`./nb check .nb-work/the-mechanics/quantization/library/the-mechanics/quantization.html --series the-mechanics --library <checkout>`

- BLOCK: 0. verdict: PUBLISHABLE. All 8 source URLs resolved (no link block).
- WARN: 1, left intentionally. W-SENTENCE-DENSITY on "Rounding is cheap for good
  schemes down to about four bits, and it is expensive when the scheme is naive,
  when the model is large, or when the grid drops below four bits, three
  conditions the tidy version leaves out." This is the brief's required wording
  correction, and the three-way parallelism is the teaching payoff; splitting it
  would scatter the correction. It is a controlled long sentence among short ones
  and passes the slop test. Six other density warnings from the first pass were
  fixed by splitting.

## Notes for the editor (decisions, not open blockers)

- No chart. The verified degradation-versus-bits series is carried as a table
  (perplexity, file size, and %-over-FP16 together for LLaMA-7B); a chart of the
  same eight points would duplicate it, so per the brief's "optional" chart, none
  was built. No source asset was used.
- Table row labels. The llama.cpp rows are labelled by nominal bit-width
  (16/6/5/4/3/2-bit) rather than the k-quant type names (Q6_K, Q4_K_M, Q2_K, ...)
  for the non-specialist reader; every perplexity and file-size value is exact
  from PR #1684 and the caption cites it. Flagging in case the editor prefers the
  literal quant-type strings.
- Feature vs weight outliers. The draft keeps the distinction the evidence draws:
  outlier *feature* dimensions (activations, LLM.int8()) are what break naive
  whole-tensor weight quantization at scale, while AWQ protects the *weight*
  channels the largest activations pass through. The bridge sentence ("one such
  outlier stretches the range ... every ordinary weight is then rounded on a grid
  spread too thin") uses the general per-tensor-scale mechanism; worth a read for
  whether the features/weights seam is clean enough for a newcomer.
- Both open items the evidence marks open are marked open in the draft (why
  outlier features arise; where the accuracy floor sits below four bits).
- Taught concepts are linked in prose at first use, not cited as sources
  (weights -> gradient-descent; the count -> parameter-count; perplexity; the
  distillation contrast -> knowledge-distillation), per press/editorial.md.

## Open evidence or voice questions

None blocking. The evidence settled every load-bearing claim, and the voice guide
resolved the register (no phrasing carried over from the quoted writers).
