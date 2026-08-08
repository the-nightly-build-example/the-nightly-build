# Draft handoff: the-instruments/needle-in-a-haystack (01)

## Original work
The article takes the near-perfect needle-in-a-haystack number apart into the
one narrow act it actually scores — copying back a single out-of-place sentence —
and then walks four harder primaries (NoLiMa, multi-needle, RULER, Lost in the
Middle) to show, capability by capability, exactly what a green grid leaves
untested, a retrieval-versus-reasoning decomposition none of the sources performs
on its own.

## Proof result
`./nb check ... --series the-instruments --library /home/user/library-checkout`
(links included, after `./nb stamp`): **BLOCK: 0, WARN: 0, PUBLISHABLE.**
Stamped words=1826, reading_minutes=8, sources=8 (7 primary, 1 secondary).
No warnings left standing.

## Precision the brief flagged — resolved against primaries
- **RULER "four models at 32K."** The evidence's quote ("only four models ...")
  conflicted with an abstract-level "only half of them" reading. I opened RULER's
  own effective-context table (arxiv HTML v2) and confirmed the paper states
  "only four models (GPT-4, Command-R, Yi-34B, and Mixtral) can maintain
  satisfactory performance at the length of 32K," with the per-model effective
  lengths (GPT-4 64K/128K, Command-R 32K/128K, Yi-34B 32K/200K, Mixtral 32K/32K)
  and the Llama-2-7B 85.6%-at-4K threshold. The nb-table is built from those
  verified values (ChatGLM 128K/4K and LWM 1M/<4K added from the same table to
  show the collapse). "Only four hold at 32K" is what the table supports; I did
  not use the looser "half" framing.
- **Verbatim quotes re-opened on the primary.** The Claude 2.1 added line "Here
  is the most relevant sentence in the context:", the needle sentence, and the
  question were confirmed character-for-character against
  claude.com/blog/claude-2-1-prompting.
- **Two capabilities kept apart.** "Finding the planted fact" (retrieval) and
  "using the whole document" (reasoning) are named once and held distinct at
  every mention; the deflating comparison rides in the clause that reports each
  strong score.
- **Fairness point carried as the lesson, not a hedge.** The Claude 2.1
  27%→98% prompt fix is the piece's evidence that a green grid is necessary but
  not sufficient; a red grid caught a real, fixable failure.

## Decision the editor should confirm — source asset substitution
The evidence's Source-assets block identifies a Claude 2.1 green/red NIAH grid on
the Anthropic post as the strong figure. On re-opening that primary, the post
carries **no** green/red grid — its actual figures are (1) the one-line prompt
diff and (2) a position bar chart. I captured the prompt diff (`asset-1.png`, via
`./nb asset image` from the cited primary) as Fig. 1 in "The failure the test did
catch," because it is the exact visual of the evidence's own quoted, established
fact (the single added reply line that moved the score 27%→98%, model and window
unchanged) and the section spends precisely what it shows. This is a substitution
within the same primary and the same claim, not an external image URL and not a
fabricated grid. Alternatives were weaker: the Gemini heatmap exists only in a
PDF with no HTML render (hard to crop cleanly), and the original green/red grid
survives only in the secondary Arize write-up. If the editor wants an actual
green grid, the cleanest primary path is a `./nb asset pdf` crop of the Gemini
1.5 report figure; flagging rather than forcing it.

## Notes left intentionally
- **Lost in the Middle** per-position percentages were evidence-flagged as
  read-off-chart approximations (±1). I used only the reliable qualitative claim
  (middle-position accuracy falls below the closed-book baseline — worse than no
  context) and printed no approximate figures. The general U-shape is linked, not
  re-taught, to the-instruments/context-window per the boundary.
- **NoLiMa illustration**: the association-only needle example (a character next
  to an opera house) is written as an explicit hypothetical, since the evidence
  record does not supply a specific NoLiMa needle string to quote.

## Open questions
None blocking.
