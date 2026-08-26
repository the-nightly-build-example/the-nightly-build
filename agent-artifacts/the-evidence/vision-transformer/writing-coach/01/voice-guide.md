# Voice guide: the Vision Transformer paper (the-evidence)

## How this piece should sound

This lesson reads one paper about the Vision Transformer for a reader who is fluent and widely read but has never trained a model or opened the paper. Several of the words the paper leans on already live in that reader's head with a looser, everyday meaning: attention, transformer, even image. Yong's passage on the word *immunity* is the model for what to do there. When a term of art and its everyday cousin part ways, stop on the word and say plainly how the technical meaning differs, before the loose one carries the reader somewhere the paper did not go.

This piece has to keep two things apart: what the paper measured, and what people now say it showed. Dan Luu's practice with numbers is the register for the first of those. When you give a figure the paper reports, say what was measured to get it and where the measurement is soft, the way Luu defines his latency from the start of key movement to the USB packet and then rounds the numbers to avoid a false sense of precision. When a result in the paper rests on a particular scale of data or compute, give that scale as a figure the reader can hold, and where the paper hedges its own claim, hedge with it. A reader should finish able to say how large a foundation sits under the headline result.

For the distance between what was proved and how it gets cited, Yong's cross-reactive T-cells passage and Potter's exception are the closest guides. When a common way of citing this paper runs past what its evidence supports, say so with the flatness Yong uses on the T-cells that "might do nothing": name what the result does establish, then what it does not, inflating neither. Where a finding holds only under some condition, name the condition the way Potter names the twenty years his trend reverses. Where a claim in circulation is a fair reading of the paper, say that too. The work is to report the gap honestly, whichever direction it runs.

Reach for the worked case whenever an idea is easy to get wrong. Potter's nails and Yong's Rube Goldberg picture both put something concrete where an abstract statement would have sat, and this subject carries a few ideas that will land as a worked example and stay vague as a generalization: why cutting an image into fixed patches is a real design choice, or what it would even mean for the amount of training data to change how a model behaves. The house voice is plain and unhurried. The confidence to say a hard thing simply, and to state plainly what is still unsettled, is what these writers share, and it is what this lesson should take from them.

## Ed Yong, "Immunology Is Where Intuition Goes to Die"

Source: https://www.theatlantic.com/science/archive/2020/08/covid-19-immunity-is-the-pandemics-central-mystery/614956/

> "Arguably the most complex part of the human body outside the brain, it's an absurdly intricate network of cells and molecules that protect us from dangerous viruses and other microbes. These components summon, amplify, rile, calm, and transform one another: Picture a thousand Rube Goldberg machines, some of which are aggressively smashing things to pieces. Now imagine that their components are labeled with what looks like a string of highly secure passwords: CD8+, IL-1β, IFN-γ."

He hands the reader a picture they can hold, then shows the intimidating notation the picture stands in for, so the jargon arrives already tamed. The run of verbs (summon, amplify, rile, calm, and transform) does real work, telling you the parts act on each other before any part is named. You can see a writer who decided the reader's confusion was his problem to fix.

> "Even the word immunity creates confusion. When immunologists use it, they simply mean that the immune system has responded to a pathogen—for example, by producing antibodies or mustering defensive cells. When everyone else uses the term, they mean (and hope) that they are protected from infection—that they are immune. But, annoyingly, an immune response doesn't necessarily provide immunity in this colloquial sense."

He separates the technical sense of a word from the everyday one and names the gap between them plainly, down to the word "annoyingly." This is a teacher who knows which word will trip the reader and stops to fix it before going on. The honest point, that a response does not guarantee protection, is delivered without drama, as a fact the reader needs.

> "But Farber cautions that having these cross-reactive T-cells 'tells you absolutely nothing about protection.' It's intuitive to think they would be protective, but immunology is where intuition goes to die. The T-cells might do nothing. There's an outside chance that they could predispose people to more severe disease. We can't know for sure without recruiting lots of volunteers, checking their T-cell levels, and following them over a long period of time to see who gets infected—and how badly."

He reports what a finding does not tell you as carefully as what it does, and lists the plain reasons it could mean nothing. "The T-cells might do nothing" refuses to inflate a result people wanted to be exciting. The person visible here would rather state what is unknown than let the reader carry off more certainty than the evidence supports.

## Dan Luu, "Keyboard latency"

Source: https://danluu.com/keyboard-latency/

> "I never trust feelings like this because there's decades of research showing that users often have feelings that are the literal opposite of reality, so got a high-speed camera and started measuring actual keypress-to-screen-update latency as well as mouse-move-to-screen-update latency."

He states his own hunch and then explains why he distrusts it, citing that people's impressions can run opposite to what is measured, so he went and measured. The voice is flat and first-person, and the skepticism is aimed at himself first. You see someone who treats an unverified claim, his own included, as probably wrong until a measurement settles it.

> "The latency measurements are the time from when the key starts moving to the time when the USB packet associated with the key makes it out onto the USB bus. Numbers are rounded to the nearest 5 ms in order to avoid giving a false sense of precision."

He defines exactly what the metric is before he reports it, then rounds the figures on purpose so the reader will not read precision that is not there. Giving the definition of the measurement is what lets a reader check the claim against it. The person visible would rather report a coarse honest number than a sharp misleading one.

> "I don't actually trust this setup and I'd like to build a completely automated setup before testing more keyboards. While the measurements are in line with the one other keyboard measurement I could find online, this setup has an inherent imprecision that's probably in the 1ms to 10ms range."

He states the limits of his own rig, gives the size of the error in real units, and says what he would build to do better. Putting the weakness of the method next to the result lets the reader weigh both. This is a writer who reports the size of his own uncertainty rather than hiding it.

## Brian Potter, "Construction Costs Rarely Fall"

Source: https://www.construction-physics.com/p/construction-costs-rarely-fall

> "All else being equal, I prefer output indexes to input indexes, because they should more closely track what we actually care about (the cost of finished buildings), and should be less subject to distortion."

He makes a methodological call in the first person and attaches the reason a reader could weigh, naming in the parentheses the thing the measure is meant to track. The judgment is his, and he stands behind it without overclaiming for it. You see a writer willing to choose between imperfect tools and show the reader why he chose.

> "We see that in almost every period of time, construction costs are rising faster than overall inflation for virtually every cost index. The major exception is the period from 1975 to 1995, where most indexes show lower rates of increase or even declines against overall inflation."

He gives the general finding and in the same breath names the stretch of years that breaks it, with the direction of the exception stated. Naming the counterexample yourself is how a broad claim earns trust. The person visible reaches for the exception rather than waiting for a reader to catch it.

> "In the 19th century, nails got cheaper due to the introduction of new nailmaking processes - replacing hand-made nails with the cut nail process, and then the wire-nail process. If we looked only at improvements in hand-made nails, we might conclude that nails on the market hadn't gotten any cheaper, even though what actually happened was that an older process had simply been replaced by a newer, better process."

He teaches a subtle measurement trap with one concrete case: track only the old kind of nail and you miss that a cheaper process replaced it. The example is specific, cut nails and then wire nails, and it does the explaining that a bare statement of the problem could not. This is a writer who reaches for the worked case when a point is easy to get wrong.
