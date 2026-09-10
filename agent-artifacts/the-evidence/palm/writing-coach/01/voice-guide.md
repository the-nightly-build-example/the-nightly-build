# Voice guide: the-evidence/palm

## How this piece should sound

This lesson reads one document, the PaLM paper, the way Piper reads the
deworming study for Vox: give the finding in the researchers' own numbers
before saying what to think of it, and let a disagreement stand in each
side's own terms rather than paraphrasing it into "critics say." Piper
reports the 37 percent annualized return, in the researchers' own framing,
before she calls it eye-popping. PaLM's own headline numbers, whether that is
the parameter count, the token count, or whatever exact MFU figure the
researcher supplies, call for the same order: the figure first, then the
number that tells the reader whether it is large or small. The
Chinchilla-implied token count for a model PaLM's size is that second number,
and putting it beside PaLM's actual token count is what turns "undertrained"
from a label into something a reader can check.

The paper's claims and their later correction can stand the way Aiken and
Davey's reanalysis stands next to Miguel and Kremer's defense in Piper's
piece: each side named and given its own sentence before the piece weighs
them. PaLM's emergent-abilities claim on BIG-bench, and the "Are Emergent
Abilities a Mirage?" rebuttal, are this lesson's version of that same shape.
The original finding comes first, in the paper's own terms, then the
challenge to it, named, before any verdict.

Where a piece of PaLM's own vocabulary needs unpacking on first use, whether
that is breakthrough, discontinuous, or compute-optimal, Evans's habit of
catching a misleading term and replacing it mid-sentence with the mechanism
underneath it is the right move. The correction lands inside the
explanation, not as a separate aside afterward. And where a rule would
otherwise stay abstract, Evans doesn't just state the caching TTL rule. She
runs it against her own domain and shows the number it produces. The
Chinchilla ratio can get the same treatment against PaLM's own token count:
run the two numbers together on the page rather than asserting the shortfall
and moving on.

Lee and Trott's habit of walking one real case all the way through before
generalizing suits whichever section of this lesson sits with one piece of
PaLM's own method, whether that's the Pathways engineering or a
chain-of-thought result, before moving to the next: a specific research
team, a specific sentence, a specific wrong word the model could have
predicted, ending in one plain sentence a reader can check against the
example. And where this lesson introduces a term the reader hasn't met
before (compute-optimal, if Background doesn't already cover it), their
habit of returning to an analogy more than once, adding one comparison at a
time, beats stating the term once and trusting it to stick.

The lesson can close on what the commission already asks for: where today's
citations of PaLM outrun what the paper showed. That is a plain claim about a
gap, not a verdict dressed up as one. Piper's debate section is the model
for leaving it there. The reanalysis and the defense both get their own
sentence, and the piece never resolves into a tidier answer than the
evidence supports.

## Kelsey Piper, "A new study finds that giving kids deworming treatment still benefits them 20 years later"

Source: https://www.vox.com/future-perfect/2020/8/6/21354847/kremer-miguel-worms-deworming

> "Individuals who received deworming as children experience substantial increases in adult consumption, hourly earnings, nonagricultural employment, and urban residence," the study concludes. The effects on income and spending are slightly smaller than those observed in a follow-up at the 10-year mark, but they're very notable nonetheless. An extra two or three years of deworming treatments in school translates to 13 percent higher hourly earnings, 14 percent higher consumer spending, and significantly increased odds of working outside of agriculture (in jobs that largely pay better and offer more opportunity for growth). The researchers calculate that the investment in deworming Kenya's children has so far had a 37 percent annualized rate of return.

Piper states the study's own number before offering any judgment of it. The
13, 14, and 37 percent figures come straight from the researchers'
calculation, in the units the researchers used (hourly earnings, consumer
spending, annualized return), not a rounded stand-in for them.

> The results are certainly eye-popping. Most global poverty interventions, even if they work, don't produce a 37 percent annualized rate of return that lasts decades (which is perhaps one reason for skepticism about the findings). It's very rare to do anything in public policy that still has significant effects 20 years later — let alone effects this large.

Only after giving the number does Piper say what she thinks of it, and she
measures it against something a reader already has some feel for: how most
global poverty interventions perform, and how rarely any policy effect lasts
two decades. The parenthetical naming a reason for skepticism is hers, and
she states it as a reason rather than a hedge.

> In 2015, British epidemiologists Alexander Aiken and Calum Davey published a reanalysis of the data from the original Kenya schools and argued that when the data was properly analyzed, "we found little evidence for some previously-reported indirect effects of a deworming intervention. Effects on worm infections, nutritional status, examination performance and school attendance on children in intervention schools were largely unchanged." Other researchers pushed back. Sure, the first worm study wasn't perfect — its school assignments were not quite perfectly random, there were no placebos (meaning students could have behaved differently because they knew they were in the treatment group), and there were some genuine errors in the paper. But its core result was very robust.

Piper lets each side of the dispute speak in its own terms: Aiken and
Davey's finding, quoted directly, then the specific weaknesses of the
original study named one by one before she reports that its core result held
up anyway. Neither side is smoothed into "critics say" or "researchers
argue."

## Julia Evans, "DNS 'propagation' is actually caches expiring"

Source: https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/

> When you make a DNS request (for example when you type google.com in your browser), you make a request to a DNS resolver, like 8.8.8.8. When you create a DNS record for a domain, you set the DNS record on an authoritative nameserver.

Evans introduces each new term, DNS resolver and then authoritative
nameserver, at the exact sentence where the reader first needs it, tied to
something the reader has actually done (typing a URL into a browser).
Nothing is defined before there's a reason to want it defined.

> But when you update a DNS record, it is slow! So why is that, if records don't need time to get pushed out? Well, DNS resolvers like 8.8.8.8 cache DNS records. And if those cached records are still valid, they'll never request a new record! So a DNS update doesn't fully take effect until all cached versions of that record have expired. When people say "we're waiting for DNS to propagate", what they actually mean is "we're waiting for cached records to expire".

She names the misleading industry phrase and replaces it, in the same
paragraph, with the mechanism underneath it. The correction happens inside
the explanation rather than as a separate aside tacked on afterward.

> Let's see what that is for subdomains of jvns.ca:
>
> $ dig soa jvns.ca
> jvns.ca. 3600 IN SOA art.ns.cloudflare.com. dns.cloudflare.com. 2264245811 10000 2400 604800 3600
>
> It's the minimum of the SOA TTL (3600) and the last number in the SOA record's value (3600). So negative caching will happen for an hour. And sure enough, the last time I caused this problem for myself, I waited an hour and everything worked! Hooray!

Evans doesn't state the caching rule and move on. She runs an actual command
against her own domain, shows the number the rule produces, and checks it
against what she'd already seen happen. The abstraction only appears once a
real instance of it exists on the page.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> Washington DC is located at 38.9 degrees North and 77 degrees West. We can represent this using a vector notation: Washington DC is at [38.9, 77] New York is at [40.7, 74] London is at [51.5, 0.1] Paris is at [48.9, -2.4] This is useful for reasoning about spatial relationships. You can tell New York is close to Washington DC because 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close to London. But Paris is far from Washington DC.

The vector explanation runs on one analogy, city coordinates, held open
through four cities and three separate comparisons rather than stated once
and left behind. Each comparison (New York to Washington, Paris to London,
Paris away from Washington) does a little more work than the last.

> Last year scientists at Redwood Research studied how GPT-2, a predecessor to ChatGPT, predicted the next word for the passage "When Mary and John went to the store, John gave a drink to." GPT-2 predicted that the next word was Mary. The researchers found that three types of attention heads contributed to this prediction: [...] In short, these nine attention heads enabled GPT-2 to figure out that "John gave a drink to John" doesn't make sense and choose "John gave a drink to Mary" instead.

The passage follows one real experiment (a named research group, one exact
sentence, one wrong word the model could have predicted instead) through to
a plain closing sentence a reader can check against the example. The finding
isn't asserted first and illustrated after. The walk-through produces the
finding.

> Here's an analogy to illustrate how this works. Suppose you're going to take a shower, and you want the temperature to be just right: not too hot, and not too cold. You've never used this faucet before, so you point the knob to a random direction and feel the temperature of the water. If it's too hot, you turn it one way; if it's too cold, you turn it the other way. The closer you get to the right temperature, the smaller the adjustments you make.

Backpropagation gets an analogy instead of a formula, built the same
incremental way as the vector analogy: one adjustment, then a rule for which
direction to turn next, before the technical term for any of it shows up.
The plain version earns the term rather than standing in for it.

Production record: run as Claude Sonnet 5 (claude-sonnet-5), effort low
(policy: writing-coach, model capable, effort low).
