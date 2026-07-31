# Draft handoff — writer 01 — when-ai-breaks/gemini-image-generation

## Original work

The evidence record gives Google's own account ("we tuned it," never specifying
an architecture) and, separately, OpenAI's own documented mechanism for DALL-E 3
(ChatGPT rewriting the user's prompt to insert diversity language before the
image model sees it). Neither source states that Gemini's failure is an
instance of the general "instructions are data" mechanism the course already
teaches through RLHF/instruction tuning. This draft's original work is
building that connection explicitly and marking exactly where it stops being
confirmed fact: it walks one worked case (The Verge's 1943-German-soldier
prompt) through both candidate architectures Google's word "tuning" could
mean, shows that either one reduces to a model obeying an instruction it
cannot distinguish from the user's own text, ties that trust to the RLHF
post-training already taught in `the-evidence/instructgpt.html`, and uses
OpenAI's independently-documented DALL-E 3 technique as the evidence that this
architecture is real and industry-standard, while explicitly stating that
Google never confirmed Gemini uses it. That inferential bridge, and the
explicit fact/reconstruction seam around it, is not present in any single
source; it is the article's own analytical contribution.

## Files changed

- `library/when-ai-breaks/gemini-image-generation.html` — full draft, edited
  from the initialized skeleton. One orientation section plus two named flex
  sections ("The rule inside one 1943 prompt," "Imagen 3 kept the rule,
  tightened it"), both bookends written after the body, 11 sources.
- `library/when-ai-breaks/gemini-image-generation/asset-1.png` — source asset:
  The Verge's own screenshot of Gemini's response to the "1943 German Soldier"
  prompt, captured fresh via `nb asset image` from the live, verified URL
  (`platform.theverge.com/.../2_22_2024_LEDE_SCREENSHOT.jpg`), then cropped to
  remove The Verge's page chrome (orange marketing background) while
  preserving the full four-image response grid and Gemini's own reply text,
  which the mechanism section's prose depends on.

## Proof result

`nb check .../gemini-image-generation.html --series when-ai-breaks --library
.../library-checkout` → **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE** (final run).

History: first full run was BLOCK 0 / WARN 4, all `W-SENTENCE-DENSITY` (long,
multi-clause sentences in the orientation and mechanism sections, plus one in
the takeaway). Fixed by splitting each flagged sentence rather than
repunctuating around the density; re-ran until WARN 0. No warnings were left
unaddressed.

`nb-meta` counts (`words`, `sources`, `reading_minutes`) were measured
directly from the built `Article` object (`ed.word_count`, `len(ed.sources)`)
after the final text edit, not estimated: words=2163, sources=11,
reading_minutes=10 (~216 wpm, consistent with recent `when-ai-breaks` pieces).

`nb preview` was run (site built: 75 articles, 16 builds, no errors) since the
source asset changed the article's layout, and the built output was inspected
directly: the article HTML and `asset-1.png` both landed at the expected path
(`library/when-ai-breaks/gemini-image-generation/asset-1.png`) and the
`<img src>` resolves correctly relative to the article. `nb render-check`
and a direct Playwright screenshot attempt both confirmed no headless Chrome
binary is available in this environment (render-check printed "no Chrome in
this environment; skipped"; Playwright's own launch failed with a missing
browser executable), so a rendered visual screenshot could not be produced
here. This is an environment limitation, not an unresolved warning — the
deterministic proof is the authority per the brief, and it is clean.

## Editorial requests addressed

N/A — this is the first draft (round 01), not a revision.

## Evidence and voice notes carried into the draft

- Marked Google's stated account ("tuning... failed to account for cases that
  should clearly not show a range") as distinct from the reconstructed
  mechanism (prompt-level instruction insertion vs. training-time
  fine-tuning); the draft states plainly that Google never confirmed which,
  and grounds the "invisible instruction" reading in OpenAI's independently
  documented, verbatim-quoted DALL-E 3 system card language (fetched and
  read in full directly from `cdn.openai.com/papers/DALL_E_3_System_Card.pdf`
  in this session — the evidence record had flagged this source as read only
  via a search summary and asked the writer to re-verify before quoting it;
  that re-verification is done).
- Did not assert any single viral screenshot (Founding Fathers portrait,
  "diverse Vikings," the @IMAO_ pope image) as a confirmed-genuine Gemini
  output; used only the two newsroom first-party reproductions (The Verge's
  1943-soldier and senator tests, CNN's pope/grandma/farmer tests) as
  confirmed record, with a single hedged sentence noting the Founding
  Fathers images circulated widely but were never confirmed by Google or
  reproduced under controlled conditions.
- Included CNN's "Irish grandma" vs. "white farmer" inconsistency specifically
  to block the flattened "Gemini refuses to draw white people" reading, per
  the evidence record's contradiction note and the commission's explicit
  instruction.
- `../the-mechanics/instructions-are-data.html` is not present in
  `/home/user/the-nightly-build/library-checkout` (checked directly; no such
  file), so no Background link was added for it. The one sentence it would
  have taught (a language model cannot distinguish an instruction the
  operator appended from one the user typed, because it only predicts what
  should follow in its context) is taught directly in the mechanism section
  instead, at the point the argument needs it.
- Linked `the-evidence/instructgpt.html` in prose, in place, at first use of
  "reinforcement learning from human feedback," per press editorial ("a plain
  link in prose at first use, never a numbered source"), and again as a
  Background row.
- No chart or additional source asset used beyond the one identified in the
  evidence record as argument-carrying; no external/hosted image URLs
  anywhere in the article.

## Remaining questions

None for researcher or writing-coach. No open evidence or voice questions.
