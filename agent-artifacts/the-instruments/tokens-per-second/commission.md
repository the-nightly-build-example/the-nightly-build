# Commission — the-instruments/tokens-per-second

## Assignment
Teach the measurement behind the speed number every model launch and inference
vendor quotes: "tokens per second." When a lab says a model runs at 250 tok/s,
or Groq/Cerebras/SambaNova advertise 1000+ tok/s, this is the number. Explain
where it comes from step by step, and show at least one real case where the
number misled people and what it cost.

## Angle
A single "tokens per second" figure hides at least four independent choices that
each move it severalfold:
1. Prefill vs decode. Reading the prompt (prefill, parallel) and writing the
   answer (decode, one token at a time) run at wildly different speeds. A quoted
   number usually means output/decode speed, but "time to first token" is a
   different measurement entirely. Ground this in the-mechanics/autoregressive-generation
   (already taught: decode is inherently sequential) — link it, do not re-teach.
2. Batch size / concurrency. Throughput per user falls as more users share the
   GPU; aggregate throughput rises. A peak "tokens/sec" from a full batch is not
   what one user feels. Connect to the-mechanics/nondeterminism (batch effects)
   only if useful.
3. Tokenizer. "Tokens" are not a fixed unit. The same text is more tokens under
   one tokenizer than another, so tokens/sec is not comparable across models
   without normalizing. (the-mechanics/letter-counting taught tokenization — link.)
4. Hardware, quantization, context length. Speed at 1K context != speed at 100K.

Then the misuse case. Best anchored on MLPerf Inference: an industry-standard,
audited benchmark with a defined procedure (scenarios: single-stream, server,
offline; strict latency constraints). Contrast a vendor's headline peak tok/s
(often batch-1, short context, best case) with what MLPerf's constrained,
audited procedure reports, or with independent measurement (e.g., Artificial
Analysis) showing real served throughput far below the marketing peak. The cost:
buyers/users pick a model or chip on a number that does not describe their
workload.

Land the judgment: "tokens per second" is not one number; it is a family of
numbers, and a bare figure without prefill/decode split, batch size, context
length, and tokenizer named is uninterpretable.

## Intended reader
House reader. They have seen "fastest model" / "N tokens per second" claims and
cannot tell what they mean.

## Required contribution
The reader can, given any tokens/sec claim, ask the four questions that decide
what it means, and can explain why two honest measurements of "the same" model
disagree.

## Source obligations (the-instruments: min 8; primary >=4, secondary >=1)
- PRIMARY: MLPerf Inference rules/spec (MLCommons) and a published MLPerf
  Inference results round (the actual results table) — this is the audited
  procedure and dataset. Read the scenario definitions and latency constraints.
- PRIMARY: at least one vendor's own published throughput methodology/claim
  (e.g., Groq or Cerebras or an OpenAI/Google model card / pricing-and-speed page)
  as the owning primary of a headline number.
- PRIMARY: a document defining time-to-first-token vs inter-token-latency vs
  throughput (e.g., NVIDIA TensorRT-LLM docs, or a vLLM paper/docs, or the
  DeepSpeed-Inference / Orca paper on continuous batching) — the engineering
  source for prefill/decode and batching.
- PRIMARY/independent: Artificial Analysis or similar independent measurement as
  a firsthand measurement (classify carefully: it is primary for its OWN measured
  numbers, secondary when it repeats a vendor claim).
- SECONDARY: reputable explainer/coverage for context only.
- Seek contradictory evidence: find a case where the vendor's number is defensible
  under its stated conditions (be fair — the peak is often real, just narrow).

## Starting sources
MLCommons MLPerf Inference (rules + latest results); NVIDIA TensorRT-LLM or vLLM
docs on TTFT/ITL/throughput; a named vendor peak-throughput claim; Artificial
Analysis methodology. Researcher verifies and completes.

## Relevant prior coverage (link, do not re-teach)
- the-mechanics/autoregressive-generation — decode is sequential. Core dependency; link.
- the-mechanics/letter-counting — tokenization / BPE. Link for the tokenizer point.
- the-instruments/context-window — the "second, smaller number" framing is
  adjacent (advertised vs real). Do NOT reuse its structure or its "number on the
  box" phrasing; this is a different measurement. Note it as a neighbor to avoid echo.

## Structures NOT to repeat
- the-instruments desk has a strong habit of "the same X scored A and B and only
  Y changed" headlines (aime, arc-agi, swe-bench, gsm8k). Do not copy that mold.
- No colon-subtitle headline; no hedged-contrast dek; no "number on the box" echo
  from context-window. Open on the concrete speed claim and the split under it.

## Neighboring articles tonight
gpt-4-technical-report (a document), tool-use (mechanics), jailbreaks (risk),
google-flu-trends (a failure). This is the only measurement piece. Stay there.

## Template / mode / paths
- template: lesson; mode: open; order: null; date: 2026-08-01.
- article: .nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second.html

## Harness / model
writer: claude-code-routine / claude-sonnet-5 / medium. researcher high, editor
high, coach low; all claude-sonnet-5. Record harness=claude-code-routine,
model=claude-sonnet-5.

## Tags
Suggest: ["throughput", "benchmarks", "inference", "mlperf"]. Writer finalizes.
