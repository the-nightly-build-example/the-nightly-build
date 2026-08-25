# Voice guide: the-evidence/clip (01)

## How this piece should sound

This lesson's whole job is the move Brian Resnick makes in the marshmallow-test
piece below: put what a paper's authors actually wrote next to what people now
say it proved, and let the gap do the work. For CLIP, that means quoting or
citing the 2021 paper's own language for what it measured. Name the datasets,
the accuracy numbers, the specific claim about "zero-shot" transfer, before the
piece turns to how "zero-shot" gets invoked today. Resnick's move is to go back
to Mischel's own 1990 paper and show it hedging where the culture that grew up
around it did not. The CLIP lesson has the same primary document to return to,
and OpenAI's own qualifications of the result are worth as much digging as the
result itself.

Teach the mechanism the way Timothy B. Lee and Sean Trott do: a plain worked
example before the abstract claim, using real numbers rather than a gesture at
scale. Their Washington-DC-coordinates bit earns the abstraction that follows
because the reader can check it themselves. CLIP's "zero-shot" claim wants the
same treatment. Give a specific test set, a specific accuracy figure, maybe one
concrete image-caption pair, before the lesson tries to explain what zero-shot
transfer means in general.

Lee and Trott are also the model for saying plainly what a result does not
establish, in the same declarative register as the rest of the sentence, with
no apology and no hedge-word doing the work instead of a fact. "We are still far
from having a comprehensive explanation for why GPT-2 decided to predict Mary"
sits right next to a description of real, published research, stated as a fact
rather than tacked on as a disclaimer. When this lesson reaches the edge of what
the CLIP paper actually showed, that boundary should read the same way: stated
plainly, in a full sentence that carries its own weight.

Scott Alexander takes a claim made at the scale of an entire field and shows
exactly how much smaller the real evidence is. That is the shape for handling
whatever overclaim about CLIP or "zero-shot" learning the piece finds itself
correcting. The correction names the specific thing that is true (his "most
centrally the sub-sub-field of social priming research") instead of only
asserting that the big claim is wrong. If this lesson finds a similar overclaim
about what CLIP's zero-shot result means for general AI capability, the fix is
the same: say what part of it holds, precisely.

The declared reader is smart, widely read, and has never opened a codebase, so
technical vocabulary (zero-shot, contrastive pretraining, whatever CLIP's paper
calls its own method) gets defined in plain words at first use and then used
exactly that way for the rest of the piece, the way Lee and Trott hold "word
vector" steady once they've built it. At 1200 to 2200 words there is room for
the paper's own numbers, one or two worked examples, and the present-day
contrast, but not for re-explaining any of the three at length once each is
taught. This lesson has room to teach a short list completely, not a long one
in passing.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "As a result, no one on Earth fully understands the inner workings of LLMs. Researchers are working to gain a better understanding, but this is a slow process that will take years—perhaps decades—to complete."

This sits three paragraphs into the piece, right after explaining that ChatGPT is built on a trained neural network rather than programmed instructions. It states a hard limit on what is known as flatly as it states anything else in the piece: no throat-clearing, no "unfortunately." The writers are visible in the choice to put this early, before the reader has any reason to doubt they can explain the subject. It is a decision to earn trust by naming the boundary first.

> "This is useful for reasoning about spatial relationships. You can tell New York is close to Washington DC because 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close to London. But Paris is far from Washington DC."

Before this passage, the piece has just given the coordinates for four cities. The abstraction that follows, that a word vector places related words near each other in a space with hundreds of dimensions, arrives only after this concrete, checkable example, built from numbers the reader was just shown. Nothing here is asserted that the prior two sentences didn't hand the reader the means to verify.

> "We love this example because it illustrates just how difficult it will be to fully understand LLMs. The five-member Redwood team published a 25-page paper explaining how they identified and validated these attention heads. Yet even after they did all that work, we are still far from having a comprehensive explanation for why GPT-2 decided to predict Mary as the next word."

This comes after several paragraphs walking through a specific, real research result: the Redwood Research team's attention-head analysis of GPT-2. Having just shown the reader exactly what the paper established, the writers state exactly what it didn't, in the same voice. The size of the paper (25 pages, five authors) is given as a fact about the scale of the effort, not as an appeal to authority. It is followed immediately by naming the limit of what that effort bought.

## Brian Resnick, "The 'marshmallow test' said patience was a key to success. A new replication tells us s'more."

Source: https://www.vox.com/science-and-health/2018/6/6/17413000/marshmallow-test-replication-mischel-psychology

> "In fairness to Mischel and his colleagues, their findings, as written in 1990, were not so sweeping. In the study linking delay of gratification to SAT scores, the researchers acknowledged the possibility that with a bigger sample size, the magnitude of their correlation could decrease. They also mentioned that the stability of the home environment may play a more important role than their test was designed to reveal. It also wasn't an experiment. The results also didn't necessarily mean that teaching kids to delay their gratification would cause these benefits later on."

This is the piece's central move, and it comes right after describing how the marshmallow test became famous. Resnick goes back to the original 1990 paper and reports what it actually hedged, line by line: the sample size caveat, the home-environment caveat, the fact that it wasn't an experiment. Each sentence is a separate, checkable claim about the document itself, not a generalization about "the research." The gap between this paragraph and the one before it, where the test "rocketed" to fame, is the whole argument. Resnick never has to state the argument, because the gap makes it.

> "That means 'if you have two kids who have the same background environment, they get the same kind of parenting, they are the same ethnicity, same gender, they have a similar home environment, they have similar early cognitive ability,' Watts says. 'Then if one of them is able to delay gratification, and the other one isn't, does that matter? Our study says, "Eh, probably not."'"

Resnick lets the replication's lead author state the finding in his own words, including the shrug of "Eh, probably not," a piece of plain speech from a working scientist that a paraphrase would have smoothed away. Quoting it exactly, informality included, is what makes the finding sound like something a person concluded rather than something a press release announced.

> "But if the recent history of social science has taught us anything, it's that experiments that find quick, easy, and optimistic findings about improving people's lives tend to fail under scrutiny. Harder work remains. Studies that find exciting correlations need to be followed up with long-term experimental research. This research is expensive and hard to conduct. But without rigorous studies, we're going to remain prone to research hype."

Near the piece's end, after several sections of specific findings about this one replication, Resnick allows himself one sentence of general pattern, and earns it by keeping it tied to the specific mechanism just described: correlational findings needing long-term experimental follow-up, rather than a moral floating free of the case. The short declaratives that follow keep the generalization tied down.

## Scott Alexander, "Psychology Research Is Mostly Fine"

Source: https://www.astralcodexten.com/p/psychology-research-is-mostly-fine

> "This misunderstands the extent of the problem. The replication crisis primarily affected the sub-field of social psychology, and most centrally the sub-sub-field of social priming research - the study of how seemingly trivial interventions can have outsized effects on behavior."

This follows two examples of people generalizing psychology's replication crisis to the whole field. Rather than arguing the generalization is wrong in the abstract, Alexander immediately narrows it to a named sub-field and then a named sub-sub-field, defining the second in the same sentence. The correction is built from nouns: a named sub-field, a named sub-sub-field, a one-sentence definition. It replaces a vague target with a precise, smaller one the reader can now picture.

> "I take some of the blame for this - not because I was involved in the original experiment, but because I was fascinated by it and gave out this grant to double-check it. Since I'm not a professor of cognitive psychology and don't usually follow the field, I only came across this because it was a crazy result hyped by the media which overturned everything normal people believe (you can learn things twice as fast just by changing your screen flicker? really?!) And of course crazy widely-hyped results like these are far more likely to fall apart than normal incremental expansion of settled science."

Alexander is explaining why he funded a replication of a specific EEG-learning study. He states plainly why the original claim caught his attention: it was hyped, not that it was well-supported. Then he states the general mechanism that follows from that fact, that hyped results fail more often than unglamorous incremental ones. The parenthetical aside registers his own reaction in the moment without pretending it was more than that.

> "If you don't like social priming, say that you don't like social priming, and leave the rest of the field alone."

The piece's closing line restates its whole argument in a single sentence built entirely from the piece's own terms. "Social priming" is the specific thing named three paragraphs earlier, not a stand-in for "bad research" in general. It closes by handing the reader the corrected, narrower claim to use in place of the broad one it opened by rejecting.
