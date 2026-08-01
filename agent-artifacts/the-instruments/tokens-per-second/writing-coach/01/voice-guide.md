# Voice guide — the-instruments/tokens-per-second

Register: a systems-performance explainer, not a benchmark recap. The reader
has seen a tok/s number and trusted it; the job is to make them permanently
unable to read one bare. Write as someone who has personally reconciled two
conflicting measurements of "the same" thing and is walking the reader
through how, not as someone summarizing what others found.

Moves that change sentences in this article:

- Open on one named, concrete claim — an actual quoted figure from an actual
  vendor or model, not a category ("fast inference chips claim..."). State it,
  then immediately name the one variable hiding under it. The complication
  arrives in sentence two, not paragraph three.
- Before explaining a variable (prefill vs. decode, batch size, tokenizer,
  context length), state the reader's default guess about what the number
  means, then show the concrete case where that guess is wrong. Guess, then
  reveal — do the complicating with a number, not with a claim that the
  subject is "more complicated than it seems."
- Every one of the four variables needs its own worked arithmetic: two
  measurements of output that look contradictory until the missing condition
  is named. A sentence asserting "batch size changes throughput" is not
  enough; show the same GPU at batch 1 and batch 32 with actual numbers, the
  way a fixed measurement setup makes a discrepancy legible.
- When you name a measurement's conditions (hardware, batch, context length,
  scenario), name all of them together in one place, the way an audited
  benchmark report would, not scattered as asides. The reader should be able
  to point at the sentence that specifies MLPerf's scenario definition the
  same way they can point at the vendor's peak-number sentence.
- Build the misuse case as a mechanism, not a scandal: what the buyer
  believed, what condition the vendor's number quietly assumed, and what
  broke when reality supplied a different condition (more concurrent users,
  longer context, a different tokenizer). Let the gap between two honest
  numbers do the accusing; do not editorialize on top of it.
- Vary sentence length the way a careful technical explanation does: short
  declaratives to land a fact, one longer sentence when a mechanism needs its
  causal chain kept in one breath. No semicolon chains connecting the four
  variables into a single overloaded sentence.
- Address the reader's intuition directly and test it, but do not perform
  incredulity or crack jokes at the reader's expense. Steelman the vendor's
  peak number where it is genuinely true under its stated conditions before
  showing what it leaves out.

Recently used, do not reuse: no "the same model scored A and B and only Y
changed" headline mold. No "number on the box" phrasing or framing borrowed
from the context-window piece. No colon-subtitle headline. No hedged-contrast
dek ("X is not Y; it is Z" and its cousins — semicolon reversal, suspended
question, comma triad). Open on the concrete speed claim and the split
underneath it, not on a category or a warning.

## Dan Luu, "Some latency measurement pitfalls"
Source: https://danluu.com/latency-pitfalls/
Craft:
- cadence: short technical sentences carry the facts; longer ones carry the
  mechanism connecting two facts. No ornament between them.
- argument: built as a sequence of discovered gaps — what the dashboard
  shows, what it actually measures, and the layer in between where the
  difference hides.
- evidence: real production numbers from a named system, compared directly
  (server-measured p99 against client-measured p99 for the same requests),
  so the discrepancy is visible before it is explained.
- stance: an engineer reporting what they found wrong with a system they
  worked on, including what remains unfixed and why fixing it is not free.
- notice: catches the exact place a metric's definition silently narrows
  ("that's probably more work than is worth it") — names the tradeoff instead
  of hiding it.
- diction: plain infrastructure nouns (netty, kernel, shard), no metaphor
  standing in for a mechanism that could instead be named.
- reader: a practitioner who will use this to audit their own dashboards, so
  every claim is checkable against a described setup.
- the miss: he never states a finding as a lesson. He states the number, the
  gap, and the mechanism, and lets the reader assemble the lesson.
Calibration: "While it's possible to plumb instrumentation through netty and
the kernel to track request latencies after Finagle has handed them off (the
kernel even has hooks that would make this somewhat straightforward), that's
probably more work than is worth it in the near future."

## Marc Brooker, "Open and Closed, Omission and Collapse"
Source: https://brooker.co.za/blog/2023/05/10/open-closed.html
Craft:
- cadence: alternates a short flat statement with a longer clause that
  supplies the reason, so each beat lands before the next complicates it.
- argument: escalates through progressively harder cases — simple
  distribution, then bimodal, then the benchmarking consequence, then the
  production failure mode — each building only on what came before.
- evidence: simulation numbers with exact parameters stated together
  (utilization, mean latency, timeout threshold), so a reader could rerun the
  scenario and get the same discrepancy.
- stance: presumes an intelligent reader who has not yet been shown the
  specific case that breaks their assumption, and walks them to it rather
  than asserting the conclusion first.
- notice: catches that a benchmark tool's own arrival model can silently
  reproduce the flaw it's supposed to expose — the pitfall is in the
  measuring instrument, not just the system measured.
- diction: precise queueing vocabulary introduced only at the point it's
  needed, defined in the sentence that uses it first.
- reader: addressed directly at moments of realization, never lectured at
  length; the address is a beat, not a register.
- the miss: the payoff of each example is a changed number, not a changed
  adjective — "25x" does the convincing, not "much worse."
Calibration: "In the long-term, though, because our utilization is only 80%
(ρ=0.8), the server always eventually catches up and the queue drains. One
way that often happens in production is because of client behavior,
specifically retries after timeouts."

## Brendan Gregg, "Frequency Trails: What the Mean Really Means"
Source: https://www.brendangregg.com/FrequencyTrails/mean.html
Craft:
- cadence: opens with a real terminal output, then a direct question to the
  reader, then a short answer that undercuts the question — a tight
  three-beat rhythm repeated across the piece.
- argument: guess-then-reveal, run several times with different production
  datasets, so the pattern (averages hide the real shape) is demonstrated
  rather than asserted once.
- evidence: a survey across hundreds of production servers with a
  proportion stated as a fact (most distributions have outliers, a fifth
  have multiple modes), not just one hand-picked anecdote.
- stance: invites the reader to notice their own bad intuition before
  correcting it — collaborative, not corrective from above.
- notice: catches that a summary statistic can be arithmetically correct and
  still describe no real request in the dataset — the mean as a fictional
  point.
- diction: concrete instrument names (iostat) and units attached to every
  figure; no unitless "significantly" or "much higher."
- reader: someone who has read a dashboard number and believed it, exactly
  the position this article's reader starts from.
- the miss: the fragments ("Not what you expected either? Exactly.") work
  because they land after a specific number, never in place of one.
Calibration: "The average, commonly the arithmetic mean, shows the index of
central tendency. But, as I've found when studying latency distributions in
production environments, the tendency is often not central, but may be
skewed by outliers, or split by multiple modes."

## Jeffrey Dean and Luiz André Barroso, "The Tail at Scale"
Source: https://www.barroso.org/publications/TheTailAtScale.pdf
Craft:
- cadence: measured and declarative, built for an audience that will cite
  it; few asides, each sentence adds one fact or one consequence.
- argument: moves from the human-scale problem (a slow reply feels slow) to
  the systems-scale multiplier (one in a hundred requests is slow, but a
  request touching a hundred machines almost always hits one), then to
  named mitigations.
- evidence: named percentiles (95th, 99th, 99.9th) attached to named causes
  (background work, resource contention, garbage collection, power
  throttling), never a percentile cited without a candidate mechanism.
- stance: authoritative and unhedged where the data supports it, careful to
  separate what the architecture guarantees from what it merely tends to
  produce.
- notice: catches that fixing average latency and fixing tail latency are
  different engineering problems requiring different techniques, so a team
  optimizing the average can leave the tail untouched or worse.
- diction: precise distributed-systems nouns (fan-out, straggler, hedged
  request), each carrying a specific engineering technique rather than a
  general idea.
- reader: an engineer who will design a system differently after reading
  this, so every claim is stated at the grain of a design decision.
- the miss: the paper earns its authority by being exact about what a
  technique costs (extra load from a hedged request) in the same breath as
  what it buys, never presenting a fix as free.
Calibration: "Adding more resources may reduce the average response time,
but it does not necessarily improve the tail latencies."
