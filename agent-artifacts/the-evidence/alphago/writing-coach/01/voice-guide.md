# Voice guide: the-evidence/alphago

## Directive

Register: a plain, committed explainer voice, addressed to a reader who
thinks in ideas, not code. Never lecture, never perform enthusiasm. State
mechanism the way a careful colleague would explain it across a table: this
happened, here is exactly what "happened" means, here is the number that
proves it.

Reader relationship: the reader is smart and has met the AlphaGo headline
before. Do not re-sell them the story. Write as if correcting your own
earlier loose paraphrase of the same fact, not as if catching the reader in
an error.

Moves that change sentences in this article:

- **Stage the worked example concrete-first, term-second.** When teaching
  Monte Carlo Tree Search or the policy/value split, open with the specific
  numbers of one small case (one board position, one branch count, one
  probability) before the term appears. Name the term in the same sentence
  or the next one, immediately after the concrete case has made it
  necessary, then never re-explain it. Finish that one sub-idea, in its own
  paragraph, before the next term appears. A paragraph that introduces two
  terms has moved too fast.
- **Let the arithmetic sit inside the sentence, not beside it.** Write "the
  search looked at 200 candidate replies before choosing one," not a
  formula or a displayed fraction. When a value needs deriving, do the
  multiplication in prose, mid-sentence, so the reader watches the number
  built rather than receives it finished.
- **Correct the "no human input" overstatement by naming the mechanism,
  not by swinging the sentence.** State plainly what the training data
  actually was and let that fact retire the myth. Reach for the "X is not
  Y, it is Z" shape at most once in the piece, and only if the popular
  claim is specific enough to quote; otherwise the correction is a flat
  declarative the reader can check, not a rhetorical reversal.
- **Give every number a comparison the reader already owns.** Convert
  machine units (positions evaluated, training games, hardware count) into
  something lived: a length of time, a familiar count, a ratio a reader
  can picture. Do this at first use of the number, not in a later aside.
- **Hold judgment to short, plain declaratives, then qualify in the next
  sentence.** State the assessment first ("this was not the breakthrough
  the coverage described"), then supply the one fact that earns or narrows
  it. Never stack qualifiers inside the judgment sentence itself.
- **Diction stays literal.** Prefer the exact word (the number of playouts,
  the specific network, the specific match) over a genre word ("massive,"
  "revolutionary," "groundbreaking"). A grand word is permitted only after
  the sentence before it supplied the fact that earns it.

Recently used, do not reuse:
- The opener mold "The number X published about itself."
- Comma-triad headings or deks (three clauses joined by commas, closed with "and").
- The semicolon-reversal dek ("X did A; Y refuses B") and the suspended-question dek ("...and the real question is whether").
- Any closer or section-opener built to be reused as a formula, or a house catchphrase.

---

## Andrej Karpathy, "AlphaGo, in context"
Source: https://karpathy.medium.com/alphago-in-context-c47718cb95a5
Craft:
- cadence: negation, then reframe, then historical grounding, in one
  breath: "AlphaGo does not generalize to any problem outside of Go, but
  the people and the underlying neural network components do, and do so
  much more effectively than in the days of old AI." The sentence corrects
  by relocating the reader's admiration, not by scolding it.
- argument: the piece never argues "it's not X, it's Y" against the hype.
  It states what is absent ("AlphaGo does not by itself use any
  fundamental algorithmic breakthroughs in how we approach RL problems")
  and lets the reader's own inflated version of the claim fall away on its
  own.
- evidence: a bounded, specific number stands in for a whole category —
  "each episode/game is relatively short, of approximately 200 actions" —
  rather than a vague claim about Go being a long or short game.
- stance: matter-of-fact and unhurried; no sentence performs surprise or
  alarm, even while revising a widely held belief.
- notice: qualifiers attach to structure, not to hedge words — the
  correction is carried by "does not... but," never by "arguably" or
  "some might say."
- diction: plain engineering nouns (components, actions, episode) over
  genre nouns (breakthrough, revolution) except where the piece is
  explicitly naming what did NOT occur.
- reader: assumes the reader already holds the popular story and is here
  to have it recalibrated, not introduced.
- the move the axes miss: the piece corrects a myth by stating what
  specifically is ordinary about the system (standard components,
  standard combination) rather than what is wrong about the reader's
  belief. The myth dissolves as a side effect of precision, never as a
  direct rebuttal.
Calibration: "AlphaGo does not by itself use any fundamental algorithmic
breakthroughs in how we approach RL problems."

## Andrej Karpathy, "Deep Reinforcement Learning: Pong from Pixels"
Source: http://karpathy.github.io/2016/05/31/rl/
Craft:
- cadence: short declarative that closes one sub-problem, then a labeled
  turn to the next — "So the only problem now is to find W1 and W2 that
  lead to expert play of Pong!" followed by a new heading. The sentence
  itself signals the paragraph is finished, not just the topic.
- argument: builds the mechanism entirely from one running concrete case
  (one frame, one paddle, one decision) before any term is named; the
  abstraction (policy network, policy gradient) arrives only once the
  concrete version has made the reader need a name for it.
- evidence: arithmetic is performed inside the sentence — "suppose we won
  12 games and lost 88. We'll take all 200*12 = 2400 decisions we made in
  the winning games" — so the reader watches the number get built rather
  than receiving a finished statistic.
- stance: a guide walking beside the reader, admitting the informality of
  the account, but never loosening the precision of the numbers inside it.
- notice: technical vocabulary is always translated back into the concrete
  case immediately after it's used — "we only produce a probability of
  moving UP" — so a new term never accumulates unexplained.
- diction: exact dimensions and counts (a 210x160x3 frame, UP or DOWN)
  stand in for the abstraction until the abstraction has earned its
  keep.
- reader: intelligent but new to the mechanism; needs the concrete case
  before the symbol, not the symbol defined and then illustrated.
- the move the axes miss: each named term is retired from concrete
  language forever after it is introduced — the piece never re-explains
  "policy" once it exists, it only uses it, which is what makes the later,
  denser paragraphs still readable.
Calibration: "For example suppose we won 12 games and lost 88. We'll take
all 200*12 = 2400 decisions we made in the winning games."

## Chris Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: alternates short declaratives with one longer explanatory
  sentence, then a plain concession — "In theory, RNNs are absolutely
  capable of handling such long-term dependencies... Sadly, in practice,
  RNNs don't seem to be able to learn them." The concession is stated
  flatly, not softened.
- argument: motivates the mechanism by analogy to a lived experience
  first ("Humans don't start their thinking from scratch every second"),
  then only afterward attaches the technical structure to that analogy.
- evidence: the piece leans on structural description over statistics —
  precise about what a component does, sparing about invoking numbers
  until a number is the point.
- stance: companionable and unhurried; the writer explains as someone
  who has already done the hard thinking and is now walking a colleague
  through it.
- notice: a technical term is defined by function in the sentence where
  it is coined — "Gates are a way to optionally let information through.
  They are composed out of a sigmoid neural net layer and a pointwise
  multiplication operation" — never defined abstractly and illustrated
  later.
- diction: concrete, almost domestic nouns for mechanism (gate, layer,
  conveyor belt) rather than pure mathematical vocabulary, without
  loosening precision about what each part does.
- reader: assumed curious and patient, willing to sit through one
  analogy before the payoff, never assumed to already know the shape of
  the answer.
- the move the axes miss: every abstraction is introduced already doing
  something to the reader's running example, never introduced as a
  definition waiting for an example to arrive later.
Calibration: "Gates are a way to optionally let information through. They
are composed out of a sigmoid neural net layer and a pointwise
multiplication operation."

## Alex Irpan, "Deep Reinforcement Learning Doesn't Work Yet"
Source: https://www.alexirpan.com/2018/02/14/rl-hard.html
Craft:
- cadence: a stark short sentence carries the judgment, a period closes
  it, and only then does a qualifying clause follow — "Unfortunately, it
  doesn't really work yet. Now, I believe it can work." The verdict is
  never buried inside its own hedge.
- argument: skepticism accumulates through a sequence of specific failure
  cases rather than through a single sweeping claim; the piece earns its
  conclusion by exhausting examples, not by asserting a mood.
- evidence: a machine unit is converted to something the reader already
  owns at first mention — "RainbowDQN passes the 100% threshold at about
  18 million frames. This corresponds to about 83 hours of play
  experience" — so the number is legible before it is used again.
- stance: professorial and level, disappointed without being cynical; the
  piece never escalates into alarm even while cataloguing failures.
- notice: plain, almost blunt diction for the hard parts ("the beautiful
  demos... hide all the blood, sweat, and tears") stands in contrast to
  careful, exact diction for the technical claims — the plainness is
  reserved for judgment, not for mechanism.
- diction: colloquial phrasing is allowed only in service of an
  assessment, never as a substitute for a technical term.
- reader: a practitioner or a close reader of the field who has heard the
  hype and wants the corrective delivered without being talked down to.
- the move the axes miss: the piece never says a claim is overstated in
  the abstract — it always cites the specific number the overstated
  version would have to be true against, and lets the gap between the two
  numbers do the arguing.
Calibration: "RainbowDQN passes the 100% threshold at about 18 million
frames. This corresponds to about 83 hours of play experience."
