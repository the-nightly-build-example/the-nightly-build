# Draft handoff: when-ai-breaks/predpol-predictive-policing (writer round 01)

## Original-work sentence

The evidence record hands over a dozen separately sourced facts (a 2011
academic model, a 2015 field trial known only secondhand, two 2018 feedback-
loop papers, a 2019 city audit, a 2020 ban, a 2021 bias story, and a 2023
accuracy exposé) plus a flagged asymmetry in how the company responded to two
different critiques; this article turns that set into one continuous
chronological argument that uses the recorded-crime/actual-crime distinction
to explain, in a single mechanism, how a system can be simultaneously
near-random and racially skewed, states the vendor-response asymmetry
honestly instead of manufacturing a rebuttal the company never gave, and
generalizes the mechanism into a transferable diagnostic ("a record of
decisions can pass for a forecast") that none of the individual sources state
as a unified claim.

## Proof result

`./nb stamp` then `./nb check .nb-work/when-ai-breaks/predpol-predictive-policing/library/when-ai-breaks/predpol-predictive-policing.html --series when-ai-breaks --library .nb-work/library` (links included):

```
BLOCK: 0
WARN:  1
  W-LENGTH-HIGH      lesson band is 1200-2200 words; found 2388
verdict: PUBLISHABLE
```

## Warning left intentionally

- **W-LENGTH-HIGH (2388 words vs. the 1200–2200 band).** Left standing after
  several trimming passes (the draft started at 3082 words). The overage is
  the direct cost of fulfilling this round's corrections in full: reporting
  the honest company-response asymmetry (silence on accuracy, a detailed
  on-record rebuttal on bias, plus the founders' narrower RCT rebuttal and
  Bertozzi's broader one) as three distinct, non-conflated positions; carrying
  the 7.4% figure through its full triangulation chain (paywalled original,
  two independent readers) without shortcutting the attribution; and keeping
  three separate published neighbors (chicago-heat-list, shotspotter-wrongful-
  arrest, compas-recidivism) distinct rather than collapsing the boundary-
  setting into one line. `when-ai-breaks`'s series config sets `strict: false`,
  so this is a WARN, not a BLOCK. All ten `W-SENTENCE-DENSITY` warnings the
  same run originally produced were fixed by splitting the flagged sentences;
  none were left standing.

## Evidence and voice notes

- No open evidence gap. The three corrections in the brief (name the
  vendor-response asymmetry honestly rather than inventing a rebuttal to the
  accuracy critique; attribute the 7.4% figure as triangulated, not
  independently verified; avoid a false-precise Santa Cruz ban date) are all
  reflected in the article as written.
- Confirmed the three neighbor library URLs directly against
  `.nb-work/library/library/when-ai-breaks/*.html` rather than guessing the
  relative-link convention.
