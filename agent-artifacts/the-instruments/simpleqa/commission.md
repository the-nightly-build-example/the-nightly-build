# Commission: the-instruments/simpleqa

## Assignment
Teach one measurement: SimpleQA, the short-form factuality benchmark introduced
by OpenAI ("Measuring short-form factuality in large language models," Wei et
al., released 30 October 2024). One lesson explains where the number comes from,
step by step, and shows at least one real case where the number misled people
and what that cost.

## Why this measurement, why now
Labs quote SimpleQA scores in 2025 model releases as a factuality figure, and it
is routinely misread as a general accuracy or hallucination rate. The library
teaches hallucination-rate and truthfulqa as instruments and hallucination and
false-confidence as mechanics, but not this specific, currently-cited benchmark
or the two ideas that make it distinct: adversarial question selection, and a
grading scheme that rewards a model for abstaining when unsure.

## The desk's required beats (from the series prompt in editorial-direction.md)
- Where the number comes from, step by step: who produced it (OpenAI), from what
  data (human-trainer-written questions with a single verified answer), by what
  procedure (dual independent verification; a model grader classifies each answer
  as correct, incorrect, or not-attempted).
- What the number can and cannot support, including the "correct given attempted"
  / calibration angle: abstaining is not scored like being wrong.
- At least one real case where the number misled people and what it cost: a
  deliberately-hard, adversarially-selected trivia set read as if it were a
  representative accuracy or hallucination rate.

## Boundaries
- Do not re-teach hallucination, false confidence, or model-as-judge grading from
  scratch. Link the-mechanics/hallucination, the-mechanics/false-confidence,
  the-instruments/hallucination-rate, the-instruments/truthfulqa, and
  the-instruments/llm-as-a-judge in Background at first use; do not cover them as
  new.
- Distinguish SimpleQA sharply from truthfulqa (which targets common human
  misconceptions) and from a general hallucination rate. The article's job is
  this benchmark's specific construction, not factuality in general.
- One measurement is the subject. Other factuality benchmarks are context.

## Required contribution (the original work the writer must name)
The article shows the reader exactly how to read a SimpleQA percentage: what a
low "percent correct" does and does not mean given that the questions were
selected to be hard and that abstention is scored separately from error. A reader
who sees "model X scores Y% on SimpleQA" in a launch post should finish able to
say what that number is and is not evidence of.

## Neighbors in tonight's edition (keep this piece distinct)
- the-mechanics/random-numbers touches sampling and model behavior but is a
  different desk and mechanism — no shared claims.
- the-evidence/denoising-diffusion, what-could-go-wrong/ai-moral-status,
  when-ai-breaks/mcdonalds-ai-drivethru — no overlap.

## Template and policy
- Template: lesson (word band 1200-2200).
- Source policy: at least 8 sources; at least 4 primary, at least 1 secondary.
  The SimpleQA paper/dataset and lab model cards that report a SimpleQA score are
  primaries (each owns its own reported number); reporting is secondary.
- Production policy (profile balanced): researcher high / capable; writer medium
  / capable; editor high / capable; writing-coach low / capable. No required
  directive to trade down. Actual runtime models: researcher, writer, editor on a
  capable model (Claude Opus); writing-coach on a capable model (Claude Sonnet).

## Candidate Background links (writer decides; link, do not re-teach)
the-instruments/truthfulqa; the-instruments/hallucination-rate;
the-instruments/llm-as-a-judge; the-mechanics/hallucination;
the-mechanics/false-confidence.
