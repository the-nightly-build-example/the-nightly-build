# Voice guide: when-ai-breaks/amazon-rekognition-congress (01)

## How this piece should sound

This lesson tells one incident: a commercial face-matching service that returned
false matches between sitting members of Congress and police arrest photos, and
the argument that followed over what the test proved. The reader is quick and
widely read but has never had face matching, a similarity score, a photo
gallery, or a confidence threshold explained. The events are strong enough to
carry themselves. Somers writes "The passenger was killed" and stops. Where this
lesson states what a false match feeding a real police investigation does to the
person it names, the sourced facts can do the work, and words that grade the
facts (alarming, chilling, damning) can stay out.

Both Somers and Langewiesche open on a concrete scene before any mechanism: a
woman dialing 911 while a man climbs through her window; passengers boarding in
Rio who would be found two years later. This incident has its own openable scene
in the ACLU test and in what a false identification does to the person it lands
on, and the events can run in the order they happened: what Rekognition was sold
to police to do, what the test did, whom the matches named, what Amazon said
about it, and what Amazon later did.

The lesson has to teach three things, and Langewiesche's stall paragraph shows
one way to teach a mechanism to someone who has never met it: he names the angle
of attack, defines a stall, and gives the recovery without leaving a term
hanging. The threshold an operator sets, the number of faces a single search
compares a probe against, and the measured differences in matching accuracy
across groups can each be defined in the plain words of the sentence it first
appears in and grounded in the test's own numbers.

The article is asked to make its central figures mean something exact.
Langewiesche does this literally: he takes a pilot's logged hours and divides
them into takeoffs and landings until the number becomes "about four hours a
year." The count of members the test flagged, the default threshold set against
the one Amazon recommends for law enforcement, the size of the gallery searched,
and the way the false matches fell across groups can each be set against
something the reader already holds, so a figure lands as a specific quantity
rather than as a large-sounding one.

Gawande keeps reported fact, attribution, and his own reading apart: he writes
"They calculated that" the checklist "had prevented forty-three infections and
eight deaths," crediting the count rather than asserting it, and later gives a
plain judgment that rests only on facts already on the page. Amazon's account of
the result and the account from the ACLU and the auditors can each be reported
in its own terms before the lesson weighs them, and whatever the piece concludes
about what the test showed can sit on the cited evidence the same way. When the
story reaches the present, Langewiesche's close, which carries the same failure
forward and adds no moral, is one way to point at where face matching operates
now and then stop.

## James Somers, "The Coming Software Apocalypse"

Source: https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

> "There were six hours during the night of April 10, 2014, when the entire population of Washington State had no 911 service. People who called for help got a busy signal. One Seattle woman dialed 911 at least 37 times while a stranger was trying to break into her house. When he finally crawled into her living room through a window, she picked up a kitchen knife. The man fled."

Somers opens a piece about software design on a woman with a knife, not on
software. The stakes of a system failure are shown through one person in one
night, with the exact date and the count of 37 calls doing the work that an
adjective would otherwise be asked to do. You can see his judgment about what
matters in the choice to lead with her rather than with the server.

> "In September 2007, Jean Bookout was driving on the highway with her best friend in a Toyota Camry when the accelerator seemed to get stuck. When she took her foot off the pedal, the car didn't slow down. She tried the brakes but they seemed to have lost their power. As she swerved toward an off-ramp going 50 miles per hour, she pulled the emergency brake. The car left a skid mark 150 feet long before running into an embankment by the side of the road. The passenger was killed. Bookout woke up in a hospital a month later."

This narrates a technical failure in the order it happened, step by step, with a
named driver and hard figures (50 miles per hour, a 150-foot skid mark). The
death is stated in four words and not dwelt on, which is what keeps the passage
from tipping into melodrama. Somers is present in the pacing: each sentence is
one action, and the shortest sentence carries the worst fact.

> "\"Computing is fundamentally invisible,\" Gerard Berry said in his talk. \"When your tires are flat, you look at your tires, they are flat. When your software is broken, you look at your software, you see nothing.\""

Somers ends by handing the point to a source and getting out of the way. The
line is concrete (flat tires you can see) and it closes the piece without a
summary or a moral. His restraint is the visible choice here: he found a quotation
that states the idea plainly and trusted it to end the article.

## William Langewiesche, "The Human Factor"

Source: https://www.vanityfair.com/news/business/2014/10/air-france-flight-447-crash

> "As the angle of attack increases, so does lift efficiency—but only up to the point where the angle becomes too steep and the oncoming air can no longer flow smoothly over the tops of the wings. At that point, the airplane stalls. The phenomenon is characteristic of all airplanes and has nothing to do with the engines. When an airplane stalls, it loses lift and its wings begin to plow through the sky with enormous drag, far greater than engine thrust can overcome. The airplane enters a deep, mushing, nose-high descent, often accompanied by difficulties in roll control. The only solution is to reduce the angle of attack by lowering the nose and diving. This is counter-intuitive but basic to flight."

Langewiesche teaches a stall to a reader who has never flown, defining each term
as he reaches it and clearing away a wrong guess ("has nothing to do with the
engines") before it forms. The explanation moves in the order a learner needs:
what the angle is, when it fails, what failure looks like, how to recover. He is
a pilot, and it shows in the confidence to say the recovery is "counter-intuitive
but basic" without hedging.

> "No crisis existed. The episode should have been a non-event, and one that would not last long. The airplane was in the control of the pilots, and if they had done nothing, they would have done all they needed to do."

The horror of the story is that nothing was wrong yet, and Langewiesche states
that flatly rather than foreshadowing it. "No crisis existed" is three words; the
last sentence turns on the plain fact that inaction would have been enough. He
lets the gap between how small the failure was and how large the outcome became
do the work, without a sentence telling the reader it is coming.

> "On Air France 447, for instance, Captain Dubois had logged a respectable 346 hours over the previous six months but had made merely 15 takeoffs and 18 landings. Allowing a generous four minutes at the controls for each takeoff and landing, that meant that Dubois was directly manipulating the side-stick for at most only about four hours a year."

Langewiesche takes a number that sounds substantial, 346 hours, and works it into
one that is alarming, about four hours a year, by dividing it against the tasks
that count. The arithmetic is shown, so the reader can follow it and trust it.
His skepticism about the "respectable" figure is visible in the word "merely" and
in the decision to convert the hours at all.

## Atul Gawande, "The Checklist"

Source: https://www.newyorker.com/magazine/2007/12/10/the-checklist

> "To save this one child, scores of people had to carry out thousands of steps correctly: placing the heart-pump tubing into her without letting in air bubbles; maintaining the sterility of her lines, her open chest, the burr hole in her skull; keeping a temperamental battery of machines up and running. The degree of difficulty in any one of these steps is substantial. Then you must add the difficulties of orchestrating them in the right sequence, with nothing dropped, leaving some room for improvisation, but not too much."

Gawande makes an abstract idea, medical complexity, concrete by listing the
particular steps and naming their failure modes (air bubbles, a lost burr hole).
The reader arrives at "the degree of difficulty" already holding the evidence for
it. Gawande the surgeon is visible in the specifics only a practitioner would
reach for, and in the closing qualifier that improvisation has a limit.

> "Pronovost and his colleagues monitored what happened for a year afterward. The results were so dramatic that they weren't sure whether to believe them: the ten-day line-infection rate went from eleven per cent to zero. So they followed patients for fifteen more months. Only two line infections occurred during the entire period. They calculated that, in this one hospital, the checklist had prevented forty-three infections and eight deaths, and saved two million dollars in costs."

Gawande reports a striking result without inflating it: the figures are exact,
the follow-up period is stated, and the largest claims are attributed with "They
calculated that" rather than asserted in his own voice. The one word of judgment,
"dramatic", is immediately backed by the drop from eleven per cent to zero. His
care with attribution is the visible discipline.

> "Pronovost remains, in a way, an odd bird in medical research. He does not have the multimillion-dollar grants that his colleagues in bench science have. He has no swarm of doctoral students and lab animals. He's focussed on work that is not normally considered a significant contribution in academic medicine. As a result, few other researchers are venturing to extend his achievements. Yet his work has already saved more lives than that of any laboratory scientist in the past decade."

Gawande delivers a verdict, and it rests entirely on facts the paragraph has just
laid out. The three plain sentences about what Pronovost lacks earn the last one,
so the judgment reads as a conclusion rather than an opinion dropped in. His point
of view is clear and stated, but it never gets ahead of the evidence under it.
