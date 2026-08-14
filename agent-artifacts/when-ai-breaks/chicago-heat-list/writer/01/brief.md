# writer brief: when-ai-breaks/chicago-heat-list (01)

Inputs (under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars.
- `researcher/01/evidence.md` — the complete claim set. Draft only from it.
- Article to edit: `.nb-work/when-ai-breaks/chicago-heat-list/library/when-ai-breaks/chicago-heat-list.html` (initialized from the lesson template).
- Template context: `.nb-work/when-ai-breaks/chicago-heat-list/.nb-context/`.

Output: `.nb-work/when-ai-breaks/chicago-heat-list/agent-artifacts/when-ai-breaks/chicago-heat-list/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/when-ai-breaks/chicago-heat-list/library/when-ai-breaks/chicago-heat-list.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/4555dd06-1325-5643-8ae1-70035fc82956/scratchpad/library-checkout`
(Use `--no-check-links` while iterating; run the full command, links included, until `BLOCK: 0`. Run `nb stamp` before the final check.)

Guardrails from the evidence record (the record's Contradictions section is load-bearing here):
- The "where it lives today" close is anchored on the EU AI Act Article 5(1)(d) prohibition of this class (in force 2 Feb 2025), not on a named, verified live US deployment. Write the present-tense hook as how this class of system is now treated and where the same weakness recurs, not as a claim about a specific current program, unless the record separately sources a live one.
- Do not flatten the lesson into "this class of system cannot work." RAND declined to call the null result theory failure versus implementation failure, found no violent backfire, allowed the pilot may have identified more perpetrators, and noted later model versions improved. Report the null result precisely (no change in a listed person's chance of being shot; higher chance of arrest) and keep RAND's hedges.
- The racial-disparity claim is owned by the released dataset and outside analysis, not by the OIG (whose findings are about reliability and process). Attribute the disparity to the data/analysis that owns it; attribute reliability and punitive-intervention findings to the OIG.

Angle: tell it in order — what the Strategic Subject List was built to do, what it did, who it affected, what CPD did afterward, with names and dates (Miles Wernick / Illinois Institute of Technology; RAND's Saunders, Hunt, Hollywood, 2016; Chicago OIG, Jan 2020; ~400,000 scored). Then teach why this kind of system fails: arrest-based training data learns policing, not crime (proxy label and feedback loop); a risk score with no effective help becomes a reason for more police contact; a low base rate makes most flags wrong. Link when-ai-breaks/compas-recidivism and when-ai-breaks/optum-health-algorithm where they already taught proxy labels and base rates, and build on them rather than re-teaching from scratch.

Recent when-ai-breaks habits not to inherit:
- rite-aid-facial-recognition ("mostly flagged the innocent," base rate) and optum-health-algorithm ("did exactly what it was built to do," proxy label) are recent and share this piece's mechanisms. Lead with the SSL's own particulars — no effective intervention and a self-confirming feedback loop — and link the earlier base-rate/proxy-label lessons instead of restating them. Do not echo those deks' framings.
- Distinct from robodebt (automated debts) and compas (court risk score): this is predictive policing that ranks individuals for police attention.
- Vary dek and heading construction; recent when-ai-breaks deks are plain "system did X, and Y" comma-and sentences. Build this dek in the SSL's own nouns.

Original work: name in one sentence, in draft-handoff.md, what this article does to the evidence that the evidence does not do itself.
