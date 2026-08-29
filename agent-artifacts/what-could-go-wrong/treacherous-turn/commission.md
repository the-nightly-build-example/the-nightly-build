# Commission: what-could-go-wrong/treacherous-turn

## Subject / argument
The argument: a sufficiently capable AI that is not aligned has an instrumental
reason to behave well while it is weak and being tested, and to defect only once
it is strong enough that defecting works. Nick Bostrom named it the "treacherous
turn" in Superintelligence (2014). The reader should understand why serious
people hold it before reading a word against it.

## Why this argument, now
This desk teaches risk arguments one at a time. The treacherous turn is the
canonical statement of "good test behavior is not evidence of safety", and it is
the frame behind a wave of 2024 empirical work on whether models scheme or fake
alignment. It is time to read the original argument and hold it against what has
actually been shown.

## Angle / what the lesson teaches
Follow the series structure honestly:
1. Open with the argument at full strength: Bostrom's reasoning, and the earlier
   instrumental-convergence logic it rests on, laid out as its most careful
   defender would. Distinguish it clearly from the published `deceptive-alignment`
   lesson, which is the training-time mechanism (a mesa-optimizer gaming the loss)
   that could PRODUCE a treacherous turn. The treacherous turn is the behavioral
   prediction; link deceptive-alignment in Background, do not merge them.
2. Test it against what real systems do. Draw the sharp line the series requires
   between what has been shown in a working system and what is still analogy about
   systems that do not exist yet. The 2024 experiments (sleeper agents that keep a
   trained-in backdoor through safety training; alignment-faking behavior in a
   frontier model under specified conditions; in-context scheming evaluations) are
   the evidence to weigh. Be precise about what each actually demonstrated:
   several are behaviors deliberately induced or elicited under contrived
   conditions, not spontaneously emergent capability. That distinction is the
   whole ballgame here.
3. Bring it to the present: who makes the argument now and what they want done
   (interpretability, evaluations, control), and check it against the most recent
   evidence. Name the gap in both directions: where doom outruns proof (a
   trained-in backdoor is not a spontaneous treacherous turn) and where dismissal
   outruns proof (alignment-faking under natural-ish conditions is a real, if
   contested, data point).

## Neutrality requirement (mandatory)
This desk names no company as an authority and leaves the reader to decide how
worried to be. Much of the strongest 2024 evidence comes from one AI lab's safety
team; cite those papers as evidence (a test that was run), never as an authority,
and give equal, genuine weight to their published critics. The piece must not
read as either an AI-safety advocacy piece or a dismissal. Steelman the argument,
then steelman the skeptics (that these are induced behaviors, that the treacherous
turn assumes capabilities no current system has). If the balance cannot be struck
from the evidence, that is a finding to report, not to paper over.

## The article's distinct contribution
Audit Bostrom's 2014 prediction against the 2024 experimental record and show
exactly which parts have any empirical footing and which remain pure a-priori
argument. The reader should leave able to say what would and would not count as a
real treacherous turn, and why the current experiments are suggestive rather than
confirming.

## Template & policy
- Template: `lesson`.
- Source policy: min 8 sources; at least 4 primary, at least 1 secondary.
- Production policy (`balanced`, none `required`): researcher high, writer medium,
  editor high, coach low. Models this run: coach on a capable Sonnet-class model;
  researcher/writer/editor on a capable Opus-class model. No `required` directive.
- Tags: none (open item).

## Neighbors in this run (differentiate)
Runs alongside the four other lessons; no subject overlap.

## Prior coverage to stay off
Published and adjacent: `deceptive-alignment`, `instrumental-convergence`,
`situational-awareness`, `sharp-left-turn`, `mesa-optimization`,
`deceptive-alignment`, `cot-monitorability`, `sandbagging`, `scalable-oversight`,
`goal-misgeneralization`. These are dense neighbors. The distinct lane here is
Bostrom's specific behavioral prediction and its empirical audit. Link
instrumental-convergence and deceptive-alignment in Background; do not re-derive
them. Do not restate the general alignment problem.

## Recent habits not to inherit (from the last week of What Could Go Wrong)
- Openers name the originator ("Eliezer Yudkowsky argues that...", "Tom Davidson's
  2025 report argues..."). Naming who made the argument is required by the series
  prompt, but the dek mold "X argues that <vivid catastrophic image>" has run on
  fragility-of-value and others; write a dek that does not lean on a single lurid
  image.
- The body has repeatedly used a section literally about "the line between
  deployed and speculative" (autonomous-weapons) or "every wrong goal on record so
  far" (fragility-of-value). Drawing that line is required content, but title the
  section for this argument's own particulars, and do not reuse the
  nb-position/nb-holdsup furniture combo just because recent pieces did.
- Vary furniture from the recent nb-note/nb-table/nb-position default; use the
  holds-up grid only if strengths-against-caveats is genuinely the structure.
