# Editorial review: the-mechanics/negation (editor/01)

## Skeptic

Thesis: one weakness — negation is rare in training text and weakly rewarded by
the next-token objective — surfaces twice, in a text language model and in the
text encoder of an image generator, so the single word meant to remove something
is the easiest for a model to override. The piece stands on four load-bearing
claims, and I tried to break each.

1. **Text models treat a negated sentence like its affirmative twin.** Ettinger's
   BERT prefers the true completion in 100% of affirmative category sentences and
   0% once "not" is added, on 72 NEG-136-SIMP items. Verified against the evidence
   record (Table 12, both model sizes) and the source landing page (s1,
   arxiv 1907.13528, correct paper and author). Kassner and Schütze corroborate at
   scale: 42,867 negated cloze sentences, fact-vs-negation rank correlation above
   85% for most sources. Verified (s2, ACL 2020, correct paper; quote in the note
   matches the record). Held.

2. **The cause the authors give is data, and it is a hypothesis, not a count.**
   The article states this correctly: "the authors of both studies offer the same
   explanation, and it is an explanation rather than a counted figure." Ettinger's
   natural-vs-stilted split (BERT-large 100% on naturally phrased negatives, 0% on
   stilted ones, attributed to training frequency) is reported in the right
   direction and is the actual clue that frequency tracks the failure. This is the
   round's central honesty check, and the piece passes it: no corpus statistic is
   ever attached to the rarity claim, and the settled-list explicitly excludes it.
   Held.

3. **The text failure is dated, and the counter-current is on the page.** The
   article locates the crisp failure in "masked and early autoregressive models,"
   then reports the instruction-tuning counter-current (Truong: RTE-neg 0.525 base
   GPT-3 to 0.767 InstructGPT; FLAN-T5-XXL 11B beating the 175B base on most NLI
   tasks) and the authors' own note that newer chat models may already beat the
   paper. It keeps the inverse-scaling caveat (bigger did worse on the sensitivity
   test) so the "scale fixes it" story is not overstated in the other direction.
   The weakness is placed in "the data and the prediction objective, not... a wall
   in the architecture," grounded in the balanced-corpus result (pretrained 0.2,
   fine-tuned 1.0). All figures verified against the record (s3, correct paper).
   Held, and honestly bounded.

4. **The image case is inference from discriminative evidence, not a measured
   generation rate.** The bag-of-words result is real and measured: shuffling all
   caption words drops CLIP Recall@1 only 50.3% to 34.1% (verified, s4, correct
   paper), and NegBench finds VLMs at chance on negation across 79,000 examples
   (verified, s5, quote exact). The article then spends a full paragraph demoting
   the generated "no elephant" to "an inference, though a sound one," and states
   plainly "it is not a measured generation-failure statistic, and no one should
   quote it as one." This is exactly the required framing. Held.

Engineering patch: classifier-free guidance is cited to Ho and Salimans (s6,
correct paper, class-conditional image generation), and the article is careful
that they "never wrote about user-supplied negative prompts" — the extension is
attributed to later tools and explainers (s7 AI Summer, s8 Hugging Face
Diffusers, both secondary and both correctly labeled). Verified.

Display text, descriptor by descriptor: headline states the finding in the
piece's own nouns and avoids both recent Mechanics molds ("A model can X and
still fail Y"; "The thing a model can't do"). Dek makes a world-claim, adds the
mechanism the headline omits, and is not a banned dek mold. Every subhead is a
step-claim in the piece's nouns; none is a scaffolding slot. Every named figure
(100/0, >85%, 0.525/0.767, 0.2/1.0, 50.3/34.1, 79,000) checks against the record
with correct denominators and directions.

`data-nb-kind` audit: s1-s6 primary (each owns its experiment/method), s7-s8
secondary (an explainer and library docs). All correct; the two secondaries carry
only the negative-prompt-as-CFG reading, which the prose already flags as
secondary interpretation. No mislabel hides a missing independent source.

Every citation href opened as printed. All eight source links and both Go-deeper
links (Ettinger TACL 2020.tacl-1.3, NegBench 2501.09425) resolve to the source
itself. Four internal cross-links (word-order, image-generation,
autoregressive-generation, attention) resolve to existing library files; the two
Background descriptors and two in-body link phrases match their targets'
subjects.

One number-handling note, checked and judged acceptable: "scored near the 50%
chance line" for CLIP on relations and attributes glosses figures the record puts
at ~59% (VG-Relation) and ~62% (VG-Attribution). The article cites no number
here, the direction is right, and "near chance" is the source's own framing for a
model that should sit near 100%. Left as written.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

One dedicated slop pass over every sentence, then the edges alone, then a
cold-link read, then the delete test.

One sentence failed and was cut: "Two caveats keep this honest." It grades the
article's own method ("keep this honest") and signposts the two qualifying
sentences that follow. Both caveats read plainly as qualifications without the
announcement, and the turn from the instruction-tuning result to "bigger models
did worse" now lands concretely instead of being pre-labeled.

Negative-parallelism reflex checked at every occurrence, since this piece leans on
contrast. Each surviving instance corrects a misconception the piece names and
the evidence records: "these look like two unrelated quirks; they are one
weakness" (the article's whole contribution), "at the data and the prediction
objective, not at a wall in the architecture" (the architecture-can't view is a
real alternative in the record), "instruction tuning, not raw scale, is the lever"
(scale is shown to move the wrong way), and the closer's "not whether it drops the
word but where" (reframing the named "just ignores negatives" folk account). None
is an invented strawman; all stay.

Edges walked out of order. The article's last sentence states the conclusion the
argument built (three named loci: data, objective, encoder) and survives the
placeholder test on its nouns. Section openers and closers carry facts or the
settled/open frame, not empty orientation. The one remaining signpost-shaped line,
"Most of those steps are settled engineering, and the last one is still open,"
carries a substantive claim that organizes the piece and was kept.

Borrowed-phrasing check against the voice-guide quotations (Evans, Willison, Luu):
the article's distinctive lines ("bets on the words it has seen most," "the
training data almost never says no," "hands the generator the elephant") are its
own subject nouns; nothing is lifted from the exemplars.

Prompt-leakage check against commission and brief: the bookends' learning-goal
sentences ("spot an explanation that skips a step," "you have the missing step
ready") are the template's required statement of what the reader gains, and the
"just ignores negatives" folk account is a reported reader situation, not a lifted
instruction. No selection rule or assignment-fulfillment claim in the body.

Furniture: two stat strips (100/0 and 50.3/34.1) carry the two systems' thesis
numbers and are cited in adjacent prose. One nb-note holds the Kassner quote as
deliberate emphasis of the fact-equals-negation collapse in the authors' words;
the desk's nb-note-by-habit tendency was weighed, and a single purposeful
quotation note is within the catalog and earns its place. The settled/open mark is
folded into the negative-prompts section rather than given a separate
"where-the-explanation-runs-out" heading, breaking the recent formula. No
component removed or added.

Punctuation: no em-dashes; the one semicolon (text mechanism; image mechanism)
binds two tightly parallel clauses and is within the rare-use allowance; colons
introduce lists or payoffs. Grammar and syntax clean throughout, including display
text and furniture.

## Reader

Read straight through as the paper's declared reader: I come away able to say why
"not" underperforms in two different systems and to name where it fails (rare in
the data, dropped by the prediction objective, flattened by a bag-of-words
encoder), and I can tell a measured result from an inferred one and a settled step
from the open one. The sources alone would not give me this: no single paper
connects the text 100-to-0 collapse to the CLIP word-shuffle result, and none
draws the measured/inferred and settled/open lines for a lay reader. The
draft-handoff's original-work sentence claims exactly this join plus the explicit
demotion of the generated case and the dating of the text failure, and the article
delivers both. The prose sits closer to the voice-guide exemplars than to a median
summary: numbers before adjectives, real prompts and their wrong outputs, and
uncertainty marked at the sentence where it applies. The headline, read last as
the largest claim, is a specific finding the piece defends.

## Edits

- Cut "Two caveats keep this honest." in the "The training data almost never says
  no" section (self-grading signpost; the two caveats stand on their own).

## Required work

None. The one edit is applied; the word count drops by four words, which the
orchestrator's stamp will reconcile.

## Decision

approve — every load-bearing figure verifies, every href lands on its source, the
image case reads as inference and the data imbalance as hypothesis, the text
failure is dated with its counter-current, and the settled/open boundary is drawn
honestly; the single slop line was cut directly.
