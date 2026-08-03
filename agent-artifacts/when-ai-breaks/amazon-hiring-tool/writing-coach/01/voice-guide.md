# Voice guide: when-ai-breaks/amazon-hiring-tool

Write this as an in-order incident narrative that never lets the story loosen
its grip on its own sourcing. The house's plain-claims, teacherly economy
(Yglesias explaining something he understands) already sets tone; what this
piece adds is discipline about *where the evidentiary weight of a sentence
lives*. Every sentence that carries the Reuters-origin account states its
source in the same clause that states the fact — never a bare claim followed,
paragraphs later, by a citation that is supposed to retroactively cover it.
When the narrative turns from what happened to why it happens, mark that
turn with one earned sentence, not a lecture. Build "the model rebuilt the
bias from proxies" by showing the concrete stand-in (a word, a verb, a
college name) before naming the mechanism, then hold that name for the rest
of the piece. Nothing here licenses distance from the record: the writer
stays exactly as close to what Reuters, Amazon, and the fairness literature
each specifically support, and no closer.

## Licenses

```text
form: inline source-weight clause
move: the origin report states a fact and the evidentiary basis for that
      fact in the same sentence, so the reader receives the claim and its
      confidence level in one motion instead of a claim now and a caveat
      later
bar:  every sentence that extends the Reuters-origin account (what the model
      penalized, what Amazon tried, why the effort ended) carries its own
      attribution clause in that sentence, not a shared footnote three
      paragraphs off; a claim resting only on anonymous sourcing never reads
      as more settled than a claim Amazon has itself acknowledged, and the
      two are worded differently on the page
```

```text
form: concrete-instance-before-abstraction sequencing
move: a technical term for the mechanism is introduced only once its
      concrete case is already stated as fact, so the abstraction has
      something specific to point back to instead of floating free
bar:  "proxy," "redundant encoding," or any equivalent term for the
      mechanism appears for the first time only after the specific stand-in
      (a term the model downgraded, a credential it read as a signal) is
      already on the page as a stated fact; once the term is used, hold it
      exactly — no later synonym for variety
```

```text
form: single reversal sentence at the narrative-to-analysis pivot
move: a hinge sentence built entirely from two facts already stated earlier
      in the piece, placed at the exact point the story stops narrating and
      starts explaining, so it reports a finding instead of announcing a
      verdict
bar:  used once, only at that hinge; it may not introduce any new claim of
      its own (every component fact must already be on the page); it never
      repeats as a section-opening tic elsewhere in the piece, and it is not
      a hedge ("not X but Y") — it is a plain statement of what the two
      already-stated facts add up to
```

```text
form: one adjacent-domain hypothetical to build mechanism intuition
move: a brief, clearly labeled hypothetical from a different hiring-adjacent
      case (not this record, not the other public-sector scoring incidents
      the commission has ruled off-limits) run right beside the mechanism
      explanation, so the reader feels how a system can select against a
      trait nobody coded in before being asked to trust the abstract claim
bar:  usable once; explicitly marked as illustrative, never phrased as
      something Amazon's tool itself did; it may not be COMPAS, the Dutch
      childcare case, or the UK A-level case — those are reserved for their
      own lessons and a link, not material here
```

An empty license keeps the house default: plain declarative narration, one
technical term at a time, no direct address, no aside that isn't already
licensed by `spec/editorial.md`.

## Recently used, do not reuse

- The series' "in about N hours/weeks" duration-count headline mold. This
  incident's real news is not a clock; do not manufacture a duration to fit
  the mold.
- Comma-triad deks and semicolon-reversal deks.
- Do not let attribution discipline flatten the story into a methodology
  section. The inline source-weight clause above exists so precision and
  narrative drive are the same sentence, not two competing ones — if a
  paragraph starts reading like a corrections log, cut the hedging back into
  the verb and noun choices instead of adding another qualifier.

## Jeffrey Dastin, "Amazon scraps secret AI recruiting tool that showed bias against women"

Source: https://www.euronews.com/business/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women
(Reuters investigation, Oct. 10, 2018; this is a syndicated republication of
the wire report, read in full for this study.)

Craft:
- cadence: plain, chronological declaratives — the project starts in 2014,
  the problem surfaces by 2015, the team is disbanded by early 2017 — each
  clause moving the timeline forward rather than circling back to restate it
- argument: builds the case entirely from sequence and specific detail; it
  never states a thesis about bias in general, it just narrates the
  particular mechanism until the reader has assembled it
- evidence: precise, graded attribution in the same breath as the claim —
  "five people familiar with the effort," "some of the people said," "who
  spoke on condition of anonymity" — each hedge sized to exactly what that
  source can support, not rounded up
- stance: neutral narrator; the piece never editorializes about what Amazon
  should have done, it lets the sequence of attempted fixes and eventual
  abandonment make the judgment for it
- notice: catches the specific proxies — the word "women's," the verbs more
  common on men's resumes, the two unnamed all-women's colleges — rather
  than describing the bias only in the abstract
- diction: concrete nouns and verbs throughout ("penalized," "downgraded,"
  "disbanded"); no euphemism for what the system did
- reader: assumes no prior technical background; explains the star-rating
  system and the historical-data problem as it goes, in the plainest
  possible terms, once each
- hedge calibration: keeps what Amazon itself later acknowledged in
  different, more confident wording than what rests solely on anonymous
  sourcing, so the reader can tell the two apart without being told to

## Karen Hao, "This is how AI bias really happens—and why it's so hard to fix"

Source: https://www.technologyreview.com/2019/02/04/137602/this-is-how-ai-bias-really-happensand-why-its-so-hard-to-fix/
(MIT Technology Review, Feb. 4, 2019)

Craft:
- cadence: alternates a general claim with an immediate, paired concrete
  illustration — never lets an abstraction sit alone for more than a
  sentence before grounding it
- argument: structured as stages of a pipeline (framing the problem,
  collecting the data, preparing the data), each stage introducing one new
  idea and closing it before the next starts
- evidence: leans on named researchers and specific, checkable cases (the
  Amazon tool among them) rather than general assertions about "AI bias"
- stance: measured and explanatory; admits the scale of the problem plainly
  ("if you're reeling... so am I") without abandoning analytical distance
- notice: catches the second-order version of the Amazon case — that the
  model kept finding new proxies (verbs like "executed," "captured") even
  after the obvious ones were removed — and uses that specifically to teach
  why removing a variable doesn't remove the bias
- diction: pairs every technical term with a plain-language double, e.g. an
  "attribute" glossed immediately as "age, income, number of paid-off loans"
- reader: a general but literate audience assumed to know nothing about
  machine learning pipelines going in, walked through each stage once
- term economy: once a term is defined via its paired example, later
  references use only the noun — no re-explaining, no synonym swap

## Julia Angwin, Jeff Larson, Surya Mattu, Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
(ProPublica, May 23, 2016. Studied for narrative craft only — this is the
COMPAS/recidivism record, which the commission keeps distinct from the
Amazon hiring incident; nothing about its subject transfers, only its
handling of contrast, disputes, and evidence.)

Craft:
- cadence: short declaratives carry the momentum ("Borden and her friend
  immediately dropped the bike and scooter and walked away"), and longer
  sentences arrive only when context needs building, never as a default
  register
- argument: moves from one fully realized concrete case to a second
  contrasting case before making any general claim, so the statistical
  finding that follows lands as confirmation of something already felt, not
  as the first piece of evidence offered
- evidence: quotes the disputing party in its own words rather than
  paraphrasing the dispute into either agreement or dismissal — "the company
  disputes our analysis," followed by Northpointe's own statement
- stance: lets the reversal ("we know the computer algorithm got it exactly
  backward") do the work of judgment; the piece does not add adjectives on
  top of it
- notice: catches the specific individual pair (a minor theft vs. an armed
  robbery record) whose risk scores were inverted, rather than opening on
  the statistic
- diction: plain, unadorned; no legal or technical jargon introduced without
  immediate use
- reader: assumed to have no background in risk-assessment tools; the piece
  defines "risk assessment" only once the human stakes are already visible
- adversarial fairness: when a subject of the reporting disputes the
  finding, the piece prints that party's own rebuttal rather than
  characterizing it, and lets the reader weigh it against the shown data

## Zeynep Tufekci, on proxy variables in hiring algorithms

Source: https://www.npr.org/transcripts/412481743
("What Makes Algorithms Go Awry?", NPR All Tech Considered interview)

Craft:
- cadence: builds toward the mechanism through short, escalating
  hypotheticals rather than defining the mechanism first and illustrating
  second
- argument: uses a parallel case — a hiring algorithm that can flag likely
  depressive episodes from social-media signals nobody explicitly coded in
  — to make "a program can discriminate on a trait no one programmed"
  intuitive before any real incident is named
- evidence: plainly marks the hypothetical as a hypothetical ("it's
  completely possible for a hiring algorithm to..."), never blurring it with
  a reported fact
- stance: direct pushback on the idea that an algorithm is neutral because
  it's a machine — "they're programs... created by us" — argued rather than
  asserted
- notice: catches that the programmers running the hiring committee would
  have no idea the discrimination is happening, which is the same blindness
  this article needs the reader to feel about proxy variables in general
- diction: plain, conversational, but exact about mechanism ("no variable
  labeled 'higher risk of pregnancy'") — precise without technical jargon
- reader: a general audience being walked, in real time, from "that sounds
  impossible" to "that's exactly how it would happen"
- domain displacement: proves the mechanism using a case that is not the
  incident being reported on, which keeps the real record from being
  over-claimed while still letting the reader feel how the mechanism works
