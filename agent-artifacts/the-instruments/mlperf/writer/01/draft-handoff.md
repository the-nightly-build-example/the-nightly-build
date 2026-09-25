# Draft handoff: the-instruments/mlperf (writer 01)

## Original-work sentence

An MLPerf result is a time or a throughput for one system on one fixed task
under one set of rules, comparable only to another result inside that same box
of division, category, scenario, and chip count, and the "N times faster"
headlines strip the box away on the way out. The article makes that visible: it
does the division in the reader's sight (205.6 / 106.5 = 1.93 from doubling
chips, everything else held fixed), and it puts the headline ratio and the
chip-count/round difference side by side in one table, so a same-box comparison
and a stripped-box one can be told apart on the page rather than asserted.

## Nuance honored

- The failure is located downstream, not inside MLPerf. The "Where the
  disclosure gets dropped" section states plainly that MLCommons' own Messaging
  Guidelines *mandate* disclosing version, division, category, status, scenario,
  and chip count, and that the loss happens when marketing or coverage keeps the
  ratio and drops the disclosures.
- The legitimate case is kept distinct from the misled one. NVIDIA's v5.0
  Blackwell-vs-Hopper claim (2.2x at 512 GPUs vs 512 GPUs, same benchmark,
  division, and category) is presented as the honest, rules-permitted kind; the
  TPU v4 normalization case (4,216-chip A100 vs 256-chip IPU on the raw MLPerf
  Training 2.0 leaderboard) is the documented misled example.
- The Tyche 256/512 timing-log figures (205.6 / 106.5 min) are kept separate
  from NVIDIA's own 512-GPU marketing figures (121.09 / 269.12 min), per the
  researcher's note that they come from different NeMo/system configs.
- Single-run caveat stated in prose: the two times are the run_0 wall clock from
  each submission's timing log, read to the minute, not the single figure
  MLCommons selects across a benchmark's several runs.
- The Google TPU v4 reading is attributed to Google as a competitor's read, not
  to MLCommons.
- Taught ground linked, not re-taught: tokens per second (inference throughput)
  and training compute are plain prose links at first use; no company is named
  as an authority on the benchmark.

## Proof status

`./nb stamp` written (words=1805, reading_minutes=8, sources=11).

- `nb check --no-check-links`: **BLOCK: 0, WARN: 0**, PUBLISHABLE.
- `nb check` with links: **BLOCK: 0, WARN: 0**, PUBLISHABLE.

No warning left standing on purpose. 11 sources (10 primary, 1 secondary);
cited primary and secondary both clear the series floor; sources numbered in
first-citation order.

## Open questions for the orchestrator

1. **Inference v6.0 throughput number withheld deliberately.** The ~2.49M
   tokens/sec DeepSeek-R1 figure was not used, because it is an MLCommons-owned
   number that rests only on secondary reporting (THE DECODER) and the researcher
   did not open the v6.0 log row for it; the commission forbids citing secondary
   for a number MLCommons owns. The article therefore uses the-decoder only for
   the framing (NVIDIA's record came from the largest configuration ever
   submitted, 288 GPUs, vs far smaller competitor systems; results only partially
   comparable). If the desk wants the throughput figure on the page, the v6.0
   primary results row needs to be opened first.
2. No new claims were introduced beyond the evidence record; no evidence gap
   blocked drafting.
