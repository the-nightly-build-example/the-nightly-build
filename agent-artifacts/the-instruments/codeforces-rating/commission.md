# Commission: the-instruments/codeforces-rating

## The measurement

The Codeforces rating (an Elo-style number, e.g. "Codeforces rating 2727,
99.8th percentile") that AI labs cite to claim a model is a world-class
competitive programmer. The Instruments teaches how one number that compares AI
systems is made, what it can support, and at least one real case where it misled.

## The angle

A Codeforces rating is not a score a model "got" the way a benchmark accuracy is.
Codeforces is a live human competitive-programming site whose rating is an
Elo-type system: your number moves only by competing against other rated humans in
timed contests and is updated from who you beat and lost to. When a lab reports a
model's "Codeforces rating," that number is almost always an *estimate*, computed
by running the model on past problems (often with many attempts, generous time,
and sometimes test-case access the contest never gave a human) and then mapping
the solve rate onto the human rating scale, or by simulating participation in past
rounds. The article's job: show step by step where the number comes from, then
draw the line between what it supports (the model can solve many isolated
competitive-programming problems) and what it cannot (a live rating earned under
human contest conditions), and name a concrete case where the gap misled readers.

## Where the number comes from, step by step

1. What a Codeforces rating actually is for a human: Elo-style, contest-driven,
   relative to a live field. Link `the-instruments/chatbot-arena-elo` for the Elo
   mechanics (pairwise outcomes updating a rating) instead of re-teaching Elo from
   scratch; teach only the Codeforces-specific parts (rated rounds, the percentile
   bands, how a rating maps to titles).
2. How a lab turns a model's problem-solving into a "rating": either
   percentile-from-solve-rate (AlphaCode's method — solve a set of past problems,
   find the percentile a human with that performance would sit at, read off the
   equivalent rating) or a simulated/estimated contest rating (OpenAI's o-series
   reporting an estimated Codeforces Elo). Spell out the assumptions: number of
   attempts allowed, time limits, whether the model's submissions were actually
   graded by Codeforces or by the lab's own harness.
3. What the number can and cannot support. It can support: strong performance on
   self-contained algorithmic problems. It cannot support, on its own: that the
   model would hold that rating in live rated contests against humans, because the
   conditions differ (attempts, time, contamination from problems in training
   data, no penalty dynamics).

## At least one real misleading case (required by the beat)

Find and verify a concrete instance where a Codeforces rating or percentile was
cited as if it meant live human-competitive standing and misled people. Strong
candidates to check: AlphaCode's "top 54%"/"28th percentile" (DeepMind, 2022) being
read as stronger than it was, or contamination critiques (a reported rating
inflated by problems that appeared in training data), or an o-series "estimated
Codeforces rating" quoted without its "estimated / under these conditions"
qualifier. The researcher confirms which case is best evidenced; the article needs
one case whose cost or distortion is documented, not merely asserted.

## What this article must not do

- Do not re-teach Elo from scratch; link `the-instruments/chatbot-arena-elo`.
- Do not drift into a general "benchmarks are gamed" essay; stay on this specific
  number and how it is manufactured.
- Do not close with the "Read [the number] as X, and ask separately whether Y"
  takeaway construction — the last two Instruments pieces (bfcl, and the CLIP
  Evidence piece) both end on that mold. Land the judgment in this article's own
  frame.
- Avoid the forming house tic "doing the work" ("the attempts, not the model, are
  doing the work"). Make the point in fresh words.

## Sources and production

- Source policy (lesson/the-instruments): at least 8 sources, at least 4 primary,
  at least 1 secondary. Primary = the documents that own the claims: Codeforces'
  own rating-system description, the AlphaCode paper (Li et al., Science 2022),
  OpenAI o1/o3 system cards or announcements reporting Codeforces Elo, any paper
  documenting contamination or condition effects. Verify every rating/percentile
  against the source that reports it, with its exact conditions.
- Production policy: profile "balanced", model tier "capable" (recorded actual:
  claude-opus-4-8). Effort guidance researcher high / writer medium / editor high
  / coach low; none `required`; effort not independently settable via the run's
  child interface, so roles run at session default reasoning; no deviation to
  report.

## Original-work target

Take the several different "Codeforces rating" claims labs have published, show
they were produced by different procedures under different conditions, and put them
on one honest footing against what a human's Codeforces rating actually certifies —
so the reader can tell a manufactured rating from an earned one.
