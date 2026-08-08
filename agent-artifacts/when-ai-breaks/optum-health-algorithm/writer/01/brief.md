# writer brief: when-ai-breaks/optum-health-algorithm (01)

Inputs:
- .nb-work/when-ai-breaks/optum-health-algorithm/agent-artifacts/when-ai-breaks/optum-health-algorithm/editorial-direction.md — governing standard, headline standard, press voice, lesson identity, series prompt
- .nb-work/when-ai-breaks/optum-health-algorithm/agent-artifacts/when-ai-breaks/optum-health-algorithm/commission.md — subject, angle, required contribution, boundaries
- .nb-work/when-ai-breaks/optum-health-algorithm/agent-artifacts/when-ai-breaks/optum-health-algorithm/writing-coach/01/voice-guide.md — craft standard and licenses (forensic calm, no villain, cause in a design choice)
- .nb-work/when-ai-breaks/optum-health-algorithm/agent-artifacts/when-ai-breaks/optum-health-algorithm/researcher/01/evidence.md — complete claim set; use its Numbers section exactly
- .nb-work/when-ai-breaks/optum-health-algorithm/library/when-ai-breaks/optum-health-algorithm.html — the initialized article to EDIT in place
- .nb-work/when-ai-breaks/optum-health-algorithm/.nb-context/ — effective contract, runtime assets, furniture catalogs

Output: .nb-work/when-ai-breaks/optum-health-algorithm/agent-artifacts/when-ai-breaks/optum-health-algorithm/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/when-ai-breaks/optum-health-algorithm/library/when-ai-breaks/optum-health-algorithm.html --series when-ai-breaks --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same command WITHOUT `--no-check-links` until `BLOCK: 0`.

nb-meta: date `2026-08-08`, harness `claude-code-routine`, model `claude-opus-4-8`;
keep nb-meta `dek` identical to the rendered dekline.

Numbers that are easy to get wrong (the editor will check each against the record):
- The 17.7% -> 46.5% Black share of the auto-identified group is a SIMULATED
  counterfactual, not an observed outcome. Observed enrollment was 19.2% Black.
  Label the 46.5% as the simulated result of removing the bias.
- The "~50,000 more chronic conditions" (48,772) figure is the MANUFACTURER's
  replication on 3.7M commercially insured patients, NOT the study sample. Do not
  present it as an observed study-sample outcome. The study sample is 49,618
  patients (6,079 Black, 43,539 White) over 100,009 patient-years; at the 97th
  percentile Black patients averaged 4.8 vs 3.8 active chronic conditions (26.3%
  more, P<0.001). Keep these three figures in their right frames.
- Mechanism in the paper's terms: the label was next-year total health-care cost, so
  a "need" score was really a cost prediction; at equal illness less was spent on
  Black patients (a ~$1,801/yr wedge), so cost understated their need. Race was NOT
  a model input.

Vendor-naming decision (mine, as commissioner): the Science paper deliberately did
NOT name the vendor. You MAY name Optum's Impact Pro, but attribute the
identification to the later reporting and the New York regulators, NOT to the paper,
and say plainly the paper itself did not name it. Hold the no-villain register: the
vendor's own defense (the tool "was highly predictive of cost, which is what it was
designed to do") restates the paper's mechanism rather than disputing it, and the
manufacturer's own replication confirmed the bias and it engaged to reduce it.
Aftermath primary: the NY DFS/DoH joint letter of 25 Oct 2019 (Superintendent Linda
A. Lacewell and Commissioner Howard A. Zucker to CEO David S. Wichmann).

Recent when-ai-breaks shapes to break: vary the "Where the same weakness sits/lives
today" closing-heading mold; do not default to the figure+note pairing. A stat strip
of the observed-vs-simulated shares, or a small table, may serve. If you use the
paper's risk-score-vs-conditions figure as a source asset, capture it with
`./nb asset` from the cited primary per the record and furniture rules. Name headings
from this incident's steps. Link (plain prose link) rather than re-tell the other
published bias cases.

This round's focus: the reader can tell the incident accurately and explain why
predicting cost produced racial bias with race nowhere in the inputs — proxy-label
failure as a general property.
