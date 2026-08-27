# Editorial review: the-mechanics/structured-output (editor/01)

## Skeptic

Thesis: a strict output format lowers a model's accuracy not because the
enforcing mask is costly in itself, but because that mask can block the
intermediate tokens the model reasons with; the damage is done by a schema that
forces the answer before the reasoning, and putting the reasoning first removes
most of the cost. The piece stands on five claims, and I tested each.

1. A format is enforced by per-token masking: at each step a program zeroes
   every token that would break the format, before the draw (settled, rung 2).
   Held. I opened Willard & Louf (s2) and XGrammar (s3). Willard & Louf apply a
   boolean mask multiplied into the distribution before sampling; XGrammar drives
   grammar-invalid logits to negative infinity before the draw. The article's two
   descriptions match both. It does not claim XGrammar "is the backend" of any
   serving engine, which the evidence record warned against.

2. Blocking those tokens blocks the computation, because a transformer computes
   more only by writing more (rung 3). Correctly linked to thinking-out-loud, not
   re-taught, and carried as prose rather than a numbered source per press policy.

3. The hinge: a schema with the answer field before the reason field forecloses
   the reasoning, and in the 2024 study one model put the answer key ahead of the
   reason key in 100% of its constrained responses (s1). Held. I confirmed the
   100% answer-before-reason finding in the Tam full text. This is the load-bearing
   link from mask to lost reasoning room, and the piece places it exactly there.

4. The size of the pure-formatting penalty is disputed (rung 4). Held as a live
   disagreement, never as a settled cost. I verified every figure against the
   owning primary. Tam GSM8K: GPT-3.5-Turbo 75.99% to 49.25% (article 76.0% /
   49.3%, prose "about 76%" to "49%"); Claude-3-Haiku 86.51% to 23.44% (article
   86.5% / 23.4%, prose "about 87%" to "23%"). dottxt re-run on Llama-3-8B: 0.77
   free text vs 0.78 structured (article 77% / 78%). All roundings are faithful.
   dottxt's stake is disclosed as the record required. The "other side" (that the
   mask is cheap) is steelmanned with an independent source (Aidan Cooper, s8) and
   Tam's own classification-task reversal, so the pro-structure reading does not
   rest on the party with a stake.

5. The fix, agreed by both camps: reason first, format after (s6). Held. OpenAI's
   docs lay out the steps-before-final_answer schema exactly as the article says.

Round focus, all confirmed:
- Settled/disputed spine intact: the mask-before-draw mechanism is stated as
  settled engineering; the penalty's size is presented as a sharp disagreement
  between Tam and dottxt, never rounded toward a settled cost.
- Quarantine respected: the OpenAI schema-following eval figures (100% / under
  40%) appear nowhere. The only "100%" in the piece is Tam's answer-before-reason
  field-order figure, which is not quarantined and is correctly cited to s1.
- Terminology kept straight throughout: "JSON mode" is used only for OpenAI's
  weaker feature, the hard-constrained thing is "constrained decoding," and the
  piece flags that Tam uses "JSON mode" in the opposite sense.

Display text: headline, dek, all five subheads, and the table cells verified
descriptor by descriptor. No How/What/Where heading openers. The dek matches none
of the three banned molds. data-nb-kind audit: all eight labels (5 primary, 3
secondary) match the evidence record's classifications.

Citation hrefs: I opened all eight as the article prints them. Every link lands
on the source itself and carries the claim cited to it: s1 Tam, s2 Willard &
Louf, s3 XGrammar, s4 Let's Data Science, s5 Willison, s6 OpenAI docs, s7 dottxt,
s8 Aidan Cooper. No miscitation, no broken central claim, no source-policy
failure. Nothing routed to the researcher.

## Cut

Slop pass against spec/slop.md, every sentence including display text and the two
furniture components. Five sentences failed and were fixed directly; none of the
failures needed reporting the writer would have to supply.

- Orientation closed on self-narration: "we will get to the argument" and "First
  the mechanism" narrate the article's own structure, which the body must not do.
  I rewrote the pair to keep only the two real ideas (the size is the disputed
  part; it depends on the mechanism) and cut the roadmap.
- "Same move, two libraries." was a redundant edge flourish: the paragraph had
  already stated the two-implementation corroboration at its top and shown both.
  It failed the delete test and was cut.
- "this lesson calls the hard kind constrained decoding" mentioned the lesson
  from inside the body, which only the bookends may do. Rephrased to state the
  naming convention without the self-reference.
- "and it names a specific flaw rather than waving at one" was a
  negative-parallelism reflex that graded the objection instead of continuing it;
  the objection's substance was already on the page. Trimmed.
- "The other side deserves the same fair hearing" was a generic transition that
  also mislabeled the paragraph, which adds weight to the pro-structure side, not
  Tam's. Rewrote to "And the case does not rest on dottxt alone," which frames the
  independent support (Cooper, Tam's classification results) correctly.

Punctuation: the one semicolon in the piece, in the disputed-size table caption
(the writer flagged it for judgment), pairs two contrasting setups that stand
perfectly well as two sentences. The house default is the period, so I made it a
period.

Considered and kept: the earned contrast "The mask did not make the model worse
at math. It took away the space where the model did the math" corrects a real,
named misconception (that the constraint degrades the model's math ability) and
states the article's core mechanism, so it survives the negative-parallelism
test. The instructional second person and "watch a single step" / "picture a
schema" moves are the register the voice guide explicitly directs (Ciechanowski's
"watch it happen"), launch genuine worked examples, and were left in rather than
flattened. The "In plain language" note earns its place and anchors s4; the
comparison table is genuinely comparative and not formula.

Leak check against the commission and briefs: the "return only JSON... quality
slip" opener restates the reader's own situation, which the commission supplies
and the standard exempts, not a planning instruction. No selection rules, planning
labels, or assignment-fulfilled claims reached the prose.

Recent-pattern check: no How/What/Where headings; dek avoids the three molds; the
piece does not close the body by returning to its opening image (the takeaway
resolves the opener's trade, which is the template's endorsed bookend pairing, not
the banned closing move). No Verdict block closes the body.

## Reader

Read straight through as the paper's declared reader, I come away with something
no single source gives: the four literatures threaded into one chain that locates
the accuracy cost in the reasoning room a schema can foreclose rather than in the
mask, and shows the Tam-versus-dottxt disagreement is really a disagreement about
whether the schema asks for the answer before the reasoning. The draft-handoff's
original-work sentence claims exactly that reconciliation, with the
answer-before-reason field order as the hinge, and the article delivers it in the
lost-reasoning section, the disputed-size reconciliation, and the fix. Both
answers survive; the piece does not restate its sources. The prose sits closer to
the voice-guide exemplars than to a median summary: plain declarative, checkable,
figures given, the settled rung stated flatly and the contested one marked
contested. The headline, read as the largest claim, is defended and honestly
hedged ("can block"): a strict output format can block the reasoning a model needs
to be right.

## Edits

- Dek (and matching nb-meta dek): "holding the answer to a schema" to "holding a
  model's output to a schema," removing a garden-path reading.
- Orientation: replaced "...the argued part of the story, and we will get to the
  argument. First the mechanism, because the size of the cost only makes sense..."
  with "...the disputed part, and its size only comes into focus once you can see
  what the format does to the model as it writes."
- The-mask: cut the trailing "Same move, two libraries."
- The-mask: "this lesson calls the hard kind constrained decoding and saves JSON
  mode for the weak one" to "the hard kind is called constrained decoding from
  here on, and JSON mode is kept for the weak one."
- Disputed-size caption: changed the semicolon to a period ("...before the
  reasoning. The Outlines team kept the reasoning...").
- Disputed-size: cut "and it names a specific flaw rather than waving at one."
- Disputed-size: "The other side deserves the same fair hearing." to "And the
  case does not rest on dottxt alone."

## Required work

None. No item is owned by the researcher, the writer, or the orchestrator beyond
the routine stamp.

## Decision

Approve. The correctness spine holds, every figure and citation checks out against
its primary, the settled/disputed line and the terminology are kept straight, and
the remaining prose issues were fixable in place.
