# Voice guide: the origin of attention

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "Within a few dozen minutes of training my first baby model (with rather arbitrarily-chosen hyperparameters) started to generate very nice looking descriptions of images that were on the edge of making sense. Sometimes the ratio of how simple your model is to the quality of the results you get out of it blows past your expectations, and this was one of those times."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-26

The enthusiasm is pinned to a specific, checkable detail — a few dozen minutes, one baby model, arbitrary hyperparameters — instead of a bare adjective like "amazing." He also undercuts himself in the same breath ("on the edge of making sense"), so the claim survives its own qualifier.

> "So how do these things work? At the core, RNNs have a deceptively simple API: They accept an input vector `x` and give you an output vector `y`. However, crucially this output vector's contents are influenced not only by the input you just fed in, but also on the entire history of inputs you've fed in in the past."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-26

He asks the exact question a reader is holding, then answers it in the next sentence with the mechanism, not a restatement. "API" is the precise word for what he means and he doesn't trade it for a softer one.

> "My favorite fun dataset is the concatenation of Paul Graham's essays. The basic idea is that there's a lot of wisdom in these essays, but unfortunately Paul Graham is a relatively slow generator. Wouldn't it be great if we could sample startup wisdom on demand? That's where an RNN comes in."

Checked: https://karpathy.github.io/2015/05/21/rnn-effectiveness/, retrieved 2026-09-26

The joke depends entirely on the real person and the real project — swap either out and it stops working. He states the setup plainly and lets the joke carry itself instead of flagging it as one.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don't throw everything away and start thinking from scratch again. Your thoughts have persistence."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-26

He opens on a claim about the reader's own mind, not on the network, and states it in four short declarative sentences that each add one step. The pivot to the technical subject only happens in the next paragraph, after the claim is already established on its own.

> "Traditional neural networks can't do this, and it seems like a major shortcoming. For example, imagine you want to classify what kind of event is happening at every point in a movie. It's unclear how a traditional neural network could use its reasoning about previous events in the film to inform later ones."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-26

The abstract shortcoming ("a major shortcoming") is immediately made concrete with one instance — classifying events in a movie — so the reader can check the claim against a case instead of taking it on faith.

> "The key to LSTMs is the cell state, the horizontal line running through the top of the diagram. The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged."

Checked: https://colah.github.io/posts/2015-08-Understanding-LSTMs/, retrieved 2026-09-26

He names the thing and locates it in the picture ("the horizontal line running through the top of the diagram") before he describes what it does, so a reader looking at the diagram and the sentence land on the same object. The conveyor-belt image is used once and then dropped for a plain mechanical claim about linear interactions, rather than repeated for color.

## Jay Alammar, "The Illustrated Word2vec"

Source: https://jalammar.github.io/illustrated-word2vec/

> "On a scale of 0 to 100, how introverted/extraverted are you (where 0 is the most introverted, and 100 is the most extraverted)? Have you ever taken a personality test like MBTI – or even better, the Big Five Personality Traits test?"

Checked: https://jalammar.github.io/illustrated-word2vec/, retrieved 2026-09-26

He grounds an abstraction (a number representing a trait) in a test many readers have actually taken, and gives the scale as bare numbers instead of a vaguer "some people are more introverted than others."

> "We can now say that this vector partially represents my personality. The usefulness of such representation comes when you want to compare two other people to me. Say I get hit by a bus and I need to be replaced by someone with a similar personality. In the following figure, which of the two people is more similar to me?"

Checked: https://jalammar.github.io/illustrated-word2vec/, retrieved 2026-09-26

The joke ("hit by a bus") is dropped in without ceremony and the very next sentence goes straight back to the technical question the figure is asking. Nothing marks the joke as a joke; it just sits inside the explanation.

> "If one wanted to give an example of an NLP application, one of the best examples would be the next-word prediction feature of a smartphone keyboard. It's a feature that billions of people use hundreds of times every day."

Checked: https://jalammar.github.io/illustrated-word2vec/, retrieved 2026-09-26

He reaches for the most familiar instance of the abstract task instead of naming the task in the abstract, then backs the claim with a figure a reader can hold (billions of people, hundreds of times a day) instead of calling it important.

## Julia Evans, "Behind 'Hello World' on Linux"

Source: https://jvns.ca/blog/2023/08/03/behind--hello-world/

> "But behind the scenes, there's a lot more going on. I'll describe some of what happens, and (much much more importantly!) explain some tools you can use to see what's going on behind the scenes yourself. We'll use `readelf`, `strace`, `ldd`, `debugfs`, `/proc`, `ltrace`, `dd`, and `stat`."

Checked: https://jvns.ca/blog/2023/08/03/behind--hello-world/, retrieved 2026-09-26

She names every tool she is about to use before using any of them, so nothing arrives as a surprise later in the piece. The parenthetical marks her own priority in her own voice without dressing it up as a general truth.

> "Now you might be wondering - Julia, what is `stat` doing? Well, when your OS opens a file, it's split into 2 steps. It maps the filename to an inode, which contains metadata about the file. It uses the inode to get the file's contents."

Checked: https://jvns.ca/blog/2023/08/03/behind--hello-world/, retrieved 2026-09-26

She addresses herself by name to voice the question a reader is probably holding, then answers it in two numbered steps of roughly equal size. The device puts the confusion on the page instead of writing around it.

> "Hopefully you have a better idea of how `hello world` gets printed! I'm going to stop adding more details for now because this is already pretty long, but obviously there's more to say and I might add more if folks chip in with extra details."

Checked: https://jvns.ca/blog/2023/08/03/behind--hello-world/, retrieved 2026-09-26

The closer states plainly what was covered and admits directly what's left out, with no summary of lessons learned and no claim about why any of it matters.

## How this piece should sound

This lesson explains one paper: what encoder, decoder, alignment, and context vector meant before this piece existed, and what the paper actually changed about how a machine translates a sentence. The register these five writers share is a flat confidence about hard material — they state what a thing is or does in one sentence, using the field's own word for it, and only reach for an image when the image does work the plain sentence couldn't. None of them announce that they are about to explain something, and none of them close by telling the reader what they now know.

Where the paper names a part — the encoder, the decoder, the alignment weights, the context vector — that part can get the Olah treatment: say what it is, and if a picture or a diagram is doing work elsewhere in the piece, locate the part in it in the same sentence, before describing what it does. A part described only by its behavior, floating free of where it sits, is harder to hold onto than one that's been pointed to first.

Where a number belongs — how long a sentence has to get before the older approach struggled, how large the training set was, how a score is read — the number can stand on its own, the way Alammar gives a scale from 0 to 100 and Evans gives billions of uses a day, rather than being translated into "small" or "significant."

The paper's own worked example — a long sentence translated badly by the older method and correctly by this one — is exactly the kind of case Karpathy and Alammar reach for: report what the model actually produced, including where it still fails, and let the specific case carry the claim instead of a verdict about how impressive it is.

A technical question a smart, non-practitioner reader would be stuck on at some point — why the older encoder-decoder setup struggles with long sentences, or what the alignment weights are actually doing — can be asked directly and answered in the same breath, the way Olah writes "But can they? It depends" and Evans writes "you might be wondering — Julia, what is X doing?" This is one way to keep the piece moving through its hardest turn without performing suspense about it.

The opening can commit to a real, checkable claim about how sentence-by-sentence translation worked before this paper, the way Olah opens on a claim about human cognition and Karpathy opens on his own result, rather than opening on what the reader has or hasn't encountered before. The close can end on what the paper found and, if the reporting supports it, what has held up or given way since — stated plainly, the way Evans's closer names exactly what's covered and exactly what isn't — rather than a gesture at the idea's importance.
