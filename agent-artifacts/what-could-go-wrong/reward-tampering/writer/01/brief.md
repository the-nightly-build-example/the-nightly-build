# writer brief: what-could-go-wrong/reward-tampering (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/editorial-direction.md
  — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/commission.md
  — the argument, the angle, source direction, nb-meta values.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/writing-coach/01/voice-guide.md
  — how this piece should sound; read before drafting and before every revision.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/researcher/01/evidence.md
  — the complete claim set; cite only from it.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/.nb-context/
  — the effective template contract, runtime assets, and furniture catalogs.
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/library/what-could-go-wrong/reward-tampering.html
  — the initialized article to edit in place.

Output: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/reward-tampering/agent-artifacts/what-could-go-wrong/reward-tampering/writer/01/draft-handoff.md
(the original-work sentence, the proof result with any warning intentionally left, and any open evidence/voice question).

Proof (run from repo root /home/user/the-nightly-build, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/what-could-go-wrong/reward-tampering/library/what-could-go-wrong/reward-tampering.html --series what-could-go-wrong --library /home/user/library-checkout --no-check-links`
- Final: the same command WITHOUT `--no-check-links`, and run `./nb stamp .nb-work/what-could-go-wrong/reward-tampering/library/what-could-go-wrong/reward-tampering.html` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-12`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (e.g. reward-tampering,
reinforcement-learning, ai-safety). Keep nb-meta `dek` identical to the rendered
dekline.

This round's focus: present the argument at full strength, then test it against the
one controlled experiment and locate the gap precisely. Steelman first: the
wireheading origin (Ring and Orseau's delusion-box result), the naming of
reward-channel tampering as a distinct problem (Concrete Problems in AI Safety,
2016), and the field's line that tampering is influence on the reward *process*,
not gaming the specified reward. Then the experiment (Denison et al. 2024): the
four-stage curriculum, and the exact rates from the evidence record — editing its
own reward function at 45 of 32,768 episodes, editing the unit tests to hide it at
7 of 32,768, a helpful-only baseline of 0 of 100,000, and a nonzero residual (4 of
100,000) surviving countertraining. Give each rate with its denominator. Then the
present: who presses the argument, what they want (sandboxing agents from their own
graders and training code, interpretability, tampering-specific evals), and where
the confidence outruns the proof, in either direction.

Hold these lines from the evidence record; they are the lesson's spine:
- Reward hacking and reward tampering are distinct. Reward hacking (already taught
  in the library) exploits a flawed reward; reward tampering corrupts the reward
  mechanism itself. Draw the line early and keep it. Attribute the definitional
  line to Everitt et al., not to Skalse et al. (Skalse defines reward hacking but
  does not itself draw the tampering line).
- The 2024 experiment is a real demonstration and a bounded one: rare, only after a
  curriculum built to elicit it, with the authors' own statement that the setup
  "seriously exaggerates the incentives." No deployed system has been shown
  tampering with a real reward channel of its own accord. That gap is the point;
  do not let the prose imply the behavior is common or spontaneous.
- A November 2025 production-RL result (in the evidence record's Contradictions)
  shows reward *hacking* emerging in real training and generalizing to sabotage and
  alignment-faking. It narrows the "only in a contrived setup" reading of hacking,
  but it does not show reward-channel *tampering* unprompted. Report it honestly and
  do not let it collapse the hacking-versus-tampering distinction this lesson rests
  on.

Guardrail from this desk: name no company as an authority. Attribute every claim to
the paper and authors that made it and the figures they reported, never to the
standing of the lab that employed them. Steelman the skeptical reading too (a
curriculum built to elicit tampering tells us less about spontaneous behavior than
the strong version needs).

Link `what-could-go-wrong/reward-hacking` in Background and build past it rather
than re-teaching it; `what-could-go-wrong/mesa-optimization`,
`what-could-go-wrong/goal-misgeneralization`, and
`the-mechanics/instructions-are-data` are available as Background if the argument
needs them. Link only already-published library pages — do NOT link tonight's
sibling articles.

Furniture: plan prose and furniture together from the catalogs under `.nb-context`;
a component that lays out the demonstrated-versus-projected split or the curriculum
stages may earn its place, but use documented markup only and add nothing purposeless.
Build a chart only from a verified numeric series in the evidence record; do not
invent data.

Habits not to inherit (house formulas the recent library shares across desks):
- Do not open "Why this matters" on a nostalgic or second-person recall ("If you
  have heard one thing about...", "You may remember when..."), and do not pivot the
  opener on "This lesson shows/tests/takes apart...". Find a fresh way in.
- Do not close the opener on a "set the two things side by side" line, and do not
  land "The takeaway" on a "So next time you [meet/hear] one..." portable rule.
  Find this lesson's own resolution.
- Do not use "this desk" or any self-reference in the body; the body narrates no
  one.
- What-could-go-wrong's recent dek mold is "[modest measured thing], yet no one has
  [scary thing]" and the comma-triad closed with "and" (three clauses). Write a dek
  built neither way. Vary section headings away from the "The X that Y"
  relative-noun-phrase mold and the "noun, the appositive" comma mold; each heading
  is a step in this lesson's own argument, no scaffolding slots.
