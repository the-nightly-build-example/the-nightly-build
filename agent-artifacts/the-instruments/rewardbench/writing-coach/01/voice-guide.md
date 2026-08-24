# voice-guide: the-instruments/rewardbench (01)

## How this piece should sound

The lesson has to make one number make sense: a reward model's aggregate accuracy on RewardBench's fixed chosen-versus-rejected pairs, split across categories and rolled up by a stated weighting. Walk through how that number is built one step at a time, with the actual counts and the actual rule. Julia Evans explains DNS with the specific IP addresses, TTLs, and `dig` commands the reader would see running the queries themselves; the specifics carry the exposition. Do the same with the pair counts, the categories, the per-category weighting, and the leaderboard's update rule.

The reader arrives assuming that a reward model at the top of RewardBench is a better reward model, and the lesson has to take that apart. Zeynep Tufekci's essay on the pandemic works because it sets up R0 as the popular number and names its exact job (mean contagiousness) before it names the number that was missing (*k*, dispersion). RewardBench needs the same setup: what the score is agreement with (a fixed labeling of chosen versus rejected) before what people read into it that it does not deliver. Downstream chatbot quality is where the misreading lives, and the sentence that draws that line is worth writing carefully.

The primary papers the researcher gathers carry the case only if their specific figures reach the page: the RewardBench paper, the RewardBench 2 rework after saturation, the sycophancy findings on preference models, the length- and formatting-bias analyses. Tufekci writes "about 19 percent of cases were responsible for 80 percent of transmission" and names the Hong Kong contact-tracing paper it came from. Dan Luu names Kyle Kingsbury and the specific databases Jepsen broke. The move to imitate is naming the paper and the figure. "Critics have noted" is the move to avoid.

Two statistical steps in the RewardBench score are easy to misread: the weighted mean across categories with different pair counts, and the accuracy computed on a small fixed set. Where one of those needs unpacking, a short concrete comparison the reader already carries can make it stick. Tufekci uses a bar and a billionaire for a heavy-tailed distribution because the analogy matches the exact distributional point she is teaching, and the paragraph ends by saying what the analogy showed. Reach for one only where the material has one waiting, and pick it for the specific move.

Evans keeps the reader's trust because in the same paragraph where she reports what a query returned she says out loud what she is guessing about ("I guess because 8.8.8.8 actually load balances to a bunch of different backends"). The lesson has room for that kind of small hedge inside its walk-through of how the score is built, and the effect is teaching by someone who watched the thing run rather than someone who read the paper's abstract.

## Julia Evans, "What happens when you update your DNS?"

Source: https://jvns.ca/blog/how-updating-dns-works/

> Hmm, it seems like that DNS server has the 1.2.3.4 record still cached for another 144 seconds. Interestingly, if I query 8.8.8.8 multiple times I actually get inconsistent results – sometimes it'll give me the new IP and sometimes the old IP, I guess because 8.8.8.8 actually load balances to a bunch of different backends which each have their own cache.

This is what a patient walk-through looks like on the page. The number is specific (144 seconds), the observation is specific (inconsistent results across queries to the same resolver), and the writer names the reason as a guess rather than a fact. The reader can see her at the terminal reading what came back.

> As with most internet protocols, not everything obeys the DNS specification. Some ISP DNS servers will cache records for longer than the TTL specifies, like maybe for 2 days instead of 5 minutes. And people can always hardcode the old IP address in their /etc/hosts.

The gap between the specification and what happens in the wild is stated with the concrete offenders: ISP resolvers ignoring the TTL, someone editing `/etc/hosts`. Evans tells the reader why the theory does not match reality by naming the ways it fails. "In practice, things are messier" would carry no information; the resolvers and the hosts file do.

## Zeynep Tufekci, "This Overlooked Variable Is the Key to the Pandemic"

Source: https://www.theatlantic.com/health/archive/2020/09/k-overlooked-variable-driving-pandemic/616548/

> By now many people have heard about R0—the basic reproductive number of a pathogen, a measure of its contagiousness on average. But unless you've been reading scientific journals, you're less likely to have encountered *k*, the measure of its dispersion. The definition of *k* is a mouthful, but it's simply a way of asking whether a virus spreads in a steady manner or in big bursts, whereby one person infects many, all at once.

Tufekci names the number the reader has heard of, states what it is in one clause, and then names the second number the reader has not heard of and states what it is in one clause. The reader knows both after two sentences. The teacherly move is doing definitional work at the point where the argument needs the definition and not before.

> Unfortunately, averages aren't always useful for understanding the distribution of a phenomenon, especially if it has widely varying behavior. If Amazon's CEO, Jeff Bezos, walks into a bar with 100 regular people in it, the average wealth in that bar suddenly exceeds $1 billion. If I also walk into that bar, not much will change. Clearly, the average is not that useful a number to understand the distribution of wealth in that bar, or how to change it. Sometimes, the mean is not the message.

The analogy is picked for one specific statistical property, a heavy-tailed distribution the mean does not describe, and the paragraph closes on the statistical claim the analogy was chosen to carry. Nothing about the bar is decorative; every clause is doing the same explanatory job.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> My go-to example for this is Kyle Kingsbury's work with Jepsen. Before Jepsen, a handful of huge companies (the now $1T+ companies that people are calling "hyperscalers") had decently tested distributed systems. They mostly didn't talk about testing methods in a way that really caused the knowledge to spread to the broader industry. Outside of those companies, most distributed systems were, by my standards, not particularly well tested.

Luu opens the case with the person and the tool by name, then sketches what the world looked like before the tool existed. The parenthetical places the reader without demanding they hold a list of companies, and "by my standards" flags that the assessment is his judgment. Nothing is stated at higher confidence than the evidence lets him state it.

> The typical response that I've seen when a catastrophic bug is reported is that the project maintainers will assume that the bug report is incorrect (and you can see many examples of this if you look at responses from the first few years of Kyle's work). When the reporter doesn't have a repro for the bug, which is quite common when it comes to distributed systems, the bug will be written off as non-existent. When the reporter does have a repro, the next line of defense is to argue that the behavior is fine (you can also see many examples of these from looking at responses to Kyle's work).

He describes a pattern he has watched play out, and each stage of it is a specific thing the maintainers did: dismiss the report, argue the behavior is fine, and so on. The reader is pointed twice at the record where the pattern can be checked. The paragraph does the work of a general observation while staying on the specific instances.
