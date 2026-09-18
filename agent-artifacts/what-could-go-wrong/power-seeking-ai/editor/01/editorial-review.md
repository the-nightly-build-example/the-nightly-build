# Editorial review: what-could-go-wrong/power-seeking-ai (editor/01)

## Skeptic

Thesis: Carlsmith turned the case for existential catastrophe from
power-seeking AI into six numbered premises, multiplied his own credence on
each into a headline figure, watched three genuinely different critiques
land on that figure, and later raised the figure himself without changing
the premises that produced it. Claims it stands on: (1) the six premises and
credences are exactly as Carlsmith stated them; (2) the ~5% (2021) and >10%
(2022) figures and dates are exact; (3) Soares, Thorstad, and the
superforecaster panel disagree with Carlsmith in three genuinely different,
non-equivalent ways; (4) the empirical record supports specification gaming
but not power-seeking itself or premise 5's disempowerment; (5) the >10%
revision is not accompanied by a revised premise table.

I pushed hardest on (2) and (3), since a wrong probability or a flattened
disagreement is this round's named worst failure. I opened the primary
directly rather than trusting the evidence record alone:

- Fetched arxiv.org/abs/2206.13353 directly. Confirmed verbatim: "an overall
  estimate of ~5% that an existential catastrophe of this kind will occur by
  2070" and the parenthetical "(May 2022 update: since making this report
  public in April 2021, my estimate here has gone up, and is now at >10%.)"
  Dates and figures hold exactly as printed in the article and evidence
  record. No drift.
- Recomputed the six-premise product by hand: 0.65 × 0.80 × 0.40 × 0.65 ×
  0.40 × 0.95 = 0.051376, which the article correctly rounds to "about 5.1%."
- Fetched reflectivealtruism.com/2023/04/08 directly. Confirmed Thorstad's
  "I returned an estimate of 0.00002%" and "I now think that an estimate of
  0.00002% was unduly generous" verbatim.
- Fetched joecarlsmith.com/2023/10/18 directly. Confirmed the full six-row
  Carlsmith-vs-superforecaster table (65/80/40/65/40/95 vs 80/90/58/25/5/40)
  and the 5% vs 1% aggregate totals, matching the article exactly, including
  the article's important discipline of comparing the panel's 1% against
  Carlsmith's original 5% rather than his revised >10% (the two are not the
  same denominator's history, and the record supports only the 5%
  comparison).
- Fetched lesswrong.com/.../qRSgHLb8yLXzDg4nf and arxiv.org/abs/2310.18244
  (Hadshar) directly. Confirmed the ten-reviewer roster, the "21
  superforecasters... funded by Open Philanthropy" line, and Hadshar's
  "strong empirical evidence of specification gaming... no public empirical
  examples of misaligned power-seeking in AI systems" verbatim.
- Attribution discipline (this round's second focus item): grepped the
  article for Garfinkel, Aschenbrenner, Levinstein, Lifland, Nanda, Tarsney,
  Wallace — zero hits. Only Soares, Kokotajlo, Thorstad, and the
  superforecaster panel are named, matching the three fully-traceable
  reviewers the evidence record can source. No attribution slipped in.

One claim broke on inspection and I fixed it directly. The orientation
section's paragraph on the lower-bound caveat had a second sentence:
"Reviewers who want a larger number often start there, at that kind of
alternate path, a case probability theorists call disjunctive, rather than
at any one of the six numbers themselves." I opened Soares's own post
(lesswrong.com/.../cCMihiwtZx7kdcKgt) to check it, since a WebSearch turned
up that the real conjunctive-vs-disjunctive framing critique traces to
Soares specifically ("Joe frames his catastrophe estimates conjunctively,
and his survival estimates disjunctively... driven ultimately by his choice
of which side gets the conjunctions"). That is a different, more specific
claim than the one the draft printed. The draft's sentence conflated
Carlsmith's own "lower bound" caveat (that catastrophe could arrive by a
route outside the six premises) with an invented generalization about
unnamed "reviewers," cited only to Carlsmith's own report (s1), which
supports the first half of the paragraph but not the "reviewers... start
there" claim. None of the three sourced reviewers actually argues for a
larger number by pointing to a disjunctive alternate path: Soares disputes
the premises via the 1-in-2^n mechanical-bias argument (already correctly
covered later in the critiques section), and Thorstad wants a smaller
number, not a larger one. This was a sourcing failure — vague attribution to
"reviewers" plus a citation that didn't support the specific claim — and
since I opened the sources to confirm the actual claim doesn't hold as
stated, and the fix that would be accurate (reattributing to Soares by name)
would introduce reporting the evidence record itself never surfaced, I cut
the unsupported half-sentence rather than rewrite it into something the
researcher didn't establish. The accurate, sourced half (Carlsmith's own
lower-bound caveat) stays.

I also checked the "documented across dozens of separate cases" claim about
specification gaming (real-systems section) against Hadshar's paper. Her
abstract supports "strong empirical evidence" but gives no count, and the
evidence record doesn't establish "dozens" either. This was an unsourced
precision the article didn't earn (editorial-direction's Numbers section:
"Give the figure, not the magnitude... a sourced range rather than a
precision the source does not support"). Cut the quantifier; the sourced
qualitative claim ("strong evidence," cited to Hadshar) stands on its own
and the linked reward-hacking lesson carries the specifics.

I checked every named person's role: Carlsmith is correctly described as
having written the report "while at Open Philanthropy, the foundation that
commissioned it" (matches evidence, which notes Soares's and Thorstad's
posts carry no stated institutional titles, and the article does not invent
any). Kokotajlo, Soares, and Thorstad are each introduced only as reviewers,
with no fabricated affiliation. This holds.

Every internal link (instrumental-convergence, the-off-switch,
orthogonality-thesis, situational-awareness, reward-hacking,
goal-misgeneralization) resolves to a real file in the library checkout —
confirmed by listing the checkout directory. Every external href I opened
(s1, s2, s3, s4, s5, s6, s7, s8) landed on the source's own page, not a
fetch endpoint, and each supported the specific claim it was cited for once
fixed. I did not re-open s9 beyond the search corroboration already in the
evidence record; its content (Kokotajlo's 2021 comment and Carlsmith's
reply) was already quoted verbatim and matched the evidence record closely
enough that I judged a fresh fetch unnecessary given the higher-risk items
above.

## Cut

Ran the slop test on every sentence, with particular attention to edges
(first/last sentence of every paragraph, section, and the article) read out
of order, per spec/slop.md.

- Grepped for spec/slop.md's and banned-terms.yaml's counted and named
  tells (highlight/underscore/reflect/cement, serves-as/stands-as, puffery
  words, vague-attribution phrases, self-reference, leverage,
  load-bearing, revolutionary, transformative, game-changing, AI race,
  machinery): zero hits outside the sources list and one CSS font URL.
  Em-dash count: 0 (max 4). Prose semicolons: 2, both earned (tight
  contrasts, not comma-splice patches or chained connectors).
- The takeaway's closing paragraph ran the same negative-parallelism
  construction three times in five sentences: "was never a demonstration.
  It was a discipline," "the smaller failure... not the one it is actually
  about," and "is not a verdict... It is the method." spec/slop.md flags
  "X is not Y, it is Z" as "a frequent tell, worth checking on every draft,"
  and three instances stacked in the article's single highest-risk position
  (its last paragraph) read as formula rather than earned contrast. I
  rewrote the paragraph to keep every fact (the ~5%, the >10%, the three
  objections, the 1% superforecaster aggregate, the untested fifth premise,
  specification gaming vs. world-scale disempowerment named concretely
  instead of left as vague referents) while cutting two of the three
  negative-parallelism constructions and closing on the same
  what-happened-to-the-number note the original had, without the repeated
  device. This also replaced two vague referents ("the smaller failure,"
  "the one it is actually about") with the concrete named terms
  (specification gaming, world-scale disempowerment), which is a clarity
  gain independent of the slop fix.
- Found one paragraph in "The estimate went up. The premises did not."
  covering two topics from two different years under one <p>: Carlsmith's
  non-response to the 2023 superforecaster panel, run straight into
  Kokotajlo's 2021 comment-thread objection with no paragraph break. Split
  into two paragraphs; no prose changed.
- Found one instance of borrowed phrasing from the voice guide rather than
  the article's own terms. The voice guide states the Silver-style point
  as: "a change in a stated number does not by itself mean the world
  changed or the reasoning was wrong." The draft's version: "A stated
  probability rising is not, by itself, evidence that the world changed or
  that the original reasoning was wrong." The clause order and key phrases
  ("by itself," "the world changed," "the reasoning was wrong") are close
  enough to read as a lightly reworded lift rather than the article's own
  formulation of a point the evidence record does support (Contradictions:
  "Carlsmith's own headline number moved without a re-run of the
  multiplication"). Rewrote it in the article's own terms — naming the
  three concrete possibilities (a premise rated worse, a new outside
  argument, a bare shift in judgment) and stating plainly that the note
  picks none of them — rather than cutting the point, since the underlying
  claim is sourced and belongs in the piece.
- Read every heading, the dek, and the headline against the round's named
  recent-pattern notes: no "researchers concede X" / "rests on a built demo
  or simulations" dek mold, no "The [noun] that [verb]" heading mold. All
  four headings ("How six premises became one number," "Three critiques of
  the same six numbers," "What real systems have actually shown," "The
  estimate went up. The premises did not.") are built differently from each
  other and from the named recent examples, and each states a step of the
  argument in the piece's own nouns rather than a scaffolding label.
- Checked the take-away and why-bookend for the desk's moralizing-close
  habit the round flags. Neither bookend closes on "how worried to be." The
  takeaway (both before and after my edit) ends on what happened to
  Carlsmith's own number, which is the form the voice guide and the
  round's focus both call for.
- Checked prompt leakage against the commission, brief, and series prompt
  more broadly (clause order, not just word matches): no other lifted
  sentences found. The "why" bookend's closing sentence, which previews
  what the lesson covers, is the template-documented job of that bookend
  (identity.md: "what they will understand by the end"), not a
  self-grading signpost, so I left it.
- Considered whether a second furniture table (the evidence record's
  Carlsmith-vs-superforecaster comparison table, offered as a source asset)
  would serve the reader better than the existing prose enumeration of the
  six per-premise numbers. The prose already lays out all six pairs and
  both aggregates clearly, the article sits close to the word ceiling, and
  the commission's "small table" allowance was already spent on the
  premises-and-credences table. I judged the existing single table
  sufficient and did not add a second one; this is a judgment call, not a
  gap I'm routing to the writer.

Roughly a dozen sentences were tested closely enough to be candidates; four
were changed (one cut outright, one quantifier cut, one paragraph split,
one rewritten), which is fewer than the number tested — most of the draft
holds up against spec/slop.md as written.

## Reader

Reading the survivors straight through as the declared reader (smart,
widely read, no codebase, meeting this argument for the first time): what I
have that the sources alone would not give me is the sorting the draft does
across three incompatible critiques that would otherwise read as one
undifferentiated "reviewers pushed back," plus the premise-by-premise line
between what specification gaming has actually shown and what remains
conceptual argument about power-seeking and disempowerment. Reading
Soares's post, Thorstad's three posts, and Carlsmith's superforecaster
post cold, in the order a curious reader would find them, would not by
itself produce the observation that Soares and Thorstad/the superforecasters
are answering different questions (method artifact vs. premise size) that
happen to look like the same objection from a distance. That is genuine
synthesis, not restatement, and matches the draft-handoff's original-work
sentence, which I opened only after forming this answer independently; the
two agree.

The prose sits closer to the voice-guide exemplars than to a median AI
summary: the premises table plus the "multiply the six numbers... about
5.1%" paragraph do the Harford-style walk-the-arithmetic-in-view-of-the-
reader move without hiding a step, and the Soares and Thorstad paragraphs
quote-then-explain in the Levine register rather than summarizing around
the quotes. The one place it had drifted toward a generic, AI-summary
cadence was the takeaway's stacked negative-parallelism, which is now
fixed.

The headline, reread as the largest claim: "Carlsmith multiplied six
probabilities into a 5% chance of catastrophe. He later raised it past
10%." Both halves are exact, checkable facts (verified against the primary
above), stated as findings with the actor named, not a question or a
hedge. It passes.

## Edits

1. Orientation section: cut the unsupported, vaguely-attributed sentence
   "Reviewers who want a larger number often start there, at that kind of
   alternate path, a case probability theorists call disjunctive, rather
   than at any one of the six numbers themselves." The claim conflated
   Carlsmith's own lower-bound caveat with an invented reviewer pattern,
   miscited to s1. Kept the sourced sentence before it.
2. Real-systems section: cut the unsourced quantifier "documented across
   dozens of separate cases" from the specification-gaming sentence; kept
   the sourced qualitative claim ("The evidence is strong for
   specification gaming... real, deployed systems finding an unintended
   shortcut to a stated objective.").
3. The-revision section: rewrote "A stated probability rising is not, by
   itself, evidence that the world changed or that the original reasoning
   was wrong. It can just as easily mean he updated on an argument that
   never entered a re-run of the calculation." into the article's own
   terms (naming three concrete possibilities: a premise rated worse, a new
   outside argument, or a bare shift in judgment), removing a clause-order
   lift from the voice guide's own formulation of the same evidenced point.
4. The-revision section: split one paragraph that ran Carlsmith's 2023
   non-response to the superforecasters directly into Kokotajlo's 2021
   objection with no break into two paragraphs. No prose changed.
5. Takeaway: rewrote the closing paragraph to remove two of three stacked
   "X is not Y, it is Z" constructions (spec/slop.md's named frequent tell),
   replacing the two vague referents ("the smaller failure," "the one it is
   actually about") with the concrete terms already established in the
   body (specification gaming, world-scale disempowerment). All facts
   preserved (~5%, >10%, three objections, 1% aggregate, untested fifth
   premise); no moralizing close introduced.
6. Minor whitespace/line-wrap cleanup around edits 1 and 2 (no text
   change).

## Required work

None blocking. No item needs the researcher or the writer this round.

- Orchestrator: the article's word count metadata in nb-meta (2191) is now
  stale after these cuts (net reduction; my own rough count puts the
  rendered body meaningfully lower, not higher). Re-stamp before the final
  check, as the process already calls for. No new content was added that
  would require an offsetting cut — the net change is a reduction, so there
  is headroom, not a deficit.

## Decision

Approve. The headline probability figures, premise credences, and dates
check out exactly against the primary; the attribution stays inside the
three traceable reviewers plus the superforecaster panel with no Garfinkel
or unsourced-reviewer slip; the has-been-shown/still-analogy line is drawn
premise by premise and matches Hadshar's own terms; instrumental convergence
and orthogonality are linked, not re-taught. The one broken claim
(the miscited "disjunctive" generalization) and one unsourced quantifier
are now cut, the one prompt-leaked sentence is rewritten in the article's
own terms, and the one repeated slop pattern in the closing paragraph is
resolved. Nothing here needs reporting the researcher or writer hasn't
already supplied.
