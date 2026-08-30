# Editorial review: the-mechanics/random-numbers (editor/01)

## Skeptic

Thesis: a chatbot asked for a random number answers 7 (or 37, 47, 73 for
1-100) not by rolling a die but by emitting a learned probability list over
next tokens that a sampler draws from; the list's shape is inherited from human
text, which over-picks the same values, and is then sharpened by alignment;
temperature rescales the list without flattening it; the fix is to let the
model call an external generator.

The claims it stands on, and how each held:

1. The behavior is measured, not anecdotal. Verified against Coronado-Blázquez
   (arXiv:2502.19965): six models, 75,600 calls, 7 dominant for 1-10 (~80% for
   the three named models), 3 for 1-5, extremes avoided. Verified against
   exmergo's 10,000-call gpt-4.1 series: 47/57/72/37/42 the top picks, χ²=15,604
   at df 99, every multiple of 10 except 10 returned zero times. The article's
   figures match the evidence record and the primaries. The chart data matches
   the exmergo series cell for cell (spot-checked 47=526, 57=457, 37=404,
   42=401, 72=415, 73=343, 27=350, 67=391, 87=337, 69=29, round numbers 0).

2. No RNG inside the model; there is a token-probability list and a decoder
   (greedy = argmax, deterministic; sampling = weighted multinomial draw), and
   the draw is the only randomness. Verified against the Hugging Face
   generation-strategies docs, which the article renders faithfully. The section
   holds the commission's critical line: it explicitly hands run-to-run
   variation to the nondeterminism lesson and answers "why 7" by the shape of
   the list, not the randomness of the draw.

3. The list is learned from human text, humans over-pick 7 (Kubovy & Psotka,
   28.4% vs ~11%), and the bias is scoped to chat/aligned models, not language
   models in general (West & Potts: 8B base 13.9 vs aligned 52.3-129.1).
   Verified. Scope is handled correctly; the article never says "architecture
   level." West & Potts prints exact divergence figures the record flags as
   summary-sourced, but the record supplies those exact values and the article
   attributes them and marks the inherited-vs-added split as unsettled, so this
   is honest.

4. Temperature rescales but cannot rebuild the list; models have no internal
   sampler (Zhao/Du/Wang, median 7%); reasoning does not rescue it (Coronado's
   DeepSeek-R1 works through coin flips and dice, then returns a favorite).
   Verified against both papers.

5. The fix is an external generator, not a better prompt (Gu et al.:
   understanding >80% but direct sampling poor; code-generation reaches "nearly
   100%"). Verified.

Display text: headline "Ask a chatbot for a random number and it says 7"
defends exactly what the piece argues. The dek makes a claim about the world
(no RNG, so it draws from a human-shaped distribution), not a grade of the
article's method. Every subhead is a step of the argument in the piece's own
nouns; a heading-only skim reconstructs the trace. Every named person's role
and every figure checked out against the owning primary. All eight citation
hrefs open on the source itself; the four internal Background/body links resolve
to real published lessons with matching titles. Source kinds (7 primary, 1
secondary) meet policy, and the Veritasium survey is correctly labeled secondary
and flagged in prose as a rough survey.

One break with the evidence, routed. The article states "Humans over-pick 69"
as established fact and rests the "runs the wrong way" 69 anomaly on it. No
source in the record measures human preference for 69: Kubovy tested single
digits and the 20s/70s, and the Veritasium survey's reported favorites are 7,
37, 73 and 77, not 69. The clause is cited via #s2 to exmergo, which measured
gpt-4.1's output and only *assumes* 69 is a crude human favorite the model
suppresses. A human-behavior claim is riding on an LLM-measurement source. This
is corroborating, not central (West & Potts already carries "alignment reworks
the shape"), so I did not settle it by writing around the gap. It goes to the
researcher for a real human source and to the writer to re-cite or cut.

One overclaim, fixed directly. The closing said "why safety tuning pushes 69
down," asserting as cause what the article itself calls "a guess, not a shown
cause" two paragraphs earlier. I recast it to "why 69 is pushed down," which
leaves the open question standing on the exmergo-measured facts (69 low, 47
high) without naming an unproven cause.

## Cut

The slop pass found the prose largely clean and specific; it names actual parts
and their actions in the Evans/Ciechanowski register the voice guide asks for.
Negative parallelism is the recurring tell in this draft, as slop.md warns to
expect. Most instances are earned, because each corrects a misconception the
piece actually names and refutes: "not a fresh roll of a fair die" (the die view
the no-generator section demolishes), "not a controlled result" (a real
methodological caveat on the survey), "the fix is not a better prompt"
(prompt-engineering, the reader's likely assumption). Those stay.

Two failed and were cut or recast:

- "The favorite is measured, not folklore." The "not folklore" was reflex; the
  piece never argues against folklore. Trimmed to "The favorite is measured,"
  which keeps the anecdote-to-data transition and drops the parallelism.
- "The question to hold is simple." A signpost in the opener that announces a
  question instead of carrying one. Cut; the question that follows lands on its
  own.

One clarity fix: "fixed the moment the model finished its forward pass" used
"forward pass," undefined jargon in a lesson written for a reader new to the
subject, and the lesson must work without opening the Background links. Recast
to "finished computing it," which loses nothing.

Two reflex semicolons joining simple independent clauses. Repaired the clearer
one ("rescales the list of odds; it never rebuilds it" to two sentences). Left
"Reading those bars off a trained model is easy; deriving them from what went in
is not," a tight antithetical parallel where the semicolon earns its place.

Edge and closer sentences hold. The article's last line resolves the opener's
question ("what is it doing when it hands you a 7?") with a stated finding, not
a signpost. Headings, dek, and openers were compared against the recent-pattern
notes: no "By the end you will know" closer, no quoted-failing-prompt headline,
no banned dek mold, and heading construction is varied (a numbered finding, a
negation, a plain statement, a negative-result line, an imperative), not the
recent two-clause comma-and rhythm. No prompt leakage: the commission's
"shape vs draw" framing is rendered in the article's own terms. No furniture
misuse; the one chart is evidence, honest, and cited.

Roughly four sentences were flagged and two cut or recast; the rest of the flags
resolved as earned contrasts or legitimate rare punctuation.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: a single step-by-step trace from the observed
"7" down to ground, no RNG, a learned token-probability list plus a weighted
draw, a human-inherited and alignment-sharpened shape, temperature that cannot
flatten it, and an external generator as the real fix, assembled from nine
measurements no one of which draws the whole chain, plus a chart that makes
"biased, not just variable" visible against a uniform baseline in one glance.
The draft-handoff's original-work sentence claims exactly this synthesis and
visualization, and the article delivers it; both answers survive, so the piece
teaches rather than restates its sources. The prose sits closer to the
voice-guide exemplars than to a median summary: it spends a full step letting
the naive "distracted person grabs a number" explanation fail before the real
mechanism arrives, and it stops honestly on the one rung still in shadow rather
than on a manufactured conclusion.

## Edits

- Cut "The question to hold is simple." from the Why this matters bookend.
- Changed "The favorite is measured, not folklore." to "The favorite is
  measured." (reflex negative parallelism).
- Changed "fixed the moment the model finished its forward pass" to "fixed the
  moment the model finished computing it" (undefined jargon).
- Split the semicolon in "temperature only rescales the list of odds; it never
  rebuilds it" into two sentences.
- Recast the closing "why safety tuning pushes 69 down while it leaves 47 alone"
  to "why 69 is pushed down while 47 is left alone" (removed an asserted cause
  the article elsewhere calls a guess).

## Required work

- **researcher:** "Humans over-pick 69" has no firsthand human source in the
  record. It is cited via #s2 to exmergo, which measured gpt-4.1's output, not
  human choices; the Veritasium survey's reported human favorites are 7, 37, 73,
  77, and Kubovy & Psotka did not test 69. Supply a firsthand human source that
  measures human over-selection of 69, or confirm none exists.
- **writer:** Depending on the researcher's result, either re-cite the
  "Humans over-pick 69" clause to a proper human source, or, if none exists, cut
  the 69 anomaly and recast the "two findings" paragraph (the "The second is a
  number that runs the wrong way ... Both point the same way" structure depends
  on there being a second finding) and reconcile the closing, which still names
  69 and its count. Do not restate the human premise without a source behind it.
- **writer:** Confirm the direct quotation attributed to Zhao/Du/Wang,
  "lack a functional internal mechanism for probabilistic sampling," is verbatim
  in the cited paper. The paper's published abstract reads "lack a functional
  internal sampler"; a quotation in quote marks must match the source exactly, so
  either the wording or the locator (currently "Abstract; Appendix A") needs to
  land on the sentence actually quoted.

## Decision

revise: a stated-as-fact human-behavior claim ("humans over-pick 69") rests on
a source that measured a model rather than people, and a direct quotation needs
its wording confirmed against the paper; both are sourcing items only the
researcher and writer can settle, so the piece cannot publish as printed.
</content>
</invoke>
