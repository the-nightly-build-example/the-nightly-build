# Editorial review: the-instruments/hallucination-rate (editor/01)

## Skeptic

Thesis: a published "hallucination rate" from Vectara's leaderboard is a
summary-faithfulness score, not a truthfulness ranking; read as "which AI lies
least," it answers a question it never measured.

The claims it stands on, each tested against the evidence record and its owning
primary:

1. The rate is manufactured as summarization faithfulness — model summarizes a
   handed passage under "use only this passage," the HHEM classifier scores
   support, rate = 100 - consistency. Source 1 (Vectara README) owns every step;
   the four-step pipeline and the 9.6% / 90.4% GPT-4o instance are exact. Holds.

2. A faithful summary of a false passage passes (faithful != true). This is the
   central seam and the headline's claim. I pushed hardest here. The worked
   example is an explicit hypothetical ("Suppose a passage states, wrongly...")
   about a drug's approval year, not a real-world record, so there is no
   fabricated fact presented as reported. Its mechanics are exact to source 4:
   HHEM scores a hypothesis's support against its premise, so a summary echoing a
   false passage scores as supported. The illustration earns its place under the
   voice guide's worked-trace license — deleting it would collapse the seam back
   into an abstract statement. Holds, and it is accurate to the record.

3. The classifier is imprecise: ~32% recall on RAGTruth-Summ (misses ~two of
   three), ~76% precision, ~55.7% balanced accuracy on FaithBench hard cases vs
   ~56.3% for zero-shot GPT-4o. All exact to sources 4 and 5. One note, not a
   break: the leaderboard is scored by HHEM-2.3 (source 1) while the quoted
   accuracy figures are HHEM-2.1-Open (source 4); the piece treats "HHEM" as one
   instrument. The evidence record itself makes this move deliberately (it bounds
   "any rate it produces" with the 2.1-Open numbers), so it is a sanctioned
   simplification rather than a miscitation. Holds.

4. Three benchmarks define hallucination incompatibly, so rates cannot be
   stacked. TruthfulQA (817 questions, no source document, 58% vs 94%), RAGTruth
   (~18,000 responses, span-level, three tasks), FaithBench (four-way taxonomy).
   Exact to sources 6, 7, 5. Holds.

5. Task-vs-open-use gap. PersonQA: o3 33%, o4-mini 48%, o1 16%, against
   single-digit summarization scores. Exact to source 8 (0.33 / 0.48 / 0.16); the
   stat strip (9.6% GPT-4o / 33% o3 / 48% o4-mini) is correctly labelled by model
   and task. The one soft edge is "belong to the same class of model" — the 9.6%
   is GPT-4o and the 33-48% is o3/o4-mini, different models. The piece is honest
   that these are different tasks and never claims one model scored both, and the
   evidence frames the contrast at the class level (OpenAI reasoning models also
   sit far below 33-48% on the board, e.g. o3-pro 23.3%). Within tolerance. Holds.

6. The "misled" case carries no invented cost. The piece states outright "The
   cost is not a line item anyone has totaled" and builds the harm from the press
   generalization (sources 2, 3) plus the task-vs-open-use gap. No dollar or
   procurement figure is fabricated. This honors the evidence record's flagged
   gap exactly. Holds.

Display text audited descriptor by descriptor. Headline is the defended central
claim, not a self-grade. Every subhead is a step in the piece's own nouns; none
is a scaffolding slot. All nine `data-nb-kind` labels are correct (README, HHEM
card, and the four papers primary; NYT, Tom's Hardware, TechCrunch secondary).
Bookends carry no citations, per the template contract. The mold-break holds: no
paired-conflicting-number headline, no ranking table.

No break retired a claim. Nothing routed to the researcher.

## Cut

The dek was the main target. At 41 words with two clause joins it carried a
fourth payload — "judged by a classifier that misses two of every three
hallucinations on one public benchmark" — that is a *different* criticism
(instrument imprecision) from the headline's thesis (faithful != true). On a
front-page card that quantified clause competes with the thesis for the reader's
first impression, exactly what the dek standard forbids, and it is what drove the
density warning. I cut it. The dek now lands at 24 words and one appositive join:
the instrument, its public role, and the reframe, setting up the headline
cleanly. This is a cut, not a rewrite, so it was mine to make; I judged the
writer's density warning here as not earned.

The second warning I judged and kept: the "three things it cannot tell you"
enumeration in Why-this-matters is a colon introducing a proper three-item list,
not a run-on, and it mirrors the three-part takeaway the template pairs it with.
The editorial standard explicitly permits writing the list. It stays.

One more cut: in the incompatible-benchmarks close, "is a mechanism of its own;
the point here is narrower" narrated the argument's own scope — a signpost, and
the semicolon was a period avoiding itself. I removed "; the point here is
narrower" and let the next concrete sentence carry the bound. The cross-reference
link already does the scope-limiting work the press voice asks for.

Worst tell found: the repeated opener. Why-this-matters opens "Ask which AI
invents the fewest facts and the answer usually comes back as a single
percentage," and the orientation section opens "Ask which chatbot invents the
fewest facts and the answer usually arrives as one percentage." Near-verbatim,
same clause, same shape, hit within a few lines when read straight through. That
is a formula and needs breaking. It cannot be cut surgically — the orientation
opener's antecedent ("those percentages") depends on it — so the rewrite of one
opener belongs to the writer.

Furniture is purposeful, not a stack of blocks: the four-step pipeline is the
"manufactured chain," the Vectara caveat note gives the builders' own words at
the seam, and the stat strip makes the cross-task contrast visible arithmetic.
No verdict block (correctly avoided per press direction). No asset requested: the
clustering argument is adequately carried in prose and the stat strip, and no
exact visual would let the reader test the central claim better than the worked
trace already does.

## Reader

Read straight through as the paper's smart, code-free reader, the piece gives
what no single source does: a mechanical account of how the rate is built, a
worked instance where a false claim earns a clean mark, the classifier's own miss
rate, the incompatibility of three benchmarks, and the open-use gap — assembled
into a usable rule for what the number can and cannot support. That matches the
draft-handoff's original-work sentence. The prose sits closer to the voice-guide
exemplars than a median summary: it runs Ritchie's concrete-case-before-principle
and Levine's grant-then-bound ("None of this makes HHEM a poor tool... The
trouble starts when its output is read as more than that one job's score"). The
headline is the largest claim and the piece defends exactly it.

## Edits

- Cut the dek's fourth clause ("judged by a classifier that misses two of every
  three hallucinations on one public benchmark") in both the `nb-meta` JSON and
  the `nb-dekline`; dek now 24 words, one join.
- Cut "; the point here is narrower" in the incompatible-benchmarks section,
  closing the clause with a period.
- Ran `nb stamp` (words 2072, reading 9 min, sources 9).

## Required work

- writer: Break the near-verbatim repeated opener. The Why-this-matters bookend
  and the orientation section both open with "Ask which AI/chatbot invents the
  fewest facts and the answer usually comes back/arrives as a[/one] percentage."
  Rewrite one opener (orientation is the natural one to change) so the two do not
  echo, keeping the "those percentages" antecedent intact. Then re-run the proof.

## Decision

revise — the article is sourced, teaches, and honors the no-invented-cost
constraint; one first-read-visible repeated opener remains and its fix is new
prose the writer owns.
