# Voice guide: the-instruments/energy-per-query

This lesson explains where the "energy per ChatGPT query" number comes from
and why two honest estimates of it can differ by 10x, then shows what that
spread does and does not license. Write it as a numerate explainer the reader
could redo the arithmetic from, not a debate recap that ends in a verdict.

Register: plain, declarative, unhurried. One fact, source, or comparison per
sentence. No rhetorical questions, no "you'd think," no lecturing openers.

Reader relationship: the reader already carries a specific number in their
head from somewhere. Treat it as a claim with a traceable origin, not a myth
to wave away. Every correction names the assumption that produced the old
number and the assumption that produces the new one, so the reader leaves
able to catch the next bad number themselves, not just trusting this one.

Moves this article needs:

1. Give every energy figure a comparison scaled to its own size. A number
   that reduces to 400,000 seconds of a toaster teaches nothing; pick the
   appliance and the duration that a person can actually picture, and match
   comparison to magnitude rather than reusing one analogy for every figure
   in the piece.
2. When two honest estimates differ by 10x, do not average them or hedge
   between them. Name the specific input that moves the number that far:
   assumed output length, assumed hardware generation, assumed utilization
   rate. The reader should see which of those inputs their own use case
   depends on.
3. Mark each number's status in the sentence that gives it: metered from a
   real data center, modeled from published specs, or scaled up to a year or
   a country. Do the marking with one plain word doing real work ("measured,"
   "estimated," "scaled up"), not with a hedge word repeated as filler
   ("roughly," "sort of," "it depends") standing in for the distinction.
4. State the range itself as the finding. "Between 0.1 and 4 watt-hours,
   depending on output length and which chip generation ran it" is a
   committed sentence. "It's complicated" or "it depends on many factors" is
   the same information with the content removed.
5. Correct the viral number by opening its calculation: show the arithmetic
   that produced it, show which term changes and why, show the new
   arithmetic. Do this instead of a "not X but Y" swap that asserts a
   replacement number without showing the work that separates them.

Recently used, do not reuse: the opener "The number X published about
itself" (used twice this week, including the sibling Instruments piece on
tokens-per-second); comma-triad or semicolon-reversal deks and headings; any
closer built as a reusable formula.

## Andy Masley, "Using ChatGPT is not bad for the environment"
Source: https://andymasley.com/writing/a-cheat-sheet-for-conversations-about/
Craft:
- cadence: states a number, then fires several parallel comparisons at it in
  quick succession rather than resting on one analogy, then closes the point
  with a short flat verdict sentence before moving on.
- argument: organized as a sequence of anticipated objections stated in the
  words a real skeptic would use, each answered on its own terms before the
  next one starts.
- evidence: fixes one sourced baseline figure early and does all later
  arithmetic as multiples of that single number, instead of introducing a
  fresh figure for every new comparison.
- stance: openly conclusive. States the flat bottom line up front, then
  spends the piece earning it, rather than building toward a reveal.
- notice: catches that a claim can be literally true (a data center really
  does draw as much power as a small city) and still mislead, because
  concentration is a fact about how data centers are built, not about total
  harm done.
- diction: names the actual machine — light bulb, microwave, incandescent —
  never a generic "device" or "appliance."
- reader: addresses someone who already feels a specific worry from a
  specific number they read, and treats that worry as reasonable rather than
  dismissing it before answering it.
- the move the axes miss: before offering a comparison, he checks whether
  multiplying the true number by 10 or 100 would still leave it negligible,
  so the analogy is chosen to survive the reader's own suspicion that he
  under-counted, not just to land well once.
Calibration: "The climate does not react to where on Earth emissions happen,
it only reacts to how much in total is emitted."

## Epoch AI, "How much energy does ChatGPT use?"
Source: https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
Craft:
- cadence: restates the viral figure in one sentence, then moves straight
  into the recalculation with no throat-clearing about "the debate."
- argument: an audit. Takes the original estimate apart term by term (token
  count, parameter count, chip generation, utilization rate), replaces each
  term with a sourced current number, and lets the new total fall out of the
  arithmetic instead of asserting it.
- evidence: names the original source of the viral number and states
  exactly which inputs it used, so the correction reads as a disagreement
  over stated assumptions rather than a vague "that number is wrong."
- stance: declares its own bias toward the reader's skepticism. Says plainly
  it erred toward the higher-cost assumption at every step, so the lower
  headline number can't be read as cherry-picked.
- notice: notices that one "energy per query" figure hides a huge range
  driven by output length, and quantifies exactly how much a 100,000-token
  input moves the number rather than leaving long queries as an unstated
  exception.
- diction: technical terms (parameters, tokens, utilization) always arrive
  paired with the number that makes them concrete in the same sentence.
- reader: assumes the reader wants to rebuild the estimate themselves, not
  just receive the corrected headline number.
- the move the axes miss: treats a disagreement between two published
  estimates as an engineering audit with a paper trail, so the reader leaves
  able to say which single assumption they would change to move the number
  themselves.
Calibration: "I've tried to err on the side of pessimism (higher energy
costs) with every assumption, but different assumptions about parameter
counts, utilization, and token output can bring the cost into the 1 to 4
watt-hour range, or down to around 0.1 watt-hours."

## Hannah Ritchie, "How much electricity does AI consume? [2025 summary]"
Source: https://hannahritchie.substack.com/p/ai-electricity-2025
Craft:
- cadence: moves macro to micro in a fixed order — global electricity
  share, regional concentration, projections, then the per-query number — so
  the small number never gets mistaken for the whole story.
- argument: flags, at first mention, exactly where the piece crosses from
  reported data into her own projection, so the two categories never blur
  later in the piece.
- evidence: gives a range instead of a point estimate wherever the
  underlying number really varies (0.1 to 0.6 Wh), and ties the width of the
  range to a named cause (task complexity) rather than presenting it as
  noise.
- stance: comfortable saying "I don't know" and stopping there, without
  padding the gap with a guess dressed as an estimate.
- notice: notices the real open question is the unexplained gap between
  top-down and bottom-up electricity accounting, not the well-covered
  per-query figure, and spends her space on that gap instead of relitigating
  the popular number.
- diction: uses everyday time units (a minute, ten seconds) as the
  comparison currency throughout, so figures of very different size land on
  one scale the reader already holds.
- reader: writes for someone tracking a running number over time, so she
  dates her claims and says what evidence would update them later.
- the move the axes miss: separates "uncertain because unmeasured" from
  "uncertain because it varies by design" and only apologizes for the first
  kind; the second she reports as a fact about the technology, not a gap in
  her research.
Calibration: "Depending on the length of the text query, asking an LLM a
question is somewhere in this 0.1 to 0.6 Wh range."
