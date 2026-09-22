# Voice guide: when-ai-breaks/iruda-chatbot

## How this piece should sound

This lesson tells one incident and then explains why that kind of system fails
that way. Iruda launched in December 2020, emitted slurs under ordinary use and
leaked real people's messages, and was shut down in about three weeks; in April
2021 the PIPC fined Scatter Lab. The reader is smart and reads widely and has
never been inside a model. They keep meeting claims about AI they cannot check,
and this is the check for this one. The register is a person who understands the
subject explaining it to be understood: plain claims, exact words, one word per
idea. The story is upsetting, so keep the sentences level and let the facts carry
the weight, the way the postmortems below stay exact even while their authors say
they are ashamed.

Iruda invites a one-line version: the chatbot said terrible things. Where the
record supports more than that line, lay out the sequence the line skips, as
Graham-Cumming names "a regular expression went bad" and then says the real
account is the chain of events. Two things happened, the slurs and the leaked
KakaoTalk messages, and the regulator moved on one of them. The piece can show
that shape without a flourish.

Give the reader the dates and the figures as plain facts inside ordinary
sentences, in the order things happened, not as a summary handed down from above.
Krebs opens on "40 million" and the breach dates; Graham-Cumming has a colleague
say "we had lost 80% of our traffic" in the moment. Name Scatter Lab, the "Science
of Love" (연애의 과학) apps the training messages came from, the PIPC, and the fine,
and put the exact number where a document owns it. The message-count, user-count
and fine figures reach us through retellings that disagree, so where accounts
differ, say which document owns the figure and what the looser versions got wrong,
the way Luu says why the loudest version of an incident is usually the wrong one.
Where a figure cannot be pinned to a document, say that.

Carry each claim down to one instance before it becomes a count. Before "it leaked
personal data," show the kind of string it returned, a name or an address; before
"hundreds of thousands of users," the persona, a 20-year-old woman on Facebook
Messenger. Luu shows one user whose name reverted before he shows the tens of
tickets; Krebs names the Pennsylvania heating firm and the stolen credentials
rather than "hackers got in." Start from the ordinary act that produced the harm,
a user chatting, reaching the machine's behavior, as Luu sets a band's press
conference beside a twenty-minute outage.

The reader needs two mechanisms taught here: that a model trained on real chat
logs can memorize and repeat private strings, and that a model tuned only for
fluent, human-like replies has no filter on the toxicity in the text it learned
from. Define each in plain words at first use, and where an analogy makes it land
use one, as Travis explains angle of attack with a hand out a car window. Link the
library's memorization and toxicity lessons rather than teaching them from the
ground.

Scatter Lab said its users had agreed through the apps' terms. State that account
in the company's own words before showing why the PIPC did not accept it. Where
the record does not reach a cause, say so, and say what evidence would settle it.

## John Graham-Cumming, "Details of the Cloudflare outage on July 2, 2019"

Source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/

> "Although the regular expression itself is of interest to many people (and is discussed more below), the real story of how the Cloudflare service went down for 27 minutes is much more complex than “a regular expression went bad”. We’ve taken the time to write out the series of events that led to the outage and kept us from responding quickly."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-09-22
He names the simple cause everyone will latch onto and then says why it is not the
whole account, and commits to the sequence instead. The figure, 27 minutes, sits
inside an ordinary sentence rather than in a headline. Graham-Cumming is visible
as the engineer who would rather walk you through the chain than hand you the
one-liner.

> "Some of these alerts hit my watch and I jumped out of the meeting I was in and was on my way back to my desk when a leader in our Solutions Engineering group told me we had lost 80% of our traffic. I ran over to SRE where the team was debugging the situation. In the initial moments of the outage there was speculation it was an attack of some type we’d never seen before."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-09-22
The account moves in the order he lived it, and the figure, 80%, is delivered by a
named colleague in the moment rather than stated from above. He reports what the
team believed at the time, that it might be an attack, without pretending they
already knew the cause. The writer is in the sentences, leaving a meeting and
running to a desk, and the numbers stay exact.

> "So when things do go wrong, it’s generally the unlikely convergence of multiple causes. Getting to a single root cause, while satisfying, may obscure the reality."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/, retrieved 2026-09-22
He resists the single cause the reader wants and says plainly why one cause would
mislead, as a claim he then supports with the list of failures that follows. It is
a writer telling you the shape of the explanation before he gives it, without
dressing the turn up.

## Dan Luu and Yao Yue, "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "One reason is that outrageously exaggerated stories are more likely to go viral, so those are the ones that tend to be remembered. Another is that there's a cottage industry of former directors / VPs who tell self-aggrandizing stories about all the great things they did that, to put it mildly, frequently distort the truth (although there's nothing stopping ICs from doing this, the most spread false stories we see tend to come from people on the management track)."

Checked: https://danluu.com/cache-incidents/, retrieved 2026-09-22
Luu says why the widely repeated version of an incident is usually wrong and names
the mechanism, viral exaggeration and self-serving retellings, instead of
gesturing at it. The parenthetical corrects his own claim before a reader can,
which is where the care shows. "to put it mildly" carries a dry judgment without
raising the volume.

> "SMAP, a former Japanese boy band that became a popular adult J-pop group as well the hosts of a variety show that was frequently the #1 watched show in Japan, held a conference to falsely deny rumors they were going to break up. This resulted in an outage in one datacenter that impacted users routed to that datacenter for ~20 minutes, until that DC was failed away from."

Checked: https://danluu.com/cache-incidents/, retrieved 2026-09-22
The sentence begins with the real-world event that drove the traffic, a band's
press conference, and lands on the exact technical effect, one datacenter down for
about twenty minutes. Trigger and failure sit in the same breath, so the reader
sees how the outside world reached the machine. He states the human cause without
a joke at its expense and without inflating it.

> "On Nov 8, a user changed their name from [old name] to [new name]. One week later, their username reverted to [old name]. Between Nov 8th and early December, tens of these tickets were filed by support agents. Twitter didn't have the instrumentation to tell where things were going wrong, so the first two weeks of investigation was mostly getting metrics into the rails app to understand where the issue was coming from."

Checked: https://danluu.com/cache-incidents/, retrieved 2026-09-22
The failure is one user's account before it is a statistic, then the count and the
dates. Luu is honest that the first weeks went to building the ability to see the
problem at all, the unglamorous part most accounts skip. He keeps to what the
record shows and dates each step.

## Brian Krebs, "Inside Target Corp., Days After 2013 Breach"

Source: https://krebsonsecurity.com/2015/09/inside-target-corp-days-after-2013-breach/

> "In December 2013, just days after a data breach exposed 40 million customer debit and credit card accounts, Target Corp. hired security experts at Verizon to probe its networks for weaknesses. The results of that confidential investigation — until now never publicly revealed — confirm what pundits have long suspected: Once inside Target’s network, there was nothing to stop attackers from gaining direct and complete access to every single cash register in every Target store."

Checked: https://krebsonsecurity.com/2015/09/inside-target-corp-days-after-2013-breach/, retrieved 2026-09-22
Krebs opens with the dates and the figure and then states the finding in plain
words: once inside, nothing stopped the attackers from reaching every register.
The aside, "until now never publicly revealed," tells the reader what is new
without claiming importance for it. He commits to the conclusion the document
supports rather than hedging it.

> "In February 2014, KrebsOnSecurity was the first to report that investigators had zeroed in on the source of the breach: Fazio Mechanical, a small heating and air conditioning firm in Pennsylvania that worked with Target and had suffered its own breach via malware delivered in an email. In that intrusion, the thieves managed to steal the virtual private network credentials that Fazio’s technicians used to remotely connect to Target’s network."

Checked: https://krebsonsecurity.com/2015/09/inside-target-corp-days-after-2013-breach/, retrieved 2026-09-22
He traces the break-in to a named third party, a Pennsylvania heating and
air-conditioning firm, and to the exact thing stolen, the VPN credentials its
technicians used. Naming the small vendor and the stolen credential turns "hackers
got in" into a chain a reader can follow. He also says who first reported it, so
the provenance of the claim is on the page.

> "From what I heard in off-the-record conversations, Target has a good story to tell in how it’s handling security threats these days. Unfortunately, the company has declined my request for the access needed to let me tell that story."

Checked: https://krebsonsecurity.com/2015/09/inside-target-corp-days-after-2013-breach/, retrieved 2026-09-22
Krebs reports the impression he formed in person and then states plainly what he
cannot tell, because the company denied him access. He keeps the off-the-record
impression apart from what he can stand behind. The reporter is visible, and so is
the edge of what the reporting reached.

## Gregory Travis, "How the Boeing 737 Max Disaster Looks to a Software Developer" (IEEE Spectrum)

Source: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer

> "The angle of attack is the angle between the wings and the airflow over the wings. Think of sticking your hand out of a car window on the highway. If your hand is level, you have a low angle of attack; if your hand is pitched up, you have a high angle of attack. When the angle of attack is great enough, the wing enters what’s called an aerodynamic stall. You can feel the same thing with your hand out the window: As you rotate your hand, your arm wants to move up like a wing more and more until you stall your hand, at which point your arm wants to flop down on the car door."

Checked: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer, retrieved 2026-09-22
Travis defines a term the lay reader needs, angle of attack, with a hand out a car
window, and the analogy does the whole job without a diagram. He introduces it
before he uses it and carries it to a physical thing the reader has felt. The
teacher is visible in the choice to let the reader feel the stall rather than be
told about it. Elsewhere the piece runs sharper, angrier asides; what transfers
here is the plain teaching in this passage.

> "Let’s review what the MCAS does: It pushes the nose of the plane down when the system thinks the plane might exceed its angle-of-attack limits; it does so to avoid an aerodynamic stall. Boeing put MCAS into the 737 Max because the larger engines and their placement make a stall more likely in a 737 Max than in previous 737 models."

Checked: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer, retrieved 2026-09-22
He says what the system does in one plain sentence and then why the company added
it, the larger engines making a stall more likely. Cause and purpose come
together, so the reader understands the design decision and not just the part. He
names the specific system and the specific reason instead of reaching for the
general.
