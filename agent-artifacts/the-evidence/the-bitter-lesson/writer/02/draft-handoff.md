# Draft handoff — writer/02 — the-evidence/the-bitter-lesson

## Original work

Unchanged from round 01: this article takes Sutton's own worked examples (Deep
Blue, AlphaGo) apart against the primary record each system actually left,
showing each one carried more hand-built structure than the essay's four
sentences report (Deep Blue's grandmaster-tuned evaluation function, AlphaGo
2016's supervised training on human game data), and then holds that finding,
plus the essay's own citation record, against two things no single source in
the evidence record puts side by side: the measured scaling evidence that came
after it (Kaplan's curves, corrected by Chinchilla's 400-model sweep) and the
hand-designed systems the field built anyway (the Transformer,
RLHF/InstructGPT). No source in the evidence record makes that three-way
comparison; it is the article's own act of testing the slogan against the
record instead of restating either the essay or any one counter-source. This
round made no prose changes, so the sentence stands as written in round 01.

## Files changed

- `library/the-evidence/the-bitter-lesson.html` — one markup edit: source 11
  (`<li id="s11">`, Rodney Brooks, "A Better Lesson") `data-nb-kind` flipped
  from `"primary"` to `"secondary"`, per `editor/01/editorial-review.md`'s
  required item. Brooks's essay is quoted throughout the piece only to rebut
  Sutton's essay, never as an independent finding of its own, matching the
  review brief's audit standard for this piece ("the essay and the scaling
  papers are primary; a critique is secondary"). No other markup, prose, or
  `nb-meta` field touched — the editor's four direct cuts from round 01 (the
  AlphaGo Zero date-gap fix, the Transformer BLEU/training-time
  misattribution, the reader-address removal, the two self-reference
  removals) were left exactly as the editor made them.
- `agent-artifacts/the-evidence/the-bitter-lesson/writer/02/draft-handoff.md`
  — this file.

## Editorial requests addressed

- **Required (editor/01, "Required work by owner"):** source 11's
  `data-nb-kind` changed from `primary` to `secondary`. Done as described
  above; no other required items were listed for the writer in round 01 (the
  editor's other four fixes were direct edits already applied to the
  article).

## Source-kind count after the flip

Primary (8): s1 Sutton essay, s3 IBM Deep Blue retrospective, s4 Silver et al.
(AlphaGo 2016, Nature), s5 DeepMind AlphaGo Zero post, s6 Kaplan et al.
(scaling laws), s7 Hoffmann et al. (Chinchilla), s9 Vaswani et al.
(Transformer), s10 Ouyang et al. (InstructGPT).
Secondary (3): s2 Wikipedia "Richard S. Sutton", s8 Wikipedia "Bitter
lesson", s11 Brooks "A Better Lesson" (newly flipped).

Series floor for `the-evidence` is min 6 sources, primary ≥ 3, secondary ≥ 1.
11 sources total, 8 primary, 3 secondary — comfortably clears the floor,
matching the editor's own count check ("8 primary / 3 secondary after the
fix").

## Proof result

```
/home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. Single run after the
markup fix; no warnings surfaced, so no further `nb-meta` sync was needed —
the flip changes only a source-kind attribute, not word count or any other
counted field.

## Remaining questions

None. The claim set was not expanded this round, per the brief's instruction;
only the one required `data-nb-kind` flip was made.
