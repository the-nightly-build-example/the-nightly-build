# Editorial review: the-mechanics/answer-length-bias (editor/01)

## Correct

Thesis, from the draft alone: a chatbot pads a simple answer because RLHF's
reward model learned to score longer answers higher, from human labels that
leaned that way modestly, and reinforcement learning turned that modest lean
into the default; how much of RLHF's apparent gain is length rather than content
has been measured on small open models, and whether raters want length itself or
the thoroughness that rides with it is unresolved.

The claims under it:
1. The behavior is real and checkable: one prompt, 59 tokens supervised vs 243
   after RLHF, near-identical content; and a lab now ships a verbosity dial.
2. The reward model scores longer answers higher (correlation 0.55-0.72), it
   learned this from labels the way OpenAI documented for hedging, and humans do
   prefer the longer answer 62% of the time; RL amplifies that modest edge.
3. Length accounts for most of the measured reward gain on some datasets: 2.0%
   non-length on open-domain QA, and a length-only reward nearly matches full
   RLHF, measured on 7B models scored by a GPT-4 simulator, with no frontier
   decomposition available.
4. Settled: reward models score longer higher and length can be regressed out.
   Open: length itself vs the thoroughness that accompanies it.

How each held. I reopened the record on every figure and mapped each to its
dataset, because the single hardest correctness point is that the fractions are
Llama-7B/GPT-4-simulator measurements. The prose and table both keep WebGPT =
open-domain QA = 2.0% non-length = 0.72 corr = 56% length-only win; RLCD =
dialogue = 27.2% = 0.67 = 64%; Stack = technical QA = 53.4% = 0.55 = 59%. All
match the numbers block. The full-PPO comparison (58-63%), the 61.5% WebGPT
accuracy against a 0.72 length correlation, the GPT-5 560/1288 tokens, the 62%
AlpacaFarm figure, Park's ~2x, the AlpacaEval 22.9->64.3 swing and 0.94->0.98
correlation, and the harmlessness ~-0.3 all check against their owners.

The scope caveat that most needed to survive did: the "two cautions" paragraph
states in prose, not only in the caption, that the decomposition is measured on
7B models on three open datasets with a GPT-4 simulator, that no study
decomposes a frontier assistant, and that the tie to today's chatbots is the
shared mechanism and not a matching number. The SFT-LONG control (length-only
reward beats the longest-of-eight baseline while producing shorter text) is kept
as the reason the win is not only the judge's own length bias, which is the
honest reading of Singhal's mitigation.

No overclaim of spuriousness. The 62% is framed as "a real preference and a
modest one," RL as amplifying it, and the closing section keeps both the
harmlessness reversal (~-0.3) and the Stack qualifier (over half the gain is not
length). The open question is stated as open in both the final body section and
the takeaway, with Singhal's own "may correspond to greater informativeness"
caveat quoted accurately.

Headline, dek and subheads: the headline carries no figure; the dek's only
number, 62%, is AlpacaFarm's and correct. Every subhead is a step of the
argument in the piece's nouns, none a scaffolding slot. data-nb-kind: seven
primary (Singhal, GPT-5 doc as vendor primary, InstructGPT, AlpacaFarm, Park,
Gao, LC-AlpacaEval) and one secondary (rlhfbook), matching the record's own
classifications; no secondary is cited for a number. Sources are numbered in
first-citation order. The taught RLHF lessons (instructgpt,
deep-rl-from-human-preferences, proximal-policy-optimization) are plain prose
links, not numbered sources, and length-control is distinguished as the opposite
failure and linked rather than re-covered. The proof opens and passes every
href, including the internal library links.

No break survived. No place where the record and a source I opened disagree, so
nothing to send back to the orchestrator.

## Reads well

One sentence went. The amplification paragraph closed on "A slight edge in the
labels becomes a dominant habit in the output," which restated the Park sentence
just before it and echoed the section heading; it survives the placeholder test
as a generic small-thing-becomes-big-thing pattern, so it is the edge sentence
the writer added with nothing left to say. Cut, not repaired; the paragraph now
lands on Park's concrete "twice as long, past its own data's length gap."

No briefing or voice-guide leak survived. The behavior list in Why-this-matters
is reworded from the voice guide's opening, but the padded-answer behavior is
the article's own subject, not a writing instruction, so it stays. The
frontier-scope sentences read as the epistemic content the piece owes, not as
lifted clauses.

No formula against the recent record: the dek does not use "the cause sits one
level below the answer"; the closer is named "Length itself, or the thoroughness
with it" for this lesson's own content, not the stock "What the builders haven't
settled"; the headings vary in construction with no "clause, and clause" join;
the one table is a decomposition, not the neighbour's table-of-examples layout.

What I lifted: the double "from" in the LC-AlpacaEval sentence ("rank
correlation with human preference from the LMSYS Chatbot Arena from 0.94") read
as a stumble; changed the first to "in." The draft otherwise held the guide's
register, carrying each figure down to a plain statement rather than an
adjective, in the manner the voice guide draws from Luu and Willison.

## The experience

Read top to bottom, the page earns its furniture: the bookends address the
reader and resolve as a pair, the body speaks to no one, and there is no leftover
Verdict block. The one table shows the three-dataset decomposition faster than
prose would and carries the scope caveat in its caption and the surrounding
prose. No component is missing; three correlation points would not beat the
table, and the roll-off example works in prose with its token contrast.

What the piece gives beyond its sources: it assembles the scattered
length-in-RLHF findings into one causal chain a lay reader can follow, from a
padded answer back to the reward model's measured length correlation, and puts
the decomposition in a single cross-dataset table that marks exactly where the
measurement stops and what it cannot separate. That is the writer's original-work
sentence, and it survives the read. The headline states that chain's finding.

## Edits

- Cut "A slight edge in the labels becomes a dominant habit in the output" (empty
  edge sentence restating the Park finding and the heading).
- Changed "rank correlation with human preference from the LMSYS Chatbot Arena
  from 0.94" to "...in the LMSYS Chatbot Arena from 0.94" (double "from").
- Re-ran nb stamp (words=1929) and the brief's exact nb check: BLOCK: 0, WARN: 0,
  PUBLISHABLE.

## Decision

approve — the argument is correct, correctly scoped to the Llama-7B measurement,
honest about the real 62% preference and the open length-vs-thoroughness
question, and reads in the guide's register; the two faults were mine to fix
directly.
