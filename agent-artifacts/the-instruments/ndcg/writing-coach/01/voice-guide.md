# Voice guide: the-instruments/ndcg (01)

## How this piece should sound

A leaderboard rank built from nDCG is a number readers already trust without
having seen what's under it. The register throughout is plain and
declarative: state what a relevance grade is, state what the discount does
to a low-ranked hit, state what normalizing divides by, in that order,
without hedging any of it as fiddly or technical-sounding before it's been
shown to be simple. A reader who has never seen a ranked list of search
results should be able to follow the construction using nothing but arithmetic
they already have, and the piece should write as if that's obviously
possible, not as a trick being pulled off.

Where the piece constructs an example — a short ranked list, a few relevance
grades, the discounted and normalized scores that come out — give the reader
the concrete numbers before any generalization about them, the way a wrong
formula and a right one get shown side by side rather than argued about in
the abstract. State the wrong intuition (say, that a metric which only counts
how many relevant results appear must be enough) and the numbers that break
it, before naming what fixes it. The verdict on why an intuition fails can
come first, with the arithmetic as its proof, rather than building up to the
verdict as a reveal.

Name the technical vocabulary plainly and once: "relevance grade,"
"discount," "normalization" each earn a sentence that defines them in the
same breath they're introduced, and after that the piece keeps using that
exact word rather than reaching for a synonym. A parenthetical aside or a
specific, named failure mode (a particular way a leaderboard number misleads,
not "certain limitations") does more work here than a general caution would.
When the piece turns skeptical of what the single number hides, it can give
the practice credit for what it does solve before it qualifies what it
doesn't — stating the limitation as a specific, checkable fact about the
metric's construction, not as a mood of doubt cast over the whole enterprise.

An analogy is worth using only where it carries the actual mechanism — a
position discount is a claim about where in the list a hit lost value, and an
analogy should let the reader locate that loss, not just gesture at "results
further down mattering less." Humor, where the material earns it, can sit in
a plain aside rather than a punchline built for quoting. The piece never
narrates itself or previews what the reader will know; it just teaches the
next piece in order and lets the takeaway bookend, written separately, do the
looking-back.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well. So what's going on?"

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

The two short sentences carry the whole setup: a plain factual claim, then a
plain question, with no throat-clearing between them. Evans is visible in the
choice not to soften "YEARS" with an adverb — the capitals do the emphasis
instead of a qualifier like "quite a while."

> "When I finally learned how to troubleshoot DNS problems, my reaction was "what, that was it???? that's not that hard!". I felt a little bit cheated!"

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

She states her own reaction as a fact to be reported, not an aside to be
apologized for. The four question marks are a specific, countable choice, not
a generic "surprised" — that specificity is what makes the sentence sound
like a person and not a summary of a person.

> "It took me probably 5 years to realize that I shouldn't visit a domain that doesn't have a DNS record yet, because then the nonexistence of that record will be cached, and it gets cached for HOURS, and it's really annoying."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

The technical term ("cached") arrives inside an ordinary sentence about
being annoyed, not set off in its own definitional sentence. She names the
exact mechanism (nonexistence gets cached, not just "something goes wrong")
and gives it a real consequence (HOURS) instead of describing it as a
limitation in general terms.

## Evan Miller, "How Not To Sort By Average Rating"

Source: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

> "You are a web programmer. You have users. Your users rate stuff on your site. You want to put the highest-rated stuff at the top and lowest-rated at the bottom. You need some sort of "score" to sort by."

Checked: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html, retrieved 2026-09-26

Five short sentences, each adding exactly one fact, build the whole problem
before any solution is proposed. Nothing here is decorated — "You have
users" is a complete thought and gets a complete sentence, which is what
lets a reader with no background start from zero without feeling talked
down to.

> "The Wilson score confidence interval isn't just for sorting, of course. It is useful whenever you want to know with confidence what percentage of people took some sort of action."

Checked: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html, retrieved 2026-09-26

Having spent the piece on one use of the formula, he states the wider claim
in two plain sentences rather than building to it as a big reveal. "Of
course" concedes the obvious point quickly instead of dwelling on it, which
keeps the sentence moving toward the new information.

> "You will quickly see that the extra bit of math makes all the good stuff bubble up to the top. (But before running this SQL on a massive database, talk to your friendly neighborhood database administrator about proper use of indexes.)"

Checked: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html, retrieved 2026-09-26

"Bubble up to the top" is the one informal phrase in an otherwise exact
piece, earned because the sentence has already done the precise work and can
afford one loose image. The parenthetical aside is a specific, practical
caution ("proper use of indexes") rather than a vague gesture at things that
could go wrong.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "Embeddings are a really neat trick that often come wrapped in a pile of intimidating jargon. If you can make it through that jargon, they unlock powerful and exciting techniques that can be applied to all sorts of interesting problems."

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

He names the obstacle (jargon) before the payoff, so the reader knows the
difficulty is being acknowledged rather than hidden. "Neat trick" is a
specific, low-key claim — not "revolutionary" or "powerful" — that he then
earns with the sentence about what the trick unlocks.

> "The best way to think about this array of numbers is to imagine it as co-ordinates in a very weird multi-dimensional space."

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

One sentence, one image, doing one job: turning a list of numbers into
something locatable. "Weird" is doing real work here — he is telling the
reader the analogy is imperfect at the same moment he offers it, rather than
presenting it as a clean equivalence.

> "To OpenAI's credit, they did promise to "cover the financial cost of users re-embedding content with these new models."—but it's still a reason to be cautious about relying on proprietary models."

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

He gives the company its due in a direct quotation before stating his own
caution, so the caution reads as a considered judgment and not a complaint.
The qualification names a specific, checkable risk (relying on a proprietary
model) rather than a general unease about the technology.
