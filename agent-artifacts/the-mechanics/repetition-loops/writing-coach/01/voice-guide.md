# Voice guide: the-mechanics/repetition-loops

## How this piece should sound

This lesson takes a behavior many readers have run into, a model repeating the same word, phrase, or sentence until it stops, and works down, one named part at a time, to what produces it. The reader is quick and widely read and has never opened the code. Write for that reader the way James Somers writes for a general audience in "The Coming Software Apocalypse": plain sentences, one real part per sentence, and the concrete thing named before any abstraction is asked of them.

Somers opens on the 911 outage in human terms and with exact figures before he names the counter or the threshold behind it. The loop can be shown the same way, as the thing on the page in its own particulars, before the descent begins, so the reader has watched the behavior happen before being asked to explain it. As the piece goes down from the decoding rule toward the training that shaped the model, Somers's habit is available at each step: name the one real part, add nothing but the next part, and leave the adjective off. He calls the threshold "a number in the millions" and lets the figure carry the weight. Where this lesson reaches a real quantity, the figure can do that work here too.

Some steps will be unfamiliar to the reader. Somers reaches for word processing before WYSIWYG to explain what it means to run a program in your head, and the parallel holds because it is exact. Where a step in this descent needs a handhold the reader already has, an exact everyday parallel is available. An inexact one misleads, so a step that has no exact parallel is clearer left plain.

The series asks the writer to mark which steps are settled engineering and which are still open. Dan Luu, in "Files are hard," marks that kind of boundary in flat sentences: he tells the reader plainly where his own account might be wrong, and the admission does not weaken the parts he is sure of. Where this lesson reaches the step that is genuinely unsettled, a plain statement of that, held to the same bar as the settled steps, is what the boundary calls for, not a hedge that makes the settled steps sound uncertain too.

The lesson also has fixes to give, each tied to the step it addresses. Luu, handed the fix most readers propose for his problem, pauses and walks through what it does and does not solve before moving on. Where this piece presents a remedy a reader might take as the whole answer, taking that obvious version seriously and showing precisely what it reaches and what it leaves to the steps below is available.

Trey Harris, in "The case of the 500-mile email," follows his chain to the speed of light and stops, at the step below which nothing about the network would change the answer. This lesson has a bottom too, whether it lands on a settled part of the system or on an open question, and it can end there in this behavior's own terms, without a closing line that reaches past what the descent found.

## James Somers, "The Coming Software Apocalypse"

Source: https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

> "There were six hours during the night of April 10, 2014, when the entire population of Washington State had no 911 service. People who called for help got a busy signal. One Seattle woman dialed 911 at least 37 times while a stranger was trying to break into her house."

Somers opens on the event in human terms, with exact figures, before he names any cause. The reader feels the behavior first. He is visible in the detail he keeps, the woman dialing 37 times, which he reports flatly and trusts to land on its own.

> "Operated by a systems provider named Intrado, the server kept a running counter of how many calls it had routed to 911 dispatchers around the country. Intrado programmers had set a threshold for how high the counter could go. They picked a number in the millions."

He traces a national outage down through named parts: a counter, a threshold, a number someone chose. Each sentence adds one real part and no assessment. Somers is visible in the restraint of "a number in the millions," which states the figure and lets the reader feel the absurdity instead of being told it is absurd.

> It used to be that all you could see in a program for writing documents was the text itself, and to change the layout or font or margins, you had to write special "control codes," or commands that would tell the computer that, for instance, "this part of the text should be in italics." The trouble was that you couldn't see the effect of those codes until you printed the document. It was hard to predict what you were going to get. You had to imagine how the codes were going to be interpreted by the computer—that is, you had to play computer in your head.

He explains an abstract idea, running a program in your head, by mapping it onto something the reader has already done: formatting a document before WYSIWYG, when you wrote a control code and could not see its effect until you printed. The parallel is exact, and that exactness is what makes it teach. He is visible in choosing a homely example over a technical one.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "I haven't used a desktop email client in years. None of them could handle the volume of email I get without at least occasionally corrupting my mailbox. Pine, Eudora, and outlook have all corrupted my inbox, forcing me to restore from backup."

The piece starts from a nuisance the writer actually lived, named concretely down to the three clients and the restored backup, and then turns it into the question the piece answers. Luu is visible in the plainness: no build-up, just what happened and why it is strange.

> "I think this is understandable, given how much misinformation is out there. Not being a filesystem dev myself, I'd be a bit surprised if I don't have at least one bug in this post."

Luu states the limit of his own certainty in one flat sentence, and it does not undercut the rest of the piece. He is visible as the writer who has read the papers and still tells you where he might be wrong, which is part of why the confident passages read as earned.

> "In fact, that's probably the most common comment I've gotten on this post. If you think this solves the problem, I'm going to ask you to pause for five seconds and consider the problems this might have."

Readers had proposed a simpler fix, copying the file to a temp file and renaming it over the original. Luu names that fix, then stops and makes the reader reconsider it before he explains where it falls short. He is visible in the patience: he takes the obvious answer seriously enough to take it apart rather than skip it.

## Trey Harris, "The case of the 500-mile email"

Source: https://www.ibiblio.org/harris/500milemail.html

> "But then I tried to send an email to Memphis (600 miles). It failed. Boston, failed. Detroit, failed. I got out my address book and started trying to narrow this down. New York (420 miles) worked, but Providence (580 miles) failed."

Before any theory, Harris establishes that the behavior is real by testing it against a list of cities and reporting which worked and which failed, with the distances beside them. The pattern is on the page for the reader to see. He is visible in the dry accounting of "Boston, failed. Detroit, failed."

> "One of the settings that was set to zero was the timeout to connect to the remote SMTP server. Some experimentation established that on this particular machine with its typical load, a zero timeout would abort a connect call in slightly over three milliseconds."

The cause is one named setting turned to zero, and he pins it to a measured figure, slightly over three milliseconds, instead of leaving it qualitative. Harris is visible in the exactness: he ran the experiment and reports the number he got.

> "An odd feature of our campus network at the time was that it was 100% switched. An outgoing packet wouldn't incur a router delay until hitting the POP and reaching a router on the far side. So time to connect to a lightly-loaded remote host on a nearby network would actually largely be governed by the speed of light distance to the destination rather than by incidental router delays."

The last step connects the timeout to the speed of light, the point below which nothing else about the network changes the answer. He reaches ground and stops. Harris is visible in following the chain one step past the setting, to the physical reason the number comes out where it does.
