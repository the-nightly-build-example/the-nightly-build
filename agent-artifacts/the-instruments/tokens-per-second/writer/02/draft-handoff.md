# Draft handoff — the-instruments/tokens-per-second (writer, invocation 02, revision)

## Original-work sentence
The one act of original work is still the comparison table in "The audited
number and the marketing number," now updated to cite the corrected MLPerf
source: it decodes six independently sourced tokens-per-second headlines
(Groq's dashboard figure, Anyscale's LLMPerf measurement of the same Groq
service, Cerebras's updated claim, NVIDIA's unverified press figure, NVIDIA's
own audited MLPerf Offline result, and MLPerf's audited Interactive result)
along the four measurement axes the lesson teaches — phase timed,
concurrency/latency bound, tokenizer, and hardware/precision/context —
something no single cited source does, since each source reports its own
number in its own terms and no source in the evidence record assembles them
side by side on a common basis.

## Paths changed
- `.nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second.html`
  (edited in place; editor's 01 s2-citation fix preserved untouched).
- `.nb-work/the-instruments/tokens-per-second/library/the-instruments/tokens-per-second/chart-1.py`
  and its rendered `chart-1.png` (rebuilt, same filenames, old data fully
  replaced): grouped bar chart, three MLPerf-audited platforms (Nebius
  B200x8, Nebius H200x8, AMD 8xMI300X), each showing Offline/Server/
  Interactive throughput for the identical Llama 2 70B model, latency bounds
  named in the legend (200 ms/token, 40 ms/token). Source: MLCommons MLPerf
  Inference v5.1 raw results file, per researcher/02/evidence.md's "NEW —
  MLPerf v5.1, same-hardware Offline/Server/Interactive throughput" table.

## Required fixes addressed
1. **Removed the confounded pillar-2 example.** Deleted the TensorRT-LLM
   "128 input and 128 output tokens held fixed" claim and its 1,349/4,750/
   11,819 figures entirely from "More users, less speed each." Did not use
   the brief's optional matched-pair aside (341 vs. 303 tok/s/GPU) — cut
   rather than kept, to stay inside the word band without diluting the
   stronger 20-platform series.
2. **Rebuilt pillar 2 on the corrected MLPerf series.** The section now
   opens on the audited 20-platform Offline/Server/Interactive series
   (roughly a third-to-two-thirds drop on every platform), points to the
   rebuilt chart, keeps the unaffected mechanism paragraph (vLLM/prefill
   reuse) and the unaffected "what the total hides" paragraph, then lands
   the existing Nebius B200 worked arithmetic (101,611 → 59,622.7, 41%)
   explicitly as one of the charted platforms, correcting "eight NVIDIA
   B200 GPUs" to "eight Nebius B200 GPUs" (the submitter named in the
   evidence's own row) and replacing the old "reverse of the chart" line
   (which described batch size on the x-axis, no longer true) with a line
   describing the latency-bound/batching-room tradeoff the new chart
   actually shows.
3. **Rebuilt chart-1 with `nb chart`** from the corrected series, grouped
   bars, latency bounds named per scenario, MLPerf results file cited in
   the caption. Inspected the rendered PNG: bars honestly show Offline ≈
   Server > Interactive on all three platforms, with visibly different drop
   sizes (41%, 32%, 64%) rather than a uniform effect.
4. **Loosened the pillar-4 context-length claim** (editor item 2): the
   1.9x/1.6x H200-vs-H100 comparison now states plainly that the two
   examples also differ in model and tensor-parallel configuration, not
   context length alone, before drawing the (still defensible) conclusion
   that hardware speedup depends on workload shape.
5. **Rewrote the takeaway's opening** away from the commission's own
   assignment phrasing ("not one measurement... a family of them"). It now
   opens directly on the two resolved cases (Groq/Anyscale, NVIDIA
   audited/unverified) and states the conclusion in the article's own terms
   ("describes one specific run... not a fixed property of the chip"). The
   "which member got measured" callback is gone with the "family" framing
   it depended on; no dangling reference remains.
6. **Renumbered sources in first-citation order** after the content
   reshuffle: the MLPerf raw-results file moved from citation 9 to citation
   5 (now first cited for the corrected pillar-2 chart, reused later for the
   Nebius worked example and the table's MLPerf Interactive row); Artificial
   Analysis's methodology and provider pages shifted from 10/11 to 9/10; the
   TensorRT-LLM H200 blog — now used only for the loosened pillar-4 aside —
   moved from citation 5 to citation 11. Total source count unchanged at 16.
   Verified the full `#sN` sequence in the rendered body is strictly
   ascending on first appearance before treating the Sources list as final.
7. The editor's item-3 fix (source `s2`'s href, already repaired directly by
   the editor) was preserved untouched, as instructed.

## Proof result
- `./nb check ... --no-check-links` → `BLOCK: 0`, `WARN: 0`, PUBLISHABLE.
- `./nb check ...` (final, with link checking) → `BLOCK: 0`, `WARN: 0`,
  PUBLISHABLE. All 16 source URLs resolved, including the new/moved MLPerf
  raw JSON citation and the TensorRT-LLM blog now cited only for the
  loosened aside.

No warnings left standing. `nb-meta` updated to the actual measured total:
words 2197 (was 2199; net change from removing the old worked example and
adding the corrected one, the pillar-4 loosening, and the takeaway rewrite
was close to neutral), reading_minutes 11 (unchanged), sources 16
(unchanged), byline reading time unchanged at "11 min read."

## Evidence/voice notes
- No remaining evidence gaps. The corrected evidence record supplied
  everything needed for both required fixes (the 20-platform MLPerf series
  for pillar 2, and enough detail on the TensorRT-LLM table's actual
  columns to loosen pillar 4 honestly rather than cut it).
- One open judgment call, not a question: the brief permitted keeping the
  llama_70b matched pair (341 vs. 303 tok/s/GPU) as a one-line aside. I cut
  it rather than keep it — the 20-platform MLPerf series already carries
  pillar 2's worked-arithmetic requirement more strongly, and the word band
  (1,200-2,200) left little room to add a second, weaker aside without
  cutting something else load-bearing.
