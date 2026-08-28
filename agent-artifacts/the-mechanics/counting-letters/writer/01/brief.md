# writer brief: the-mechanics/counting-letters (01)

Inputs:
- editorial-direction.md   (house standard, paper voice, series prompt, template identity)
- writing-coach/01/voice-guide.md   (how this piece should sound; read before drafting)
- researcher/01/evidence.md   (the complete claim set; read its Contradictions closely)
- the initialized article at library/the-mechanics/counting-letters.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-mechanics/counting-letters/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/counting-letters/library/the-mechanics/counting-letters.html --series the-mechanics

The one thing this lesson must get right (the research sharpened it):
Tokenization is a genuine PRIMARY cause but NOT the SOLE cause, and the honest
lesson marks settled vs open. Settled: BPE tokens are frequency-merged
word-pieces (often whole words), not letters, so a token does not directly expose
the characters inside it — show the real tiktoken worked example from the record
("strawberry" -> str|aw|berry in cl100k_base; a single token with a leading
space). Open: models can often spell a token's letters correctly yet still fail
to count or manipulate them (CUTE), the failure persists even when the word is
split into several tokens, and probing shows character identity is partly
recoverable from the token vector. So the cause is "the model reads word-pieces,
not letters, and character information is only weakly and indirectly available,"
not "the tokenizer makes it impossible." Do not overclaim tokenization as the
whole story; the series requires marking which steps are settled engineering and
which are open. No code (series rule); prefer a table for the tokenization
example over any code listing.

Two record traps: (1) the "GPT-4o/Claude answered two r's" instance rests on
SECONDARY reporting (TechCrunch), not a primary transcript — attribute it as
such or lead with a primary-sourced failure. (2) CUTE has NO counting task —
never cite it as a letter-counting benchmark; cite it for the spell-but-fail-to-
manipulate finding only.

Continuity / differentiation (link, do not re-teach or overlap):
- the-mechanics/text-in-images is the closest neighbor and is about IMAGE
  generation spelling. Make the distinction explicit (same root cause, different
  behavior/surface) and link it; do not repeat its worked example.
- the-mechanics/multilingual-gap: link for "what a tokenizer is / token counts,"
  but the point here is character identity inside a token, not token count.
- the-mechanics/getting-math-wrong: different mechanism (next-token arithmetic);
  do not conflate letter-counting with it.

Recent shapes in The Mechanics to break: short declaratives about a behavior are
the house style, but do not copy the build of the most recent two, and steer
clear of text-in-images' framing. Avoid banned dek molds and the comma-plus-"and"
heading join. No verdict block in the body — the takeaway bookend lands the
judgment.

nb-meta you own: date 2026-08-28; harness "Claude Code"; model
"claude-opus-4-8".
