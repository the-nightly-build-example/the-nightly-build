# Commission: when-ai-breaks/ai-writing-detectors

## Assignment

Teach one failure: AI writing detectors deployed to schools flagged real students'
own writing as machine-generated, and the accusations that followed fell hardest on
students who write differently from the training norm. The reader should finish
knowing what happened in order, why this kind of detector produces false positives,
and where the same weakness sits today.

Tell it in order: what the detectors were built to do (flag AI-generated text in
student submissions); the scale of deployment (Turnitin launched its AI-writing
detector in April 2023 to thousands of institutions with a low claimed
false-positive rate); what actually happened (independent tests and documented
student cases found false positives, and studies showed the detectors flag
non-native English writers far more often); who it affected (accused students, and
disproportionately ESL and some neurodivergent writers); and what operators did
afterward (universities such as Vanderbilt disabled Turnitin's detector; OpenAI
withdrew its own AI Classifier in July 2023 for low accuracy; Turnitin's own later
statements walked back the reliability). Name the companies, institutions, and
dates, and verify each against the record.

Then explain why this kind of system fails: a detector judges text by statistical
signatures (how predictable or uniform it is), and human writing that is plain,
formulaic, or by a non-native speaker reads as machine-like, so it is flagged.
There is research arguing reliable detection is not achievable and that paraphrasing
defeats it. Teach the needed piece on the spot; where taught ground helps, link the
existing lesson the-instruments/perplexity rather than re-teaching it. Close on
where the weakness lives now: detectors still sold and used to make consequential
calls.

## Angle and boundaries

- Work from the record: the studies, the universities' own announcements, the
  vendors' own statements, and reporting that held up. When the false-positive rate
  is disputed (the vendor's claim versus independent findings), present the
  strongest account of each and say what evidence would settle it.
- Distinguish from neighbors and link, do not re-teach: when-ai-breaks/cnet-ai-articles
  (AI writing published as journalism) is a different failure. This lesson owns the
  detector and the false accusation.

## Sources

Policy: at least 8 sources, at least 4 primary, at least 1 secondary. Primary
candidates: the peer-reviewed studies (e.g. Liang et al. 2023 on bias against
non-native writers; Sadasivan et al. 2023 on the limits of reliable detection),
Turnitin's own statements/claims, OpenAI's AI Classifier withdrawal note, and a
university's own announcement disabling the tool. Reporting (Washington Post, The
Markup, etc.) is secondary. Researcher owns the set, verifies every figure and date
against its owning source, and records the vendor-versus-independent dispute in full.

## Production policy (balanced profile)

- researcher high, writing-coach low, writer medium, editor high; capable model.
- nb-meta harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
  series `when-ai-breaks`, slug `ai-writing-detectors`. No `required` directive.

## This edition's siblings (keep each piece distinct)

Publishing with lessons on the adversarial-examples paper, the toxicity score,
hands in generated images, and the AI-boxing argument. This piece owns the
detector-failure incident. The toxicity-score piece (the-instruments) is about a
different classifier and is a how-the-number-is-made lesson, not an incident; keep
this one to the deployment and its harm.

## Recent-pattern notes (habits not to inherit)

Recent when-ai-breaks deks/headlines, not to echo in mold:
- "McDonald's spent nearly five years building an AI to take drive-thru orders, then switched it off"
- "A court let Workday be sued as an employer's 'agent' for the AI that screens applicants"
- "CNET let an AI draft its finance advice under a staff byline"
- "The FTC found DoNotPay never tested its robot lawyer against a human one"
- "SafeRent scored renters on their credit and never counted the voucher paying their rent"
The most recent piece (mcdonalds) ran an nb-figure "three things have to work"
section and an nb-position verdict-style section; do not default to that shape.
Only the two bookends address the reader. No Verdict block at the body's close.
