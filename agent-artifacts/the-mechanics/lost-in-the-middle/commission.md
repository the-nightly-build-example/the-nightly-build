# Commission: the-mechanics/lost-in-the-middle

## The assignment

Explain the "lost in the middle" behavior: give a model a long input and it uses
information placed near the beginning or the end far better than the same
information placed in the middle, so accuracy traces a U as the key fact moves
through the context. This is The Mechanics: start from the visible behavior and
work backward, step by step, to what produces it, marking settled engineering from
open questions. No code.

Selected because it is a concrete, well-documented behavior the reader meets every
time they paste a long document into a chatbot or rely on retrieval, and the
library has not covered it. It is distinct from the behaviors already taught.

## What the lesson must do

- Show the behavior with its demonstration and numbers (Liu et al. 2023, "Lost in
  the Middle: How Language Models Use Long Contexts," TACL): the U-shaped accuracy
  by position of the relevant document, measured on multi-document QA and
  key-value retrieval, present even in models marketed as long-context.
- Work backward to cause, each step a real part of the system: how position enters
  the model at all (positional encoding, taught briefly or linked), how attention
  distributes weight across a long input, and primacy/recency effects tied to how
  training data is structured. Give a small concrete example at each step.
- Reach ground and mark what is settled versus open. Settled: the effect is real,
  reproducible, and not removed merely by advertising a bigger context window.
  Open or debated: the precise mechanism (positional-encoding decay vs attention
  dilution vs training-distribution effects) and how much newer models and
  mitigations reduce it.
- Close where the same weakness lives in systems the reader uses: long-context
  prompting and retrieval-augmented generation, where burying the key passage in
  the middle of many retrieved chunks degrades the answer.

## Boundaries

- One behavior, one mechanism. Distinct from irrelevant-context (distractor
  content hurting, already a lesson) and from the needle-in-a-haystack test (an
  instruments lesson); link irrelevant-context and, for the attention machinery,
  the-mechanics/attention in Background rather than re-teaching them.
- Build only the machinery the explanation needs, in plain words. Assume algebra
  and probability. No code.
- Report the effect at the size the primaries measured; do not overstate ("models
  ignore the middle") or understate it.

## Required contribution

The reader should finish able to explain why where a fact sits in a long prompt
changes whether the model uses it, that this is not fixed by a larger context
window alone, and how to place the important material so a model actually uses it.

## Source obligations

From `nb source-policy --series the-mechanics`: at least 8 sources, at least 4
primary, at least 1 secondary. Primaries center on Liu et al. 2023 and should
include primary work on positional encoding/attention behavior over long inputs
and later evaluations or mitigations. Verify reported effect sizes against the
owning primary; record bounding or contradicting findings.

## Recent habits not to inherit (the-mechanics)

- Headlines are concrete demonstrations, often a paired before/after; a concrete
  demonstration is right for this desk, but do not copy that paired rhythm, and
  keep negative parallelism out of the headline.
- Opening body headings have been a bare instance count or two-clause observation;
  vary how the first heading is built.
- The closing "where it lives now" section is required; do not reuse a recent
  closer's shape.

## Neighboring articles in tonight's edition

Running now, do not overlap: the-evidence/variational-autoencoder, the-instruments/
f1-score, what-could-go-wrong/alignment-faking, when-ai-breaks/hirevue-facial-
analysis. Keep this on the mechanism of one behavior.

## Production record

- Harness: Claude Code (remote). Model for every role: claude-opus-4-8 (capable
  tier; no stage required).
- Effort targets (`nb production-policy --series the-mechanics`): researcher high,
  writer medium, editor high, writing-coach low. Recorded as targets.
- No source or production directive was traded down.
- Note: an earlier commissioning round in this run mistakenly selected already-
  published slugs; this slug was verified absent from the full library first.
