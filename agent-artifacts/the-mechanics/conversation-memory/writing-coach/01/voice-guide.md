# Voice guide: the-mechanics/conversation-memory (01)

## How this piece should sound

This lesson explains a behavior the reader has watched many times: a chatbot referring back to something they typed several messages earlier. Write it in the register Bartosz Ciechanowski holds in "Mechanical Watch," which is calm, concrete, one idea at a time, with no drama around the moment the explanation turns a corner. The reader is smart and has simply never looked under this particular hood. Julia Evans shows how to address that reader in her DNS piece: name the thing, give its reach in plain numbers, and get to the part they came for, as if talking to a friend who has not examined it yet. Follow her in showing the full detail rather than a simplified version of it, since this reader can carry the real thing.

The piece corrects an intuition the reader arrives with, that the model is holding the conversation in some kind of memory. Ciechanowski's line about how "one could naively think that we could just attach a watch hand to the barrel" is a model for stating the reader's first guess in their own voice and then letting it fail, with no mockery, before the mechanism arrives. Patel's "It only sees the graph" is the companion move: draw a hard line around what a system can and cannot know, name the specific things it does not carry, and say the boundary more than once so it holds. Where the correction comes, it may want stating plainly and only once, without a flourish added to sell it.

Much of the mechanism turns on quantities: how long the running transcript has grown, how much fits in the context window, how many earlier turns survive. Where a number decides the behavior, the arithmetic can happen in front of the reader the way Ciechanowski counts forty hours into 2,400 rotations before he names the gears that produce them, so the part is introduced only after its job is visible. When an abstract step like resending the transcript, or pasting stored facts into the prompt, threatens to float free of anything the reader can picture, it can be pinned to one small concrete exchange, the way Patel attaches the idea of a movement "cost" to Civilization's move-points with actual figures.

The everyday consequences the reader already knows are where the lesson pays off: a brand-new chat that starts blank, a long chat that loses its beginning, a product "memory" feature that seems to recognize them across sessions. Each can close by tying the mechanism back to the thing the reader has seen, the way Ciechanowski ends on a beat count by naming the smooth motion of the hand it produces. Where a product's trimming, summarizing, or retrieval is undocumented, Evans's stance in the DNS piece applies: show what is known and say plainly where the mechanism genuinely varies between products or is not published, rather than smoothing over the gap. Patel's habit of starting from input and output fits the order this piece needs, since what the application hands the model on each turn and what comes back are the reader's way in, before anything about what happens inside a single call.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "We’ve managed to make some parts rotate and one could naively think that we could just attach a watch hand to the barrel to make it track time. Unfortunately, that won’t really work – you can witness this in the demonstration below."

He states the reader's obvious first guess in the reader's own voice, then shows it failing before he explains the fix. "Naively" carries no mockery, so a reader who had exactly that thought is not made to feel foolish. The correction is the plain "Unfortunately, that won't really work," and Ciechanowski adds nothing dramatic on top of it.

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in."

He works the problem in numbers before he names a single part. By the time "gears" appears, the reader already knows the exact job the gears must do, because the 40 hours and the 2,400 rotations came first. Ciechanowski does the arithmetic out loud instead of asserting that some mechanism is required.

> "In this watch movement the balance wheel does a full back and forth swing four times per second, hitting the pallet fork twice during each cycle, for a total of 8 beats per second or 28,800 beats per hour. While different watches may have different rates, they all do a tiny turn of the second hand many times per second, which gives mechanical watches the illusion of a very smooth hand motion."

The passage ends by connecting the count back to the thing the reader can already see, the smooth sweep of the hand. He gives the rate two ways, per second and per hour, so the reader can keep whichever is easier to hold. The word "illusion" names the distance between what the eye reports and what the parts are actually doing.

## Amit Patel, "Introduction to the A* Algorithm" (Red Blob Games)

Source: https://www.redblobgames.com/pathfinding/a-star/introduction.html

> "The first thing to do when studying an algorithm is to understand the data. What is the input? What is the output?"

He starts from what goes in and what comes out, before any mechanism. The two short questions set the order the rest of the page follows. Patel makes his method visible on the surface of the sentence: understand the data first, then the steps that move it.

> "A* doesn’t see anything else. It only sees the graph. It doesn’t know whether something is indoors or outdoors, or if it’s a room or a doorway, or how big an area is. It only sees the graph! It doesn’t know the difference between this map and this other one."

He draws a hard line around what the system can and cannot know, and repeats "it only sees the graph" so the boundary stays put. The list of things it does not know, indoors, doorway, area, is concrete, which makes the limit something a reader can check rather than take on faith. This is the move of correcting a reader who credits a system with more awareness than it has.

> "So far we’ve made steps have the same “cost”. In some pathfinding scenarios there are different costs for different types of movement. For example in Civilization, moving through plains or desert might cost 1 move-point but moving through forest or hills might cost 5 move-points. In the map at the top of the page, walking through water cost 10 times as much as walking through grass."

The abstract idea of a movement "cost" arrives attached to a game the reader may know, with real figures: 1 against 5, water ten times grass. Patel reaches for the concrete case the moment the idea could drift loose of anything the reader can picture. He keeps the reader's own experience of the game in front of the definition.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "For example, take DNS. We’ve been using DNS since the 80s (for more than 35 years!). It’s used in every website on the internet. And it’s pretty stable – in a lot of ways, it works the exact same way it did 30 years ago."

She sets up a system the reader meets every day and gives its age and reach in plain numbers before she says anything hard about it. The sentences are short and carry one fact each. Evans writes as though talking to a smart friend who has simply not looked at this particular thing yet.

> "And it’s not “dumbed down” or anything! It’s the exact same information, just formatted in a more structured way. ... I want to see all the information! I just want it to be presented clearly."

She insists that making something clear and taking detail out of it are two different things. The stance is explicit and first person, and it shows how she treats a reader: everything stays on the page, and nothing is removed to make the explanation go down easier. Evans is most visible here, in the refusal to trade completeness for an easier read.
