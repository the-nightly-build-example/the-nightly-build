# Draft handoff: the-mechanics/text-in-images (writer 01)

## Original-work sentence

The article reorders the evidence's scattered source claims and its three
flagged tensions into a single backward causal chain, from the garbled sign
down to subword tokenization and back up, and from that chain it builds a
diagnostic the evidence never states outright: given a garbled sign, tell an
encoder failure (the model not knowing the letters) from a drawing-step failure
(the model not shaping the letters it was given), while keeping the two encoder
levers (size vs character-awareness) distinct. The work is visible in the final
section ("So look again at the sign") and the settled-versus-open split that
runs through the piece.

## Proof result

Command (from repo root, links included):

```
./nb check .nb-work/the-mechanics/text-in-images/library/the-mechanics/text-in-images.html \
  --series the-mechanics \
  --library /tmp/claude-0/-home-user-the-nightly-build/795ad1d0-7e30-55f8-9f00-32962f849f5d/scratchpad/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. Stamped words=2179,
reading_minutes=9, sources=8 (7 primary, 1 secondary), within the lesson band
(1200-2200). No warnings intentionally left; the six initial
W-SENTENCE-DENSITY notes were all resolved by splitting the long sentences.

A press-check `nb preview` build succeeded and rendered the article with its
furniture (the quotation note and the stat strip) and Background links intact.
The build's own exit code 2 is a whole-site press-check advisory unrelated to
this article; `nb check` is the authoritative gate and is clean.

## Keystone handling (don't-overclaim)

- The spine is stated as commissioned: the failure is set at the text encoder,
  before any pixel. But the piece explicitly holds that the encoder governs
  whether the model *knows* the letters, while the diffusion decoder governs
  whether it can *shape and place* them (the settled-vs-open line), and that a
  character-blind model at very large scale recovers spelling (PaLM 540B >99%,
  T5-XXL 66%), so the letters are "degraded and expensive to reach," not erased.
  The draft says so in as many words ("The letters are not erased.").
- Encoder SIZE (Imagen's frozen T5-XXL, 4.6B) and encoder TYPE (character-aware
  ByT5) are kept as two distinct levers: "Size helped first" vs "the gain comes
  from reading letters, not from a bigger model."
- Background links point only to already-published lessons (image-generation,
  letter-counting, word-embeddings). CLIP is named inline and cited as source
  s5 only; the-evidence/clip is not linked.

## Open questions

- Source asset not captured this round. The Character-Aware paper's Figure 1
  (matched prompts, character-blind top row vs character-aware bottom row,
  garbled vs clean) is the single strongest available visual and would let the
  argument "spend what it shows." I left it out to avoid a fiddly PDF-region
  crop under a medium-effort budget; the article stands without it. If the
  editor wants it, it is a clean add via `nb asset pdf` from arXiv 2212.10562,
  cropped to keep one matched pair and the two row labels.
- The DALL·E 3 source (s4) is a ~28 MB PDF cited to the document (Sec 5.2,
  "Text rendering"); the URL resolves and passed link-check. The quotation note
  quotes from "We suspect..." to skip the source's own grammatical slip
  ("words are have") without altering the load-bearing sentence.
