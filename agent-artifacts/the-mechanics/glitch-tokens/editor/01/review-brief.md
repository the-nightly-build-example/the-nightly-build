# editor review-brief: the-mechanics/glitch-tokens (01)

Inputs:
- editorial-direction.md   (house standard, slop/headline specs, paper voice, template identity)
- commission.md            (the assignment, its boundaries, the reader's situation)
- writer/01/brief.md        (the exact writer brief incl. precision constraints — check for leaks against it)
- writing-coach/01/voice-guide.md   (read first; how the piece should sound; check for borrowed phrasing)
- researcher/01/evidence.md   (the claim set; reread cited passages for what breaks each claim)
- writer/01/draft-handoff.md   (open its original-work sentence only on the third read)
- the drafted article at library/the-mechanics/glitch-tokens.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-mechanics/glitch-tokens/editor/01/editorial-review.md
Proof (orchestrator stamps and runs after your edits): ./nb check .nb-work/the-mechanics/glitch-tokens/library/the-mechanics/glitch-tokens.html --series the-mechanics

Recent-pattern notes (check the draft against these library habits):
- The Mechanics headlines are short declaratives about one behavior. Flag a rote clone of the most recent two.
- The closest published neighbor is the-mechanics/letter-counting (characters hidden inside a normal token) —
  the opposite end of the same tokenizer story. Check the distinction is explicit and the framing does not echo it.
- Banned dek molds: comma-triad, semicolon reversal, suspended question. Heading habit to break: comma + "and".
- Bookend openers must hold to this lesson's particulars, not generic importance.

This round's focus (verify against the evidence record):
- PRECISION: the piece must treat this as a tokenizer-MODEL PAIRING effect, NOT "GPT-2 does this."
  " SolidGoldMagikarp" was not verified under-trained in GPT-2 itself; the original behavior was on GPT-3
  (davinci-instruct-beta) and ChatGPT, with embedding geometry examined on GPT-J/Phi-2 (which reuse the GPT-2
  tokenizer, different training data). Flag any sentence that attributes the glitch to "GPT-2."
- Under-training must be framed as the MAIN but NOT SOLE cause (some glitch tokens are unreachable in
  pre-tokenization, BPE junk, or config artifacts). Check it is not overclaimed as the whole story.
- Settled vs OPEN must be marked honestly: settled = vocab built separately from training, undertrained tokens
  have near-random embeddings, and detection is solved (Land & Bartolo, ~0.1-1% of vocab across 25 models;
  Pythia/NeoX low because tokenizer trained on the same Pile corpus). OPEN = the path from a near-dead embedding
  to a SPECIFIC weird output is unexplained and must NOT be invented.
- Check the token strings and origins against the record; inline <code> is correct for exact token strings.
  No code listings (series rule) — a table is correct for token/per-model examples.

Note on internal links: the prose links to the-mechanics/word-embeddings and the-mechanics/letter-counting use
CORRECT real published slugs and resolve on the library branch, not this workspace — do not treat as broken.
No verdict block in the body — the takeaway bookend lands the judgment.
