# Voice guide: the-evidence/atari-dqn (01)

## Directive

Keep the house register: plain claims for a smart reader who has no codebase, every
term taught in the sentence it appears. Three moves specialize it for this lesson, and
each one changes sentences the default would leave flat.

1. **Sequence by breaking things.** The two stabilization tricks are the spine of this
   lesson, and they only land if the reader watches the naive version fail first. Build
   the plain "neural network trained by Q-learning" the reader would build. Show the
   exact thing that wrecks it: consecutive Atari frames are nearly identical, so the
   network trains on a stream of near-duplicates and forgets everything else; the target
   it fits is computed from the same weights it is updating, so it chases a number that
   moves every step. Only then name experience replay and the target network, each as
   the removal of one named failure. Never introduce a fix before its failure is on the
   page.

2. **Let the record puncture the phrase.** The gap between "human-level control" and the
   29-of-49 count and Montezuma's Revenge at 0 is the article's argument. Report the
   numbers flat and adjacent to the phrase, and let the distance between them carry the
   weight. Do not reach for a verdict adverb ("merely", "supposedly", "in reality"); the
   number already convicts the phrase, and an adverb tells the reader what to feel
   instead of showing it.

3. **Put the reader inside one decision.** At the Breakout moment, make the reader run
   the computation the network runs: four stacked frames in, one Q-value per action out,
   act on the largest. A worked instant the reader executes beats a described one.

Everything else is the house voice. Do not narrate the lesson, do not stack synonyms for
"the network," and hold sentences to one job.

## Licenses

form: second-person direct address ("you")
move: Karpathy seats the reader inside the agent and asks them to feel the problem
  ("I'd like you to appreciate just how difficult the RL problem is") rather than reporting
  it from outside.
bar: the sentence makes the reader perform the agent's computation or face its blindness;
  a "you" that only receives a fact is cut.

form: dry understatement at the hype-versus-record seam
move: Karpathy's self-aware flatness about the field's own hype ("DQN is so 2013 (okay I'm
  50% joking)") states the deflating fact without raising its voice.
bar: at most once, and it rides entirely on a cited number already on the page; it may add
  no judgment the number has not already made.

form: a single concrete analogy for a mechanism the reader cannot see
move: Pavlus makes a failure mode visible with one physical image (an agent trapped
  watching flickering TV noise); Olah fixes a component with one object (a conveyor belt).
bar: the image maps one-to-one onto the mechanism (the moving target, the correlated
  frames, or the missing exploration), and the sentence drops it immediately; an analogy
  extended into a running bit is cut.

## Recently used, do not reuse

- The "the paper never did X" dek and reveal mold (attention-is-all-you-need's "never
  trained a language model"; alphago's "never mentions Lee Sedol"). The Montezuma-zero
  fact is strong enough to carry its own line; do not frame it as another "never."
- The recent the-evidence heading cadence that joins two clauses with a comma and "and."
  Vary the heading shape; a reader skimming only the headings should still reconstruct the
  argument.

## Andrej Karpathy, "Deep Reinforcement Learning: Pong from Pixels"
Source: https://karpathy.github.io/2016/05/31/rl/
Craft:
- cadence: hard swings in sentence length; a dense technical passage is relieved by a
  short colloquial aside, which resets the reader's attention before the next climb.
- argument: observation, then framework, then mechanism, then honest limits; positions the
  algorithm as almost disappointingly simple, then earns back the surprise.
- evidence: shows the concrete instance (the code, the pixels) before the abstraction, so
  the reader experiences simplicity before being told it is simple.
- stance: a curious insider translating for outsiders, openly amused by the field's hype
  cycles rather than selling them.
- notice: small telling details (weights that encode a ball's trajectory; the credit-
  assignment problem) chosen for insight over coverage.
- diction: plain and physical, with the occasional exact technical term set down without
  ceremony.
- reader: direct address and shared amazement; a smart peer thinking aloud, never a
  textbook pronouncing.
- the important move: he states plainly what the method cannot do as vividly as what it
  can, which is the exact honesty this "human-level" lesson needs.

## John Pavlus, "Clever Machines Learn How to Be Curious" (Quanta Magazine)
Source: https://www.quantamagazine.org/clever-machines-learn-how-to-be-curious-20170919/
Craft:
- cadence: alternates concrete scene, concept, technical detail, then real-world stake, in
  a repeating rhythm that keeps a lay reader through hard material.
- argument: opens inside a game the reader can picture, then names the research, then the
  mechanism, then why it matters beyond the game.
- evidence: lets the mechanism be explained in plain behavioral terms rather than by
  citation, grounding every abstract term in something observable.
- stance: conversational but rigorous, knowing without being arch, refusing the jargon
  wall.
- notice: turns a failure mode into one physical picture (an agent stuck on random TV
  noise it can never predict), which is directly transferable to why value learning
  without exploration scores 0 on Montezuma's Revenge.
- diction: everyday nouns doing technical work; "surprise" and "no points in the real
  world" carry the concepts.
- reader: respects the reader's intelligence while translating every term; patient teacher
  naming things as it goes.
- the important move: explains a technical failure in an image the reader already holds,
  the model for making DQN's collapse on long-horizon games visible.

## Christopher Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: measured and stepwise; each paragraph closes one idea before the next opens, so
  the reader never carries two unresolved threads.
- argument: problem-first throughout; establishes why the standard approach fails, then
  introduces each component only as the answer to a failure already shown.
- evidence: a single running example (a language model predicting the next word) anchors
  every new piece of machinery, so no abstraction floats free.
- stance: rigorous without condescension; tells the reader when a detail can be set aside
  and when it cannot.
- notice: gives each component one concrete function before any formalism (the cell state
  "like a conveyor belt").
- diction: calm and exact; new terms enter one at a time, each defined by the job it does.
- reader: intimate and reassuring, respecting intelligence while lowering anxiety.
- the important move: "here is the naive thing, here is exactly how it breaks, here is the
  fix" is the precise engine for teaching experience replay and the target network.
