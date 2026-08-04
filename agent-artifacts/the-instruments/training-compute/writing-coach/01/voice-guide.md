# Voice guide: the-instruments/training-compute (01)

## Directive

Write for a reader who trusts a number that looks exact. The whole lesson turns
on one reversal: the headline training-FLOP figure wears the costume of a
measurement (a clean power of ten, a chip count, a threshold in law) while being
a guess assembled two ways, each with a loose joint. The house voice already
gives you plainness and short sentences. What it does not give you is the
discipline this particular article needs: to make a precise-looking number *feel*
loose without a paragraph of arithmetic, and to hold apart what the number
honestly settles (the rough size of a training run) from what it is asked to
certify (frontier status, systemic risk) without reaching for the "not X, it is
Z" reflex the standard already rations.

Three moves change sentences here.

First, when you state a FLOP figure, let the reader see the estimate underneath
it in the same breath the first time, then trust them. Do not re-caveat every
later mention; a number established as an estimate stays an estimate.

Second, the article's spine is a forward/backward flip: the number answers "how
big was the run," and regulation reads it as the answer to "how capable, how
dangerous." Build that flip as two plain positive statements about what the
number does, not as a correction of a strawman. The misreading you name must be
one a real document or official actually made, cited, or it is invented contrast
and gets cut.

Third, an estimation method fails for a concrete, physical reason (chips rarely
run near peak; 6ND counts parameters a mixture-of-experts model does not all
use). Reach the reader through the mechanism, not the percentage. The number is
the receipt; the analogy or the worked case is what the reader carries.

Do not restate the commission's findings, the 6ND derivation, or template rules.
Specify how to write, never what to say.

## Licenses

form: everyday-scale analogy for an estimation failure mode
move: Nuzzo makes a subtle statistical limit felt by swapping in a decision the
  reader has faced (a morning headache that is far likelier an allergy than a
  brain tumour; a replication as surprising as a coin coming up tails). The
  image carries the actual mechanism, not a mood.
bar: one use must make a specific looseness concrete (why real utilization lands
  near a third of peak, why active parameters differ from total). If the analogy
  would still fit a different measurement, it is decoration and comes out.

form: the forward/backward pivot on what the number answers
move: Nuzzo's core observation is that a P value summarizes data under one
  assumption and "cannot work backwards" to the reality people want from it.
  The same shape fits FLOP: it sizes a run forward; it is read backward as proof
  of capability.
bar: state both directions as things the number does, each tied to a named
  user of it (a lab's disclosure, a regulation's threshold). No "not X but Y"
  scaffolding; if the backward reading is not one a cited party actually made,
  cut it. One such pivot carries the article; a second reads as a tic.

form: the visible gap between what was measured and what is claimed
move: Kucharski makes uncertainty tangible by showing the proportional collapse
  under a headline figure — a classifier validated on a handful of cases,
  applied to hundreds — so error compounds through steps the final interval
  never counted.
bar: anchor to one documented figure with a real denominator (a disclosed MFU,
  an undisclosed run circulating only as a third-party estimate). Show the gap
  with the actual numbers once; do not gesture at "wide error bars" in the
  abstract.

form: claim, then the complication that undoes the clean reading
move: Harford sets a plain fact and immediately turns it — the figure is real,
  yet what it omits changes what it means. The turn lands because the setup was
  granted in full, not strawmanned.
bar: the complication must be a property of the estimate itself (a hidden
  assumption, an excluded cost like post-training or failed runs), not a
  rhetorical "but." Grant the number its honest strength before you show its
  limit.

## Recently used, do not reuse

The commission flags the "number swings N-fold / both true" dek mold. The recent
library confirms it is exhausted across deks, headlines, and headings. Avoid:

Dek and headline molds:
- "swings N-fold" / "swings Nx" / "fell from X% to Y%" / "swung by N points"
  (cost-per-token, energy-per-query, aime, llm-as-a-judge).
- "X by one honest measure and Y by another" / "X and Y are both true"
  (energy-per-query, tokens-per-second).
- "the gap traces to N stacked assumptions" / "one of at least four choices that
  decide" (energy-per-query, tokens-per-second).
- "depending only on [the one variable]" as the dek's hinge (energy-per-query,
  llm-as-a-judge, perplexity).
- "a 1-2 point difference is a coin flip" / a headline verb of a score rising or
  falling by a stated amount (bleu, aime, perplexity). Do not make the swing the
  headline; this desk has done it five nights running.

Heading molds (vary the shape, per the standard):
- "A X is not a Y" (cost-per-token: "A price list is not a bill," "A token is
  not a fixed unit").
- "What X does and does not settle" / "What X cannot promise" (bleu,
  cost-per-token, energy-per-query).
- "N ways to price the same X" / "The same task, priced N ways" (cost-per-token,
  energy-per-query).
- "The [evaluation] where the [ranking] flipped" (bleu).

The finding here is real; earn a fresh shape for it rather than restamping the
desk's mold onto a number that swings.

## Regina Nuzzo, "Scientific method: Statistical errors" (Nature, 2014)
Source: https://www.nature.com/articles/506150a
Craft:
- cadence: a human sentence sets the scene, a short one turns it. "The results
  were 'plain as day.'" Then: "But then reality intervened." Setup granted at
  length, reversal delivered short.
- argument: opens on one researcher's near-miss (Motyl's p=0.01 becoming 0.59
  on replication), then generalizes from the case to the flaw. The story is the
  on-ramp, not an ornament bolted on after the explanation.
- evidence: exact figures used as anchors, not proof-by-volume (0.01 vs 0.59;
  "73% — or only 50%"), each immediately translated into stakes a reader feels.
- stance: unhurried, on the reader's side against a number that intimidates
  experts too. Names the flaw plainly without scolding the people fooled by it.
- notice: the number answers one question and is read as answering its reverse;
  "it cannot work backwards" is the whole lesson in four words.
- diction: concrete everyday nouns for abstract statistics (mosquitoes, a
  headache, a coin toss, the emperor's new clothes); the analogy always carries
  the mechanism.
- reader: assumes numeracy, explains none of the arithmetic, spends the saved
  words on what the number means.
- the missed move: she earns the right to state the limit by first showing the
  number at its most convincing (a "sexy hypothesis," data "plain as day"), so
  the deflation is the evidence's, not the writer's.

## Adam Kucharski, "When it comes to uncertainty, AI research is lagging behind"
Source: https://kucharski.substack.com/p/when-it-comes-to-uncertainty-ai-research
Craft:
- cadence: short declaratives carrying the claim, longer sentences carrying the
  qualification. "Even something as simple as adding up numbers can have a whole
  bunch of hidden assumptions and failure modes."
- argument: error is not one number at the end; it compounds through processing
  steps the reported interval never saw. A headline figure of confidence sits on
  top of uncounted uncertainty below.
- evidence: the tell is a denominator — a classifier validated on 131 cases,
  applied to 872 combinations. The proportional collapse does the persuading.
- stance: measured, technical but colloquial ("marked its own homework"), treats
  the reader as a peer who can hold a caveat without being alarmed.
- notice: a tool can be "noisy, biased, and non-reproducible on their own" and
  still get treated as a clean instrument once its output is a single number.
- diction: plain engineering vocabulary; enumerates failure modes in threes to
  make an abstract risk feel itemized and real.
- reader: numerate and skeptical; given the mechanism of the error, not just its
  existence.
- the missed move: he quantifies the gap between what was tested and what is
  claimed, so uncertainty becomes a ratio the reader can see rather than a
  hedge word.

## Tim Harford, "How Politicians Poisoned Statistics" (FT Magazine, 2016)
Source: https://timharford.com/2016/04/how-politicians-poisoned-statistics/
Craft:
- cadence: claim then complication, often one blunt sentence then its reversal.
  Parallel structure escalates ("useless for winning power ... useless for
  wielding it, too").
- argument: the hardest numbers are not hard to count but hard to *define*;
  once the definition is contested, the tidy figure is a weapon, not a fact.
- evidence: a concrete institutional detail makes the abstraction legible (a
  fund "set up with £125m ... just five years ago" backing "more than 100
  evaluations"), so the later betrayal of that evidence stings.
- stance: skeptical of the people wielding the number, sympathetic to the
  reader who has to live with it; never numbing.
- notice: a figure can be technically true and still mislead, because the fight
  is over what it was ever measuring.
- diction: plain, argumentative, unafraid of a flat verdict once earned.
- reader: assumed to distrust statistics already; the essay gives them the
  precise reason rather than a general caution.
- the missed move: he separates the number's existence from the claim built on
  top of it, holding the two in view at once — exactly the FLOP measures-a-run
  vs certifies-a-risk split, done without a hedged contrast.
