# draft-handoff: when-ai-breaks/ai-writing-detectors (writer/02)

## Original-work sentence

The article fuses four separate results (Liang, Sadasivan, OpenAI, Turnitin)
into one causal account: the single property a detector measures, low
perplexity, is what makes it both unfair to plain and non-native writers and
useless against anyone who paraphrases, so the same mechanism explains the false
accusation and the missed cheat, and the tool is sold anyway. This holds
unchanged after the revision.

## Editorial request resolved

- editor/01 "Required work" (the only blocking item): the paraphrase-collapse
  table and its lead-in misstated the metric scale, asserting a floor of 50 that
  DetectGPT's own after-value of 25.2 breaks and that only fits one of the three
  rows. Reframed the scale honestly per metric, grounded in Sadasivan:
  - Body lead-in (ceiling section): replaced "One common score runs from 50, a
    coin flip, up to 100, perfect." with a sentence stating the scores are each
    out of 100 but not one scale — DetectGPT's is an AUROC where 50 is a coin
    flip and a lower score is worse than one, while the other two are detection
    rates (share of AI or watermarked text caught) whose floor is zero.
  - DetectGPT "What is scored" cell: changed "detection score, 50 to 100" to
    "detection AUROC, 50 is a coin flip", which names the metric and no longer
    asserts a false floor.
  The 25.2 after-value is now consistent (below 50 = worse than a coin flip).
  The other two rows' cells were left as-is; they describe detection rates with
  an implicit floor of zero and never asserted the false 50-floor. No lead-in
  reader address was reintroduced (the editor's cut of "Watch where the
  paraphrase leaves it." stands).

## Numbers

None moved. All six table values are unchanged: DetectGPT 96.5% -> 25.2%,
OpenAI RoBERTa 100% -> 60%, watermarking 99.3% -> 9.7%. Only the scale framing
(prose lead-in and the DetectGPT scored-column cell) changed.

## Proof result

Full `nb check` (links included), from repo root:
  ./nb check .nb-work/when-ai-breaks/ai-writing-detectors/library/when-ai-breaks/ai-writing-detectors.html --series when-ai-breaks
BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` updated words 1758 -> 1763.
Standing note: "library state not provided (--library); open-mode dedupe and
commission checks skipped" — expected for this single-file proof; no warning
left intentionally.

## Open questions

None. Settled work preserved; the claim set was not expanded.
