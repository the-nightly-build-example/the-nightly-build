# writer brief: the-evidence/constitutional-ai (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — house standard, paper
  voice, series prompt, lesson template identity
- commission.md (../../commission.md) — the document, angle, required contribution,
  boundaries, continuity
- voice-guide.md (../../writing-coach/01/voice-guide.md) — how this piece sounds
- evidence.md (../../researcher/01/evidence.md) — the verified claim set; your only
  source of facts
- the initialized article: ../../../../library/the-evidence/constitutional-ai.html
  (edit in place; keep skeleton, engine assets, required labels)
- the effective template contract and furniture under ../../../../.nb-context/

Output: draft-handoff.md (this directory)

Proof: /home/user/the-nightly-build/nb check
  /home/user/the-nightly-build/.nb-work/the-evidence/constitutional-ai/library/the-evidence/constitutional-ai.html
  --series the-evidence --library /home/user/library-checkout
  (iterate with --no-check-links; run nb stamp then the full check, links included,
  until BLOCK: 0)

Honor these decisions from the evidence and commission:

- State results DIRECTIONALLY, not as hard scores. The CAI paper reports no
  absolute Elo numbers; its headline result is a preference margin read off charts
  from a modest crowdworker sample (about 10,274 helpfulness and 8,135 harmlessness
  comparisons across snapshots of one lab's 52B models). The honest claim is that
  RL-CAI was preferred and less harmful at a given helpfulness, not a quoted
  "score." Report the scale exactly as the evidence gives it.
- The sizing IS the article's original work: preference modeling on one lab's
  models, aimed at harmlessness — not a governance mechanism and not a general
  proof that AI judgment equals human judgment. Make that visible.
- Carry the real tensions the evidence records: (1) the 2022 paper did not directly
  compare human vs AI feedback efficacy (Google/Lee et al. state this); (2) RLAIF
  can match RLHF using a plain labeler preamble rather than a written constitution,
  which cuts against loose talk of a model "having a constitution" doing the work;
  (3) the AI-feedback labeler reached human-feedback parity only by extrapolation
  above 52B. Weigh these; don't bury them.
- Show one or two constitution principles verbatim as the evidence quotes them, so
  the reader sees what "a principle" is. Note the paper's own admission that
  principles were "selected in an ad hoc manner for research purposes."
- RLHF/preference models/reward models are taught: link the-evidence/
  direct-preference-optimization, /instructgpt, /deep-rl-from-human-preferences in
  Background rather than re-teaching. One document only.
- Anthropic and Google appear as authors of documents, reported as fact; cite no
  company as an authority on whether the method is good.

Recent shapes to break (see commission for full list): avoid the two-clause
", and"-twist dek and the comma-triad dek; don't default to a negative-fact
headline or a trailing second clause; vary the closing present-day heading away
from "Where X still Y."

This round's focus: teach the two stages and the constitution concretely, size the
evidence honestly, and land the present-day tension between the 2022 result and how
"constitution"/RLAIF are talked about now.
