# Editorial review 01 — when-ai-breaks/gemini-image-generation

## Skeptic

`Skeptic: thesis "Gemini's diversity rule fired context-blind on prompts history had
already answered because the model cannot tell an operator's appended instruction
from the user's own, the same tradeoff every bias-mitigating system makes"; tested
6 claims: (1) launch-to-pause timeline and dates, (2) Raghavan's title, (3) the
"completely unacceptable" quote's wording/attribution/scope, (4) the fact/reconstruction
seam on the tuning mechanism, (5) "acknowledged outputs vs. cherry-picked screenshots,"
(6) every data-nb-kind label; broke: the Pichai-memo sentence's scope (fixed — see
Edits), a clarity ambiguity in "the model that replaced Gemini's" (fixed).`

Verified against the record directly (not just against the evidence file):
- **Dates.** 1 Feb (launch), 21 Feb (Verge/CNN first-party tests, Google's first X
  post, Krawczyk statement), 22 Feb (pause), 23 Feb (Raghavan post), 26 Feb
  (Hassabis, MWC), 27 Feb (Pichai memo, "four days later" from the 23rd — correct),
  4 Mar (Brin), 28 Aug 2024 (Imagen 3 restoration) — all check against the evidence
  record and the article's own arithmetic ("three weeks," "four days later," "six
  months later") holds.
- **Raghavan's title.** Article: "Prabhakar Raghavan, a Google senior vice president."
  Matches both the blog byline ("Senior Vice President") and NBC's independent
  phrasing ("a senior vice president at Google") exactly, and correctly avoids his
  fuller real-world title, which no source in the record confirms. No fix needed.
- **The "completely unacceptable" quote.** Re-fetched the Semafor article directly
  (not just the evidence file) to check wording and scope. Wording and attribution to
  Pichai's staff memo are exact. But the quote's "that's" covers *both* the image
  controversy and a separate text controversy (Gemini equating Musk with Hitler) —
  confirmed by the direct fetch, and flagged in the evidence record. The draft's
  paragraph is entirely about images and gave no signal the memo covered more than
  that, which would leave a reader thinking the memo was image-specific. **Fixed**
  (see Edits).
- **Fact vs. reconstruction.** The mechanism section states plainly, twice, that
  Google never confirmed which of the two candidate architectures "tuning" means,
  and grounds the "invisible instruction" reading in OpenAI's DALL-E 3 system card
  rather than in an unconfirmed claim about Gemini's own internals. Re-verified the
  OpenAI quote independently by search ("primarily white, young, and female" /
  "tuned ChatGPT's transformation of the user prompt to specify more diverse
  descriptions of people") — matches the article's quoted text exactly. This is the
  article's own stated original contribution and it holds up.
- **Acknowledged outputs vs. cherry-picked screenshots.** The article never asserts
  the Founding Fathers portrait, the diverse Vikings, or the @IMAO_ pope image as
  confirmed Gemini output; it explicitly says none was reproduced under controlled
  conditions and rests its visual and textual evidence only on The Verge's and CNN's
  own first-party tests. Two independent newsrooms, two independent tests — the
  desk's confirmation bar is cleared for the pattern; the article does not overstate
  it to cover any single viral image.
- **data-nb-kind audit.** Checked all 11 sources against the evidence record's
  classifications and against what each in-text citation actually cites. The one
  "secondary" label (NBC, s4) is used only where the article cites NBC's own framing/
  reporting. Every "primary" label is used only where the citation carries a first-
  party artifact — Google's own words, an executive's own on-record quote, or a
  newsroom's own captured Gemini output — consistent with how the evidence record
  itself classifies split-use sources (Verge, CNN, Semafor, AI Business, Fortune,
  TechCrunch: outlet framing secondary, quoted/captured artifact primary). No
  mislabeling found.

## Cut

`Cut: 2 sentences (net); worst tell: "It is not a stretch" — a self-grading hedge
asserting the article's own inference is sound instead of doing more argument.`

Direct edits made:
- Cut "It is not a stretch." from the takeaway (self-grading; the two sentences
  before it already carry the reasoning it was vouching for).
- Two semicolons converted to periods (orientation section, twice) — each joined two
  separate factual statements about two different prompts, not a single tightly
  bound thought; the plainer mark was overdue per house punctuation standard.
- "the model that replaced Gemini's" → "the model that replaced Imagen 2" — the
  original was ambiguous (reads as if Imagen 3 replaced Gemini itself); the article
  had already named Imagen 2 as the specific model in the orientation section, so
  the fix is a one-word swap to the already-established name.
- Added a short clause marking the Pichai memo's dual scope (see Skeptic).

Checked and kept: culture-war vocabulary (woke, DEI, anti-white, bias hysteria,
race-swapping) — none present; the piece stays in engineering terms throughout, as
directed. No colon-subtitle headline. Heading cadence varies across the three body
headings and does not repeat the banned comma-and-clause join. The "one clean
tradeoff sentence" recurs across the mechanism section, the Imagen-3 section, and
the takeaway in different phrasing each time — this tracks the desk's required
"where the same weakness lives today" close and the template's takeaway
requirement rather than a mechanical restatement; after cutting the self-grading
line the repetition reads as the argument building, not an echo.

## Reader

`Reader: this gives me the actual, worked mechanism (an appended, context-blind
instruction a model can't distinguish from the user's own prompt) behind a story I
only knew as a political fight, plus the fact/reconstruction seam Google itself
never closed — not available by reading any single cited source.`

Compared against the original-work sentence in `draft-handoff.md`: the draft's
stated original contribution is building the bridge between Google's
architecture-agnostic word "tuning" and the general "instructions are data"
mechanism, using OpenAI's independently documented DALL-E 3 technique as evidence
while marking Gemini's specific implementation as unconfirmed. That bridge is
exactly what survives the read — present in the mechanism section's two-candidate
walkthrough and referenced again, not re-argued, in the takeaway. Prose sits closer
to the voice-guide exemplars (Travis, Graham-Cumming, Feynman) than to a median AI
summary: dated, named, one worked case before generalizing, Google's account
attributed in the sentence that carries it, no scene-setting, no naming of the
political sides.

## Visual evidence

Inspected `library/when-ai-breaks/gemini-image-generation/asset-1.png` directly.
The crop retains exactly what the argument spends: all four generated portraits
(white man, Asian woman, Black man, and a fourth ambiguous-race woman, all in the
same period German uniform) plus Gemini's own reply text ("Sure, here is an
illustration of a 1943 German soldier"), with The Verge's page chrome removed. The
caption ("Only one of the four figures is a plausible answer to the prompt as
asked") is factual and checks against the image. Alt text matches the image
exactly. Citation is inline, attributed to The Verge, with a locator and URL. The
image is a locally captured asset (`nb asset`), not an external/hosted URL — no
proof-bar issue. No recrop needed.

## Other checks

- No Background link to `../the-mechanics/instructions-are-data.html` — confirmed
  directly against `/home/user/the-nightly-build/library-checkout/library/
  the-mechanics/`, which has no `instructions-are-data.html`. Correctly omitted;
  the one needed sentence is taught in place in the mechanism section instead.
  `the-evidence/instructgpt.html` and `when-ai-breaks/compas-recidivism.html`, both
  linked, do exist in the checkout.
- No scripts, styles, or iframes added; no external image URLs anywhere in the
  article.
- Banned terms: 0 em-dashes in prose (limit 4), 0 uses of "leverage," "load-bearing,"
  "machinery," "revolutionary/transformative/game-changing," or "AI race."

## Required work

None. All findings were fixable as surgical edits within this pass; no gap needs
new evidence or new prose.

## Proof

```
nb check .nb-work/when-ai-breaks/gemini-image-generation/library/when-ai-breaks/gemini-image-generation.html --series when-ai-breaks --library /home/user/the-nightly-build/library-checkout
```
Result: `BLOCK: 0` / `WARN: 0` / `verdict: PUBLISHABLE` — clean after edits.
`nb-meta` word/source counts remain within the proof's self-count tolerance after
the edits; no meta update required.

## Decision

Publishable as edited. No redraft required.
