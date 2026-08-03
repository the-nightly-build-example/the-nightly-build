# review-brief: the-evidence/alphafold (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/writer/01/brief.md — exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/writing-coach/01/voice-guide.md
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/researcher/01/evidence.md
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/writer/01/draft-handoff.md
- Article: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/library/the-evidence/alphafold.html
- Template context dir: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/editor/01/editorial-review.md

Recent-pattern notes (this series, break formulas): the-evidence overuses the
"the famous paper never did X" reveal headline (attention "never trained a
language model," GPT-4 "declares no further details," AlphaGo "never mentions
Lee Sedol," the bitter lesson "zero citations") and comma-triad / semicolon-
reversal deks. Check headline, dek, headings against these.

This round's focus:
- Verify no number the evidence did not confirm firsthand appears. In
  particular the ~170,000 PDB training figure must NOT be present; training
  scale should use only the verified ~100,000 experimentally-solved and
  ~350,000 self-distillation figures. The hard accuracy claim (0.96 A r.m.s.d.95
  vs 2.8 A) is paper-owned; the 92.4 GDT median must be attributed to DeepMind's
  CASP14 announcement, not the Nature paper's body. Check each attribution.
- The angle's honesty test: the piece must separate the one measured result
  (single-chain structure-prediction accuracy on CASP14) from the three
  unearned credits (function, folding dynamics, replacing experimental biology).
  The overclaim must not be a strawman — the "solved" framing appears in
  DeepMind's own blog and the Nobel explanatory prose while the formal citation
  stays narrow. Confirm Terwilliger 2024 is used as the independent bound.
- Zero-biology reader: protein, amino-acid sequence, 3D structure, structure
  prediction, CASP, GDT_TS, pLDDT each defined in plain words at first use.
- One chart (chart-1.py + PNG) built from the four verified r.m.s.d.95 figures.
  Inspect its committed provenance, recompute against the evidence and the cited
  primary, and read the image as a reader (labels, scale, honesty). Request
  corrections; do not edit the asset yourself.
- The writer intentionally left ONE W-SENTENCE-DENSITY warning on the body's
  closing sentence: it is the voice guide's licensed two-half verdict (the
  does/moves/replace triad), which must be a single "and"-juxtaposed sentence.
  Protect that licensed form if it clears the voice guide's bar; do not force a
  split that would break the license. Judge it on the bar, not the warning.
- Byline gate: the article's <div class="nb-byline"> must show the real read
  time (e.g. "N min read" placeholder replaced to match nb-meta reading_minutes),
  not the literal "N min read". If it still reads "N min read", flag it as a
  writer markup fix.
