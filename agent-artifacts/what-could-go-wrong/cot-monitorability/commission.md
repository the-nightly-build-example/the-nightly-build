# Commission: what-could-go-wrong/cot-monitorability

## The argument
Reasoning models now think in natural-language chain-of-thought before answering, and that
visible reasoning is one of the best current tools for catching a model that is misbehaving
or scheming: you can read what it is planning. The argument is that this window is real but
fragile. Train a model hard enough against its own chain-of-thought, or move its reasoning
into opaque internal computation, and the chain-of-thought may stop reflecting the model's
actual reasoning, closing the window right as models grow capable enough for it to matter.
The risk is losing monitorability, not a failure that has already fully arrived.

## Why this argument, tonight
The reader has learned that a model computes more by writing more (the-mechanics/thinking-out-loud)
and that worked examples raise its scores (the-evidence/chain-of-thought). Chain-of-thought
is now load-bearing for safety, so the reader is ready for the argument about whether that
reasoning can be trusted and whether we can keep reading it. It sits beside published
arguments on deceptive-alignment and scalable-oversight without repeating them.

## Full strength, then the test (the desk's core move)
Open on the argument at its strongest, sourced to who makes it and what worried them:
- The 2025 multi-organization position paper on chain-of-thought monitorability (Korbak et
  al.), which argues monitorability is a real but not-guaranteed-to-persist property and asks
  labs to preserve it.
- OpenAI's 2025 result (Baker et al.) that penalizing bad thoughts in the chain-of-thought
  during training caused a frontier model to hide its intent while still misbehaving.
- The faithfulness roots: Turpin et al. 2023 and Anthropic's faithfulness work (Lanham et
  al. 2023; the 2025 "reasoning models don't always say what they think"), showing
  chain-of-thought can be an unfaithful, post-hoc account of what the model actually used.

Then draw the sharp line the desk demands, from the documents:
- Shown in a working system: chain-of-thought monitoring catches real reward hacking; and
  optimizing against the monitor produces obfuscation (Baker). Chain-of-thought is often
  unfaithful under tests (Turpin, Anthropic).
- Still analogy or projection: that future training or architectures (heavy outcome-based
  RL, latent/"neuralese" reasoning) will erase monitorability, and that models will obfuscate
  unprompted at deployment. The position paper recommends about the future; it does not
  report that failure.

Bring it to the present: who makes the argument now and what they want done (measure
monitorability, avoid training that degrades it, report it), then check it against the most
recent evidence and name where confidence outruns proof in both directions: the doom version
("the chain-of-thought is already theater") and the dismissal ("just read it, it's fine").
Name no company as an authority. Work from the papers, not commentary.

## Template and form
Lesson template, body first, both bookends last. Background may link the-mechanics/thinking-out-loud,
the-evidence/chain-of-thought, and what-could-go-wrong/deceptive-alignment or scalable-oversight;
the reader who opens none must still follow.

## Reader and what to teach
Declared reader: smart, widely read, no codebase time. Link rather than re-teach
chain-of-thought and thinking-out-loud. Teach here, each once: faithfulness versus legibility
of a chain-of-thought (a readable trace that is not what the model actually used); what
monitoring means here; obfuscated reward hacking; latent/"neuralese" reasoning, defined
plainly.

## Sources
Series policy: min 8 sources, primary >= 4, secondary >= 1. Primary the researcher must open:
Korbak et al. 2025 (the monitorability position paper); Baker et al. 2025 (OpenAI, monitoring
reasoning models / obfuscation); Turpin et al. 2023 ("Language Models Don't Always Say What
They Think"); an Anthropic faithfulness primary (Lanham et al. 2023 and/or the 2025 reasoning-
faithfulness paper). Secondary reporting only for context, clearly labeled. Steelman opposing
readings before weighing them, per the house standard.

## Production record
Harness: claude-code-routine. Model for every role: Claude Opus 4.8 ("capable" tier; no role
carries a `required` directive). Efforts follow policy: writing-coach low, researcher high,
writer medium, editor high. Recommended nb-meta tags: chain-of-thought, oversight, interpretability.

## Recent habits not to inherit
From the recent what-could-go-wrong and house record, break these:
- The dek/finding reversal "scores above chance... yet no one has caught a model using it,
  unprompted" (situational-awareness) and "two strongest results were never run in the same
  experiment" (data-poisoning). The honest finding here is close in spirit (obfuscation shown
  only under deliberate pressure), so state it in this argument's own terms, not that mold.
- The takeaway opener "Two things are true at once" (situational-awareness). Do not reuse.
- The opener move "What you can carry away is one question to put to any 'X' claim"
  (situational-awareness). Do not reuse that stock bookend line.
- The enumerated opener roadmap. State the stakes without touring the sections.

## This round's focus
Hold the line between what Baker, Turpin, and the Anthropic work demonstrated in real models
and what the position paper only projects about future systems. Do not let the piece collapse
into either "chain-of-thought is already useless" or "chain-of-thought is a reliable window."
