# Commission: what-could-go-wrong/algorithmic-monoculture

## The argument

Algorithmic monoculture: when many decision-makers use the same model to score
the same candidates, applicants, or documents, its errors line up across every
user of it, so being rejected once is being rejected everywhere. The worry is
that this correlation is worse for the affected group than each individual
model would be on its own, even a slightly worse one, because independent
mistakes at least distribute their harm. The lesson teaches the argument, then
tests it.

## The angle

Open with the argument at full strength, in the terms Jon Kleinberg and Manish
Raghavan used in the paper that named it, then extended it. Their theoretical
result is that under stated conditions monoculture can leave applicants strictly
worse off than a decentralized market of independent, less accurate scorers,
because a single system's biases are amplified by shared adoption rather than
averaged out. State the result and the conditions it depends on.

Then draw the desk's line. Test the argument against what real deployments have
shown. On the demonstrated side: cases where widely deployed models produced
correlated failures across users (e.g. resume-screening incidents; the CrowdStrike
outage as an analogue for correlated-failure risk; the studies of embedding
similarity across models built from similar corpora). On the analogy side: the
strong version — every applicant is scored by the same model across every
hiring firm — has not been shown to hold as strictly as the argument imagines;
markets remain fragmented and models still differ meaningfully.

Bring it to the present. Who argues it today (Kleinberg, Bommasani et al.'s
"picking on the same losers" and the AI Now / Stanford CRFM work), what they
want done, and what the recent evidence says on how correlated model outputs
actually are in the wild. Where confidence outruns proof on either side, name
the gap.

## Teach, in this order

1. The argument: shared use of a scorer plus its inevitable errors means
   applicants rejected once tend to be rejected everywhere, and this can be
   collectively worse than a market of independent worse scorers. Attribute it
   to the people who made it, and state the formal result with its conditions.
2. The demonstrated-versus-analogy line: what has been shown (correlated model
   outputs across deployments, resume-screening incidents, cascading-failure
   analogues) versus the strong strict-monoculture premise, grounded in the
   primaries that report it.
3. The present: who argues it now, what they want (evaluation transparency,
   model diversity mandates, procurement rules), and the latest empirical
   evidence on how correlated deployed models actually are.

## Sources

Series policy requires at least eight sources, at least four primary and at
least one secondary. Kleinberg and Raghavan's foundational papers are anchor
primaries. Bommasani et al.'s "picking on the same losers" (and the CRFM
follow-ups) is a primary for the empirical study. A critical response from a
peer-reviewed venue steelmanning the opposing view belongs in the set. The
researcher resolves the exact set and records contradictory evidence in full.

## Boundaries and neighbors

The 2026-08-24 edition runs this alongside the-evidence/retrieval-augmented-
generation, the-instruments/rewardbench, the-mechanics/first-token-latency, and
when-ai-breaks/nyc-mycity-chatbot. No topic overlap with those.

Within what-could-go-wrong, model-collapse (training on synthetic data),
racing-dynamics (competition between labs), and gradual-disempowerment cover
different failure modes and belong in Background if useful. Do not re-run any
of them. Keep this lesson on the shared-scorer / correlated-error argument
specifically. Hold to the desk's no-hype-no-doom rule.

## Production record

Template: lesson. Series: what-could-go-wrong (open section, self-chosen
topic). Production policy resolved to the balanced profile: writing-coach
effort low, researcher effort high, writer effort medium, editor effort high,
model "capable" for every role. No `required` directive applies.
