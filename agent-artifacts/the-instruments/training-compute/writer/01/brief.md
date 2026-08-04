# writer brief: the-instruments/training-compute (01)

Inputs:
  ../../commission.md — the measurement, angle, boundaries, sources plan
  ../../editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
  ../../writing-coach/01/voice-guide.md — register, forward/backward spine, licenses, do-not-reuse list
  ../../researcher/01/evidence.md — the complete claim set; use its Numbers and Sources exactly
  ../../../../library/the-instruments/training-compute.html — the initialized article to edit (do not recreate the skeleton)
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs
Output: ./draft-handoff.md
Proof (links included, until BLOCK: 0):
  ./nb check .nb-work/the-instruments/training-compute/library/the-instruments/training-compute.html --series the-instruments --library /home/user/library-checkout

Round focus — use the verified numbers exactly:
- EU AI Act 10^25 FLOP systemic-risk presumption (Art. 51(2), Reg (EU) 2024/1689;
  it is a rebuttable presumption — say so); EO 14110 §4.2(b) thresholds (10^26
  for AI, 10^23 biological, 10^20/s clusters), REVOKED 2025-01-20 by EO 14148 —
  state the current status plainly.
- C = 6ND provenance: Kaplan et al. 2020 (factor 6 = 2 MAC × 3 for the backward
  pass), named and used in Chinchilla (Table A4). MFU ~30–50% (PaLM 46.2%,
  Llama 3 ~38–43%).
- The clean case: Llama 3.1 405B's DISCLOSED 3.8×10^25 FLOP reproduces via 6ND
  and sits above the EU line, below the EO line; GPT-4's ~2.1×10^25 is Epoch's
  ESTIMATE, never disclosed — the estimate-treated-as-fact case.
- Honest refinement: "almost never measured" holds for undisclosed models, but
  Llama 3.1 405B is a real disclosure counter-case — handle as nuance (disclosure
  is the exception, and even a disclosed figure is a 6ND/hardware accounting
  estimate, not a metered quantity), not a contradiction of the thesis.
- Contradictions to weigh in prose: Hooker (a FLOP threshold is a poor risk
  proxy) vs. Heim & Koessler (defensible); note the EU law itself encodes the
  doubt. Record in draft-handoff (for the editor) that the two legal-text URLs
  are bot-gated on automated fetch; the researcher verified via the govinfo PDF
  and a verbatim reproduction, and the canonical URLs resolve in a browser.
Do not turn this into a scaling-laws lesson; link the-evidence/scaling-laws-kaplan
and the-evidence/chinchilla rather than re-arguing compute-optimal training.
