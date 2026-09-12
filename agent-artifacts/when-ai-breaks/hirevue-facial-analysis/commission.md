# Commission: when-ai-breaks/hirevue-facial-analysis

## The assignment

Tell the HireVue facial-analysis failure: HireVue sold AI video-interview software
that scored job candidates partly on their facial movements and tone of voice,
deployed it at scale, was challenged as scientifically baseless and biased, and in
2021 dropped the facial-analysis component. This is When AI Breaks: tell what
happened in order with names, companies, and dates; explain why that kind of
system fails that way; and close with where the same weakness lives in systems the
reader meets.

Selected because it is a well-documented deployed-system failure with a distinct
mechanism the library has not covered: inferring competence or traits from a face
and voice, a measurement with no scientific basis. It is distinct from the other
hiring-AI incidents in the library (resume-screening bias, applicant rejection,
age discrimination); the failure here is construct validity, not training-data
bias.

## What the lesson must do

- Tell what happened in order. What HireVue built (asynchronous video interviews
  scored by AI on word choice, tone, and, until 2021, facial expressions / facial
  action units, producing an "employability" or competency ranking); the scale of
  deployment (name the figures the record supports: number of enterprise customers
  and candidates assessed, and named clients such as Hilton and Unilever if the
  record supports them); what went wrong (the facial-analysis basis was
  scientifically unsupported and raised bias concerns for people who express
  differently, including by disability or culture); who it affected (job seekers
  scored and filtered by it); and what the operator did (commissioned an audit and
  announced in early 2021 it was removing facial analysis while keeping other
  components). Name HireVue, its leadership at the time, EPIC, and the dates.
- Explain why that kind of system fails that way, teaching the missing piece: the
  scientific consensus that facial expressions do not reliably reveal inner states
  or traits (cite the Barrett et al. 2019 review), the resulting construct-validity
  failure (the system measures something, but not the thing it claims), and the
  automation bias that let an unvalidated score gate real hiring decisions.
- Close with where the same weakness lives today: emotion-recognition AI still
  sold for hiring, proctoring, and surveillance, and the general hazard of
  inferring internal traits from faces or voices.

## Boundaries

- One incident. This is HireVue's facial-analysis component and its withdrawal, not
  a survey of hiring AI. Link amazon-hiring-tool, workday-hiring-screening, and
  itutorgroup-age-discrimination in Background; the mechanism here (invalid
  measurement) is the distinct contribution, so do not re-run their bias angle.
- Work from the record: EPIC's 2019 FTC complaint, HireVue's own 2021 statement,
  the Illinois Artificial Intelligence Video Interview Act, the Barrett et al.
  review, the ORCAA/algorithmic audit as reported, and reporting that held up. When
  the cause or HireVue's account is disputed, present the strongest version of each
  side and say what would settle it.

## Required contribution

The reader should finish able to explain why scoring a candidate on facial
expressions fails as measurement rather than merely as biased data, what HireVue
actually removed versus kept, and how to recognize the same infer-traits-from-a-
face hazard in other deployed systems.

## Source obligations

From `nb source-policy --series when-ai-breaks`: at least 8 sources, at least 4
primary, at least 1 secondary. Primaries should include EPIC's FTC complaint,
HireVue's 2021 announcement, the Illinois AI Video Interview Act text, and the
Barrett et al. 2019 review; secondary reporting supplies context. Verify every
figure (customers, candidates, dates) against the primary or the reporting that
owns it, and be careful not to overstate what facial analysis contributed to a
score beyond what the record supports.

## Recent habits not to inherit (when-ai-breaks)

- Do not copy the recent possessive-actor-verb-object headline cadence by reflex,
  and keep negative parallelism out of headline and dek.
- The closing "where it lives now" section is required; do not open it with
  "Today's..." or reuse a recent closer's shape.

## Neighboring articles in tonight's edition

Running now, do not overlap: the-evidence/variational-autoencoder, the-instruments/
f1-score, the-mechanics/lost-in-the-middle, what-could-go-wrong/alignment-faking.
Keep this on the incident and its measurement-validity mechanism.

## Production record

- Harness: Claude Code (remote). Model for every role: claude-opus-4-8 (capable
  tier; no stage required).
- Effort targets (`nb production-policy --series when-ai-breaks`): researcher high,
  writer medium, editor high, writing-coach low. Recorded as targets.
- No source or production directive was traded down.
- Note: an earlier commissioning round in this run mistakenly selected already-
  published slugs; this slug was verified absent from the full library first.
