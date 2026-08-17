# Commission: what-could-go-wrong/model-collapse

## The argument

Model collapse: train models on data that is itself increasingly machine-generated
and they degrade, losing the rare cases in the tails of the distribution first,
until output converges toward bland, wrong, or repetitive. The worry is that as
the open web fills with AI text and images, the data future models learn from is
polluted by earlier models' output, and quality erodes generation over generation.

## Angle

Open with the argument at full strength. Name who made it and what they showed: a
2024 study (with a 2023 precursor) demonstrated, in controlled experiments, that
feeding a model's own output back as training data recursively makes later
generations degrade and the distribution's tails vanish. Lay out the reasoning a
careful defender would give, so the reader sees why serious researchers worry
before reading a word against it.

Then test it against what real systems do. Draw the sharp line: what has been
shown (recursive training with the previous model's output *replacing* the data
collapses models in these experiments) versus what is extrapolation about the real
web (that mixing at internet scale will cause the same collapse). The case turns on
exactly that: a primary rebuttal shows that *accumulating* real and synthetic data,
rather than replacing, breaks the curse, and real training pipelines curate and mix
rather than blindly retrain on raw model output. Note the live tension with
evidence that curated synthetic data has *helped* models.

Bring it to the present: who presses the collapse worry now and what they want
(data provenance, keeping human data), checked against the most recent primary
evidence. Where confidence outruns proof, name the gap, whether it is alarm or
dismissal.

## What it teaches (short, complete)

1. The argument and its demonstration: recursive training on model output degrades
   models and erases distribution tails, shown in controlled experiments. One
   worked result the reader can hold.
2. The demonstrated-versus-extrapolated line: replacement collapses; accumulation
   and curation may not. Give the primary rebuttal its full strength.
3. What recent primary work does and does not establish about collapse at real-web
   scale, and the tension with cases where curated synthetic data helped.

## Boundaries

- Study how the field reasons about this risk without joining it or writing it off.
  No hype, no doom. Name no company as an authority: cite documents and authors,
  never a lab as arbiter. Steelman both the alarmed and the dismissive readings.
- Work from the original documents (the collapse study, the rebuttal), not
  commentary.
- Established course: `nb history --library` and LINK published neighbors rather
  than re-teach: candidates what-could-go-wrong/data-poisoning (deliberate vs
  accidental corruption), the-mechanics/memorization, and the-evidence tension case
  the-evidence/textbooks-are-all-you-need (synthetic data that helped).

## Neighbors in tonight's edition (avoid overlap)

the-evidence/foundation-models, the-instruments/tau-bench,
the-mechanics/length-control, when-ai-breaks/biden-deepfake-robocall.

## Source policy

Template minimum 8 sources: at least 4 primary, at least 1 secondary. Primary: the
collapse study (Nature 2024 and/or the 2023 precursor), the accumulation rebuttal,
and any primary work on synthetic-data curation that bears on the line. Reporting
is secondary context. A contested figure needs the primary.

## Production record

Series production policy: balanced profile, model tier `capable` for every stage,
none `required`; efforts writing-coach low, researcher high, writer medium, editor
high. Roles run as isolated subagents on this harness's capable-tier model;
effort set to policy where settable, else harness default. No `required` directive
traded down. In nb-meta set `harness` to `Claude Code` and `model` to `capable`
(production tier; specific model identifier kept out of the published article per
harness policy). The writing-coach guide here was reused from a same-series
sibling lesson; take its craft and register, not its subject.
