# Voice guide: the-evidence/constitutional-ai

## How this piece should sound

This lesson explains a two-stage training method to a reader who has never
trained a model and cannot check the claim for themselves. The register that
serves that reader is Lee's: state the mechanism, then show it happening to a
specific thing, in the order the reader needs to follow it. When Lee introduces
"compounding errors," he doesn't leave the term to do its own work — he defines
it in the same breath ("the more mistakes they make, the more likely they are
to make additional mistakes... (Machine learning experts say that these
situations are 'out of distribution.')") and moves on. Do the same with AI
feedback, preference model, and RLAIF: define each once, in the sentence that
introduces it, and never again. A reader who has to hold three undefined terms
through a paragraph about a two-model pipeline has already lost the pipeline.

Piper's move for making a training stage legible is to stop describing it and
instead produce the actual artifact: she doesn't say a base model is
unpredictable, she runs one and quotes what it actually output. This lesson has
the same option and should take it. Quote a real principle from the
constitution verbatim, not a paraphrase of what a constitution is like — the
paper's own sentence is short enough to show in full, and showing it is more
convincing than describing it as "a set of principles." The same move applies
to the critique-and-revise step: if the paper gives an example of a harmful
answer being critiqued and revised, that concrete before-and-after belongs in
the lesson more than a summary of the step ever could.

Lee also shows how to reach for an analogy without losing precision: the
classroom passage ("teachers demonstrate math problems on the board... the
teacher gives students feedback by grading their answers") maps imitation and
reinforcement onto something the reader has already lived through, and it does
this without claiming the analogy is the mechanism. This lesson's two stages —
learn from AI-written revisions, then learn from AI-made preference
comparisons — can use one comparison like that if one earns its place, but the
comparison should illustrate the shape of the two stages, not stand in for what
the paper actually measured.

For the scale section, follow Willison's habit with numbers: give the actual
figure, and when the figure means nothing to a reader on its own, anchor it to
something they can already picture, the way he turns a training-cost figure
into "a single digit number of fully loaded passenger flights from New York to
London." Model sizes, the count of crowdworker comparisons, an Elo score — pick
the ones the reader has no way to scale unassisted and give them a comparison
from outside machine learning to hold instead. And when a number is being used
to sound impressive rather than to inform — Willison catches this in his own
copy, noting that a headline-ready cost figure "make[s] for a great
attention-grabbing headline" before he gives the real one — this lesson's
required honesty about scale (one lab's models, evaluated mostly by preference
comparison) can take the same shape: name the impressive-sounding version of
the claim, then give the reader the number that actually supports it.

The lesson's present-day section is where Piper's other habit matters: she
never argues against a vague "some people think," she names the exact claim
("large language models... 'do not, cannot, and will not understand anything at
all'") and then shows what it gets wrong. When this lesson takes up today's
loose talk about a model "having a constitution," it should do the same —
name what that phrase is doing in an argument, then show the mechanical
distance between that and what the 2022 paper actually built.

## Timothy B. Lee, "Reinforcement learning, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/reinforcement-learning-explained

> "Ross wanted to help develop better techniques for training robots on tasks like these (he's now working on self-driving cars at Waymo), but it's not easy to experiment in such high-stakes domains. So Ross started with an easier problem: training a neural network to master SuperTuxKart, an open-source video game similar to Mario Kart."

Lee opens a technical explanation with a specific person doing a specific,
smaller thing, before the general lesson arrives. The reader gets a concrete
scene — a named researcher, a video game, a stated reason for choosing the
easier problem — to hang the abstraction on, rather than being told up front
that "researchers study imitation learning."

> "The broader lesson, Ross and Bagnell argued, was that imitation learning systems can suffer from 'compounding errors': the more mistakes they make, the more likely they are to make additional mistakes, since mistakes put them into situations that aren't well represented by their training data. (Machine learning experts say that these situations are 'out of distribution.') As a result, a model's behavior tends to get more and more erratic over time."

The term arrives already defined. Lee states the plain mechanism first — more
mistakes make more mistakes likely — and only then attaches the field's own
word to it, in a parenthetical that a reader can skip without losing the
sentence. Nothing here asks the reader to already know what "out of
distribution" means.

> "In school, teachers demonstrate math problems on the board and invite students to follow along (imitation). Then the teacher asks the student to work some problems on their own. The teacher gives students feedback by grading their answers (reinforcement)."

The analogy is built from something almost every reader has lived through, and
it stays disciplined: each clause maps to one piece of the mechanism (imitation,
then reinforcement), labeled in parentheses rather than left for the reader to
infer.

## Kelsey Piper, "When 'technically true' becomes 'actually misleading'"

Source: https://www.theargumentmag.com/p/when-technically-true-becomes-actually

> "I happen to have an LLM at this stage of training — the GPT-2 'base' model — installed on my computer. If I ask it 'who was the president in 1880,' it continues the sentence with the following text: 'who was the president in 1880 and the first president ever to resign under fire in his final year as president) was elected to Congress in 1887.' That's a pure text-predictor for you."

Piper doesn't describe what an untrained-for-instructions model does. She runs
one and quotes the actual, slightly deranged output, then names what it shows
in one short sentence. The claim is checkable because she showed her work
instead of characterizing it.

> "For example, if I say to GPT-2-base 'who was the president in 1880 answer in iambic pentameter' it continues 'after this question). It took some time for this question to be answered, though. [...] This is an 1881 letter from Mrs. C. H. Taylor to her sister-in-law Hildreth S. Linnemann.' That is, it interprets the instruction 'answer in iambic pentameter' as part of the text that it's continuing, and so spins up a probable continuation for that string of text."

Same move, applied to the next stage of training: rather than asserting that an
un-instruction-tuned model can't follow instructions, she gives it an
instruction and quotes exactly how it fails to follow it, then states plainly
what the failure means.

> "If all LLMs are doing — all they inherently could do — is spit out the likeliest next token, why can they also spit out the unlikeliest? The right answer is that, of course, these are, in a sense, very similar tasks, and anything good at one will be good at another. But now we have obviously moved toward thinking of next-token prediction as a capacity the LLM has that it can deploy, including deploying it backward, rather than what the LLM is."

After two demonstrations, she reasons in the open: she poses the question the
reader is probably already asking, answers it in one plain sentence, and then
states the larger point it supports. Nothing here is asserted before it's
earned by the examples just given.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/

> "Here's a fun napkin calculation: how much would it cost to generate short descriptions of every one of the 68,000 photos in my personal photo library using Google's Gemini 1.5 Flash 8B (released in October), their cheapest model? [...] That's a total cost of $1.68 to process 68,000 images. That's so absurdly cheap I had to run the numbers three times to confirm I got it right."

Willison turns an abstract efficiency claim into an arithmetic problem with a
real input (his own photo library) and a checkable answer, then admits his own
surprise at the result instead of asserting the number is impressive.

> "For less efficient models I find it useful to compare their energy usage to commercial flights. The largest Llama 3 model cost about the same as a single digit number of fully loaded passenger flights from New York to London. That's certainly not nothing, but once trained that model can be used by millions of people at no extra training cost."

A training-cost figure with no intuitive size on its own gets anchored to
something the reader has actually experienced — a transatlantic flight — and
the sentence immediately qualifies the comparison rather than letting it stand
as the whole verdict.

> "Not quite, but almost! It does make for a great attention-grabbing headline. The big news to end the year was the release of DeepSeek v3 — dropped on Hugging Face on Christmas Day without so much as a README file, then followed by documentation and a paper the day after that."

Willison names the version of the claim built to sound impressive before
giving the reader the real figure behind it, catching the same move in his own
subject that a skeptical reader would want caught.
