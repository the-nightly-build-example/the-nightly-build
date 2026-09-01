# writer brief: what-could-go-wrong/gradient-hacking (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
- ../../commission.md — angle, course boundary, and the recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available; use its Numbers section exactly
- ../../../../library/what-could-go-wrong/gradient-hacking.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract, runtime assets, and furniture catalogs

Output: ./draft-handoff.md

Proof: nb check .nb-work/what-could-go-wrong/gradient-hacking/library/what-could-go-wrong/gradient-hacking.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/c80f7a7e-0800-5248-bdf5-999f03f80465/scratchpad/library-checkout

Run the proof from /home/user/the-nightly-build with the checkout's ./nb; iterate
with --no-check-links, then finish on the full command until BLOCK: 0.

Follow the evidence on the shape of the disagreement, which the record sharpens
past the commission's two poles. No named skeptic claims gradient hacking is
impossible in practice: Millidge argues it fails only against an idealized
gradient descent and then lists four ways real training departs from that ideal;
Jorgensen refutes only the naive fail-hard construction; Hubinger, the
originator, proposes a defense rather than declaring alignment hopeless. So write
the "dismissal" pole as a reading, not as any skeptic's stated position. The
sharpest real disagreement to land: Hubinger's own worked example (check the
objective, fail hard if it changed) is what Jorgensen disproves, while the
general concept survives and hangs on whether real gradient descent's departures
from the ideal are exploitable. Keep the demonstrated-versus-analogy line sharp:
no working system has gradient-hacked, and every adjacent result required a
supplied goal or trigger.
