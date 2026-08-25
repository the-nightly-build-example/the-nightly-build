## Malcolm Gladwell, "The Order of Things"

Source: https://www.newyorker.com/magazine/2011/02/14/the-order-of-things

> "A ranking can be heterogeneous, in other words, as long as it doesn't try to be too comprehensive. And it can be comprehensive as long as it doesn't try to measure things that are heterogeneous. But it's an act of real audacity when a ranking system tries to be comprehensive and heterogeneous—which is the first thing to keep in mind in any consideration of U.S. News & World Report's annual "Best Colleges" guide."

Three paragraphs of car-review arithmetic (three different cars win, depending only on how the same twenty-one variables get weighted) get compressed into one rule, and the rule is named rather than hinted at: comprehensive, heterogeneous, and why combining them is the trap. The same sentence closes the toy example and opens the real subject, so the piece never announces a transition — it just keeps applying the rule it already earned.

> "Take the category of "faculty resources," which counts for twenty per cent of an institution's score. "Research shows that the more satisfied students are about their contact with professors," the College Guide's explanation of the category begins, "the more they will learn and the more likely it is they will graduate." That's true. According to educational researchers, arguably the most important variable in a successful college education is a vague but crucial concept called student "engagement"—that is, the extent to which students immerse themselves in the intellectual and social life of their college—and a major component of engagement is the quality of a student's contacts with faculty. As with suicide, the disagreement isn't about what we want to measure. So what proxies does U.S. News use to measure this elusive dimension of engagement?"

The move is to name the real thing first (engagement), concede that nobody disputes it matters, and only then show what actually gets counted in its place. "As with suicide" reaches back to an earlier example instead of re-explaining it, so the reader carries the point forward rather than relearning it. The paragraph ends on a real question, the one the next paragraph is about to answer, not a rhetorical one.

> "In other words, when U.S. News asks a university president to perform the impossible task of assessing the relative merits of dozens of institutions he knows nothing about, he relies on the only source of detailed information at his disposal that assesses the relative merits of dozens of institutions he knows nothing about: U.S. News. A school like Penn State, then, can do little to improve its position. To go higher than forty-seventh, it needs a better reputation score, and to get a better reputation score it needs to be higher than forty-seventh. The U.S. News ratings are a self-fulfilling prophecy."

The repeated clause is not padding — the same phrase appears twice because the same blind judgment is being fed back into itself, and repeating it is how the loop gets shown instead of described. The short sentence that ends the paragraph is allowed to be short because the loop just demonstrated it; nothing is asserted that the sentences above didn't already prove.

## Julia Evans, "Benchmarking correctly is hard (and techniques for doing it better)"

Source: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/

> "I'm less interested in the question of academic rigor here and more interested in the idea of benchmarking correctly in practice – I'd like to make programs faster, and a great way to make your stuff WAY FASTER is to make many small 5% improvements. So you need to actually be able to detect a 5% improvement."

One number does two jobs at once: it's the size of a real win worth chasing, and it's the size of the noise a sloppy benchmark can't tell apart from a win. Stating it once lets both points land off the same figure instead of needing a separate sentence for each. "You need to actually be able to detect" keeps the abstract research question tied to something the reader might go do this afternoon.

> "In the first one, at first everything is slow. Maybe the code is in Java, and the JIT hadn't kicked in yet. But then the samples speed up, everything stabilizes, and you're golden. You can probably meaningfully average them after that point (but remember to throw away the samples at the beginning!!)."

The example isn't decoration for an abstract idea (independent samples) — it's the actual, specific reason benchmarks lie to people, named by its mechanism (JIT warm-up) rather than left as an unexplained caveat. The aside in parentheses reads like something she'd say twice out loud to make sure it landed, not a hedge.

> "The idea is – if you have a series of benchmarks over time (like the periodic one I drew above), and then you randomly shuffle all of the benchmarks, does the randomly shuffled one look basically the same as the original? if not (like if the original was monotonically decreasing one, and the shuffled one isn't), then it's not independent!"

This describes a test the reader could actually run — she poses the question and then gives the exact case that would break it, so the claim comes with its own check attached. The technical vocabulary (monotonically decreasing, independent) stays exact even in a sentence built from casual, spoken rhythm; the precision and the casualness aren't in tension.

## Nate Silver, "How we calculate our PELE ratings"

Source: https://www.natesilver.net/p/pele-methodology

> "Rating updates are based on what we call harmonic margin or "h-margin". In h-margin, each additional goal has diminishing returns: the second goal in a 2-goal victory counts ½ as much as the first one, the third goal counts ⅓ as much, and so on."

The rule is given twice in two different registers — once as an idea (diminishing returns) and once as arithmetic (½, then ⅓) — so a reader who trusts the idea and a reader who wants to check the number both get what they need from the same two sentences. Neither version is left to carry the point alone.

> "PELE does not use FIFA confederations for anything: these do not correlate all that well with football performance, and can be influenced by political and other arbitrary factors. They can also be blunt instruments for continents as large as Asia. Instead, we crafted our own set of 12 regions, which deliberately contain some overlap. I'm going to be honest, we went through a lot of different versions of these."

The rejected alternative is named specifically (FIFA's own confederations) and the charge against it is concrete (correlated with politics, too blunt for a landmass the size of Asia), which is what makes the claim checkable instead of a vague gesture at "some other approach." "I'm going to be honest" isn't a hedge here — it's a flag that a genuinely arbitrary call is about to be admitted, and the next sentence doesn't try to dress it up as anything else.

> "From first principles, for example, you'd expect Argentina to defeat American Samoa. Even if you'd never seen a soccer game, you'd know that Argentina is much larger, has a much longer football legacy, and comes from a region where football plays a much more prominent role in the culture."

The claim — that team strength is partly predictable before a single match is played — is proven with a case obvious enough that a reader who has never watched soccer can check it unaided. Two separate reasons are given (size, legacy, culture) rather than the one that came to mind first, which is the difference between an example and a reach.

## How this piece should sound

This lesson opens a black box: a number people already cite ("this model is good at tool use") and a procedure almost none of them have looked at. The job the passages above model, over and over, is naming the real thing being asked about, naming what actually gets measured instead, and showing — not asserting — the gap between them. Gladwell's "engagement" passage is the template move: say what the leaderboard is supposed to be standing in for, concede that's a reasonable thing to want to know, and only then show what the score is actually built from. That structure does the teaching so no sentence has to announce "here's the catch."

Every mechanism this lesson explains should get the h-margin treatment: stated once as an idea, once with the real numbers next to it. Silver doesn't leave "diminishing returns" to do the work alone, and doesn't leave the fraction to do it alone either — a reader who wants the intuition and a reader who wants to verify get the same two sentences. Wherever the benchmark makes a scoring or categorization choice, that choice can carry a real number the way the ½ and ⅓ do, rather than a description of the choice in the abstract.

Where a design choice in the benchmark was a judgment call rather than a necessity, Silver's move is worth borrowing over Gladwell's: name the alternative that was passed over and say concretely why, the way he names FIFA's confederations and charges them with being politically distorted and too blunt for Asia. A vague "this is one of several ways to do it" teaches nothing a reader can check; a named alternative and a specific reason does. If the benchmark's own documentation makes a case for a choice the way U.S. News does for its faculty-resources proxies, that reasoning is fair game to quote and then hold up against what the number can actually support — that is the whole engine of the Gladwell passages, and it works exactly because he quotes the guide's own justification rather than paraphrasing it.

Ground every abstraction the way Silver grounds "predictable team strength" in Argentina versus American Samoa: pick a comparison the declared reader can check without having opened the leaderboard, and give more than one reason so it reads as an example rather than a reach. The lesson's own worked example — the one that carries a reader through what a score actually rewards — should be built the same way: concrete, checkable without outside expertise, and stated plainly rather than hedged.

If the argument reaches a place where the number's own dynamics feed on themselves — a benchmark that rewards a specific kind of performance well enough that models get built or tuned specifically to clear it — Gladwell's self-fulfilling-prophecy paragraph is the shape to study, not the phrase to borrow. The repetition there does the proving; state the loop once, plainly, and let the short sentence that follows be earned by what came right before it rather than announced ahead of it.

Evans's "randomly shuffle it and see" is a useful register for the moment this lesson turns from what the number means to what a skeptical reader could do about it: state a check as something the reader could picture running, not a claim to take on faith. That voice — plain, direct, technical words left exactly as precise as the field uses them — is closer to this paper's register than Gladwell's magazine cadence or Silver's insider-methodology density, and it is the one to lean on for the passages doing the most direct teaching. But her exclamation points, asides, and diary-like first person ("I don't know which is better!") belong to a personal blog and not to this lesson's body, which never turns to address the reader or narrate its own thinking; keep her precision and her plainness, not her voice on the page. The two bookends are the one place in the piece that gets to speak to the reader directly and admit what the lesson is doing — that's where a Silver-style "I'm going to be honest" about what the reader is about to learn, if the piece earns one, belongs, not in the body.

Save the human cost — the case where the number misled someone and what it cost them — for after the mechanism is fully built, the way Gladwell holds Penn State's president until the reader already understands selectivity, efficacy, and why a school can't score well on both. A reader who hasn't yet been shown how the score is built has nothing to measure the misreading against.
