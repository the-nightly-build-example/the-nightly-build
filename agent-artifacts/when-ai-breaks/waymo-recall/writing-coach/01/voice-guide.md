# Voice guide: when-ai-breaks/waymo-recall (01)

## How this piece should sound

This lesson reconstructs a driverless car's collision with a towed truck and the
recall that followed, then teaches why a machine-perception system mispredicts
the path of a rare object. The reader is smart and reads widely and has never
worked on a perception stack. Hold the register the series holds: plain,
concrete, and sober. No one was hurt in this incident, so the writing has no
drama to reach for, and reaching for it would cost the reader's trust.

Carry the incident on a clock. Langewiesche narrates ValuJet 592 in clock times,
altitude readouts, and headings, and marks the reconstructed parts as
reconstruction ("Investigators later calculated that the airplane rolled to a
sixty-degree left bank and dove 6,400 feet in thirty-two seconds"). The Waymo
sequence has the same raw materials: when the vehicle detected the truck, what
it predicted the truck would do, when it braked or steered or did neither, how
far apart the two contacts were. Where the record shows only what was
reconstructed after the fact rather than logged in the moment, the writing can
say so in the same plain way, so the reader knows which is which.

Teach the technical cause as a chain of plain steps. Langewiesche explains the
oxygen generator one physical link at a time, each link naming the next, until a
reader who knows no chemistry holds the whole mechanism. A perception system's
misprediction has that shape too: what the sensors return, how the system
classifies what it sees, how it predicts where a moving thing will go next, and
how the planner acts on that prediction. Laid out link by link, why a towed
truck defeats a step built for ordinary traffic becomes something the reader can
follow.

When a term of art is unavoidable, give it its plain meaning in the sentence it
first appears, the way Wise defines an aerodynamic stall as he uses it ("an
aerodynamic stall, which means that the wings had lost their ability to generate
lift"). A design feature the reader has never met can be reached through the
familiar case they already picture: Wise explains the Airbus's asynchronous side
sticks by setting them against the linked controls of the plane most readers
imagine, then says why the difference mattered that night. A towed vehicle, or
whatever made this object unlike normal traffic, can be reached the same way,
from the ordinary case the system usually handles.

The hardest thing this piece has to do is make the reader see why a careful
system still hit something rare, without excusing the system or inflating what
happened. Feynman's account of the shuttle's eroded seals is built for exactly
that problem: a fault the machine survived many times before is still a fault,
and the survivals are not evidence of safety. If the Waymo system had
encountered and handled unusual vehicles many times before this one, that record
is worth stating plainly and worth reading the way Feynman reads it. Where the
cause sits in the design of the system rather than in any single failure, the
writing can name that precisely, as Langewiesche names the confusion between
"expired" and "expended" canisters, and can decline to assign blame the evidence
does not support. Wise keeps a genuine danger in proportion by naming it and its
rarity in the same breath ("the most dangerous component of a modern commercial
jetliner is the brain of the pilot at its controls. The majority of fatal
airline accidents (vanishingly rare though they may be) are due to pilot
error"). For an incident that injured no one, stating the seriousness of the
failure mode and the limits of what happened together is the move that keeps the
piece honest.

## William Langewiesche, "The Lessons of ValuJet 592"

Source: https://www.theatlantic.com/magazine/archive/1998/03/the-lessons-of-valujet-592/306534/

> "Two and a half minutes had gone by. It was 2:13 P.M. The airplane was passing through 7,500 feet when suddenly it tightened the left turn and entered a steep dive. Fisher's radar showed the turn and an altitude readout of XXX—code for such a rapid altitude change that the computer cannot keep up. Investigators later calculated that the airplane rolled to a sixty-degree left bank and dove 6,400 feet in thirty-two seconds."

The passage runs on a clock, and every number is one a reader can hold: elapsed
time, altitude, bank angle, feet lost, seconds. Langewiesche is visible in the
last sentence, where he hands the precise figures to the investigators who
computed them rather than stating them as if he had watched the dive himself.
The radar's "XXX" is left as the raw thing the screen showed and then explained,
so the reader learns the instrument and the moment at once.

> "To activate oxygen flow the passenger pulls a lanyard, which slides a retaining pin from a spring-loaded hammer, which falls on a minute explosive charge, which sparks a chemical reaction that liberates the oxygen within the sodium-chlorate core. This reaction produces heat, which may cause the surface temperature of the canister to rise to 500° Fahrenheit if the canister is mounted correctly in a ventilated bracket, and much higher if it is sealed in a box with other canisters, which may themselves be heating up."

A mechanism most readers have never thought about is taught as one physical chain,
each clause handing off to the next: lanyard, pin, hammer, charge, reaction,
heat. Langewiesche's control shows in how he saves the danger for the end, where
the same device that is safe in its bracket becomes something else packed in a
box. The technical vocabulary stays exact ("sodium-chlorate core", "ventilated
bracket") and the sentence still moves.

> "This required a gang of hard-pressed mechanics to draw a verbal distinction between canisters that were "expired," meaning most of the ones they were removing, and canisters that were not "expended," meaning many of the same ones, loaded and ready to fire, on which they were expected to put nonexistent caps. Also involved were canisters that were expired and expended, and others that were not expired but were expended. And then, of course, there was the set of new replacement canisters, which were both unexpended and unexpired. If this seems confusing, do not waste your time trying to figure it out—the SabreTech mechanics did not, nor should they have been expected to."

Langewiesche piles the confusing distinctions on the reader on purpose, then
tells them to stop trying to untangle it, and the confusion he made them feel is
the cause he is assigning. He locates the fault in the wording of the procedure
rather than in the men following it, and says so plainly in the last clause. The
judgment is exact about where blame belongs and where it does not.

## Jeff Wise, "How Panic Doomed an Airliner"

Source: https://www.jeffwise.net/2011/12/07/how-panic-doomed-an-airliner/

> "Instead, neither man consulted a checklist, and Bonin pulled back on the controls, causing the airplane to climb and lose airspeed. Soon, he had put the plane into an aerodynamic stall, which means that the wings had lost their ability to generate lift. Even with engines at full power, the Airbus began to plummet toward the ocean."

Wise defines the one term the sentence needs the moment he uses it, so a reader
who has never heard "aerodynamic stall" is not left behind. The cause and its
effect follow in order, action then consequence, without a technical detour. The
plain "began to plummet toward the ocean" states the outcome and stops.

> "Unlike a Boeing jet, in which one pilot's movement of the control yoke moves the other pilot's yoke as well, an Airbus features "asynchronous" controls, meaning that moving one control doesn't cause the other to move as well. Bonin's colleagues probably never knew that he had the controls all the way back—perhaps because they never imagined that any certified airline pilot could engage in such a misguided response."

A design detail the reader has never considered is explained through the
contrast with what they would assume, and then tied at once to why it mattered
in the cockpit. Wise is visible in the second sentence, where he marks his own
inference ("probably", "perhaps") instead of stating the pilots' minds as fact.
The distinction between the mechanical fact and the guess about intent is kept
clean.

> "What can we learn from AF447? Above all, the tragedy reinforces an unfortunate truth about air travel that many passengers do not appreciate: that the most dangerous component of a modern commercial jetliner is the brain of the pilot at its controls. The majority of fatal airline accidents (vanishingly rare though they may be) are due to pilot error."

Wise makes a strong claim and keeps it in proportion in the same breath: the
parenthetical "vanishingly rare though they may be" sits inside the sentence
that names the danger. He is visible in the willingness to state the blunt claim
plainly rather than hedge it. The seriousness and the rarity are held together,
so neither cancels the other.

## Richard P. Feynman, "Personal Observations on the Reliability of the Shuttle" (Appendix F, Rogers Commission Report)

Source: https://history.nasa.gov/rogersrep/v2appf.htm

> "But erosion and blow-by are not what the design expected. They are warnings that something is wrong. The equipment is not operating as expected, and therefore there is a danger that it can operate with even wider deviations in this unexpected and not thoroughly understood way. The fact that this danger did not lead to a catastrophe before is no guarantee that it will not the next time, unless it is completely understood. When playing Russian roulette the fact that the first shot got off safely is little comfort for the next."

Feynman explains why a fault the machine survived before is still a fault, in
short declarative steps that build one to the next. The reasoning is the point,
and he shows every link of it rather than asserting the conclusion. The single
image at the end is grounded in the exact situation he is describing, a risk run
repeatedly without harm, so it carries the argument instead of decorating it.

> "If a bridge is built to withstand a certain load without the beams permanently deforming, cracking, or breaking, it may be designed for the materials used to actually stand up under three times the load. This "safety factor" is to allow for uncertain excesses of load, or unknown extra loads, or weaknesses in the material that might have unexpected flaws, etc. If now the expected load comes on to the new bridge and a crack appears in a beam, this is a failure of the design. There was no safety factor at all; even though the bridge did not actually collapse because the crack went only one-third of the way through the beam."

Feynman corrects a technical misconception by walking the reader through a
physical example they already understand, a loaded bridge, rather than by
stating that the reasoning was wrong. He defines "safety factor" in use and then
shows the exact place the reasoning broke. He never states the correction
outright; the bridge example makes it for the reader.
