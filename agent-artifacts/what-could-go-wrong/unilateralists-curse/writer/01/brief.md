# writer brief: what-could-go-wrong/unilateralists-curse (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Voice guide: ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- Evidence record: ../../researcher/01/evidence.md — your complete claim set (add no facts it lacks). Read its Contradictions/limitation notes.
- The initialized article: ../../../../library/what-could-go-wrong/unilateralists-curse.html (edit; do not recreate the skeleton).
- Template context: ../../../../.nb-context/ — effective contract, furniture catalogs, runtime assets.

Output: ./draft-handoff.md (writer/01/draft-handoff.md)

Proof: run from repo root /home/user/the-nightly-build —
`./nb check .nb-work/what-could-go-wrong/unilateralists-curse/library/what-could-go-wrong/unilateralists-curse.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`
New slug; no `--revision`. Use `--no-check-links` while iterating; run it links-on until `BLOCK: 0`.

## Recent patterns to break (what-could-go-wrong tics)

- Dek: do NOT close on a deflating comma-and caveat ("Finding, and [the catch]").
- Headings: avoid "The [noun] that/where [clause]," "The strongest [case/push]
  for X," and the wh-reckoning heading.
- Opener: avoid the "In [Month Year], [named researcher] described..." opener and
  the "Everyone agrees..." consensus opener.
- Closer: avoid ending on "does not exist yet"/"has been shown, so far" plus a
  numbered-questions close.
- Required distinction, fresh words: draw the shown-vs-analogy line (the beat),
  but avoid the stock phrasings "the line between shown and projected," "the
  strongest [case/demonstration]," "Alarm and dismissal sit at the same distance,"
  "the gap is symmetric," "runs ahead of its evidence."
- Cross-series: no "By the end you will be able to..."; no "The next time..., ask"
  close; "shown vs projected" as a set phrase; "honest" as a virtue word.

## Decisions the inputs may not settle (from the researcher's report)

- **The single most important guardrail.** The explicit, NAMED invocation of "the
  unilateralist's curse" is thin in the primary AI-governance release literature.
  Shevlane & Dafoe (2020), Seger et al. (GovAI 2023), Brundage's "Malicious Use"
  report, OpenAI's GPT-2 release report, and the 2025 International AI Safety
  Report all reason in the curse's STRUCTURE (counterfactual possession,
  independent discovery, unilateral release, the value of coordination) but do
  NOT use the label. Do NOT claim governance authorities routinely invoke "the
  curse" by name for current model releases. The clearest named AI application is
  from a critic (Armstrong) and, as a citation, Bostrom's 2017 openness paper.
  (An automated fetch fabricated a Shevlane-Dafoe quote using the phrase; it does
  not appear — do not reproduce any such quote.)
- **Draw the shown-vs-analogy line thus:** what is proven is a decision-theoretic
  result that holds under specific assumptions (independent actors, a shared
  common-good payoff, private symmetric errors, naive non-strategic agents).
  Calling any particular open-weight release "the unilateralist's curse" is an
  analogy that imports assumptions real releases violate — commercial rather than
  purely altruistic motives, correlated rather than independent errors, and
  communication and coordination that are actually present. Do NOT present any
  specific release as a proven instance; present it as a structural analogy.
- **Figures from the paper** (use the record's exact values): near a true value of
  -1, five independent actors act with about a 50% chance; the group passes a 50%
  chance of acting at four actors; the individually optimal caution threshold
  rises toward 1 as actors are added. Use the paper's own numbers and scope.
- **Real-system instances to ground it** (as analogy, not proof): Meta's open-
  weight Llama 2 (18 Jul 2023) and Llama 3.1 405B (23 Jul 2024) with Zuckerberg's
  stated reasoning; the GPT-2 staged withhold (Feb 2019) undercut by an
  independent OpenGPT-2 replication (Aug 2019) before OpenAI's own Nov 2019
  release.
- **The strongest objection** (the beat requires it): Stuart Armstrong's 2016
  reply grants the result is true but argues existing institutions and
  coordination already manage it and that the remedy can license a heckler's veto
  or excessive caution; and the paper's own meta-rationality/Discussion and its
  Ellsberg/mavericks counter-case. Give this its due.
- Link, do not re-argue: `what-could-go-wrong/racing-dynamics` (distinguish:
  rivalry vs independent-actor statistics), `.../vulnerable-world-hypothesis`.
