# Editorial review: the-mechanics/text-to-speech-pronunciation (editor/01)

## Skeptic

Thesis: a text-to-speech voice mispronounces a word for one of two reasons that
sit at different points in the front end, before any audio exists. Either the
right sound was never generated (a normalization or grapheme-to-phoneme failure)
or the right sound existed and the wrong sense was chosen (a homograph failure).

The claims it stands on, and how each held:

- **Pronunciation is decided in a front end, before the back end makes a sound.**
  Cited to WaveNet (s1). The paper's appendix lays out the two-part pipeline
  (text analysis outputs a phoneme sequence; synthesis consumes it), so the link
  owns the claim. The abstract page does not itself print the pipeline sentence,
  but the researcher located it in the appendix and the citation lands on the
  right paper. Held.
- **Two real Siri failures trace to two different steps.** "Des Moines" (silent
  letters sounded out) is traced to G2P: a name with no dictionary entry, sounded
  out from spelling, no meaning in play. "Mobile, Ala." (adjective vowel on a
  city) is traced to homograph disambiguation: a common word already in the
  dictionary with two correct sounds, the wrong one chosen. Both tracings match
  the mechanism and the NPR source (s2). NPR returned a transient 503 on my
  fetch; the URL is the article's own canonical page and the researcher quoted
  Breen's "first port of call" line directly, so the citation stands. Held; this
  is the article's own diagnostic work, not restated evidence.
- **Normalization figures.** 99.3% overall English accuracy and the £900m→"euros"
  / 2mA→"two units" rows match Sproat & Jaitly (s3), and the caption scopes them
  correctly as an experimental normalizer's output with the production filter
  noted. Held and honestly bounded.
- **G2P figures.** 25.8% word error rate (≈ one in four), 21.3% with a
  statistical backstop, on held-out CMUDict words, match Rao et al. (s4). The
  inference that rare names fail more often is the article's, grounded in the
  paper's framing. Held.
- **Homograph ladder.** 85.0 / 89.3 / 95.4 / 99.0 (Gorman, s5, server figures)
  and Amazon's independent 99.1% with no rules (Nicolis & Klimkov, s6) match the
  Numbers record, and the "present" case (every system wrong) is used exactly as
  the source reports it. The article scopes the ceiling to a located, known
  homograph rather than "homographs are solved." Held.
- **Neural TTS.** Tacotron 2 near-human, end-to-end, still trained on normalized
  text, still mispronounces (6/100), skips (1/100), and mishandles prosody
  (23/100); vendors patch with lexicons (Polly, s8, "W3C" → "World Wide Web
  Consortium"). All match Shen et al. (s7) and the AWS docs, both links resolving.
  The floor case ("I read it" cannot be resolved from the sentence alone) is the
  correct ground step. Held.

Display text checked descriptor by descriptor. Headline states the finding and
carries no recent-pattern mold. Dek names Siri, the two examples, and the
"before either becomes a sound" detail without restating the headline, and is not
a comma-triad or semicolon-reversal. Every subhead is a step in the piece's own
nouns. All eight `data-nb-kind` labels are correct (NPR the lone secondary; the
seven papers/docs primary, each owning its claim). One citation label was wrong:
Gorman's title is "Improving homograph disambiguation with **supervised** machine
learning," and the article dropped "supervised" in both the Sources list and the
Go deeper row. The right source was in hand, so I corrected the title in place
rather than routing it. No break belongs to the researcher or writer.

## Cut

Slop pass, every sentence including furniture and display text. Sentences that
failed the test and were removed or trimmed:

- **"That ceiling is real, and so is its limit."** A paragraph-opening edge
  sentence that reduces to "that X is real, and so is its Y" and carries nothing
  the next sentence does not. Deleted; the scoping sentence after it already
  makes the pivot.
- **"What the experiment shows is how much interpretation..."** A "what the
  experiment shows is" signpost frame. Rewrote to state the two facts under it
  (interpretation is needed; it drifts without a check) without the frame.
- **"That's why Siri's other failure resolves the way it does."** An empty
  transition ("resolves the way it does"). Deleted and replaced its follow-on
  with a sentence that does real work: "Mobile" is the opposite case, in the
  dictionary unlike "Des Moines," so the right sound was there. This sharpens the
  two-failure through-line instead of signposting it.

Three sentences failed outright. No repeated slop pattern ran through the piece.
The negative-parallelism constructions that remain ("no meaning to weigh, no
pronunciation chosen badly"; "It fixes the word someone added, not the mechanism
that got it wrong") each correct a real, named distinction the argument rests on,
so they stay.

Grammar and register: fixed "A homograph looked at alone cannot be gotten right
through any spelling knowledge" to "A homograph seen in isolation cannot be
resolved by spelling alone." The lesson's stricter term rule caught two terms
used before they were built and not needed by the argument: "spectrogram" (undefined,
cut, the point survives as "almost straight to audio") and "attention mechanism"
(undefined and never linked; recast as the back end / the model misjudging pace and
stress, which is what the evidence attributes and keeps the mechanistic honesty).
The muddled phoneme aside ("the 'p' and 'b' sounds differ by one phoneme") became
a clean minimal pair ("the difference between 'pat' and 'bat' is a single phoneme").

Reader-address: the lesson allows only its two bookends to speak to the reader.
The diagnostic note's label read "Which failure you just heard," second person in
the body. Relabeled "Which failure just happened," which keeps the diagnostic and
drops the address. The note's body and the rest of the body speak to no one.

Prompt-leakage: compared the authored text against the commission, brief, voice
guide, and evidence. The two-failure diagnostic is the article's own rendering of
the required contribution in the subject's own words and examples, not a lifted
instruction; the "settled vs open" marking is enacted, not announced. No planning
labels, selection rules, or assignment-fulfilled sentences. No distinctive
phrasing borrowed from the voice guide's quoted writers.

Formula: opener heading names this lesson's first step, not the series' "answer it
won't give" mold; the closer heading uses this lesson's nouns, not the "tendency no
rule removes / where it lives" mold. One heading joins two clauses with a comma and
"and," but it is the only one in the piece, so it is not a within-piece formula.

Furniture: two tables (both genuine comparisons) and one note (the diagnostic, the
article's contribution, deliberate emphasis). No stack-of-blocks effect and no
missing component the material needs. No code anywhere, as required; the inline
`<code>` on "Dr.", "St.", "2010" marks literal written forms whose exact
characters are the subject, which is the licensed use.

## Reader

Read straight through, the piece gives a reader something the sources alone do
not: a reusable test for a mispronunciation they just heard, tracing two real
Siri failures to the exact step that produced each and naming the difference
between a sound that was never generated and a sound that existed but was assigned
the wrong sense. The draft-handoff's original-work sentence claims exactly this,
and the article delivers it in the note and the takeaway, resolving both examples
set up at the top. Both answers survive, so the piece is not a restatement of its
sources. The prose sits closer to the voice-guide exemplars than a median summary:
plain claim, one small real case (Des Moines, Mobile, £900m, "present", "I read
it"), then a flat statement of what the step does and does not settle, with the
term "phoneme" built before it is named.

## Edits

- Recast the muddled phoneme aside to a clean minimal pair ("pat" / "bat").
- Cut the undefined, unneeded term "spectrogram"; the clause now reads "almost straight to audio."
- Recast "the attention mechanism misjudging pace" (undefined, unlinked term) as the back end / the model misjudging pace and stress rather than choosing the wrong word.
- Deleted the empty edge sentence "That ceiling is real, and so is its limit."
- Trimmed the "What the experiment shows is" signpost to state its two facts directly.
- Deleted the empty transition "That's why Siri's other failure resolves the way it does" and rewrote the follow-on so "Mobile" is set against "Des Moines" as the in-dictionary, right-sound-existed case.
- Smoothed "cannot be gotten right through any spelling knowledge" to "cannot be resolved by spelling alone."
- Relabeled the diagnostic note "Which failure you just heard" to "Which failure just happened" (removed reader address from the body).
- Corrected Gorman's cited title to "Improving Homograph Disambiguation with Supervised Machine Learning" in the Sources list (s5) and the Go deeper row.

## Required work

None blocking. Every issue was fixable in place and is fixed. No evidence gap,
broken central claim, source-policy failure, chart, or source asset routes to the
researcher or writer.

- writer / orchestrator: standard handoff only. The edits net a small word cut
  from the 2198-word draft (well inside the 1200-2200 band), so re-run the proof
  (`./nb check ... --series the-mechanics`) and re-stamp before the PR.

## Decision

approve — the article's central claim, figures, and both Siri tracings hold
against the evidence, and every slop, term-rule, reader-address, and citation-label
issue was resolved in place.
