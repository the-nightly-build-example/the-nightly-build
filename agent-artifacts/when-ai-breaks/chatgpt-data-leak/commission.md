# Commission: when-ai-breaks/chatgpt-data-leak

## Assignment

Tell the March 20, 2023 ChatGPT data exposure: for a window that day, some users
saw other users' chat titles in their history sidebar, and a subset of ChatGPT
Plus subscribers had personal and partial payment information exposed to other
users. OpenAI took ChatGPT offline, investigated, and published a postmortem
tracing the bug to the open-source Redis client library it used. Days later
Italy's data-protection authority, the Garante, ordered a temporary halt to
ChatGPT in Italy, citing this breach among other concerns.

This is a lesson on When AI Breaks. Tell what happened in order: what the system
was built to do, what it actually did, who it affected, and what the operator did
afterward. Name the people, the companies, and the dates. Then explain why that
kind of system fails that way — teach the caching-and-concurrency mechanism on
the spot. Close where the same weakness lives today, in services the reader
actually uses. Work only from the record: OpenAI's postmortem, the open-source
bug report and its fix, the regulator's order, and the reporting that held up.

## The gap this closes

Every ChatGPT incident the library covers is about the model — `when-ai-breaks/
chatgpt-defamation` (a hallucinated accusation), `gpt-4o-sycophancy` (a behavior
regression), `grok-antisemitic-outputs` (a prompt change). This one is not about
the model at all. It is an ordinary software bug in the plumbing around the
model, turned by scale into a privacy breach and then into a data-protection
case. That is the distinct lesson: an AI product carries the whole conventional
failure surface of any high-traffic web service, and regulators now treat these
as data-protection events.

## Required contribution

Leave the reader with two things they can carry:

- **The mechanism, taught plainly.** How a bug in request handling — a cancelled
  request and a pooled/cached connection returning another request's data — can
  bleed one user's information to another under heavy concurrent load. Build it
  from the postmortem and the actual bug report, so the reader understands why
  connection pooling plus cancellation is a classic source of cross-user data
  exposure, not a mystery specific to AI.
- **The record, straight.** The order of events and the exact scope OpenAI
  reported (chat titles and first messages; the payment-data subset and what
  fields), how OpenAI's account developed, and what the Garante actually ordered
  and why, with dates. Where any account was revised or is contested (e.g. scope,
  or how the breach fit the regulator's broader concerns), present the strongest
  version of each and say what would settle it.

Then the close the beat requires: where this same weakness lives now, in any
AI service that caches per-user state behind a shared, pooled backend. Keep the
whole piece factual and mechanism-focused; it examines a privacy failure and
gives no instructions for causing one.

## Sources

Floor (from `nb source-policy`): at least 8 sources, at least 4 primary, at least
1 secondary. Primary means the document that owns the claim: OpenAI's own
postmortem and any security/help note; the open-source client library's bug
report and fix; the Garante's order and any later decision. Reporting from
outlets that held up is secondary context. Verify the breach scope and every date
against the primary that owns it; a regulator's finding is quoted from the order,
not from coverage of it.

## Template and metadata

Template: `lesson`. `nb-meta` tags (writer sets, 4-6, lowercase hyphenated),
candidates: openai, chatgpt, data-breach, privacy, gdpr. Date 2026-09-21.
`harness` "claude-code"; `model` the writer's actual served model.

## This run's neighbors

Four other lessons publish tonight: `the-evidence/backpropagation`,
`the-instruments/comet-score`, `the-mechanics/false-premise-questions`,
`what-could-go-wrong/negative-side-effects`. Distinct subjects; nothing to
deconflict.

## Recent shapes to break (habits, not rules)

Recent When AI Breaks lessons (predpol-predictive-policing, amazon-rekognition-
congress) run: a striking figure as the headline, then "behind the tool is a
score and a cutoff" mechanism, then "who it hit," closing on "where this runs
today." Deks lean on a dollar figure plus "at the default setting," or "sold it
for years before anyone checked." Find this piece's own headline surprise and
closing image; do not copy the dollar-figure dek or the "where it runs after the
pause" closer.

## Production policy (actual)

`nb production-policy`: profile `balanced`, tier `capable`, no `required`.
Resolved for this run's isolated subagents: researcher Opus 4.8 (high),
writing-coach Sonnet (low), writer Opus 4.8 (medium), editor Opus 4.8 (high).
Efforts advisory.
