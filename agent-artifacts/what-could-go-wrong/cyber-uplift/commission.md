# Commission: what-could-go-wrong/cyber-uplift

## Authorized work
Scheduled duty for 2026-08-04 returned `what-could-go-wrong` as an open section.
This commission fills it with one lesson on one risk argument. One article.

## The argument
Advanced AI could give attackers a decisive advantage in offensive cyber
operations: discovering vulnerabilities, writing exploits, and running
intrusions at a scale and speed no human team matches, collapsing the cost of
attack faster than defense can adapt.

## Angle
Follow the desk method exactly: open the argument at full strength with its
originators; test it against what real systems have actually been shown to do,
drawing a sharp line between demonstrated and conjectured; then bring it to the
present and name where confidence outruns proof — in both directions. The
organizing move: split the uplift argument into **three claims with different
evidential status** —
1. AI finds real, novel vulnerabilities (shown),
2. AI runs end-to-end autonomous intrusions against hardened, novel targets at
   scale (not shown; evals cap out below expert real-world tasks),
3. this yields a decisive *attacker* advantage (unshown and contested, because
   the same capability uplifts defenders) —
and show that today's strongest evidence supports (1), gestures at (2), and says
little about (3). Name no company as an authority. Leave the reader to decide
how worried to be.

## What the writer must establish (verify against primary documents)
- The argument at strength: who first made the modern version and what they had
  seen (the 2018 "Malicious Use of AI" report is the early form; lab safety
  teams carry the LLM-era version). Steelman it before any rebuttal.
- Shown, with specifics: an AI system finding a real, previously-unknown,
  exploitable vulnerability (e.g., the Google "Big Sleep" SQLite finding, late
  2024 — verify exactly what, when, and whether exploitable); the DARPA AI Cyber
  Challenge results (find-and-patch at scale on real open-source code); frontier
  model cyber/CTF eval results from lab system cards and the academic
  benchmarks. Report pass rates honestly.
- Not shown / conjectured: a fully autonomous end-to-end intrusion of a hardened
  novel target at scale; a decisive strategic edge. Evals show models help most
  where a skilled human already could and stumble on hard, novel, multi-step
  operations. The novice-vs-expert uplift distinction is contested — report the
  disagreement, do not resolve it by fiat.
- Present tense: who makes the argument today (lab safety teams, national cyber
  agencies, RAND-type analysts) and what they want done; the most recent
  evidence, including that the same tools uplift defenders (automated patching,
  defensive vuln discovery). Name the gap on both sides: doom ("AI breaks all
  defense") and dismissal ("just a chatbot").

## Boundaries
- Work from original documents — the reports, the lab evals, the challenge
  results, the benchmark papers — never the commentary about them. Where a
  number comes from a lab evaluating its own model, say so and treat it as an
  interested party.
- This is not a how-to. Teach how the field reasons about the capability and its
  evidence; include no operational detail that functions as attack instruction.
  Discuss capabilities at the level the public evals and reports discuss them.
- Contradictions are the point of this desk. The evidence record's Contradictions
  section must be full: doom claims, dismissal claims, and the novice/expert
  uplift dispute all belong there.

## Structure note (anti-repetition)
The library already holds `what-could-go-wrong/bioweapon-uplift`, which is built
around a single red-team null result. Do **not** mirror that shape. Lead this
piece with the concrete positive demonstrations (the real vulnerabilities found)
and let the three-claims split carry the structure, so the two "uplift" lessons
read as different arguments, not one template run twice.

## Sources plan
Series policy: min 8 sources, at least 4 primary and at least 1 secondary.
Target primaries: Brundage et al. 2018 (Malicious Use of AI); the Google "Big
Sleep"/Project Zero writeup; the DARPA AIxCC official results; at least one lab
system card / dangerous-capability eval reporting cyber results (e.g., a Claude
or GPT/o-series system card, or Phuong et al. 2024 on evaluating frontier models
for dangerous capabilities); an academic exploit/CTF benchmark (e.g., CyBench, or
the Fang et al. 2024 autonomous-exploit work *and* its critiques); a national
cyber-agency assessment (e.g., the UK NCSC assessment of AI and the cyber
threat). At least one secondary for context (reporting on AIxCC finals or the
HackerOne leaderboard result). Researcher verifies every capability claim and
pass rate against the owning document and flags interested-party sourcing.

## Neighboring articles this run (avoid overlap)
Tonight also publishes `the-evidence/alexnet`, `the-instruments/training-compute`,
`the-mechanics/retrieval`, `when-ai-breaks/nh-predict`. Keep clear of the
`bioweapon-uplift` piece's framing as noted above.

## Recent shapes to break
This desk's recent deks lean on the reversal/limit mold ("the model that drives
safety to zero needs a lead nobody has held," "clear the substeps and fail the
loop"). Land the finding without copying that stamped shape. Vary heading
cadence; avoid the comma-and-"and" molds. Coach supplies the do-not-reuse list.

## Production record
- Profile: balanced. Model directive: `capable` for every stage (not required).
  Effort directives: writing-coach low, researcher high, writer medium, editor
  high.
- Actual harness: roles run as isolated subagents on model `claude-opus-4-8`.
  Per-stage effort inherited (not independently settable); recorded as a
  permitted deviation. Writer records the model string in `nb-meta`.
