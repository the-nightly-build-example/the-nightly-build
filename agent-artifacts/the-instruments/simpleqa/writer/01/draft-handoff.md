# Writer draft handoff: the-instruments/simpleqa (01)

## Original-work statement

The article takes one number in circulation, GPT-4.5's reported "37% hallucination
rate," and traces it back through SimpleQA's adversarial question-selection and its
three-way abstention grading to show that "hallucinated 37 percent" and the "62.5
percent correct" leaderboard figure are the same run under two names, and that only
the framing changed. The evidence supplies the construction rule, the abstention
grade, and the o1-card relabeling as separate facts; the article is the thing that
assembles them into a single causal account of why that one number is misread.

## Proof result

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped
words=2039, reading_minutes=9, sources=8. No warnings left standing. Five
sentence-density warnings from the first pass were resolved by splitting the
sentences, not waived.

## For the editor's attention

- **Source floor and TruthfulQA.** The lesson template's floor is 8 sources
  (>=4 primary, >=1 secondary). The evidence's non-taught sources number seven
  (SimpleQA paper, simple-evals, o1 card, GPT-4.5 card, DeepSeek-V3, ABC, AIMon).
  To reach eight I cited the TruthfulQA paper (s7) for one specific contrast fact
  the argument genuinely uses to separate SimpleQA from "does the model lie" (817
  questions, built from human misconceptions), and I also link the truthfulqa
  *lesson* in Background and in prose at first use. This is a reference to a
  contrast fact, not a re-teaching of TruthfulQA, but flagging it because the
  press rule "link the earlier lesson, never a numbered source" is adjacent. If
  the editor prefers TruthfulQA carry no numbered citation, the article is one
  source short of the floor and the researcher would need to supply an eighth
  non-taught source.

- **Attribution flags handled as briefed.** The 62.5% / 37.1% GPT-4.5 figure is
  attributed to the simple-evals leaderboard (s2), and the article states plainly
  that the GPT-4.5 system card measures hallucination with PersonQA, not SimpleQA
  (s5). The "hallucination rate" relabel is sourced to OpenAI's o1 system card
  (s4); the "hallucinated 37 per cent" phrasing to ABC (s1). Cross-snapshot
  variance is handled as a caution (release-day scores in prose and the table),
  not as a weakness of the benchmark.

- **Furniture.** Stat strip (the two framings of one run), numbered steps (the
  three-stage construction pipeline), one table (per-model abstention breakdown,
  the reason correct-given-attempted exists), and one plain note (what the
  "hallucination rate" label swaps). No chart or source asset: the table carries
  the categorical breakdown better than a chart would, and no captured document
  image was needed for the argument.

## Open questions

None blocking. One minor note: the "Introducing SimpleQA" release blog was gated
(403) for the researcher, so the 2024 release framing rests on the paper and the
o1 card rather than the blog; the article makes no claim sourced only to that page.
