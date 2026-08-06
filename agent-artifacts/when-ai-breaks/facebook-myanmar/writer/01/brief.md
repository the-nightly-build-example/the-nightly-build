# writer brief: when-ai-breaks/facebook-myanmar (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../commission.md — subject, angle, required contribution, boundaries
- ../../writing-coach/01/voice-guide.md — the craft standard (restraint, proportion)
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../library/when-ai-breaks/facebook-myanmar.html — the initialized article to edit (relative to workspace root)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md (and the edited article HTML)

Proof: ./nb check .nb-work/when-ai-breaks/facebook-myanmar/library/when-ai-breaks/facebook-myanmar.html --series when-ai-breaks --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --no-check-links while iterating, then full command with links until BLOCK: 0)

Restraint and proportion (non-negotiable for this piece):
- A mass atrocity is in the record. Write exact and unsentimental; never lurid,
  never minimizing. Carry human stakes through verified fact, not adjectives.
- Responsibility: the Tatmadaw (Myanmar military) bears PRIMARY responsibility; no
  source contests this. Even the plaintiffs plead Facebook as "a substantial
  cause," not the cause. The defensible synthesis the record supports: engagement
  ranking amplified inflammatory content and near-absent Burmese-language
  moderation let it run unchecked, materially widening the reach of a campaign the
  military deliberately drove — a substantial contribution of CONTESTED MAGNITUDE,
  not a measured share and not the primary cause. Write it exactly that way.
- The load-bearing recommender claim ("proactively amplified," Amnesty) rests on
  general Facebook-Papers evidence about how engagement ranking behaves PLUS
  inference — NOT on Myanmar-specific distribution telemetry (which does not exist
  in the record; Facebook told the UN it could not provide country-specific data).
  Present "proactively amplified" as Amnesty's CONCLUSION, not a measured fact.
  What would settle it: Myanmar-specific distribution data plus a counterfactual,
  neither of which exists. Say the uncertainty plainly.
- Human particular: at most one, sourced, in service of the mechanism, with no
  described injury; keep it out of the bookends' register (per the voice guide's
  conservative license). Do not narrate violence.

Decisions the inputs do not carry:
- Strong verified facts to anchor on: the moderation gap (one Burmese-speaking
  reviewer in 2014 → ~60 by Aug 2018 for ~20M users, outsourced to Accenture in
  Kuala Lumpur, no in-country staff); "Facebook is the internet" dominance; the
  UN FFM's exact "useful instrument for those seeking to spread hate" wording
  (para 74) and its attribution of genocidal intent / crimes against humanity to
  the Tatmadaw (paras 87-88); Facebook's own "weren't doing enough... to foment
  division and incite offline violence" admission (Warofka, Nov 2018); the Aug 28
  2018 account/page removals; the ~700,000+ who fled to Bangladesh (UNHCR); the
  Dec 6 2021 Doe v. Meta class action.
- The mechanism to teach: an engagement-optimizing recommender promotes what
  maximizes predicted engagement; outrage/fear reliably drive engagement, so such
  content is systematically amplified absent countermeasures; pair that with
  near-absent local-language moderation and it runs unchecked. Teach engagement
  optimization and moderation-at-scale on the spot or link where taught.
- nb-meta: date 2026-08-06; harness "claude-code-routine"; model set to the model
  you are actually running on. `nb stamp` writes counts.
- Recent habits to break: the headline must be exact and restrained, stating the
  mechanism finding, not performing shock; avoid the "restated X as Y" / count-gap
  molds and the "spent N weeks" opener. Vary headings away from comma-and pairs.
- Link, do not re-teach: microsoft-tay (a chatbot learning from users) and
  ai-overviews (retrieval answers) are distinct prior lessons; link if useful.
  This is feed ranking/recommendation at population scale.
