# editor review-brief: the-mechanics/counting-letters (01)

Inputs:
- editorial-direction.md   (house standard, slop/headline specs, paper voice, template identity)
- commission.md            (the assignment, its boundaries, the reader's situation)
- writer/01/brief.md        (the exact writer brief — check for leaks against it)
- writing-coach/01/voice-guide.md   (read first; how the piece should sound; check for borrowed phrasing)
- researcher/01/evidence.md   (the claim set; reread cited passages for what breaks each claim)
- writer/01/draft-handoff.md   (open its original-work sentence only on the third read)
- the drafted article at library/the-mechanics/counting-letters.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-mechanics/counting-letters/editor/01/editorial-review.md
Proof (orchestrator stamps and runs after your edits): ./nb check .nb-work/the-mechanics/counting-letters/library/the-mechanics/counting-letters.html --series the-mechanics

Recent-pattern notes (check the draft against these library habits):
- The Mechanics headlines are short declaratives about one behavior ("A model can't count the words it's
  writing," "ChatGPT multiplies two five-digit numbers and misses by 913,200"). Fine as a house shape, but
  flag a rote clone of the most recent two.
- The closest published neighbor, the-mechanics/text-in-images ("A generated image gets its letters wrong
  before the picture is ever drawn"), shares this root cause. Check the draft does not echo its framing or
  repeat its worked example; the distinction (image spelling vs text letter-counting) must be explicit.
- Banned dek molds: comma-triad, semicolon reversal, suspended question. Check the dek.
- Heading habit to break: comma + "and" two-clause join. Vary construction.
- Bookend openers must hold to this lesson's particulars, not generic importance.

This round's focus:
- Verify the SETTLED-vs-OPEN line held and is honest: settled = BPE tokens are frequency-merged word-pieces,
  not letters; open = how much character information a model recovers (it can often spell a token yet miscount
  it). The piece must NOT overclaim tokenization as the sole/whole cause — that is a required revision if it does.
- Confirm the two record traps are handled: the "GPT-4o/Claude said two r's" instance must be attributed as
  secondary (TechCrunch) reporting; CUTE must be cited only for the spell-but-fail-to-manipulate finding,
  never as a letter-counting benchmark.
- Check the worked tokenization example against the evidence record (str|aw|berry in cl100k_base; the r's split
  across pieces; single token with a leading space). No code (series rule) — a table is correct.
- Continuity: the Background links to the-mechanics/multilingual-gap, the-mechanics/text-in-images, and
  the-mechanics/getting-math-wrong use the CORRECT real published slugs (confirmed) — do not treat them as
  broken; they resolve on the library branch, not in this isolated workspace.
