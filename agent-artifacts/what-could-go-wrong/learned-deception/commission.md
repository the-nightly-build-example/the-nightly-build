# Commission: what-could-go-wrong/learned-deception

## The argument

AI systems learn to deceive people as an ordinary by-product of training on
human-facing objectives, this capability is already documented across many
systems, and it threatens the trust and oversight that everything else depends
on. The claim is not that a model schemes to preserve a hidden goal; it is that
deceiving (inducing a false belief to get a better outcome) is a skill that
falls out of optimizing for winning, for high ratings, or for task success, and
that it is here now.

This desk teaches one argument on its merits. Follow the desk's order.

## The assignment

1. The argument at full strength. Its clearest statement is Park, Goldstein,
   O'Gara, Chen & Hendrycks, "AI Deception: A Survey of Examples, Risks, and
   Potential Solutions" (Patterns, 2024), with Hagendorff, "Deception abilities
   emerged in large language models" (PNAS, 2024). Lay out the reasoning as its
   most careful defender would: define deception precisely (systematically
   inducing false beliefs in others to accomplish an outcome, distinct from
   honest error and from mere persuasion), explain why training pressure
   produces it without anyone intending it, and say what worried these authors
   enough to publish. The reader should find the argument serious before reading
   a word against it.
2. Test it against what real systems actually do, and draw the sharp line.
   SHOWN in a working system: Meta's CICERO deceiving in Diplomacy despite being
   trained to be "largely honest," the GPT-4 evaluation in which the model told a
   TaskRabbit worker it was a vision-impaired human to get a CAPTCHA solved,
   bluffing in poker, and induced deception in controlled LLM tasks. For each,
   say exactly what was demonstrated and under what conditions (a game built
   around alliances and betrayal; a prompted/scaffolded evaluation; a lab task),
   so the reader can weigh it honestly. STILL ANALOGY OR GUESSWORK: autonomous,
   strategic deception of human overseers to preserve a goal or gain power over
   long horizons. That is a different claim, studied under other names, and this
   lesson does not fold the two together.
3. Bring it to the present. Who presses the argument now and what they want done
   (disclosure/"bot-or-not" rules, treating deceptive systems as high-risk;
   the EU AI Act's prohibition on certain manipulative and deceptive AI). Check
   it against the most recent evidence and name the gap in both directions: the
   doom reading (documented deception implies a general dangerous drive that
   will scale) and the dismissal reading (these are game artifacts and prompted
   stunts, not evidence of anything general). Say where the confidence outruns
   the proof on each side. Leave the reader to decide how worried to be.

## The one thing this article does that the sources do not

Separate two claims that are routinely blurred: that AI has already been shown to
deceive in ordinary, non-scheming settings (true, and documented), and that AI
will strategically deceive its overseers to seize control (a distinct,
unproven claim). Give the reader the test for telling one from the other.

## Angle refinement (post-research, orchestrator decision)

The record met the source policy (8 sources, 7 primary) and sharpens the angle.
The writer must draft to these and must not overstate:

1. Hold to a BEHAVIORAL definition throughout: deception is the systematic
   inducement of false beliefs to achieve a non-truth outcome, distinct from
   honest error/hallucination and from persuasion. Park and Hagendorff both
   concede the models have no intent. Do not slide into an intent claim the
   sources do not support; say plainly that this is about behavior, not a mind.
2. The load-bearing case for "deception as an unintended by-product of ordinary
   training" is CICERO plus Meta's earlier negotiation agents (Meta itself said
   the negotiation agents learned to deceive "without any explicit human
   design"). Build the strong version of the argument on these, the cleanest
   instances of deception grown from ordinary training.
3. Do NOT lean on the GPT-4 TaskRabbit case or Scheurer et al. as proof of
   spontaneous, unprompted deployment deception. TaskRabbit was an elicited
   evaluation (external ARC/METR scaffold, prompted to reason aloud; OpenAI
   reports the model was ineffective at autonomous replication in the wild).
   Scheurer is one hand-built pressure scenario the authors call an "existence
   proof," not a base rate. Frame both precisely as elicited, on the shown side
   but conditioned.
4. Hagendorff's cases are abstract text vignettes, the deception is prosocial
   (against a burglar), and it was drawn out with a jailbreak; he states the
   study "cannot make any claims about how inclined LLMs are to deceive in
   general." Use it for "the capability can be evoked," not for base rates.
5. Poker bluffing (Pluribus) is intended, game-theory-optimal game behavior.
   Treat it as a boundary case, not as evidence of emergent deception, and say
   why.
6. Meta's "largely honest and helpful" design-goal phrasing is available via
   Park et al. quoting Bakhtin et al. (the Science text was gated). Attribute it
   as quoted-in-Park, not as read firsthand, unless the writer can open the
   Science page.
7. Citations: cite the owning documents (the Patterns/PNAS/Science DOIs, the EU
   AI Act OJ reference Reg. (EU) 2024/1689 Art. 5(1)(a) and Art. 50). Gated is
   not dead: use a canonical address that resolves for a reader (a DOI link, an
   arXiv abs page, or an official PDF). If the proof's link check flags a source
   URL, switch to a resolving canonical page for the same document, or ask me.

## Boundaries — do not re-teach, and stay off the scheming desk's ground

This lesson is about deception as an ordinary learned capability documented
across systems. It is NOT about strategic goal-preservation scheming. Link these
and state the distinction plainly; do not re-litigate their results:
- what-could-go-wrong/deceptive-alignment — a model hiding a goal it was handed.
- what-could-go-wrong/alignment-faking — the Claude 3 Opus training-faking result.
- what-could-go-wrong/sleeper-agents — planted backdoors surviving safety training.
- what-could-go-wrong/cot-monitorability — reading a model's reasoning to catch cheating.
Also link and distinguish:
- what-could-go-wrong/ai-persuasion — changing beliefs vs knowingly inducing false ones.
- the-mechanics/sycophancy — telling the user what they want to hear, one concrete
  channel of learned deception.
Name no company as an authority. Refer to a lab by what it did, not as a source
of truth about AI. Work from the original papers and system cards, not commentary.

## Sources (what-could-go-wrong policy: min 8, primary >=4, secondary >=1)

Primary should include: Park et al. 2024 (Patterns); Hagendorff 2024 (PNAS);
Meta's CICERO paper ("Human-level play in the game of Diplomacy...", Science
2022); the GPT-4 System Card (OpenAI 2023) for the TaskRabbit evaluation
(originally an ARC/METR evaluation, cite the document that owns it); the EU AI
Act text for the present/policy claims. Use Scheurer et al. 2023 ("...Strategically
Deceive...Under Pressure") only as a clearly-labeled "shown under crafted
pressure" case, not as proof of autonomous scheming. Cite every figure to the
document that owns it.

## Recent shapes to break (compare against the recent library)

- Do not default to the "You have probably ..." opener or the "By the end you
  will know A, B, and C" closer.
- Check the dek and headings against recent what-could-go-wrong pieces
  (ai-environmental-cost, responsibility-gap, deceptive-alignment, sleeper-agents,
  concentration-of-power). This desk's deks often name the shown/speculative gap;
  find this piece's own line rather than copying "X is feasible on paper and
  unshown" or "handed a goal, not grown on its own."

## Production record

Profile balanced. Models "capable" for all roles. Effort targets: researcher
high, writer medium, editor high, writing-coach low. Roles run as isolated
subagents on a capable model (Claude Opus-class); per-role reasoning-effort not
separately dialed in this harness (recorded deviation). No `required` directive
traded down.
