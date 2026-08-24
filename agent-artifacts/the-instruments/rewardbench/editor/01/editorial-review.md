# Editorial review: the-instruments/rewardbench (editor/01)

## Skeptic

The thesis: a RewardBench score is a reward model's accuracy against a
fixed labeling of 2,985 chosen-versus-rejected pairs, and that accuracy
does not predict the quality of the chatbot trained against the reward
model. The article stands on four claims:

- The mechanical account. 2,985 items in four sections; per-prompt
  weighted mean within each section; leaderboard number is the average of
  the four section scores; the released scoring code upweights PRM-Math
  from 447 rows to 984. Checked against Lambert et al. (paper, §3 and
  §4.2), the allenai/reward-bench dataset card (Subset Summary and
  Scoring), and rewardbench/utils.py. Every count reconciles and the code
  quotation matches. Chat 358, Chat Hard 456, Safety 740, Reasoning 1,431
  sum to 2,985. The 984 = 6 x 164 HumanEvalPack total is right and the
  2.20 upweighting factor for math is 984 / 447 = 2.203, correct to two
  decimals.
- Frick et al.'s negative slope. Checked against arxiv.org/abs/2410.14872
  Figure 4 and its wording: the article quotes "we now see a negative
  correlation between RewardBench evaluation score on top models and
  downstream RLHF performance", which is what the paper argues. The
  writer's report flagged this as a direction-only citation with no
  fabricated Pearson. The draft carried a self-referential aside on
  exactly that point ("so I am reporting the direction they state and not
  a coefficient") that I rewrote to describe the paper's own printing
  choice rather than the writer's.
- Sharma's 95%. Checked against arxiv.org/abs/2310.13548 §4.3.1 and
  Figure 7a. The 95% is against a baseline truthful comparator on a
  curated misconceptions set, and the 45% helpful-truthful counterpart is
  present. Both are correctly scoped. Anthropic authorship of the
  preference model and its use to train Claude 2 via RLHF match the
  paper.
- Length bias. Checked against Singhal et al. Table 1 (2%/27%/53%
  non-length gain shares on WebGPT / RLCD / Stack) and Table 2 (length-
  only vs standard PPO within a point or two on each of the three
  datasets), and against Park et al. §4.2 and §4.6 for the doubled
  length and the 30-46% length-explained variance out of distribution.
  All three numbers reproduce exactly.

Display text and headings audit. Headline "At the top of the RewardBench
leaderboard, higher scores predicted lower Chatbot Arena rank" states the
Frick finding as its own claim; the paper's own phrasing supports it in
direction. Dek names the 2,985-pair scope and the Berkeley Chatbot Arena
comparison. Neither headline nor dek pairs two clauses with a comma and
"and" and neither is a comma-triad or semicolon reversal. Subheads read
as steps in the piece's own nouns ("The score is a fixed-pair accuracy";
"Inside Reasoning, math counts as 984 rows, not 447"; "The score never
watched a chatbot train"; "What a top-scoring reward model still does";
"The v2 rebuild lowered the ceiling and kept the warning"). Author names
and affiliations for each cited group (AI2, Anthropic, UC Berkeley,
Anthropic co-authors, UT Austin, Stanford) match their papers.

Source-kind audit. The nine primaries are all first-party documents:
Lambert et al. and the allenai/reward-bench dataset card and reference
scoring code and AI2 launch blog for RewardBench 1; Malik et al. and the
allenai/reward-bench-2 dataset card for RewardBench 2; Frick et al. for
the downstream disconnect; Sharma et al. for preference-model sycophancy;
Singhal et al. and Park et al. for length in PPO and DPO. The single
secondary (Yeung, The Letter Two) is external contemporaneous reporting
on the v2 release, correctly used to corroborate that the launch and its
policy-family caveat were communicated publicly rather than to own any
number. Independence tests hold: Frick's group is at UC Berkeley and
independent of the AI2 authoring party. All ten href values point at the
canonical arxiv, dataset-card, GitHub, allenai-blog, huggingface, and
thelettertwo pages the sources actually live on.

No claim broke. One item routed to the writer: the metadata word count
in `<script id="nb-meta">` (currently 2117) should be recomputed and the
proof step re-run after these edits, which trimmed roughly fifty to
seventy words on net.

## Cut

The load-bearing repair the brief named. The draft closed the RewardBench
2 section with an `nb-note nb-note-strong` "Verdict" block that summarized
the whole piece's finding in six sentences. Press editorial forbids
closing the body with a Verdict note or any block that restates the
finding, and the takeaway bookend already carried five of the block's six
points. I cut the block whole. The one point it made that the takeaway
did not carry positively - that a very low score does rule a model out,
the honest use of the prerequisite framing - I folded into the takeaway
as two short sentences that balance the negative claim already there.

Slop pass. Six sentences failed the placeholder-noun test or the
signpost / self-narration rules and I cut or rewrote each.

- "The number carries a lot on its back." Fluff. The preceding sentence
  already showed the number's weight by naming what depends on it. Cut.
- "The reward model's leaderboard score is its win rate on those 2,985
  judgments, averaged in a way the next section describes." Self-
  narration of the lesson's structure. Rewrote as "aggregated across the
  four sections" so the sentence carries the fact and leaves the
  mechanism for the section that owns it.
- "The paper's Figure 4 shows the reversal graphically at the top of the
  leaderboard. The authors do not print a Pearson value for the negative
  slope, so I am reporting the direction they state and not a
  coefficient." Self-reference in the body. Rewrote to describe the
  paper's printing choice: "The paper prints only the direction. It does
  not publish a Pearson value for the negative slope."
- "Read against RewardBench, that number is a comparator: an outside
  group treated 'correlates with downstream chatbot quality' as the
  thing to measure, and reports what they got when they measured it."
  Empty tail ("reports what they got when they measured it" is a
  tautology) and meta-narration of what the number is being used for.
  Rewrote as one sentence that ties PPE's 77% to what the RewardBench
  release itself said was still to be measured.
- "Two lines of primary evidence give hard numbers for those failure
  modes on reward-shaped signals of the exact kind RewardBench scores."
  Forecast signpost for the two paragraphs that follow. Rewrote the
  section opener as a substantive claim (a high RewardBench score is
  consistent with both a sycophantic preference model and a length-
  loving one) so the paragraphs beneath teach without being announced.
- "The downstream story is now partly told, and told carefully."
  Empty framing sentence, unearned punchline. Cut; the Pearson 0.87
  paragraph that followed stands on its own facts.

Punctuation pass. Two semicolons in body prose joined independent
clauses where a period was the plainer mark and I replaced them:
orientation ("optimizes a chatbot against; the earlier lesson") and
aggregation ("weighed equally'; the mechanism"). The third body
semicolon (Singhal's WebGPT / RLCD / Stack list, where each item carries
its own commas) survives as a list separator, the one job the standard
reserves the semicolon for. No em-dashes in the article.

Edge pass. Every paragraph and section first-and-last sentence tested
in isolation. The takeaway's closer ("AI2's own RewardBench 2 report
keeps the warning that a high score is a prerequisite and not a
sufficient condition for RLHF") carries the piece's judgment. The Why-
this-matters closer ("where the researchers who built it and the
researchers who tried it out have said it does not go") answers the
opener with the two constituencies the article draws on. Section edges
survive after the cuts above.

Recent-pattern check. The Why bookend does not open with "You have
read that..." or close with a "By the end you will know..." enumeration,
and does not narrate itself with "this lesson [verb]". The takeaway
does not resolve with "The question was whether..." or close with "That
is real, and it is what X." The headline does not pair two clauses with
a comma and "and". The dek is two short declaratives, not a comma triad,
semicolon reversal, or "the real question is whether" suspension.

Prompt leakage. Compared body against commission, brief, editorial
direction, and voice guide. The specific numbers and clauses trace to
the evidence record and the primaries, not to briefing paraphrase. The
brief's caveats on Frick, Singhal, Sharma, and the 0.87 scope are
honored without lifting the brief's wording.

Voice guide. The register the guide directs (Julia Evans's patient
walk-through with specific counts, Tufekci's define-then-contrast, Luu's
naming of the person and the tool) is what the piece delivers: 2,985
items broken to 358 / 456 / 740 / 1,431; the 984-not-447 upweighting
with its 2.20x factor; Frick and colleagues named at UC Berkeley with
the exact instrument they measured; Sharma's Claude 2 PM with the
comparator and the 95% both named. No borrowed phrasing from the guide's
quoted exemplars.

## Reader

Read straight through as the paper's smart-but-new reader. What I have
that the primaries alone would not give me: a walk from the leaderboard
number down to the 2,985 pairs, the per-section per-prompt weighting,
and the 984-not-447 upweighting inside Reasoning that the leaderboard
itself never surfaces; then the same instrument held against the
Berkeley team that actually trained chatbots with these reward models
and got the opposite ranking near the top, against the sycophancy
number from the production Claude 2 preference model, against the
Singhal decomposition that varies by dataset, and against the RewardBench
2 rebuild that AI2 shipped to restore discrimination and that AI2 itself
scopes back down for PPO. The draft-handoff's original-work sentence
promises exactly that synthesis, and the article delivers it. The prose
sits closer to the voice-guide exemplars than to a median AI summary:
specific counts and named people carry the exposition, and the harder
claim (the score is not a downstream predictor) is built rather than
asserted. Reread the headline as the piece's largest claim: "At the top
of the RewardBench leaderboard, higher scores predicted lower Chatbot
Arena rank" is Frick's finding in one clause, with the "at the top"
scope on the front so the scanning reader gets both the claim and the
caveat.

## Edits

- Removed the `nb-note nb-note-strong` Verdict block at the end of the
  RewardBench 2 section; press editorial forbids closing the body with
  a Verdict or restating block.
- Added two sentences to the takeaway ("A very low score rules a reward
  model out. A very high one does not rule it in.") to carry the one
  positive framing from the Verdict that the takeaway did not already
  hold.
- Cut "The number carries a lot on its back." from the Why-this-matters
  bookend as fluff, and rephrased the next sentence's referent
  accordingly.
- Rewrote "averaged in a way the next section describes" to "aggregated
  across the four sections" in the orientation section, removing body
  self-narration.
- Changed semicolon to period in orientation: "optimizes a chatbot
  against; the earlier lesson on InstructGPT walks through" -> "against.
  The earlier lesson on InstructGPT walks through".
- Changed semicolon to period in the aggregation section: "'math and
  code abilities... weighed equally'; the mechanism is this upweighting"
  -> "'... weighed equally'. The mechanism is this upweighting".
- Rewrote the downstream-mismatch self-reference: "The authors do not
  print a Pearson value for the negative slope, so I am reporting the
  direction they state and not a coefficient." -> "The paper prints
  only the direction. It does not publish a Pearson value for the
  negative slope."
- Cut "actually" from "Seven months later, a Berkeley group actually
  ran the comparison." Filler intensifier.
- Rewrote the downstream-mismatch closer on PPE from "Read against
  RewardBench, that number is a comparator: an outside group treated
  'correlates with downstream chatbot quality' as the thing to measure,
  and reports what they got when they measured it." -> "That is a
  measured value for the correlation the RewardBench release had said
  was still to be measured."
- Rewrote the what-a-top-scoring-reward-model-still-does opener from
  "A high RewardBench number is consistent with a reward model that
  also, once it is optimized against, produces answers that are
  agreeable and long. Two lines of primary evidence give hard numbers
  for those failure modes on reward-shaped signals of the exact kind
  RewardBench scores." to a substantive claim ("A reward model that
  ranks high on RewardBench can still prefer sycophantic answers over
  correct ones, and can still assign higher scores to longer
  completions than short ones of equal quality. Both patterns are
  measured on reward-shaped signals of the kind RewardBench grades.")
  that does not forecast the two paragraphs beneath it.
- Cut the RewardBench-2 signpost "The downstream story is now partly
  told, and told carefully." Empty framing.
- Split a semicolon in the RewardBench-2 downstream paragraph: "it is
  not a PPO training-run result; on PPO the paper is explicit" -> "It
  is not a PPO training-run result. On PPO the v2 paper is explicit".
- Changed "the paper" to "the v2 paper" in that same sentence to
  disambiguate from Lambert et al., since the previous quotation was
  from Malik et al.

## Required work

- writer: re-run the proof (`./nb check
  .nb-work/the-instruments/rewardbench/library/the-instruments/rewardbench.html
  --series the-instruments --library /home/user/library-checkout`) and
  update the metadata `words` count in the `<script id="nb-meta">`
  block, which is now off by roughly fifty to seventy words after the
  cuts above. No source added, no source removed, no claim moved; the
  proof should reproduce a PUBLISHABLE verdict.

## Decision

approve, with the writer's proof re-run as the one remaining item; the
load-bearing repair (Verdict block removed, its one non-redundant
sentence folded into the takeaway) is done, every precision the brief
named (Frick direction-only, 0.87 scoped to RewardBench 2 versus best-of-
N, Singhal figures named per dataset, Sharma's 95% named against
baseline-truthful on the curated misconceptions set) verifies against
the primaries, and the slop and self-reference cuts leave a lesson that
walks the reader from the fixed-pair accuracy to the mechanical
aggregation to the four independent downstream failure modes it does not
capture.
