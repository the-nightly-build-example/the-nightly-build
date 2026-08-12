# writer brief: the-evidence/grokking (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/editorial-direction.md
  — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/commission.md
  — the document, the angle, source direction, nb-meta values.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/writing-coach/01/voice-guide.md
  — how this piece should sound; read before drafting and before every revision.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/researcher/01/evidence.md
  — the complete claim set; cite only from it.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/.nb-context/
  — the effective template contract, runtime assets, and furniture catalogs.
- /home/user/the-nightly-build/.nb-work/the-evidence/grokking/library/the-evidence/grokking.html
  — the initialized article to edit in place.

Output: /home/user/the-nightly-build/.nb-work/the-evidence/grokking/agent-artifacts/the-evidence/grokking/writer/01/draft-handoff.md
(the original-work sentence, the proof result with any warning intentionally left, and any open evidence/voice question).

Proof (run from repo root /home/user/the-nightly-build, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-evidence/grokking/library/the-evidence/grokking.html --series the-evidence --library /home/user/library-checkout --no-check-links`
- Final: the same command WITHOUT `--no-check-links`, and run `./nb stamp .nb-work/the-evidence/grokking/library/the-evidence/grokking.html` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-12`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (e.g. grokking, generalization,
weight-decay). Keep nb-meta `dek` identical to the rendered dekline.

This round's focus: hold a real, small result apart from the large claim it is
cited for. Teach what the paper actually did with honest scale (the ~400k-parameter
2-layer transformer, binary operation tables over 97 elements, the headline
division-mod-97 run at 50% training data, AdamW with weight decay, train accuracy
near-perfect below ~10^3 steps while validation reaches it only near ~10^6 steps),
then what later work established (the reverse-engineered modular-addition circuit
and the progress measures; weight decay driving the transition). Then bring it to
the present: how "grokking" is invoked for large-model improvement and what the
evidence actually licenses.

Handle these from the evidence record precisely:
- The author line is Power, Burda, Edwards, Babuschkin, Misra (OpenAI, 2022). It is
  Burda, not "Burns"; the commission had it wrong. Use the evidence record's names.
- The "sudden" jump is sudden in the watched test-accuracy curve; the generalizing
  circuit forms gradually beneath it on the progress measures. Keep that
  distinction alive; do not call generalization literally instantaneous.
- Weight decay's role: the original paper calls it "most effective," Nanda et al.
  call it "necessary." Cite whichever owns the exact wording you use; do not merge
  them into a stronger claim than either makes.
- The 2025 result on a 7B mixture-of-experts model (in the evidence record's
  Contradictions) both widens grokking's reach beyond toy scale and reframes it as
  local, asynchronous, per-domain delayed generalization detected by internal
  proxies, explicitly contrasted with the toy setting's single global jump. Weigh
  it honestly: it is a separate 2025 finding, not something the 2022 paper's scale
  can carry, and it cuts against the "sudden unlock" shorthand rather than for it.
  Do not let it turn the lesson into a claim that big models simply "grok."
- No digitized accuracy-versus-steps series exists for a chart; the curves live
  only in the figures. Do not invent chart data. Landmark step/accuracy points from
  the Numbers section can be stated in prose.

Link `the-evidence/emergent-abilities`, `the-evidence/emergence-loss-perspective`,
and `the-mechanics/memorization` in Background rather than re-teaching overfitting,
generalization, emergence, or memorization; `the-evidence/scaling-laws-kaplan` is
available if the present-day framing needs it. Link only already-published library
pages — do NOT link tonight's sibling articles.

Furniture: plan prose and furniture together from the catalogs under `.nb-context`;
add only components that earn their place with documented markup.

Habits not to inherit (house formulas the recent library shares across desks):
- Do not open "Why this matters" on a nostalgic or second-person recall ("If you
  have heard one thing about...", "You may remember when..."), and do not pivot the
  opener on "This lesson reads/shows/takes apart...". Find a fresh way in.
- Do not close the opener on a "set the measured result and the famous story side
  by side" line, and do not land "The takeaway" on a "So when someone tells you
  X..." portable rebuttal. Find this lesson's own resolution.
- Do not use "this desk" or any self-reference in the body; the body narrates no
  one.
- The-evidence recent dek mold is the concessive reversal: "[names] reported X in
  [year], and later analyses found Y" (a second clause that reverses the first).
  Write a dek that is not built on a reversing second clause. Vary section headings
  away from the "The X that Y" relative-noun-phrase mold and the "noun, the
  appositive" comma mold; each heading is a step in this lesson's own nouns.
