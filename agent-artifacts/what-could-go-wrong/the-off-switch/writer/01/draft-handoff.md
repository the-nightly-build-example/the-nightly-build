# Draft handoff — writer 01 — what-could-go-wrong/the-off-switch

## Original work

This lesson separates the theoretical off-switch/corrigibility argument into
two named, independently sourced claims the evidence record kept braided
together — a proven existence result (uncertainty about the objective gives a
system a mathematical incentive to defer, per the Off-Switch Game's Theorem 1
and Corollary 1) versus a set of empirical "resistance" demonstrations that
each required an experimenter to hand the model a goal and instruct it to
guard that goal above anything else — and for every empirical result states,
in the sentence carrying the number, exactly who supplied the goal and how
contrived the setup was, so the reader can see that the formal fix and the
observed behavior are answering two different questions rather than
confirming or refuting the same one.

## Article and asset paths changed

- `library/what-could-go-wrong/the-off-switch.html` (full draft; no other
  assets — no chart or source-image asset was warranted, per the researcher's
  own note that a chart was optional and the argument is fully carried by the
  comparison table already in the piece).

## Proof result

```
./nb check .nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html --series what-could-go-wrong --library /home/user/the-nightly-build/library-checkout
```

`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

Warnings encountered and resolved during drafting (none left standing):
- `W-LENGTH-HIGH` — first draft ran to 2886 words against the lesson band's
  1200–2200; trimmed across five passes (cutting redundant restatements,
  shortening the utility-indifference aside, tightening the empirical section
  now that the comparison table carries the exact figures) to a final 2198.
- `W-SENTENCE-DENSITY` — multiple long/dense sentences (up to 93 words) were
  split or shortened per the house punctuation rule (period over comma-splice
  or colon-stacking) until none remained.
- `W-SELF-COUNT` — `nb-meta.words` and `reading_minutes` were placeholders
  during drafting; set to the checker's measured counts (2198 words, 9 min)
  once the text stabilized.

No warnings intentionally left standing.

## Editorial requests addressed

None — this is round 1, no prior `editorial-review.md` exists yet.

## Remaining evidence or voice questions

None. The evidence record fully supported the piece as commissioned: the
four theoretical primaries (Omohundro, Soares et al., Hadfield-Menell et al.,
Orseau & Armstrong), the three empirical primaries (Palisade, Anthropic,
Apollo/OpenAI o1) with their exact conditions, the DeepMind rebuttal, the
Thorstad critique, and the one secondary source (eWeek) for present-day
register were all used and cited. No researcher request was needed.

Verified against the brief: "AI race" appears 0 times; em-dash count is 0;
`machinery`, `load-bearing`, `revolutionary`, `transformative`,
`game-changing` all 0; `leverage` 0 (under the ≤1 cap); no company is named
as a safety authority (Anthropic, OpenAI, and Palisade are cited only for
their own reported methods and numbers). The rendered dekline text is
byte-for-byte identical to `nb-meta.dek`. Sources: 11 total, 10 primary, 1
secondary (min 8 / primary ≥4 / secondary ≥1, all satisfied). Builds on
`../what-could-go-wrong/instrumental-convergence.html` via a Background link
in the "Why this matters" bookend; that lesson is not re-run.
