# Draft handoff: the-evidence/textbooks-are-all-you-need (writer 01)

## Original-work sentence

This article lifts the phi-1 paper's own Table 3 non-similar column out from
under the paper's "not due to contamination / by a large margin" conclusion,
reads it as the fair test, and joins it to the GPT-3.5/GPT-4 distillation the
paper concedes only later, to state the single claim the paper never makes:
curated data bought phi-1 real efficiency, but not the seventeen-point headline
magnitude, which collapses to about three points and then reverses once the
benchmark-like exercises are pruned.

## Proof result

Full `nb check` (links included) after `nb stamp`: **BLOCK: 0, WARN: 0,
verdict PUBLISHABLE**. Stamp: words=1776, reading_minutes=8, sources=7. No
warnings left intentionally; none were raised. Chart rendered with `nb chart`
and inspected: retrained phi-1 (gold) leads StarCoder-Prompted (blue) at
tau=0.95/0.90/0.85 and trails at tau=0.80, matching Table 3 (32.3/29.0,
36.6/32.4, 34.5/31.0, 27.1/31.2). Em-dash count: 0.

## One interpretive decision worth flagging (not an open question)

The seventeen-point headline gap is phi-1 (50.6%) over base StarCoder (33.6%)
from Table 1; the paper's decontamination test in Table 3 compares the retrained
phi-1 against StarCoder-Prompted (the stronger variant). The two are different
StarCoder configurations. I named this explicitly in the pruning-test section
("StarCoder-Prompted, the same StarCoder run with a coaching prompt") so the
figure, the caption, and the prose all use the same baseline the paper used for
that comparison, and the "three points rather than seventeen" line is a
deliberate before/after of the paper's own two honest comparisons, not a single
matched pair. If the editor prefers a strict like-for-like, the alternative is
to state both StarCoder rows in Table 1 and hold the non-similar comparison to
StarCoder-Prompted throughout; I judged the current framing clearer for a new
reader without losing accuracy.

## Scope discipline held

GSM1k and Maini are presented only as scrutiny of later phi models
(phi-1.5/2/3), explicitly kept off phi-1's HumanEval result, which rests on the
paper's own Table 3. The contamination discussion stays inside phi-1's own
pipeline; it does not generalize into a benchmark-contamination essay. Schaeffer's
satire is offered as Go-deeper reading only, not cited in the body. The desk's
recent "the paper got its own explanation wrong" reveal is remade in phi-1's
particulars (overall retrained score vs the non-similar subset) rather than that
stock framing.

## Open evidence or voice questions

None blocking. Every body claim draws on the evidence record; no fact was needed
that the record did not carry.
