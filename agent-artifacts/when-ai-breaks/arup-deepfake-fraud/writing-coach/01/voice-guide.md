# Voice guide: when-ai-breaks/arup-deepfake-fraud (01)

## How this piece should sound

This lesson tells one fraud in order and then explains the weakness that let it work, for a reader who is quick but has never stopped to ask how a video call proves who is on it. The register is plain and serious: claims the reader can check, figures that carry their own weight, and no reaching for effect. The three writers below all report an attack this way, and each shows a different part of the job.

Open on the fact, the way Krebs opens on Fazio Mechanical rather than on a scene. This incident has a firm, a place, a date, an amount, and a police briefing behind it, and those can carry the first lines on their own. Krebs also pins each claim to who said it, as in his "investigators told this reporter." That habit is worth having here, because the case has a real line between what the Hong Kong police described, what Arup confirmed, and what only reporting alleges, and the reader should be able to feel which is which as the story moves.

Tell the sequence in steps, the way Greenberg tells the first minutes at Maersk: the message about a confidential transaction, the suspicion, the video call that settled it, the transfers, the later check with head office that undid it. Greenberg builds those minutes from what people saw and the exact words in front of them; the equivalent here is what the employee actually met on the call, reported concretely rather than summarized. The moment when the reassuring call becomes the thing that fools the employee is the center of this lesson, and it lands hardest if the reader has been walked through the call in the order the employee lived it.

When the mechanism arrives, explain it the way Greenberg explains EternalBlue and the way Schneier walks a man-in-the-middle attack from one step to the next: name each piece in plain words as it enters, and follow the attack in the order it happens. What the reader should end up understanding about why a live face and voice no longer settle who is speaking is yours to reach, not to assert; Schneier's passage on passwords shows the move that gets a reader there, which is to give the concrete failures first and let the general point form only after them. Voice cloning has already been taught in the course and can be linked at first use instead of explained again.

The exact amounts do much of the work, so handle them the way these writers handle figures. Give the real numbers, and where one is disputed or unconfirmed, mark it as Krebs marks Litan's estimate: attributed, ranged, and plainly said to be unsettled. If a figure is hard for the reader to feel, set it beside one they already hold, as Greenberg sets NotPetya's cost against WannaCry's. The lesson also has to end where this weakness still sits, in ordinary organizations that treat a face or a voice on a call as proof of identity, and it can say plainly what actually helps and why spotting the fake is not the thing that saves you. Keep that ending in the same plain voice as the rest.

## Brian Krebs, "Target Hackers Broke in Via HVAC Company"

Source: https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/

> "Sources close to the investigation said the attackers first broke into the retailer's network on Nov. 15, 2013 using network credentials stolen from Fazio Mechanical Services, a Sharpsburg, Penn.-based provider of refrigeration and HVAC systems."

Krebs opens on the fact itself: who broke in, when, and through which named company, with the attribution built into the same sentence. There is no scene and no wind-up, and the unglamorous specific (a small refrigeration and HVAC firm in Sharpsburg) does the work a vaguer phrase could not. You can see the reporter's discipline of tying every claim to who told it to him.

> "By the end of the month — just two days later — the intruders had pushed their malware to a majority of Target's point-of-sale devices, and were actively collecting card records from live customer transactions, investigators told this reporter. Target has said that the breach exposed approximately 40 million debit and credit card accounts between Nov. 27 and Dec. 15, 2013."

The timeline moves in dated steps and then lands a hard number with its date range, and Krebs keeps flagging where each part came from, separating what investigators said from what Target itself stated. The alarm is carried by the sequence and the figure, not by any adjective. Krebs is visible in how carefully he keeps those two sources apart inside one short passage.

> "In any case, Litan estimates that Target could be facing losses of up to $420 million as a result of this breach, including reimbursement associated with banks recovering the costs of reissuing millions of cards; fines from the card brands for PCI non-compliance; and direct Target customer service costs, including legal fees and credit monitoring for tens of millions of customers impacted by the breach."

Here Krebs handles a large money figure without inflating it: he names the analyst behind it (Litan, a Gartner fraud analyst he introduced a line earlier), marks it as an estimate with "up to" and "could be facing," and then breaks the figure into the parts it is made of. The itemizing is how he makes a big number legible instead of merely impressive. The estimate stays plainly an estimate.

## Andy Greenberg, "The Untold Story of NotPetya, the Most Devastating Cyberattack in History"

Source: https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/

> "And on the afternoon of June 27, 2017, confused Maersk staffers began to gather at that help desk in twos and threes, almost all of them carrying laptops. On the machines' screens were messages in red and black lettering. Some read 'repairing file system on C:' with a stark warning not to turn off the computer. Others, more surreally, read 'oops, your important files are encrypted' and demanded a payment of $300 worth of bitcoin to decrypt them."

Greenberg tells the first minutes through what people actually saw: staff drifting to a help desk in twos and threes, the exact words on the screens, the precise date. He explains nothing yet and lets the messages sit as the employees found them. The reporting is built from concrete, observed detail rather than from a summary of what happened.

> "NotPetya was propelled by two powerful hacker exploits working in tandem: One was a penetration tool known as EternalBlue, created by the US National Security Agency but leaked in a disastrous breach of the agency's ultrasecret files earlier in 2017. EternalBlue takes advantage of a vulnerability in a particular Windows protocol, allowing hackers free rein to remotely run their own code on any unpatched machine."

This is the technical mechanism explained in ordinary words: two tools working together, each named for what it does and defined in the same breath it appears ("a penetration tool known as EternalBlue"). A reader who holds no security vocabulary still follows how the attack ran. Greenberg teaches the machinery without stopping the narrative to lecture.

> "Even WannaCry, the more notorious worm that spread a month before NotPetya in May 2017, is estimated to have cost between $4 billion and $8 billion. Nothing since has come close."

To convey a cost the reader cannot feel, Greenberg sets it against another attack the reader may have heard of and gives a sourced range instead of one showy number. The short flat sentence that follows, "Nothing since has come close," carries weight because the figures in front of it earned it. The judgment stays tied to the numbers rather than floating above them.

## Bruce Schneier, "Two-Factor Authentication: Too Little, Too Late"

Source: https://www.schneier.com/essays/archives/2005/04/two-factor_authentic.html

> "Two-factor authentication isn't our savior. It won't defend against phishing. It's not going to prevent identity theft. It's not going to secure online accounts from fraudulent transactions. It solves the security problems we had 10 years ago, not the security problems we have today."

A run of short flat sentences, each removing one thing the reader might have hoped was true, building to a single longer line that says what is actually going on. The rhythm comes from sentence length, not from volume, and none of the sentences reaches for a phrase. Schneier's plainness is the entire effect.

> "The problem with passwords is that it is too easy to lose control of them. People give their passwords to other people. People write them down, and other people read them. People send them in email, and that email is intercepted. People use them to log into remote servers, and their communications are eavesdropped on. Passwords are also easy to guess. And once any of that happens, the password no longer works as an authentication token because you can never be sure who is typing in that password."

He explains why passwords fail by listing the ordinary ways people lose them, one concrete human action per clause, and only then states the point: you can never be sure who is typing. The abstract idea, a token you can no longer trust, arrives after the concrete examples have built it, not before. The parallel sentences make a dry point easy to hold in the head.

> "An attacker puts up a fake bank Web site and entices a user to that Web site. The user types in his password, and the attacker in turn uses it to access the bank's real Web site. Done correctly, the user will never realize that he isn't at the bank's Web site."

Schneier walks an attack through step by step, in the order it happens, using the plainest possible actors: an attacker, the user, the bank's real Web site. By the last sentence the reader sees how the trick defeats the very check it imitates, with no technical term used. The clarity comes from following the sequence and naming each move as it occurs.
