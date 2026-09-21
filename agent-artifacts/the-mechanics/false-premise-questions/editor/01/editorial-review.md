# Editorial review: the-mechanics/false-premise-questions (editor/01)

## Skeptic

Thesis: a chatbot answers a false-premise question fluently because the false
part arrives inside the prompt, where a next-token predictor conditions on it as
given; stopping would take two separate abilities (noticing the presupposition,
then verifying it is false), and underneath both, the training default is to
answer, because the text models learn from answers questions far more than it
corrects them and post-training rewards answering, not premise-rejection. The
objective and the data distribution are settled; whether and when newer models
detect false premises, whether the fix is worth its cost, and whether a
correction is understanding or another matched pattern are open.

Claims it stands on, and how each held:

1. Models answer false-premise questions fluently but handle them worse
   (orientation). Tested against (QA)² and CREPE. (QA)²: one model 56% acceptable
   on sound questions vs 40% on questionable — the article correctly reads the
   zero-shot text-davinci-003 valid-vs-questionable pair from the record, not the
   coincidental 56% "best overall" figure. CREPE: 26% of 8,466 ELI5 questions
   carry a false presupposition. Both match the evidence record. Held.
2. The premise sits in the prompt and is conditioned on as given (in-the-prompt),
   cited to GPT-3 (autoregressive). The gloss "not held at arm's length as claims
   to be judged" is reasoning on the mechanism, not an over-read. Held.
3. Detection and verification are distinct, verification the bottleneck
   (two-jobs). CREPE detection ~67% (question only) to ~76% (with comment),
   correction quality ~1.8/3 vs 2.8 reference, difficulty traced to retrieval;
   Kim 2021 ~21% of unanswerable questions, verification named as the component
   that falls short. The two jobs are not collapsed anywhere, including the
   takeaway. Held — and I preserved the split through every edit.
4. The training default is to answer, and premise-correction is rare in the
   corpus, stated at indirect strength (the-ground). Supported by FalseQA:
   170B+ models fail zero-shot yet hold the knowledge, and 256 example pairs lift
   3B/11B models to ~77-79% discrimination. The "no one has counted the corpus"
   caveat is explicit. Held at exactly the strength the brief requires.
5. Post-training rewards helpfulness/answering, not premise-checking
   (the-ground), cited to InstructGPT. Held.
6. Open part: newer models correct more but plateau below half (Cancer-Myth
   table), the failure generalizes to political questions (Sieker), the obvious
   fix degrades true-premise QA (Wang/Shwartz/Gonen 2026), and
   understanding-vs-pattern is unresolved. Each figure matches the record; the
   piece does not resolve the open questions into a verdict. Held.

I tried hardest to break claim 4, since it is the one the article itself flags
as thin. It does not overreach: the corpus-frequency step is inferred from
behavior, and the article says so. No claim broke.

Citations: I opened every printed href. All ten source links resolve to the
source itself (arXiv abstract pages for s1-s7, s9, s10; the Cancer Today feature
for s8), and every title and author list matches what is cited. The two "Go
deeper" links are non-citation bookend rows; the Wolfram link resolves, and the
Ars Technica link could not be fetched through my tool's proxy (host-blocked, not
dead) — it is the known-good URL the voice guide itself cites and it passed the
draft's links proof. Nothing here would fail a re-proof.

data-nb-kind audit: s1-s7, s9, s10 are primary (each authoring team owns the
dataset, method, or model description it is cited for); s8 is secondary (Ornes
reports the USC study from outside the authoring team). The secondary is used as
general-audience context for a finding the primary (s7) already owns, so it does
not stand in for a missing independent source. All labels correct; the 8/4/1
floor is met (9 primary, 1 secondary).

Display text, descriptor by descriptor: the headline is a claim the piece
defends (fluency is high on false and true premises alike; the failure is not
flagging, per Cancer-Myth answer quality 4.13/5 and "the models write well").
The dek breaks the recent "training presses X into its probabilities" mold and
commits to real content (four false-premise datasets; the cause in the prompt).
Every subhead is a step of the argument in the piece's own nouns, and reading the
five in order reconstructs the descent. The table caption is a factual, cited
label ("585 expert-verified" matches the source's wording). No wrong labels.

Numbers recomputed: 26% of 8,466 = 2,202 (record agrees); 301 + 301 (QA)²; 585
Cancer-Myth; "more than 500" (s8) is consistent with 585. Directions checked:
newer models correct more; better on false premises means worse on true ones.
All correct.

## Cut

Slop is light. Six sentences failed a test; five were cut or trimmed and one
was recast. The one repeated pattern: the descent between sections was carried by
signpost sentences ("the first reason it does is the plainest," "That is the next
step down," "the next level down is not about ability at all") of exactly the
kind the voice guide warns against, since the series descent is meant to be
carried by the substance and the section headings, not announced. I removed the
signpost scaffolding and let each section now end on its own reasoning or data,
which is a stronger edge in every case and suits the descent structure.

The other failures were two self-grading tails on the indirect-strength step:
"so this step has to be stated with care" and "and should be held at that
strength." Both rate the writer's own care rather than adding anything the reader
can check; the plain statements around them ("No one has counted...", "inferred
from the behavior, not read off a direct count") carry the epistemic honesty the
brief requires, so the safeguard is fully intact after the trim.

Edges walked alone read clean after those cuts. Negative constructions are all
earned: each "not X" corrects a real, named misconception ("this behavior is
neither" hallucination nor sycophancy; the failure "was not missing knowledge"
per FalseQA; "the gap is not about answer quality" per the 4.13/5 rating). None
is a strawman. No prompt leakage survives inspection: the "hit ground" and "open
even to the people who build these systems" framings are the series method
enacted with this article's own content, not lifted assignment sentences, and
"smuggled in" describes the behavior rather than restating the commission. No
distinctive phrasing is borrowed from the voice-guide exemplars; the
"explanation runs out here" close uses the Wolfram move, not his words. Em-dashes:
zero. Banned terms: none. Grammar: no breaks. The illustration (a novel never
written; "why did the author revise the ending") is honest and attributed to no
source; the flagged candidate questions were correctly left unprinted.

The one table earns its place: seven models of one shape, where the spread from
GPT-4o (5.8%) to GPT-5 (42.1%) and the ceiling below half is the point, and the
prose leans on it. No furniture is missing; adding any would only spend words the
piece does not have.

## Reader

Read straight through as the paper's reader, what I have that the sources alone
would not give me: a single causal chain that names, in order, why the model can
answer a false premise (it is in the prompt), why it usually does (the training
default), and where the residual difficulty actually sits (verifying, not
noticing) — plus a clean line between what is settled and what is open, so I can
name the step a glib explanation skips. No single source supplies that; each
measures one link. The draft-handoff's original-work sentence claims exactly this
synthesis, and the article delivers it. After the cuts the prose sits closer to
the voice-guide exemplars than to a median summary: it commits to concrete
objects and reports plainly where the explanation runs out, rather than narrating
its own method. The headline, reread as the largest claim, is accurate and
defended.

## Edits

- Cut the orientation closer "The model answers well while stepping over the false part, and the first reason it does is the plainest." (restatement plus descent signpost); section now ends on the (QA)² result.
- Cut "That is the next step down." at the end of in-the-prompt (bare signpost).
- Recast the two-jobs closer, removing "and the next level down is not about ability at all." (signpost); it now ends "Verification cannot be the whole story."
- Trimmed "so this step has to be stated with care" from the indirect-strength sentence in the-ground (self-grading); the caveat and its plain statement remain.
- Trimmed "and should be held at that strength" from the "inferred from the behavior" sentence in the-ground (self-grading); the factual claim remains.

## Required work

None. All items were within editing reach and are fixed in place. The cuts only
shorten the piece (it was at the 2200 top of band), touch no citation, href,
number, name, or furniture structure, and preserve the detection/verification
split and the indirect-strength framing, so the orchestrator's re-stamp and
re-proof (links included) should be unaffected.

Two verified-with-note items, no action needed: the article's CREPE figure of
26 percent is the paper's precise dataset statistic (2,202 of 8,466), which the
abstract rounds to 25 percent — the record owns 26.0%, so the more precise figure
is correct. And FalseQA's "about 77 to 79 percent" covers Macaw-3B (76.5%) and
Macaw-11B (79.2%); the low end rounds up slightly but stays within "about."

## Decision

approve — the causal chain holds, every citation lands on its source and every
data-nb-kind is correct, the flagged focus items are all handled honestly, and
the only slop was descent signposting and two self-grading tails, now cut.
