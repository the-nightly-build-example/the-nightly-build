# Voice guide: Chicago's Strategic Subject List

## How this piece should sound

The reader is smart and widely read and has never worked inside a system like the Strategic Subject List. Write for that reader: plain claims, one idea at a time, the stakes made concrete. The lesson tells what the heat list did to real people, in order and with names and dates, and then teaches why a scoring system built to predict involvement in gun violence fails the way this one did. Hold every judgment to the record, let the evidence carry the weight, and save any grand word for after the argument earns it.

The narration can open the way Julia Angwin and her co-authors open "Machine Bias," on a named person met as an ordinary event before any score is attached, built from small checkable facts: a date, a place, a figure, a specific object. A concrete case is what keeps the program from staying abstract. When a term the reader does not hold arrives, the risk score, the tier a person was placed on, whatever the Chicago Police Department called the number, it can be defined in the sentence where it first appears, as those authors define "risk assessments" the moment the word is used. The plain account of who was flagged and what officers did with the flag may carry the stakes on its own.

Before the story leans on a claim, the lesson can fix what the record actually supports, the way Dan Luu and Yao Yue say up front exactly what their count covers and concede that cache was only "at least partially" to blame. Where the SSL's role in an arrest or a police visit is partial or disputed, the sentence can say so instead of rounding it to a single cause. When the lesson reaches the mechanism, the failure can be set out as a chain the reader follows one step at a time, from the data the model scored to the police contact that followed, the way Luu walks a small delay into an outage. Shown this way, a cause does not need alarm placed around it.

Numbers do their work when they are exact and scaled to something the reader already holds: how many people were scored, how many sat on the highest tier, how the list was used. McKenzie earns his sharpest line only after a plain figure and a step of reasoning stand in front of it, and a verdict on the SSL is available on the same terms, once the reasoning is on the page. If the lesson's own point runs against what the reader expects about the system, it can be stated plainly and stood behind, the way McKenzie tells the reader a counterintuitive claim is true and then makes the case that it is.

## Dan Luu and Yao Yue, "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "This is a collection of information on severe (SEV-0 or SEV-1, the most severe incident classifications) incidents at Twitter that were at least partially attributed to cache from the time Twitter started using its current incident tracking JIRA (2012) to date (2022), with one bonus incident from before 2012. Not including the bonus incident, there were 6 SEV-0s and 6 SEV-1s that were at least partially attributed to cache in the incident tracker, along with 38 less severe incidents that aren't discussed in this post."

The writers begin by saying exactly what they counted and where the count came from: a severity label, a specific tracker, a date range, and the 38 incidents they set aside. "At least partially attributed to cache" concedes that cache was seldom the only cause, so the size of the claim is settled before any story is told. Luu is visible in the refusal to round, giving 6, 6, and 38 where another writer would put "several."

> "Increased cache latency along with the design of tweet service using cache caused shards of the service using cache to enter a GC death spiral (more latency -> more outstanding requests -> more GC pressure -> more load on the shard -> more latency), which then caused increased load on remaining shards."

The parenthetical lays the failure out as a chain, each step causing the next, so a reader can watch a small delay grow into an outage. Each step shows why the following one is worse, so the writers never have to call the result a disaster. Naming "the service using cache" twice, rather than reaching for a shorter synonym, is the same discipline that keeps the chain unambiguous.

> "For this and other incident analysis projects we've done, links to documents and tickets from the past few years tend to work (90%+ chance), but older links are less likely to work, with the rate getting pretty close to 0% by the time we're looking at things from 2012."

Before drawing on the record, the writers say how much of it survives, and they say it with a rate instead of a complaint. Admitting that the older evidence is mostly gone makes the claims built on the newer evidence easier to trust. Luu treats the condition of the sources as a reportable fact, like any other in the piece.

## Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

> "On a spring afternoon in 2014, Brisha Borden was running late to pick up her god-sister from school when she spotted an unlocked kid's blue Huffy bicycle and a silver Razor scooter. Borden and a friend grabbed the bike and scooter and tried to ride them down the street in the Fort Lauderdale suburb of Coral Springs. Just as the 18-year-old girls were realizing they were too big for the tiny conveyances — which belonged to a 6-year-old boy — a woman came running after them saying, "That's my kid's stuff." Borden and her friend immediately dropped the bike and scooter and walked away. But it was too late — a neighbor who witnessed the heist had already called the police. Borden and her friend were arrested and charged with burglary and petty theft for the items, which were valued at a total of $80."

A piece about an algorithm opens on a named person, a date, and a blue Huffy bicycle that was part of $80. Every detail is small and checkable, and the smallness is the point: the reader meets the case as a minor theft before the system's score of it arrives. The child's bike and the exact figure are how the authors keep the scene concrete.

> "Scores like this — known as risk assessments — are increasingly common in courtrooms across the nation. They are used to inform decisions about who can be set free at every stage of the criminal justice system, from assigning bond amounts — as is the case in Fort Lauderdale — to even more fundamental decisions about defendants' freedom."

The term "risk assessments" is defined the instant it appears, set inside the sentence rather than saved for later. The next sentence says plainly what the scores decide and names the bond in Fort Lauderdale, so the category has a real courtroom under it. The authors let the concrete use carry the stakes without a word like "grave."

> "We ran a statistical test that isolated the effect of race from criminal history and recidivism, as well as from defendants' age and gender."

The sentence states exactly what the test controlled for and names the other factors one by one, so a reader can see what it rules out and what it does not. It reports a method, not a result, which is what lets the result that follows be believed. The list is specific enough that a doubter knows where to press.

## Patrick McKenzie, "The optimal amount of fraud is non-zero"

Source: https://www.bitsaboutmoney.com/archive/optimal-amount-of-fraud/

> "This is counterintuitive and sounds like it is trying a bit too hard to be clever. You should believe it."

McKenzie names his claim's weakness first, that it sounds like showing off, and then tells the reader to accept it anyway. Two short sentences hold the whole stance: willing to be doubted, and unwilling to hedge. "You should believe it" is the writer standing behind the claim in the plainest words available.

> "The card issuer will, following the credit card brand's rules (which developed in symbiosis with regulation), automatically seek recovery of the loss from the business's payments processor. It will, similarly, automatically seek recovery of the loss from the business itself."

The passage moves the loss from one party to the next in the order it actually travels, so the reader learns the mechanism by following the money rather than by being handed a definition. "Automatically" appears twice on purpose, marking that no person decides this in the moment. McKenzie fits the history into a parenthesis, crediting the rules to regulation without stopping the sentence.

> "Consider businesses which sell IP, like video game companies, streaming services, or SaaS. Because their margins are often 90%+, if you were to present them with a menu of strategies which traded off conversion rate and fraud rate, they'd maximize for conversion rates until fraud at the margin reached levels not seen in even the most corrupt places imaginable."

The judgment is built on a figure the reader can hold, a 90% margin, and then reasoned to its end instead of asserted. The vivid close, fraud past the most corrupt places imaginable, has been paid for by the margin and the tradeoff that came before it. McKenzie reaches for the strong phrase only after the arithmetic is on the page.
