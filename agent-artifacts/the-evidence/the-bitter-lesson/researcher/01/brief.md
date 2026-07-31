# Brief 01 — researcher — the-evidence/the-bitter-lesson

## Begin with these inputs only
- `agent-artifacts/the-evidence/the-bitter-lesson/editorial-direction.md`
- `agent-artifacts/the-evidence/the-bitter-lesson/commission.md` (carries the
  document, the angle, the required contribution, the source obligations, and the
  named starting sources)

Do not browse the repository or archive as background. `nb` is at
`/home/user/the-nightly-build/nb`; `nb history --library /home/user/the-nightly-build/library-checkout`
is available for a specific continuity question only.

## Task
Follow the **researcher** skill (Skill tool: `researcher`). Produce the evidence
record the writer and editor will use.

- Read **The Bitter Lesson** essay in full (incompleteideas.net) — it is short;
  capture Sutton's exact wording, the examples he gives, and his stated cause.
  Verify the date (13 March 2019) and Sutton's exact title/affiliation.
- Read the measured scaling evidence the lesson weighs the essay against: Kaplan et
  al. 2020 (arXiv 2001.08361) and Hoffmann et al. 2022 / Chinchilla
  (arXiv 2203.15556). Pull the specific findings that refine "just add compute."
- Read the primary for Sutton's headline examples where the argument leans on them
  (AlphaGo / AlphaGo Zero Nature papers; the Deep Blue record).
- **Contradiction hunting is required:** read at least one substantive critique
  (Rodney Brooks, "A Better Lesson," 2019, rodneybrooks.com) and gather the concrete
  counter-evidence that human-designed structure mattered (the transformer
  architecture itself; RLHF/instruction tuning; data curation / "textbooks"-style
  data-quality results). Also assemble the strongest steelman of the essay.
- Classify every source primary/secondary with a reason (authorship and stake).
- Verify every quoted number/word against the owning primary; never record an
  unverified URL (a 403/paywall is gated — try a real browser fetch).

## Source policy to meet
min 6 sources; **primary ≥ 3, secondary ≥ 1** (aim higher on primary).

## Output (write only this)
`agent-artifacts/the-evidence/the-bitter-lesson/researcher/01/evidence.md` with the
skill's stable sections (opening strong/thin paragraph, Sources, Contradictions,
Numbers, Source assets, Discarded). Return `DONE researcher <path>` (or
`BLOCKED`/`REQUEST` per the skill).
