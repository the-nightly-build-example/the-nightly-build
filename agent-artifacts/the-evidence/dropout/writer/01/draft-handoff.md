# Draft handoff: the-evidence/dropout (01)

## Original work

The article lines up the paper's own Section 7.4 dataset-size finding (dropout's
benefit rises then fades as data grows, and is nil on 100-500 examples) against
the disclosed dropout settings of later large-data models, reading the
present-day narrowing as the continuation of a boundary the 2014 paper had
already measured rather than a later reversal of it. That synthesis is the work
the evidence record (a list of claims) does not do itself; it is carried by the
"The gain shrinks as the data grows" and "Where the largest models leave it off"
sections and landed in the takeaway.

## Proof

`nb check ... --series the-evidence --library /home/user/library-checkout` (links
included): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp`: words=1903,
reading_minutes=8, sources=7 (6 primary, 1 secondary; series floor met).

## Furniture

One table (per-benchmark error, with and without dropout) carries the results
comparison; one note ("In plain language") renders the 2ⁿ weight-sharing
ensemble intuition. No chart: the dataset-size experiment (Sec. 7.4 / Figure 10)
has no numeric series in the evidence record, so it is carried in prose, not a
fabricated chart. The evidence record flags JMLR Figure 10 as a candidate source
asset; it is not captured here (the prose spine carries it and a PDF crop adds
risk without new argument). Capturing it later is a reasonable enhancement if the
editor wants the curve on the page.

## Accuracy cautions honored

- Dropout narrowed, not abandoned: stated explicitly (still 0.1 in the
  Transformer, used in PaLM finetuning, small doses after batch-norm in vision).
- "Off in the largest models" attributed to disclosed reports (PaLM states it,
  LLaMA omits it, the 2025 study tests it), not a survey; frontier proprietary
  settings named as undisclosed. GPT-3 is not cited as dropout = 0.
- Transformer rate cited to Vaswani (0.1 base, 0.3 large EN-DE); the 2025 paper's
  "0.3 at each layer" is not repeated.

## Open question

None blocking. Minor: the citation count (source 2) is a live figure recorded
2026-09-06 as "more than 44,000"; if the article sits before publication for a
while, that floor stays true but could be refreshed.
