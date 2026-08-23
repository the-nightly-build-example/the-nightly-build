# Voice guide: the-evidence/adam-optimizer

## How this piece should sound

This is one lesson in The Evidence, reading the 2015 Adam paper for a reader who is fluent and widely read but new to optimization. The register is plain, concrete, and confident: explain what Adam does and what its convergence theorem claimed without waving the mathematics away, and without dressing it up either. Keep the field's exact vocabulary — a per-parameter adaptive learning rate, the running averages of the gradient and its square, bias correction, the regret bound the theorem states — and define each term in plain words the first time it is used. Gregory Gundersen is the model for that balance: he keeps "ill-conditioned," "singular values," and "backward error" on the page and stays readable, because he defines them as he goes rather than trading them for something vaguer.

Adam's reach is a figure the reader cannot scale on their own — a citation count past a hundred thousand, against experiments run on MNIST and CIFAR-10 rather than anything near frontier size. Where a number like that appears, it can be anchored to a comparison the reader already holds, the way Olah turns "ten million times faster" into a model taking a week to train set against one taking 200,000 years. The size of the foundation under Adam — logistic regression, small MLPs, one convnet — is worth showing at that same concrete grain.

The theorem, and how Reddi, Kale, and Kumar broke it, will carry best through the specific counterexample rather than a description of one. Karpathy makes an abstract failure — a net that "fails silently" — land by working a single case, the flipped labels the network quietly learns to undo. A convex problem on which Adam converges to the wrong point is that kind of case, and it can be worked with its real quantities rather than paraphrased.

A reader arrives assuming that a proof in a landmark paper, cited that many times, must be sound. It was not, and the lesson can say so as plainly as Karpathy punctures the "plug and play" impression of the 30-line snippet, or as plainly as Gundersen asks whether a widely referenced claim is supported by anything. The harder honesty is the one Gundersen models when he defends "never invert a matrix" and then grants that the folk wisdom "may stress the point too much": the Adam proof was flawed, AMSGrad repairs it, and plain Adam is still the sensible default in practice. Both the broken theorem and the working method stay in view at once, with neither hype nor doom.

Where a real contrast organizes the material — what the paper proved against how the field uses it, the empirical claim that held against the theoretical one that did not — a clean parallel can carry it, the way Olah's "Forward-mode differentiation tracks how one input affects every node. Reverse-mode differentiation tracks how every node affects one output" sets two exact statements side by side. The contrast has to be genuine for the parallel to earn its place. And the reaction that a disproven convergence theorem should have sunk the method, or that Adam's success was obvious from the start, is worth voicing and then answering, the way Olah says "Oh, that's just the chain rule!" out loud before showing why it was harder than it looks.

## Christopher Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That's the difference between a model taking a week to train and taking 200,000 years."

Olah states the claim flatly, then spends the third sentence turning an unscalable number into a picture: a week against 200,000 years. The figure does the persuading, and he adds no adjective to it. What is visible is a writer who trusts a concrete comparison more than an intensifier.

> "Forward-mode differentiation tracks how one input affects every node. Reverse-mode differentiation tracks how every node affects one output."

Two sentences built the same way, each naming exactly what one mode tracks. The parallel reads clean because the contrast under it is real: one direction follows an input outward, the other follows an output back. Olah is precise here without a wasted word, and the symmetry of the phrasing is itself the explanation.

> "When I first understood what backpropagation was, my reaction was: "Oh, that's just the chain rule! How did it take us so long to figure out?" I'm not the only one who's had that reaction. It's true that if you ask "is there a smart way to calculate derivatives in feedforward neural networks?" the answer isn't that difficult."

Olah voices the reader's own reaction — that backprop is just the chain rule — in quotation marks, and admits he had it too. Then he takes the easy version of the question seriously before, in the sentences that follow, complicating it. The person shows in his willingness to say the obvious objection out loud rather than pretend the reader would never think it.

## Andrej Karpathy, "A Recipe for Training Neural Networks"

Source: https://karpathy.github.io/2019/04/25/recipe/

> "It is allegedly easy to get started with training neural nets. Numerous libraries and frameworks take pride in displaying 30-line miracle snippets that solve your data problems, giving the (false) impression that this stuff is plug and play."

Karpathy names the comfortable belief — that training is plug and play — and puts a crack in it in the same breath, with the concrete detail of the "30-line miracle snippets" carrying the work. The "(false)" is dropped in without ceremony. What shows is a writer confident enough to contradict the reader's expectation head-on.

> "For example, perhaps you forgot to flip your labels when you left-right flipped the image during data augmentation. Your net can still (shockingly) work pretty well because your network can internally learn to detect flipped images and then it left-right flips its predictions."

An abstract claim, that a net can fail with no error thrown, becomes a single traceable case: flipped labels the network learns to flip back. The example is specific enough to picture and to check. Karpathy teaches the general point by making one instance of it fully concrete.

> "The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data. This step is critical. I like to spend copious amount of time (measured in units of hours) scanning through thousands of examples, understanding their distribution and looking for patterns."

The advice is counterintuitive — start by not touching the model — and Karpathy states it plainly, then grounds it with "(measured in units of hours)," a parenthetical that says what "copious" actually means. The first person is doing real work: he is reporting what he does, not prescribing what one ought to do.

## Gregory Gundersen, "Why Shouldn't I Invert That Matrix?"

Source: https://gregorygundersen.com/blog/2020/12/09/matrix-inversion/

> "So why and when is one approach better than the other? John Cook has a blog post on this topic, and while it is widely referenced, it is spare in details. For example, Cook claims that "Solving the system is more numerically accurate than the performing the matrix multiplication" but provides no explanation or evidence."

Gundersen takes a claim that is "widely referenced" and points out it arrives with "no explanation or evidence," which is the reason his piece exists. He is exact and unhostile about it, quoting the original before he questions it. Visible here is a writer who treats a popular claim as something to be checked rather than passed along.

> "Both decompositions can be used for solving linear systems and inverting matrices, but I'll focus on the LU decomposition because, at least as I understand it, it is typically preferred in practice."

He commits to the LU decomposition and gives his reason, then hedges the reason honestly with "at least as I understand it." The exact terms stay — LU decomposition, linear systems — and the sentence is still easy to follow. The hedge is where the person shows: he marks the edge of what he is sure of.

> "That said, the forward error between matrix inversion and direct solving can be much closer than expected for well-conditioned problems, a point argued by (Druinsky & Toledo, 2012). Thus, in practice, if you care only about the forward error, the folk wisdom that you should never invert a matrix may stress the point too much."

After building the whole case for "never invert a matrix," Gundersen grants that the folk wisdom "may stress the point too much" for well-conditioned problems, and cites the paper that argues it. He holds the rule and its limit at once, softening neither. The honesty is in refusing to oversell a conclusion he just spent the piece supporting.
