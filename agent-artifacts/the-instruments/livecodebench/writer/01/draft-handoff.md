# Draft handoff: the-instruments/livecodebench (01)

## Original work

The article welds the evidence's separately recorded facts (the moving-cutoff
contamination fix, an early DeepSeek model's ~60 → ~0 collapse across its
cutoff, the six dated dataset versions, and DeepSeek's and Qwen's mismatched
self-chosen windows) into one causal chain: the same release-date rule that
exposes a memorized answer is what makes two LiveCodeBench scores incomparable,
and from that single mechanism the piece derives a reading rule the evidence
never states — name the window, version, scenario, and shot count before
setting two figures side by side.

## Proof result

`nb check ... --series the-instruments` with links on: **BLOCK: 0, WARN: 0,
PUBLISHABLE.** No warnings left standing. (En route: cleared W-SOURCES-MIN by
citing all eight non-discarded evidence sources; cleared W-PLACEHOLDER by
writing real table headers; cleared two W-SENTENCE-DENSITY warnings by
splitting the four-scenarios definition and the why-bookend preview.)

## Notes on evidence handling (no request needed)

- The ~60 → ~0 collapse is the paper's base-model statement (DS-Base-33B, Sec.
  5.1). Figure 1 plots the instruction-tuned sibling and GPT-4-O, so prose
  names "an early DeepSeek coding model" and the caption "a DeepSeek model and
  GPT-4-O" — no variant is conflated, and neither is confused with the separate
  DeepSeek-V3 whose base 19.4 appears later.
- DeepSeek-V3's 19.4 is presented strictly as the base-model figure, pass@1,
  3-shot, window 0801-1101, honoring the record's caveat. The widely-quoted
  chat/instruct figure the record could not fully verify is not referenced.
- The counter-material is kept honest and non-refuting: the cutoff is
  vendor-supplied, post-cutoff problems can be reused in future contests
  (survey), and the found contamination was LeetCode-specific while AtCoder
  stayed smooth.

## Open questions

None. Evidence and voice guide settled the draft; no researcher request or
commission decision is outstanding.
