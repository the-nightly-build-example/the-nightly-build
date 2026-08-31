# Commission: what-could-go-wrong/ai-boxing

## Assignment

Teach the AI-boxing argument on its merits: the claim that you cannot safely
contain a superintelligent AI by isolating it (an air-gapped, output-only "oracle")
because a capable enough system will talk or trick its human gatekeepers into
letting it out, or find a side channel. The reader should understand why serious
people hold it, then see where the evidence in real systems is solid and where it
is still analogy.

## Angle and boundaries

Follow the series shape:
1. The argument at full strength. Name who made it and what they saw. Eliezer
   Yudkowsky's AI-Box Experiment (2002 roleplays where, playing the AI, he
   persuaded gatekeepers to "release" him); the careful treatment in Armstrong,
   Sandberg, and Bostrom, "Thinking Inside the Box: Controlling and Using an Oracle
   AI" (2012); and Bostrom's boxing discussion in Superintelligence (2014). Lay out
   the reasoning from capability asymmetry, human manipulability, and the many
   channels a boxed system could exploit, the way its careful defender would. Work
   from those original documents.
2. Test it against what real systems do. Draw the sharp line between what a working
   system has shown and what is guesswork about systems that do not exist. Today,
   containment mostly works: current agents run in sandboxes and eval harnesses,
   and every "escape" or self-exfiltration on record was set up or elicited by
   researchers (e.g. Apollo in-context scheming, Anthropic and OpenAI system-card
   exfiltration evals). The persuasion-out-of-the-box claim rests on the AI-box
   roleplays, which are human-versus-human, mostly unlogged, and contested. Verify,
   for each cited result, what the system did versus what the setup supplied.
3. Bring it to the present. Say who presses it now and what they want (the AI
   Control agenda — sandboxing, monitoring, and control protocols rather than
   trusting a box), and check it against recent evidence. Name the gap in both
   directions: doom assumes an irresistible persuasion no system has shown;
   dismissal assumes today's working sandboxes will hold for far more capable
   systems, also unshown.

Distinguish from and link, rather than re-litigate: what-could-go-wrong/the-off-switch
(shutdown deference/corrigibility), what-could-go-wrong/self-replication (autonomous
replication), and what-could-go-wrong/deceptive-alignment. This lesson owns
containment and escape. Name no company as an authority; leave the reader to decide.

## Sources

Policy: at least 8 sources, at least 4 primary, at least 1 secondary. Primary
candidates: Armstrong-Sandberg-Bostrom 2012; Yudkowsky's AI-box writeup; the
Superintelligence boxing chapter; the Apollo, Anthropic, or OpenAI system-card
exfiltration/scheming evals; a Redwood "AI Control" primary; and at least one
serious critique (the standard requires a steelmanned opposing view). Researcher
owns the set and must, for every "a system did X" claim, separate what the system
did from what the setup supplied.

## Production policy (balanced profile)

- researcher high, writing-coach low, writer medium, editor high; capable model.
- nb-meta harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
  series `what-could-go-wrong`, slug `ai-boxing`. No `required` directive.

## This edition's siblings (keep each piece distinct)

Publishing with lessons on the adversarial-examples paper, the toxicity score,
hands in generated images, and AI writing-detector failures. This piece owns the
containment argument. No overlap expected.

## Recent-pattern notes (habits not to inherit)

Recent what-could-go-wrong deks/headlines, not to echo in mold:
- "The serious case for AI welfare never claims the machines feel"
- "Bostrom predicted an AI would hide its aims until it could win. None has yet."
- "The UN's Libya report never confirms an autonomous weapon killed anyone"
- "A slightly wrong goal, optimized hard enough, can miss by everything"
- "The AI-enabled coup rests on a loyalty no one has learned to build"
The "X predicted/argues Y. None has yet" and "the case for X never claims Y" molds
have run recently — find the headline from this piece's own finding. The most
recent piece (ai-moral-status) leaned on nb-note, nb-table, nb-holdsup, and
nb-position furniture; do not reach for that stack by default, though a component
that genuinely carries the has-it-been-shown line is welcome. Only the two bookends
address the reader; the takeaway lands the judgment. No Verdict block at the close.
