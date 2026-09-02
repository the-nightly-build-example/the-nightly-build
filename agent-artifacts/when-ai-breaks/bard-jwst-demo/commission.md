# Commission: when-ai-breaks/bard-jwst-demo

## The incident

Google's first public demo of Bard, its ChatGPT competitor, shipped a confident
factual error. In the promotional example Google published ahead of its February
2023 launch event in Paris, Bard answered a question about the James Webb Space
Telescope by stating that JWST "took the very first pictures of a planet outside
our own solar system." That is false: the first image of an exoplanet was made in
2004 by the European Southern Observatory's Very Large Telescope (the object
2M1207b). Astronomers flagged it immediately; the error was widely reported; and
in the days around it Alphabet's share price fell sharply (reported around 9%,
roughly $100 billion in market value). The lesson tells this incident in order and
explains why this kind of system fails this way.

## What the lesson must do

- Tell it in order, with names and dates. What Bard was built to be (Google's
  large-language-model chat assistant, its answer to ChatGPT), where the false
  claim appeared (Google's own announcement blog post / promotional post, dated),
  who caught it and how fast, who it affected (Alphabet, its investors, the
  public reading a flagship demo), and what Google did afterward (its statement,
  and that it proceeded with the launch). Pin the market-value figure to reporting
  and state it as reported, not as proven causation.
- Explain the failure. A large language model generates fluent, plausible
  continuations from patterns in text; it has no built-in check that a confident
  sentence is true, and "sounds right" is not "is right." Teach or link the piece
  the reader needs (the library has the-mechanics/hallucination and
  the-mechanics/false-confidence). Make clear this was not a rare glitch but the
  ordinary behavior of the technology, surfaced in a high-stakes ad.
- Close on where the same weakness lives now, in systems the reader uses:
  AI-generated search summaries and assistant answers that state wrong facts with
  the same fluency, in products people rely on daily.

## Required contribution

The reader leaves understanding that fluent confidence is not verification, and
that a polished demo is not a test of truth — and able to spot the same failure in
the AI answers they meet every day. The article's work is using one well-recorded
launch-day error to make the general mechanism concrete and its cost legible.

## Boundaries and continuity

- Hallucination and false confidence are taught (the-mechanics/hallucination,
  the-mechanics/false-confidence): link them in Background and teach only the
  minimum needed here; do not re-derive next-token prediction from scratch.
- Report the market-value drop as reported and resist implying the demo alone
  caused it; note that the Paris event and competitive context were part of the
  week. Keep the causal claim honest.
- Discuss Google/Alphabet as the operator, reported as fact; name no company as an
  authority.

## This run's neighbors

Four other lessons publish tonight on other desks. No overlap; this is the
when-ai-breaks desk's single incident for the run.

## Source policy

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Candidate
primaries: Google's Bard announcement blog post (Sundar Pichai, "An important next
step on our AI journey," Feb 6 2023) and/or the promotional post carrying the
erroneous answer, as the artifact; the ESO 2004/2005 press release on the first
imaged exoplanet (2M1207b); a NASA/ESA JWST page or NASA exoplanet record
establishing the true first-image history; Google's follow-up statement. Secondary:
Reuters/The Verge/other reporting on the error and the share-price fall (the
market figure is secondary). The researcher confirms kind and count, and records
the erroneous sentence verbatim from a source that shows it.

## Production policy (recorded)

profile balanced. writing-coach low, researcher high, writer medium, editor high.
Model "capable" for every role, none required; roles run on this harness's
default capable model. Record actual models in handoffs.

## Recent patterns to break (habits, not rules)

- Deks recur as a two-clause ", and"-twist (galactica: "..., and Meta's own paper
  had already measured...") or a comma triad (banned). galactica is this desk's
  closest recent piece and also a fabrication-in-a-demo story — do not echo its
  dek or headline construction.
- Headlines default to a negative-fact reveal or a trailing second clause
  (galactica: "..., and its public demo lasted about two days"). Find this
  incident's own headline.
- The closing present-day section keeps getting a "Where X still Y" heading; vary
  it.
