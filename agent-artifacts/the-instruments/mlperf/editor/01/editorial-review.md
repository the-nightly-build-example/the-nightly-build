# Editorial review: the-instruments/mlperf (editor/01)

## Correct

Thesis, stated from the draft alone: an MLPerf result is a time or a throughput
for one system on one fixed task under one set of rules, comparable only to
another result in the same box of division, category, scenario, and chip count;
the "N times faster" headline fails downstream, when marketing or coverage keeps
the ratio and drops the box. Claims under it: (1) a run becomes a number by a
fixed task and quality target timed to the wall clock; (2) the division and the
availability category are the labels that decide whether two numbers compare;
(3) the comparable number supports a system-against-system time, not a model or
workload claim, and nothing across a boundary; (4) a documented case, the raw
MLPerf Training 2.0 leaderboard ranking a 4,216-chip A100 against a 256-chip
IPU, shows what dropping the box costs.

I tried to break each against the owning document and could not.

- Closed and Open, training: checked against training_rules.adoc via the record.
  Closed requires the same preprocessing, model, training method, and quality
  target as the reference; Open lets the submitter change the model or method.
  The draft states both correctly and cites the rules doc, not coverage.
- Availability categories: checked against submission_rules.adoc. Available =
  rentable or purchasable now; Preview = committed to ship within a set window;
  RDI = research/development/internal, may never ship; the categories apply to
  Closed, Network, and Open alike. The draft's plain-language rendering holds and
  the "apply to all divisions" line matches the quoted rule.
- Every figure recomputed against its owner. 205.6 / 106.5 = 1.93 (the log values
  205.61 / 106.53 give the same), 256 vs 512 GB200 GPUs, Closed, Available
  on-premise, all from the v5.0 Tyche logs. v5.0 round: 201 results, 20 orgs,
  June 2025, from the MLCommons announcement. TPU v4 case: A100 4,216 vs IPU 256
  (about sixteenfold; 4,216 / 256 = 16.5), the 4x-larger 4,096-chip system
  "nearly 10x faster," equal-size TPU v4 leads of ~4.3x and ~4.5x over the IPU,
  all from the TPU v4 paper. The draft keeps 4,216 (largest entry) and 4,096
  (the scaling claim) distinct, as the evidence does. NVIDIA generational claim:
  2.2x at 512 vs 512 GPUs, up to 2.6x per GPU. No break.
- The Google reading is attributed to Google as a competitor's read, not to
  MLCommons ("That reading is a competitor's, since Google submits too").
- The single-run caveat is present and precise: the two times are the run_0 wall
  clock from each timing log, not the figure MLCommons selects across a
  benchmark's several runs.
- data-nb-kind audited row by row against the researcher's primary/secondary
  test. The two arXiv design papers, the four MLCommons rules/results documents,
  the v5.0 logs, and the v5.0 announcement are primary; the TPU v4 paper is
  primary for its own analysis and is framed as a competitor's read; the NVIDIA
  blog is primary only for the claim NVIDIA makes and is used only for that; THE
  DECODER is the one secondary and carries framing, never a number MLCommons
  owns. Eleven sources, ten primary, one secondary, above the series floor.
- The withheld MLPerf Inference v6.0 throughput figure (~2.49M tokens/sec, which
  rests only on secondary reporting) stays out; the piece uses the-decoder for
  framing alone. Correct call, left in place.
- The "misled" example crosses a real boundary and is stated precisely: it is a
  system-scale mismatch (4,216 vs 256 chips) within the same task, not a division
  or category violation, and the draft does not overstate it as one. The
  legitimate same-count generational claim (2.2x at 512 vs 512) is kept distinct
  and named the honest kind. No fair comparison is called unfair, and none the
  reverse.
- The key nuance holds: "None of this is hidden inside MLPerf ... The failure
  happens later." MLPerf mandates disclosure; the fault is the stripped box
  downstream. No company is named as an authority on the benchmark.
- Every href opened through the link-checked proof and every citation lands on
  its owning document; the internal Background and Go-deeper links resolve.

No break required a redraft. The one number I could not tie to an explicit
evidence line is the Division = Closed label on the two MLPerf 2.0 table rows;
the researcher framed that pair as a scale mismatch within comparable rules, and
standard MLPerf Training leaderboard entries are Closed, so the label is
consistent with the argument and with the record. Left as is.

## Reads well

Two sentences went because they narrated the lesson from inside the body, which
the lesson template forbids and none of the three most recent the-instruments
pieces do. "Everything that follows is about when two of those quantities may be
set beside each other" was structural throat-clearing at a paragraph edge; I
deleted it and the paragraph now ends on the concrete thesis-setup. "Comparing
across those labels ... is the failure the rest of this lesson tracks" pointed at
the lesson itself; I rewrote it to the substantive point it was standing in for,
"A comparison that crosses those labels, or drops them, is not one the rules
allow."

The Why-this-matters opener repeated a mold the recent record already ran twice:
tokens-per-second opened "Every model launch and every inference vendor now
leads with a speed number," training-compute opened "Every few months a model
arrives with a headline about its size," and this draft opened "Every few weeks a
chipmaker announces ..." Three in a row is formula. I recast it to "When a
chipmaker says its new accelerator set a record ..." which keeps the content and
breaks the cadence.

I left the body's generic "you" and its arithmetic imperatives ("do the division
a headline would skip," "Put the 106.5-minute figure on a slide"). The voice
guide asks for the division done in the reader's sight, and the published series
uses body second-person freely (HELM nine times), so this is the house register,
not a fault, and I did not introduce a new standard against it. No slop survived
the placeholder test at the section and article edges; the last sentence resolves
the opener's promise (find the two chip counts and do the division) and teaches
nothing the body had not set.

## The experience

The rendered page carries its argument in one table: the top pair differs only in
chip count and compares directly, the bottom pair differs sixteenfold and does
not, so a same-box and a stripped-box comparison sit next to each other rather
than being asserted. The 205.6 / 106.5 = 1.93 division is done in the reader's
sight, exactly the move the voice guide names. What the piece gives beyond its
sources: it puts the headline ratio and the chip-count difference on the same
page and shows the reader the one column that separates a real record from a
misleading one, which none of the rules documents or vendor posts does on its
own. That matches the original-work sentence in the handoff.

## Edits

- Recast the Why-this-matters opener from "Every few weeks a chipmaker
  announces ... and that number almost always comes from an MLPerf submission" to
  "When a chipmaker says its new accelerator set a record, or runs some number of
  times faster than the last one, the figure behind the claim almost always comes
  from an MLPerf submission," to break the recent record's "Every X ..." opener
  mold.
- Deleted "Everything that follows is about when two of those quantities may be
  set beside each other" (body self-narration at a paragraph edge).
- Rewrote "Comparing across those labels, or leaving them off, is the failure the
  rest of this lesson tracks" to "A comparison that crosses those labels, or drops
  them, is not one the rules allow" (removed body self-reference; kept the point).
- Re-ran `nb stamp` (words=1790, reading_minutes=8, sources=11) and the
  link-checked proof: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The argument is right, correctly sourced, and lands the required nuance;
the remaining work was slop and recent-pattern removal, which is done, and the
proof is clean with links.
