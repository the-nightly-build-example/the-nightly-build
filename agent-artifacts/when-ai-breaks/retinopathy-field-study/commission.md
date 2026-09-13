# Commission: when-ai-breaks/retinopathy-field-study

## Assignment
Tell the story of Google Health's diabetic retinopathy screening system in Thai
clinics: a deep-learning model with high laboratory accuracy that stumbled once
nurses used it on real patients, documented in a 2020 human-centered field study.
One lesson on the When AI Breaks desk. Template: lesson. Publication date:
2026-09-13.

## Why this incident, now
The desk has taught medical algorithms that were bad, biased, or opaque
(`when-ai-breaks/epic-sepsis-model`, `when-ai-breaks/optum-health-algorithm`,
`when-ai-breaks/ibm-watson-oncology`, `when-ai-breaks/nh-predict`). It has not
taught the failure that a good model still runs into: a system that scores like an
expert on curated test images and then fails in a clinic because real conditions,
real workflows, and real people are not the test set. The reader has met
distribution shift once as a self-driving cause (`when-ai-breaks/waymo-recall`);
this lesson teaches it as the gap between lab accuracy and field deployment, the
weakness under a great many medical-AI claims.

## Tell it in order (the desk's arc)
- What the system was built to do: screen retinal photographs for diabetic
  retinopathy and flag patients for referral, trained and validated to accuracy
  on par with ophthalmologists on graded image sets. Name the model's origin
  (the 2016 JAMA algorithm) and the deployment (Google Health / Verily with
  Thailand's Ministry of Public Health, in real screening clinics).
- What it actually did in the field: the human-centered study (CHI 2020) found
  the system rejecting a large share of images for not meeting its quality bar,
  nurses and patients losing time, dependence on clinic internet, and referrals
  that the workflow made harder rather than easier. Give the numbers the study
  reports.
- Who it affected: the nurses running screening and the patients who traveled for
  it, in the specific clinics studied. Name people and roles as the sources give
  them; name the companies and the dates.
- What the operator did afterward: what Google's own researchers recommended and
  reported.
- Why that kind of system fails that way: teach the missing piece on the spot,
  distribution shift and the sociotechnical gap, that a model validated on clean,
  high-quality, well-graded images meets a field where lighting, cameras, patient
  flow, and connectivity differ from the training distribution, so accuracy on the
  bench does not transfer to outcomes in the room.
- Where the same weakness lives today: any medical AI, and any AI, validated only
  on curated data and reported by a bench number, deployed into a different real
  distribution.

## What the reader already holds — do not re-teach, link instead
- Distribution shift as a failure cause: link `when-ai-breaks/waymo-recall` in
  Background; teach the medical-screening version here without re-teaching the
  concept from zero.
- How an accuracy number is made and why a bench score is fragile: the reader has
  the Instruments desk; link one relevant lesson only if a Background row earns it
  (e.g., a ranking/threshold metric).

## Research directions (researcher owns depth)
1. The field study itself as the spine: Beede and colleagues, "A Human-Centered
   Evaluation of a Deep Learning System Deployed in Clinics" (CHI 2020, Google
   Health). Read it for the exact findings, the number of clinics, the image
   rejection rate, the workflow and connectivity problems, and the direct quotes
   from nurses. Every field figure comes from here or the paper it cites.
2. The model's lab pedigree: Gulshan et al., "Development and Validation of a Deep
   Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus
   Photographs" (JAMA, 2016), for the validation accuracy and what set it was
   graded on.
3. The deployment context: Google Health / Verily and Thailand's Ministry of
   Public Health, dates, and scale. Operator statements and any follow-up.
4. Secondary reporting that held up (for public context and framing), kept
   subordinate to the primary study.

## Contradictions to probe
Whether the failure was the model, the images, the workflow, or the deployment
decision, and how Google framed it versus how independent observers did. The study
is Google's own, so weigh that. Record disagreement in full.

## Sources
Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primary: the
CHI 2020 field study, the JAMA 2016 validation paper, operator documentation.
Contested figures need the primary that owns them. Accusations need two
independent confirmations.

## Boundaries
No code. Tell one incident and teach one cause. This is not a general essay on
medical AI; keep it to this deployment and the lab-versus-field lesson it carries.
Do not re-teach distribution shift from scratch; link the prior lesson and teach
the screening-specific version.

## Production policy (balanced; none required)
writing-coach capable/low; researcher capable/high; writer capable/medium; editor
capable/high. "capable" served by the run's default subagent model (Opus-class);
record the actual writer model in nb-meta.

## Neighbors in this run
the-evidence/mamba, the-instruments/bertscore,
the-mechanics/speech-to-text-hallucination,
what-could-go-wrong/capability-elicitation. No overlap.

## Habits from the recent record not to inherit
- The desk's headlines put a named actor, a hard number, and a date up front;
  keep that discipline but find this piece's own claim rather than echoing a
  recent one's shape.
- Keep the order (built to do / did / who / operator / why / where it lives) but
  name sections for this incident, never with stock labels.
