# Voice guide: the-mechanics/counting-objects-in-images

## How this piece should sound

This lesson takes a failure everyone who has typed a number into an image generator has already seen and walks downhill from it until nothing is left to explain. Take the move Bartosz Ciechanowski makes over and over in "GPS": state what the current, simpler account of the pipeline gets right, say exactly what it still can't do, then add only the one part that closes that specific gap. His path from trilateration to pseudoranges to the fourth satellite works because each new piece, whether a term or a mechanism, arrives only once the reader has already felt the gap it fills. The pipeline here has the same shape: an encoder that registers "apple" but not "six," a diffusion process that spreads that embedding across a canvas instead of placing counted objects, and no component anywhere that checks the result against the request. Each of those three can get the same treatment Ciechanowski gives trilateration: a real win, immediately followed by the specific reason it isn't the whole story, immediately followed by the next real part. That sequencing is what keeps three named components from reading as a parts list.

Introduce each term the way Simon Willison introduces an embedding in "Embeddings: What they are and why they matter": define it in the sentence that first uses it, out of words already on the page, and hand the reader something to picture rather than a formal definition. When this piece needs its own plain phrase for what the research literature calls compositional or bag-of-words behavior, Willison's habit with "vibes-based search" is the model: settle on one unpretentious phrase for it, then reuse that exact phrase everywhere it recurs rather than reaching for a synonym the second time.

The commission asks the piece to mark what's settled engineering against what's still open: how far better captioning, scaling, or added guidance methods actually close the counting gap. Julia Evans, in "What happens when you press a key in your terminal?", keeps pushing an explanation past the phenomenon everyone already knows (a process gets killed) down to an actual mechanism (a kernel receiving one byte and sending a signal), and she says plainly how sure she is of each claim along the way. This lesson's body can't use her first person, but the underlying move carries over: state the settled half as a settled claim, and give the open half its own sentence naming it as unresolved, rather than letting a hedge creep into the settled claim or false confidence into the open one.

Two decisions belong to this piece specifically, since no exemplar can supply them. hands-in-generated-images already spent "nothing in the pipeline counts" on fingers, so every worked example here can stay a count of separate, whole objects (apples, dogs, chairs) and never drift toward a body part, which is the surest way this piece would end up sounding like a rerun. And one example count can carry all three steps rather than a fresh example per step: pick a number early and let the reader watch that same request fail at the encoder, fail again through cross-attention, and land wherever the training data made likely, instead of introducing a new scenario at each stage.

## Bartosz Ciechanowski, "GPS"

Source: https://ciechanow.ski/gps/

> "The process of calculating a location of a point using measurement of distances is called trilateration – that procedure lies at the heart of a GPS receiver. However, being tied to two or three measuring tapes is certainly not how any GPS device functions, so let's keep on making our primitive positioning system better."

He names the real technique the toy version just demonstrated, trilateration, then immediately says why the toy version can't be the answer. Nothing about the sentence oversells the small win before moving past it. The next problem is already lined up in the same breath.

> "Because of that unknown time bias we're no longer calculating the true time of flight and therefore we're not measuring the true range. Instead, we calculate a so-called pseudorange. The length of a pseudorange depends on what we assume the bias to be."

A new technical term, pseudorange, gets defined in the sentence that introduces it, using only words the piece has already earned (time bias, range). He doesn't stop to elaborate past that one sentence before moving on.

> "Fortunately, we can solve this problem by flipping it on its head. Instead of the users sending audio signals to the landmarks, we'll have the landmarks emit the sounds and have the users listen to those sounds."

He names the specific failure of the current design in the sentence just before this, then states the fix as a literal inversion of the same nouns: senders and listeners swap roles. "Fortunately" is earned here, not decorative, because a genuine dead end was just described.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "Embeddings are based around one trick: take a piece of content—in this case a blog entry—and turn that piece of content into an array of floating point numbers. The key thing about that array is that it will always be the same length, no matter how long the content is. The length is defined by the embedding model you are using—an array might be 300, or 1,000, or 1,536 numbers long. The best way to think about this array of numbers is to imagine it as co-ordinates in a very weird multi-dimensional space."

Four short moves build the abstraction: name the trick, say what stays constant, give the actual range of numbers, then hand the reader a picture to hold. He never asks the reader to accept the term "embedding" before showing what one is made of.

> "What's interesting about this is that it's not guaranteed that the term "backups" appeared directly in the text of those READMEs. The content is semantically similar to that phrase, but might not be an exact textual match. We can call this semantic search. I like to think of it as vibes-based search. The vibes of those READMEs relate to our search term, according to this weird multi-dimensional space representation of the meaning of words."

He coins one plain, slightly funny name for the phenomenon he just showed working, then uses that exact name again in the very next sentence instead of a more technical-sounding synonym. His voice shows in choosing the unpretentious word and then treating it as seriously as any other term in the piece.

> "The key idea is this: a user asks a question. You search your private documents for content that appears relevant to the question, then paste excerpts of that content into the LLM (respecting its size limit, usually between 3,000 and 6,000 words) along with the original question."

One sentence carries the actor, the action, and the constraint together, with the caveat folded into a parenthetical rather than given its own hedging sentence. He gets to the mechanism without a run-up.

## Julia Evans, "What happens when you press a key in your terminal?"

Source: https://jvns.ca/blog/2022/07/20/pseudoterminals/

> "Echoing: The client sends l and then immediately receives an l sent back. I guess the idea here is that the client is really dumb – it doesn't know that when I type an l, I want an l to be echoed back to the screen. It has to be told explicitly by the server process to display it."

She reports what she observed, then states in plain words what that observation implies about the design, and marks the implication as her own inference ("I guess") rather than dressing it up as an established fact.

> "I believe the reason cat gets interrupted when we press Ctrl+C is that the Linux kernel on the server side receives this \x03 character, recognizes that it means "interrupt", and then sends a SIGINT to the process that owns the pseudoterminal's process group. So it's handled in the kernel and not in userspace."

The explanation doesn't stop at the phenomenon everyone already knows: a running program gets killed. It keeps going until it names an actual mechanism, a specific byte reaching a specific piece of the kernel. She also says how confident she is in that account, so the reader can tell the verified part from her best guess.

> "There's definitely a lot more to know about terminals (we could talk more about colours, or raw vs cooked mode, or unicode support, or the Linux pseudoterminal interface) but I'll stop here because it's 10pm, this is getting kind of long, and I think my brain cannot handle more new information about terminals today."

She ends by naming a plain, human-scale reason to stop rather than a summarizing line that claims the subject is closed. The close is honest about being a limit of the post, not a verdict on the topic.
