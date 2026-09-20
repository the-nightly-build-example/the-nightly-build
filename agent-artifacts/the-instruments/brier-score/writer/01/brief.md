# writer brief: the-instruments/brier-score (01)

Inputs:
- ../../commission.md — assignment: how the Brier score is made, what it bundles/
  hides, a real misled case, boundaries, habits to break.
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only what it opened; Numbers section used exactly.
- article to edit: /home/user/the-nightly-build/.nb-work/the-instruments/brier-score/library/the-instruments/brier-score.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/brier-score/.nb-context/

Output: ./draft-handoff.md

Proof (from repo root /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/the-instruments/brier-score/library/the-instruments/brier-score.html --series the-instruments --library .nb-work/library
Run ./nb stamp before the final check.

This round's focus and decisions the inputs do not settle:
- Source caveats the researcher flagged: Murphy's (1973) decomposition is sourced
  one remove via Ferro & Fricker (2012), which reproduces his equations — cite it
  as the record does, not Murphy's gated original. Brier (1950) was read directly
  (Internet Archive scan) — cite it. The platform-methodology source is Good
  Judgment Open's FAQ (Metaculus's was gated).
- Use the genuine SECOND comparability trap the record surfaced: Good Judgment
  Open scores on Brier's original two-term 0-to-2 scale, while Halawi et al. and
  ForecastBench use the one-term 0-to-1 scale — so two numbers both called "Brier
  score" can differ by a factor of two before any question-set difference. This
  directly supports the anchor (a Brier comparison means nothing until you know the
  questions AND the convention). Use it, but keep the lesson focused — it is a
  sharp second trap, not a licence to catalogue every convention. The editor will
  judge if it earns its space.
- Keep the anchor foregrounded: a Brier score can be gamed by predicting the base
  rate or by an easier question set, so "our model beats humans" means nothing
  until the questions are the same, the convention is the same, and the model
  actually moved off the base rate.
- One worked numeric example carries the definition; keep the Murphy decomposition
  (reliability/resolution/uncertainty) in plain words, no algebra. Contrast by link
  with the published calibration-error (ECE) and auroc lessons — do not re-teach
  them. Confirm library URLs via a specific ./nb history query if needed. No code.
- Break the recent Instruments habits the commission lists (the "By the end you
  will know..." opener; two-part-balance takeaway; the "Reading X as Y" closer;
  "How a X becomes a Y" headings). Outline the reasoning before naming sections.

nb-meta fields to fill: "date": "2026-09-20"; "harness": "claude-code"; "model":
your exact running model ID (capable-tier this run; if unknown use
"claude-sonnet-4-5"); "tags": 3-5 concrete topical tags; "dek": identical to the
rendered dekline. ./nb stamp writes counts.

Do not tour the repository or expand the claim set. If a needed fact is missing,
return a precise researcher request. Report the draft-handoff path, the
original-work sentence, the final BLOCK count, and any gap.
