# Editorial review: the-instruments/training-cost (editor/01)

## Skeptic

Thesis: a "$X million to train" figure is not a company's budget but an
arithmetic product, a measured GPU-hour count times an assumed rental price,
scoped to one training run; reading DeepSeek-V3's $5.576 million as an all-in
build cost helped move a market that took $589 billion off Nvidia in a session.

The claims it stands on, and how each held:

1. The number is a construction: 2.788M H800 GPU-hours x an assumed $2/GPU-hour =
   $5.576M, final run only. Recomputed against Table 1 and the evidence. The
   stage split (pre-training 2,664K/$5.328M, context extension 119K/$0.238M,
   post-training 5K/$0.01M) sums to 2,788K GPU-hours and $5.576M, and 2,788K x $2
   = $5.576M. The 180K GPU-hours per trillion tokens, the 14.8T-token pre-train,
   and the 671B/37B size all match the primary. Held.

2. Both inputs are choices: the hour count is measured for one run, the $2 rate
   is an assumption stated in the same breath as the total, not a bill paid.
   Supported verbatim by the report. Held.

3. DeepSeek's own caveat excludes only prior research and ablation experiments,
   not salaries or data acquisition; the ~$1.6B capex / >$500M / ~50,000-GPU
   all-in framing is SemiAnalysis's own estimate, and "did not build OpenAI for
   $5M" is Rasgon's. The article quotes the caveat exactly and keeps reported
   fact (the caveat), estimate (SemiAnalysis, Rasgon), and synthesis separate.
   Held. This was the round's attribution correction and it stuck.

4. The market case: NVDA $142.62 (Fri) to $118.42 (Mon 27 Jan 2025), a $24.20
   fall, "nearly 17 percent" (16.97%), ~$589B erased, largest single-day company
   loss on record, more than double the $279B prior record (Nvidia, ~5 months
   earlier). Every figure matches the exchange data and the Bloomberg/CNBC/Forbes
   reporting. The headline ratio (589e9 / 5.576e6 = ~105,600) supports "more than
   100,000 times." Held.

Cross-number honesty (the round's guard): the headline and the stat strip set a
one-day market-cap move beside a training-run bill. They are labeled as different
kinds of thing (a "loss" against a "bill"; "market loss" against "reported
training cost"), the dek hedges to "helped trigger," and the body states plainly
that no source ties the loss to the misreading alone. The piece performs the
scale juxtaposition the voice guide asked for without implying the two numbers
are the same quantity or that the bill caused the loss. Held.

Breaks found and fixed on this read:

- The report was called "peer-reviewed." It is an arXiv technical report /
  preprint; the evidence records a v1/v2 submission, no peer review. Cut the
  descriptor to "a public report." (fix)
- R1 was said to have been "released five weeks later." The evidence carries no
  R1 release date, and R1 shipped ~20 Jan 2025, roughly 3.5 weeks after the 27
  Dec report, not five. Removed the specific interval; the supported point (R1 is
  a separate model with a separate run and cost) stands. (fix)
- Rasgon was titled "Bernstein's semiconductor analyst." The record supports
  "Bernstein analyst"; his desk title is not in it. Trimmed to what the evidence
  states. (fix)

Nothing broke a central claim, no figure conflicted with its owning primary, and
every source href matches the evidence and points at the source itself, so no
skeptic finding routed to the researcher or writer.

## Cut

Slop failures found and cut: two.

- A body self-reference closing the orientation section: "This lesson works
  through both choices, then follows the number into the week a market read it
  past its own scope." The lesson template allows self-reference only in the two
  bookends; this was body self-narration and a pure signpost (it reported where
  the argument would go without doing any of it). Deleted; the section now ends
  on the "two choices" sentence that the next section unpacks.
- A method-narration punchline: "Change either input and the total changes with
  it, which is the whole point of writing the multiplication out instead of just
  quoting the answer." The trailing clause both narrated the article's own method
  and used the "whole point" construction. Cut the clause; the fact-bearing
  sentence remains.

Edge sentences read out of order held up: the paragraph and section openers and
closers each carry a fact or a step. The one imprecise closer was in the selloff
section: "What $589 billion shows is that the misreading was expensive when it
happened" read the aggregate move as a measure of the misreading's cost, which
its own next sentence denied. Rewrote to bound the causation cleanly.

Prompt-leakage pass: the takeaway's closing questions ("How many hours were
counted. What price was assumed for them. Which part of the process they
covered.") deliver the commission's required contribution in the article's own
terms rather than lifting its wording, and the bookend previews are template
function, not leaked planning. No leaks cut.

Borrowed-phrasing pass against the voice-guide quotations: the draft follows the
exemplars' moves (credit-then-turn on the caveat, the multiplication worked on
the page, the gap left for the reader) without borrowing their clauses. Nothing
cut.

Furniture: the stat strip and both figures do real work and their labels are
factual; none reads as a stacked block or a recurring formula. No component added
or removed.

Formula check against the recent-pattern notes: the heading "A measured count
times an assumed price" avoids the "number is the model plus the effort" mold;
the closing section "A $589 billion trading session" avoids the "What a high
score does not promise" / "Where the same X lives" molds; the dek is a single
committed sentence, not a comma triad or a semicolon reversal. No formula found.

Punctuation and banned terms: no em-dashes; no use of leverage, load-bearing,
machinery, revolutionary, transformative, game-changing, or "AI race." Nothing to
trim.

## Reader

Read straight through as the paper's reader, what I have that the sources alone
would not give me: a way to take any "$X million to train" figure apart into a
measured hour count and an assumed price, scoped to one run, plus the discipline
to keep the report's narrow caveat separate from analysts' all-in estimates and
to refuse a market's sole-cause reading. The raw figures live in Table 1, the
exchange data, and the analyst notes; the decomposition, the attribution split,
and the bounded juxtaposition are the article's. The draft-handoff's
original-work sentence claims exactly this, and it survives the read. The piece
teaches rather than restates its sources. The prose sits closer to the
voice-guide exemplars than to a median summary: concrete, literal, the
arithmetic done in front of the reader. The headline, reread as the largest
claim, is arithmetically true and paid off honestly by the body.

## Edits

- Cut a body self-reference signpost closing the orientation section ("This
  lesson works through both choices...").
- Cut the "which is the whole point of writing the multiplication out..." clause
  in the arithmetic section.
- Changed "peer-reviewed report" to "public report" (unsupported descriptor).
- Changed "released five weeks later" to "released weeks later" (unsupported and
  incorrect interval).
- Changed "Bernstein's semiconductor analyst Stacy Rasgon" to "Bernstein analyst
  Stacy Rasgon" (unverified title).
- Rewrote the selloff section's final two sentences into one bounded closer:
  "How much of the $589 billion the misreading caused on its own, no source
  separates out, and none claims it was all of it."

## Required work

None blocking. Optional, writer: if a verified DeepSeek-R1 release date is worth
carrying, restore a specific interval sourced to the primary; I removed the
incorrect "five weeks" rather than guess. The chart and the Table 1 asset were
inspected and need no correction, so nothing routes to the writer on furniture.

## Decision

approve. Every load-bearing figure recomputes against the primary, the
cross-number comparison stays honest and bounded, and the skeptic and slop fixes
were all reachable by editing; nothing publication-blocking remains.
