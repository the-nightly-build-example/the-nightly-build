# Commission: when-ai-breaks/chatgpt-defamation

## The incident

A deployed chatbot stated false, damaging facts about named real people, and the
courts were left to decide who answers for it. Center the lesson on Mark Walters
v. OpenAI, the first U.S. defamation suit over a chatbot's output: ChatGPT told a
journalist that Walters, a radio host, had been accused of embezzling from a gun-
rights group, complete with a fabricated lawsuit. A Georgia court ruled for
OpenAI in May 2025. Use the 2023 episodes as the pattern this case sits in: law
professor Jonathan Turley falsely named by ChatGPT as accused of harassment with
an invented Washington Post article, and Australian mayor Brian Hood, whom
ChatGPT described as a convict in a bribery case he had in fact exposed.

## What the lesson teaches

Tell it in order, from the record, then explain the mechanism and where the
weakness lives today.

1. What happened, named and dated. Who asked the chatbot what, what it asserted,
   who was harmed, and what each party did next: the complaint, the court's
   reasoning, and the outcome. Keep fact, allegation, and ruling distinct;
   Walters is decided, the others did not reach a verdict.
2. Why a chatbot asserts a confident false biography. The model predicts a
   plausible continuation; a defamatory but statistically ordinary sentence about
   a public-adjacent name is as easy to generate as a true one, and nothing
   checks it. The reader has the hallucination lesson; link it and do not
   re-teach the mechanism. Teach the piece that is specific here: why false claims
   about real, identifiable people are a distinct kind of harm.
3. The legal question the incident exposed. Defamation needs a false statement of
   fact, publication, fault, and (for a public figure) actual malice. Walters
   turned on whether a reasonable reader would take the output as a factual claim
   and on fault. Explain what the ruling decided and what it left open, plainly,
   without overclaiming a settled doctrine.
4. Where the same weakness lives today. Retrieval-less assistants still generate
   confident biographies of real people, now often with citations that do not
   exist. Tie to the present without hype.

## Distinct value, and boundaries

When AI Breaks already covers mata-v-avianca (a lawyer sanctioned for fake case
citations), deloitte-ai-report (fabricated citations in a paid report), and
air-canada-chatbot (a bot inventing a refund policy the airline had to honor).
This lesson is not another "the model made something up" piece: its subject is
defamation of a named real person and the unsettled question of civil liability
for an AI's false factual claims about people. Foreground that. Link the
hallucination mechanics lesson rather than re-explaining why models confabulate,
and do not reuse air-canada's heading shapes.

This is a sober, record-only treatment. Report from primary documents (court
filings, rulings, the people's own public statements, and reporting that held
up). Attribute contested claims as allegations. Name people and dates. No
sensationalism.

## Source obligations

Series floor, from `nb source-policy --series when-ai-breaks`: at least 8
sources, at least 4 primary and at least 1 secondary. Primary: the Walters v.
OpenAI complaint and the court's ruling/order (Gwinnett County / Georgia), the
contemporaneous primary accounts from Turley and Hood (Turley's own writing;
statements from Hood or his lawyers), and any OpenAI statement. Secondary:
reputable reporting that held up. Every quantity, date, title, and role checked
against the owning primary.

## Production policy

From `nb production-policy --series when-ai-breaks` (profile: balanced). Models
are the "capable" tier (not required); this run resolves "capable" to
claude-opus-4-8. Efforts: writing-coach low, researcher high, writer medium,
editor high. Harness: claude-code. Record the writer's actual model in nb-meta.

## Recent patterns to break (for writer and editor)

1. Dek: avoid the two-clause "claim, and/so the twist" mold and the comma-triad.
   The air-canada and mata deks both used the "when X did Y, a tribunal/judge
   did Z" shape; do not copy it.
2. Closing body heading: when-ai-breaks pieces close on a "the same setup is
   running right now" heading (air-canada: "The same setup is answering support
   questions right now"). Keep the where-it-lives-today content; build the
   heading differently.
3. Orientation heading is its own concrete step, not a paraphrase of the headline.
4. Furniture: nb-note and nb-stat-strip recur by reflex. A defamation piece may
   not need a stat strip at all; use only what the material calls for.

## Original contribution target

The reader should finish understanding why a chatbot can libel a real person as
easily as it can praise one, and exactly what a court has and has not decided
about who is liable.
