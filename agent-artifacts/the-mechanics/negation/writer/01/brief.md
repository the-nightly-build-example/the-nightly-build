# writer brief: the-mechanics/negation (01)

All paths are relative to the repo root /home/user/the-nightly-build.
Let AR = .nb-work/the-mechanics/negation/agent-artifacts/the-mechanics/negation

Inputs:
- $AR/editorial-direction.md — house standard, paper voice, series prompt, template identity, furniture
- $AR/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting and before every revision
- $AR/researcher/01/evidence.md — the complete claim set available to you
- $AR/commission.md — the behavior, the causal chain to teach, the distinct contribution to make visible
- Article to edit: .nb-work/the-mechanics/negation/library/the-mechanics/negation.html (initialized from the lesson template)
- Template contract and furniture catalogs: .nb-work/the-mechanics/negation/.nb-context/

Output: $AR/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/negation/library/the-mechanics/negation.html --series the-mechanics --library /home/user/library-checkout
(run from repo root; use --no-check-links while iterating, then the full command with links to BLOCK: 0)

Recent habits on this desk to break (do not inherit):
- Headline molds "A model can <do X> and still <fail Y>" (counting-letters) and "The <thing> a model can't <do>" (glitch-tokens). State the negation finding in its own nouns.
- Body sections have run as 4-6 short titled steps often ending on a "where the explanation runs out" section. The settled/open mark is required content, but do not copy that section title.
- nb-note is on nearly every recent mechanics piece by default. Use it only where a labeled failed-prompt-and-output example genuinely reads better as a note.

This round's focus: keep it concrete — real negated prompts and their wrong outputs
at each step — while covering both the text case and the image (bag-of-words) case,
and mark cleanly which steps are settled (data imbalance, measured negation gaps,
bag-of-words behavior, what negative prompts/CFG do) versus open (the precise
attention-level mechanism). Work backward from the behavior to ground; no code.
Link tokenization/image pieces in Background rather than re-teaching them.
