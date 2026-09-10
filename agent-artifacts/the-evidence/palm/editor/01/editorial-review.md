# Editorial review: the-evidence/palm (editor/01)

## Skeptic

Thesis: PaLM was the largest densely activated language model of its moment, but
by the compute-optimal rule DeepMind published a week earlier it saw roughly a
fourteenth of the training data its size called for, and two of its headline
results carry conditions that today's citations tend to drop. The piece stands on
four claims.

Claim 1, the load-bearing comparison. Recomputed from the primaries the article
cites, not from the record's summary: 780B / 540.35B = 1.4435, printed as 1.44
tokens per parameter (correct). Chinchilla 1.4T / 70B = 20.0 tokens per parameter
(correct). Chinchilla's Table 3 compute-optimal budget for a 520B model is 11.0T
tokens; 11.0T / 780B = 14.1, so PaLM saw about one-fourteenth (correct). The
headline "a fourteenth" and the table's three rows (1.44, 20, ~20) all hold. The
one place the piece is careful and right: the third table row is labeled
"Compute-optimal for a 520B model," not PaLM's own 540B, so the ~20 approximation
is honest rather than a false-precision claim about PaLM itself. This is the
strongest claim and the one I pushed hardest on; it held descriptor by descriptor.

Claim 2, "undertrained means inefficient, not weak." Earned and fair. The article
gives both required guards: PaLM could not have used Chinchilla (posted seven days
apart, training already finished — the reading is retrospective), and PaLM 540B
beat the smaller Chinchilla on downstream tasks by spending more compute, so the
verdict is efficiency, not strength. Chinchilla's own "considerably over-sized"
line is quoted in scope. No gotcha, as the brief demanded.

Claim 3, the GSM8K asterisk. The paper's 58% used an external calculator; plain
8-shot chain-of-thought scored 54%, below the 55% prior record (Cobbe et al.).
The article states all three numbers and draws the exact conclusion the record
licenses: a citation crediting PaLM with beating the record through reasoning
alone is crediting the calculator. Matches the evidence and Contradiction 1.

Claim 4, emergence as claim-then-challenge. The paper's discontinuity numbers
(25% of 150 tasks >+10%, 15% >+20%; 44 of 58 common tasks) are the textual
aggregates, not figure-read per-task percentages — the figure-read caveat is
respected and Figure 5 is not reproduced. Wei's definition is given first, then
Schaeffer, Miranda & Koyejo's rebuttal, then the verdict that PaLM's graph is one
contested exhibit. I confirmed the direction of the rebuttal against the primary:
Schaeffer et al.'s abstract says nonlinear/discontinuous metrics produce apparent
emergence while linear/continuous metrics show smooth change — exactly the
direction the article prints. Presented as claim-then-challenge, as required.

Citations: I opened all seven hrefs as printed. Every one resolves and lands on
its own source: 2204.02311 (PaLM), 2203.15556 (Chinchilla), 2206.07682 (Wei),
2304.15004 (Schaeffer), the research.google PaLM announcement, 2305.10403 (PaLM
2), 2312.11805 (Gemini). Display descriptors check out: 540.35B / 780B / 6,144
TPU v4 / two pods / 8.63B and 62.50B variants / 46.2% MFU vs 21.3% GPT-3 and
32.5% Gopher / 28 of 29 English NLP / 1.8B and 3.25B Gemini Nano. The Google
announcement's "log-linear behavior similar to prior models" and "breakthrough
performance" framing are Google's own words, confirmed on the page, and used to
make the internal-contradiction point (Contradiction 2), not to launder a
technical claim.

One break. The `nb-note` prints Wei's definition inside quotation marks as a
verbatim quote: "An ability is emergent if it is not present in smaller models
but is present in larger models." Wei et al.'s abstract (2206.07682), read as
printed, reads "We consider an ability to be emergent if it is not present in
smaller models but is present in larger models." The tail matches; the opening
clause does not. The note component is documented specifically to carry a
verbatim quotation, so a near-quote in quotation marks is a fidelity failure the
desk should not ship. The evidence record's Quote field records the same altered
form the article uses, so the record and the source I opened disagree. I do not
settle a quote or a record/source conflict by rewriting; routed to the writer.

data-nb-kind audit: s1–s4, s6, s7 are labeled primary; each authoring party owns
what the article cites it for (PaLM's own scale/results; Chinchilla's rule; Wei's
definition; Schaeffer's rebuttal; PaLM 2 and Gemini owning their own
disclosures). s5, the Google announcement, is labeled secondary. The article uses
it mostly for Google's own framing (where it is arguably primary), so "secondary"
is the conservative label and hides no missing independent source; it also
satisfies the floor's one-secondary requirement. No label change needed.

## Cut

Slop pass, every sentence including display text and furniture. Three sentences
failed and were fixed directly; the piece is otherwise clean at the edges.

1. Self-reference in the body. "We cover the finding itself in its own lesson"
   narrates the newsroom, which the lesson template bars everywhere but the two
   bookends (slop.md self-reference; template identity: "the body speaks to no
   one and never mentions the lesson"). Recast to "The finding has its own
   lesson," which keeps the Chinchilla link as reporting and drops the "we."

2. Signpost. "the point here is that PaLM's graph is one exhibit in it" grades
   where the argument stands rather than continuing it. Cut the signpost clause;
   the claim survives on its own as "PaLM's graph is one exhibit in it, not a
   settled finding."

Negative-parallelism check: three "X, not Y" / "X rather than Y" constructions
appear ("not the best model you could build... the best model for a fixed amount
of arithmetic," "a claim about efficiency, not strength," "an effect of
exact-match scoring rather than a new ability switching on"). Each corrects a
misconception the piece names and the evidence carries (compute-optimal misread
as best-possible; undertrained misread as weak; emergence taken as settled), so
each is an earned contrast and stays.

Delete-test on the edges: the orientation closer ("that size was more than its
training data could justify") and the article closer ("Cited today as proof that
size alone produces new abilities, it is asked to prove more than it did") each
carry a disputable, load-bearing claim and survive. The takeaway recaps each
finding, but every sentence lands a judgment rather than re-teaching, which is
the takeaway's job here; left intact.

Punctuation: one semicolon joined two independent clauses where the house default
is a period ("needed a calculator; without one, chain-of-thought scored below the
prior record"). Split into two sentences. No em-dashes in the piece; the one
remaining semicolon ("its own lesson; here it is a ruler") binds a genuinely
tight elsewhere/here contrast and stays.

Prompt-leakage check against the commission and briefs: the "citations outrun the
paper" conclusion is stated as a claim about the world with its own specifics, not
lifted from the commission's phrasing. No planning labels, selection rules, or
assignment-fulfilled claims survive.

Formula check against the recent-pattern notes: the headline is a declarative
finding that does not open on a figure (breaks the number-forward habit), and the
dek is a single sentence that avoids the desk's comma-plus-conjunction two-parter.
The five headings are argument steps in the piece's own nouns and none joins two
clauses with a comma and "and." No formula.

Voice-guide borrowing: no distinctive clause is lifted from the Piper, Evans, or
Lee-Trott exemplars; the piece applies their habits (figure-before-judgment,
catching a term as it goes past, running two numbers together) in its own words.

## Reader

Read straight through as the paper's declared reader: what I have that the two
papers alone would not give me is the one-page collision the sources never stage
against each other — PaLM's 1.44 tokens per parameter set beside Chinchilla's
~11-trillion-token budget for a model its size, with the retrospective, efficiency
reading spelled out so I can see it is inefficiency and not weakness, and the
emergence and GSM8K headlines each staged as claim-then-condition so I can see
where later citations overreach. The draft-handoff's original-work sentence claims
exactly this synthesis, and the article delivers it. The prose sits closer to the
voice-guide exemplars than to a median summary: figure first then judgment, terms
caught and unpacked at first use, the token math run on the page rather than
asserted. Headline as the largest claim holds: "PaLM was trained on a fourteenth
of the data its size called for" is what the piece proves.

## Edits

- token-budget: "We cover the finding itself in its own lesson" -> "The finding
  has its own lesson" (removed newsroom self-reference; Chinchilla link kept).
- big-bench: cut the signpost "the point here is that" and split the semicolon;
  now "The emergence debate is its own lesson. PaLM's graph is one exhibit in it,
  not a settled finding."
- takeaway: split the semicolon in "needed a calculator; without one..." into two
  sentences (house-default period).

## Required work

- writer: The `nb-note` labeled "The claim, defined" prints Wei et al.'s
  definition inside quotation marks as a verbatim quote ("An ability is emergent
  if it is not present in smaller models but is present in larger models"), but
  the paper (arXiv 2206.07682) reads "We consider an ability to be emergent if it
  is not present in smaller models but is present in larger models." The evidence
  record's Quote field carries the same altered wording, so record and source
  disagree. Confirm the exact wording in the paper and either quote it verbatim or
  drop the quotation marks and paraphrase. Altering a quote is outside the
  editor's authority, so this is the writer's (with the researcher confirming the
  record's Quote field if the paper's wording differs from what was logged).

## Decision

revise — the article is sound in argument, arithmetic, sourcing, and prose after
my edits, but the Wei definition is printed as a verbatim quotation that does not
match the primary, and a quote fix belongs to the writer.

Production record: run as Claude Opus 4.8 (claude-opus-4-8), effort=high.
