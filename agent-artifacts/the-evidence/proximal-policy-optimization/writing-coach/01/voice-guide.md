# Voice guide: the-evidence/proximal-policy-optimization (01)

## How this piece should sound

Introduce the clipped objective the way Sutton and Barto introduce a new term
in the bandit chapter: define it in the sentence where the piece needs it, then
use the very next sentence to say what changes because of it. When the
probability ratio and the clip range enter, one sentence can carry what the
ratio measures and the next can carry what the clip does to it, stated as a
fact about this optimizer rather than a general truth about policy gradients —
the way Sutton and Barto write "exploitation is the right thing to do to
maximize the expected reward on the one step, but exploration may produce the
greater total reward in the long run" as a fact about the bandit problem, not
a maxim about learning.

Run the worked example the way Karpathy's backprop notes run theirs: pick
actual numbers for the ratio and the advantage, carry them through the
unclipped and the clipped objective side by side, and show which term the
`min` in the objective actually selects and why. Karpathy's example works
because every number in it — the −2, the 5, the resulting 3, the −12, the −4
— is one the reader could recompute by hand; a single example carried
completely this way teaches more than two sketched partially.

Where the 2017 paper's own claims are modest, informal, or asserted without
proof, say so as plainly as Goh says a familiar account "isn't wrong, but it
fails to explain" the behavior it's supposed to cover: name exactly what is
established and what is left unexplained, in the same breath, without
treating the gap as an apology. This piece has more than one place that calls
for it — the paper's own theoretical justification for the clip, and the leap
from what the 2017 benchmarks measured to what the method is trusted for now.

Hold benchmark scale and current use as two separate, both-true facts rather
than letting one stand in for the other, the way Goh holds gradient descent's
appealing exponential rate and its "infuriatingly small" progress in practice
as two things that are both real at once. State the size of the 2017 test
suite in its own sentence, state today's use in its own sentence, and let the
distance between them be visible in the reporting rather than declared.

Define each term of art once, at the sentence where the piece cannot proceed
without it — advantage, surrogate objective, clip range, trust region — the
way Karpathy's circuit notes earn "beautifully local" by immediately cashing
it out into the two concrete things a gate computes, rather than asserting the
adjective and moving on. Once a term is set, this piece reuses it exactly;
nothing here calls for a second name for the same thing.

## Richard S. Sutton and Andrew G. Barto, "Reinforcement Learning: An Introduction" (2nd ed.), Chapter 2: Multi-armed Bandits

Source: http://incompleteideas.net/book/RLbook2020.pdf (Chapter 2, "Multi-armed Bandits")

> "The most important feature distinguishing reinforcement learning from other
> types of learning is that it uses training information that evaluates the
> actions taken rather than instructs by giving correct actions. This is what
> creates the need for active exploration, for an explicit search for good
> behavior."

This opens a new chapter by stating the one contrast the chapter needs and
nothing else: what evaluative feedback is, what it isn't, and what that
absence requires. No sentence precedes it announcing that the distinction
matters; the distinction is left to do that work itself.

> "When you select one of these actions, we say that you are exploiting your
> current knowledge of the values of the actions. If instead you select one
> of the nongreedy actions, then we say you are exploring, because this
> enables you to improve your estimate of the nongreedy action's value.
> Exploitation is the right thing to do to maximize the expected reward on
> the one step, but exploration may produce the greater total reward in the
> long run."

Two terms get defined in two short sentences, each right where the argument
first needs it, and then the sentence that follows commits to a claim about
one of them and immediately narrows it. The narrowing ("on the one step" against
"in the long run") is doing the actual work; without it the sentence would be
a slogan instead of a finding.

> "It achieved a reward-per-step of only about 1, compared with the best
> possible of about 1.54 on this testbed."

A result reported as one number against another, both qualified with "about"
because the underlying figure is an average over 2000 runs and the authors
say so a few sentences earlier. The comparison, not an adjective, is what
tells the reader the greedy method failed.

## Gabriel Goh, "Why Momentum Really Works"

Source: https://distill.pub/2017/momentum/

> "We often think of Momentum as a means of dampening oscillations and
> speeding up the iterations, leading to faster convergence. But it has other
> interesting behavior. It allows a larger range of step-sizes to be used,
> and creates its own oscillations. What is going on?"

The opening states the reader's existing understanding first, names two things
that understanding doesn't cover, and only then asks the question — so the
question isn't an attention-getting device, it's the exact thing the rest of
the piece has to answer. A reader knows by the fourth sentence what the piece
owes them.

> "gradient descent is a man walking down a hill. He follows the steepest
> path downwards; his progress is slow, but steady. Momentum is a heavy ball
> rolling down the same hill. The added inertia acts both as a smoother and
> an accelerator, dampening oscillations and causing us to barrel through
> narrow valleys, small humps and local minima."

The metaphor is given in full, without hedging while it's being told. It earns
the right to be corrected in the very next sentence because it was stated
plainly enough first to be worth correcting.

> "For a step-size small enough, gradient descent makes a monotonic
> improvement at every iteration. It always converges, albeit to a local
> minimum. And under a few weak curvature conditions it can even get there at
> an exponential rate. But the exponential decrease, though appealing in
> theory, can often be infuriatingly small. Things often begin quite well —
> with an impressive, almost immediate decrease in the loss. But as the
> iterations progress, things start to slow down. You start to get a nagging
> feeling you're not making as much progress as you should be."

The theoretical guarantee and the lived experience of running the algorithm
are stated back to back, both asserted as true, with neither cancelling the
other. "A nagging feeling you're not making as much progress" names something
a person who has actually watched a loss curve would recognize, which is where
the writer is visible in an otherwise mathematical passage.

## Andrej Karpathy, CS231n course notes: "Backpropagation, Intuitions"

Source: https://cs231n.github.io/optimization-2/

> "Notice that backpropagation is a beautifully local process. Every gate in
> a circuit diagram gets some inputs and can right away compute two things:
> 1. its output value and 2. the local gradient of its output with respect to
> its inputs. Notice that the gates can do this completely independently
> without being aware of any of the details of the full circuit that they are
> embedded in."

"Beautifully local" is an adjective that could float on its own, but the very
next clause converts it into two checkable facts about what a single gate
computes. The claim is earned before the sentence is allowed to end.

> "The add gate received inputs [-2, 5] and computed output 3. Since the gate
> is computing the addition operation, its local gradient for both of its
> inputs is +1. The rest of the circuit computed the final value, which is
> -12. During the backward pass in which the chain rule is applied
> recursively backwards through the circuit, the add gate (which is an input
> to the multiply gate) learns that the gradient for its output was -4."

Every number here is one the reader can independently recompute: the inputs,
the intermediate output, the final value, the returning gradient. The passage
narrates the actual order of computation — forward, then backward, then this
one gate — instead of restating the chain rule as a general law.

> "To be clear, this function is completely useless and it's not clear why
> you would ever want to compute its gradient, except for the fact that it is
> a good example of backpropagation in practice."

The writer admits the worked example has no purpose beyond being a good
example, a fact a less careful writer would leave out to sound more
consequential. Saying it plainly here is exactly why the harder technical
claim that follows it reads as trustworthy rather than oversold.
