# Voice guide: When AI Breaks — McDonald's AI drive-thru

## How this piece should sound

This lesson tells a chronological story about a specific machine before it explains the mechanism that broke it, so the opening moves should be Doug Seven's: state the concrete stakes in one plain declarative sentence, actors and figures named, before any throat-clearing. Seven opens "Knightmare" by saying flatly what happened and what it cost; this lesson can open its own narrative the same way, with the deployment, the reversal, and whatever figure anchors the scale of it, stated rather than teased.

Once the story reaches the mechanism, hold the domain's own vocabulary the way Gregory Travis holds "angle of attack" and "elevator feel computer": name the actual pieces of a voice order-taking pipeline — the part that turns sound into text, the part that turns text into an order, the part that decides when a human takes over — and define each once, in the sentence that needs it, then reuse the same name every time after. Don't reach for a softer synonym on the second mention; Travis never calls the angle-of-attack sensor anything else once he's named it.

The subject invites an easy joke at the drive-thru's expense, and the piece can afford one, but it should be built the way Luu builds the seatbelt line and Travis builds the pilot-and-dog line: out of this incident's own specific facts, not a generic crack about talking to a robot. A joke that would still work if you swapped in a different company's AI mishap is the one to cut.

Cause here has more than one place to land — the model, the reviewers who approved deploying it at this scale, the design of the fallback to a human — and Luu's reframe of "human error" as "process error" is the right instinct for sorting that out: look for the missing review step or the missing kill switch before landing on the one moment that happened to be visible. Seven's account of the Knight Capital deployment names the technician who skipped a server without ever making him the story's villain; the piece can extend the same discipline to whichever named person or team touched this deployment.

When the piece reaches the count of what went wrong — how many orders, how long the system ran before someone pulled it, what it cost to fix or replace — Seven's move of translating a large, unfamiliar figure into one the reader can hold ("in laymen's terms...") is worth having ready. So is Travis's habit of letting a bare fact close a paragraph with nothing added after it: once the sequence of causes is fully laid out, the last fact in that sequence can be left to stand on its own, the way "And 346 people are dead" is left to stand once everything before it has already explained why it happened.

None of the three exemplars below address a reader directly or step outside their own narrative — that discipline is exactly right for this lesson's body, which never mentions itself either. It breaks only at the two bookend cards, which speak to the reader by the lesson template's own design; nothing in these passages should be read as a model for how those two cards sound, since none of the three writers ever needed to write one.

## Gregory Travis, "How the Boeing 737 Max Disaster Looks to a Software Developer"

Source: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer

> "Long ago there was a joke that in the future planes would fly themselves, and the only thing in the cockpit would be a pilot and a dog. The pilot's job was to make the passengers comfortable that someone was up front. The dog's job was to bite the pilot if he tried to touch anything."

This lands a joke and then spends the rest of the piece cashing it in: a few paragraphs later, Travis writes that in a fight between the flight computer and the pilots, "the computer will bite humans until they give up and (literally) die." The joke becomes the explanation's vocabulary. That only works because the joke is built from this story's own object, an airplane that bites its pilot.

> "The airplane manufacturers said, “Sounds good to us.” The FAA said, “And say hi to Joe, we miss him.”"

Travis has just explained that the FAA, unable to afford enough of its own engineers, deputized manufacturer employees to certify their own company's designs. He stages the arrangement as two lines of dialogue and lets the reader hear how casual it was, with no sentence added afterward to say what to make of it. The judgment sits entirely in the staging.

> "In the 737 Max case, the rules were also followed. The rules said you couldn't have a large pitch-up on power change and that an employee of the manufacturer, a DER, could sign off on whatever you came up with to prevent a pitch change on power change. The rules didn't say that the DER couldn't take the business considerations into the decision-making process. And 346 people are dead."

This comes after two full sections of technical setup: the engine placement, the sensor design, the certification process. By the time the sentence about the dead arrives, nothing needs to be added to it — the paragraphs before it already did the work of explaining why the rule that let this happen was still, technically, a rule being followed. The plain fact is left to close the paragraph with nothing after it.

## Dan Luu, "Reading postmortems"

Source: https://danluu.com/postmortem-lessons/

> "There's a sense in which this is obvious -- error handling is generally regarded as being hard. If I mention this to people they'll tell me how obvious it is that a disproportionate number of serious postmortems come out of bad error handling and cascading failures where errors are repeatedly not handled correctly. But despite this being “obvious”, it's not so obvious that sufficient test and static analysis effort are devoted to making sure that error handling works."

Luu names the exact gap he's writing about: everyone agrees the lesson is obvious, and almost no one acts on it. Putting “obvious” in quotation marks the second time he uses it is the whole argument in miniature — it marks the word as something people say rather than something they do anything about.

> "I can understand why -- it's often hard to set up a good QA environment that mirrors prod well enough that config changes can get tested, and like driving without a seatbelt, nothing bad happens the vast majority of the time. If I had to make my own seatbelt before driving my car, I might not drive with a seatbelt either. Then again, if driving without a seatbelt were as scary as making config changes, I might consider it."

The seatbelt comparison does real explanatory work — it's why companies keep skipping a safeguard that seems obviously necessary in hindsight — and then Luu turns it over once more for a dry laugh at the end, without ever letting the joke replace the explanation.

> "But humans are even more error prone than machines. Don't get me wrong, I like humans. Some of my best friends are human. But if you repeatedly put a human in a position where they can cause a catastrophic failure, you'll eventually get a catastrophe."

Luu opens this section by renaming "human error" as "process error," and this is the sentence that earns the rename: the joke ("some of my best friends are human") clears space for the actual claim, which is that blaming the person misses where the fix belongs.

## Doug Seven, "Knightmare: A DevOps Cautionary Tale"

Source: https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/

> "This is the story of how a company with nearly $400 million in assets went bankrupt in 45-minutes because of a failed deployment."

One sentence, and the reader already has the stakes, the timeframe, and the cause. Everything about the company's business and the trading system it built follows this sentence; its only job is to earn that setup.

> "When the Power Peg flag on the eighth server was activated the Power Peg functionality began routing child orders for execution, but wasn't tracking the amount of shares against the parent order – somewhat like an endless loop. Imagine what would happen if you had a system capable of sending automated, high-speed orders into the market without any tracking to see if enough orders had been executed. Yes, it was that bad."

The technical explanation comes first, in full, using the system's own terms (Power Peg, parent order, child orders) without translation. The dry aside only arrives once the reader has enough to feel the size of the problem for themselves, once the explanation has already done its work.

> "In the first 45-minutes the market was open the Power Peg code received and processed 212 parent orders. As a result SMARS sent millions of child orders into the market resulting in 4 million transactions against 154 stocks for more than 397 million shares. [...] In laymen's terms, Knight Capital Group realized a $460 million loss in 45-minutes. Remember, Knight only has $365 million in cash and equivalents."

Seven gives the exact figures a trading-systems reader would want, then immediately regrounds them for everyone else by putting the loss next to the number that makes it a bankruptcy: what the company actually had in the bank. Both figures stay in the sentence; neither one is asked to stand in for the other.
