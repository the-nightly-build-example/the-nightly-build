# Draft handoff — the-instruments/tokens-per-second (writer, invocation 01)

## Original-work sentence
The one act of original work is the comparison table in "The audited number
and the marketing number," which decodes six independently sourced
tokens-per-second headlines (Groq's dashboard figure, Anyscale's LLMPerf
measurement of the same Groq service, Cerebras's updated claim, NVIDIA's
unverified press figure, NVIDIA's own audited MLPerf Offline result, and
MLPerf's audited Interactive result) along the four measurement axes the
lesson teaches — phase timed, concurrency/latency bound, tokenizer, and
hardware/precision/context — something no single cited source does, since
each source reports its own number in its own terms and no source in the
evidence record assembles them side by side on a common basis.

## Paths changed
- `.nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second.html`
  (drafted in place; skeleton's required anchors — why, orientation, takeaway,
  sources — filled; four subject-named flex sections added: "Where the
  stopwatch starts," "More users, less speed each," "The tokenizer, the chip,
  and the prompt length," "The audited number and the marketing number").
- `.nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second/chart-1.py`
  and its rendered `chart-1.png` (new): throughput vs. batch size, Llama-13B
  on a single H200 GPU, 128-in/128-out tokens held fixed, batch 64/128/1,024
  → 1,349/4,750/11,819 tok/s. Source: NVIDIA/TensorRT-LLM H200 launch blog
  (evidence source 12 / article source 5), Numbers table row "TensorRT-LLM,
  Llama-13B, H200, batch-size sweep." Categorical x-axis used deliberately
  (batch sizes are not evenly spaced); provenance script committed beside the
  PNG per docs/charts.md.

## Proof result
Both required runs are clean:
- `./nb check ... --no-check-links` → `BLOCK: 0`, `WARN: 0`, PUBLISHABLE.
- `./nb check ...` (final, with link checking) → `BLOCK: 0`, `WARN: 0`,
  PUBLISHABLE. All 16 source URLs resolved, including the raw GitHub JSON
  results file and the MLCommons/Cerebras/Groq/SemiAnalysis/IEEE Spectrum
  pages.

No warnings were left standing — the draft went through several length and
sentence-density passes (`W-LENGTH-HIGH`, `W-SENTENCE-DENSITY`) to land at
2,199 words (band: 1,200-2,200) with no flagged sentence, and `nb-meta` was
updated to the actual measured values (words, reading_minutes, sources=16)
rather than an estimate.

## Evidence/voice notes
- Cited 16 of the evidence record's 17 sources in first-citation order
  (1 secondary: IEEE Spectrum; 15 primary), each `data-nb-kind` carried
  through from the evidence record's own classification. Omitted only
  evidence source 5 (the v5.0 round-participation statistics, 17,457
  results/23 orgs) — the argument didn't lean on it once the piece had the
  Nebius Server-vs-Interactive comparison and the NVIDIA per-GPU
  normalization to carry the "audited round" framing; including it would
  have padded rather than sourced a claim.
- Followed the commission's structure-avoidance list: no colon-subtitle
  headline, no hedged-contrast dek, no "the same X scored A and B" mold, no
  "number on the box" echo from context-window. Opened on the concrete
  Groq/Anyscale claim and resolved it in the first flex section, per the
  voice guide's "guess, then reveal" instruction, applied once per variable
  (prefill/decode resolves the opener; batch size gets its own worked
  TensorRT-LLM/MLPerf pair; tokenizer and hardware/quantization/context are
  taught together, since the evidence record itself flags the tokenizer
  point as comparatively thin — no invented worked-arithmetic example was
  added there, consistent with "draft only from the evidence record's
  claims").
- Linked (not re-cited) the-mechanics/autoregressive-generation at first use
  in "Where the stopwatch starts" and the-mechanics/letter-counting at first
  use in "The tokenizer, the chip, and the prompt length," both also listed
  in the Why-bookend Background band, per press/editorial.md's link-not-recite
  rule. Noted the-instruments/context-window as a neighbor only insofar as
  its structure and phrasing were deliberately avoided; it is not linked or
  cited, since it teaches a different measurement.
- No remaining evidence or voice questions. The evidence record's own caveat
  (no single named victim with a dollar figure for the misuse case) is
  carried into the article as three convergent mechanisms — the
  Groq/Anyscale gap, the NVIDIA unverified-vs-audited gap, and the industry's
  own corrective actions (MLPerf's Interactive scenario, SemiAnalysis's
  InferenceMAX) — matching the evidence record's explicit framing rather than
  overstating a single-victim narrative the sourcing doesn't support.
