# Draft handoff: the-mechanics/familiar-pattern-override (writer 01)

## Original-work sentence

The article turns eight separate measurements (AIW's per-model p-values,
PHANTOM RECALL's 149-puzzle table and Thinking/Non-Thinking deltas, Jang's two
worked overrides, Razeghi's and McCoy's frequency numbers, Wu's coordinate
figures) into one causal chain no single source states end to end: training
frequency sets a high prior on a puzzle's canonical answer, surface similarity
to the memorized template is what lets that prior outvote a changed premise,
and — against the commission's original framing — the record shows this is
*not* cleanly fixed by reasoning training, since Jang's own reasoning-trained
model overrides the stated condition more than its base model does on the same
prompt.

## Proof result

`./nb stamp` then `./nb check .nb-work/the-mechanics/familiar-pattern-override/library/the-mechanics/familiar-pattern-override.html --series the-mechanics --library .nb-work/library` (links included, default link-checking on):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

2199 words, 8 sources (7 primary, 1 secondary — Nezhurina/AIW, Mukhopadhyay/PHANTOM
RECALL, Jang, Razeghi, McCoy, Wu, Arkoudas primary; Open Thoughts secondary),
10 min read. No warnings left outstanding.

## This round's corrections, resolved

- Anchor: dropped "fades on obscure puzzles" as a measured claim. The
  training-prior section states it explicitly as an inference from Razeghi's
  and McCoy's frequency numbers, not a separately measured result, and says so
  twice (in the body and implicitly by never citing a puzzle-fame study,
  because none exists in the record).
- Open question: presents the reasoning-training question as genuinely mixed,
  not partly fixed. Cites PHANTOM RECALL's own Thinking-mode gains (+30.2 /
  +10.1 / +8.0) alongside its authors' "narrow and model-specific" /
  "persists across all systems" language, AIW's o1-preview-vs-o1-mini split
  inside one lineage, and Jang's rabbit/Tower-of-Hanoi examples where the
  reasoning-trained model overrides *more* than its base model. Jang's Tables
  2–3 are not cited; only the prose claims and Figure 1 worked examples are
  used, per the evidence record's caveat.
- Mechanism kept as the spine (training prior + surface similarity), marked
  settled; what it proves about reasoning and whether training fixes it
  marked open, under a heading built from this behavior's own nouns ("More
  reasoning training does not reliably beat the override"), not a stock
  reasoning-boundary heading.
- Distinct from irrelevant-context, memorization, and prompt-sensitivity: each
  is named and linked once, with the specific difference stated, not
  re-taught. Library URLs confirmed by reading the three published articles
  directly (same-series relative paths), not via `nb history`.
- Recent-pattern habits avoided: no "by the end you will know" triad, no
  two-part balance closer, no reused stock headings, no comma-triad/
  comma-splice dek, no article-authored scripts or styles, no code.

## Evidence/voice gaps

None outstanding. One deliberate compression: Wu et al.'s three coordinate-
convention figures (62%/71%/75%) are given as a range ("between 62% and 75%")
rather than all three values, to fit the lesson's word band; the range is
accurate to the Numbers section, not invented.
