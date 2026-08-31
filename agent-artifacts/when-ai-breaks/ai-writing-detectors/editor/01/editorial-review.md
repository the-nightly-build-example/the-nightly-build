# Editorial review: when-ai-breaks/ai-writing-detectors (editor/01)

## Skeptic

Thesis: an AI writing detector judges text by how predictable it is (low
perplexity), and that single property makes the same tool both systematically
wrong against plain and non-native human writing, which produces false
accusations, and trivially beaten by paraphrase, which lets a real cheat through.
The tool was sold on a sub-1-percent false-positive claim, students were accused
on its flags, and it is still sold and still deciding cases. The piece stands on
these claims:

1. Turnitin switched the detector on in April 2023 for its whole installed base
   (thousands of institutions), marketing a document-level false-positive rate
   under 1 percent. Held. Owned by s1 (gated 403 but resolves; now returns 200),
   independently restated by Vanderbilt (s4) and Inside Higher Ed (s9). The
   38.5M-submissions / 9.6% >20% / 3.5% >80% figures are cited to s2 and match
   the evidence exactly.

2. A low rate becomes hundreds of accusations at institutional scale: at 1% of
   Vanderbilt's ~75,000 2022 papers, ~750 could have been wrongly flagged;
   Vanderbilt disabled the detector on August 16 2023. Held. 1% x 75,000 = 750,
   arithmetic correct; date and reasons (false accusations, opacity, non-native
   bias) match s4. The real-accusation claim is cited to s3 (WaPo); no individual
   student is named, consistent with the paywalled record and the brief.

3. Mechanism: detectors score perplexity, low perplexity reads as machine, and
   plain or non-native writing sits in that low-perplexity range. Liang et al.
   measured a 61.22% average false-positive rate on non-native TOEFL essays
   against near-perfect accuracy on native US eighth-grade essays, 18 of 91 TOEFL
   essays flagged unanimously by all seven detectors, and a fall to 11.77% after
   the essays were rewritten with richer vocabulary. Held. All figures match the
   evidence and are cited to s5. Direction correct (richer vocabulary -> fewer
   flags; lower perplexity -> more flags). Perplexity is linked to
   the-instruments/perplexity, not re-taught; only its direction is used.

4. Two-operator precision, the round's hardest push. Held and kept distinct.
   OpenAI FULLY WITHDREW its own AI Text Classifier (26% true-positive / 9%
   false-positive on its own set; pulled, verbatim July 20 2023 note in the
   nb-note furniture, cited s7/s8). Turnitin did NOT withdraw: it conceded a
   ~4% sentence-level rate against its under-1% document-level claim, added an
   under-20% asterisk, and kept selling (Chechitelli, chief product officer,
   cited s9). The article states each separately and contrasts them in the close.
   No conflation.

5. Scope of the harsh figures. Held. 61.22% is labeled Liang's average on
   non-native TOEFL essays, not Turnitin's rate; the body states plainly that
   Turnitin's detector was not among Liang's seven and that the mechanism, not
   the vendor, carries the bias, with Vanderbilt naming it. The Washington Post
   ~50% small-sample figure is not used anywhere, so no small-sample number is
   presented as a general rate.

6. Ceiling: Sadasivan et al. prove the best-possible detector approaches a coin
   flip as models improve, and paraphrase collapses deployed detectors. Held.
   The plain-language rendering of Theorem 1 is faithful (a detector separates
   the two text kinds only as far as they differ; models erase that difference).
   The before/after table figures match the evidence (DetectGPT 96.5 -> 25.2;
   OpenAI RoBERTa 100 -> 60; watermarking 99.3 -> 9.7), cited s6.

Display text checked descriptor by descriptor. Headline ("AI writing detectors
flag non-native students' own essays as machine-written") is the largest claim
and is defended by claim 3; actors named, present tense for the ongoing event.
Dek matches the rendered dekline exactly and the nb-meta dek; it adds Turnitin,
the thousands of schools, the 1% promise and the accusations without restating
the headline, and carries no banned dek mold. Every subhead is a step in the
piece's own nouns and reconstructs the argument when skimmed; none is
scaffolding. Chechitelli's title (chief product officer) is correct against s9.
No other person is named.

Sourcing: 9 sources, 5 primary (s1, s4, s5, s6, s7), 4 secondary (s2, s3, s8,
s9); meets the >=8 / >=4 primary / >=1 secondary policy. Every data-nb-kind is
correct. The two gated primaries (s1 Turnitin, s7 OpenAI) own their figures and
each has independent restatement in the set, so the primary label hides no
missing independent source. Per-section citation coverage holds in every
non-exempt section.

Links: opened all ten printed hrefs. s6, s8, s9, s2, s4 and both arXiv addresses
(s6 and the figure's data-nb-url 2304.02819) return 200. s1 returns 200. s5
(cell.com) and s7 (openai.com) return 403 bot gates that still resolve. s3
(washingtonpost.com) returns no HTTP response over HTTP/2 or HTTP/1.1: the proxy
tunnel connects (200 Connection Established), the host is not an egress-policy
denial (no 403/407, not in the proxy's recent relay failures), and it is a
well-formed dated WaPo article path. This is a site-side bot gate, the same class
as the resolving 403 primaries, and does not fail the link. No broken link.

No central claim broke. Nothing routed to the researcher; the evidence supports
the piece end to end.

## Cut

Ran the sentence-by-sentence slop pass, then the edges alone, then the
dangling-referent and delete tests, against spec/slop.md. The draft is clean at
the sentence level and written in the ProPublica register the voice guide asks
for: facts placed in order, the mismatch between a flagged essay and its real
author left to stand without an adjective. Four sentences failed and were cut:

- Orientation: "That share has a name a lot of teachers were about to learn." A
  decorative lead-in to the false-positive-rate definition. Fails the
  noun-replacement test and the delete test; the definition stands on its own.
- Accusations, section opener: "The accusations were real and had names attached
  to them." Tells the reader what the next sentence shows (the WaPo students).
  Cutting it opens the section on the concrete WaPo fact, which the voice guide
  prefers.
- Ceiling: "The argument is short to state." A summary of the article's own
  method, cut per the signpost/delete test.
- Ceiling: "Watch where the paraphrase leaves it." A body sentence that addresses
  the reader with an imperative ("Watch"), which the lesson template forbids
  outside the two bookends, and a lecture-opener tell. Cut.

Furniture read as prose: the figure caption, table caption, and nb-note are
factual and free of slop. Earned contrasts were checked one by one and kept, each
correcting a misconception the piece actually names: "it does not read for
meaning, it reads for how predictable your sentences are" (the thesis); "That
last reason is not particular to Turnitin. It is how every one of these detectors
works" (bias is structural); "A low score is a statement about predictable
writing, never about honesty" (the lesson's point). None is an invented strawman.

Punctuation: the one semicolon (takeaway: "OpenAI read those results and pulled
its detector; Turnitin read them, added an asterisk, and kept selling") is a
valid tight parallel antithesis, not a splice. No em-dashes in the body. No
grammar or syntax breaks found.

Prompt-leakage and borrowed-phrasing passes: no commission or brief framing
lifted; the only self-reference is in the bookends, where the template allows it.
No distinctive clause borrowed from the voice guide's quoted writers.

Recent-pattern check against the five recent when-ai-breaks deks and the
mcdonalds shape: this dek is a two-clause causal ("sold... promising... and
students were accused"), not the McDonald's "spent... then switched it off" or
the SafeRent "did X and never Y" mold; the headings vary in build; there is no
nb-figure "three things have to work" section and no verdict block. Shape
differs. No formula.

## Reader

Read straight through as the paper's declared reader. What I have that the sources
alone would not give me: one causal account tying four separate results into a
single chain, that the one property a detector measures, low perplexity, is what
makes it both unfair to plain and non-native writers and useless against anyone
who paraphrases, so the same mechanism explains the false accusation and the
missed cheat, and the tool is sold anyway. No single source says this; Liang,
Sadasivan, OpenAI and Turnitin each own one link. The draft-handoff's original-work
sentence claims exactly this fusion, and it survives the read. The prose sits
closer to the voice-guide exemplars than to a median AI summary: it shows the
mechanism on a real flagged corpus rather than defining machine-like text in the
abstract, and it lets the vocabulary-rewrite result carry the point without an
adjective. The headline, reread as the largest claim, is defended.

## Edits

- Cut "That share has a name a lot of teachers were about to learn." from the
  orientation section (decorative signpost).
- Cut "The accusations were real and had names attached to them." from the top of
  the accusations section (tell-not-show; the WaPo sentence now opens it).
- Cut "The argument is short to state." from the ceiling section (method summary).
- Cut "Watch where the paraphrase leaves it." from the ceiling section
  (body sentence addressing the reader; not permitted outside the bookends).

## Required work

writer: The table's before/after scale is misdescribed and needs the source in
hand to fix. The body sentence "One common score runs from 50, a coin flip, up to
100, perfect." and the DetectGPT row's "detection score, 50 to 100" cell both
assert the score's floor is 50, but the same DetectGPT row shows an after-value
of 25.2, below that floor. AUROC ranges 0 to 100, and 25.2 means worse than a
coin flip; the "50 to 100" claim is contradicted on its own line. The framing
also implies all three rows share one 50-floor scale, but only DetectGPT's row is
that score: the OpenAI RoBERTa row ("AI text caught at a 1% false-alarm setting")
and the watermarking row ("watermarked text detected") are rates that run 0 to
100 with a floor of 0, where there is no coin flip at 50. Reframe so the scale
statement is honest for each metric and is not contradicted by DetectGPT's 25.2,
without altering any number (all six values match the evidence and are correct).
I removed the reader-addressing "Watch where the paraphrase leaves it." that
followed the scale sentence, so the writer can supply a clean, non-addressing
lead-in if one is wanted. This is the only blocking item.

Note for the orchestrator: only prose was edited plus this one furniture-cell
reframing routed to the writer; re-run nb stamp and nb check after the writer's
fix. The word count will drop from the four cuts.

## Decision

revise. The reporting, sourcing, two-operator precision, and figure scopes all
hold, and the prose edits are done; one furniture defect remains, the table's
"50 to 100" scale claim contradicted by DetectGPT's own 25.2, which needs the
writer and the Sadasivan source to correct honestly.
