# Voice guide: when-ai-breaks/nyc-mycity-chatbot

## How this piece should sound

The lesson tells a deployed failure most readers know as headline but not as sequence: New York City put a chatbot on its own website as its answer for people running a business, and the chatbot answered questions of law with sentences that were plainly wrong. Open the way Somers opens on the Washington State 911 outage or Angwin opens on two teenagers riding a stolen Huffy — with the concrete event, named actors, and specifics the reader can hold. The Markup's investigation has the reproduced prompts and the city's response, and the MyCity page has the disclaimer under which those answers were served. Work from that record.

Teach the mechanism at the level of the object. Somers stays with the Intrado counter and the threshold set to a number in the millions; Tkacik stays with the engines mounted forward of the wings and what that did to the plane's aerodynamics. The paper has already taught hallucination and retrieval-augmented generation, so link those articles rather than reteach them, and spend the room on what is specific to this incident: a retrieval-plus-generation system deployed as an official answer, and a disclaimer telling the user to check with an official source while the city itself was the one publishing the answer.

Attribute every claim to a named human or a named document. Tkacik puts Peter Lemme's own line on record; Angwin quotes Northpointe's letter and Brennan's testimony; Somers cites Nancy Leveson with her chair and her book. The record for this incident includes The Markup's investigation, city statements, follow-up reporting from AP, WNYC, The Verge, and Ars Technica, and the MyCity site itself. Give the specific law each answer contradicted, the reporter who reproduced the prompt, the date, and the official who responded on the record. The reader is smart and reads widely, so name the housing-voucher rule, the tip-pooling statute, and the retaliation provision rather than referring to "workplace protections" or "housing law."

Sentences run short and specific where the material lets them. When Somers writes "They picked a number in the millions," the earlier paragraph is inside it. Where an ordinary explainer would offer a verdict on Boeing or on Northpointe, Tkacik and Angwin give the exact number, quote, or document instead, and leave the verdict to the takeaway. The body of this lesson does the same. The takeaway bookend names what the lesson found; the body does not double it with its own summary sentence.

## Maureen Tkacik, "Crash Course: How Boeing's Managerial Revolution Created the 737 MAX Disaster"

Source: https://newrepublic.com/article/154944/boeing-737-max-investigation-indonesia-lion-air-ethiopian-airlines-managerial-revolution

> Nearly two decades before Boeing's MCAS system crashed two of the plane-maker's brand-new 737 MAX jets, Stan Sorscher knew his company's increasingly toxic mode of operating would create a disaster of some kind. A long and proud "safety culture" was rapidly being replaced, he argued, with "a culture of financial bullshit, a culture of groupthink."

Tkacik opens by naming the one person whose warning frames the story, dates the warning against him ("nearly two decades before"), and lets him speak in the sentence he is introduced in. Tkacik does not put her own vocabulary on the page here — the two phrases inside the quotation marks are Sorscher's own words, and the sentences around them report rather than assess.

> This alteration created a shift in the plane's center of gravity pronounced enough that it raised a red flag when the MAX was still just a model plane about the size of an eagle, running tests in a wind tunnel. The model kept botching certain extreme maneuvers, because the plane's new aerodynamic profile was dragging its tail down and causing its nose to pitch up. So the engineers devised a software fix called MCAS, which pushed the nose down in response to an obscure set of circumstances in conjunction with the "speed trim system," which Boeing had devised in the 1980s to smooth takeoffs.

The paragraph teaches a physical mechanism in three sentences: what the change did to the plane, what the wind-tunnel model showed, and what software Boeing wrote in response. Each sentence explains the next without a technical term the reader has not already been shown. "This alteration" refers to a redesign the previous paragraph names — mounting the new, larger engines forward of the wings — and the paragraph sits inside a longer chronological account.

## James Somers, "The Coming Software Apocalypse"

Source: https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

> There were six hours during the night of April 10, 2014, when the entire population of Washington State had no 911 service. People who called for help got a busy signal. One Seattle woman dialed 911 at least 37 times while a stranger was trying to break into her house. When he finally crawled into her living room through a window, she picked up a kitchen knife. The man fled.

Somers opens on the concrete facts of the failure: the state, the date, the number of hours, the count of 37 calls, the man at the window, the knife. Nothing in the paragraph gestures at the argument to come. The reader is placed inside the outage before it is analyzed.

> The 911 outage, at the time the largest ever reported, was traced to software running on a server in Englewood, Colorado. Operated by a systems provider named Intrado, the server kept a running counter of how many calls it had routed to 911 dispatchers around the country. Intrado programmers had set a threshold for how high the counter could go. They picked a number in the millions.

The mechanism arrives with the object at the center — a server in Englewood, a counter, a threshold — and lands the cause in a short, plain final sentence. Somers is a programmer himself, and the vocabulary he keeps ("counter," "threshold") is what a practitioner would use.

## Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

> On a spring afternoon in 2014, Brisha Borden was running late to pick up her god-sister from school when she spotted an unlocked kid's blue Huffy bicycle and a silver Razor scooter. Borden and a friend grabbed the bike and scooter and tried to ride them down the street in the Fort Lauderdale suburb of Coral Springs.

The opening is a specific person doing a specific thing before any of the reporting arrives. Every detail is a specific one — a name, an age (introduced a sentence later), a Florida town, a Huffy and a Razor identified by brand. The sentence carries no adjective on top of the specifics.

> Northpointe's core product is a set of scores derived from 137 questions that are either answered by defendants or pulled from criminal records. Race is not one of the questions. The survey asks defendants such things as: "Was one of your parents ever sent to jail or prison?" "How many of your friends/acquaintances are taking drugs illegally?" and "How often did you get in fights while at school?" The questionnaire also asks people to agree or disagree with statements such as "A hungry person has a right to steal" and "If people make me angry or lose my temper, I can be dangerous."

The mechanism appears as the mechanism itself: the number of questions on Northpointe's survey, and four of the actual questions the survey asks. The reader learns what the algorithm looks at by reading what the algorithm asks about.
