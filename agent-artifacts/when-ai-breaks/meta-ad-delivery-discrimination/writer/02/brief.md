# writer brief: when-ai-breaks/meta-ad-delivery-discrimination (02, revision)

Inputs:
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/editor/01/editorial-review.md` — apply every required item; the editor's direct edits are already in the article
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/editorial-direction.md`
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/writing-coach/01/voice-guide.md`
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/researcher/01/evidence.md`
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/commission.md`
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html` — the editor-edited article to revise in place
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/.nb-context/`

Output: `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/writer/02/draft-handoff.md`

Proof: `./nb check .nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links`; final with links to `BLOCK: 0`.)

The required item (editor-routed): the VRS-audit stat strip and the
"36 paired campaigns" sentence state figures the primary does not support.
Re-read the cited independent-audit primary (Imana, Shen, Heidemann, Korolova,
FAccT '25), specifically its sections 4.1.1 and 4.2.1 and Figure 3, and correct
them to what the paper says. The editor's read of the primary found: at the 10%
compliance threshold, race variance went from 0 of 18 (without the remediation)
to 18 of 18 (with it); the 15-of-18 figure is the stricter 5%-threshold race pass
count; for gender, 15 of 18 already passed without the remediation; and all 36
paired experiments are housing-declared, with the employment/credit comparison a
separate, smaller test. Verify each against the paper yourself before writing it,
correct the stat strip and the sentence so they no longer conflate thresholds or
categories, and keep the ending's honest "reduced, not fixed" nuance intact.
Preserve all settled work and the editor's direct edits; change only what the
review requires and what logically follows. Do not expand the claim set. Rerun the
full proof and update nb-meta counts with nb stamp if wording changes shift them.
