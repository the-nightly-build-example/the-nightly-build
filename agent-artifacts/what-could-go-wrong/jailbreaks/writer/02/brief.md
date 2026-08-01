# Writer brief 02 — what-could-go-wrong/jailbreaks (revision)

Load the `writer` skill. Invocation 02, a revision. Reread the voice guide first.
Edit the CURRENT article in place (it carries the editor's 01 surgical cuts —
preserve them). Do not recreate the skeleton.

## Inputs (named)
- Corrected/expanded evidence (authoritative now): `../../researcher/02/evidence.md`
  — see its "Addition (invocation 02) — the marginal-risk / already-public
  steelman" section (sources 14+: Kapoor/Bommasani/Narayanan et al. ICML 2024
  marginal-risk framework; RAND red-team null-uplift, now verified firsthand;
  Soice et al. MIT as the rebuttal; Peppin/Reuel/Casper review as field consensus).
- The editor review that triggered this: `../../editor/01/editorial-review.md`.
- Prior article, voice guide, editorial-direction, commission, .nb-context — as in
  `../01/brief.md`.

## Required fix (the one the editor named) + honest weighing
The "bring it to the present" section must now genuinely steelman the counter-
argument that jailbreak risk is overstated because the harmful information is
already publicly accessible — attributed to a real, developed source (the Kapoor
et al. marginal-risk framework is the clearest general statement; the RAND
red-teamer's own words and the null-uplift result corroborate the empirical side).
Then weigh it, do not just assert it: give the strongest rebuttal (Soice et al. —
the barrier was tacit skill in USING the information, not its existence, and that
is what a model can compress), and land where the evidence actually sits. Keep the
desk's rule: check confidence against proof in BOTH directions (name the gap when
"jailbreaks are catastrophic" outruns evidence AND when "it's basically harmless
because it's all public" outruns evidence).

- Cite the marginal-risk point to its owning primary; where RAND/bioweapon-uplift
  is the anchor, LINK the neighbor lesson what-could-go-wrong/bioweapon-uplift
  rather than re-teaching it (a plain prose link, not a numbered source, per house
  rule on taught ground). Number any genuinely new sources in first-citation order.
- Preserve the sharp DEMONSTRATED vs CONJECTURED line already in the piece; the new
  material is about how much the demonstrated jailbreaks MATTER, not whether they exist.
- Mend any seam the insertion creates. Update `nb-meta` sources/words to true totals.

## Prove and hand off
Run to `BLOCK: 0` (final proof WITH link checking):
`./nb check .nb-work/what-could-go-wrong/jailbreaks/library/what-could-go-wrong/jailbreaks.html --series what-could-go-wrong --repo /home/user/the-nightly-build --library /home/user/library-checkout`
Write `writer/02/draft-handoff.md`: original-work sentence; paths changed; proof
result + warnings left; every editor/researcher request addressed; open questions.

Return exactly one line: `DONE writer .../writer/02/draft-handoff.md`, or a REQUEST line.
