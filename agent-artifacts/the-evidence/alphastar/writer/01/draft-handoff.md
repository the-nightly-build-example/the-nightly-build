# writer draft-handoff: the-evidence/alphastar (01)

## Original-work sentence

The article separates what AlphaStar actually demonstrated (Grandmaster-tier,
anonymous ladder play from human-replay imitation plus league reinforcement
learning, under a camera and a 22-actions-per-5-seconds cap that the paper's own
ablations show cost it strength) from how it is remembered ("AI beat the pros"),
by pinning the January 2018/2019 demonstration agent and the Nature ladder agent
side by side in one table and grading the "superhuman" framing against the
paper's own limits and its explicit ladder-versus-controlled-series caveat.

## Proof result

`./nb check ... --series the-evidence --library <scratchpad>/library-checkout`
run with links: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` written
(words 1977, reading 9 min, sources 6). No warnings left standing.

Earlier iteration cleared three W-SENTENCE-DENSITY warnings by splitting the
imperfect-information, ablation, and Korzekwa-burst sentences; none remain.

## Open evidence / voice questions

- No source asset or chart was used. The evidence names strong figure candidates
  (Fig 3g/3h ablations, Fig 2a ranking, Fig 1a/1c interface and league
  diagrams), and Fig 3h in particular would visually prove the central point
  that the camera interface reduced performance. It was left in prose because the
  research record read the paper via a PDF it did not preserve, so there is no
  captured figure to run through `nb asset`, and the Nature page gates the full
  text. If the editor wants the ablation shown, the researcher would need to
  supply the exact figure crop (percentile axis / baseline labels retained).
- Version-attribution guardrails were honored throughout: the ~280 average APM
  and the pros' several-hundred APM are attributed to DeepMind's January post;
  the 400/500-APM combat bursts and whole-map vision to Korzekwa; the camera +
  22/5s cap and the ~110 ms / 370 ms delays to the Nature version. The January
  "clicked faster" critique is confined to the December demonstration agent, and
  the TLO "doesn't feel superhuman" quote is placed on the constrained (Nature)
  version, as the paper states. No claim rests on the unopened supplementary
  code/data files. No open question blocks handoff.
