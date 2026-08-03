# Commission: when-ai-breaks/amazon-hiring-tool

## Assignment
Teach one real AI failure: Amazon's experimental resume-screening engine, built
from around 2014 and scrapped by 2018 after it learned to penalize resumes that
signaled the applicant was a woman. This is the when-ai-breaks desk: tell what
happened in order (what it was built to do, what it actually did, who it
affected, what the operator did afterward), then explain why that kind of system
fails that way, then close with where the same weakness lives today in systems
the reader actually uses.

## What happened (in order)
Amazon built machine-learning models to score applicants' resumes 1–5 stars,
trained on the company's own hiring decisions over roughly a decade. Because
that historical data reflected a male-dominated applicant pool and set of hires,
the model learned to down-rank resumes containing signals correlated with women
(the word "women's," as in "women's chess club captain"; some all-women's
colleges). Amazon engineers tried to neutralize those specific terms but could
not guarantee the model would not find other proxies, and the team's ratings
were never the sole basis for hiring. Amazon disbanded the effort by 2018. The
account is Reuters' 2018 report sourced to people who worked on it, later
acknowledged in outline by Amazon.

## Why it fails that way (the lesson's core teaching)
Teach, on the spot, the mechanism the reader keeps: a model trained to predict
"who did we hire before" optimizes to reproduce the past, including its bias;
removing the protected attribute does not remove bias because the model
reconstructs it from correlated proxies (redundant encoding); "the humans made
the final call" does not launder a biased ranking. This is a training-data /
proxy-discrimination failure, distinct from the deployment failures the series
has already covered.

## Where the weakness lives today
Resume-screeners and automated hiring tools are now widespread, which is why New
York City's Local Law 144 mandates bias audits of automated employment decision
tools — a published the-paper lesson (ai-in-the-world/nyc-hiring-bias-audits)
that this piece can point to for the regulatory response. Name concrete present
systems/patterns where proxy bias in training data recurs.

## Boundaries
- One lesson, lesson template, 1200–2200 words.
- Distinct from published when-ai-breaks pieces: this is the hiring/employment
  training-data bias incident; COMPAS (recidivism) and the Dutch childcare and
  UK A-level cases are public-sector scoring — do not blur them together. The
  reader may be sent to those or to the NYC-audit lesson via links, not
  re-taught.
- Careful sourcing: the core account rests substantially on one Reuters
  investigation sourced to anonymous insiders. Treat it as strong but attribute
  it precisely, seek independent corroboration, and mark what is confirmed vs
  what rests on that single origin. Do not state the tool rejected real
  applicants at scale if the record says it was experimental and never the sole
  screen — say exactly what the record supports.

## Source policy (from `nb source-policy --series when-ai-breaks`)
- Minimum 8 sources; primary >= 4, secondary >= 1.
- The record here is largely journalistic. Primary = the documents/records that
  own their claims: the Reuters investigation (the origin report), any Amazon
  statement, the text of NYC Local Law 144 and its rules, EEOC guidance on
  automated hiring, and peer-reviewed work on proxy/redundant-encoding bias
  (e.g. the machine-learning fairness literature that owns the mechanism).
  Secondary = other outlets' retellings (note that retellings of the Reuters
  story count as one origin, not independent confirmation).

## Production policy (from `nb production-policy --series when-ai-breaks`, profile balanced)
- writing-coach: capable / low  → claude (sonnet)
- researcher: capable / high     → claude (opus, claude-opus-4-8)
- writer: capable / medium       → claude (opus, claude-opus-4-8)
- editor: capable / high         → claude (opus, claude-opus-4-8)
No `required` directive; capable tier honored, no deviation.

## Tags
No tag prompt-fragments configured for this series; ships with empty tag list.

## This edition's neighbors (keep distinct, one paper)
Runs tonight with the-evidence/alphafold, the-instruments/cost-per-token,
the-mechanics/prefill-and-decode, what-could-go-wrong/self-replication. No
overlap; this is the run's incident lesson. The proxy-bias mechanism it teaches
is its own; keep it concrete to hiring.

## Recent shapes in this series to break (do not inherit)
The series' recent headlines lean on a time/count reveal ("learned racism in
about 16 hours," "overshot for 100 of 108 weeks") and the "X did Y" incident
frame with a number. A number-led headline is fine if the number is truly this
story's; do not reuse the "in about N hours/weeks" duration mold. Avoid
comma-triad and semicolon-reversal deks.
