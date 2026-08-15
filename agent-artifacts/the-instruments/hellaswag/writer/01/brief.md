# writer brief: the-instruments/hellaswag (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/agent-artifacts/the-instruments/hellaswag/editorial-direction.md — house standard, slop standard, headline standard, this paper's voice, the lesson template identity, and the series prompt.
- /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/agent-artifacts/the-instruments/hellaswag/writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages to read for register before drafting.
- /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/agent-artifacts/the-instruments/hellaswag/researcher/01/evidence.md — the complete set of claims available to you. Its Contradictions and Numbers sections govern.
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/library/the-instruments/hellaswag.html
- Effective template contract and furniture catalogs under: /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/agent-artifacts/the-instruments/hellaswag/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-instruments/hellaswag/library/the-instruments/hellaswag.html --series the-instruments --library /home/user/library-checkout
       (iterate with --no-check-links; run `./nb stamp <article>` before the final check; the final proof must pass with links included, BLOCK: 0)

Orchestrator rulings for this round (these resolve open decisions; follow them):
- Do not say models climbed past or surpassed the human score. The best verified
  current figure, GPT-4 at 95.3% (10-shot), sits just below the 95.6% human
  baseline. The defensible, sourced claim is that the top models are level with
  people and clustered within about a point, so the test no longer separates them.
  Say "level with" or "indistinguishable," never "beat the human number."
- State the item count as the released dataset's 59,950 rows (39,905 train /
  10,042 validation / 10,003 test), and note the paper advertised a rounded "70k."
  Give the checkable figure, not the round number alone.
- The saturation case is carried by "indistinguishable from human, gaps within a
  point are noise," not by "past human." Keep the misleading-case concrete: a
  current high HellaSwag figure still cited as commonsense ability after the test
  saturated, and what that costs a reader who reads two close scores as a ranking.

Recent habits to break (from the commission's read of the library):
- Do not open the "Why this matters" bookend with the house "by the end you will
  be able to" formula. Find this test's own reason to read.
- Recent the-instruments pieces close the "what the number cannot support" section
  under headings like "What a high score would not prove" and "The dimensions
  overlap cannot see." Write a fresh heading and close in HellaSwag's own nouns.
- Vary the headline from the recent comma-continuation molds. A worked item or a
  saturation figure can lead if it is the surprise, stated plainly.
