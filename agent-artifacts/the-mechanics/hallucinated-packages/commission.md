# Commission: the-mechanics/hallucinated-packages

## The behavior

Ask a coding assistant for code and it writes `import` lines for libraries that
do not exist: a plausible-sounding package name, confidently used, that is not in
any registry. Anyone who has coded with an AI assistant has hit this. The
Mechanics desk works backward from the behavior to what produces it, no code in
the lesson beyond the short illustrative token or name a claim depends on.

## What the lesson teaches

Work backward, step by step, marking settled engineering versus open question:

1. The model is predicting a package name as text. A library name is a token
   sequence like any other; the model continues the most likely next tokens for
   "a plausible import here," with no connection to a package index. Our reader
   met next-token prediction and the point that a model has no lookup step; link
   the hallucination lesson rather than re-teaching why models invent things.
2. The new ground: these inventions repeat. The distinct, counterintuitive fact
   is that the same nonexistent name recurs across runs and across prompts far
   more than random sampling would suggest. Teach why a low-entropy region of the
   name distribution produces the same confident guess again and again, and why
   that predictability is the whole danger. This is what separates this lesson
   from the general hallucination lesson: repeatability, not just invention.
3. Where the weakness lives today: slopsquatting. Because the hallucinated names
   are predictable, an attacker can register one as a real malicious package, and
   the next developer who pastes the assistant's import installs it. Name the
   research and any real-world proof-of-concept. This is the step that makes the
   behavior matter.
4. What fixes it and what does not. Grounding the assistant in a real registry
   (tool use / retrieval) removes most of the inventing; link those lessons.
   Mark what is settled (why it happens) and what is open (how far it can be
   driven down, measured rates across languages/models).

## Distinct value, and boundaries

The course covers hallucination (fabricated facts and citations, and the grading
incentive), tool-use, and retrieval. This lesson is not "hallucination again": it
owns the repeatability of invented identifiers and the supply-chain attack that
repeatability enables. Link hallucination for the base mechanism and do not
re-teach it; spend the lesson on what that lesson did not cover. No live
malicious instructions or working exploit code; the attack is explained, not
demonstrated.

## Source obligations

Series floor, from `nb source-policy --series the-mechanics`: at least 8 sources,
at least 4 primary and at least 1 secondary. Primary: the academic package-
hallucination study or studies (e.g., Spracklen et al., "We Have a Package for
You!" / package-confusion work, 2024-2025) for the rates and the repeatability
finding; the security-firm disclosures that coined or popularized "slopsquatting"
(e.g., Socket, Lasso, Trend Micro, or the researcher who named it); any registry
or vendor advisory; and a documented real malicious-upload case if one exists.
Take every rate from its owning primary and give its denominator.

## Production policy

From `nb production-policy --series the-mechanics` (profile: balanced). Models are
the "capable" tier (not required); this run resolves "capable" to
claude-opus-4-8. Efforts: writing-coach low, researcher high, writer medium,
editor high. Harness: claude-code. Record the writer's actual model in nb-meta.

## Recent patterns to break (for writer and editor)

1. Dek: avoid the two-clause "claim, and/so the twist" mold, the comma-triad, and
   the "The [thing] that..." opener.
2. Closing body heading: recent mechanics pieces end on a terse limit/verdict
   heading ("A self-report is no proof of who built it," "Hand it the source, and
   the inventing mostly stops" as a section closer-idea). Keep the "where it lives
   today / what fixes it" content; vary the heading's build.
3. Orientation heading is its own concrete step, not a paraphrase of the headline.
4. Furniture: nb-note and nb-table recur by reflex. A table of hallucination rates
   by ecosystem could be genuine; an nb-note is not owed. Earn each.

## Original contribution target

The reader should be able to explain why a coding assistant invents a library,
why the same fake library keeps coming back, and why that repeatability turns a
nuisance into an attack they can actually guard against.
