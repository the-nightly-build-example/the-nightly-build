# Commission: what-could-go-wrong/lethal-trifecta

## The argument

An AI agent becomes dangerous to its own user when three things are true at once:
it can read private data, it is exposed to untrusted content it did not write, and
it can communicate to the outside world. Under those conditions an instruction
hidden in the untrusted content can hijack the agent into exfiltrating the private
data. Simon Willison named this combination the "lethal trifecta" in 2025, pulling
together a string of demonstrated attacks on shipping products. What Could Go
Wrong teaches the argument on its merits.

## What the lesson teaches

Follow the desk's arc.

1. The argument at full strength. Who named it and what they had seen: Willison
   and the security researchers behind the concrete exploits. Lay out the
   reasoning its careful defender would: a language model draws no firm line
   between instructions and data (our reader has that lesson; link
   the-mechanics/instructions-are-data), so once an agent has tools and reads
   attacker-controlled text, the attacker can borrow the agent's permissions.
2. Test it against what real systems actually do. This argument's strength is
   that the dangerous part is already shown, not speculated. Walk the documented
   2025 cases: the Microsoft 365 Copilot "EchoLeak" zero-click data-exfiltration
   vulnerability, the ChatGPT connectors / Google Drive and GitHub-MCP
   exfiltration demonstrations, and similar. Draw the sharp line the beat
   requires: what has been demonstrated on a working system (data pulled out via
   injected text) versus what is still extrapolation (autonomous agents causing
   open-ended catastrophe). Be precise about which demos were researcher
   proof-of-concept and which were exploited in the wild.
3. Bring it to the present. Who makes the argument now and what they want done:
   the trifecta framing says you cannot reliably patch prompt injection, so the
   mitigation is to deny one leg of the trifecta (cut private-data access, or
   untrusted input, or exfiltration channels). Check it against the most recent
   evidence and name the gap where confidence outruns proof, in either direction:
   vendors who claim a classifier fixes it, and doom that treats every agent as
   already compromised.

Name no company as an authority. Work from the vulnerability disclosures and the
demonstrations themselves, not commentary about them; Willison's posts are the
origin of the framing and may be cited as that, but the exploits are the evidence.

## Distinct value, and boundaries

The course covers jailbreaks (bypassing content policy), instructions-are-data
(the mechanism, in Mechanics), ai-control (overseeing a scheming model), and
data-poisoning (training-time). This lesson owns a different failure surface: a
deployed agent with tool access exfiltrating private data via injected
instructions at inference time. It is a security/misuse argument, not an
alignment argument, and it must not drift into "the model wants to betray you."
Link instructions-are-data for the mechanism; do not re-teach it.

## Source obligations

Series floor, from `nb source-policy --series what-could-go-wrong`: at least 8
sources, at least 4 primary and at least 1 secondary. Primary: the CVE/advisory
and technical writeups for EchoLeak and the other named exploits, the security
researchers' own demonstration posts, and vendor advisories. Willison's
"lethal trifecta" post for the framing. Every exploit claim needs its owning
primary; an accusation that a product was vulnerable needs the disclosure, not a
retweet.

## Production policy

From `nb production-policy --series what-could-go-wrong` (profile: balanced).
Models are the "capable" tier (not required); this run resolves "capable" to
claude-opus-4-8. Efforts: writing-coach low, researcher high, writer medium,
editor high. Harness: claude-code. Record the writer's actual model in nb-meta.

## Recent patterns to break (for writer and editor)

1. Dek: avoid the two-clause "claim, and/so the twist" mold, the comma-triad,
   and the "The [thing] that..." opener. The recent wcgw deks ("Its authors admit
   they can't yet show how the loop closes, and the starkest real cases...")
   lean on the comma-and twist; build this one differently.
2. Closing body heading: recent wcgw pieces close on a "the confidence outruns the
   proof" verdict heading ("The doom and the dismissal both outrun the evidence,"
   "The reassurances run out where it would matter most"). Keep the required
   present/gap content; do not stamp the heading to that mold.
3. Orientation heading is its own concrete step, not a paraphrase of the headline.
4. Furniture: nb-note, nb-stat-strip recur by reflex; a holds-up grid
   (nb-holdsup) or position card fits a for/against argument if the material wants
   it. Earn each; do not stack blocks.

## Safety note

Explain the attack pattern and mitigations; do not include working injection
payloads or step-by-step exploit instructions. The teaching is the threat model,
not a recipe.

## Original contribution target

The reader should be able to tell, for any AI agent they are handed, whether it
has all three legs of the trifecta, and to separate the part of the worry that is
already demonstrated from the part that is still forecast.
