# writer brief: what-could-go-wrong/takeoff-speeds (01)

Inputs (under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars.
- `researcher/01/evidence.md` — the complete claim set. Draft only from it.
- Article to edit: `.nb-work/what-could-go-wrong/takeoff-speeds/library/what-could-go-wrong/takeoff-speeds.html` (initialized from the lesson template).
- Template context: `.nb-work/what-could-go-wrong/takeoff-speeds/.nb-context/`.

Output: `.nb-work/what-could-go-wrong/takeoff-speeds/agent-artifacts/what-could-go-wrong/takeoff-speeds/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/what-could-go-wrong/takeoff-speeds/library/what-could-go-wrong/takeoff-speeds.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/4555dd06-1325-5643-8ae1-70035fc82956/scratchpad/library-checkout`
(Use `--no-check-links` while iterating; run the full command, links included, until `BLOCK: 0`. Run `nb stamp` before the final check.)

Two hard constraints from the evidence record:
- Several fast-case items (Yudkowsky, Hanson, the AI-2027 material, the MIRI transcript) are marked `Reported` in the record because they came through page-summarizing fetches. Do not set any of them inside quotation marks unless you reopen the source and confirm the exact words. Paraphrase and cite otherwise. The same applies to Bostrom's moderate/fast takeoff definitions: substance is confirmed, verbatim wording is not, so paraphrase them.
- The honest hinge the piece must hold: the METR time-horizon trend is the empirical fuel for both sides — read straight it grounds continuity, extrapolated it grounds the fast scenario, and the observed data has not resolved the argument. And continuous does not mean safe: Christiano's own essay argues a slow takeoff may be harder to govern. Do not let the piece slide into treating continuity as reassurance.

Angle and boundaries: steelman the fast case at full strength first, then test it against observed systems, drawing the sharp line between shown (scaling continuity; METR's measured six-year trend) and analogy/projection (evolution, AlphaGo, recursive self-improvement in systems that do not exist). Bring it to the present with who argues each side and what they want. This piece is about speed and continuity of takeoff, not the self-improvement mechanism (link what-could-go-wrong/intelligence-explosion) and not capabilities outrunning alignment (link what-could-go-wrong/sharp-left-turn). Link scaling-laws-kaplan and chinchilla rather than re-teaching them. Name no company as an authority.

Recent what-could-go-wrong habit not to inherit: recent pieces close on the move "the measured gap is small and the scary version is still an analogy/projection" (sharp-left-turn, situational-awareness, cot-monitorability, intelligence-explosion). This piece must make the shown-versus-projected distinction, so make it in takeoff's own particulars and do not reuse that closing sentence shape.

Original work: name in one sentence, in draft-handoff.md, what this article does to the evidence that the evidence does not do itself.
