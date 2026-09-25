# researcher brief: what-could-go-wrong/ai-environmental-cost (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md)
Output: ./evidence.md

Work from these inputs. Do not tour the repository. Ask me where something is missing.

Read the primary documents in full, with locators:
- Strubell, Ganesh & McCallum 2019, "Energy and Policy Considerations for Deep
  Learning" (ACL). Record the headline training-carbon figure and exactly what
  it covered (which model, whether it included neural architecture search), and
  the paper's own caveats — this number was widely misquoted, so record what it
  did and did not claim.
- Patterson et al. (Google) 2021 "Carbon Emissions and Large Neural Network
  Training" and/or the 2022 follow-up. Record how grid mix, location, and
  accounting change a training run's carbon by large factors; record a concrete
  figure with its conditions.
- Luccioni, Viguier & Ligozat, BLOOM carbon footprint paper. Record the
  training and (if given) inference footprint and the accounting boundary.
- IEA report on electricity and data centers (a specific dated edition, e.g.
  Electricity 2024 or the 2025 data-centre/energy report). Record the aggregate
  data-center electricity figure and the projection, with the base year and the
  uncertainty range. This is the measured-aggregate anchor.
- de Vries 2023, "The growing energy footprint of artificial intelligence"
  (Joule). Record its projected AI electricity figures and its explicit caveats
  about extrapolation.

Establish the per-unit vs aggregate distinction with numbers on both sides.
Find and document ONE widely-quoted per-query claim (e.g. a water-per-query or
energy-per-query viral figure) and trace how it was derived and why it is weak or
was walked back (reputable reporting or a correction). Record the correction.

Source floor: min 8, >=4 primary, >=1 secondary. Classify each with a reason.
Contradictions: record the dispute between alarmist per-query claims and
dismissive "it's tiny per query" claims, and any efficiency-gain counterpoint
(e.g. improving PUE, more efficient chips), in full. Numbers: training carbon,
per-query estimates, aggregate TWh and projections, water figures — each with
owner, accounting boundary, base year, and scope. Limits: note that aggregate
projections are uncertain and that water/inference disclosure is thin. Source
assets: an IEA data-center electricity chart is a candidate.

Report the path and the most important limit.
