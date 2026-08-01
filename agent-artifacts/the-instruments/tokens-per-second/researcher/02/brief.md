# Researcher brief 02 — the-instruments/tokens-per-second (evidence correction)

Load the `researcher` skill. This is invocation 02: a targeted correction. Read
ONLY your prior evidence record (`../01/evidence.md`) and re-open the primary
source below. Write a complete new `researcher/02/evidence.md` that preserves all
still-valid 01 work and fixes the defect; do not overwrite 01.

## The defect the editor found (must fix)
Your 01 Numbers row for the Llama-13B batch-size sweep records
1,349 / 4,750 / 11,819 tok/s as if "128 input / 128 output tokens" and the same
model/hardware/context were held fixed across all three batch sizes. Re-reading
the primary (NVIDIA/TensorRT-LLM H200 launch blog table) shows those three
throughput figures come from DIFFERENT input/output length configurations
(reported as roughly: 2,048/128 at batch 64; 128/2,048 at batch 128; 128/128 at
batch 1,024). That confounds batch size with prompt/output length, so the numbers
CANNOT support a "batch size alone drives throughput" worked example, and the
article's pillar-2 example and chart-1 built on them are wrong.

## What to do
1. Re-open the exact primary table and transcribe every row faithfully: batch
   size, input length, output length, hardware, and the reported tok/s. State the
   table's real structure so the writer cannot re-misread it. Give the exact URL
   and locator.
2. Decide honestly whether that source contains a clean apples-to-apples series
   (same input+output length, varying ONLY batch size / concurrency) that would
   support the pillar-2 point (throughput per user falls / aggregate rises with
   concurrency). If yes, extract that clean series (full numbers for a possible
   chart). If no, say so plainly.
3. If that primary has no clean batch-only series, find one in another PRIMARY you
   can verify firsthand for the concurrency/batching effect — candidates: the vLLM
   paper/docs or its continuous-batching benchmarks; the Orca (OSDI 2022) paper;
   NVIDIA TensorRT-LLM in-flight-batching docs; or MLPerf Inference Offline-vs-
   Server on the same system+model (aggregate throughput vs latency-bounded). Give
   a verified apples-to-apples series the writer can use for the worked example and
   chart, with exact numbers, units, and locators.
4. Update the Numbers, Sources, and Source-assets sections accordingly. If you add
   a source, classify it primary/secondary with a reason. Keep the total honest
   (do not pad). Note in Contradictions the batch-vs-length confound as a trap.

## Output
`researcher/02/evidence.md` (complete, self-contained). Confirm every URL resolves.

Return exactly one line: `DONE researcher <path to researcher/02/evidence.md>`,
or `BLOCKED researcher <reason>`, or `REQUEST orchestrator <need>`.
