# Editorial review: what-could-go-wrong/unilateralists-curse (editor/01)

## Skeptic

Thesis: the unilateralist's curse is a proven decision-theoretic result about
the statistics of independent estimates, and labelling any particular AI model
release an instance of it is an analogy that breaks the assumptions the proof
rests on. The piece stands on four claims, and each held.

- Headline claim, "the most optimistic one decides." The paper says exactly
  this: "it is the highest estimate that will determine whether an initiative is
  undertaken, not the average estimate" (s1, p.355). The article quotes it
  verbatim and reasons from it. Held.
- The counting claim, that more actors make a bad outcome likelier. Two figures
  carry it and both match the primary and the committed asset. At V* near -1
  with five actors the initiative still goes ahead about half the time (s1
  Fig.1, p.354); the chance of a wrong action passes one-half at four actors and
  climbs toward certainty (s1, p.353 and note 9, p.368). I compared the rendered
  asset-1.png against the caption: the S-curve crosses 50% just left of the
  origin, near -1, with the negative-V* region intact. Held.
- The four-assumption test, the article's own construction. The 2016 paper
  carries no AI case at all, so converting its assumption list (independence,
  shared common-good payoff, private symmetric error, naive actors; s1
  pp.354-356) into a portable test is synthesis, not restatement. Each row is
  fair to the paper: the independence and symmetric-error rows track the authors'
  own notes that correlated or skewed errors change the result (notes 10-11,
  p.368), and the naive-actor row tracks their meta-rationality result that a
  careful Bayesian can "manage the curse even without communication" (p.358).
  Held.
- The shown-vs-analogy line. The article draws it in its own words ("stops being
  a proof about AI and becomes an analogy to it"; "It is a shape, not a proof"),
  not the series' stock phrasings. Held, and this is the beat the commission
  requires.

Naming guardrail (the round's highest-priority check): passed. The body does
NOT claim governance authorities routinely invoke the curse by name. It states
the opposite twice: the governance work "reasons in this same structure without
using the name," and "Neither invokes the curse by name. The named application
to AI is scarce, and the sharpest one comes from a critic of the remedy." This
matches the evidence record's finding exactly. GPT-2 and the Llama releases are
staged strictly as structural analogies. No fabricated Shevlane-Dafoe (or other)
quote appears: I traced every quotation to the evidence record and each is
genuine — Bostrom "arises in many contexts"/"highest estimate"/"manage the curse
even without communication"/"principle of conformity"; Zuckerberg "stealing
models that fit on a thumb drive is relatively easy" (confirmed against s6);
Seger "should not be open-sourced, at least not initially" and "dissipate control
away from unilateral decision-makers" (s7 abstract confirmed); Armstrong "has
the advantage of being true"/"valid individual warning..."/"shouldn't rely on
their own naive initial judgement." Shevlane-Dafoe is cited only for the real
term "counterfactual possession," never for a curse quote.

Display text, descriptor by descriptor: headline, dek, four subheads, figure
caption, and timeline labels all check out. Authors named correctly (Bostrom,
Douglas, Sandberg; Gokaslan and Cohen as the two master's students; Seger and
"about two dozen" co-authors; Shevlane and Dafoe; Armstrong). Armstrong is
called "a colleague of the authors," which honestly flags the tie the record
notes (he is thanked in the paper's acknowledgments) rather than passing him off
as a fully independent critic. Dates and parameter counts (1.5B GPT-2 across
Feb/Aug/Nov 2019; Llama 2 July 2023; Llama 3.1 405B July 2024) all match.

data-nb-kind audit: all nine labels correct. s1/s2/s3/s6/s7/s8/s9 primary,
s4/s5 secondary. The one place independence matters — the OpenGPT-2 replication —
is carried by a primary self-interested account (s3, the replicators' own post)
and corroborated by an independent secondary (s4, TechXplore). No wrong label
hides a missing independent source. Source floor met: 9 sources, 7 primary, 2
secondary, against a floor of 8/4/1.

Citation hrefs: I opened them as printed. s1, s5, s6, s7, s8 resolve to the
source and support what they are cited for (confirmed Zuckerberg's thumb-drive
line and Llama 3.1 405B; Heikkila's Llama 2 piece with the undisclosed-training-
data caveat; Seger's "should not be open-sourced, at least not initially"; the
Shevlane-Dafoe title/authors). s4 resolves and I read its real headline (see
below). s2 (arXiv 1908.09203), s3 (Medium), and s9 (social-epistemology landing)
returned bot-protection 403s to my fetch tool, not broken-link errors; the
writer's links-on proof passed BLOCK:0 against all of them, and the s9 landing
page is the reply's reader-facing home. No broken citation.

Source 4 (TechXplore) title, resolved per the brief. The printed title was a
paraphrase. The outlet's verified headline is "Fake news model in staged release
but two researchers fire up replication." I chose to correct the title rather
than prune the source: s4 is the only independent corroboration of the
replication and its timeline (s3 is the replicators' own account), so it earns
its place, and correcting keeps the source count and numbering stable — no
renumber, and no renumber-driven proof. Fixed directly.

## Cut

A dedicated slop pass, then the edges alone, then the link-arrival read, then the
delete test. No sentence required cutting. The prose is dense with fact; the
edge positions where slop collects are carrying weight here.

- Negative-parallelism tell: every "X not Y" in the piece corrects a real, named
  misconception — "the most hopeful estimate decides, not the average" (the
  paper's core point), "not rivals" (the deliberate contrast with racing-
  dynamics the commission asked for), "It is a shape, not a proof" (the required
  shown-vs-analogy beat), "caution and not prohibition" (Armstrong's own gloss).
  None is an invented strawman. All earned.
- Edges: paragraph and section openers/closers were read out of order. "The
  trouble comes only from the statistics of many independent guesses,"
  "That gap is exactly where the argument stops being a proof about AI," and
  "Neither invokes the curse by name..." each carry a fact or a reasoning step.
  The takeaway's last line, "How worried to be is left where the evidence leaves
  it, with you," is the series' explicit mandate delivered in the takeaway
  bookend, which the template allows to address the reader; it lands the stance
  rather than grading the piece, so it stays.
- Two borderline lines I weighed and kept: "The counting is what bites" names
  the specific combinatorial driver and leads into the four-actor fact (a
  fragment that depends on its noun, not filler); "There is a second edge"
  enumerates the second of two distinct objections and orients rather than
  merely signposting. Neither is empty.
- Recent-pattern comparison. Dek: it does not match the flagged deflating
  "Finding, and [the catch]" mold — there is no ", and" caveat; the trailing
  clause names the load-bearing condition (the four assumptions), which is the
  thesis, not a throwaway. Kept. Headings reconstruct the argument in the
  piece's own nouns (mechanism, assumptions, real case, objection) and avoid the
  flagged "The [noun] that/where," "The strongest [case] for X," and wh-reckoning
  molds. Opener leads with names describing a situation, not the flagged
  date-first "In [Month Year], [researcher] described..." mold, and carries no
  dangling referent for a reader arriving cold. Closer avoids the "does not exist
  yet"/numbered-questions pattern. Cross-series tics absent: no "By the end you
  will be able to," no "The next time..., ask," no "shown vs projected" set
  phrase, no "honest" as a virtue word.
- Prompt-leakage: authored text compared against commission, brief, and
  handoff. "A shape, not a proof" is the writer's own phrasing, not lifted from
  any brief. The bookends' "this lesson builds..." self-description is the
  template's sanctioned use, not a leak. No planning labels or assignment-
  fulfilled claims.
- Voice-guide borrowing: no distinctive phrase from the Alexander, Aaronson, or
  Simler exemplars appears in the draft.
- Grammar, punctuation: sentences are well-formed; colons introduce lists or
  definitions; no comma splices; em-dash count is 0 (the caption's -1 is a minus
  sign). British spelling is used (neighbouring, licence, cancelling);
  "misjudgment/judgment" is a both-acceptable variant, so I left it rather than
  legislate trivia the standard says not to.

Furniture: three components, each earning its place and each in a different
section. The source asset (Fig.1) is inspected under Reader/asset notes below;
the four-assumption table is the load-bearing device and reads clean; the GPT-2
timeline compresses the withhold -> replication -> release sequence honestly. No
Verdict block (correctly, per press direction). Nothing to add or remove.

## Reader

Read straight through as the paper's declared reader — smart, widely read, new
to AI governance. What I have that the sources alone would not give me: a single
four-assumption test I can apply myself to decide whether a given release "is the
curse," and that test run against GPT-2, Llama, and the anti-open-release
governance literature, landing on a bounded judgment — the theorem is proven and
narrow, the release-labelling is analogy, and the one piece that carries over is
the counting. The 2016 paper contains no AI example, so this mapping is the
article's own work; it matches the handoff's original-work sentence. Both
answers survive.

The prose sits closer to the voice-guide exemplars than to a median summary. It
builds the argument at full strength before testing it (Alexander's steelman),
keeps the proof/analogy distinction exact rather than letting the general worry
absorb it (Aaronson's square-root discipline), and closes bounded, handing the
judgment to the reader (Alexander's "no positive answer" register). The headline,
read last as the largest claim, is specific, supported, and carries no false
label.

## Edits

- Corrected source 4 (TechXplore) display text from the paraphrase "Researchers
  replicate the GPT-2 text generator OpenAI held back" to the outlet's verified
  headline "Fake news model in staged release but two researchers fire up
  replication."

## Required work

- writer: run a fresh proof on the edited article (the title correction is the
  only change; source count and numbering are unchanged, so no renumber). Then
  the orchestrator stamps.
- No researcher work. No unresolved evidence gap.

## Decision

approve — the naming guardrail holds, every claim traces to a read source with
no fabricated quote, the shown-vs-analogy beat is drawn in the piece's own words,
and the one flagged issue (source 4's title) is fixed directly; only a
confirming proof and stamp remain.
