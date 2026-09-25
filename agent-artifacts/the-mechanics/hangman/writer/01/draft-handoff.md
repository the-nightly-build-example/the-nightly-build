# Draft handoff: the-mechanics/hangman (writer 01)

## Original-work sentence

The evidence proves separately that a public-only agent cannot stay consistent
with an undetermined secret and that models measurably contradict themselves;
this article does the thing the sources do not, reading the observed "cheating"
as the visible signature of a system with no place to store a commitment, and
separating performing a commitment from holding one so the reader can see there
was never a secret to lie about, only a word that was never written anywhere.

## Proof

`./nb stamp` then `./nb check ... --series the-mechanics --repo $(pwd)`:

- `--no-check-links`: BLOCK: 0, WARN: 0.
- with links: BLOCK: 0, WARN: 0.

words 1956 (band 1200-2200), sources 10 (8 primary, 2 secondary; series minimum
is 8 sources, >=4 primary, >=1 secondary). No warnings left standing on purpose.

Cleared during iteration: a W-CITE-ORDER (renumbered by reordering the
orientation and exception citations into first-appearance order) and seven
W-SENTENCE-DENSITY warnings (split the long sentences rather than resyntaxing
them).

## Scope and precision held to the brief

- The clean "no hidden state" claim is scoped to a plain chat with the word
  withheld: no private memory that survives from one turn to the next, so the
  withheld word is written nowhere and does not exist. It is never stated as "no
  state at all"; the KV cache is named as per-request working state (source 8).
- The exception is stated exactly: within one response a reasoning model or a
  scratchpad carries the commitment in generated tokens (sources 6, 7), and
  product-level memory or tools can persist it as inspectable written text
  (source 9). Those within-response tokens are discarded between turns in
  standard chat (source 1), so whether state survives a turn is marked as a
  product choice, not settled architecture.
- conversation-memory and autoregressive-generation are linked in prose (not as
  numbered sources) and built past: the point is commitment, not recall. The
  resend is cited, not re-taught.
- The transcript is an explicitly labelled illustrative reconstruction ("An
  illustrative round"), introduced as "reconstructed... not a saved log," and it
  is consistent with the measured failure modes (over-confirmation / affirming a
  wrong letter, then a reveal that breaks an earlier clue). It carries no
  citation and is not presented as captured evidence.
- Measured figures used exactly as the record gives them: self-consistency
  roughly 2-26% for vanilla vs 56-100% with an explicit private-working-memory
  workflow (source 1, Table 1, reported as ranges); GPT-4o self-contradicted in
  173 of 200 games and GPT-4o mini in all 200 (source 2, Table 4).

## Open questions

None blocking. Two things the orchestrator should be aware of, both already
flagged in the researcher's Limits and handled in-draft:

1. No openable, reputable consumer chat transcript of the answerer-withholding
   failure was verified (the closest write-ups were bot-blocked, and the
   openable ones show the guesser side). The draft therefore uses a labelled
   illustrative reconstruction plus the papers' measured behaviour, rather than
   an invented "captured" transcript. If an openable answerer-side transcript is
   wanted as a source asset, that is new evidence and would come from the
   researcher.
2. The self-consistency numbers are used only as the ranges the record supplies.
   If the editor wants a single per-cell figure to carry weight, it should be
   confirmed against Table 1 first (researcher's note).
