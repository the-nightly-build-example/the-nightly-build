# Commission: the-mechanics/answer-length-bias

## The assignment
This desk starts from one behavior anyone who uses AI has seen and explains what
produces it. Tonight's behavior: ask a chatbot a simple question and the answer
comes back padded — a restated question, a preamble, bullet points, a summary,
caveats — far longer than the answer needs. Work backward from that behavior to
its cause, step by step, naming a real part of the system at each step.

The chain to teach, ending on ground:
1. The behavior: modern assistant models default to long, structured answers;
   show it with a concrete, checkable instance (e.g. a one-word-answerable
   question answered in several sentences).
2. The proximate cause: these models are tuned with reinforcement learning from
   human feedback (RLHF). A reward model scores candidate answers, and the policy
   is optimized toward higher reward.
3. The mechanism: the reward model assigns higher scores to longer answers,
   partly because human raters preferred longer/more-thorough answers during
   preference labeling. Length becomes a feature the reward correlates with
   quality. Optimizing against that reward therefore inflates length. Cite the
   measured length-reward correlation and the demonstrations that a large share
   of RLHF's apparent quality gain is explained by length alone (Singhal et al.
   2023, "A Long Way to Go: Investigating Length Correlations in RLHF"; and the
   length-controlled AlpacaEval work, Dubois et al. 2024, which had to correct
   for exactly this).
4. Where the ground is: name what is settled engineering (reward models pick up
   length; length can be regressed out; RLHF pressure raises length) and what is
   open (how much of "helpfulness" is truly length vs content, and whether raters
   prefer length itself or the thoroughness that usually comes with it).

By the end the reader can explain why answers run long and can tell when someone
blames "the model's personality" for what is a measurable training artifact.

## The one-sentence contribution this article owes
Trace the verbose default to a specific, measured place — the reward model's
correlation between answer length and score — and show, with numbers, how much of
RLHF's "improvement" is length rather than substance.

## Boundaries and what not to re-teach
- RLHF, reward models, and preference data are taught across the library. Link
  `the-evidence/instructgpt`, `the-evidence/deep-rl-from-human-preferences`,
  and `the-evidence/proximal-policy-optimization` in Background; use them in
  prose with a plain link at first mention, not numbered sources. Teach only the
  length-correlation piece here.
- Do NOT re-cover `the-mechanics/length-control` (why a model can't hit a target
  word count). This lesson is about the *default* pull toward length, not
  instruction-following on length. Distinguish them explicitly and link it.
- Do not drift into `the-mechanics/sycophancy` or `hedging`; length bias is its
  own mechanism. Link if you must, don't re-teach.
- No code.

## Source obligations (resolved)
`nb source-policy --series the-mechanics`: minimum 8 sources; at least 4 primary,
at least 1 secondary. Primary: Singhal et al. 2023 (length correlations in RLHF);
Dubois et al. 2024 length-controlled AlpacaEval (and the original AlpacaEval);
the InstructGPT paper (Ouyang et al. 2022) for the RLHF pipeline and any human
length preference; a reward-model or RLHF paper documenting the length/reward
relationship (e.g. the "reward model over-optimization" line, or Anthropic/OpenAI
RLHF papers); documentation or model cards where a lab notes verbosity. Secondary:
reputable technical writing for context only, never for a number. Read the papers
for the exact correlation figures and the fraction of the win-rate gain explained
by length.

## Production record (resolved)
`nb production-policy --series the-mechanics`: profile balanced. researcher high /
capable; writer medium / capable; editor high / capable; writing-coach low /
capable. None required; use the most capable available model per role, record
actuals in `nb-meta`.

## Tonight's neighbours (one paper, no overlap)
- the-evidence/long-short-term-memory.
- the-instruments/helm — a holistic benchmark leaderboard. HELM is being kept off
  "judges prefer length," so this lesson owns the length-reward story cleanly.
- what-could-go-wrong/responsibility-gap.
- when-ai-breaks/iruda-chatbot.

## Recent shapes and habits to break (from the last ~2 weeks of this desk)
- This desk keeps closing on a section named like "What the builders haven't
  settled" (false-premise-questions, and the pattern in familiar-pattern-override).
  Mark settled vs open as the series requires, but name that closing section for
  this lesson's own content, not that stock label.
- Recent mechanics deks lean on "the cause sits one level below the answer."
  Don't reuse that phrasing.
- Avoid comma-triad headings closed with "and"; vary construction.
- The behavior-first opener is the series form; find this lesson's own concrete
  instance rather than echoing the neighbour's table-of-examples layout.
