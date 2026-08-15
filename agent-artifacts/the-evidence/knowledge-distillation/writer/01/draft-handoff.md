# Draft handoff: the-evidence/knowledge-distillation (01)

## Original work

The article stages the 2015 paper's own soft-target method against two systems
both now called "distillation" (DistilBERT keeps the mechanism, DeepSeek-R1 keeps
only the name) to hand the reader a concrete test for which of two meanings any
"distillation" claim intends, and it reorders the paper's three experiments so the
never-distilled largest one (JFT) carries the scale honesty and the digit it never
showed (MNIST omit-the-3) carries the proof — a framing and a reader's test the
evidence record supplies claims for but does not itself build.

## Proof result

`./nb check ... --series the-evidence --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing.

Getting there cleared: a mislabeled required section (`orientation`), the flex
count (4 flex sections: soft-targets, mnist, scale, family), a citation-order warn
(renumbered so first-appearance order holds: Hinton 1, DeepSeek 2, Bucila 3,
Kim & Rush 4, Gou survey 5, IBM 6, DistilBERT 7), and three sentence-density warns
(split). Sources are 5 primary / 2 secondary, kinds carried from the evidence
record.

## Framing guardrails (all followed)

- "Dark knowledge" appears nowhere; the idea is taught in the paper's own words
  (soft targets, relative probabilities of wrong answers) with the paper's own
  BMW / garbage-truck / carrot quote.
- JFT is presented as the ensemble/specialists result at scale (25.0 to 26.1,
  specialists in days vs the baseline's ~six months), and the section states
  plainly the specialists were never distilled back into one net. The two
  end-to-end distillations shown are MNIST and speech.
- Drift is the narrower sourced version: distillation became a family of methods,
  broadening began within a year (Kim & Rush 2016), and the present-day gap is
  drawn between DistilBERT (keeps temperature-softened soft targets) and
  DeepSeek-R1 (SFT on generated text, no soft targets, no temperature). No blanket
  "everyone misuses the word."
- The 98.6% MNIST figure is given with its manual-bias caveat; the headline stands
  on the un-nudged 86.8% (877/1010 threes, never a labeled 3 seen).

## Editorial judgment worth a look

The evidence record offered the speech results table as a capturable source asset.
I presented speech in prose and gave one native `nb-table` to MNIST (the headline's
payoff) instead, judging that cleaner and within furniture budget for a ~1,900-word
lesson. Softmax and temperature are linked to the earlier `sampling-temperature`
lesson rather than re-taught, per the press rule on taught ground; that lesson
already credits this paper for the scaled softmax, so the continuity is exact.

## Open questions

None blocking. The evidence record fully supported every claim the piece rests on;
no researcher gap was hit.
