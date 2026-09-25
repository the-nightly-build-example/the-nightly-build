# Voice guide: the-evidence/elmo

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still remember when I trained my first recurrent network for Image Captioning. Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-25

The claim ("something magical") is allowed because the very next sentence cashes it in with a specific memory: a real model, a real training run, a result he can describe. He doesn't stay on the abstraction.

> "So how do these things work? At the core, RNNs have a deceptively simple API: They accept an input vector x and give you an output vector y. However, crucially this output vector's contents are influenced not only by the input you just fed in, but also on the entire history of inputs you've fed in in the past."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-25

The question is answered in the same sentence, not held for suspense. He states the mechanism in one plain clause first ("deceptively simple API") and only then adds the complication ("However, crucially"), so a reader has the simple version before the catch.

> "Again, what is beautiful about this is that we didn't have to hardcode at any point that if you're trying to predict the next character it might, for example, be useful to keep track of whether or not you are currently inside or outside of quote. We just trained the LSTM on raw data and it decided that this is a useful quantitity to keep track of."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-25 (the misspelling "quantitity" is in the original)

He states the finding before the mechanism that produced it: what the network learned, then how. "We just trained... and it decided" keeps the actor visible in a sentence that could easily have gone passive ("this behavior emerges").

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don't throw everything away and start thinking from scratch again. Your thoughts have persistence."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-25

He motivates the mechanism from an experience the reader already has, before naming any network. Each sentence adds one fact and repeats the same words ("start from scratch") rather than reaching for a synonym, so nothing is left to guess at.

> "The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged. The LSTM does have the ability to remove or add information to the cell state, carefully regulated by structures called gates."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-25

One analogy (a conveyor belt) carries the whole paragraph; he doesn't add a second image on top of it. The analogy explains something plain prose alone would take longer to establish: that information can pass through mostly unchanged.

> "Written down as a set of equations, LSTMs look pretty intimidating. Hopefully, walking through them step by step in this essay has made them a bit more approachable."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-25

The closing line names the real difficulty (the equations are intimidating) instead of a generic note of importance, and says plainly what the piece did about it. No verdict, no restated summary of every section above it.

## Jay Alammar, "The Illustrated Transformer"

Source: https://jalammar.github.io/illustrated-transformer/

> "Let's begin by looking at the model as a single black box. In a machine translation application, it would take a sentence in one language, and output its translation in another. Popping open that Optimus Prime goodness, we see an encoding component, a decoding component, and connections between them."

Checked: https://jalammar.github.io/illustrated-transformer/, retrieved 2026-09-25

The joke ("Optimus Prime goodness") only works because it is doing the actual work of the sentence: it names the action (popping open a sealed box) that the diagram right after it shows. Cut the nouns around it and the joke goes with them.

> "Don't be fooled by me throwing around the word "self-attention" like it's a concept everyone should be familiar with. I had personally never came across the concept until reading the Attention is All You Need paper. Let us distill how it works."

Checked: https://jalammar.github.io/illustrated-transformer/, retrieved 2026-09-25

He places himself at the reader's starting point before he teaches anything, which earns the plain explanation that follows instead of assuming it.

> "What does "it" in this sentence refer to? Is it referring to the street or to the animal? It's a simple question to a human, but not as simple to an algorithm."

Checked: https://jalammar.github.io/illustrated-transformer/, retrieved 2026-09-25

One worked example (a single sentence with one ambiguous "it") carries an abstract claim about the model, instead of a list of cases. The two questions are answered immediately after, so they read as setup and not padding.

## Julia Evans, "How to trick a neural network into thinking a panda is a vulture"

Source: https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture

> "But of course, neural networks aren't magic–nothing is! I recently read a paper, "Explaining and Harnessing Adversarial Examples", that helped demystify neural networks a little for me. The paper explains how to force a neural network to make really egregious mistakes."

Checked: https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture, retrieved 2026-09-25

She names the source paper by title in the second sentence and states in one clause what she is about to show ("force a neural network to make really egregious mistakes"). The claim of the piece is on the table before any mechanism.

> "Now, none is this is too surprising to me–machine learning is my job, and machine learning habitually produces super weird stuff. But if we're going to fix the super weird errors, we need to understand why they happen!"

Checked: https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture, retrieved 2026-09-25 (the wording "none is this is" is a typo in the original, quoted as written)

She rates her own reaction ("not surprising to me") against her actual job, not against a generic authority, which is what makes the claim checkable rather than performed.

> "When I started doing this, I didn't know almost anything about neural networks. Now that I've tricked them into thinking a panda is a vulture and seen how it's smarter at dealing with dogs than pandas, I understand them a tiny bit better. I won't say that I don't think what Google is doing is magic any more–I'm still pretty confused by neural nets."

Checked: https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture, retrieved 2026-09-25

The close names exactly what changed ("I understand them a tiny bit better") and exactly what didn't ("I'm still pretty confused"), instead of a tidy final verdict. Both halves are concrete enough to be wrong.

## How this piece should sound

This is a lesson on one paper, for a reader who already has word2vec and is about to meet BERT. Write it the way Olah motivates the LSTM cell state before naming a single gate: give the reader the plain need (a word's vector has to change with its sentence) before the machinery that met it (a two-layer biLSTM language model, its internal states pulled out and combined per task). State what ELMo's representation actually is in one clause, the way Karpathy states the RNN's API in one clause, before the sentence that complicates it.

The six-task result is where Karpathy's "quote detection cell" passage is the model to follow: state the finding, then the mechanism, then the number, in that order, and let "added on top of an existing task model" do the surprising work instead of a word like significant. Give the actual relative error reductions the paper reports for each task, not a description of how large they were.

The idea/machinery split is this lesson's whole spine, and the commission is explicit that it cannot be staged as a last-section reveal. Evans's close is the shape to take instead: name exactly what survived (context-dependent representations from a pretrained language model) and exactly what didn't (the frozen biLSTM, concatenated features) side by side, as two things that are true at once, not as a twist saved for the end. That split can be stated early and then shown working through the six tasks and into BERT's own paper.

Where the paper's own vocabulary carries a distinction (feature-based versus fine-tuned, frozen versus updated, forward and backward language models), use that vocabulary once it's defined, the way Olah keeps saying "cell state" instead of varying it. Alammar's "I had personally never came across the concept" move — placing the explainer at the reader's own starting point — has no first-person home in a lesson's body, but its instinct does: define the biLSTM and "language model" at the level the reader needs them and no further, then treat them as known for the rest of the piece; the LSTM lesson is a link, not a re-teach.

A joke or an aside is welcome exactly where Alammar's is: tied to the article's own nouns (the biLSTM, the six tasks, "bank" changing meaning between sentences), never a generic aside about AI or about the paper being a big deal. If nothing in the material earns one, the piece is better without it.
