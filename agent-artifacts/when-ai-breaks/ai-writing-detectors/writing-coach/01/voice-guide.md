# Voice guide: when-ai-breaks/ai-writing-detectors (01)

## How this piece should sound

This lesson tells one thing that happened. Schools ran AI writing detectors over student submissions, the detectors called real students' own writing machine-generated, and students were accused on that basis. Some of those students wrote in plainer or less native English, and the lesson has to handle that unfairness precisely. Write the incident the way ProPublica narrates a person's record in the Borden and Prater passage: set what the detector reported and what the student actually wrote next to each other, in order, and leave the mismatch there without an adjective telling the reader it was unjust. The unfairness is legible from the facts of a flagged essay and a real author, and a sentence added to spell it out would weaken it. Where an accused student's own account is on the record, the Rivelli passage shows the handling. Give the person's words and the plain surrounding facts, and do not tell the reader what the quote proves.

The detectors were sold with a claimed false-positive rate, and independent testers reported a different one. Two passages carry a dispute like that. ProPublica's appeal passage states the case for the tool plainly before weighing it, which is what the vendor's side is owed here: say what the detector was built to do and why a school would want it, in those terms, before the independent findings arrive. Luu's config passage shows the other half. He gives a figure he can stand behind and, in the same sentence, the limit on it, so a contested number is reported without being oversold. When the record does not settle whose rate is right, Luu's human-error passage shows how to leave it open honestly: state the strongest version of each account, then say plainly what evidence would decide it.

Then the lesson has to explain why a detector flags human writing at all, for a reader who is new to it. Willison's email passage is the model for that explanation. He sets one concrete case first, then states the cause in a single plain sentence the reader can carry. The cause here is statistical, so name the specific mechanism and ground it in a real flagged passage instead of a general description of what machine-like text is supposed to look like. Willison's calibration passage sets the register for the close, where the same detectors are still sold and used to make consequential calls: say what they decide for real students in plain terms and let that carry the weight, without lifting it into a warning. Someone who finishes should be able to explain to another person why a plain human sentence can read as machine-written to a detector.

## Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

> "Yet something odd happened when Borden and Prater were booked into jail: A computer program spat out a score predicting the likelihood of each committing a future crime. Borden — who is black — was rated a high risk. Prater — who is white — was rated a low risk.
>
> Two years later, we know the computer algorithm got it exactly backward. Borden has not been charged with any new crimes. Prater is serving an eight-year prison term for subsequently breaking into a warehouse and stealing thousands of dollars' worth of electronics."

The authors put two records side by side, state the score each person got, and then state what each person did afterward, with no word telling the reader how to feel about it. The contrast is clear because the facts are placed in order and left alone. Angwin and her co-authors are visible in that restraint: the words "black" and "white" sit in plain apposition, and the outcome is reported without being named unjust.

> "The appeal of risk scores is obvious: The United States locks up far more people than any other country, a disproportionate number of them black. For more than two centuries, the key decisions in the legal process, from pretrial release to sentencing to parole, have been in the hands of human beings guided by their instincts and personal biases.
>
> If computers could accurately predict which defendants were likely to commit new crimes, the criminal justice system could be fairer and more selective about who is incarcerated and for how long. The trick, of course, is to make sure the computer gets it right."

Before criticizing the tool, the writers give the strongest version of the case for it: why the scores appeal, and what they could do if they worked. The paragraph is fair to the other side first, and only then adds the plain sentence about getting it right. The authors are visible in the choice to be accurate about the tool's promise before they are critical of it.

> "James Rivelli, a 54-year old Hollywood, Florida, man, was arrested two years ago for shoplifting seven boxes of Crest Whitestrips from a CVS drugstore. Despite a criminal record that included aggravated assault, multiple thefts and felony drug trafficking, the Northpointe algorithm classified him as being at a low risk of reoffending.
>
> "I am surprised it is so low," Rivelli said when told by a reporter he had been rated a 3 out of a possible 10. "I spent five years in state prison in Massachusetts. But I guess they don't count that here in Broward County.""

The passage gives the man his own words when he hears his score, including the flat aside about the record not following him. The writers do not gloss the quote or say what it demonstrates; they place it against the plain facts of his history and move on. The care is in letting a person sound like himself, in his own flat phrasing.

## Dan Luu, "Reading postmortems"

Source: https://danluu.com/postmortem-lessons/

> "Configuration bugs, not code bugs, are the most common cause I've seen of really bad outages. When I looked at publicly available postmortems, searching for "global outage postmortem" returned about 50% outages caused by configuration changes. Publicly available postmortems aren't a representative sample of all outages, but a random sampling of postmortem databases also reveals that config changes are responsible for a disproportionate fraction of extremely bad outages."

Luu gives the figure he found and then, in the same passage, says what the figure cannot support, because the sample is not representative. He keeps the count and its limit together, so the number stays usable without being pushed further than the data goes. The habit of qualifying his own evidence is where Luu is visible on the page.

> "My guess is that's because companies are less likely to write up public postmortems when the root cause was human error enabled by risky manual procedures. A prima facie plausible alternate reason is that improved technology actually increases the fraction of problems caused by humans, which is true in some industries, like flying. I suspect that's not the case here due to the sheer number of manual operations done at a lot of companies, but there's no way to tell for sure without getting access to the postmortem databases at multiple companies."

Luu states his own explanation, then builds the best version of a competing explanation, then says plainly that he cannot settle the question without data he does not have. His reasoning is shown, and his uncertainty stays marked as uncertainty. He is visible in stating a guess as a guess and naming the rival as plausible without choosing between them.

## Simon Willison, "Prompt injection: What's the worst that can happen?"

Source: https://simonwillison.net/2023/Apr/14/worst-that-can-happen/

> "Since this system works by reading and summarizing emails, what would it do if someone sent the following text in an email? … Classic prompt injection: in the default case, there's nothing to stop the assistant from following additional instructions that are concatenated into their prompt from the content of an email message."

Willison sets up a concrete situation, an assistant that reads someone's email, asks what a crafted message would do, and then names the cause in one plain sentence: the system cannot tell instructions apart from the content it is reading. He explains the mechanism by showing it happen: the concrete case does the work a definition would. He is visible in the plain "in the default case, there's nothing to stop" phrasing, which claims exactly as much as he can support.

> "For some applications, it doesn't really matter. My translation app above? Not a lot of harm was done by getting it to talk like a pirate.
>
> If your LLM application only shows its output to the person sending it text, it's not a crisis if they deliberately trick it into doing something weird."

Willison declines to inflate the danger. He names the cases where the flaw does no real harm before he reaches the cases where it does, and he does it in ordinary words. The calibration is the writing here: he is visible in the willingness to say out loud that some versions of the problem do not matter.
