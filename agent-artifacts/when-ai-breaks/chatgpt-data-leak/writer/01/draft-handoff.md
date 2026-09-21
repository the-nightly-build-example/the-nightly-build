# Draft handoff: when-ai-breaks/chatgpt-data-leak (01)

## Original-work sentence

The article turns a "ChatGPT broke" story into a lesson about ordinary web
plumbing: it teaches the cancelled-request / pooled-connection fault as a
general cross-user leak pattern (not an AI-specific one), and it separates what
the Garante actually ordered on 30 March 2023 (training legal basis,
transparency, data accuracy, age verification, with the breach absent as a
ground, and the later fine annulled) from the widely-repeated claim that the
breach grounded the block. The evidence record flags both moves; the article is
where they become argued prose, in the "shared-caches" and "italy-block"
sections.

## Proof result

Command run (exact, links included):
`./nb check .../when-ai-breaks/chatgpt-data-leak.html --series when-ai-breaks --repo /home/user/the-nightly-build`

- **BLOCK: 0** — verdict PUBLISHABLE.
- WARN: 2, both `W-SENTENCE-DENSITY` (one 43-word / 2-join sentence, one
  49-word / 2-join sentence).

## Warnings intentionally left

The two `W-SENTENCE-DENSITY` warnings stand by choice. The worst offenders the
first proof flagged (a 69-word takeaway sentence and a 64-word / high-punctuation
grounds sentence) were split. The two that remain are controlled parallel
constructions, and at least one is a verbatim quotation from OpenAI's postmortem
or the redis-py bug report that must be reproduced unaltered. The editorial
standard permits a long sentence under control, and the lesson bookends run "at
whatever length clarity needs"; splitting these further would chop a parallel
list or break a quote. No `W-CITE-ORDER`, banned-term, caps-run, or link
warnings remain.

## Notes for the editor

- Sources are numbered in first-citation order. TechCrunch (secondary) is cited
  in the italy-block before the later Garante releases, so it is source 7 and
  the Garante block/decision/reinstatement releases follow as 8/9/10; this is
  deliberate, not a chronology.
- Composition: 10 sources, 8 primary and 2 secondary (floor: 8 / 4 / 1).
- Both commission corrections are applied: the order is stated as resting on
  training/transparency/accuracy/age grounds with the breach not among them, and
  the €15M fine is presented as annulled (Court of Rome, judgment published
  18 March 2026), not as the settled ending.
- Model recorded in nb-meta is `claude-opus-4-8` (the served model), harness
  `claude-code`, date 2026-09-21.

## Open evidence / voice questions

None. Every claim drew on the evidence record; no gap required a researcher
request, and the voice guide settled the register and the causal-chain-in-prose
approach without ambiguity.
