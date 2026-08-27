# Commission: what-could-go-wrong/fragility-of-value

## The argument

The fragility (and complexity) of value: the claim that human values are
intricate and high-dimensional, so any objective simple enough to write down
will leave most of them out, and that because a powerful optimizer drives to the
extreme of whatever objective it is given, a near-miss on values does not
produce a near-miss in outcome. It produces a catastrophe, because the maximum
of a slightly wrong objective can be arbitrarily bad. Eliezer Yudkowsky stated
it as "value is fragile" and "the complexity of value" (around 2009-2011); Nick
Bostrom gave the same worry as "perverse instantiation" and "malignant failure
modes" in *Superintelligence*.

## Why this lesson, now

The desk has run several failures that assume this idea without teaching it. The
reader has met the orthogonality thesis (a system can be capable and still want
anything), goal misgeneralization (an agent that pursued the wrong goal
off-distribution), and reward hacking (a system gaming its measure). Fragility of
value is the argument that ties those into a claim about why alignment is
considered hard: getting the goal almost right is not good enough. The reader
should meet it at full strength and see exactly where its force comes from and
where it thins out.

## The angle to test (steelman first, then draw the line)

Open with the argument as its authors made it: value is complex, so a short
objective misses most of it; and under strong optimization the correlation
between a proxy and what we actually want holds in the ordinary range and breaks
at the extreme ("the tails come apart"), so optimizing a proxy hard yields a
perverse maximum. Give the mild illustration honestly (optimize for smiles, get
a world drugged into smiling, or tiled with smiley faces) as a proof that a
gentle-sounding target plus a hard-enough optimizer is enough for disaster, not
as a joke.

Then draw the series' line between what real systems have shown and what is still
analogy about systems that do not exist. On the shown side: goal
misgeneralization (Langosco/Shah et al., 2022) and specification-gaming/
reward-hacking examples are real near-misses where a system optimized a proxy and
did something unintended. On the projection side: those failures were caught,
bounded, and not catastrophic, and today's RLHF-trained models are imperfectly
but tolerably aligned to messy human preference, which the strongest form of the
argument did not obviously predict. Report the strongest critique: value may be
less fragile than claimed, since preference learning captures a great deal
cheaply, and the extremal-catastrophe step assumes an optimizer far more
single-minded than trained systems are (link mesa-optimization for that
assumption). Bring it to the present: who presses the argument now and what they
want (get values right before systems are powerful, do not rely on trial and
error), against who reads current empirical alignment as evidence it is
tractable. Name the gap wherever confidence outruns proof, in either direction.

The researcher must work from the original statements (Yudkowsky's own posts,
Bostrom's own text) and the primary empirical near-miss papers, not commentary
about them. Name no company as an authority.

## Boundaries

Do not re-teach the orthogonality thesis, goal misgeneralization, reward hacking,
or mesa-optimization as if new; link them in Background where they carry a piece.
Keep this on the fragility argument itself, distinct from orthogonality (which
says a system *can* have bad goals) and from goal misgeneralization (a shown
near-miss). This is one of five lessons tonight; no overlap with a fine-tuning
paper, an embedding benchmark, format-constrained decoding, or a deployment
failure.

## Source policy

Series floor: 8 sources, at least 4 primary and at least 1 secondary. Yudkowsky's
and Bostrom's statements and the empirical near-miss papers are primary to their
claims. Meet the floor with sources that change the interpretation, including the
strongest critique.

## Production

Profile balanced; no stage required. This run: writing-coach and researcher on
the strong model, researcher at high effort; writer at medium effort; editor at
high effort.

## Recent habits not to inherit

- The two-clause "and/but" dek is the current house default; build the dek
  another way and avoid the three banned molds in `spec/headlines.md`.
- The desk keeps closing on a "Who makes the case now" section. The present-day
  turn is required; name its section in this piece's own nouns.
- Recent safety pieces lean on a "shown result vs projection" spine; that spine
  fits here, but do not echo their deks or headings.
