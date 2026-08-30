# writer brief: the-mechanics/random-numbers (01)

Inputs:
- editorial-direction.md (house standard, the paper's voice, The Mechanics prompt)
- writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- researcher/01/evidence.md (the complete claim set; use the Numbers section
  exactly; a full measured 1-100 series is preserved for a chart)
- library/the-mechanics/random-numbers.html (the initialized article to edit)
- .nb-context/ (effective template contract, runtime assets, furniture catalogs)

Output: writer/01/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/the-mechanics/random-numbers/library/the-mechanics/random-numbers.html
Proof: ./nb check .nb-work/the-mechanics/random-numbers/library/the-mechanics/random-numbers.html --series the-mechanics --library /home/user/library-checkout

## This round's focus
Work backward from the behavior (asked for a random number, the model over-picks
7 for 1-10, and 37/42/47 for 1-100) to ground: no random number generator; the
model emits a probability distribution over next tokens and a sampler draws from
it; that distribution's shape is learned from human text, which over-picks the
same values. Hold the line the commission names: this is about the SHAPE of the
distribution over which number is chosen (why it is lumpy), not run-to-run
variation (nondeterminism) or what the temperature knob does (sampling-
temperature). Link both and do not re-teach them.

The evidence gives you measured numbers — use them, do not merely assert the
bias. A chart from the preserved 1-100 series is warranted if a comparison is the
point (build it only from the verified series, via nb chart, with honest axes and
a cited source). Close on the real fix (hand the model a tool that calls a real
RNG; link the-mechanics/tool-use) and mark settled vs open.

Evidence flags (the record details them):
- Scope the bias to chat / instruction-tuned models: base models are measurably
  closer to uniform (West & Potts), and alignment appears to amplify the "7"
  preference. Do NOT say "LLMs at the architecture level."
- The human "37/73 for 1-100" pattern is owned by a Veritasium crowdsourced
  survey the researcher flagged as secondary (video not opened); the peer-reviewed
  human primary is Kubovy & Psotka 1976 (28.4% chose 7 for 0-9). Keep them
  distinct and cite each to its owner.
- Large-study per-cell percentages read from HTML are approximate; headline
  figures are solid. Do not print a precision the record does not support.

Link the-mechanics/autoregressive-generation, the-mechanics/sampling-temperature,
the-mechanics/nondeterminism, and the-mechanics/tool-use in Background at first
use rather than re-teaching.

## Recent habits to break (do not inherit these from recent pieces)
- Do not end the "Why this matters" opener with "By the end you will know / be
  able to …". Let the takeaway resolve the opener's setup.
- Avoid a quoted-failing-prompt headline that echoes the recent the-mechanics
  piece (negation: "'No onions' gets onions"). The concrete "7" is this piece's
  own hook; build the headline in its own nouns.
- Avoid the recent heading rhythm ("Two systems drop the same word" / "A language
  model bets on the words it has seen most"). Vary heading construction.
- Check the dek against spec/headlines.md's banned molds: no two-clause "and"
  contrast, no comma-triad, no atmospheric colon subtitle.
