# Voice guide: when-ai-breaks/itutorgroup-age-discrimination

## How this piece should sound

This lesson tells one hiring-discrimination case and then explains why that kind of automated screening fails. Write it in this paper's plain, unhurried register, for a reader who is sharp and widely read but new to hiring software and to U.S. employment law. Terms the field takes for granted, such as the ADEA, a consent decree, or an automated knockout rule, get a plain definition in the sentence where they first appear, and nothing is talked down to.

The piece is built on a sequence of events, and Brian Krebs's reconstruction of the Target breach shows how much a plain sequence can carry. He names the vendor, the town, and the two-month gap, and he attributes each step as he goes; the account never dramatizes because the order of events is enough on its own. This case has that kind of record. The EEOC complaint and the consent decree fix the companies, the dates, the two age cutoffs, and the number of rejected applicants, so the narration can name people, companies, and dates and let the sequence do the work. Where the record is thin or the operator never confirmed something, Krebs's habit of saying so plainly, as in "they probably didn't, at least at first," is the honest move, and the same restraint fits any point here the primary documents do not settle.

The commission asks for an honest account of the mechanism, and honesty here is a specific claim: iTutorGroup's software rejected applicants by a date-of-birth cutoff that someone configured, not a model that learned bias from data. Dan Luu's power-loss incident shows how to make a mechanism vivid by trusting the specifics instead of a general word for the failure: 48 hosts, 37 failures, one directory a script expected and did not find. The explicit age rule can be shown that concretely, and the contrast the piece draws with a learned proxy, the kind of bias in the Amazon recruiting tool that the reader can reach through Background, stays sharp when each mechanism is described by what it actually does.

The law has to be usable by a reader who has never read a statute, and Amy Howe's court explainers are the model. She states the rule in a sentence a non-lawyer can hold before she applies it, quotes the opinion only for the words that carry the standard, and keeps the citation apparatus out of the prose. The ADEA's plain content can be stated that plainly before the case turns on it: it protects workers 40 and older, so a rejection keyed to age is discrimination on its face. A verdict is welcome once the facts earn it, the way Howe reports a court's conclusion without adding heat of her own; if the explicit rule is what made this case clean to prove, the facts already on the page can carry that judgment.

No hype and no doom. A grand word about automated hiring belongs only after the evidence has earned it. The close, where the piece finds the same weakness in the screening tools a reader might actually be filtered by, reads harder as a plain description of what those tools do than as a warning about them.

## Brian Krebs, "Email Attack on Vendor Set Up Breach at Target"

Source: https://krebsonsecurity.com/2014/02/email-attack-on-vendor-set-up-breach-at-target/

> "Last week, KrebsOnSecurity reported that investigators believe the source of the Target intrusion traces back to network credentials that Target had issued to Fazio Mechanical, a heating, air conditioning and refrigeration firm in Sharpsburg, Pa. Multiple sources close to the investigation now tell this reporter that those credentials were stolen in an email malware attack at Fazio that began at least two months before thieves started stealing card data from thousands of Target cash registers."

This tells the origin of the breach in order, naming the vendor, the town, the kind of firm, and the two-month gap before the card theft, and it marks its sources as it goes. Krebs is visible in how much he is willing to attribute and how little he rounds off: the credentials were issued, then stolen, then used, and each step is named rather than compressed into a summary. Nothing is dramatized, and the sequence carries the paragraph.

> "Many readers have questioned why the attackers would have picked on an HVAC firm as a conduit for hacking Target. The answer is that they probably didn’t, at least at first. Many of these email malware attacks start with shotgun attacks that blast out email far and wide; only after the attackers have had time to comb through the victim list for interesting targets do they begin to separate the wheat from the chaff."

Krebs answers a question a reader would actually ask, and his answer corrects the natural assumption by describing how the attack really worked rather than reaching for a flourish. The flatness of "they probably didn't, at least at first" is where the writer shows himself: he would rather be exact than sound knowing.

## Dan Luu, "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "There are a couple reasons we want to write this down. First, historical knowledge about what happens at tech companies is lost at a fairly high rate and we think it's nice to preserve some of it. Second, we think it can be useful to look at incidents and reliability from a specific angle, putting all of the information into one place, because that can sometimes make some patterns very obvious."

This states plainly why the incidents are worth collecting and what the collection is for, without claiming importance in the abstract: the reason given is that patterns become visible when everything sits in one place. The author is visible in the flatness of the claim: a couple of reasons, numbered and stated, nothing sold.

> "The trigger for this incident was power loss in two rows of racks. In terms of the impact on cache, 48 hosts lost power and were restarted when power came back up, one hour later. 37 of those hosts had their caches fail to come back up because a directory that a script expected to exist wasn't mounted on those hosts."

The mechanism is made concrete by exact figures and one small fact: 48 hosts lost power, 37 failed to recover, because a script expected a directory that was not there. The writing trusts the specifics to do the explaining and never reaches for a general word like "fragility." The engineer shows in the refusal to round 37 up to "most."

## Amy Howe, "Opinion analysis: Unanimous court throws out 'Bridgegate' convictions"

Source: https://www.scotusblog.com/2020/05/opinion-analysis-unanimous-court-throws-out-bridgegate-convictions/

> "In 2013, officials with ties to Chris Christie, then the governor of New Jersey, altered the traffic pattern on the George Washington Bridge in an effort to punish the mayor of nearby Fort Lee, New Jersey, for his failure to support Christie’s reelection bid. The change in the traffic pattern led to four days of gridlock on the streets surrounding the bridge before the original pattern was eventually restored."

Howe opens by telling what happened in one plain sequence: who acted, on what, to punish whom, and what it caused. The names and the year do the work, and the second sentence gives the concrete result, four days of gridlock, instead of characterizing it. Howe shows in how little she editorializes a story that invites it.

> "After Mark Sokolich, the mayor of Fort Lee, declined to endorse Christie in 2013, Baroni and Kelly – along with David Wildstein, a Port Authority staffer – decided to retaliate against Sokolich by reducing the number of lanes reserved for Fort Lee drivers to one. They made the change on the first day of school in September 2013, without notifying Sokolich in advance. To explain the change to Port Authority employees, the trio concocted a fictitious traffic study."

The scheme is laid out step by step, every actor named and dated: the mayor declined, the officials retaliated, the change went in on the first day of school, a fake study was written to cover it. A reader who knows no law follows it completely. Howe's control shows in the verbs she chooses: declined, decided, concocted, each one plain and exact.

> "In a 13-page opinion, Kagan emphasized that the government needed to show “not only that Baroni and Kelly engaged in deception,” but that they did so to obtain property. The Supreme Court has made clear that unless bribes or kickbacks are involved (which, Kagan noted, are not at issue in this case), federal fraud laws cannot be used as a general tool to fight public corruption; they apply only when efforts to obtain money or property are involved."

Here Howe states the legal rule in a sentence a non-lawyer can hold: the fraud laws reach deception only when it aims to obtain money or property, not public corruption in general. She quotes the opinion for the few words that carry the standard and paraphrases the rest, so the reader gets the rule without the citation apparatus. The law is made usable, not simplified away.
