# writer brief: the-mechanics/multilingual-gap (01)

Inputs (all paths under this article's artifact root unless absolute):

- `editorial-direction.md` — house standard, slop, headline standard, press voice,
  lesson identity, series prompt. Binds every sentence.
- `commission.md` — the behavior, angle, neighbors, required contribution.
- `writing-coach/01/voice-guide.md` — how this piece should sound; read before
  drafting; reuse the subject's terms, never the exemplars' phrasings.
- `researcher/01/evidence.md` — the complete set of claims available to you,
  including a reproducible tiktoken token-count series (UDHR Article 1, 13
  languages, 33 tokens English to 512 Burmese).
- Article to edit in place:
  `/home/user/the-nightly-build/.nb-work/the-mechanics/multilingual-gap/library/the-mechanics/multilingual-gap.html`
- Template context: `/home/user/the-nightly-build/.nb-work/the-mechanics/multilingual-gap/.nb-context/`

Output: `writer/01/draft-handoff.md`.

Proof: `./nb check /home/user/the-nightly-build/.nb-work/the-mechanics/multilingual-gap/library/the-mechanics/multilingual-gap.html --series the-mechanics --library /home/user/library-checkout`
(run from `/home/user/the-nightly-build`).

This round's focus:

- Lead with data distribution as the primary cause; make the token tax the
  secondary amplifier, per the commission. The token-count series is a natural
  table or chart if it earns its place (build a chart only from the verified
  series via `nb chart`).
- Carry the four caveats the evidence records, and do not tell a clean single-
  cause story: (1) the token disparity is not always a data-share artifact
  (Ahia); (2) the performance benchmark is machine-translated, so part of the
  English-vs-other gap is translation quality, not the model; (3) the gap is
  narrowing but not closing; (4) the token premium is a property of the
  tokenizer's training, not the script itself (MuRIL tokenizes Telugu at 1.21x
  where English-centric tokenizers charge 5x+). Mark settled versus open as the
  record does.
- Handle the dated-proxy honestly: the 93%-English figure is GPT-3 (2020); no
  current frontier model discloses its per-language mix. Attribute it to GPT-3 and
  pair it with the raw-web Common Crawl share rather than implying it is today's
  frontier mix. Link tokenization rather than re-teaching it.

Habits not to inherit (from the commission and the recent shelf):

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula, and do not model The Mechanics' "the thing that
  feels like X is not what happens" opener. Do not close on a stock "where this
  lives now" heading; name the closing section for its content. Do not land the
  takeaway on negative parallelism. Deks: avoid the banned molds.

Set nb-meta `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`.
Make the display-text pass before proving, and prove to `BLOCK: 0` with links
included.
