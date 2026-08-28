# writer brief: the-mechanics/glitch-tokens (01)

Inputs:
- editorial-direction.md   (house standard, paper voice, series prompt, template identity)
- writing-coach/01/voice-guide.md   (how this piece should sound; read before drafting)
- researcher/01/evidence.md   (the complete claim set; read its Contradictions closely)
- the initialized article at library/the-mechanics/glitch-tokens.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-mechanics/glitch-tokens/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/glitch-tokens/library/the-mechanics/glitch-tokens.html --series the-mechanics

Precision the research demands (do not overstate):
- It is a tokenizer-MODEL PAIRING effect, not a property of "GPT-2." " SolidGold-
  Magikarp" was NOT verified under-trained in GPT-2 itself; the original weird
  behavior was observed on GPT-3 (davinci-instruct-beta) and ChatGPT, and the
  embedding geometry was examined on GPT-J and Phi-2 (which reuse the GPT-2
  tokenizer but train on different data). Say "models using the GPT-2/GPT-3
  tokenizer," not "GPT-2 does this."
- Under-training is ONE cause among several, not the only one: some glitch tokens
  are unreachable in pre-tokenization, BPE junk fragments, or config artifacts.
  Frame under-training as the main, best-established cause while noting it is not
  the whole story (the record supports this in Contradictions).
- Settled vs OPEN (series requires marking this): settled = the tokenizer's
  vocabulary is built separately from training, so a token can be in the vocab yet
  near-absent from training, leaving its embedding near random initialization;
  detection of under-trained tokens is solved (Land & Bartolo, "Fishing for
  Magikarp," EMNLP 2024: under-trained tokens are ~0.1-1% of the vocabulary across
  25 models; models whose tokenizer trained on the same corpus as the model, e.g.
  Pythia on the Pile, have far fewer). OPEN = the precise path from a near-dead
  embedding to a SPECIFIC weird output (why one token spells doom, another
  insults) is NOT explained. Do not invent that mechanism.

Use real, verified token strings from the record (e.g. " SolidGoldMagikarp",
" TheNitromeFan", " petertodd", "StreamerBot") and their origins (a Reddit
counting forum's usernames; game/e-commerce backend strings). Inline <code> is
appropriate for exact token strings the reader must preserve.

Continuity (link, do not overlap): the-mechanics/letter-counting is about
characters hidden inside a normal token — the opposite end; make the distinction
explicit and link it. the-mechanics/word-embeddings for "an embedding is a learned
vector" (here it was NOT learned) — link. No code (series rule); prefer a table
for the token examples or the per-model counts. No verdict block in the body — the
takeaway bookend lands the judgment.

Recent shapes in The Mechanics to break: short behavior-declarative headlines are
the house style; do not clone the most recent two, and steer clear of
letter-counting's framing. Avoid banned dek molds and the comma-plus-"and" heading
join.

nb-meta you own: date 2026-08-28; harness "Claude Code"; model "claude-opus-4-8".
