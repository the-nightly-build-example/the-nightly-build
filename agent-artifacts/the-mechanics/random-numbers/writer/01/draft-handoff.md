# Writer handoff: the-mechanics/random-numbers (01)

## Original-work statement (one sentence)

The article assembles nine separate measurements and one raw 1-to-100 count
table into a single step-by-step trace that works backward from the observed
"7" to the token-probability-list-plus-sampler that produces it, then to the
human-learned and alignment-sharpened shape of that list, and it renders the raw
exmergo series as a uniform-referenced chart so the reader sees at a glance that
the choice is biased rather than merely variable, which is synthesis and
visualization the evidence record does not itself perform.

## How the work is visible in the article

- The argument descends in named rungs: the measured behavior (orientation) to
  "there is no generator, only a distribution and a draw" (no-generator) to "the
  distribution is learned from human text and sharpened by alignment"
  (human-shape) to "temperature rescales but cannot flatten it" (temperature) to
  "let it call a real generator" (real-generator). Each rung names a real part
  and what it does, per the series brief.
- The chart (chart-1.py / chart-1.png) is built only from the verified exmergo
  1-100 series, keeps the full axis, and marks the fair rate (about 100) as a
  reference line, so the zero-height round numbers and the 69 dip carry the
  "biased, not variable" point visually.
- The two human sources are kept distinct and cited to their owners: Kubovy &
  Psotka (peer-reviewed, single-digit 28.4% for 7) and the Veritasium
  crowdsourced 1-100 survey (flagged in prose as a rough survey, not a
  controlled result).
- Settled vs open is marked in-prose per the series prompt: settled that the
  shape tracks human bias, that alignment amplifies it, and that no knob or
  chain-of-thought fixes it; open how much of the final shape is inherited
  versus added by alignment, and the 69 suppression (exmergo's safety-tuning
  guess is presented as a guess, not a shown cause).
- Bias scoped to chat/aligned models throughout (West & Potts base-vs-aligned),
  never "LLMs at the architecture level."

## Recent-habit checks (from the brief)

- "Why this matters" does not end on "By the end you will know / be able to";
  it ends on the open question ("what is it doing when it hands you a 7?"), which
  the takeaway resolves.
- Headline is built in this piece's own nouns around the concrete "7"; it is not
  a quoted-failing-prompt echo of the recent negation piece.
- Heading construction is varied (a finding, a flat statement, an imperative, a
  negative-result line), not the recent two-clause comma-and rhythm.
- Dek carries no banned mold: no two-clause "and" contrast, no comma-triad, no
  atmospheric colon subtitle. nb-meta dek and the rendered dekline are identical.

## Proof result

- Command: `./nb check .nb-work/the-mechanics/random-numbers/library/the-mechanics/random-numbers.html --series the-mechanics --library /home/user/library-checkout`
- Full proof with links: BLOCK: 0, WARN: 0, verdict PUBLISHABLE.
- Article is 2200 words (lesson band 1200-2200), 8 sources (7 primary, 1
  secondary), stamped. 0 em-dashes; no banned lexical terms.
- No warnings intentionally left.

## Open questions

None blocking. One editorial note for the editor's judgment: the "37/73"
human-1-to-100 datapoint rests on the Veritasium crowdsourced survey, whose
video the researcher did not open; it is used only as corroborating context and
flagged as a rough survey in the prose, with the peer-reviewed human claim
(Kubovy & Psotka) carrying the load. If the editor wants that datapoint dropped
rather than flagged, the sentence and source 5 can be removed without disturbing
the argument.
