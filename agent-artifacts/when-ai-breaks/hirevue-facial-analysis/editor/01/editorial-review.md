# Editorial review: when-ai-breaks/hirevue-facial-analysis (editor/01)

## Skeptic

Thesis: HireVue scored job candidates partly on their faces at large scale; the
facial scoring rested on a premise the science rejects, so it failed as
measurement (a construct-validity failure, not a training-data problem); HireVue
withdrew the component but framed the removal as a value decision and never
conceded invalidity; and the same infer-a-trait-from-a-face move is still sold.

The claims it stands on, and how each held:

1. The product scored candidates partly on faces, at scale. Held. The
   employability score on word choice, tone, and facial movements, and the 2019
   reach (100+ companies, 1M+ applicants), are carried by MIT Technology Review
   (s1) and EPIC (s2, ¶23, ¶31); I opened both. The 2021 platform totals (18M+
   interviews, 114M chat engagements, 700+ customers) sit on HireVue's own
   release (s5), which I confirmed, and the draft correctly marks them
   platform-wide rather than AI-scoring reach.

2. The facial scoring was invalid measurement. Held, at the right altitude. This
   is the claim I pushed hardest on, because the tempting overstatement is that
   Barrett et al. tested and refuted HireVue's tool. The draft does not make that
   error: it says Barrett removes the precondition (faces do not reliably and
   specifically reveal an inner state) and that HireVue's trait/competence claim
   is a further step the review does not itself run. The blockquote is verbatim
   against s4; I confirmed the source and the executive-summary finding.

3. HireVue framed the removal as value, never conceding invalidity or bias.
   Held. Attribution is clean: "scientifically baseless" is never put in
   HireVue's mouth. The invalidity case is carried by Barrett (s4) and EPIC (s2);
   HireVue's framing ("visual analysis no longer significantly added value") is
   quoted and labelled as the company's own (s5). I confirmed the release wording.

4. The same inference is still sold. Held. Barrett's "continues to fuel
   commercial applications in industry and government" is quoted verbatim (s4).

Display-text audit. The one real break was the date label. The headline, dek,
`<title>`, and nb-meta title/dek all read "dropped it in 2020," and two body
positions (the orientation and the takeaway) plus the section heading repeated
the bare 2020. That year rests only on HireVue's own account ("early in 2020,"
per s5); the verifiable public event is the January 12, 2021 announcement. In an
accountability story, stamping the company's self-reported proactive-removal year
as the paper's own finding adopts the framing the piece is otherwise careful to
attribute. The writer flagged this in the draft handoff as an open question. Fix
made directly: display text now anchors on the verified 2021 announcement, and
the body attributes the 2020 timing to HireVue's announcement rather than stating
it flat.

Every other display descriptor checks out: the executive titles (Larsen, CTO;
Mondragon, chief IO psychologist; Parker, chairman and CEO) match s2 and s6; the
statute label (820 ILCS 42 / Public Act 101-0260, effective Jan 1, 2020) matches
s3; the two weight figures and the two deployment pairs are dated and kept
separate. No FTC order is implied. The ORCAA audit is held to its scope (one
early-career assessment, no technical-design evaluation, NDA, no construct
validity).

Citations. I opened all eight hrefs as printed. Six resolve to the correct source
and carry the cited content (s1, s2, s5, s6, s7, s8; the EPIC PDF s2 downloads as
the complaint itself). Two returned automated-fetch errors on the correct
canonical URLs: s3 (ilga.gov, HTTP 503) and s4 (journals.sagepub.com, HTTP 403
bot-block). These are the same transient/bot conditions the researcher recorded,
not miscitations, and the writer's prior proof passed link checks against them.
The data-nb-kind labels pass the primary/secondary test (4 primary, 4 secondary),
meeting the source policy.

No unsupported claim survived and no central claim broke, so nothing routes to the
researcher.

## Cut

Slop pass, every sentence including display text and furniture. The piece was
already lean; the failures were few.

Cut as slop or misplaced address:

- "and that is where it fails" (measurement) — a forward signpost pointing at
  reasoning the next paragraphs do; the argument reaches the failure without it.
- "The finding is narrow and firm at once" — an empty-conclusion opener (idea +
  copula + assessment); the concrete sentence after it already teaches the
  duality it named.
- "Start with the smaller version of the claim..." recast to a declarative
  ("The smaller version of the claim is..."). The imperative addressed the
  reader, which the lesson template confines to the two bookends.
- The still-for-sale close ("put to it the question... What evidence links...?")
  recast to a declarative with the question embedded after a colon. It carried a
  second-person imperative and a rhetorical question at the reader, both
  disallowed in the body.

Negative parallelism: three "X, not Y" contrasts remained after the pass. Two are
earned against misconceptions the piece names and I kept them (the law "governs
notice and consent, not whether the measurement means anything"; the removal was
"a matter of value, not of validity"). The audit one sat two paragraphs from the
value/validity one and read as a local mold, so I recast it into two sentences
("The audit tested a fairness process. It did not test whether the scoring
measures what it claims."). The remaining "platform-wide count, not the reach of
the AI video scoring" is a factual clarification of a figure, not a rhetorical
reversal, and stays.

Edges, delete test, dangling referents: the section openers and closers each
carry a fact or a step; none is a summary of the piece's own method. No prompt
leakage (the bookend roadmap is the template's allowed self-reference; the
reader-situation language is reported, not lifted). No borrowed phrasing from the
voice-guide exemplars: the draft follows their technique (state each side at
strength, let the source's words carry the verdict, anchor a figure the reader
cannot scale against one they can) without taking their words.

Formula check against the recent catalogue: the old headline shared the recent
plain past-tense actor-verb-object DNA; the rewritten two-part narrative headline
("scored... then announced in 2021 it had dropped the practice") breaks it and is
not possessive. The closer does not open with "Today's..." and does not reuse the
recent closer shapes. Headings are varied and none is a scaffold slot; I changed
"The face comes out in 2020" to "HireVue calls the removal a value decision,"
which also removes the contested year and states the section's step.

Furniture: the note (the Barrett quotation, deliberate emphasis on the
load-bearing finding) and the table (the two weight accounts, which prose alone
would blur) each earn their place; both are documented components used correctly.
The body carries no Verdict note or finding-restating block, so the takeaway
bookend holds the judgment as press/editorial.md requires. Nothing added or
removed.

## Reader

Read straight through as the paper's reader, the piece gives what the sources do
not hand over separately: why a face-and-voice score fails as measurement rather
than as biased data, so that no better training set can rescue it; what HireVue
actually removed versus kept, and why its value framing does not settle the
validity question; and a portable test for the same inference in a proctor or a
workplace monitor. That synthesis sets the two weight accounts and the
commissioned audit against Barrett to show the weighting contest was beside the
point, which is exactly the original-work claim in draft-handoff.md, and the
article delivers it rather than restating it. The prose sits closer to the
voice-guide exemplars than to a median summary: flat, concrete, and content by
content, with the cited sources' own words carrying the verdicts.

## Edits

- `<title>`, nb-meta `title`, and `<h1>`: "then dropped it in 2020" to "then
  announced in 2021 it had dropped the practice" (verified announcement date).
- nb-meta `dek` and visible dek: replaced "HireVue dropped it in 2020 without
  conceding it was invalid or biased" with "HireVue framed the removal as its own
  value decision, without conceding it was invalid or biased."
- Orientation: "and, until 2020, facial movements" to "and, until HireVue removed
  it, facial movements."
- Withdrawal heading: "The face comes out in 2020" to "HireVue calls the removal
  a value decision."
- Withdrawal opening sentence: recast so the January 12, 2021 announcement is the
  stated fact and the "early in 2020" removal is attributed to that announcement.
- Takeaway: "took the face out in 2020" to "took the face out."
- Measurement: cut "and that is where it fails."
- Measurement: cut "The finding is narrow and firm at once."
- Measurement: "Start with the smaller version of the claim, whether..." to "The
  smaller version of the claim is whether..."
- Audit: "tested a fairness process, not whether the scoring measures what it
  claims" split into two sentences.
- Still-for-sale close: recast the imperative-plus-question into one declarative
  sentence with the question after a colon.

## Required work

- writer: a fresh proof is owed because prose changed (headline, dek, `<title>`,
  nb-meta title/dek, and several body sentences). The link re-check should confirm
  s3 (ilga.gov) and s4 (journals.sagepub.com) still pass; both are the correct
  canonical sources and returned only transient/bot errors to a manual fetch.
- orchestrator: re-stamp before the PR. The cuts and rewrites move the word count
  and reading time off the stamped 2199 / 10 min, and nb-meta must be brought
  current.

No researcher work: the evidence record is complete and supports every surviving
claim.

## Decision

approve — every claim holds and the citations resolve; the one display-text break
(HireVue's self-reported 2020 timing presented as the paper's own) and the few
slop and reader-address sentences were fixable in place, leaving only the
mechanical re-stamp and a fresh writer proof owed for the prose changes.
