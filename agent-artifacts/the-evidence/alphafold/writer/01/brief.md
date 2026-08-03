# writer brief: the-evidence/alphafold (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/commission.md — assignment, angle, boundaries
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/writing-coach/01/voice-guide.md — register and licensed forms
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/researcher/01/evidence.md — the complete claim set; use its Numbers exactly
- Article to edit: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/library/the-evidence/alphafold.html
- Template context dir: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/.nb-context/

Output (draft handoff): /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/writer/01/draft-handoff.md

Proof: run from repo root /home/user/the-nightly-build using the checkout's nb.
  Iterate: ./nb check --series the-evidence .nb-work/the-evidence/alphafold/library/the-evidence/alphafold.html --library /tmp/claude-0/-home-user-the-nightly-build/6cb4c49e-7d08-5720-bd17-76474fa73d16/scratchpad/library-checkout --no-check-links
  Final (BLOCK: 0, links included): same without --no-check-links. Run ./nb stamp before the final check.
Note the-evidence source floor is 6 (>=3 primary, >=1 secondary), lower than the other desks.

This round's focus (decisions the inputs do not fully carry):
- Do NOT print the "~170,000 PDB training structures" figure: the researcher
  could not verify it firsthand (it is in the Supplementary Information). Either
  omit it, or use the verified figures instead — the abstract's ~100,000 unique
  experimentally-determined proteins and the ~350,000 self-distillation set.
  Never state a number the evidence record did not verify.
- The hard, paper-owned accuracy number you can state flatly is 0.96 Å r.m.s.d.95
  vs 2.8 Å for the next-best method. The median 92.4 GDT (0–100 scale) is owned
  by DeepMind's CASP14 announcement and the CASP14 assessment, NOT the Nature
  paper's readable body — attribute it to the owner the evidence records.
- The angle is well supported and sharpened by a real tension: the "solved"
  framing is not only loose press — DeepMind's own blog calls it "a solution to
  a 50-year-old grand challenge" and the Nobel body's explanatory prose says
  they "solve" the problem, while the FORMAL Nobel citation stays narrow ("for
  protein structure prediction"). Use that tension; do not strawman the
  overclaim. Terwilliger et al. 2024 is the independent bound: even
  top-confidence predictions carry ~2x experimental error and are hypotheses,
  not experimental structures.
- Teach for a reader with zero biology: define protein, amino-acid sequence, 3D
  structure, what "structure prediction" is, CASP, GDT_TS, and pLDDT — each in
  plain words at first use, by consequence (voice guide), e.g. what a ~90 GDT or
  a low pLDDT lets the reader conclude.
- Keep the separation clean: what the paper demonstrated (a measured jump in
  single-chain structure-prediction accuracy on CASP14) vs the three things it
  is credited with but did not show (predicting function, folding dynamics,
  replacing experimental structural biology).
- Headline/dek: do NOT use the series' "the paper never did X" reveal mold or
  the semicolon-reversal / comma-triad dek. The voice guide licenses one
  two-half verdict sentence — use it for what CASP14 showed vs what AlphaFold is
  credited with beyond it.
- nb-meta: date 2026-08-03, harness, writer model you ran as; tags array empty.
