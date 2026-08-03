# Editorial review: the-evidence/alphafold (editor/01)

## Skeptic

Thesis: AlphaFold precisely measured one thing on a blind test — how closely a
predicted static shape of a single protein chain matches the lab-solved one —
and that single measured result is narrower than the "AI solved biology"
shorthand stacked on top of it. The piece stands on four load-bearing claims:
(1) the formal Nobel citation is narrow ("for protein structure prediction")
while DeepMind's and the Nobel body's explanatory prose say "solve"; (2) the
CASP14 accuracy was a large, independently scored jump; (3) three popular
credits — function, folding dynamics, replacing the wet lab — were never tested;
(4) an independent group (Terwilliger) bounds the last one.

Each claim held under pushing.

- The overclaim is not a strawman. The article sources the "solved" framing to
  DeepMind's own blog title and the Nobel explanatory line (s1, s2), then sets
  the narrow formal citation beside it (s1). This matches the evidence record's
  central contradiction. The tension is real, not invented.
- The hard accuracy number is correctly attributed. 0.96 Å r.m.s.d.95 vs 2.8 Å
  (backbone) and 1.5 vs 3.5 (all-atom) carry #s4 (Jumper paper) — paper-owned, as
  required. 92.4 GDT and the Moult "~90 ≈ experiment" convention carry #s2
  (DeepMind's CASP14 blog), NOT the Nature body — the exact ownership the brief
  demanded. I confirmed both figures firsthand on the DeepMind blog and confirmed
  244.02 vs 90.82 on the live CASP14 Z-score table (#s5, group 427 vs 473).
- The forbidden ~170,000 PDB figure does not appear (grep clean). Training scale
  uses only the verified ~100,000 experimentally-solved and ~350,000
  self-distillation figures. 58% / 36% / 17% / 98.5% and the derived "roughly
  42%" (100 − 58) carry #s6 (human-proteome paper); arithmetic checks. MSA depth
  "< ~30 sequences" carries #s4. Terwilliger's 0.6 Å median and ~10% > 2 Å carry
  #s7. Every number traces to its owning primary.
- Display text: headline names the actor and a defended finding; the dek states
  who/what and the blind-test margin without restating the headline. Subheads are
  argument steps in the piece's own nouns, none a scaffolding slot. No named
  person's title or affiliation is misstated (Hassabis/Jumper, Google DeepMind;
  Moult as CASP chair).
- data-nb-kind audit: s3 (Callaway) correctly secondary; the seven primaries are
  each the document that owns its claim, including the independent checks (CASP
  table s5, Terwilliger s7) that keep the dominance and the bound from resting on
  DeepMind reporting on itself. Source floor (>=6, >=3 primary, >=1 secondary)
  is cleared with 7 primary + 1 secondary.
- Every citation href lands on its source. CASP, both DeepMind blogs, the
  AlphaFold DB, Quanta and Tech Review resolve directly; the four Nature links
  (s3/s4/s6/s7) return Nature's standard 303 cookie handshake to idp.nature.com
  and back to the same canonical article URL (host gating, correct address);
  Nobel (s1) is host bot-gated (403 to fetchers, resolves in a browser). No href
  substitutes a text endpoint for the source page.

No claim retired; nothing routed to the researcher.

## Cut

The piece is tight; it survives the earns-its-place test with little to remove.
Every body sentence carries a fact, a definition-by-consequence, or the licensed
pivot. I found no prompt leakage: the learning-objective line in "Why this
matters" and the "AI solved biology" framing are template-licensed furniture and
the real popular shorthand, not copied instructions. Punctuation is plain
throughout; the one colon (takeaway) introduces its question correctly, and there
is no semicolon chain or em-dash reflex.

The closing two-half verdict ("On CASP14, AlphaFold matched the accuracy of a
laboratory ... three separate questions the test never scored") is the article's
one licensed density warning. Judged on the voice guide's bar, not the warning:
it lands at the exact pivot the commission's separation names, both halves are
cited earlier (CASP14 accuracy in the blind-test section; the three unshown
claims in the table and the Terwilliger paragraph), and it uses a flat "and"
juxtaposition with no "but"/"yet"/semicolon carrying the turn. It clears the bar.
Protected as one sentence; splitting it would break the license.

Worst tell available for cutting: the transitional "Everything above is one
measurement" leans on a mild back-reference to the document, but it points at the
measurement's content rather than narrating the newsroom, and reads as ordinary
glue; not worth a cut that risks the voice. No repeated shape across
headings/deks/closers — the piece steers clear of the series' "never did X"
reveal mold and the comma-triad / semicolon deks the pattern notes flag.

No direct cuts were needed, so the declared counts stay honest and no re-stamp
was required.

## Reader

Read straight through as a smart reader with no biology, the piece delivers what
no single source gives: the one measured CASP14 result cleanly separated from the
three things AlphaFold is credited with but never tested, taught from protein up
(protein, amino-acid sequence, folded 3D shape, structure prediction, CASP, GDT,
pLDDT each defined in plain words at first use, GDT and pLDDT by consequence), and
bounded by an independent 2024 evaluation. That is exactly the original-work
sentence in the handoff, and it survives. The prose sits with the voice-guide
exemplars — sourced hedges inside the sentence, thresholds pre-converted to their
judgment, plain declaratives — not with a median summary. The headline reads as
the piece's largest defended claim.

## Chart (Fig. 1)

chart-1.py plots four values: AlphaFold 0.96 / 1.5, next-best 2.8 / 3.5, y-axis
"Median error (Å r.m.s.d.95)". Recomputed against the evidence Numbers and the
cited primary (#s4, Jumper abstract + opening Main): all four match exactly, and
both series are the same r.m.s.d.95 statistic in the same unit, so sharing one
axis is honest. Read as a reader: linear scale anchored at 0 (no truncation),
grouped bars, clear legend, categories "Backbone (Cα)" / "All atoms", caption
"shorter is closer to the experimental structure" is a factual label cited to the
owning paper. The chart is honest and correctly provenanced. No correction
requested.

## Edits

None. The article required no surgical cut or prose fix.

## Required work

- writer — Byline markup fix: `<div class="nb-byline">` still prints the literal
  placeholder `<span>N min read</span>`. nb-meta reading_minutes is 7 (1,710
  words), so it must read "7 min read". The deterministic proof does not catch
  this; it is the brief's byline gate and is publication-blocking.

Optional (not blocking, writer's call): the dek tail "a margin worth
understanding before the Nobel-season shorthand runs past it" leans faintly on
"worth understanding"; it still makes a world claim, so it clears, but a tighter
verb there would remove the last trace of reader-instruction.

## Decision

revise — the article is clean on content, sourcing, numbers, attributions,
citations, and the chart, but the byline still shows the literal "N min read"
placeholder instead of "7 min read", a writer markup fix the brief gates on.
