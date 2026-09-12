# Voice guide: the-evidence/variational-autoencoder

## How this piece should sound

This lesson explains one paper, Kingma and Welling's variational autoencoder, to a reader who is smart and reads widely but has never been taught what an autoencoder is. Assume algebra and probability and nothing else about the method. The register is plain and unhurried: state each claim directly, the way someone explains a method they understand well, and where clarity and polish conflict, choose clarity.

The hardest stretch is teaching the evidence lower bound and the reparameterization trick without an equation dump. Nielsen's two-variable passage shows the move that makes that possible. He puts up a simplified picture, uses it, and says plainly where it stops being accurate, so the reader trusts it exactly as far as it holds. The latent space, the two terms of the ELBO, and the random sampling step can each ride on a picture like that, provided the piece stays as honest as Nielsen is about where the picture stops holding. When a term of art first appears, and KL divergence is the one the commission asks you to define, Olah's habit is worth following: ask the plain question the term answers before the symbol for it shows up, the way he asks how one quantity moves when another changes a little.

A worked example will likely do more than any general statement of what the ELBO balances. Karpathy teaches his mechanism on a four-letter alphabet and one short word, small enough to trace by hand. The reconstruction term, the term that pulls the latent distribution toward the prior, and the sampling step whose gradients the reparameterization trick reroutes can each be shown on a case that small before the paper's own experiments arrive. Concrete numbers earn their place even when they are invented for the occasion.

Two kinds of honesty the piece will need are already in the exemplars. The paper was a small-scale proof, run on MNIST and the Frey Face data. Karpathy grades his own generated sample down in flat terms, calling it not good enough while naming what makes it impressive anyway, and that register keeps such a judgment from reading as either debunking or apology. The popular shorthand that VAEs generate images runs ahead of the paper, and correcting it asks for a tone that neither ridicules the shorthand nor oversells the correction; Karpathy's aside that raises a grand claim about RNNs and then deflates it is that tone. When a figure appears, a likelihood value or the size of a dataset, Olah's move of turning a bare number into a comparison the reader already holds is worth borrowing.

The reader will reach a latent space with many dimensions and may feel that following the method means picturing them. That is the worry Nielsen names in his own reader and answers, that nobody visualizes that many dimensions and nobody needs to. The piece can clear it the same way, plainly, without flattering the reader for having felt it.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: http://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "In fact, it is known that RNNs are Turing-Complete in the sense that they can to simulate arbitrary programs (with proper weights). But similar to universal approximation theorems for neural nets you shouldn’t read too much into this. In fact, forget I said anything."

Karpathy states an impressive-sounding fact about RNNs, then spends the next two sentences telling the reader not to make much of it, and closes with a joke at his own expense. The retraction is more emphatic than the claim was. What shows here is a practitioner who has watched this kind of fact get oversold and would rather undersell it than mislead.

> "As a working example, suppose we only had a vocabulary of four possible letters “helo”, and wanted to train an RNN on the training sequence “hello”. This training sequence is in fact a source of 4 separate training examples: 1. The probability of “e” should be likely given the context of “h”, 2. “l” should be likely in the context of “he”, 3. “l” should also be likely given the context of “hel”, and finally 4. “o” should be likely given the context of “hell”."

He teaches the setup on the smallest example that still contains every part: a four-letter alphabet and the word "hello," written out as the four next-character predictions it implies. A reader can work the whole thing by hand before any real dataset appears. Karpathy is visible in his patience with a toy case, where stating the general rule would have been shorter.

> "Okay, clearly the above is unfortunately not going to replace Paul Graham anytime soon, but remember that the RNN had to learn English completely from scratch and with a small dataset (including where you put commas, apostrophes and spaces)."

Right after displaying a generated sample, Karpathy says plainly it will not replace the writer it imitates, and then gives the honest reason it is still worth showing: the model started from nothing and had little to learn from. He marks down his own result before the reader can. That is what lets the enthusiasm elsewhere in the piece stay credible.

## Christopher Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

> "Backpropagation is the key algorithm that makes training deep models computationally tractable. For modern neural networks, it can make training with gradient descent as much as ten million times faster, relative to a naive implementation. That’s the difference between a model taking a week to train and taking 200,000 years."

Olah gives the speed-up as a bare multiple and then immediately restates it as two lengths of time anyone can feel, a week set against 200,000 years. The multiple alone would pass by unread; the comparison makes it register. Olah is doing the reader's arithmetic of scale for them rather than leaving a large number to fend for itself.

> "If one wants to understand derivatives in a computational graph, the key is to understand derivatives on the edges. If a directly affects c, then we want to know how it affects c. If a changes a little bit, how does c change? We call this the partial derivative of c with respect to a."

Olah defines a technical term at the moment it is needed, and he defines it by first asking the plain question it answers: if a changes a little bit, how does c change? The words arrive before the symbol. What is visible is a writer who will not spend a term on the reader without handing them the meaning in the same place.

> "When I first understood what backpropagation was, my reaction was: “Oh, that’s just the chain rule! How did it take us so long to figure out?” I’m not the only one who’s had that reaction. It’s true that if you ask “is there a smart way to calculate derivatives in feedforward neural networks?” the answer isn’t that difficult."

Olah reports his own first reaction to backpropagation, that it looked like just the chain rule, and then argues for several paragraphs against that dismissal. Letting the reader share the feeling that a result is obvious, and then showing why it was not, keeps a simple-looking idea from reading as a small one. The admission that he underrated it at first is the person on the page.

## Michael Nielsen, "Neural Networks and Deep Learning," Chapter 1

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "We carry in our heads a supercomputer, tuned by evolution over hundreds of millions of years, and superbly adapted to understand the visual world. Recognizing handwritten digits isn't easy. Rather, we humans are stupendously, astoundingly good at making sense of what our eyes show us. But nearly all that work is done unconsciously."

Nielsen takes an act the reader performs without thinking, reading digits off a page, and makes it feel hard by counting the evolutionary time behind it, then states outright that we are "stupendously, astoundingly good" at something we never notice doing. The stakes are assembled from concrete facts instead of asserted. His patience shows in how long he stays on why the easy thing is difficult before moving on.

> "(After asserting that we'll gain insight by imagining C as a function of just two variables, I've turned around twice in two paragraphs and said, "hey, but what if it's a function of many more than two variables?" Sorry about that. Please believe me when I say that it really does help to imagine C as a function of two variables. It just happens that sometimes that picture breaks down, and the last two paragraphs were dealing with such breakdowns. Good thinking about mathematics often involves juggling multiple intuitive pictures, learning when it's appropriate to use each picture, and when it's not.)"

Nielsen offers a two-variable picture, then admits in a parenthesis that he has just undercut it twice, apologizes, and asks the reader to trust it anyway while naming the exact conditions under which it fails. He holds a useful simplification and its limits in view at once. The aside is plainly a teacher speaking, aware of the confusion he has created and getting ahead of it.

> "Some people get hung up thinking: "Hey, I have to be able to visualize all these extra dimensions". And they may start to worry: "I can't think in four dimensions, let alone five (or five million)". Is there some special ability they're missing, some ability that "real" supermathematicians have? Of course, the answer is no. Even most professional mathematicians can't visualize four dimensions especially well, if at all."

Nielsen states a worry a new reader genuinely has, that the material demands visualizing many dimensions, quotes it in the reader's own words, and answers that professional mathematicians cannot do it either and use other methods instead. He clears an obstacle out of the way before it can stop anyone. The reassurance is specific and true, which is why it does not come across as talking down.
