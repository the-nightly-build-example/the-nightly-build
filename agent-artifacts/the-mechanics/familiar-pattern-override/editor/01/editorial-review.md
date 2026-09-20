# Editorial review: the-mechanics/familiar-pattern-override (editor/01)

## Skeptic

Thesis: a language model does not check an edited riddle against the idea
inside it; training gives the puzzle's unedited, canonical answer such a high
prior probability that a lightly changed prompt, which still looks almost
identical to the memorized version, rarely outvotes it. What that shows about
"reasoning" is a separate, unsettled question. The claims it stands on:

1. **The behavior is real and measured at scale**, not anecdotal. Tested
   against Jang et al.'s Tower-of-Hanoi-denial prompt (2505.17225, Fig. 1) and
   PHANTOM RECALL's 149-puzzle set (2510.11812). I fetched the HTML render of
   both papers and confirmed every number and quote printed in the table and
   body against the source text: the six closed-model accuracy figures, the
   Thinking-vs-Non-Thinking deltas (+30.2/+10.1/+8.0), the exact "this is not
   a Tower of Hanoi problem" / "permanently infertile" → "temporarily
   infertile" wording, and the "narrow and model-specific" / "persists across
   all systems" quotes. All held exactly. AIW's p=0.649/p=0.431 and its
   below-p<0.2 / o1-preview-near-1 / o1-mini-collapse claims (2406.02061) also
   checked out against the fetched paper text, as did McCoy's 97%/53% (Table
   1, 2309.13638), Razeghi's 70-point gap (2202.07206), and Wu's 99%→62/71/75%
   figure (footnote 11, 2307.02477). No miscitation found; nothing broke.
2. **The mechanism (training frequency sets a high prior) is general, not
   puzzle-specific.** Held by Razeghi's and McCoy's numbers, verified above.
   Tried to break it by asking whether the puzzle domain is special; it isn't
   — Wu's coordinate-convention result shows the identical override on a
   non-puzzle task, which the piece already uses this way. Holds.
3. **The "fades on obscure puzzles" idea is correctly downgraded to an
   inference.** Checked against the round's specific instruction and the
   evidence record's Contradictions section: no puzzle study tests reversion
   rate against fame directly, and the article says so twice, in the puzzle
   section and by never citing a fame-specific study. This is honest.
4. **"Reasoning training does not cleanly fix it" is argued straight, not
   softened.** I pushed on this hardest, since it reverses the commission's
   original framing. The body cites PHANTOM RECALL's own Thinking-mode gains
   alongside its authors' "narrow" verdict, AIW's o1-preview/o1-mini split
   inside one lineage, and Jang's worked examples going the other way
   entirely (reasoning-trained model overrides more than its base). It cites
   Jang's prose and Figure 1, never the unextracted Tables 2–3, matching the
   evidence record's caveat. Holds.

Two breaks, both fixed directly rather than routed:

- **Internal miscount.** The "Why this matters" bookend promised the reader
  it could "tell it apart from two failures that only look similar," but the
  body distinguishes the behavior from three (irrelevant-context,
  memorization, prompt-sensitivity). Fixed the opener to say three.
- **Display-text overclaim in the mechanism paragraph.** "The rest of that
  sentence still looks... almost exactly like a version the model has
  already seen" was fine, but a nearby sentence attributed the
  fame-vs-obscurity claim to "this record cannot measure directly" —
  process language, not a claim about the world, and worth cutting per the
  Cut section below rather than a skeptic break per se.

Named people: Konstantine Arkoudas and the AIW/PHANTOM RECALL/Jang author
teams carry no titles or affiliations in the article, and none are claimed
that the sources don't support, so there is nothing to check there.

## Cut

Ran the slop test on every sentence, the edges twice (in place and pulled
alone), the delete test, and the prompt-leakage check against every briefing
file. Direct cuts made:

- **Broke a six-plus-article opener formula.** The "why this matters" bookend
  opened "You have probably watched this trick, or pulled it yourself" — the
  identical "You have probably [watched/done/been told] X" construction
  opens at least six other published Mechanics lessons (irrelevant-context,
  model-self-identity, overthinking, overused-words, repetition-loops,
  lost-in-the-middle's "you have probably done this"), one of them a direct
  neighbor this piece links. Rewrote to open on the scene itself, no
  "you have."
- **Broke the "By the end you [X], [Y], and [Z]" triad**, the specific habit
  the commission and brief named. Cut it to two items and removed the
  redundant "say why this happens" clause (already promised by "This lesson
  gives you the mechanism" one sentence earlier), which also fixed the
  three-vs-two miscount above.
- **Cut a verbatim house catchphrase.** "That much is settled." closes the
  first paragraph of the open-question section. The identical four words
  close the equivalent paragraph in ten other published Mechanics articles,
  including irrelevant-context.html, a linked neighbor. The sentence before
  it ("the sources above are not divided") already carries the same claim,
  so the phrase failed the delete test on its own terms; cut rather than
  reworded.
- **Broke the "What stays [settled/open] is [Y]" formula** in the takeaway.
  "What stays argued is what to conclude from it" and the closing "this
  evidence does not close it" match the identical pivot construction that
  closes irrelevant-context's, hedging's, and poetic-meter's takeaways
  ("What stays open is...", "What stays unsettled is..."). Rewrote the whole
  back half of the takeaway with a different architecture ("The disagreement
  starts one level up, over what the override proves... It does not decide
  which side of the reasoning argument is right"), while tightening a
  related overclaim: "reasoning-trained models do this too, sometimes more
  than the models underneath them" generalized past what the record
  supports (only Jang's two worked examples show this reversal); it now
  names Jang's own worked examples specifically.
- **Cut internal-process language.** "a claim this record cannot measure
  directly" and "No puzzle study read here tested..." narrated the research
  process rather than reporting a fact. Rewrote to state the claim and the
  gap directly, tightening two short sentences into one along the way.
- Ran `./nb check` after these edits: two `W-SENTENCE-DENSITY` warnings came
  back from two of my own merged sentences (49 and 45 words). Split both back
  into shorter sentences per the editorial direction's clarity rule. Final
  check: `BLOCK: 0`, `WARN: 0`, `verdict: PUBLISHABLE`.

No further slop found. The one earned "not X, it is Y" construction in the
takeaway opener ("not comparing... it is predicting") corrects a real,
named misconception this whole lesson is built to correct, so it stays per
`spec/slop.md`'s exemption for a real, named misconception. The nb-note and
nb-pull components are each used once, with article-specific labels, and
earn their place. No prompt leakage found beyond the process language above;
the commission's framing appears only as corrected facts, never as copied
sentences.

## Reader

Reading it straight through as the declared reader: I have a single causal
chain — training frequency sets a prior, surface similarity lets that prior
outvote a changed premise — built by combining eight separate measurements
that no cited paper states end to end, plus an honest, source-by-source
account of why "more reasoning training fixes it" does not hold up (PHANTOM
RECALL's gains against its own "narrow" verdict, AIW's split lineage, Jang's
reversal). None of the eight sources argues this synthesis or draws this
conclusion; that is what the sources alone would not give me. The prose sits
closer to the voice-guide exemplars than a median AI summary: it opens on a
plain scene and states the finding flatly (Luu), keeps its terms fixed once
set (Ciechanowski's discipline, "prior," "template," "surface similarity"),
and names the specific worked examples and studies that would move the open
question rather than rating how contested it is in the abstract (Evans). The
draft-handoff's original-work sentence matches what the piece actually does.
The headline, reread as the largest claim, is supported directly by Jang's
own worked example and does not overreach it.

## Edits

- Rewrote the "Why this matters" opener to drop the "You have probably
  watched/pulled" construction (matches six+ published Mechanics openers).
- Rewrote the "By the end..." closing sentence of that same paragraph,
  cutting it from a three-item list to two and fixing a three-vs-two
  miscount against the body's neighbor comparison.
- Rewrote "a claim this record cannot measure directly" / "No puzzle study
  read here tested..." to state the claim and the evidentiary gap directly,
  without process language.
- Cut "That much is settled." (verbatim catchphrase reused in ten published
  Mechanics articles, one a linked neighbor).
- Rewrote the takeaway's back half: replaced "What stays argued is what to
  conclude from it" and "this evidence does not close it" (matching the
  "What stays open/unsettled is..." formula in three other takeaways) with a
  different sentence architecture, and tightened "reasoning-trained models
  do this too, sometimes more than the models underneath them" to name
  Jang's worked examples specifically rather than generalizing past them.
- Split two sentences that `nb check` flagged as over-dense after the edits
  above (49 words / 45 words), restoring `WARN: 0`.

## Required work

None. All findings in this round were fixable by direct edit and are logged
above; no gap needs the researcher, no rewrite needs the writer, and no
missing context needs the orchestrator.

The orchestrator must run `./nb stamp` and `./nb check` again before
preparing the PR: this review's edits change the word count and heading
text that the stamp records, and the proof above was run locally against
this checkout's copy, not through the stamped pipeline.

## Decision

approve — the piece passes the skeptic and reader tests, and every cut
found was fixable directly; `./nb check` returns `BLOCK: 0, WARN: 0` after
the edits, but the orchestrator must re-stamp and re-check before the PR
since this review changed the article after the writer's stamp.
