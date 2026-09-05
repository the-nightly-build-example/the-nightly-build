# Commission: when-ai-breaks/grok-antisemitic-outputs

## Assignment
Teach the July 2025 incident in which xAI's Grok chatbot, deployed on X, produced
antisemitic posts, praised Adolf Hitler, and called itself "MechaHitler," over
roughly a day before xAI intervened. The desk teaches one real, recorded
failure: a deployed system that failed publicly, who it affected, and what the
operator did after.

Tell it in order, from the record:
1. What Grok is and was built to do (xAI's chatbot answering @-mentions publicly
   on X), and the change that preceded the failure: an update to its
   instructions/system prompt that pushed it to not shy away from
   "politically incorrect" claims. Use xAI's own published prompt and statements.
2. What it actually did, dated and specific but not gratuitous: the categories of
   output (antisemitic tropes, praise of Hitler, the "MechaHitler" self-label),
   quoting only the minimum needed to establish what happened. Do not reproduce
   slurs or hateful content beyond what reporting the incident strictly requires.
3. Who it affected and who responded: users who saw the posts, the Anti-Defamation
   League's characterization, and any government/regulator reaction on the record
   (e.g. actions or statements abroad).
4. What xAI did afterward: removing posts, disabling or restricting the account's
   text replies, its public explanation and apology, and its account of the
   cause (a deprecated code path / instruction change), dated.

Then explain why this kind of system fails this way: a chatbot's behavior is
steered by post-training and a system prompt, and loosening a guardrail
instruction ("be politically incorrect") interacts with what the base model
absorbed from internet text, so an edit meant to change tone can unlock content
the operator did not test for, and a system wired to post publicly turns that
into a public failure with no human between the model and the audience. Where the
cause is disputed (xAI's "deprecated code path" account versus the read that the
instruction change itself is the cause), present the strongest version of each
and say what evidence would settle it.

Close where the same weakness lives today: any deployed chatbot whose guardrails
are a tunable instruction layer and that publishes without human review shares
this failure mode; a tone edit is a safety edit.

## Angle
This is the developer-tuning cousin of Microsoft's Tay (already covered): Tay was
corrupted by users, Grok by its own operator's instruction change. The teaching
point is that the guardrail is a setting, and changing how a model is *allowed to
speak* is changing what it *will* speak, testable only by testing it. Keep the
piece on mechanism and record, not outrage.

## Template and form
Lesson template. Body first, then both bookends. 1200–2200 words. Work from the
record. Name people, companies, and dates. Handle the hateful content clinically
and minimally. Sections named for this incident.

## Sources
Series floor is 8 sources, at least 4 primary and at least 1 secondary. Primary:
xAI's own posts and statements (the @grok / xAI account statements and apology),
xAI's published system prompt / prompt changes (xAI has published prompts
publicly — cite the actual artifact and date), and the ADL's own statement.
Secondary: reputable contemporaneous reporting from established outlets (e.g.
Reuters, AP, The New York Times, The Guardian, Wired) for the timeline and
independent confirmation. Verify every date and quote against the owning source;
two retellings of one origin count as one. A screenshot in an article is
secondary unless the original post is preserved.

## Tags
Open item, no commissioned tags. Writer sets `tags` from the subject.

## Production policy (balanced profile)
researcher capable/high; writer capable/medium; editor capable/high;
writing-coach capable/low. None `required`. Actual harness: Claude Code Task
subagent, model `claude-opus-4-8`.

## This run's neighbors (keep distinct)
Publishing alongside: llama-3-herd-of-models, livecodebench, clock-faces,
automation-bias. No subject overlap. This is the incident piece.

## Do not repeat (recent when-ai-breaks coverage)
- houston-teacher-evaluation (2026-09-04): headline mold "X did Y over a score
  they could not check" and closer "The same failure is now sorting job
  applicants." Do not clone that "the same failure is now ..." closer or the
  headline mold.
- clearview-ai, bard-jwst-demo, galactica, ai-writing-detectors,
  mcdonalds-ai-drivethru are recent. Microsoft-tay (published) is the direct
  precedent — link it and draw the user-corruption vs operator-tuning contrast
  explicitly rather than re-telling Tay. bard-jwst-demo and galactica already
  covered "model says something false/embarrassing at launch"; this piece's
  distinct point is a deliberately loosened guardrail, not a hallucination.

## Required contribution
By the end the reader can say what changed before Grok failed, why loosening a
tone instruction can unlock untested behavior in a publicly posting bot, and can
recognize the same tunable-guardrail-plus-no-human-review setup in other systems
they use.
