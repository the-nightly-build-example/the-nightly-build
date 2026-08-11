# Draft handoff: when-ai-breaks/bing-sydney (01)

## Original work

The article turns the evidence record's separately-sourced first-week episodes
into one ordered causal account and makes an argument the evidence only implies:
that Microsoft's choice of a conversation-length cap over a retrain is itself the
diagnosis, which is what lets the piece hold the two firmly-documented failures
(rules extractable by asking, persona instability in long chats) apart from the
labeled inference about their internal cause. The visible carrier of that work is
the section "The turn cap is the diagnosis."

## Proof result

Final `nb check` with links included, after `nb stamp`: `BLOCK: 0  WARN: 0`
(verdict PUBLISHABLE). Stamp wrote words=2182, reading_minutes=9, sources=10.

No warning is left standing. One deliberate sourcing decision to flag, since it
resolves cleanly rather than as a warning:

- The Kevin Liu primary disclosure tweet
  (`x.com`/`twitter.com` `/kliu128/status/1623472922374574080`, the id the
  evidence record recorded) is now deleted and returns 404 on both hosts, and
  web.archive.org is egress-blocked from this session, so no page Liu himself
  posted resolves. A live link to it was a hard `B-SOURCE-DEAD` block. I dropped
  it as a standalone numbered source and cite Liu's disclosure through the two
  resolving records the evidence names as the read route: Ars Technica (source 3,
  which republishes his screenshots credited "Kevin Liu") for the leaked-rules
  note and the leak timeline, plus Microsoft's on-record confirmation that the
  rules are genuine (source 2). Liu is still named as the discloser in the prose
  and the note's attribution line. Source floor still met: 10 sources, 7 primary,
  3 secondary. Von Hagen's primary tweet (source 4) resolves and stands as the
  primary posted disclosure of the leak.

## Open question

Minor, for the editor: the leaked-rules block quote is cited to Ars (source 3)
for locality with the leak paragraph; Simon Willison (source 10) reproduces the
full leaked "Sydney document" verbatim and would be an equally faithful cite for
that verbatim block if the desk prefers pointing a quotation at its fullest
reproduction. Both resolve.
