# Draft handoff — writer 01 — the-mechanics/instructions-are-data

## Original work

This article's original act is the reduction itself: it assembles one
illustrative prompt (a system instruction, a user request, and a pasted
message, concatenated in the ChatML format) and uses that single artifact,
never swapped for a second example, to walk three phenomena the evidence
record treats separately — hidden system prompts, jailbreaks, and prompt
injection — down to the one architectural fact (an undifferentiated token
stream with no privileged channel) and the one trained fact (obedience is a
learned tendency, not an enforced rule) that all three instantiate; no single
cited source states that reduction, or builds that example, itself.

## Article and asset paths changed

- `library/the-mechanics/instructions-are-data.html` (edited in place from
  the initialized skeleton; no other assets).

## Proof result

Ran the exact command from the brief:

```
/home/user/the-nightly-build/nb check .nb-work/the-mechanics/instructions-are-data/library/the-mechanics/instructions-are-data.html --series the-mechanics --library /home/user/the-nightly-build/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE` (link checking on, the
default). No warnings intentionally left; the initial draft's `W-LENGTH-HIGH`,
five `W-SENTENCE-DENSITY` findings, one `W-PLACEHOLDER` (an all-caps code-head
label, fixed to lowercase per the existing gallery sample), and `W-SELF-COUNT`
were all fixed by trimming/splitting sentences and setting `nb-meta` `words`/
`reading_minutes` from the final counted total (2180 words, 10 min).

## Editorial requests addressed

None — this is round 1, no prior `editorial-review.md` exists.

## Remaining questions

None outstanding. The evidence record's numeric material (InstructGPT's
85±3% preference figure; Wallace et al.'s 63%/34%; Nasr et al.'s >90%;
Anthropic's Opus 5 vs. Opus 4.8 Gray Swan figures) was used sparingly, only
where the evidence record flagged it as load-bearing or as the steelman/
rebuttal pair for the open section, never as the piece's organizing shape —
the lesson stays qualitative per the brief. The Gemini image-generation
incident (tonight's sibling article) is not mentioned; the piece stayed
strictly architectural and did not need it. No Background link points to
that article, per the brief.
