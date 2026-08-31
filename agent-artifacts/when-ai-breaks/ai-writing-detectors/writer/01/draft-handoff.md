# Draft handoff: when-ai-breaks/ai-writing-detectors (01)

## What the article does to the evidence that the evidence does not do itself

It fuses the record's separate findings into one causal account: it shows that
the single property a detector measures, low perplexity, is what makes the same
tool both biased against plain and non-native writing and trivially evadable by
paraphrase, so one mechanism explains the false accusation and the missed cheat
at once. The evidence record holds these as unconnected results (Liang's bias
numbers, Sadasivan's ceiling and paraphrase attacks, OpenAI's withdrawal,
Turnitin's claim and concession); the article makes them a single chain, visible
across the mechanism, ceiling, and takeaway sections.

## Proof result

`./nb check ... --series when-ai-breaks` (links included): **BLOCK: 0, WARN: 0,
verdict PUBLISHABLE.** `nb stamp` wrote words=1758, reading_minutes=8, sources=9.
The gated owning pages (turnitin.com s1, openai.com s7) return HTTP 403 to the
link probe, which the checker classifies as resolving; they do not block.

No warnings were left standing. The two W-SENTENCE-DENSITY notes from the first
pass were fixed by splitting the sentences, not waived.

## Precision the round required (all handled)

- OpenAI fully withdrew its own classifier (July 20 2023; 26% TP / 9% FP), shown
  with its verbatim editor's note. Turnitin did not withdraw: it added the
  under-20% asterisk and conceded ~4% sentence-level, and kept selling. The two
  responses are stated separately and contrasted in the close.
- The harsh false-positive figures are labeled to their samples: 61.22% is
  Liang's average on non-native TOEFL essays against near-perfect on native US
  essays. Turnitin's under-1% is stated as its own document-level launch claim.
  I did not use the Washington Post ~50% figure at all, so no small-sample number
  is presented as a general rate.
- Turnitin's detector is stated as **not** one of Liang's seven tested detectors,
  with the mechanism (not the vendor) carrying the bias and Vanderbilt naming it.
- Perplexity is linked (prose link to the-instruments/perplexity.html), not
  re-taught; only its direction is used.
- No individual student is named.

## Furniture

- Source asset (Fig. 1): panel (a) of Liang et al. Figure 1, captured from the
  arXiv PDF (2304.02819) with `nb asset pdf`. Carries the near-perfect-on-native
  vs wildly-wrong-on-non-native contrast that the prose numbers cannot show on
  their own. Cited to s5 with locator/url/note.
- Table: Sadasivan et al. paraphrase collapse (DetectGPT, OpenAI RoBERTa,
  watermarking), before/after, cited to s6.
- Note (quotation): OpenAI's verbatim withdrawal editor's note, cited to s7.

## Open questions

None. If the editor wants a live browser render of the figure and table, note
that `nb render-check` was skipped here for lack of Chrome in this environment;
CI will run it.
