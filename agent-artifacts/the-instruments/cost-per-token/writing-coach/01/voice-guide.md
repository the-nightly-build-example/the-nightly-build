# Voice guide: the-instruments/cost-per-token

Write like someone walking a colleague through their own cloud bill, line by
line: plain, specific, and already on the reader's side. The house register
(Yglesias-plain, no fuss) covers tone. What this piece needs on top is a way
to run one fixed task through four separate price shocks — input/output
split, cache, batch, tokenizer — without either re-deriving the arithmetic
from scratch each time or dumping a spreadsheet. And it needs a way to name
whoever got the comparison wrong without turning the lesson into a takedown.
The reader relationship stays teacher-to-reader throughout; the numbers do
the arguing, not the writer's tone toward the people who got them wrong.

Every idea in this lesson keeps the same fixed task and the same headline
number from first mention to last. Move the number by naming, in the same
sentence, exactly one thing that changed about it. Never restate the whole
calculation to get there.

## Licenses

```text
form: single-anchor recomputation
move: SemiAnalysis's sticker-vs-blended move ("AI Value Capture: The Shift
      To Model Labs") states the published per-token price once, then moves
      to the real number by naming the one variable responsible (an
      input:output ratio, then a cache-hit rate) rather than rebuilding the
      math. The reader tracks the number changing for a reason, not a new
      number appearing.
bar:  each restated figure in the worked example must differ from the one
      before it by a single, named cause the reader could repeat back
      ("because three in four tokens here are cached input, not because the
      sticker price changed"). A recomputed number with no stated cause, or
      one sentence carrying two causes at once, breaks the license.
```

```text
form: one small honest table
move: SemiAnalysis defers its full method to a linked table and keeps the
      prose to the two numbers that matter (sticker, blended); the body
      text never turns into the table. License a single compact table in
      this piece the same way: it holds the running example's price at each
      step of the worked calculation, after prose has already stated the
      first and last figures in an ordinary sentence.
bar:  the table may appear once, adds no figure the prose has not already
      named, and exists to make already-stated numbers scannable side by
      side, not to introduce the comparison. If the table is doing
      explanatory work the prose skipped, cut the table and write the
      sentence.
```

```text
form: ratio-in-prose compression
move: Patrick McKenzie ("Anatomy of a Credit Card Rewards Program") keeps
      figures in a single consistent unit (basis points) inside ordinary
      sentences instead of parenthetical decimals, so a margin or a gap
      reads as one clause, not an aside doing arithmetic.
bar:  any dollar or token figure introduced in prose resolves, in the same
      sentence, to a ratio or multiple the reader already has a feel for
      (a fraction of the sticker price, tokens-per-output-token) rather than
      standing alone as a bare number or percentage.
```

```text
form: naming the misled party plainly
move: Ben Thompson ("Who's Afraid of Chinese Models?") states exactly what
      number an actor used and exactly what it cost them to trust it, then
      lets the reader supply the judgment from the figures already given,
      rather than characterizing the actor.
bar:  the misuse-case sentence names the actor, the specific number they
      relied on, and the concrete consequence. It carries no adjective
      judging the actor ("naive," "gullible," "sloppy"). If the sentence
      needs an adjective to land, the facts before it were not sufficient
      and need another sentence, not a stronger one.
```

Recently used, do not reuse: this series' "two numbers are both true" twin
headline mold; comma-triad and semicolon-reversal deks. Let the single
worked example carry the persuading instead — the piece should not need a
rhetorical reversal to make its point once the numbers have moved.

## Ben Thompson, "Who's Afraid of Chinese Models?"
Source: https://stratechery.com/2026/whos-afraid-of-chinese-models/
Craft:
- cadence: long paragraphs that build one economic principle before
  introducing the number that tests it; the price comparison arrives after
  the reader already has the frame (commodity pricing, cost structure) to
  judge it.
- argument: states the cheaper headline price, then reopens the question by
  asking what it costs to reach a correct answer, not just a token.
- evidence: real, dated per-token prices for named models, quoted directly
  rather than rounded into "cheaper" or "pricier."
- stance: skeptical of both the panic and the hype it corrects; commits to
  a conclusion instead of leaving the tension open.
- notice: treats a lower sticker price as a claim to test, not a fact to
  report.
- diction: business-school terms (COGS, commodity market, marginal cost)
  defined in the same breath they're used, never left assumed.
- reader: a smart generalist who reads the news but wants the economics
  under the headline, not an insider who already has it.
- the move the axes miss: he lets the reader watch him revise his own first
  reaction to the cheaper price, rather than announcing the correction from
  above. The correction is dramatized, not asserted.

## SemiAnalysis, "AI Value Capture: The Shift To Model Labs"
Source: https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model
Craft:
- cadence: short, declarative sentences that each move the number once;
  no sentence both introduces a variable and recomputes the total.
- argument: sticker price is a starting figure, not a wrong one; the piece
  earns the real number by naming what a live workload actually looks like.
- evidence: a named model, a named price, a named ratio (input tokens per
  output token) and a named cache-hit rate, each cited to how the number was
  produced.
- stance: matter-of-fact, no surprise performed at the gap between sticker
  and blended price; the size of the gap is left to do its own work.
- notice: treats "the sticker price is $X" and "the price we actually pay is
  $Y" as two different, both-true facts about the same product, not a
  gotcha.
- diction: a handful of terms of art (blended price, cache hit rate) used
  exactly once defined, then reused verbatim.
- reader: an industry buyer who wants the number they'd actually be billed,
  not a definition of tokens.
- the move the axes miss: it defers full methodology to a linked table
  entirely outside the prose, keeping the article's own arithmetic to
  exactly the two numbers the argument needs.

## Simon Willison, LLM pricing posts (simonwillison.net, tag: llm-pricing)
Source: https://simonwillison.net/2025/Oct/15/claude-haiku-45/ (representative
of the recurring pattern across https://simonwillison.net/tags/llm-pricing/)
Craft:
- cadence: the cost calculation lands as one flat clause at the end of a
  paragraph, not a build-up — input count, output count, result, done.
- argument: doesn't argue that price matters; demonstrates it by running an
  actual task through the math in front of the reader.
- evidence: his own real usage numbers (exact token counts from a real
  request), never a hypothetical example.
- stance: curious and unbothered — the number is offered for the reader to
  check, not defended.
- notice: treats the input/output split as ordinary and worth stating every
  time, never assumed after the first mention.
- diction: plain, almost terse; no adjective sits between the numbers and
  the dollar figure.
- reader: someone who could run the same numbers themselves and might want
  to.
- the move the axes miss: he links out to a calculator so the reader can
  change one variable and watch the price move, which is the prose
  equivalent of the single-anchor recomputation this piece needs on the
  page itself, without a link.

## Patrick McKenzie, "Anatomy of a Credit Card Rewards Program"
Source: https://www.bitsaboutmoney.com/archive/anatomy-of-credit-card-rewards-programs/
Craft:
- cadence: sentences vary hard, from a punchy fragment to a long clause
  chaining several causes, matching the rhythm to how surprising the claim
  is.
- argument: builds a margin (revenue in, cost out, margin kept) entirely in
  prose, in one consistent unit, so the reader never has to convert units
  mid-argument.
- evidence: industry structure and named mechanisms (interchange, a
  specific card's headline rate) rather than a single company's leaked
  number.
- stance: skeptical of the program design without treating the people who
  use it as marks; a fee structure can be exploitable and its users still
  rational.
- notice: flags where the reader is about to reach for the wrong intuition
  ("money is fungible... but many people don't orient their lives as if
  this were true") before it costs the argument anything.
- diction: industry shorthand (basis points) introduced once, then used
  bare for the rest of the piece.
- reader: addressed directly and occasionally as a stand-in decision-maker
  ("you, a program manager"), which puts the reader inside the mechanism
  instead of outside looking at it.
- the move the axes miss: he warns the reader off a rabbit hole ("I
  strongly recommend you don't [look up the interchange tables], as you
  will be reduced to gibbering madness") instead of walking into it himself
  — a model for how this piece should wave off tokenizer or vendor-tier
  minutiae that would sink the single worked example.

## Self-test

A writer following only the house default would ground the lesson in "a
worked example," name real prices, and avoid hedged contrasts — all true
here already. What they would not know, without this guide, is how to move
one number through four causes without re-deriving it each time, how much
table is too much, how to compress a cost gap into a ratio instead of a
paragraph of decimals, and how to write the misuse case so the number
convicts and the writer doesn't. Those four moves are what this guide adds.
