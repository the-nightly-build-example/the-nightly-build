# writer brief: what-could-go-wrong/data-poisoning (01)

Inputs:
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/editorial-direction.md — governing standard, headline standard, press voice, lesson identity, series prompt
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/commission.md — subject, angle, required contribution, boundaries
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writing-coach/01/voice-guide.md — craft standard and licenses (one flat evidentiary temperature; demonstrated-vs-analogy as the spine)
- .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/researcher/01/evidence.md — complete claim set; use its Numbers section exactly
- .nb-work/what-could-go-wrong/data-poisoning/library/what-could-go-wrong/data-poisoning.html — the initialized article to EDIT in place
- .nb-work/what-could-go-wrong/data-poisoning/.nb-context/ — effective contract, runtime assets, furniture catalogs

Output: .nb-work/what-could-go-wrong/data-poisoning/agent-artifacts/what-could-go-wrong/data-poisoning/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/what-could-go-wrong/data-poisoning/library/what-could-go-wrong/data-poisoning.html --series what-could-go-wrong --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same command WITHOUT `--no-check-links` until `BLOCK: 0`.

nb-meta: date `2026-08-08`, harness `claude-code-routine`, model `claude-opus-4-8`;
keep nb-meta `dek` identical to the rendered dekline.

The central discipline (this is the article's spine and the editor's first check):
Do NOT stitch the results into a single "any model could already carry a
safety-surviving 250-document backdoor" claim. That composition is NOT shown, and
the piece exists to draw exactly that line:
- Sleeper Agents installed its backdoor by hand-written supervised fine-tuning with
  a researcher-chosen trigger (not realistic fractional poisoning), and showed it
  survived SFT / RLHF / adversarial training (and that adversarial training can hide
  it).
- Souly et al. (arXiv:2510.07192) showed a backdoor can be installed with a roughly
  constant small count (~250 documents) almost regardless of model/data scale, but
  it was NOT tested through safety post-training and in fact decays under continued
  clean training, and was a narrow/low-stakes trigger at <=13B scale.
- "Easy to install" and "survives safety training" come from DIFFERENT setups and do
  not yet compose. Keep them in separate frames and say so.
- Feasibility cross-check: Carlini et al. (arXiv:2302.10149) "6.5% of Wikipedia" is
  restated by Souly et al. as "~0.27% of DOLMA" — same finding, two denominators;
  do not double-count.

Other precision: some Sleeper Agents per-variant persistence percentages exist only
in figures, not as text; if you quote a precise per-variant figure, verify it before
printing (or state the range the text supports). What has NOT been shown: a
consequential, attacker-inserted backdoor found in a deployed frontier model in the
wild. Name the gap in BOTH directions per the commission. Report labs as sources of
specific results, not authorities.

Recent what-could-go-wrong shapes to break: no "Where the evidence stops and X takes
over" heading mold, no reflexive nb-position/nb-stat-strip; name headings from this
argument's steps. Link (plain prose link) to deceptive-alignment / jailbreaks /
reward-hacking rather than re-teaching them.

This round's focus: the reader can state the poisoning argument at full strength,
separate the controlled insertions from what remains analogy about the wild, and see
why the strongest results do not (yet) compose into the scariest claim.
