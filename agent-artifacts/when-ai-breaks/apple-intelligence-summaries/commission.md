# Commission: when-ai-breaks/apple-intelligence-summaries

## The incident

Apple's on-device AI feature that summarizes grouped notifications ("Apple
Intelligence" notification summaries, launched in the US with iOS 18.1 in October
2024) generated false news alerts under real news organizations' names. In
December 2024 the BBC complained after a summary of its notifications falsely told
users, under the BBC's own name, that Luigi Mangione (the man charged in the
killing of UnitedHealthcare executive Brian Thompson) had shot himself, which was
untrue. Other false summaries followed. In January 2025 Apple said it would update
the feature to make AI summaries clearly labeled and temporarily disabled them for
news and entertainment apps. The lesson tells it in order and explains why a
summarizer fails this way.

## Structure the series requires

1. **What the system was built to do, what it actually did, who it affected, what
   the operator did after.** Apple Intelligence groups and shortens a batch of
   notifications into a one-line summary that appears under the sending app's name
   and icon. Trained to compress text, it produced summaries that stated things
   the underlying articles did not: the false BBC "Mangione shoots himself" alert;
   a summary that declared darts player Luke Littler the champion before the final
   was played; a summary that misstated a Rafael Nadal story. Because each false
   line appeared beneath a trusted masthead (BBC News), the error inherited the
   outlet's credibility. The BBC and press-freedom bodies (e.g. Reporters Without
   Borders) objected. In mid-January 2025 Apple announced a software update to
   clarify when text is an Apple Intelligence summary and to pause summaries for
   the News & Entertainment app category while it improved them. Get every date,
   the exact false-summary wording, the affected outlets, and Apple's exact
   statement from primaries.
2. **Why this kind of system fails this way.** Teach the mechanism: a summarizer
   is a language model producing the most probable short rendering of an input,
   with no check that its rendering preserves the truth of the source; compression
   forces it to drop and re-combine facts, and a fluent, wrong summary is as easy
   to produce as a right one. Add the specific aggravator here: the summary is
   displayed under the original sender's identity, so a machine's error is
   attributed to a human newsroom. Teach any needed idea in plain words or link an
   existing lesson (the paper already covers how a model builds a fluent false
   statement, and faithfulness/summary-vs-source; link, do not re-teach).
3. **Where the same weakness lives today.** AI summaries of email, chats,
   documents, search results, and news are now default features across products.
   Tie the mechanism to systems the reader meets, with plain in-prose links to
   related library lessons rather than re-telling them.

## Required contribution

The evidence carries the reporting. This piece's own work is to separate two
things the headlines merged: the summary was not "made up" in the way a chatbot
invents a citation, it was a lossy compression of real notifications that changed
their meaning, and the reason it did damage is that a trusted brand's name sat on
top of a machine's sentence. The reader should leave able to see an AI summary
under a familiar app's name and know it is the model's sentence, not the sender's.

## Boundaries (from the series prompt)

- Work from the record: the affected outlets' own reporting (BBC), Apple's
  statements, and press-body objections. Name the people, companies, and dates.
  Where a detail is disputed or a summary's exact wording varies across retellings,
  use the outlet's own account and say what is uncertain.
- Distinct from covered incidents. This is not a launch-demo error (bard-jwst),
  not fabricated citations from a research model (galactica), and not Google's
  search AI Overviews (ai-overviews). It is a notification summarizer changing the
  meaning of real news under the sender's name. Do not re-tell those; link where
  the mechanism connects (e.g. the-instruments/hallucination-rate on faithful vs
  unfaithful summaries; the-mechanics/hallucination). The researcher should surface
  the best library links.
- No hype and no doom. A summarizer compressed news wrongly and a company pulled
  the feature for news. Let the record carry the weight. Name no company as an
  authority; Apple and the BBC are subjects.

## Source policy (when-ai-breaks / lesson)

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primaries:
the BBC's own reporting/complaint, Apple's statement (as quoted by press), the
specific false-summary reports, and a press-freedom body's statement; plus a
primary on the summarization/faithfulness mechanism (a hallucination-in-
summarization paper) to ground the "why." Where an outlet is the affected party
reporting on itself, treat its account as primary for the fact that the alert
appeared. Read the underlying source for every quote and date. Record what is
single-sourced.

## Production policy

Profile balanced. Roles run as Claude Code sub-agents using this checkout's `nb`.
Model "capable" for every stage. Actual models this run: writing-coach sonnet
(low), researcher opus (high), writer sonnet (medium), editor opus (high). No
`required` directive to deviate from.

## Recent-pattern habits not to inherit

- When-ai-breaks openers often shape the first heading as "What OpenAI shipped on
  April 25." Name the first heading for this incident's own opening beat.
- The series prompt asks every piece to close on "where the same weakness lives
  today," so that close reads as formula if built like the last one. Write it
  around this incident's own nouns and avoid the recurring "Where the same X still
  sits/lives" heading shape.
- `spec/headlines.md` bans the comma-triad and semicolon-reversal dek molds.
  Commit the dek to this incident's specific find (a false line under the BBC's
  name that the BBC never wrote).

## Neighboring articles in tonight's run (keep distinct)

the-evidence/computing-machinery-and-intelligence; the-instruments/training-cost;
the-mechanics/text-to-speech-pronunciation; what-could-go-wrong/recommender-
radicalization. This is tonight's only deployed-failure incident piece. (It
replaces an earlier when-ai-breaks commission on Amazon's recruiting tool, which
was withdrawn as a duplicate of the published lesson when-ai-breaks/amazon-hiring-
tool.)
