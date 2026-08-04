# Editorial review: the-instruments/training-compute (editor/01)

## Skeptic

Thesis: the headline training-compute (FLOP) figure that regulation now writes
into law is almost never a measurement. It is reconstructed after a run, two
ways, each an estimate with a physical soft spot, and regulation reads a number
that honestly sizes a run backward into a verdict on how capable or dangerous a
model is.

The load-bearing claims and how each held:

1. **GPT-4 sits above the EU line on an undisclosed number (headline).** ~2.1×10^25
   > 10^25, and the figure is Epoch's third-party estimate from inferred
   hardware and duration, never published by OpenAI. Confirmed against the
   Epoch page (s3), which resolves and states the estimate and its provenance
   ("estimated using training hardware and training duration"). The headline's
   own "on a number OpenAI never disclosed" clause carries the caveat, so
   stating "sits above" as fact is honest, not overclaimed.

2. **The number is almost never measured; disclosure is the exception.** Handled
   exactly as the commission and coach asked: carried as thesis, then refined,
   not contradicted. Llama 3.1 405B is named as the disclosure counter-case, and
   even its disclosed 3.8×10^25 is framed as Meta's own 6ND-and-hardware
   accounting rather than a metered quantity. No overstatement.

3. **The two estimation methods and their numbers.** Hardware method (chips ×
   peak FLOP/s × wall-clock × MFU) and analytic 6ND both match the evidence and
   Epoch (s4, resolves; confirms the 0.3 LLM default and the "factor of 1.7"
   agreement). MFU figures check out: PaLM 46.2% (s5), Llama 38–43% (s8, evidence
   Table 4: 43/41/38), Epoch default 30%, older-model 10% (s9). The 6ND
   derivation (2 for the forward pass, ×3 for forward-plus-backward) matches
   Kaplan (s6) and the Chinchilla cross-check (s7).

4. **Regulatory thresholds, stated exactly.** EU 10^25 as a rebuttable
   presumption under Art. 51(2), with Recital 111's "one of the relevant
   approximations" quoted from inside the law; EO 14110's 10^26 (AI), 10^23
   (biological), and 10^20/s (cluster) triggers; revocation on 2025-01-20 by EO
   14148. Every figure matches the evidence record and the owning texts. EO
   14148 revocation confirmed live at s10 (item (ggg)).

5. **Llama 3.1 405B worked case.** 6 × 405e9 × 15.6e12 = 3.79×10^25, rounding to
   the disclosed 3.8×10^25; above the EU line (~3.8×), below the EO line (~0.38×).
   Recomputed independently and correct.

6. **The forward/backward flip.** Built as two plain positive statements ("the
   number does honest work" reading forward; "regulation reads it the other way"
   reading backward), each tied to a named user (Meta's disclosure, Epoch's
   catalog, the EU/EO thresholds). No invented strawman: the backward reading is
   one the cited laws actually make. This is the voice guide's spine, executed
   without "not X but Y" scaffolding.

No claim broke. The contested question (Hooker against, Heim & Koessler for) is
steelmanned on both sides, with the law's own hedge shown from inside the text —
exactly the standard's requirement for a contested figure. s11 and s12 resolve
and confirm the article's quotations verbatim ("an imperfect proxy for risk";
"shortsighted and likely to fail to mitigate risk").

Display text, descriptor by descriptor: headline actors (GPT-4, EU, OpenAI) and
the "above the line / never disclosed" claim all hold; the dek's world-claims
(regulators write it into law, almost no lab measures it, reconstructed two ways)
all hold and none grade the article's own method; the four section subheads are
each a true step in the piece's own nouns. Every named figure, date, and quantity
in the stat strip, table, and note block traces to its owning primary.

`data-nb-kind` audit: 9 primary / 3 secondary, all correctly labelled. Epoch's
"models over 1e25" page (s3) is correctly secondary (Epoch reporting on models it
did not build); Epoch's own methodology writeup (s4) is correctly primary (Epoch
owns its estimation procedure). Hooker and Heim & Koessler are secondary
commentary on the law. Source floor met (12; ≥4 primary, ≥1 secondary).

Citation link check: all 12 hrefs opened as printed. s1 (EUR-Lex) returns the
documented bot-gate empty body and is not failed, per the brief; the EU wording
was verified by the researcher against a verbatim reproduction. s2 (govinfo EO
PDF) returns HTTP 200, a 437KB Federal Register PDF — resolves cleanly. s3–s12
resolve to the exact cited sources. The five in-prose library links
(scaling-laws-kaplan, chinchilla, cost-per-token, energy-per-query,
tokens-per-second) all exist in the checkout.

## Cut

I ran the earns-its-place test sentence by sentence and found the piece already
tight; no pure deletion improves it without cost. Cases I weighed and rejected:

- The metering metaphor recurs three times ("not a reading off a meter" in the
  opener, "not a reading from an instrument" in the body, "not a metered
  quantity" in the takeaway). The coach warns against re-caveating. But this is
  one sustained thesis image, not a repeated structure carrying different cargo,
  and each instance sits at a load-bearing spot (opener setup, body landing,
  takeaway payoff). Cutting any removes a thesis statement, not filler. Kept.
- The loose-joints closer ("Disclosure is the exception, and a disclosed figure
  is still an estimate. It is just the lab's own.") reads slightly redundant with
  the sentence before it. Every clean deletion either strips the commission's
  required nuance ("disclosure is the exception"), the thesis ("still an
  estimate"), or a sharp section ending, or breaks a pronoun antecedent. The
  passage resists cutting because it earns its place. Kept.
- "The odd thing about these lines is that..." is a mild setup, not an unearned
  punchline: the argument proves the oddity in the next sentence (GPT-4). Within
  the plain register. Kept.

Worst tell considered: "loose joint" in the dek echoes the coach's directive
language. It is not leakage — the writer adopted it as the article's organizing
image (the body section is titled "The loose joints"), which is authored
structure, not a copied instruction, planning label, or selection rule. No
"fulfilled the assignment" claims, no planning vocabulary, no copied brief
phrasing anywhere in the authored text. The "Why this matters" opener's "This
lesson shows..." is template-licensed bookend furniture, not self-narration.

Formula check: dek and all four headings clear the coach's do-not-reuse list —
no "swings N-fold," no "X and Y both true," no "N stacked assumptions," no
"depending only on," no "A X is not a Y," no comma-and heading cadence. The dek's
colon introduces a payoff whose lead-in clause stands on its own (valid
punctuation), and it supplies who/what without restating the headline's
GPT-4-specific claim. Grammar and punctuation are clean throughout; the piece
notably avoids the em-dash reflex. Furniture (math figure, MFU table, stat strip,
Recital 111 note) each carries a distinct purpose — the table makes "a single
fraction moves the whole answer" concrete, the stat strip is the visual heart of
the two models straddling one line — and the piece does not read as a stack of
blocks.

No direct edits made.

## Reader

Read straight through, the piece gives what no single source does: the
recognition that the very number a lab produces to report run size is what
regulation reads backward as a capability-and-danger verdict, dramatized by one
disclosed frontier model (Llama, Meta's own accounting) and one estimate-only
model (GPT-4, Epoch's ~2.1×10^25) straddling the same EU line, so the frontier is
being drawn on markings that are mostly inferred. The draft-handoff's
original-work sentence claims exactly this synthesis, and the article delivers
it; both answers survive. The prose sits closer to the voice-guide exemplars
(Harford's grant-then-complicate, Nuzzo's "cannot work backwards") than to a
median AI summary — it commits to specific numbers, grants the estimate its
honest strength before showing its limit, and lands the forward/backward spine
in the takeaway rather than hedging. The headline, reread as the largest claim,
is the sharpest true instance of the thesis and is defended in the body.

## Edits

None. No pure deletion improves the piece without removing required nuance, the
thesis, or a section ending; the article is clean on all three reads.

## Required work

None. No publication-blocking work remains.

## Decision

approve — every regulatory and technical number verifies against the owning
primaries, all citations resolve, the sourcing labels are correct, the voice and
formula standards are met, and the piece delivers genuine synthesis beyond its
sources. I made no direct edits, so the counts are unchanged and the writer's
proof (BLOCK 0, PUBLISHABLE, 2186 words, 12 sources) stands; the orchestrator can
run `nb stamp` + `nb check` as a final gate before delivery.
