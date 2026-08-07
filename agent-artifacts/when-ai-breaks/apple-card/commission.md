# Commission: when-ai-breaks/apple-card

## Assignment
Tell one incident in order. In November 2019 the software developer David
Heinemeier Hansson posted that the Apple Card gave him a credit limit ~20x his
wife's despite shared finances; Steve Wozniak reported the same; the story went
viral and the New York Department of Financial Services opened an investigation
into Goldman Sachs, the card's issuer. Name the people, the company, and the
dates. Then explain the mechanism the episode exposed, and what the March 2021
DFS report actually found. Close with where the same weakness lives now.

## Why this incident, now
It is a clean, famous case where an algorithm was publicly accused of gender
bias, and the honest record is more interesting than the headline: the
regulator found no fair-lending law violation, yet the episode still exposed
real failures of transparency and the near-impossibility of an applicant
proving algorithmic discrimination. It teaches proxy variables, disparate
impact vs disparate treatment, and model opacity, all core AI-literacy ideas.

## Angle boundaries
- The subject is the **incident and what it teaches**. The spine is the March
  2021 NY DFS "Report on the Apple Card Investigation." Take the load-bearing
  findings from the report itself, not from 2019 hot-takes. The report found no
  unlawful disparate treatment on the evidence reviewed AND documented the
  transparency and customer-service failures; carry both faithfully.
- The disputed cause is the teaching. Present the strongest version of the bias
  case (shared finances, wildly different limits, no explanation given to
  customers) AND the strongest version of the "no violation" finding (limits
  set by individual income/credit factors, gender not an input), then say
  exactly what evidence would settle it and why an applicant could not get it.
- Explain the mechanism with course-taught ideas: a model can produce a
  disparate outcome without using the protected attribute, through correlated
  proxies, and "the model doesn't use gender" does not clear it. Teach only the
  missing piece on the spot; keep it tight.
- Distinct from published when-ai-breaks pieces: amazon-hiring-tool (gender bias
  in resume screening, never deployed) and compas-recidivism (criminal risk
  scores, the two-definitions-of-fairness fight). This is consumer credit, a
  deployed product, and a case where the regulator did NOT find a violation.
  Reference compas for the fairness-definition point rather than re-deriving it.
- Do not inflate. The individual harms are real (denied limits, no recourse,
  public humiliation), but the documented finding is nuanced. Its weight is the
  transparency lesson and the proof problem, not a proven discrimination verdict.

## Required contribution
The reader should be able to recount what happened and when, state precisely
what the DFS found and did not find, explain how an algorithm can produce a
biased-looking outcome without using the protected attribute (proxies) and why
that is so hard to prove or disprove, and name where the same opacity sits today.

## This edition (neighbors — keep distinct)
- the-evidence/resnet — a landmark paper as a document
- the-instruments/hallucination-rate — how a reliability number is manufactured
- the-mechanics/thinking-out-loud — why writing steps improves answers
- what-could-go-wrong/sharp-left-turn — a capability jump outrunning safety

## Template & policy
- Template: lesson.
- Source policy: min 8 sources; >=4 primary, >=1 secondary. Primary: the NY DFS
  report; Goldman Sachs / Apple public statements; the original Hansson/Wozniak
  posts as primary artifacts of the complaint; relevant fair-lending law (ECOA)
  text or regulator guidance. Secondary: contemporaneous reporting that held up
  (context only, never the source for the DFS findings). If four primaries are
  genuinely hard to reach, record what you found and flag it.
- Production policy (balanced): coach low, researcher high, writer medium,
  editor high; model "capable"; none required.
- Actual harness/model: `claude-code-routine`, `claude-opus-4-8` for all roles.
  Record in nb-meta (date 2026-08-07).

## Habits not to inherit (for the writer brief)
Recent when-ai-breaks pieces open by naming the operator and the failure in the
headline and close on a "where the same weakness runs now" section. Keep the
closing move (it is the series mandate) but vary its phrasing, and find this
incident's own opener rather than the recurring "Operator did X" mold. Check
the recent library's deks and headings first.
