# Editorial review: the-mechanics/politeness-and-pressure (editor/01)

## Skeptic

Thesis: a please, a tip, or a threat is ordinary text the model conditions on,
so it genuinely shifts the output, but no specific phrasing reliably improves
the answer on current models. The settled cause (sensitivity to all prompt
text, a trained disposition) is kept separate from the unsettled payoff
(reliable improvement).

Claims it rests on, and how each held:

- Headline and dek. "A please or a threat shifts a model's answer without
  reliably improving it" is the claim the piece defends, subject and verb with
  the surprise first, no colon mold, no Betteridge question. The dek carries the
  two load-bearing figures (a single-question swing up to 60 points either way,
  an average gain of zero) and adds what the headline omits. Both check out
  against the body and the record.
- Output is a prediction over all the prompt's text; no effort dial (settled).
  Sourced to Ouyang et al. (s2) for the training step and framed in the article's
  own "no effort dial" image. Held.
- Yin GPT-3.5 MMLU 60.02 / 59.44 / 51.93. Verbatim-confirmed in the record.
  Article's "gap of about eight points" (8.09) and "maximum politeness barely
  beat the middle" (0.58) are correct arithmetic. The GPT-4 "relatively stable"
  and Llama-2-70B "nearly proportional" characterizations are verbatim-supported.
  Held.
- Wharton Report 1: politeness swings one question up to 60 points, washes out
  in aggregate. The 60-point figure comes from the authors' Wharton write-up, not
  the PDF body (the record flags the PDF would not render); it is quoted, printed
  as "up to 60 points," not as a false exact. Held, and not overstated.
- Wharton Report 3: no meaningful average gain; per-question +36 to -28 (GPQA);
  a sick-relative plea moved one model by about ten points. Matches the record
  verbatim; "about ten points" hedges the ~10. Held.
- Mind Your Tone: rude beat polite on ChatGPT-4o, 84.8% vs 80.8%, reversing
  Yin's direction. Verbatim. Held.
- Woolf: tips $100-$100,000, fines, death threats, no coherent gradient, best
  output carried neither, author called it inconclusive. Verbatim. Held.
- Steelman (EmotionPrompt +115% BIG-Bench / +8% instruction tasks; Bsharat
  tip/penalty principles). Stated at full strength in the note, then weighed: the
  115% is flagged as a relative gain against a best-case aggregation, and both
  papers are placed on 2023-era or smaller models against the 2024-25 nulls. This
  is the record's own inflation-and-vintage caveat, presented as synthesis, not
  as a single measured fact. Held and correctly weighed, not dropped.

Pushed hardest on the claim I most wanted to keep, that the cross-study
disagreement is itself the finding: the record's Contradictions section supports
reading the unstable sign as the result rather than as noise, and the article
does not overreach past "no specific trick reliably and substantially improves
the answer." No break.

Unverified-decimal check (round focus): the only exact decimals are the
verbatim-confirmed Yin cells and the paper-abstract EmotionPrompt percentages.
The summary-sourced Bsharat ~57.7 / ~36.4 cells are correctly given as direction
only ("rose with model size... largest on GPT-4"). No unverified decimal is
printed as exact.

data-nb-kind audit: seven primary (Ouyang, Yin, both Wharton reports, Mind Your
Tone, Li, Bsharat), two secondary (TechRadar coverage of the viral claim, Woolf
as outside-party reporter on the anecdote). Labels match the primary/secondary
test and the record. Source policy met: 9 sources, 7 primary, 2 secondary.

Citations: opened all nine hrefs as printed plus the "Go deeper" Wharton index
and Woolf links; every one returns 200 and lands on the source itself. The three
internal Background/inline links (prompt-sensitivity, instructions-are-data,
sycophancy) resolve against the library checkout. The commission's required
links are present: prompt-sensitivity and instructions-are-data in Background,
sycophancy inline where the reward-model step is named and held distinct from
this lesson.

No code crept in.

## Cut

Two direct cuts, both against the delete/signpost test in `spec/slop.md`:

- "This is the hinge of the whole question." A signpost that labels where the
  argument stands and does none of the reasoning; the two sentences after it
  carry the pivot ("Training made the model sensitive to framing. It did not make
  any particular framing reliably better."). Cut.
- "and the fairest version of it deserves to be stated at full strength."
  A summary of the article's own method, redundant with the section heading and
  the note label "The claim, stated at full strength." Trimmed to "The folklore
  is not baseless."

Everything else survived the pass. Edge sentences carry facts or reasoning steps
("The advice is checkable and rarely checked" sets the lesson's motive; "That
much is settled" is the series-required settled marking; "That disagreement
across careful studies is itself the finding" is earned interpretive synthesis
the record supports). The negative-parallelism instances ("There is no effort
dial... instead is a prediction"; "Training made the model sensitive... It did
not make any particular framing reliably better") each correct a misconception
the piece actually names, so they are earned, not invented strawmen.

Recent-pattern tics all avoided: no "By the end you will/can" bookend closer, no
"It is tempting to say X. That goes too far," no "doing the work," no
text-in-images "You [do a small thing], and [the failure]" opener, and the
takeaway does not close on a posed diagnostic question. Voice sits in the plain,
concrete register the guide asks for; the "naive picture" paragraph runs the
Ciechanowski move (take the reader's guess seriously, then show what it would
actually do) in the article's own words. No borrowed phrasing from the Evans /
Ciechanowski / Regis exemplars. No prompt leakage: shared wording with the
commission is reported fact (EmotionPrompt's stimulus carries no task
information), not lifted framing. Grammar and punctuation clean; no em-dashes,
colons used correctly.

Furniture: the note is documented and its label names the move it makes; the
comparison table is documented and earns its place, since the cross-study
disagreement it makes scannable is the article's finding, not decoration. No
component reads as a stack-of-blocks filler.

## Reader

Read straight through as the paper's reader, I come away with one mechanism that
the sources do not hand over on their own: output is a prediction conditioned on
every token of the prompt, tone included, which explains in a single frame both
why the tricks move an answer and why they do not reliably move it the good way,
with the settled cause split cleanly from the unsettled payoff and the
cross-study disagreement read as the result. The draft-handoff's original-work
sentence claims exactly this, and the article delivers it. Neither answer is a
restatement of the sources. The prose sits closer to the voice-guide exemplars
than to a median summary. The headline, reread as the largest claim, is one the
body earns.

## Edits

- Cut the signpost sentence "This is the hinge of the whole question." from the
  "How the words reach the model" section.
- Trimmed the method-signpost clause "and the fairest version of it deserves to
  be stated at full strength" from the "strongest case" opener, leaving "The
  folklore is not baseless."

## Required work

None blocking.

- orchestrator: re-run `nb stamp` before the PR. My two cuts lower the word
  count, so the nb-meta `words` (currently 1766) and `reading_minutes` fields are
  now slightly stale.

Optional, not blocking (writer, if a later round revisits visuals): the record
proposes Yin's Figure 3 (three per-level curves: steep for Llama-2-70B, nearly
flat for GPT-4, peak not at maximum politeness) as a source asset that would let
a reader see the "effect shrinks on stronger models" contrast directly. The
handoff explains it was left to prose and the comparison table because the GPT-4
and Llama cells are confirmed only qualitatively. Prose carries the argument, so
this is an opportunity, not a gap.

## Decision

approve — every load-bearing claim held against the reopened sources, the
settled/open line is drawn honestly, the steelman is weighed rather than dropped,
no unverified decimal is printed as exact, and the two slop cuts were the editor's
to make; only a re-stamp remains for the orchestrator.
