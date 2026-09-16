# Commission: when-ai-breaks/meta-ad-delivery-discrimination

## The incident

Facebook's ad-delivery system delivered housing, employment, and credit ads in
demographically skewed ways even when advertisers set broad, neutral targeting.
The skew came from the machine-learned system that decides who actually sees an
ad, downstream of the advertiser's choices. It drew a peer-reviewed study, a
federal housing charge, and a first-of-its-kind Justice Department settlement.
The lesson tells this incident in order and explains why that kind of system
fails that way. The researcher confirms the record, the dates, the named parties,
and every figure.

## Why this incident, now

The reader hears that an AI system was "biased" and cannot tell whether that means
someone wrote a biased rule, chose biased targeting, or something subtler. This
case teaches the subtler and more common thing: a system optimizing for
engagement reproduced demographic patterns at the delivery step, where no
advertiser chose them and no one could see them happening. It is the clearest
documented instance of discrimination arising from optimization itself, and the
mechanism sits inside every engagement-ranking system the reader uses.

## The declared reader and the fit

The reader is smart and has never bought an ad or trained a ranking model. Build
up every part: what ad targeting is, what ad delivery is and how it differs, what
the delivery system is optimizing for, and why "relevance" or "engagement"
prediction can encode a protected attribute without being told it. Name the
people, companies, agencies, and dates, as the desk requires.

## What the lesson teaches (in order, then the cause)

1. What the system was built to do: given an advertiser's budget and audience,
   predict who will engage and deliver the ad to them to maximize a relevance or
   engagement objective per dollar.
2. What it actually did: the controlled study that varied only an ad's content
   and held targeting and budget fixed, and measured the delivery skew by gender
   and race, with its real numbers and scope. This is the evidence that isolates
   delivery from targeting; give it the weight the incident turns on.
3. Who it affected and what the operator did afterward, in order: the civil-rights
   complaints and settlement that removed protected-category targeting, the
   federal housing charge, and the Justice Department settlement that required a
   new delivery system, with the dates and named parties. Note what the operator
   built in response and what verification followed.
4. Why that kind of system fails that way: an optimizer trained to predict
   engagement learns the demographic regularities in past behavior and delivers
   accordingly, so "relevance" becomes a proxy that carries protected attributes,
   and the skew appears at delivery, invisible to the advertiser. Teach this as
   the transferable lesson.
5. The disputed cause, steelmanned both ways: the operator's position that
   delivery reflects user behavior and relevance rather than discrimination, and
   the researchers' and regulators' position that the optimization itself produces
   disparate delivery. Say what evidence settles it and why the controlled study
   is that evidence.
6. Where the same weakness lives today: any engagement- or relevance-optimizing
   delivery, ranking, or recommendation system can reproduce demographic skew the
   same way, in systems the reader uses.

The original work: showing that the discrimination was produced by the
optimization at delivery, not by anyone's targeting choice, and making that
distinction precise enough that the reader can spot the same failure elsewhere.

## Sources plan

Template and series floor: eight sources, at least four primary and one
secondary. Primary: the peer-reviewed delivery-skew study (read its method and
tables), the federal housing charge, the Justice Department complaint and
settlement, the earlier civil-rights settlement that changed targeting, and the
operator's own description of the delivery system it built afterward. Read the
cited passages, not summaries of them. Secondary reporting sets context only.
Every number carries its denominator and period; an accusation needs the primary
that owns it, and the operator's contested position is attributed to the operator,
not stated as fact.

## Continuity and neighbors

The library covers other algorithmic-harm cases (tenant screening, hiring
screening, claims denial, facial recognition). This one is distinct: disparate
delivery of opportunity ads from engagement optimization. Confirm slugs and link
the closest one in Background only if it helps the reader place this case; do not
re-tell it. Tonight's other lessons are on unrelated desks.

## Recent shapes to break

When AI Breaks has lately opened with a two-sentence headline whose second
sentence is a short flat reversal ("He hadn't."). Do not reach for that mold by
reflex. Watch for the "X, not Y" heading (negative parallelism) that recurs on
this desk; use it only where it corrects a misconception the piece names.

## Production record

Roles run on a capable-tier model (Claude Sonnet) via isolated subagents.
Effort per the balanced profile: researcher high, writer medium, editor high,
writing-coach low. No required directive was traded down.
