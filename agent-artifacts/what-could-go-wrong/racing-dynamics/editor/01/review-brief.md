# Editor review-brief: what-could-go-wrong/racing-dynamics (round 01)

## Inputs (begin here; read the voice guide first)
- This brief.
- Editorial direction: `../../editorial-direction.md`
- The EXACT writer brief (leak detection): `../../writer/01/brief.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`
- Draft handoff (open original-work sentence at third read):
  `../../writer/01/draft-handoff.md`
- Article: `/home/user/the-nightly-build/.nb-work/what-could-go-wrong/racing-dynamics/library/what-could-go-wrong/racing-dynamics.html`
- Template context: `.../racing-dynamics/.nb-context/`

Three ordered reads (skeptic, cut, reader); surgical edits only.

## Points to test hardest (skeptic read)
- **The model, faithfully.** Verify the setup and both results against the
  evidence: competition drives equilibrium safety down; as capability's
  importance → 0 the equilibrium is zero safety; the information result (no
  information safest, public information most dangerous) with the correct
  mechanism (private: a team cuts corners only when it knows its own capability
  is low; public: the leader cuts corners whenever the runner-up is close).
  Check the `nb-math` equation s = µ/(en) and the µ/2 two-team/enmity-1 case.
- **Report vs model-claim vs synthesis kept distinct.** The equilibria are
  if-then claims *inside the model*, not facts about the world. Flag any sentence
  that lets the model's conclusion read as established reality.
- **The assumption audit (the original work).** Confirm each premise is marked
  holds / unproven / contradicted against the record: the winner-take-all /
  durable first-mover assumption is the weak one (Epoch: gaps close in months —
  7-month avg US–China, ~4-month o1→R1). Verify these numbers against evidence.
- **Neutrality.** The desk takes no side. Flag any sentence that tips into doom
  or into dismissal rather than weighing. "Confidence outruns proof on both
  sides" should be shown, not just asserted.
- **The FT "days" claim** must be labeled second-hand/single-origin, with METR's
  three weeks as the verified datapoint. Confirm they are never conflated.
- **No company as authority.** OpenAI's framework, Seoul commitments, FLI letter
  = what a party said/asked, not proof. Karnofsky = Carnegie visiting scholar
  (2024), not speaking for a company.
- **The information result's open status.** It must read as the model's claim
  with no technical rebuttal found, robustness untested — not settled.
- Audit `data-nb-kind` labels; verify display text (headline, dek, subheads) as
  claims and as labels (names, dates, numbers).

## Cut read — banned terms are a hard gate here
- Verify by search that **"AI race" / "artificial intelligence race" appear zero
  times outside the Sources section** (two source titles legitimately contain the
  phrase and are exempt). Also confirm zero "load-bearing", "machinery",
  em-dashes ≤4, leverage ≤1. If any banned string is in body/heading/dek, it
  must be rewritten (return to writer if it needs new prose).
- Cut self-grading, signposts, stock revelation frames, prompt leakage (compare
  against the writer brief). Watch for the jailbreaks "teaches a pattern, not a
  boundary" mold and comma-triad headings/deks; compare against recent library.

## Reader read
One sentence on what the piece gives beyond its sources; compare with the
draft-handoff's original-work sentence (the assumption audit). Judge voice
against the exemplars. Retest the headline as the largest claim.

## Furniture
Inspect the `nb-table` of the three information regimes and the `nb-math`
equation: each must have a clear communicative purpose and be accurate to the
evidence. Request corrections through the writer; do not edit markup yourself.

## Output
Write `../../editor/01/editorial-review.md` with the three required lines, direct
edits made, required work by owner, and the decision. Return `DONE editor <path>`
only if no redraft is required; otherwise `REQUEST writer/researcher <need>`. Do
not run the proof; the writer reruns it on any revision.
