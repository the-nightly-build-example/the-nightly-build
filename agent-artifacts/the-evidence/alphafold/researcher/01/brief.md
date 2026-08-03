# researcher brief: the-evidence/alphafold (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/commission.md — assignment, angle, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-evidence/alphafold/agent-artifacts/the-evidence/alphafold/researcher/01/evidence.md

Source floor (exclusive of nothing; this is the minimum): >= 6 sources, >= 3
primary, >= 1 secondary. Read the primary documents themselves, not coverage.

Questions the evidence must answer:
1. Exactly what the 2021 Nature paper (Jumper et al., "Highly accurate protein
   structure prediction with AlphaFold") reported: the CASP14 result in numbers
   — median GDT_TS for AlphaFold vs the field, what GDT_TS is and its 0–100
   scale, how many CASP14 targets, backbone vs all-atom accuracy (the ~0.96 Å
   RMSD_95 figure if you can source it). Get the figures from the paper/CASP,
   not press.
2. What the model was trained on and its scale: ~170,000 PDB structures, use of
   MSAs and templates, the Evoformer + structure module at a plain-word level
   (no code, no equations beyond what a lesson can carry). What pLDDT is and
   what a low pLDDT region means.
3. The companion database paper (Tunyasuvunakool et al. 2021) and the size of
   the AlphaFold DB (hundreds of thousands → 200M+ predictions later). Date the
   200M figure to its announcement.
4. The honest limits stated by the authors or shown by independent work: single
   chains vs complexes (AlphaFold-Multimer), static structure vs dynamics and
   function, low accuracy for some disordered/orphan proteins, that a prediction
   is a hypothesis not an experimental structure. Find at least one independent
   source that bounds or corrects a specific overclaim.
5. The present-day usage to test: the 2024 Nobel Prize in Chemistry (who shared
   it, for what, exact citation), and concrete claims in circulation that AI
   "solved" protein folding / made structural biology obsolete. Contrast the
   claim with what the paper measured.

Contradictions to hunt: places where popular usage ("solved biology,"
"predicts function") conflicts with the paper's own scope. Where CASP
organizers' framing differs from DeepMind's. Record every figure with owner,
scope, and period. Note any source asset (e.g. the CASP14 accuracy figure, a
pLDDT-colored structure) that could carry the argument better than prose.
