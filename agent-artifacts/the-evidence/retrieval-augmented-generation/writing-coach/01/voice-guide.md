## How this piece should sound

This lesson reads the 2020 Lewis et al. paper that named RAG, and reports honestly on the gap between what the paper measured and what "RAG" now names in the off-the-shelf retriever-plus-LLM stacks that inherit the term. The reader is smart and widely read and encounters the name from products, not from the paper.

Timothy Lee's opening move is available. He starts on the shorthand about LLMs the reader has probably already heard ("predict the next word"), and says out loud that the usual explanation stops there. The equivalent starting point exists for this piece: the reader knows "RAG" from a product, not the 2020 method. Lee's other habit worth taking is anchoring every number the reader cannot scale on their own to a comparison they already hold. When the lesson gives the paper's Wikipedia-dump size, the parametric baseline it beat, or its open-domain QA numbers on NQ or TriviaQA, name the reference point beside them.

Sebastian Raschka is useful for two habits. He defines a contested term in his own words and follows the definition with the smallest example that fixes it, rather than paraphrasing a paper's own definition. The paper's terms of art (dense passage retriever, jointly trained seq2seq generator, fixed Wikipedia dump) deserve that first move. He also separates what a technical report actually claims from what he is guessing about a product whose methods are not disclosed, and marks which is which. The distinction between the paper's jointly trained system and today's inference-time pipelines that carry its name is exactly that separation.

Simon Willison holds one discipline the third teaching beat needs. When he weighs a paper against practice around what it studies, he stays with specifics the paper measured, such as the mechanic ("bulleted lists and answers of a very specific length") that would explain the drift, rather than describing the drift in the abstract. When the lesson reports later work qualifying the retriever-plus-LLM pipeline (long-context comparisons, retrieval failure modes, grounding studies), give the specific measurement each study made. The press bans hype and doom on both sides. Report the numbers the paper measured and the numbers the later studies measured, and skip the adjectives about vindication or correction.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "If you know anything about this subject, you've probably heard that LLMs are trained to 'predict the next word,' and that they require huge amounts of text to do this. But that tends to be where the explanation stops. The details of how they predict the next word is often treated as a deep mystery."

Lee names the shorthand the reader has probably already heard about LLMs, and then says where the usual explanation runs out, before starting his own. He uses first person and his name sits on the byline; the voice belongs to a specific person from the first sentence.

> "For example, the most powerful version of GPT-3 uses word vectors with 12,288 dimensions—that is, each word is represented by a list of 12,288 numbers. That's 20 times larger than Google's 2013 word2vec scheme. You can think of all those extra dimensions as a kind of 'scratch space' that GPT-3 can use to write notes to itself about the context of each word."

Lee gives the exact figure, sets it against a number the reader might have already heard about from 2013, and then says in plain words what the extra dimensions are used for. He does not let a large number stand without a comparison the reader can hold.

> "GPT-1 and GPT-2 flunked this test. But the first version of GPT-3, released in 2020, got it right almost 40 percent of the time—a level of performance Kosinski compares to a three-year-old. The latest version of GPT-3, released last November, improved this to around 90 percent—on par with a seven-year-old. GPT-4 answered about 95 percent of theory-of-mind questions correctly."

Lee reports each model's score in turn, and pairs each score with a human comparison from the researcher who ran the test. The comparisons come from the paper he is citing, not from Lee reaching for a metaphor of his own.

## Sebastian Raschka, "Understanding Reasoning LLMs"

Source: https://magazine.sebastianraschka.com/p/understanding-reasoning-llms

> "In this article, I define 'reasoning' as the process of answering questions that require complex, multi-step generation with intermediate steps. For example, factual question-answering like 'What is the capital of France?' does not involve reasoning. In contrast, a question like 'If a train is moving at 60 mph and travels for 3 hours, how far does it go?' requires some simple reasoning."

Raschka writes the definition for this piece rather than lifting one from a paper, and follows it with the smallest example that shows what the definition includes and what it excludes. The definition and the example are held together as one move.

> "Note: The exact workings of o1 and o3 remain unknown outside of OpenAI. However, they are rumored to leverage a combination of both inference and training techniques."

Raschka names what is not known about a specific product and separates it from what he is guessing about it. The hedge is on the record, in the same voice as the rest of the piece.

> "One particularly interesting approach I came across last year is described in the paper O1 Replication Journey: A Strategic Progress Report – Part 1. Despite its title, the paper does not actually replicate o1. Instead, it introduces an different way to improve the distillation (pure SFT) process."

Raschka names the paper, notes that its title claims more than the paper does, and then says what the paper does instead. The correction is stated before anything else he takes from the paper.

## Simon Willison, "Understanding the recent criticism of the Chatbot Arena"

Source: https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/

> "The Chatbot Arena has become the go-to place for vibes-based evaluation of LLMs over the past two years. The project, originating at UC Berkeley, is home to a large community of model enthusiasts who submit prompts to two randomly selected anonymous models and pick their favorite response. This produces an Elo score leaderboard of the 'best' models, similar to how chess rankings work."

Willison introduces the object of the paper for a reader who may not know it, and gives the specific mechanic in one sentence: two anonymous models, a user picking a favorite, Elo scoring. The register is chatty ("vibes-based evaluation") and precise at the same time.

> "If proprietary model vendors can submit dozens of test models, and then selectively pick the ones that score highest it is not surprising that they end up hogging the top of the charts!
>
> This feels like a classic example of gaming a leaderboard. There are model characteristics that resonate with evaluators there that may not directly relate to the quality of the underlying model. For example, bulleted lists and answers of a very specific length tend to do better."

Willison spells out what the paper's finding would produce if left alone, and hands the reader a specific mechanic that would explain the drift: bullet points, and answers of a specific length. He does not describe the gaming in the abstract.

> "I'm dissapointed by this response, because it skips over the point from the paper that I find most interesting. If commercial vendors are able to submit dozens of models to the arena and then cherry-pick for publication just the model that gets the highest score, quietly retracting the others with their scores unpublished, that means the arena is very actively incentivizing models to game the system. It's also obscuring a valuable signal to help the community understand how well those vendors are doing at building useful models."

Willison names a specific counterparty and says what its response failed to address. He argues with a claim that is on the record, not with the state of the field in general.
