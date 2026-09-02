# Editorial review: the-evidence/constitutional-ai (editor/01)

## Skeptic

Thesis: the 2022 Constitutional AI paper showed that an AI model, guided by a
short written list of instructions, could train a chatbot crowdworkers judged
less harmful than one trained on human harm labels, but that result is a
preference margin on one lab's 52B models aimed at harmlessness, not a
governance mechanism and not proof that AI judgment matches human judgment in
general, and today's "the model has a constitution" talk has drifted well past
what the paper measured.

The claims it stands on, and how each held:

- **The method is two stages that each swap a human judgment for an AI one.**
  Stage one: a helpful-only model critiques and revises its own answers against
  sampled principles (SL-CAI); stage two: a copy of the model picks the less
  harmful of two answers, and those AI preference labels train the preference
  model that drives RL (RL-CAI/RLAIF). Checked sentence by sentence against the
  evidence record's paraphrase of arXiv 2212.08073; the article's account
  matches, including that the final preference model blends AI harmlessness
  labels with human helpfulness labels. Held.

- **The "constitution" is a small set of author-written instructions, not a
  charter.** Sixteen critique/revision principles plus sixteen comparison
  principles. The article quotes one comparison principle and one
  critique/revision pair verbatim (both match the evidence exactly) and carries
  the paper's own admission that the principles were "selected in an ad hoc
  manner for research purposes." Held. One precision break: the draft twice
  called the total "thirty-two sentences," and its own stage-one blockquote is
  labeled a two-sentence "critique-revision pair," so sixteen such pairs are not
  thirty-two sentences. The number thirty-two (16 + 16 principles) is right; the
  unit noun was wrong. Fixed directly to "instructions" (the article's own word
  from the orientation), number untouched.

- **The headline result is directional, not a score.** The article states the
  paper reports no absolute Elo numbers, that its chart caption warns only
  differences are meaningful, and that the result reads as a margin one model
  won by. This matches the evidence's insistence on directional reporting. No
  invented score anywhere. Held. Every figure traces to arXiv 2212.08073: 52B
  model size, 10,274 helpfulness and 8,135 harmlessness comparisons across 24
  snapshots, 182,831 AI harmlessness comparisons, 438 HHH questions. All check
  out against the evidence's Numbers block.

- **At 52B the AI feedback labeler had not reached human-feedback parity; parity
  was extrapolated.** Anchored on the paper's Figure 4 and its caption ("models
  larger than 52B will be competitive..."), quoted verbatim. I inspected the
  committed asset (a crop of Figure 4): the human-feedback preference-model line
  sits above the two chain-of-thought AI-judge lines across every size and ends
  higher at ~52B, exactly what the caption claims. The chart's numbers, labels,
  scales, and legend are honest and match the prose. Held.

- **Later work confirms the harmlessness win but narrows the broad reading.** Lee
  et al. (Google) is quoted stating the 2022 paper "did not directly compare the
  efficacy of human vs. AI feedback," and its win rates (71/73, 63/64, ~50%
  head-to-head, 88/76/64 on harmlessness) match the evidence. The article also
  reports Google's judge used a plain one-line preamble, not a written
  constitution, with only "mixed" gains from a detailed one. Held. All three
  commissioned tensions are carried in the open, not buried.

I opened every source URL as the article cites it. All six resolve to the
source's own page: arXiv 2212.08073, 2204.05862, and 2309.00267 (title confirmed
as "RLAIF vs. RLHF"); Anthropic's "Claude's Constitution" (the "trained with
Constitutional AI" phrase, the principle-source list, the "neither finalized"
caveat, and the Jan 21 2026 update banner all present); Anthropic's Collective
Constitutional AI writeup (~1,000 adults, Polis, nine-dimension BBQ, MMLU/GSM8K
equivalence, "very preliminary and imperfect"); and the TIME report. Internal
Background and prose links (instructgpt, deep-rl-from-human-preferences,
direct-preference-optimization) all exist in the library. The figure's
data-nb-url points to the paper's own PDF at the figure's page, which is the
source itself.

One break I could not fix from the record, because the source I opened
contradicts the record. The draft reads: "Reporting on the update quotes
Anthropic's Amanda Askell describing the constitution as text 'addressed to
Claude and used at different stages in the model's training to shape its
character.'" I read the TIME article twice. That phrase is the reporters'
(Ostrovsky and Perrigo) own narration, with no quotation marks and no
attribution to Askell. Askell is quoted elsewhere in the piece, but not for
these words. The evidence record repeats the same error, recording the phrase as
an "Amanda Askell (quoted by TIME)" quotation. This is a false quotation
attributed to a named person, so it goes back rather than getting silently
reworded: the researcher corrects the record and the writer corrects the prose.
The article's sizing argument does not depend on the attribution (the words are
genuine TIME reporting and still show the present-day drift), so the fix is
narrow.

## Cut

No sentence needed deleting for slop. I ran the placeholder test on every edge
and every furniture sentence. The negative-parallelism constructions
("not a charter or a set of legal principles," "not a score," "not a general
test of AI judgment," "Suggest, not show") each correct a misconception the
piece actually names and then spends the paragraph on, so they are earned
contrasts, not the reflex. The dek is a main clause plus a trailing appositive,
avoiding both the ", and"-twist and the comma-triad molds the pattern notes
flag. The five section headings reconstruct the argument in the article's own
nouns and none share a construction; the closing heading ("The constitution
changed more than the evidence has") breaks the recurring "Where X still Y"
mold. The bookends address the reader as the template allows and each sentence
belongs to this lesson's particulars. No prompt leakage: the sizing language
("one lab's models," "not a governance mechanism") is substantive analysis the
evidence supports, not a planning label lifted from the commission. No borrowed
phrasing from the voice-guide exemplars.

Two writing-correctness fixes rather than slop cuts: the semicolon splice in the
how-big section became a period (house punctuation default), and the "sentences"
unit error above. One furniture repair: the stat strip's 182,831 was the only
stat with no prose anchor, which the stat-strip standard requires, so I anchored
it in the stage-two sentence that already carries the s1 citation.

## Reader

Read straight through as the paper's reader — smart, no time in a codebase — I
finish able to say what "AI feedback" and a model "constitution" are
mechanically (two models, thirty-two short instructions, critique-and-revise
then an AI preference comparison) and, more than any single source gives me, how
much weight the 2022 result can bear: a harmlessness preference margin on one
lab's 52B models, with parity to human feedback extrapolated rather than shown,
and with later work suggesting a plain preamble, not the written constitution,
may carry the effect. The draft-handoff's original-work claim — that the article
gathers the paper's scattered admissions into one sizing verdict a newcomer can
hold — survives the read; the piece delivers exactly that. The prose sits closer
to the voice-guide exemplars than to a median summary: it defines each term in
the sentence that introduces it (Lee's habit) and anchors Elo to chess rather
than leaving the number bare (Willison's). The headline, read as the largest
claim, holds: the stage-two AI judge is guided by sixteen comparison principles,
and RL-CAI was the less-harmful result, with no invented score.

## Edits

- Changed "thirty-two sentences in total" to "thirty-two instructions in total"
  (rulebook intro): sixteen stage-one units are critique/revision pairs, so the
  total is not thirty-two sentences.
- Changed "these thirty-two sentences were chosen" to "these thirty-two
  instructions were chosen" (ad hoc paragraph), same reason.
- Changed the stat-strip label "sentences in the constitution" to "instructions
  in the constitution" to match.
- Anchored the stat-strip figure 182,831 in prose: "blends those AI-made
  harmlessness labels" became "blends 182,831 AI-made harmlessness labels" in the
  stage-two paragraph, inside the existing s1 citation, so every stat is carried
  by cited prose.
- Replaced the semicolon splice in the how-big section ("the result; there is no
  number to quote") with a period.

## Required work

- **researcher:** The evidence record's TIME (s6) entry records the phrase
  "addressed to Claude and used at different stages in the model's training to
  shape its character" as a quotation from Amanda Askell. The TIME article
  presents those words as the reporters' own narration, not as an Askell quote.
  Correct the record so the misattribution does not propagate.
- **writer:** In the present-day section, the sentence "Reporting on the update
  quotes Anthropic's Amanda Askell describing the constitution as text 'addressed
  to Claude and used at different stages in the model's training to shape its
  character'" attributes to Askell words that are TIME's own description.
  Reattribute the phrasing to the reporting itself (source s6), keeping the
  wording and the citation, and drop the Askell attribution. Then rerun the
  proof.

## Decision

revise — the article is otherwise sound and well-sized, but it attributes a
verbatim quotation to a named person, Amanda Askell, that the cited source
presents as the reporters' own words; that misattribution (mirrored in the
evidence record) must be corrected by the researcher and writer before publication.
