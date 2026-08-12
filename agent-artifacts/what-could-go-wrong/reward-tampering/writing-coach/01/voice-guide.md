# Voice guide: what-could-go-wrong/reward-tampering

## How this piece should sound

This lesson teaches an argument about reward tampering to a reader who has never seen a training loop, then weighs that argument against a single controlled experiment. The register that holds both is plain and exact, the one Alexander, Yong, and Luu share below. It lets the piece keep the field's real vocabulary, the reward function, the training environment, specification gaming, while keeping the underlying mechanism visible, the way Yong keeps CD8+ and interferon inside a sentence a non-immunologist can still follow.

Teach the mechanism before you weigh it. Alexander builds the spread of study results out of one ordinary drug and a few plain steps before he draws any conclusion from it, and Luu starts the file problem from `a foo` that has to become `a bar`. The reward-tampering incentive can be built the same way, from a concrete case the reader can hold, before the argument turns on it. With no codebase time behind the reader, a worked example is what makes an abstract incentive followable.

Open the worry at full strength. The series asks for the argument as its most careful defender would put it, and Yong's handling of the cross-reactive T-cells shows what granting a case its best form looks like while still testing it: he states the appealing reading plainly, gives it a real hearing, and only then holds it against what the evidence supports. The tampering worry can be stated that fully before a word is raised against it.

Then draw the line the commission turns on: what the experiment demonstrated, at what rate, under what setup, against what remains projection about systems that do not yet exist. Yong reports a low rate by quoting the figure exactly and then saying both what it does and does not mean, doing the arithmetic rather than settling for "rare" or "common." When this piece reports how often the behavior appeared and under what curriculum, that same precision is available to it. Alexander's warning against the man of one study points the other way on the same problem: one dramatic result, however real, does not settle a question, and the piece can hold the surrounding evidence in view the way he lays competing meta-analyses side by side.

Report the experiment as evidence, attributed to the people who ran it. Luu names exactly which systems failed and ties each finding to the paper or the talk it came from, never to the reputation of anyone involved. This desk forbids naming a lab as an authority, and Luu's habit of crediting the result rather than the source's standing shows how to keep that line.

The lesson reaches its own verdict, and when it does the reasoning behind it should be on the page. Alexander's funnel-plot paragraph arrives at a conclusion and hedges it exactly as far as the evidence allows, showing every step from the shape of the plot to the reading he takes from it. Where the confidence on this subject outruns the proof, in either direction, the piece can name the gap plainly and leave the reader to decide how worried to be.

## Scott Alexander, "Beware The Man Of One Study"

Source: https://slatestarcodex.com/2014/12/12/beware-the-man-of-one-study/

> "For example, take medical research. Suppose a certain drug is weakly effective against a certain disease. After a few years, a bunch of different research groups have gotten their hands on it and done all sorts of different studies. In the best case scenario the average study will find the true result – that it’s weakly effective."

Alexander builds a general idea, the spread of results a single drug produces across many studies, out of one ordinary example and a few plain steps. He states the true effect first and then shows how noise and study quality scatter the findings around it, so the reader holds the whole distribution before any claim is made about it. The patience with the setup is Alexander's: he explains the machinery before he uses it.

> "Depends which one you want. Do you go with this meta-analysis of fourteen studies that shows that any presumed negative effect of high minimum wages is likely publication bias? With this meta-analysis of sixty-four studies that finds the same thing and discovers no effect of minimum wage after correcting for the problem? Or how about this meta-analysis of fifty-five countries that does find effects in most of them? Maybe you prefer this systematic review of a hundred or so studies that finds strong and consistent effects?"

Alexander lays four reviews side by side, each with its count and its finding, and lets them disagree without telling the reader which to believe. The specific numbers carry the paragraph, and his own view stays out of it. The reader meets the conflicting evidence at full strength before anyone weighs it.

> "This is more of a needle curve than a bell curve, but the point still stands. We see it’s centered around 0, which means there’s some evidence that’s the real signal among all this noise. The bell skews more to left than to the right, which means more studies have found negative effects of the minimum wage than positive effects of the minimum wage. But since the bell curve is asymmetrical, we intepret that as probably publication bias. So all in all, I think there’s at least some evidence that the liberals are right on this one."

Here Alexander does reach a conclusion, and he shows every step that got him there, from the shape of the plot to the asymmetry he reads as publication bias. The verdict is hedged exactly as far as the evidence allows, "at least some evidence," "probably," and the reasoning stays visible the whole way. A reader can check his logic because he never hides it.

## Ed Yong, "Immunology Is Where Intuition Goes to Die"

Source: https://www.theatlantic.com/health/archive/2020/08/covid-19-immunity-is-the-pandemics-central-mystery/614956/

> "Picture the lymph nodes as bars full of grizzled T-cell mercenaries, each of which has just one type of target they’re prepared to fight. The messenger cell bursts in with a grainy photo, showing it to each mercenary in turn, asking: Is this your guy? When a match is found, the relevant merc arms up and clones itself into an entire battalion, which marches off to the airways."

Yong explains one of the most intricate systems in biology through a concrete picture, and the picture is exact: each part of it maps to a real step, the single-target cell, the messenger, the search, the cloning. He keeps the technical machinery intact while making it something a reader can watch happen. This is Yong teaching a hard subject without thinning it out.

> "But Farber cautions that having these cross-reactive T-cells “tells you absolutely nothing about protection.” It’s intuitive to think they would be protective, but immunology is where intuition goes to die. The T-cells might do nothing. There’s an outside chance that they could predispose people to more severe disease. We can’t know for sure without recruiting lots of volunteers, checking their T-cell levels, and following them over a long period of time to see who gets infected—and how badly."

Yong takes the appealing reading, that these cells protect people, states it plainly, and then holds it apart from what the evidence actually supports. He lists what the cells might do instead, including the possibility they make things worse, and names exactly the study that would be needed to know. The restraint is the point: he gives the intuitive case a hearing and still refuses to claim more than the data shows.

> "So far, the fact that reinfections are still the subject of smattered anecdotes suggests that “it’s happening at a very low rate, if at all,” Cobey says. But remember: A bigger pandemic is a weirder pandemic. When there are almost 5 million confirmed cases, something that occurs just 0.1 percent of the time will still affect 5,000 people."

Yong reports a low rate carefully, quoting the researcher's own hedge and then doing the arithmetic that shows why a rare event still reaches thousands of people. He neither inflates the anecdotes into a trend nor waves them away. The figure is stated precisely, with both what it means and what it does not spelled out in the same breath.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "Let's look at a simple example of what it takes to save data in a way that's robust against a crash. Say we have a file that contains the text a foo and we want to update the file to contain a bar. The pwrite function looks like it's designed for this exact thing. It takes a file descriptor, what we want to write, a length, and an offset."

Luu opens the problem with the smallest concrete case he can find, a file that says `a foo` and should become `a bar`, and reaches for the obvious tool before showing what goes wrong with it. The difficulty is demonstrated step by step rather than announced. The plainness is deliberate, and it is how Luu makes a low-level subject followable for a reader who has never touched it.

> "The authors find issues with most of the applications tested, including things you'd really hope would work, like LevelDB, HDFS, Zookeeper, and git. In a talk, one of the authors noted that the developers of sqlite have a very deep understanding of these issues, but even that wasn't enough to prevent all bugs."

Luu reports what the study found in exact terms, naming the specific systems that failed and crediting each observation to the paper or the talk it came from. He notes that even careful, expert developers did not prevent every bug, which raises his estimate of the difficulty rather than softening it. Nothing is generalized past what the authors actually showed.

> "Files are hard. Butler Lampson has remarked that when they came up with threads, locks, and condition variables at PARC, they thought that they were creating a programming model that anyone could use, but that there's now decades of evidence that they were wrong. We've accumulated a lot of evidence that humans are very bad at reasoning about these kinds of problems, which are very similar to the problems you have when writing correct code to interact with current filesystems."

Luu draws a broad conclusion, that people are simply bad at reasoning about this class of problem, and grounds it in a named source and years of accumulated evidence rather than his own impression. The claim is large but earned, and the path to it is on the page. This is Luu reaching an analytic judgment and still tying it to evidence a reader can check.
