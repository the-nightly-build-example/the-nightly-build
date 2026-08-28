# Editorial review: when-ai-breaks/cnet-ai-articles (editor/01)

## Skeptic

Thesis: a major newsroom published AI-drafted finance copy as vetted staff
work, and the failure was not that a model produced a false number but that
fluent prose let a wrong number pass the human check the byline promised. The
piece stands on four claims, each tested against the evidence record and the
cited sources.

Claim 1 — the flagship error. The AI wrote that $10,000 at 3 percent would
"earn $10,300 at the end of the first year," when the interest earned is $300
and $10,300 is principal plus interest. I opened Futurism's error report
(futurism.com/cnet-ai-errors) and confirmed the quote verbatim, including the
matching $25,000-at-4-percent "flat $1,000 in interest per year" car-loan
error. Arithmetic checks: $10,000 x 3% = $300; the article's "overstate a year
of savings by more than thirtyfold" is right ($10,300 / $300 ≈ 34x). The note
block attributes the quote correctly to "CNET's AI engine ... as quoted by
Futurism." Held.

Claim 2 — the count is not CNET's. The article says Guglielmo "gave no total,"
that the "more than half" figure "did not come from CNET," that The Verge
counted correction notes on the live articles, and that Engadget "put the count
at 41 of the 77 ... an outside tally ... not a figure CNET announced." This is
exactly the record's correction. The word "substantial" stays tied to
Guglielmo's "a small number requiring substantial correction." No number is put
in CNET's mouth. Held — this was the round's highest-risk item and it is clean.
The Verge byline (Sato and Roth, not James Vincent) is not asserted in prose;
source entry s5 carries the correct URL and verbatim headline, so there is
nothing to correct.

Claim 3 — the mechanism, dated. The Kalai et al. paper is introduced as "a 2025
paper," quoted accurately ("sometimes guess when uncertain, producing plausible
yet incorrect statements instead of admitting uncertainty"), and explicitly
framed as postdating: "That paper came out two years after the CNET stories and
says nothing about them. It describes the class of failure, not CNET's
particular tool, whose design the company never published." arXiv:2509.04664 is
September 2025; the incident is 2023; "two years after" is correct. The GPT-3
next-token citation (s10) is generalized responsibly as "a language model of
this kind." Held.

Claim 4 — the Bankrate/plagiarism claim. The article says the AI's sentences
"closely tracked text already published elsewhere, including on Bankrate, a
personal-finance site owned by Red Ventures." I opened Futurism's plagiarism
report (futurism.com/cnet-ai-plagiarism) and confirmed Bankrate is named as a
Red Ventures sister site the AI plagiarized from. The article does NOT assert
Bankrate ran its own AI engine — the unsupported claim the record warned
against. The Forbes Advisor paired quote ("overdraft and NSF fees need not be
the norm" vs "don't have to be a common consequence") matches the evidence
record verbatim. Held.

Display text and labels: headline, dek, and all four subheads checked descriptor
by descriptor. The dek's "77 stories" and "$10,300 in a year" match the record;
it adds to the headline without restating it and avoids the three banned molds.
All eleven `data-nb-kind` labels are correct (5 primary: CNET note, CNET
corrected article, WGA East, Brown et al., Kalai et al.; 6 secondary), meeting
the >=4 primary / >=1 secondary / >=8 total policy. Timeline dates, the
~100-worker union figure, and the WGA quote all match the record.

One break found and fixed: three Futurism source titles (s2, s3, s7) were
content-accurate paraphrases, not the outlets' published headlines — the
evidence record supplied URLs and authors but not verbatim titles. I opened all
three source pages and replaced the descriptive titles with the real headlines
(see Edits). The URLs were already correct and land on the sources.

## Cut

Slop pass against `spec/slop.md`, every sentence including display text and
furniture. Three sentences failed and were cut; no fourth survived on
re-reading the edges.

1. "The staff drew the sharpest line." — a characterization opener that tells
   the reader how to feel about the union, reducing to "the X drew the sharpest
   Y." It also runs against the voice guide's rule that no sentence tells the
   reader how to feel about CNET's decisions. The fact (the unionization)
   follows in the next sentence, so the paragraph now opens on it.
2. "This is the part of the episode worth understanding, and it is not special
   to CNET." — self-grading signpost plus a comma-and join. The generalization
   it gestured at is already carried by "a language model of this kind" and
   stated outright later ("the class of failure, not CNET's particular tool").
   Cut whole, per the delete-don't-repair rule.
3. "The errors were not the only problem the reporting turned up." — a pivot
   signpost reducing to "the X were not the only Y the Z turned up." The
   plagiarism finding in the next clause does the pivoting itself.

The earned contrasts were left in place: "because that string was a plausible
continuation, not because anything computed the interest" and the takeaway's
"not better-sounding output. It is a person verifying the claim" both correct a
misconception the lesson names, so they pass the negative-parallelism test. The
strongest mechanism lines ("a plausible continuation reads exactly as fluent
when it is wrong as when it is right"; "the polish that made the stories
publishable is the same polish that made their errors easy to wave through")
match the voice guide's flat, side-by-side register and stay.

No prompt leakage: the thesis language shared with the commission ("passing AI
copy off as vetted editorial") is the article's own reported point grounded in
the record, not a lifted instruction. No borrowed phrasing from the voice
guide's quoted exemplars. Against the recent-pattern notes: the headline is a
specific "[Actor] [did] [specific]" without a rote clone shape, the dek avoids
comma-triad / semicolon-reversal / suspended-question, and no section heading
uses the comma-plus-"and" two-clause join. No verdict block in the body — the
takeaway lands the judgment, as directed. The timeline, note, and bookends each
carry material; none reads as a formula block.

## Reader

Read straight through as the paper's declared reader, then against the
original-work sentence. What the piece gives that the sources alone do not: it
uses one verified arithmetic error as the worked case that proves next-word
prediction is exactly as fluent when wrong as when right, then separates this
publishing/trust failure from the chatbot failures the reader already
associates with AI, and names the specific guard (a person verifying the claim
plus an honest byline). That synthesis is the article's own; no single source
carries it. Both the reader answer and the original-work sentence survive. The
prose sits closer to the voice-guide exemplars (Angwin's flat declaratives,
Newton's figures set side by side) than to a median AI summary. The headline
holds as the largest claim.

## Edits

- s2 source title: "CNET Has Been Quietly Publishing AI-Generated Articles" ->
  verbatim headline "CNET Is Quietly Publishing Entire Articles Generated By AI".
- s3 source title: "CNET's AI-Written Articles Are Full of Errors" -> verbatim
  headline "CNET's Article-Writing AI Is Already Publishing Very Dumb Errors".
- s7 source title: "CNET's AI-Written Articles Are Riddled With Plagiarism" ->
  verbatim headline "CNET's AI Journalist Appears to Have Committed Extensive
  Plagiarism".
- Cut "The staff drew the sharpest line." from the union paragraph.
- Cut "This is the part of the episode worth understanding, and it is not
  special to CNET." from the mechanism section.
- Cut "The errors were not the only problem the reporting turned up." from the
  plagiarism paragraph.

Re-ran `./nb check ... --no-check-links` after the edits: BLOCK 0, WARN 0,
PUBLISHABLE.

## Required work

None blocking. One optional, non-blocking note for the orchestrator to pass to
the writer at stamp time: the three cut sentences drop the body by roughly two
dozen words, so `nb-meta.words` (1664) now slightly overstates; the writer owns
nb-meta and can refresh it on the next proof. The check passes clean either way,
so this does not gate publication.

## Decision

approve — every round-focus item (count attribution, byline, the postdated
Kalai paper, the compound-interest arithmetic, and the Bankrate plagiarism
framing) is correctly handled in the draft; the only fixes needed were within
the editor's remit (three source-title corrections to verbatim headlines and
three slop cuts), all made in place, leaving the article clean.
