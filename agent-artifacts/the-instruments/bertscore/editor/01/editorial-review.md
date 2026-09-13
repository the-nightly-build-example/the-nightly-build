# Editorial review: the-instruments/bertscore (editor/01)

## Skeptic

Thesis: BERTScore grades how much a candidate resembles a reference in a
pretrained encoder's representation, not by shared words; that is more than word
counting and often beats BLEU on translation, but the resemblance is the
encoder's own, so a high score does not promise a correct sentence, two scores
are comparable only within one configuration, and the encoder's blind spots and
biases pass straight through.

The claims it stands on, and how each held:

1. The mechanism (token to vector, greedy cosine match, average into
   precision/recall/F1). Verified against the paper's Sec. 3 and the evidence
   record's formula. The annotated recall equation and its three-term legend
   match the primary exactly (x is the reference, |x| its length; the legend's
   "reference token / candidate token this reference token resembles most /
   average over every reference token" is correct). The cosine-to-dot-product
   reduction for normalized vectors is the paper's own. Held.

2. Rescaling arithmetic and scope (the round's first focus). Recomputed:
   0.959333 to 0.759045 rounds to 0.959 to 0.759; 0.9311 to 0.5758 rounds to
   0.931 to 0.576. Both are the source's own reported before/after values, not
   the article's arithmetic, and the article cites each to its owner (README
   example pair to s3/s4, WMT18 De-EN corpus to s3/s4, the paper's formula and
   ~1M-pair baseline to s1). Solving the rescale formula backward from each pair
   gives a consistent baseline near 0.83, so the two figures are internally
   coherent. Every figure carries its scope in the prose ("one example pair from
   the documentation," "across the WMT18 German-to-English set," raw band "often
   between 0.85 and 0.95"). Held; I fixed one clarity item (semicolon to period)
   noted under Cut/Edits.

3. Function-word blindness (Hanna & Bojar, s5) and its tension with the paper's
   PAWS robustness (the round's second focus). Both are present and reconciled,
   not hidden: the article states PAWS reorders content words (which the matching
   catches) while a swapped function word barely moves the vectors, and closes
   "standing up to the first kind of change buys no protection from the second."
   That is exactly the evidence record's reconciliation, and the robustness
   result is not offered as a general robustness claim. Held.

   One break, fixed. The draft placed the figures "correct translations averaged
   an F1 of 0.815, and the function-word cases fell only to 0.712" immediately
   after "the broken tag question barely lowers the score," which invited the
   reader to take 0.712 as the wrong candidate's score. Both figures are Hanna &
   Bojar's Table 1 means for *correct* translation pairs (0.815 overall, 0.712 in
   the function-word category); the wrong-candidate point is carried by the
   condition-(ii) accuracy (42.9% vs 75.5%). I recast the sentence to attribute
   0.815/0.712 to correct translations and to lean the "barely penalized" point
   on the 42.9% accuracy, changing no number and no citation. The reasoning added
   ("little room left to mark a wrong one down") follows from the compressed band
   plus the near-coin-flip accuracy, both in the record.

4. Inherited bias (Sun et al., s6). Reference sentence matches verbatim; 70.14
   vs 38.87 and the 31-point gap, the 0-to-100 scale, the ~7 average gap vs
   traditional metrics near or below 3 all match the record. Held.

5. "Not the strongest metric" (Kocmi s7, SummEval s8). Kocmi values (COMET 96.5,
   BLEURT 93.8, BERTScore 92.2, BLEU 88.2) and the SummEval figures (F1 ~0.04
   consistency below ROUGE-1 0.53; recall 0.66, precision negative) match the
   record. One attribution overreach, fixed: the draft had the study recommend
   "BLEURT and COMET"; Kocmi recommends COMET specifically, so I pointed the
   recommendation at COMET.

Display text, descriptor by descriptor: five author names, the ICLR 2020 date,
roberta-large as default encoder, ~130 models, the version-hash string
(character for character against the record), the WMT18 De-EN scope, the tag
question, the carpenter/clerk reference, and every quantity check out against the
owning primary. The version-hash "compliance" question (third focus) is handled
correctly: the article states the request exists and borrows from sacreBLEU, and
makes no claim about whether practitioners follow it.

data-nb-kind audit: s1 (paper), s3/s4 (authors' own repo and journal), s5-s8
(each study owning its findings) are correctly primary; s2 (Hugging Face card,
third-party redistribution) is correctly secondary, and the only argument it
carries is adoption/context. Floor met (8 sources, 7 primary, 1 secondary).

Links: I opened all eight source hrefs plus both Go-deeper links. Every one lands
on the named source, including the two adjacent WMT URLs that are a swap risk
(s5 = 2021.wmt-1.59 is Hanna & Bojar; s7 = 2021.wmt-1.57 is Kocmi) and the deep
link s4 (the rescaling journal, which carries the 0.9311 to 0.5758 line). All
five internal Background targets exist in the library checkout.

No central claim broke; no evidence is missing for what the article asserts; no
source-policy failure. Nothing routes to the researcher.

## Cut

This is a genuinely clean draft on slop. On the sentence-by-sentence pass, the
edge pass, and the delete test I found no empty conclusion, no unearned
punchline, no puffery, no vague attribution, no decorative analysis, and no
fluff opener. Zero sentences failed the slop test and were cut.

Negative parallelism appears three times and each earns its place against a
misconception the piece names: "grades meaning rather than word overlap" (the
framing the lesson spends the article complicating, and attributed with "often
described as"), "instead of matching words, it matches..." (against the
word-counting of BLEU/ROUGE just established), and "over dozens of tables rather
than one figure" (a sourced fact about how the paper presents its evidence).
None is a strawman.

Bookend self-reference is confined to the two cards the lesson template allows,
and both cards say something specific to this lesson (the mechanism it will
follow; the two things the reader will be able to do by the end). The body
speaks to no one and never narrates itself. No prompt leakage: the article's
angle sentences are its own, with no lifted commission framing, planning labels,
or assignment-fulfilled claims. No phrasing borrowed from the voice-guide
exemplars (Miller/Gregg/Olah).

Punctuation, against the editorial direction's period-default: I converted two
reflex semicolons to periods (the rescaling data-point sentence; the PAWS
catch/miss contrast). Zero em-dashes and zero en-dashes in the piece. One
imprecision fixed: cosine similarity is exactly bounded in [-1, 1], so "between
about -1 and 1" became "between -1 and 1."

Formula check against the recent Instruments record (the round's fourth pattern
focus). One heading was built to a prior article's mold: "One output, several
different numbers" is the same "One [X], [N] different [Y]s" construction as
the-instruments/mteb's "One average, eight different rulers." I rewrote it to
"Two BERTScores are rarely the same measurement," which is the section's own
claim in the piece's own nouns. Separately, two of the four body headings opened
with "What ..." ("What BERTScore actually compares" and "What a high score does
not promise"), which the headline standard's "vary how they are built" rule
discourages; I recast the weaker, more generic one ("What BERTScore actually
compares") to "Meaning as a language model sees it," which states the
orientation section's step and threads the article's thesis. The four headings
now skim as the argument: it compares meaning as a model sees it, every token
finds its partner, two BERTScores are rarely the same measurement, what a high
score does not promise. The headline and dek clear the desk's banned molds
(no "a metric can hide/misled," no single-dramatic-number dek, no comma triad,
no semicolon reversal, no suspended question).

Furniture: the one annotated equation is the right call and the catalog's
one-per-article limit is respected; its markup is correct and I left it to the
writer's domain untouched in substance. I considered a small ranking table for
the Kocmi comparison (four metrics with scores) and the SummEval figures, and
judged the prose clear enough that a table would be optional variety rather than
a comprehension gain, so I added none. There are no charts and no source assets,
so there was no chart provenance or crop to inspect.

## Reader

Read straight through as the paper's declared reader: what I have that the
sources alone would not give me is a single derivation that builds recall,
precision, and F1 out of one greedy cosine-matching rule, and then reads every
limitation back off that same "resemblance in the encoder" idea, including the
non-obvious reconciliation that the paper's PAWS robustness and the later
function-word failure are compatible rather than contradictory. Seven separate
papers plus a repo would leave the reader to assemble that; the article assembles
it and shows each limit following from the recipe. The draft-handoff's
original-work sentence claims exactly this, and the article delivers it. The
prose sits with the voice-guide exemplars, not a median summary: concrete worked
cases (the river/money "bank," the tag-question pair, the pronoun pair, the
rescaling numbers) and hard conclusions stated without hedging.

On the round's fifth focus (no per-token cosine worked example in the evidence):
I judge the mechanism does land without one. The annotated equation shows the
operation's structure concretely, the rescaling arithmetic runs on real numbers,
and the token matching is shown as a real case on the tag-question pair. The
template's bar is a worked example "with real numbers or a real case," and a
real case is present; inventing per-token cosine values would breach cite-only,
and the record supplies none. This is a strengthening opportunity, not a
publication blocker, so I did not route it. The headline is the one place I most
weighed a change: it is more definitional than the desk's finding-forward
headlines, but "look alike to a language model" is the load-bearing surprise
(the resemblance is the model's, which the whole limits half pays off) and the
dek carries the costs, so I judged it in-standard and left it.

## Edits

- Retitled section heading "What BERTScore actually compares" to "Meaning as a language model sees it" (broke a two-of-four "What ..." repetition; states the section's step).
- Retitled section heading "One output, several different numbers" to "Two BERTScores are rarely the same measurement" (broke the mteb "One average, eight different rulers" formula mold).
- Changed "between about -1 and 1" to "between -1 and 1" (cosine is exactly bounded).
- Changed the rescaling data-point semicolon to a period ("...becomes 0.759. Across the WMT18...").
- Recast the Hanna & Bojar figures to attribute 0.815/0.712 to correct translation pairs and to rest the "barely penalized" point on the 42.9% accuracy; no number or citation changed.
- Unified the PAWS description to "reorders" in both mentions ("an adversarial test that reorders a sentence's content words to change its meaning") and changed its catch/miss semicolon to a period.
- Corrected the Kocmi recommendation from "BLEURT and COMET, which the authors recommended instead" to "The authors of that study recommended COMET instead" (the study recommends COMET specifically).

## Required work

None. Every issue found was editor-fixable and is fixed in the article.

## Decision

Approve. The mechanism is accurately derived and every figure checks against its
owning primary with its scope; the two focus contradictions (PAWS vs
function-word blindness, and the unsourced hash-compliance question) are handled
correctly; the draft carried no slop to cut; and the two heading formulas, the
figure-attribution ambiguity, and the reflex punctuation were all repairable in
place.
